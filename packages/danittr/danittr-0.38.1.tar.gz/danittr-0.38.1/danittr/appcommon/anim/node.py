"""Facility for node class."""

from pygame import Rect

from ...common.math import invert_point
from ..autoblit import BasicObject


class Node(BasicObject):
    """Provides operations for tree-structured animation.

    This class is used to represent an object as part of a
    compound object, that is a node in a tree of objects.

    It provides operations to change its positions over time
    relative to a parent node which can be (re)assigned
    anytime to the 'parent' attribute.

    Thanks to that, it can be easily (re)arranged into
    multiple combinations with other instances into a
    tree structure just by having a parent assigned to each
    node, except for the 'top' parent (the root), which
    should have 'None' assigned to the parent attribute in
    order to work properly. This is how this object is
    intended to be used.
    """

    def __init__(self, node_name, node_data):
        """Store data and perform setups.

        ### Arguments

        node_name (string)
            Unique name of the node.

        node_data (dict)
            data about the node's dimensions and, if it has
            collision data, the dimensions of the collision
            rect and its offset relative to the center of
            the node rect, if any.
        """
        ### store unique name
        self.name = node_name

        ### process geometry related data

        geometry_data = node_data["geometry"]

        ## Create normal rect/image attributes
        width, height = geometry_data["dimensions"]
        self.rect = Rect((0, 0), (width, height))

        ## Process collision data if existent

        try:
            collision_data = geometry_data["collision_data"]

        except KeyError:
            self.col_rect = None

        else:
            ## Create col_rect attribute for collisions

            width, height = collision_data["dimensions"]
            self.col_rect = Rect(self.rect.topleft, (width, height))
            self.col_rect_offset = collision_data.get("offset", (0, 0))

    def set_pos(self, relative_pos):
        """Set node position relative to parent.

        relative_pos (2-tuple of integers or list with 2 integers)
            Contains x and y distance of this node relative
            to the parent, center to center.
        """
        ### try moving the rect center to the moved center
        ### of the parent
        try:
            self.rect.center = self.parent.rect.move(relative_pos).center

        ### if parent is None (an attribute error will be
        ### raised trying to access 'rect') check if rect
        ### needs to be offset relative to col_rect
        except AttributeError:

            ## try offseting rect relative to collision rect

            try:

                # invert collision rect offset
                inverted_pos = invert_point(self.col_rect_offset, True, True)

                # offset rect
                self.rect.center = self.col_rect.move(inverted_pos).center

            ## do nothing if inexistence of col_rect_offset
            ## attribute causes an error
            except AttributeError:
                pass

        ### if everything went ok, we just
        ### check if col_rect needs to be positioned
        else:

            ## try positioning col_rect relative to rect.

            try:
                self.col_rect.center = self.rect.move(self.col_rect_offset).center

            ## do nothing if inexistence of col_rect_offset
            ## attribute causes and error
            except AttributeError:
                pass

    def get_distance_from_parent(self):
        """Return 2-tuple of x and y distance from parent.

        The distance is measured between the center of the
        node's rect and parent's rect.
        """
        ### get the inverted center of parent

        inv_parent_center = invert_point(self.parent.rect.center, True, True)

        ### return the center of a rect obtained from
        ### moving the node rect towards the inverted
        ### coordinates of the parent's rect

        return self.rect.move(inv_parent_center).center
