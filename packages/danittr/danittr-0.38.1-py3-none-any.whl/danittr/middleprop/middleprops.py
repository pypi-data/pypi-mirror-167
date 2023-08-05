"""Facility for the back_props layer."""

### local imports

from ..common.behaviour import empty_function
from ..appcommon.autoblit import BasicObject
from ..appcommon.surf import render_image


class VinesLadder(BasicObject):
    """A ladder made of vines.

    Objects whose prop_name attibute contain 'ladder'
    string are treated by player.main.Player as climbable.
    """

    level = None

    prop_map = {
        "vines_climbable": render_image("vines_climbable.png"),
        "vines_top": render_image("vines_top.png"),
        "vines_grid_climbable": render_image("vines_grid_climbable.png"),
        "vines_grid_top": render_image("vines_grid_top.png"),
    }

    def __init__(self, prop_name, coordinates):
        """Initialize superclass and variables.

        prop_name
            A string representing the prop name.
        coordinates
            List or tuple of x and y coordinates representing
            the desired bottomleft coordinates for the
            rect attribute.
        """
        self.prop_name = prop_name

        prop_value = VinesLadder.prop_map[prop_name]

        # TODO this load_image wasn't even imported; this
        # must be code left by mistake here; review it
        # (along with entire module); in fact, there should
        # be a package-wide refactoring soon;
        if isinstance(prop_value, str):
            prop_value = load_image(prop_value).convert_alpha()
            VinesLadder.prop_map[prop_name] = prop_value

        self.image = prop_value

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


class SimpleDoor(BasicObject):
    """A simple door. Portal like behaviour."""

    level = None

    prop_map = {"simple_door": render_image("simple_door.png")}

    def __init__(self, prop_name, coordinates, next_level, portal_name, destination):
        """Initialize superclass and variables.

        prop_name
            A string representing the prop name.
        coordinates
            List or tuple of x and y coordinates representing
            the desired bottomleft coordinates for the
            rect attribute.
        next_level
            A string with the basename of the level filepath.
        portal_name
            A string representing the specific portal name of
            this door instance (entrance). Used to identify
            the portal.
        destination
            A string representing the specific portal name of
            the portal on which we will end up exiting. Used
            to identify such portal.
        """
        self.prop_name = prop_name

        self.image = SimpleDoor.prop_map[prop_name]

        self.rect = self.image.get_rect()
        self.rect.bottomleft = coordinates

        self.next_level = next_level
        self.portal_name = portal_name
        self.destination = destination

        self.update = empty_function

    def scroll(self, x, y):
        """Scroll by x and y in respective axis.
        x
            Integer indicating scrolling in x axis.
        y
            Integer indicating scrolling in y axis.
        """
        self.rect.move_ip(x, y)


class CaveEntrance(BasicObject):
    """A cave entrance. Portal like behaviour."""

    level = None

    prop_map = {"cave_entrance": render_image("cave_entrance.png")}

    def __init__(self, prop_name, coordinates, next_level, portal_name, destination):
        """Initialize superclass and variables.

        prop_name
            A string representing the prop name.
        coordinates
            List or tuple of x and y coordinates representing
            the desired bottomleft coordinates for the
            rect attribute.
        next_level
            A string with the basename of the level filepath.
        portal_name
            A string representing the specific portal name of
            this door instance (entrance). Used to identify
            the portal.
        destination
            A string representing the specific portal name of
            the portal on which we will end up exiting. Used
            to identify such portal.
        """

        self.prop_name = prop_name

        self.image = CaveEntrance.prop_map[prop_name]

        self.rect = self.image.get_rect()
        self.rect.bottomleft = coordinates

        self.next_level = next_level
        self.portal_name = portal_name
        self.destination = destination

        self.update = empty_function

    def scroll(self, x, y):
        """Scroll by x and y in respective axis.
        x
            Integer indicating scrolling in x axis.
        y
            Integer indicating scrolling in y axis.
        """
        self.rect.move_ip(x, y)
