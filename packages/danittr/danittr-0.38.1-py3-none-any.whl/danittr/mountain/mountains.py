"""Facility for parallax mountains."""

### local imports

from ..config import SCREEN_RECT
from ..common.behaviour import empty_function
from ..appcommon.autoblit import BasicObject
from ..appcommon.surf import render_image


# XXX
# maybe smooth the edges of the mountain.png image.


class Mountain(BasicObject):
    """Base class for mountains."""

    def __init__(self):
        """Position and perform setups.

        bottomleft
            Bottomleft coordinates for a pygame.Rect instance.
        """
        self.image = render_image("mountain.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = SCREEN_RECT.midbottom

        # 40: just an arbitrary value.
        # It means we can scroll down the screen
        # 10 times and the image still won't leave the
        # screen boundaries.
        self.rect.y += 40

        self.update = empty_function

    def scroll(self, dx, dy):
        """Scroll by dx and dy in respective axis.

        dx
            Integer indicating scrolling in x axis.
        dy
            Integer indicating scrolling in y axis.
        """
        self.rect.move_ip(dx / 160, dy / 180)
