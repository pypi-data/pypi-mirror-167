"""Facility for the main menu class and related tools."""

from os import listdir
from os.path import isdir, join
from collections import deque
from functools import partialmethod


### third-party imports

from pygame import (
    QUIT,
    KEYDOWN,
    K_RETURN,
    K_w,
    K_UP,
    K_s,
    K_DOWN,
    MOUSEBUTTONDOWN,
    MOUSEMOTION,
)

from pygame.display import update
from pygame.event import get as get_events
from pygame.draw import rect as draw_rect


### local imports

from ..logconfig import APP_LOGGER
from ..config import SCREEN, SCREEN_RECT, GAME_REFS, SAVES_DIR, STATE_FILE_NAME

from ..common.jsonhandler import load_json

from ..appcommon.task import update_task_manager
from ..appcommon.surf import render_rect, render_image
from ..appcommon.style import give_depth_finish
from ..appcommon.autoblit import BlitterSet, BasicObject
from ..appcommon.exception import (
    QuitGameException,
    LevelSwitchException,
    ManagerSwitchException,
)
from ..appcommon.text.main import render_text
from ..appcommon.behaviour.load import load_game

from ..font import get_font
from ..sound import SOUNDS_MAP
from ..music import MUSIC_MANAGER
from ..palette import CERULEAN, BLACK, WHITE, SKY_COLOR

from .newgame import NewGameWidget
from .loadgame import LoadGameWidget
from .options.main import OptionsWidget


logger = APP_LOGGER.getChild(__name__)


class MainMenu:
    """A group-like class for a main menu sprites."""

    def __init__(self):
        """Set this instance."""
        ### handle music
        MUSIC_MANAGER.cue("tense")

        ### gather conditions

        save_folder_exists = isdir(SAVES_DIR)
        it_is_not_empty = listdir(SAVES_DIR)

        ### evaluate then

        if save_folder_exists and it_is_not_empty:

            self.widget_names = [
                "Continue",
                "New game",
                "Load game",
                "Options",
                "Credits",
                "Exit game",
            ]

            self.load_game_widget = LoadGameWidget(self)

        else:

            self.widget_names = ["New game", "Options", "Credits", "Exit game"]

        self.new_game_widget = NewGameWidget(self)
        self.options_widget = OptionsWidget(self)

        # XXX
        # code the credits screen
        # as well as the respective main menu widget method
        self.credits_screen = None

        self.background = render_rect(*SCREEN_RECT.size, color=SKY_COLOR)

        self.game_logo = render_image(
            "danittr.png", return_obj=True, coordinates_value=(660, 100)
        )

        self.build_items()

    def build_items(self):
        """Create menu item widgets."""
        ### Create menu widget group and its buttons
        self.menu_widgets = deque()

        x, y = 250, 120
        for name in self.widget_names:
            ### Chose command
            if name == "Continue":
                command = self.load_last_save
            elif name == "New game":
                command = self.create_new_game
            elif name == "Load game":
                command = self.load_game
            elif name == "Options":
                command = self.present_options
            elif name == "Credits":
                command = self.play_credits
            elif name == "Exit game":
                command = self.exit_game

            ### Instantiate and set up

            menu_widget = render_text(
                name,
                font_size=38,
                foreground_color=WHITE,
                background_color=BLACK,
                return_obj=True,
                coordinates_value=(x, y),
            )

            menu_widget.image = give_depth_finish(menu_widget.image)

            menu_widget.invoke = command
            self.menu_widgets.append(menu_widget)
            y += 70

        ### Create group to help manage blitting
        self.widgets_group = BlitterSet(self.menu_widgets)

        self.selected_item = self.menu_widgets[0]
        self.highlight_rect = self.selected_item.rect

    def control(self):
        """Update menu state based on event_queue."""
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
                    self.selected_item.invoke()

            ### Mouse
            elif event.type == MOUSEMOTION:
                self.mouse_motion_routine(event.pos)

            elif event.type == MOUSEBUTTONDOWN:

                if event.button == 1:
                    self.mouse_click_routine(event.pos)
                self.mouse_motion_routine(event.pos)

    def update(self):
        """Update the task manager."""
        update_task_manager()

    def draw(self):
        """Draw menu and draw its items."""
        SCREEN.blit(self.background, (0, 0))
        SCREEN.blit(self.game_logo.image, self.game_logo.rect)

        self.widgets_group.draw()
        draw_rect(SCREEN, CERULEAN, self.highlight_rect, 4)

        update()

    def rotate_selection(self, amount=0):
        """Assign selected item after rotating by amount."""
        self.menu_widgets.rotate(amount)
        self.selected_item = self.menu_widgets[0]
        self.highlight_rect = self.selected_item.rect
        SOUNDS_MAP["gui_step"].play()

    select_previous = partialmethod(rotate_selection, 1)
    select_next = partialmethod(rotate_selection, -1)

    def mouse_motion_routine(self, mouse_position):
        """Check if mouse touches any widget and select it.

        mouse_position
            Tuple with x and y integers representing
            mouse position coordinates relative to
            screen topleft corner and constrained to
            the screen.
        """
        ### Search widgets
        for item in self.menu_widgets:
            if item.rect.collidepoint(mouse_position):
                touched_item = item
                break
        else:
            touched_item = None

        ### If already selected, we are done
        if touched_item == self.selected_item:
            return

        ### Select widget + admin tasks
        if touched_item:
            for i in range(len(self.menu_widgets)):
                if touched_item == self.menu_widgets[0]:
                    self.rotate_selection()
                    break
                self.menu_widgets.rotate(1)

    def mouse_click_routine(self, mouse_position):
        """Invoke widget if mouse click over it.

        mouse_position
            Tuple with x and y integers representing
            mouse position coordinates relative to
            screen topleft corner and constrained to
            the screen.
        """
        ### Search widget
        for item in self.menu_widgets:
            if item.rect.collidepoint(mouse_position):
                touched_item = item
                break
        else:
            touched_item = None

        ### Select item if needed, then invoke it
        if touched_item:
            if touched_item != self.selected_item:
                self.mouse_motion_routine(mouse_position)
            touched_item.invoke()

    def load_last_save(self):
        """Load most recent save file."""
        ### Define variables
        last_date = ""
        respective_dir = ""

        ### Iterate over dirs to determine most recent one
        for directory in listdir(SAVES_DIR):

            state_path = join(SAVES_DIR, directory, STATE_FILE_NAME)

            data = load_json(state_path)

            str_datetime = data["last_played_datetime"]

            if not last_date:
                last_date = str_datetime
                respective_dir = directory

            else:
                if max(last_date, str_datetime) != last_date:
                    last_date = str_datetime
                    respective_dir = directory

        ### Play sound + start game

        SOUNDS_MAP["game_start"].play()

        GAME_REFS.dirname = respective_dir

        level_name = load_game()

        raise LevelSwitchException(level_name)

    def create_new_game(self):
        """Load the new game setup."""
        raise ManagerSwitchException(self.new_game_widget)

    def load_game(self):
        """Load a list of save game from which to choose."""
        raise ManagerSwitchException(self.load_game_widget)

    def present_options(self):
        """Present the options setup."""
        raise ManagerSwitchException(self.options_widget)

    def play_credits(self):
        """Present the game credits."""
        # XXX
        # To be coded

    def exit_game(self):
        """Exit game."""
        logger.debug("Exiting game from main menu.")
        raise QuitGameException
