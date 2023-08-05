"""Tools to improve styles."""

from pygame.draw import line as draw_line

from ..palette import HIGHLIGHT, SHADOW, BLACK


def give_depth_finish(surf, highlight_color=HIGHLIGHT, shadow_color=SHADOW):
    """Give a subtle finish which conveys depth.

    surf
        Instance of pygame.Surface.
    highlight_color
    shadow_color
        Tuple containing three integers representing
        red, green and blue values from 0 to 255.
        Used for highlights and shadows respectively.
    """
    width, height = surf.get_size()

    start = (0, 0)
    end = (width, 0)
    draw_line(surf, highlight_color, start, end, 1)

    start = (0, 0)
    end = (0, height)
    draw_line(surf, highlight_color, start, end, 1)

    start = (0, height - 1)
    end = (width - 1, height - 1)
    draw_line(surf, shadow_color, start, end, 1)

    start = (width - 1, 0)
    end = (width - 1, height - 1)
    draw_line(surf, shadow_color, start, end, 1)

    return surf
