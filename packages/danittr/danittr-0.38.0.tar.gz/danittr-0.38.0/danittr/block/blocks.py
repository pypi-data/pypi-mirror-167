"""Facility for the blocks layer."""

from ..common.behaviour import empty_function
from ..appcommon.surf import render_image
from ..appcommon.autoblit import BasicObject


class StaticBlock(BasicObject):
    """A simple static block."""

    level = None
    prop_map = {
        "stone_block": render_image("stone_block.png"),
        "dirt_block01": render_image("dirt_block01.png"),
        "sand_block": render_image("sand_block.png"),
    }

    def __init__(self, prop_name, coordinates):
        """Assign variables.

        prop_name
            string representing the name of the prop.
        coordinates
            bottomleft coordinates for the rect attribute.
        """
        self.prop_name = prop_name

        self.image = StaticBlock.prop_map[prop_name]

        self.rect = self.image.get_rect()

        self.rect.bottomleft = coordinates

        self.update = empty_function

    def scroll(self, x, y):
        """Scroll by x and y in respective axis.
        x
            Integer indicating scrolling in x axis.
        y
            Integer indicating scrolling in y axis.
        """
        self.rect.move_ip(x, y)
