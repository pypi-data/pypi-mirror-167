"""Facility for simple object display."""

from functools import partialmethod

### local imports

from ..config import SCREEN_RECT

from ..common.behaviour import empty_function

from ..appcommon.surf import INVISIBLE_SURF, render_image
from ..appcommon.autoblit import BasicObject

from .proc import process_tasks


class SimpleObject(BasicObject):
    """Simple object to hold sprite."""

    def __init__(
        self, image_name, tasks, exchange_pos_attrs=("center", "center"), offset=(0, 0)
    ):
        """Create attributes."""
        ### store a loaded image attribute and also
        ### reference it on the self.image attribute

        self.image = self.loaded_image = render_image(image_name)

        ### create, store and position a pygame.Rect
        ### instance from the surface referenced on the
        ### image attribute

        ## create and store rect
        self.rect = self.image.get_rect()

        ## position it

        rect_attr, screen_rect_attr = exchange_pos_attrs

        screen_pos = getattr(SCREEN_RECT, screen_rect_attr)

        setattr(self.rect, rect_attr, screen_pos)

        # offset if requested
        self.rect.move_ip(offset)

        self.visibility_off()

        ### define update behaviour
        self.update = empty_function

        ### process tasks
        process_tasks(self, tasks)

    def change_visibility(self, visible=True):
        """Turn the object invisible."""
        if visible:
            self.image = self.loaded_image
        else:
            self.image = INVISIBLE_SURF

    visibility_on = partialmethod(change_visibility, True)
    visibility_off = partialmethod(change_visibility, False)
