"""Facility for escape menu class and related tools."""

from collections import deque
from functools import partialmethod

### third-party imports

from pygame import QUIT, KEYDOWN, K_RETURN, K_ESCAPE, K_w, K_s

from pygame.display import update
from pygame.event import get as get_events

### local imports

from ..config import SCREEN, GAME_REFS

from ..appcommon.surf import render_rect
from ..appcommon.autoblit import BlitterSet, BasicObject
from ..appcommon.exception import QuitGameException, ManagerSwitchException
from ..appcommon.text.main import render_text
from ..appcommon.behaviour.buffer import remove_buffers

from .classes import remove_level_reference

from ..palette import BLACK, WHITE


class EscapeMenu(object):
    """Presents an escape menu."""

    def __init__(self, level):
        """Initialize instance.

        level
            the instance of gamelevel.main.Level."""
        self.font_size = 32
        self.level = level

        self.widget_names = ["Resume game", "Quit to main menu", "Quit to desktop"]

        self.background = render_rect(400, 420)
        self.build_items()
        self.set_arrow_widget()

    def build_items(self):
        """Create menu item widgets."""
        self.menu_widgets = deque()
        x, y = 620, 320
        for name in self.widget_names:
            escape_menu_widget = EscapeMenuWidget(name, self, self.level, (x, y))
            self.menu_widgets.append(escape_menu_widget)
            y += 50

        self.widgets_group = BlitterSet(self.menu_widgets)

        self.selected_item = self.menu_widgets[0]
        self.widgets_group.update(self.menu_widgets)

    def set_arrow_widget(self):
        """Create a highlight arrow for selected items."""
        self.arrow_widget = BasicObject()
        self.arrow_widget.image = render_text(
            ">",
            font_size=self.font_size,
            foreground_color=WHITE,
            background_color=BLACK,
        )
        self.arrow_widget.rect = self.arrow_widget.image.get_rect()
        self.arrow_widget.rect.midright = self.selected_item.rect.midleft
        self.widgets_group.add(self.arrow_widget)

    def control(self):
        """Handle events in level event queue."""
        for event in get_events():

            if event.type == QUIT:
                raise QuitGameException

            elif event.type == KEYDOWN:

                if event.key == K_w:
                    self.select_previous()

                elif event.key == K_s:
                    self.select_next()

                elif event.key == K_RETURN:
                    self.invoke_item_action()

                elif event.key == K_ESCAPE:
                    raise ManagerSwitchException(self.level)

    def update(self):
        """Update menu state."""
        self.arrow_widget.rect.midright = self.selected_item.rect.midleft

    def draw(self):
        """Draw objects."""
        SCREEN.blit(self.background, (580, 260))
        self.widgets_group.draw()

        update()

    def rotate_selection(self, amount):
        """Assign selection after rotating by amount."""
        self.menu_widgets.rotate(amount)
        self.selected_item = self.menu_widgets[0]

    select_previous = partialmethod(rotate_selection, 1)
    select_next = partialmethod(rotate_selection, -1)

    def invoke_item_action(self):
        """Invoke the action on selected menu item."""
        self.selected_item.action()


class EscapeMenuWidget(object):
    """Escape menu item widget."""

    def __init__(self, name, escape_menu, level, topleft):
        """Initialize superclass and set instance.

        name
            string representing the item text. Also used
            to associate it with its method.
        escape_menu
            the instance of ingame.escapemenu.EscapeMenu
            class.
        level
            the instance of gamelevel.main.Level
        topleft
            the topleft coordinates for the rect attribute
        """
        self.font_size = 32

        self.name = name
        self.escape_menu = escape_menu
        self.level = level

        if name == "Resume game":
            self.action = self.resume_game
        elif name == "Quit to main menu":
            self.action = self.quit_to_main_menu
        elif name == "Quit to desktop":
            self.action = self.exit_game

        self.image = render_text(
            name,
            font_size=self.font_size,
            foreground_color=WHITE,
            background_color=BLACK,
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft

    def resume_game(self):
        """Resume game."""
        raise ManagerSwitchException(self.level)

    def quit_to_main_menu(self):
        """Load main menu."""
        remove_level_reference()

        remove_buffers()

        del GAME_REFS.dirname

        raise ManagerSwitchException("main_menu")

    def exit_game(self):
        """Exit game."""
        raise QuitGameException
