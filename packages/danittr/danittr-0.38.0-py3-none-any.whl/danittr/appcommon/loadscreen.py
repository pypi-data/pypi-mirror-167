"""Facility for load screen management."""

from math import radians
from os.path import join
from itertools import cycle

### third-party imports

from pygame.time import wait, get_ticks as get_millisecs
from pygame.image import load as load_image
from pygame.display import update

### local imports

from ..config import SCREEN, SCREEN_RECT, MILLISECS_PER_FRAME, IMAGES_DIR

from ..palette import BLACK, WHITE
from ..logconfig import APP_LOGGER

from .text.main import render_text


logger = APP_LOGGER.getChild(__name__)


### class definition


class LoadScreenManager:
    """Common behaviour/objects for elegant screen loading."""

    def __init__(self):
        """Instantiate text objects, store millisec count."""
        ### create text objects to assist the class

        ## please wait text

        topright = SCREEN_RECT.move(-50, 35).topright

        self.wait_text = render_text(
            "Please wait...",
            font_size=36,
            foreground_color=BLACK,
            return_obj=True,
            coordinates_name="topright",
            coordinates_value=topright,
        )

        ## resources text

        center = SCREEN_RECT.move(0, 40).center

        self.resources_text = render_text(
            "Loading resources...",
            font_size=36,
            foreground_color=BLACK,
            return_obj=True,
            coordinates_name="center",
            coordinates_value=center,
        )

        self.millisecs_count = 0

        ### load surface objects for simple loading animation

        mushroom_filenames = (
            "mushroom_topleft.png",
            "mushroom_topright.png",
            "mushroom_bottomright.png",
            "mushroom_bottomleft.png",
        )

        surfs = [
            load_image(join(IMAGES_DIR, filename)).convert_alpha()
            for filename in mushroom_filenames
        ]

        ### store a function to indefinitely return the next
        ### surface from the list
        self.get_next_surf = cycle(surfs).__next__

        ### create a rect from one of the mushroom surfaces
        ### and position at the center of the screen

        self.mushroom_rect = self.get_next_surf().get_rect()
        self.mushroom_rect.center = SCREEN_RECT.center

    def blit_loading_screen(self):
        """Blit simple message while loading."""
        logger.info("Displaying loading screen.")

        SCREEN.fill((245, 245, 245))

        self.wait_text.draw()

        update()

        # wait around just half a second (500 milliseconds)
        # so the user can read the "Please wait" message;
        # this is just an usability measure; if we didn't
        # wait a bit, the text would disappear almost
        # immediately, since loading time is quick, and the
        # user might be left confused wondering whether the
        # text they couldn't read was important;
        wait(500)

    def blit_resource_loading(self):
        """Blit resource loading message as time passes."""
        ### calculate delta of time

        current_millisecs = get_millisecs()
        delta_t = current_millisecs - self.millisecs_count

        ### if delta time equals or surpasses the average
        ### millisecs per frame, blit resource loading
        ### message and update millisecs_count attribute

        if delta_t >= MILLISECS_PER_FRAME:

            SCREEN.fill((245, 245, 245))

            self.resources_text.draw()

            SCREEN.blit(self.get_next_surf(), self.mushroom_rect)

            update()

            self.millisecs_count = current_millisecs


load_screen_manager = LoadScreenManager()
blit_loading_screen = load_screen_manager.blit_loading_screen
blit_resource_loading = load_screen_manager.blit_resource_loading
