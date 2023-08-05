"""Facility for sign middle prop class."""

### local imports

from ..common.behaviour import empty_function
from ..appcommon.autoblit import BasicObject
from ..appcommon.signfactory import sign_factory


class Sign(BasicObject):
    """A class to represent a sign or signpost.

    The surfaces are generated in
    appcommon/signfactory.py
    """

    #     _______        _______|\         _______|\
    #    |       |      |         \       |         \
    #    | Hello |  or  | Hello    \  or  | Hello    \
    #    |_______|      |          /      |          /
    #                   |_______  /       |_______  /
    #                           |/           |  | |/
    #                                        |  |
    #                                        |__|

    level = None

    def __init__(
        self,
        prop_name,
        coordinates,
        text,
        fg_color,
        bg_color,
        signpost_height=0,
        direction=None,
    ):
        """Initialize superclass and variables.

        prop_name
            A string representing the prop name.
        coordinates
            List or tuple of x and y coordinates representing
            the desired bottomleft coordinates for the
            rect attribute.
        text
            A string to be used on the sign surface.
        fg_color
            The foreground color of the sign. A tuple
            or list with three integers representing
            r, g, b values from 0 to 255.
        bg_color
            The background color of the sign. A tuple
            or list with three integers representing
            r, g, b values from 0 to 255.
        signpost_height
            Integer representing the height of the
            post which supports the sign. If 0 there will
            be no such post.
        direction
            A string of the set {'n', 's', 'e', 'w'} or
            None. If none, the sign won't be represented
            by an arrow pointing in a specific direction,
            but by a rectangle.
        """
        self.prop_name = prop_name

        self.image = sign_factory(text, fg_color, bg_color, signpost_height, direction)

        self.rect = self.image.get_rect()
        self.rect.bottomleft = coordinates

        if signpost_height:
            self.rect.y += 4

        self.update = empty_function

    def scroll(self, x, y):
        """Scroll by x and y in respective axis.
        x
            Integer indicating scrolling in x axis.
        y
            Integer indicating scrolling in y axis.
        """
        self.rect.move_ip(x, y)
