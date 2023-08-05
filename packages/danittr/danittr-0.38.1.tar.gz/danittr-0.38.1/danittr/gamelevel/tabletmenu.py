"""Facility for tablet menu classes and tools."""

# XXX
# This class is currently just a placeholder class created
# with escape menu old code. It should be properly coded soon.

from collections import deque

### third-party imports

from pygame import Surface, QUIT, KEYDOWN, K_RETURN, K_ESCAPE, K_w, K_s, K_m

from pygame.display import update
from pygame.event import get as get_events

### local imports

from ..config import SCREEN

from ..appcommon.autoblit import BlitterSet, BasicObject

from ..font import get_font
from ..palette import BLACK, WHITE


class TabletMenu(object):
    """Presents a tablet menu."""

    def __init__(self, level):
        """Initialize instance."""
        self.font = get_font(32)
        self.level = level

        self.widget_names = [
            "Resume game",
            "Save game",
            "Quit to main menu",
            "Quit to desktop",
        ]

        self.set_background()
        self.build_items()
        self.set_arrow_widget()

    def set_background(self):
        """Set a background for the menu."""
        self.background = Surface((400, 420)).convert()
        self.background.fill(BLACK)

    def build_items(self):
        """Create menu item widgets."""
        self.widgets_group = BlitterSet()
        self.menu_widgets = deque()
        x_coordinate, y_coordinate = 620, 320
        for name in self.widget_names:
            self.menu_widgets.append(
                TabletWidget(name, self, self.level, (x_coordinate, y_coordinate))
            )
            y_coordinate += 50

        self.selected_item = self.menu_widgets[0]
        self.widgets_group.update(self.menu_widgets)

    def set_arrow_widget(self):
        """Create a highlight arrow for selected items."""
        self.arrow_widget = BasicObject()
        self.arrow_widget.image = self.font.render(">", True, WHITE, BLACK)
        self.arrow_widget.rect = self.arrow_widget.image.get_rect()
        x, y = self.selected_item.rect.topleft
        self.arrow_widget.rect.topleft = (x - 20, y)
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

                elif event.key in (K_ESCAPE, K_m):
                    raise ManagerSwitchException(self.level)

    def update(self):
        """Update menu state."""
        x, y = self.selected_item.rect.topleft
        self.arrow_widget.rect.topleft = (x - 20, y)

    def draw(self):
        """Draw objects."""
        SCREEN.blit(self.background, (580, 260))
        self.widgets_group.draw()

        update()

    def select_previous(self):
        """Select previous menu item."""
        self.menu_widgets.rotate()
        self.selected_item = self.menu_widgets[0]

    def select_next(self):
        """Select next menu item."""
        self.menu_widgets.rotate(-1)
        self.selected_item = self.menu_widgets[0]

    def invoke_item_action(self):
        """Invoke the action on selected menu item."""
        self.selected_item.action()


class TabletWidget(object):
    """Escape menu item widget."""

    def __init__(self, name, escape_menu, level, topleft):
        """Initialize superclass and set instance."""
        self.font = get_font(32)

        self.name = name
        self.escape_menu = escape_menu
        self.level = level

        if name == "Resume game":
            self.action = self.resume_game
        if name == "Save game":
            self.action = self.save_game
        if name == "Quit to main menu":
            self.action = self.quit_to_main_menu
        elif name == "Quit to desktop":
            self.action = self.exit_game

        self.image = self.font.render(name, True, WHITE, BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft

    def resume_game(self):
        """Resume game."""
        raise ManagerSwitchException(self.level)

    def save_game(self):
        """Save game and level states and give feedback."""

    def quit_to_main_menu(self):
        """Load main menu."""

    def exit_game(self):
        """Exit game."""
