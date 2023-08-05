"""Facility for common collision operations.

Those collision operations are usually abstractions of the
pygame.Rect class underlying methods.
"""

from ..config import SCREEN_RECT
from .autoblit import BlitterSet


# XXX
# Lots of changes to be expected here, specially
# regarding collisions

# XXX
# Proposal about collision handling:
# Each object would update its own collisions by checking,
# for instance, if an specific damaging rect inflicted
# damage on another object on the screen by asking said
# object whether it has a damageable rect colliding with
# the damaging rect. It could be flexible enough to
# allow for multiple kinds of collisions using rects, like
# checking for rect collisions or a radius reach, etc, etc.
# (I could describe it better)
# Ponder.


def does_touch_screen(obj):
    """Return True if obj touches screen.

    obj
        Any gaming obj.
    """
    if SCREEN_RECT.colliderect(obj.rect):
        return True
    else:
        return False


def get_objs_onscreen(group):
    """Return all objs which touch the screen.

    group
        A appcommon.autoblit.BlitterSet object.
    """
    onscreen = BlitterSet()
    for obj in group:
        if does_touch_screen(obj):
            onscreen.add(obj)
    return onscreen
