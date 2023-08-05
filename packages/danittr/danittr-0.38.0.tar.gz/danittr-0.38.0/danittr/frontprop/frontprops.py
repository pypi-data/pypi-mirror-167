"""Facility for the front_props layer."""

### local imports

from ..common.behaviour import empty_function
from ..appcommon.autoblit import BasicObject
from ..appcommon.surf import render_image


class LeafCarpet(BasicObject):
    """A leaf carpet on a wall."""

    level = None
    prop_map = {"leaf_carpet": render_image("leaf_carpet.png")}

    def __init__(self, prop_name, coordinates):
        """Initialize superclass and variables.

        prop_name
            string representing the name of the prop.
        coordinates
            the bottomleft coordinates for the rect attribute.
        """
        self.prop_name = prop_name

        self.image = LeafCarpet.prop_map[prop_name]

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


class FrozenCover(BasicObject):
    """A cover made of ice."""

    level = None
    prop_map = {"frozen_cover": render_image("frozen_cover.png")}

    def __init__(self, prop_name, coordinates):
        """Initialize superclass and variables.

        prop_name
            string representing the name of the prop.
        coordinates
            the bottomleft coordinates for the rect attribute.
        """
        self.prop_name = prop_name

        self.image = FrozenCover.prop_map[prop_name]

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
