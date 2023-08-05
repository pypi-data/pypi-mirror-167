"""Facility for showing temporary messages."""

### third-party imports

from pygame import QUIT, KEYDOWN

from pygame.display import update
from pygame.event import get as get_events

### local imports

from ..config import SCREEN, SCREEN_RECT

from ..palette import WHITE

from ..common.behaviour import empty_function

from .task import update_task_manager
from .text.main import render_text
from .exception import QuitGameException, ManagerSwitchException
from .surf import render_rect


class MessageScreen(object):
    """A temporary update manager to show messages."""

    def __init__(self):
        """Assign variables and perform setups."""
        self.message_map = {}
        self.update_manager = None
        self.current_message = None
        self.extra_routine = empty_function

        self.background = render_rect(*SCREEN_RECT.size)
        self.set_press_prompt()

    def set_press_prompt(self):
        """Set a surface and coordinates for prompt message.

        Such message is a prompt for the user to press
        any key in order to remove the message screen.
        """
        self.press_prompt = render_text(
            "Press any key to exit",
            font_size=32,
            foreground_color=WHITE,
            return_obj=True,
        )

        self.press_prompt.rect.topright = SCREEN_RECT.topright

        self.press_prompt.rect.x += -100
        self.press_prompt.rect.y += 35

    def cache_message(self, message_name, text):
        """Create and store a text obj for later use.

        message_name
            String representing a field in a dict which
            is used to retrieve information later.
        text
            String used to generated text surface.
        """
        obj = render_text(text, font_size=32, foreground_color=WHITE, return_obj=True)

        obj.rect.center = SCREEN_RECT.center

        self.message_map[message_name] = obj

    def display_message(self, message_name, update_manager, extra_routine=None):
        """Retrieve from map and display surface.

        message_name
            String representing the field in a dict whose
            value is the surface to be displayed.
        update_manager
            Any update_manager instance which
            should be reassigned back to
            game.Game.update_manager back after
            showing messages.
        extra_routine
            Optional callable to be executed after
            displaying the message.
        """
        if extra_routine:
            self.extra_routine = extra_routine

        self.update_manager = update_manager
        self.current_message = message_name

        raise ManagerSwitchException(self)

    def control(self):
        """Handle events."""
        for event in get_events():

            if event.type == QUIT:
                raise QuitGameException

            elif event.type == KEYDOWN:
                self.exit_message_screen()

    def update(self):
        """Blit message on screen."""
        self.extra_routine()
        update_task_manager()

    def draw(self):
        """Draw objects."""
        SCREEN.blit(self.background, (0, 0))

        message = self.message_map[self.current_message]
        SCREEN.blit(message.image, message.rect)

        SCREEN.blit(self.press_prompt.image, self.press_prompt.rect)

        update()

    def exit_message_screen(self):
        """Get back to previous update_manager."""
        raise ManagerSwitchException(self.update_manager)

    def clear(self):
        """Clear messages and other data."""
        self.message_map.clear()
        self.update_manager = None
        self.current_message = None
        self.extra_routine = empty_function


MESSAGE_SCREEN = MessageScreen()
cache_message = MESSAGE_SCREEN.cache_message
display_message = MESSAGE_SCREEN.display_message
clear_messages = MESSAGE_SCREEN.clear
