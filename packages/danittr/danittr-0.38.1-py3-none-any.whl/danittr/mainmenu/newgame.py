"""Facility for new game creation.

Here we provide an object which manages the screen.
It's purpose is to present the player with means to
enter a name for a new save to be created.

Once the name is entered and approved, the player starts
to play the first level."""

from os import listdir
from random import seed, choice
from string import ascii_lowercase, digits
from itertools import cycle

### third-party imports

from pygame import QUIT, KEYDOWN, K_ESCAPE, K_BACKSPACE, K_RETURN

from pygame.display import update
from pygame.event import get as get_events

### local imports

from ..config import SCREEN, SCREEN_RECT, SAVES_DIR, GAME_REFS

from ..appcommon.task import update_task_manager
from ..appcommon.surf import INVISIBLE_SURF, render_rect
from ..appcommon.dialog import cache_message, display_message
from ..appcommon.autoblit import BlitterSet
from ..appcommon.text.main import render_text
from ..appcommon.exception import (
    QuitGameException,
    LevelSwitchException,
    ManagerSwitchException,
)

from ..appcommon.behaviour.save import setup_new_save
from ..appcommon.behaviour.load import load_game

from ..sound import SOUNDS_MAP
from ..palette import WHITE, SKY_COLOR


CHARACTERS = ascii_lowercase + digits


class NewGameWidget(object):
    """Widget for setting up a new game and its data.

    The user is prompted for a name for a new save."""

    def __init__(self, main_menu):
        """Set variables and perform setups.

        main_menu
            The instance of the mainmenu.main.MainMenu class.
        """
        self.main_menu = main_menu

        self.error_sound = SOUNDS_MAP["error"]

        self.set_labels()
        self.background = render_rect(*SCREEN_RECT.size, color=SKY_COLOR)

        self.prompt = TextPrompt((520, 340), self)

        cache_message("three_or_more", "Save name must have 03 or more characters.")
        cache_message("name_exists", "The name you picked already exists.")
        cache_message("ten_or_less", "Save name must have 10 or less characters.")

    def set_labels(self):
        """Create a sprite to serve as a label."""

        label_texts = [
            "Please, enter name for new save slot:",
            "use lowercase letters and numbers;",
            "the name must have from 03 to 10 characters;",
            "press <ENTER> when done;",
            "press <BACKSPACE> to delete last character;",
        ]

        self.labels = BlitterSet()
        y = 40
        for text in label_texts:

            label = render_text(
                text,
                font_size=32,
                foreground_color=WHITE,
                return_obj=True,
                coordinates_value=(60, y),
            )

            self.labels.add(label)
            y += 40

    def control(self):
        """Update widget state based on event_queue."""
        for event in get_events():
            if event.type == QUIT:
                raise QuitGameException

            ### Keyboard
            elif event.type == KEYDOWN:

                if event.unicode in CHARACTERS:
                    self.prompt.insert_char(event.unicode)

                elif event.key == K_BACKSPACE:
                    self.prompt.delete_last_char()

                elif event.key == K_RETURN:
                    self.create_new_game()

                elif event.key == K_ESCAPE:
                    raise ManagerSwitchException(self.main_menu)

    def update(self):
        """Update the task manager."""
        update_task_manager()

    def draw(self):
        """Draw widget objects."""
        SCREEN.blit(self.background, (0, 0))
        self.labels.draw()
        self.prompt.draw()

        update()

    def create_new_game(self):
        """Retrieve string from prompt to create new save."""
        save_name = self.prompt.save_name

        if len(save_name) <= 2:

            self.error_sound.play()
            display_message("three_or_more", self)

        else:

            dirname = "save_" + save_name

            if dirname in listdir(SAVES_DIR):

                self.error_sound.play()
                display_message("name_exists", self)

            else:

                setup_new_save(dirname)

                SOUNDS_MAP["game_start"].play()

                GAME_REFS.dirname = dirname
                level_name = load_game()

                raise LevelSwitchException(level_name)


class TextPrompt:
    """A text prompt which displays input."""

    def __init__(self, topleft, new_game_widget):
        """Initialize superclass and set instance.

        topleft
            the topleft coordinates to begin blit
            surfaces in the update method.
        new_game_widget
            reference to mainmenu.newgame.NewGameWidget class.
        """
        self.topleft = topleft
        self.new_game_widget = new_game_widget

        self.save_name = ""

        seed()
        self.typing_sounds = [SOUNDS_MAP["key_typing01"], SOUNDS_MAP["key_typing02"]]

        self.build_surface_map()
        self.blinking_cursor = BlinkingCursor()

    def build_surface_map(self):
        """Create and store text surfaces each character."""
        self.surface_map = {}
        for char in CHARACTERS:
            text_surf = render_text(char, font_size=56, foreground_color=WHITE)
            self.surface_map[char] = text_surf

    def draw(self):
        """Update widget state."""
        x, y = self.topleft

        for char in self.save_name:
            surf = self.surface_map[char]
            width = surf.get_width()
            SCREEN.blit(self.surface_map[char], (x, y))
            x += width

        self.blinking_cursor.blit_on_topleft((x, y))

    def delete_last_char(self):
        """Delete last char in save name."""
        if self.save_name:
            self.save_name = self.save_name[:-1]

    def insert_char(self, char):
        """Replace first '_' character by provided char.

        char
            A string of length == 1.
        """
        if len(self.save_name) < 10:
            self.save_name = self.save_name + char
            choice(self.typing_sounds).play()

        else:
            SOUNDS_MAP["error"].play()
            display_message("ten_or_less", self.new_game_widget)


class BlinkingCursor:
    """A blinking cursor to assist the text prompt."""

    def __init__(self):
        """Assign variables and perform setups."""
        self.image = render_rect(40, 70, WHITE)

        ### create callable to return True in the first
        ### n calls, then False in the next n calls, and
        ### so on

        n = 15
        self.blit = cycle((True,) * n + (False,) * n).__next__

    def blit_on_topleft(self, topleft):
        """Blit surface on screen in topleft coordinates.

        topleft
            Topleft coordinates wherein to blit the surface.
        """
        if self.blit():
            SCREEN.blit(self.image, topleft)
