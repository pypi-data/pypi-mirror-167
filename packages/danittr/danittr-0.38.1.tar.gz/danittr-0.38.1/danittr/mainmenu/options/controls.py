"""Facility for controls configuration.

Here we provide an object which manages the screen.
It's purpose is to present the player with means to
change settings in the USER_SETTING["keys_map"] mapping and have them applied.
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
    MOUSEBUTTONDOWN,
    MOUSEMOTION,
)

from pygame.key import name as name_key
from pygame.draw import rect as draw_rect
from pygame.event import get as get_events
from pygame.display import update

### local imports

from ...config import SCREEN, SCREEN_RECT, USER_SETTINGS, DEFAULT_SETTINGS, KEYS_MAP

from ...common.behaviour import empty_function

from ...appcommon.surf import render_rect
from ...appcommon.style import give_depth_finish
from ...appcommon.dialog import cache_message, display_message
from ...appcommon.autoblit import BlitterSet
from ...appcommon.exception import QuitGameException, ManagerSwitchException
from ...appcommon.text.main import render_text
from ...appcommon.behaviour.setting import apply_user_settings

from .widgets import get_button

from ...sound import SOUNDS_MAP
from ...palette import CERULEAN, BLACK, WHITE, SKY_COLOR
from ...keymapping import VALID_KEYS_MAP


# TODO
# I should probably use strings for control values instead
# of their integer values; this ways the same controls
# scheme can be used in different systems;


class ControlsWidget:
    """Widget for setting up custom controls.

    The user is allowed to change controls for some
    specific actions.
    """

    def __init__(self, options_widget):
        """Set variables and perform setups.

        options_widget
            The instance of mainmenu.options.OptionsWidget.
        """
        self.options_widget = options_widget

        self.set_labels()

        ### Instantiate and store a background surface
        self.background = render_rect(*SCREEN_RECT.size, color=SKY_COLOR)

        self.build_widgets()
        self.set_other_objects()

        cache_message(
            "not_free", "The key you chose is already being used" + " in another action"
        )
        cache_message("not_valid", "The key you chose isn't considered valid.")

        ### define behaviours

        self.draw = self.draw_control_widgets
        self.control = self.handle_events

    def set_labels(self):
        """Create a sprite to serve as a label."""
        self.labels = BlitterSet()

        self.texts = [
            "Player left movement",
            "Player right movement",
            "Player up movement",
            "Player down movement",
            "Player jump movement",
            "Player fire item action",
            "Player interact action",
            "Advance dialogue/deny prompt",
            "Accept prompt",
        ]
        y = 25
        self.max_width = 0
        for text in self.texts:
            label = render_text(
                text,
                32,
                foreground_color=WHITE,
                background_color=BLACK,
                return_obj=True,
                coordinates_value=(60, y),
            )
            label.text = text
            y += 60
            self.labels.add(label)

            self.max_width = max(self.max_width, label.rect.w)

        for label in self.labels:
            label.rect.x = label.rect.x + self.max_width - label.rect.w

    def build_widgets(self):
        """Create option widgets."""
        self.widgets_deque = deque()

        fields = [
            "player_left",
            "player_right",
            "player_up",
            "player_down",
            "jump",
            "fire_item",
            "interact",
            "advance_deny",
            "accept_prompt",
        ]

        arbitrary_offset = 80
        x = self.max_width + arbitrary_offset
        y = 25
        for text, field in zip(self.texts, fields):
            widget = ControlSwitcher(self, field, (x, y))
            widget.text = text
            self.widgets_deque.append(widget)
            y += 60
        self.widgets_deque.append(
            get_button("Restore default controls", (x, y), self.restore_defaults)
        )

        self.widgets = BlitterSet(self.widgets_deque)

        self.current_widget = self.widgets_deque[0]
        self.highlight_rect = self.current_widget.rect

    def set_other_objects(self):
        """Create additional objects to help."""
        self.prompt_labels = BlitterSet()

        txt01 = "Please, type the new key"
        txt02 = "for the action you chose:"
        txt03 = "(or press <ESCAPE> if you want to cancel)"
        type_prompt01 = render_text(
            txt01,
            font_size=42,
            foreground_color=WHITE,
            background_color=BLACK,
            return_obj=True,
        )

        type_prompt02 = render_text(
            txt02,
            font_size=42,
            foreground_color=WHITE,
            background_color=BLACK,
            return_obj=True,
        )
        type_prompt03 = render_text(
            txt03,
            font_size=28,
            foreground_color=WHITE,
            background_color=BLACK,
            return_obj=True,
        )

        type_prompt01.rect.midbottom = type_prompt02.rect.midtop = SCREEN_RECT.center

        self.action_name_topleft = type_prompt02.rect.bottomleft

        type_prompt03.rect.bottomright = SCREEN_RECT.bottomright
        type_prompt03.rect.x += -35
        type_prompt03.rect.y += -35

        self.prompt_labels.update([type_prompt01, type_prompt02, type_prompt03])

    def handle_events(self):
        """Update widget state based on event_queue."""
        for event in get_events():

            if event.type == QUIT:
                raise QuitGameException

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    raise ManagerSwitchException(self.options_widget)

                elif event.key == K_RETURN:
                    self.invoke_button()

                elif event.key in (K_w, K_UP):
                    self.go_up()

                elif event.key in (K_s, K_DOWN):
                    self.go_down()

            elif event.type == MOUSEMOTION:
                self.mouse_motion_routine(event.pos)

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse_click_routine(event.pos)

    def update(self):
        """Update widgets."""
        self.widgets.update_objs()

    def draw_control_widgets(self):
        """Draw control widgets and other widgets."""
        SCREEN.blit(self.background, (0, 0))
        self.labels.draw()
        self.widgets.draw_objs()
        draw_rect(SCREEN, CERULEAN, self.highlight_rect, 4)

        update()

    def change_field_key(self, field):
        """Change the field key input."""
        self.field = field

        self.current_label = [
            label for label in self.labels if self.current_widget.text == label.text
        ].pop()

        self.draw = self.show_key_prompt
        self.control = self.get_new_key

    def show_key_prompt(self):
        """Prompt user to type new key."""
        SCREEN.blit(self.background, (0, 0))
        self.prompt_labels.draw()
        SCREEN.blit(self.current_label.image, self.action_name_topleft)

        update()

    def get_new_key(self):
        """Get new key typed by user."""
        for event in get_events():
            if event.type == QUIT:
                raise QuitGameException

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:

                    self.draw = self.draw_control_widgets
                    self.control = self.handle_events

                else:
                    self.check_key(event.key)

    def check_key(self, key):
        """Verify and switch key if appropriate."""
        valid = key in VALID_KEYS_MAP.values()
        free = key not in KEYS_MAP.values()

        if free and valid:

            KEYS_MAP[self.field] = key
            self.current_widget.update_surface()

            apply_user_settings()

            self.draw = self.draw_control_widgets
            self.control = self.handle_events

        elif not free:
            SOUNDS_MAP["error"].play()
            display_message("not_free", self)

        elif not valid:
            SOUNDS_MAP["error"].play()
            display_message("not_valid", self)

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
        """Check if mouse touches any widget and select it."""
        touched_item = None

        for item in self.widgets_deque:

            if item.rect.collidepoint(mouse_position):
                touched_item = item
                break

        if touched_item == self.current_widget:
            return

        if touched_item:
            for i in range(len(self.widgets_deque)):

                if touched_item == self.widgets_deque[0]:
                    self.switch_widget()
                    break
                self.widgets_deque.rotate(1)

    def mouse_click_routine(self, mouse_position):
        """Invoke widget if mouse click over it."""
        touched_item = None

        for item in self.widgets_deque:

            if item.rect.collidepoint(mouse_position):
                touched_item = item
                break

        if touched_item:

            if touched_item != self.current_widget:
                self.mouse_motion_routine(mouse_position)

            touched_item.invoke()

    def restore_defaults(self):
        """Restore control defaults."""
        USER_SETTINGS["keys_map"].update(DEFAULT_SETTINGS["keys_map"])

        for widget in self.widgets:

            try:
                widget.update_surface()
            except AttributeError:
                pass

        apply_user_settings()

    def invoke_button(self):
        """Invoke current widget, if it can be invoked."""
        self.current_widget.invoke()


class ControlSwitcher:
    """Widget to change control for specific action."""

    def __init__(self, controls_widget, field, topleft):
        """Assign data and perform setups."""
        self.controls_widget = controls_widget

        self.field = field
        self.topleft = topleft

        self.update_surface()

        ### define update behaviour
        self.update = empty_function

    def draw(self):
        """Update object state."""
        SCREEN.blit(self.image, self.rect)

    def invoke(self):
        """Change key of the action."""
        self.controls_widget.change_field_key(self.field)

    def update_surface(self):
        """Update image surface."""
        text = name_key(KEYS_MAP[self.field])

        if text == "return":
            text = "enter"

        surf = render_text(
            text, font_size=32, foreground_color=WHITE, background_color=BLACK
        )

        self.image = give_depth_finish(surf)

        self.rect = self.image.get_rect()
        self.rect.topleft = self.topleft
