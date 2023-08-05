"""A head sprite to represent the pc."""

### local imports

from ..common.behaviour import empty_function
from ..appcommon.autoblit import BasicObject
from ..appcommon.surf import render_image


class Head(BasicObject):
    """A player's head featured alongside healthbar."""

    def __init__(self):
        """Initialize superclass and set variables."""
        self.image = render_image("dani_head.png")

        self.rect = self.image.get_rect()
        self.rect.topleft = (30, 30)

        self.update = empty_function
