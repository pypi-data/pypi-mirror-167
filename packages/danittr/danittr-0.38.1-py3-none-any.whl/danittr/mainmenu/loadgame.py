"""Facility for loading game on main menu."""

from os import listdir
from types import SimpleNamespace
from os.path import join
from functools import partialmethod

### third-party imports

from pygame import (
    QUIT,
    KEYDOWN,
    K_RETURN,
    K_ESCAPE,
    K_w,
    K_UP,
    K_s,
    K_DOWN,
    MOUSEBUTTONDOWN,
    MOUSEMOTION,
)

from pygame.display import update
from pygame.event import get as get_events
from pygame.image import load as load_image
from pygame.draw import rect as draw_rect
from pygame.mouse import get_pos as get_mouse_pos

### local imports

from ..config import SCREEN, SCREEN_RECT, GAME_REFS, SAVES_DIR, STATE_FILE_NAME

from ..common.math import get_reaching_multiple
from ..common.behaviour import empty_function
from ..common.jsonhandler import load_json
from ..common.wdeque.main import WalkingDeque

from ..appcommon.task import add_task, update_task_manager
from ..appcommon.surf import render_rect
from ..appcommon.style import give_depth_finish
from ..appcommon.autoblit import BlitterSet
from ..appcommon.exception import (
    QuitGameException,
    LevelSwitchException,
    ManagerSwitchException,
)
from ..appcommon.text.main import render_text
from ..appcommon.behaviour.load import load_game

from ..sound import SOUNDS_MAP
from ..palette import CERULEAN, BLACK, WHITE, SKY_COLOR


SLOT_DISTANCE = 110

# XXX
# Now, besides the art, the only thing the mainmenu subpackage
# lacks is mouse style and animation. This would be a fine
# touch.


