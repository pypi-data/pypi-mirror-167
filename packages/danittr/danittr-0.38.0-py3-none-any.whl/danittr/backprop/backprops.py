"""Facility for the back_props layer."""

### local imports

from ..common.behaviour import empty_function
from ..appcommon.surf import render_image
from ..appcommon.autoblit import BasicObject


class StaticBackProp(BasicObject):
    """A simple static back prop."""

    prop_map = {
        "dirt_back_prop": render_image("dirt_block01.png"),
        "dirt_darker_back_prop": render_image("dirt_darker_back_prop.png"),
        "stone_darker_back_prop": render_image("stone_darker_back_prop.png"),
        "sand_back_prop": render_image("sand_back_prop.png"),
        "stone_back_prop": render_image("stone_back_prop.png"),
    }

    def __init__(self, prop_name, coordinates):
        """Assign variables.

        prop_name
            string representing the name of the prop.
        coordinates
            bottomleft coordinates for the rect attribute.
        """
        self.prop_name = prop_name

        self.image = StaticBackProp.prop_map[prop_name]

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
