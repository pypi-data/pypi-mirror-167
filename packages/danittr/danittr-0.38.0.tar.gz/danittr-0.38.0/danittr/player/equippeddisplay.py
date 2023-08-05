"""Player class facility."""

from ..config import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
from ..common.behaviour import empty_function
from ..appcommon.surf import render_image, INVISIBLE_SURF

# XXX
# art: blit a backpack besides the items
# and also, maybe, blit a semi-transparent
# black background behind the items to
# give a bit contrast with the game world

SURFACE_MAP = {"mushroom": render_image("mushroom_topleft.png")}


class EquippedDisplay:
    """A display for equipped items."""

    def __init__(self):
        """Initialize superclass and set variables."""
        self.image = INVISIBLE_SURF
        self.rect = self.image.get_rect()

        self.perform_setup()

        self.update = empty_function

    def perform_setup(self):
        """Set useful variables for operation."""
        self.current_item_name = None
        self.current_item_count = 0
        self.positions = []

    def draw(self):
        """Update object state."""
        if self.current_item_count:
            for i in range(self.current_item_count):
                SCREEN.blit(self.image, self.positions[i])

    def update_visual_data(self, item_name, count):
        """Update surfaces whenever item or count changes.

        item_name
            A string representing a item name.
        count
            An integer. Represents how many items
            are on the inventory.
        """
        if self.current_item_name != item_name:
            self.current_item_name = item_name
            self.image = SURFACE_MAP[item_name]
            self.calculate_surface_positions()
        self.current_item_count = count

    def calculate_surface_positions(self):
        """Calculate positions to blit self.image.

        This takes into account the dimensions of the
        current item surface to give a pleasing padding/
        offset, so the surfaces aren't displayed too far
        or near the edges of the screen since items can have
        different dimensions."""
        self.positions = []

        surf_width, surf_height = self.image.get_size()

        vertical_padding = 32
        y = SCREEN_HEIGHT - (vertical_padding + surf_height)

        horizontal_padding = 32
        x = SCREEN_WIDTH - (horizontal_padding + surf_width)

        surfaces_distance = horizontal_padding + surf_width
        for i in range(6):
            offset = surfaces_distance * i
            position = (x - offset, y)

            self.positions.append(position)