class LoadGameWidget(object):
    """Widget to help loading new games."""

    def __init__(self, main_menu):
        """Set the instance.

        main_menu
            Reference of mainmenu.main.MainMenu instance.
        """
        self.main_menu = main_menu

        self.thumb = render_rect(640, 360, return_obj=True, coordinates_value=(630, 25))

        self.build_slot_list()

        self.background = render_rect(*SCREEN_RECT.size, color=SKY_COLOR)

        self.set_labels()

        self.error_cooldown_task = SimpleNamespace(finished=True)

    def set_labels(self):
        """Set a labels group to display labels."""
        self.labels = BlitterSet()

        font_size = 28

        text01 = "Please,"
        label01 = render_text(
            text01,
            font_size,
            foreground_color=WHITE,
            padding=0,
            return_obj=True,
            coordinates_value=(25, 25),
        )

        text02 = "select a save:"
        label02 = render_text(
            text02,
            font_size,
            foreground_color=WHITE,
            padding=0,
            return_obj=True,
            coordinates_value=(25, 60),
        )

        self.labels.update([label01, label02])

    def build_slot_list(self):
        """Build each individual slot with info."""
        ### Collect saves information
        saves = []
        for dirname in listdir(SAVES_DIR):
            path = join(SAVES_DIR, dirname, STATE_FILE_NAME)
            last_played = load_json(path)["last_played_datetime"]
            save = SimpleNamespace(dirname=dirname, last_played=last_played)
            saves.append(save)

        ### Sort by last played, generate visual slots
        # pygame don't handle lambdas well, so using this.
        def get_last_played(item):
            """Return last played attribute value."""
            return item.last_played

        saves.sort(key=get_last_played, reverse=True)

        x, y = 200, 25
        slots = []
        for save in saves:
            topleft = (x, y)
            slot = SaveSlot(save.dirname, save.last_played, topleft)
            slots.append(slot)
            y += SLOT_DISTANCE

        ### Create groups of such slots to help manage them
        self.slots_deque = WalkingDeque(slots)
        self.slots = BlitterSet(self.slots_deque)

        ### Define choosen one and rect to highlight it
        self.selected_slot = self.slots_deque[0]
        self.highlight_rect = self.selected_slot.rect
        self.thumb.image = self.selected_slot.thumb

    def control(self):
        """Update widget state based on event_queue."""
        for event in get_events():

            if event.type == QUIT:
                raise QuitGameException

            ### Keyboard

            elif event.type == KEYDOWN:

                if event.key in (K_w, K_UP):
                    self.select_previous()
                elif event.key in (K_s, K_DOWN):
                    self.select_next()
                elif event.key == K_RETURN:
                    self.load_game_from_slot()
                elif event.key == K_ESCAPE:
                    raise ManagerSwitchException(self.main_menu)

            ### Mouse
            elif event.type == MOUSEMOTION:
                self.mouse_motion_routine(event.pos)

            elif event.type == MOUSEBUTTONDOWN:

                if event.button == 1:
                    self.mouse_click_routine(event.pos)
                elif event.button == 4:
                    self.scroll_down()
                elif event.button == 5:
                    self.scroll_up()

    def update(self):
        """Update the task manager."""
        update_task_manager()

    def draw(self):
        """Draw widget objects."""
        SCREEN.blit(self.background, (0, 0))
        self.labels.draw()

        self.slots.draw()
        draw_rect(SCREEN, CERULEAN, self.highlight_rect, 4)

        SCREEN.blit(self.thumb.image, self.thumb.rect)
        update()

    def rotate_selection(self, amount=0, from_mouse=False):
        """Assign selected item after rotating by amount.

        amount
            Integer representing amount of deque rotation.
        from_mouse
            Boolean. If true, scroll check isn't performed,
            since it is expected that the user perform
            the scrolling itself with the mouse wheel.
        """
        self.slots_deque.walk(amount)
        self.selected_slot = self.slots_deque[0]
        self.highlight_rect = self.selected_slot.rect
        self.thumb.image = self.selected_slot.thumb

        if not from_mouse:
            self.check_scrolling()

        SOUNDS_MAP["gui_step"].play()

    select_previous = partialmethod(rotate_selection, -1)
    select_next = partialmethod(rotate_selection, 1)

    def mouse_motion_routine(self, mouse_position):
        """Check if mouse touches any widget and select it.

        mouse_position
            Tuple containing mouse coordinates relative to
            screen topleft and always constrained to it.
        """
        ### Search slot

        for item in self.slots_deque:

            if item.rect.collidepoint(mouse_position):
                touched_item = item
                break

        else:
            touched_item = None

        ### If already selected, get out
        if touched_item == self.selected_slot:
            return

        ### Select slot + admin tasks

        if touched_item:

            for i in range(len(self.slots_deque)):

                if touched_item == self.slots_deque[0]:
                    self.rotate_selection(from_mouse=True)
                    break

                self.slots_deque.walk(1)

    def mouse_click_routine(self, mouse_position):
        """Invoke widget if mouse click over it.

        mouse_position
            Tuple containing mouse coordinates relative to
            screen topleft and always constrained to it.
        """
        ### Search slot

        for item in self.slots_deque:
            if item.rect.collidepoint(mouse_position):
                touched_item = item
                break

        else:
            touched_item = None

        ### Select slot if not already + load slot

        if touched_item:

            if touched_item != self.selected_slot:
                self.mouse_motion_routine(mouse_position)

            self.load_game_from_slot()

    def scroll(self, amount):
        """Scroll slots by amount.

        amount
            Integer representing amount to be added to
            rect.y attribute, which is how scrolling is done.
        """
        ### Refuse to scroll up if first slot is on screen

        if amount > 0:

            first_slot = self.slots_deque.get_mem_value(0)

            if SCREEN_RECT.contains(first_slot.rect):
                self.play_error()
                return

        ### Refuse to scroll down if last slot is on screen

        elif amount < 0:

            last_slot = self.slots_deque.get_mem_value(-1)

            if SCREEN_RECT.contains(last_slot.rect):
                self.play_error()
                return

        ### Otherwise, scroll and check if mouse hovers any
        for slot in self.slots:
            slot.rect.y += amount

        self.mouse_motion_routine(get_mouse_pos())

    scroll_up = partialmethod(scroll, -SLOT_DISTANCE)
    scroll_down = partialmethod(scroll, SLOT_DISTANCE)

    def play_error(self):
        """Time and execute play error appropriately."""
        if self.error_cooldown_task.finished:
            SOUNDS_MAP["error"].play()
            self.error_cooldown_task = add_task(empty_function, 800)

    def check_scrolling(self):
        """Check if current slot needs to be scrolled.

        This is to be sure the selected slot is aways
        on screen.
        """
        ### Store reusable values
        slot_top = self.selected_slot.rect.top
        slot_bottom = self.selected_slot.rect.bottom
        screen_top = SCREEN_RECT.top
        screen_bottom = SCREEN_RECT.bottom

        ### How much scrolling if slot is bellow screen
        if slot_top < screen_top:
            distance = screen_top - slot_top
            to_scroll = get_reaching_multiple(SLOT_DISTANCE, distance)
            self.scroll(to_scroll)

        ### How much scrolling if slot is above screen
        elif slot_bottom > screen_bottom:
            distance = slot_bottom - screen_bottom
            to_scroll = get_reaching_multiple(SLOT_DISTANCE, distance)
            self.scroll(-to_scroll)

    def load_game_from_slot(self):
        """Load the game from slot dirname attribute."""
        SOUNDS_MAP["game_start"].play()

        GAME_REFS.dirname = self.selected_slot.dirname

        level_name = load_game()

        raise LevelSwitchException(level_name)


class SaveSlot:
    """Container representing a save slot."""

    font_size = 28

    # XXX
    # 2018-01-12 10:29:12
    # Include last level/section on the slots blited info
    # And also a screenshot that must be saved on dirname
    # whenever saving the game within the interactive levels.

    def __init__(self, dirname, last_played, topleft):
        """Save slot."""
        self.dirname = dirname
        self.save_name = dirname.replace("save_", "", 1)
        self.last_played = last_played

        surf = render_rect(420, 80)
        self.image = give_depth_finish(surf)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft

        self.blit_details()
        self.load_thumb()

    def blit_details(self):
        """Blit the final details on the image surface."""
        save_name_text = "Name:  {}".format(self.save_name)
        save_name_surf = render_text(
            save_name_text,
            font_size=self.font_size,
            foreground_color=WHITE,
            background_color=BLACK,
            padding=0,
        )

        last_played_text = "Last played:  {}".format(self.last_played)
        last_played_surf = render_text(
            last_played_text,
            font_size=self.font_size,
            foreground_color=WHITE,
            background_color=BLACK,
            padding=0,
        )

        self.image.blit(save_name_surf, (5, 1))
        self.image.blit(last_played_surf, (5, 35))

    def load_thumb(self):
        """Load and store thumb surface.

        Such surface is referenced by other objects to
        blit it in the appropriate location.
        """
        path = join(SAVES_DIR, self.dirname, "thumb.png")

        self.thumb = load_image(path).convert()
