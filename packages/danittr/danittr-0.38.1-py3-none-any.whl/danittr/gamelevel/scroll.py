"""Facility for GameLevel class tools."""

from pygame import Rect

from ..config import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_RECT
from ..appcommon.surf import render_rect
from ..appcommon.autoblit import BlitterSet
from ..palette import WHITE


class ScrollBarrier(object):
    """A barrier to trigger scrolling when touching player."""

    def __init__(self, rect, scroll_command):
        """Initialize superclass and perform setup."""
        self.invoke = scroll_command

        self.rect = rect
        self.image = render_rect(*self.rect.size, color=WHITE)

    def update(self):
        """Update object state."""
        SCREEN.blit(self.image, self.rect)


def set_scroll_handles(level):
    """Set level handles for scrolling.

    level
        Instance of gamelevel.main.Level.
    """
    vertical_handle_width = horiz_handle_height = 10

    ## left
    left_rect = Rect((0, 0), (vertical_handle_width, SCREEN_HEIGHT))
    left_rect.midleft = SCREEN_RECT.midleft
    left_barrier = ScrollBarrier(left_rect, level.scroll_left)

    ## right
    right_rect = Rect((0, 0), (vertical_handle_width, SCREEN_HEIGHT))
    right_rect.midright = SCREEN_RECT.midright
    right_barrier = ScrollBarrier(right_rect, level.scroll_right)

    ## upper
    upper_rect = Rect((0, 0), (SCREEN_WIDTH, horiz_handle_height))
    upper_rect.midtop = SCREEN_RECT.midtop
    upper_barrier = ScrollBarrier(upper_rect, level.scroll_up)

    ## lower
    lower_rect = Rect((0, 0), (SCREEN_WIDTH, horiz_handle_height))
    lower_rect.midbottom = SCREEN_RECT.midbottom
    lower_barrier = ScrollBarrier(lower_rect, level.scroll_down)

    ## Setups
    level.scroll_barriers = BlitterSet(
        [left_barrier, right_barrier, upper_barrier, lower_barrier]
    )

    level.horizontal_barriers = BlitterSet([left_barrier, right_barrier])

    level.vertical_barriers = BlitterSet([upper_barrier, lower_barrier])
