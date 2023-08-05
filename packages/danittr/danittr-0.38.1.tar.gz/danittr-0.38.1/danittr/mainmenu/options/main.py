"""Facility for options configuration.

Here we provide an object which manages the screen.
It's purpose is to present the player with means to
change settings in the USER_SETTING mapping and have
them applied.
"""

from collections import deque
from functools import partialmethod

### third-party imports

from pygame import (
    QUIT,
    KEYDOWN,
    K_ESCAPE,
    K_RETURN,
    K_w,
    K_UP,
    K_s,
    K_DOWN,
    K_a,
    K_LEFT,
    K_d,
    K_RIGHT,
    MOUSEBUTTONDOWN,
    MOUSEMOTION,
)

from pygame.display import update
from pygame.event import get as get_events
from pygame.draw import rect as draw_rect

### local imports

from ...config import SCREEN, SCREEN_RECT, DEFAULT_SETTINGS, USER_SETTINGS

from ...appcommon.task import update_task_manager
from ...appcommon.surf import render_rect
from ...appcommon.autoblit import BlitterSet
from ...appcommon.exception import QuitGameException, ManagerSwitchException
from ...appcommon.text.main import render_text

from ...appcommon.behaviour.setting import apply_user_settings

from .widgets import VolumeScale, get_button
from .controls import ControlsWidget

from ...sound import SOUNDS_MAP
from ...palette import CERULEAN, BLACK, WHITE, SKY_COLOR


class OptionsWidget(object):
    """Widget for setting up a new game and its data.

    The user is prompted for a name for a new save."""

    def __init__(self, main_menu):
        """Set variables and perform setups.

        main_menu
            The instance of the mainmenu.main.MainMenu class.
        """
        self.main_menu = main_menu

        self.set_labels()
        self.background = render_rect(*SCREEN_RECT.size, color=SKY_COLOR)
        self.control_widget = ControlsWidget(self)
        self.build_widgets()

    def set_labels(self):
        """Create a sprite to serve as a label."""
        self.labels = BlitterSet()

        text01 = "Music Volume"
        label01 = render_text(
            text01,
            32,
            foreground_color=WHITE,
            background_color=BLACK,
            return_obj=True,
            coordinates_value=(100, 130),
        )

        text02 = "SFX Volume"
        label02 = render_text(
            text02,
            32,
            foreground_color=WHITE,
            background_color=BLACK,
            return_obj=True,
            coordinates_value=(100, 250),
        )

        self.labels.update([label01, label02])

    def build_widgets(self):
        """Create option widgets."""
        ### Create container and define variable
        self.widgets_deque = deque()

        update_command = apply_user_settings

        ### Music volume
        self.widgets_deque.append(
            VolumeScale(USER_SETTINGS, "music_volume", (100, 180), update_command)
        )

        jump_sound = SOUNDS_MAP["player_jump01"]

        ### Sound volume
        self.widgets_deque.append(
            VolumeScale(
                USER_SETTINGS,
                "sound_volume",
                (100, 300),
                update_command,
                jump_sound.play,
            )
        )

        ### Restore defaults
        self.widgets_deque.append(
            get_button("Restore volume defaults", (100, 400), self.restore_defaults)
        )

        ### Configure controls
        self.widgets_deque.append(
            get_button("Configure controls", (100, 520), self.switch_to_control)
        )

        ### Create group to help manage blitting
        self.widgets = BlitterSet(self.widgets_deque)

        ### Select first widget and rect to be highlighted
        self.current_widget = self.widgets_deque[0]
        self.highlight_rect = self.current_widget.rect

    def control(self):
        """Update widget state based on event_queue."""
        for event in get_events():

            if event.type == QUIT:
                raise QuitGameException

            ### Keyboard

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    raise ManagerSwitchException(self.main_menu)

                elif event.key == K_RETURN:
                    self.invoke_button()

                elif event.key in (K_w, K_UP):
                    self.go_up()

                elif event.key in (K_s, K_DOWN):
                    self.go_down()

                elif event.key in (K_a, K_LEFT):

                    try:
                        self.current_widget.decrease()
                    except AttributeError:
                        pass

                elif event.key in (K_d, K_RIGHT):

                    try:
                        self.current_widget.increase()
                    except AttributeError:
                        pass

            ### Mouse

            elif event.type == MOUSEMOTION:
                self.mouse_motion_routine(event.pos)

            elif event.type == MOUSEBUTTONDOWN:

                if event.button == 1:
                    self.mouse_click_routine(event.pos)

    def update(self):
        """Update widgets states."""
        self.widgets.update_objs()
        update_task_manager()

    def draw(self):
        """Draw widgets and update screen."""
        SCREEN.blit(self.background, (0, 0))

        self.labels.draw()
        self.widgets.draw_objs()

        draw_rect(SCREEN, CERULEAN, self.highlight_rect, 3)

        update()

    def switch_widget(self, steps=0):
        """Switch widgets by steps.

        steps
            integers representing how many the widgets deque
            should rotate.
        """
        self.widgets_deque.rotate(steps)
        self.current_widget = self.widgets_deque[0]

        self.highlight_rect = self.current_widget.rect
        SOUNDS_MAP["gui_step"].play()

    go_up = partialmethod(switch_widget, 1)
    go_down = partialmethod(switch_widget, -1)

    def mouse_motion_routine(self, mouse_position):
        """Check if mouse touches any widget and select it.

        mouse_position
            Tuple with x and y integers representing
            mouse position relative to the topleft corner
            of the screen, constrained to the screen.
        """
        ### Search widget
        for item in self.widgets_deque:
            if item.rect.collidepoint(mouse_position):
                touched_item = item
                break
        else:
            touched_item = None

        ### If already selected, we are done
        if touched_item == self.current_widget:
            return

        ### Select widget
        if touched_item:
            for i in range(len(self.widgets_deque)):
                if touched_item == self.widgets_deque[0]:
                    self.switch_widget()
                    break
                self.widgets_deque.rotate(1)

    def mouse_click_routine(self, mouse_position):
        """Invoke widget if mouse click over it.

        mouse_position
            Tuple with x and y integers representing
            mouse position relative to the topleft corner
            of the screen, constrained to the screen.
        """
        ### Search widget
        for item in self.widgets_deque:
            if item.rect.collidepoint(mouse_position):
                touched_item = item
                break
        else:
            touched_item = None

        ### Select it if needed then invoke it
        if touched_item:
            if touched_item != self.current_widget:
                self.mouse_motion_routine(mouse_position)
            self.invoke_button()

    def restore_defaults(self):
        """Restore volume defaults."""
        USER_SETTINGS["music_volume"] = DEFAULT_SETTINGS["music_volume"]

        USER_SETTINGS["sound_volume"] = DEFAULT_SETTINGS["sound_volume"]

        apply_user_settings()

        for widget in self.widgets_deque:

            try:
                widget.place_handle()
            except AttributeError:
                pass

    def switch_to_control(self):
        """Switch update manager to control widget."""
        raise ManagerSwitchException(self.control_widget)

    def invoke_button(self):
        """Invoke current widget, if it can be invoked."""
        try:
            self.current_widget.invoke()
        except AttributeError:
            pass
