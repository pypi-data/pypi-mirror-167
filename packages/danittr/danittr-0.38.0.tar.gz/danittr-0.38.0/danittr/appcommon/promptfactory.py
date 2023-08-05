"""Facility for prompt generation."""

from math import pi

### third-party imports

from pygame import Rect
from pygame.draw import (
    rect as draw_rect,
    circle as draw_circle,
    line as draw_line,
    arc as draw_arc,
    polygon as draw_polygon,
)

### local imports

from ..palette import BLACK, ARBITRARY_COLORKEY, PROMPT_BACKGROUND, has_same_rgb
from .surf import render_rect
from .text.main import render_text


def prompt_factory(
    prompt_text, object_pos, item_list, background_color=PROMPT_BACKGROUND
):
    """Return a list of interlocutor/surface pairs.

    ### ASCII art: generated surfaces take this final form:
    # obs.: + and * represent the area of different surfaces
    # that are drawn bellow the prompt text.
     _____________     __________________________
    (             )   (                          )
    | Want, this? |   | Should I take the items? |
    | +++         |   | +++  ***                 |
    | +++         |   | +++  ***                 |
    (_____________)   (__________________________)

    Notice the width and height are
    automatically adjusted to comprise the text surface
    and item surfaces.

    prompt_text
        A string representing the text of the prompt.

    object_pos
        Position of object generating the prompt.

    item_list
        List of surfaces representing the items offered
        in the prompt.

    background_color
        A tuple or list of r, g, b values which are
        integers ranging from 0 to 255. This color will
        be in several pygame.draw drawing calls.

        Though this function wasn't intended to be used
        in this way an optional alpha value within the
        same range can also be provided in the tuple
        or list, and the purpose of this can be read
        in the link bellow:
        https://www.pygame.org/docs/ref/draw.html

        Here's the specific excerpt:
        "Most of the arguments accept a color argument
        that is an RGB triplet. These can also accept
        an RGBA quadruplet. The alpha value will be
        written directly into the Surface if it contains
        pixel alphas, but the draw function will not draw
        transparently. The color argument can also be an
        integer pixel value that is already mapped to the
        Surface's pixel format."
    """
    if has_same_rgb(background_color, ARBITRARY_COLORKEY):
        msg = "'background_color' can't be equal to" + " 'ARBITRARY_COLORKEY' constant."
        raise ValueError(msg)

    bg_color = PROMPT_BACKGROUND
    common_width = 4

    ### Preparation to create initial surf to use as canvas

    line_str = prompt_text
    interlocutor_pos = object_pos

    text_surf = render_text(line_str, font_size=22, foreground_color=BLACK, padding=0)
    text_surf_height = text_surf.get_height()

    total_width = 0
    for item in item_list:
        total_width += item.get_width()

    box_width = (max(total_width, text_surf.get_width())) + 40

    # pygame don't handle lambdas well, so using this instead
    def get_height(item):
        """Return item height."""

    box_height = (
        max(item_list, key=get_height).get_height() + text_surf.get_height() + 20
    )

    surf = render_rect(box_width, box_height)
    surf.fill(ARBITRARY_COLORKEY)

    ### Prompt box volume (blocking)

    ## 02 rects
    # width and height depend on text and item surfaces
    # inside
    #
    #    rect1
    # |---------------|
    #     _________      _
    #  __|         |__   |
    # |__           __|  |  rect2
    #    |_________|     |
    #
    #
    hrect = Rect((0, 20), (box_width, box_height - 40))
    vrect = Rect((20, 0), (box_width - 40, box_height))
    draw_rect(surf, bg_color, hrect)
    draw_rect(surf, bg_color, vrect)

    ## 04 circles
    #
    # tlpos _________ trpos
    #    __.         .__
    #   |__.         .__|
    # blpos|_________| brpos
    #
    # each point above represents the center where
    # the circles will be drawn. This way it'll appear
    # that the box has round edges.
    #
    # Also, in next code blocks,
    # tl means topleft, tr means topright,
    # bl means bottomleft and  br means bottomright.
    tlpos, trpos, blpos, brpos = (
        (20, 20),
        (box_width - 20, 20),
        (20, box_height - 20),
        (box_width - 20, box_height - 20),
    )
    radius = 20
    draw_circle(surf, bg_color, tlpos, radius)
    draw_circle(surf, bg_color, trpos, radius)
    draw_circle(surf, bg_color, blpos, radius)
    draw_circle(surf, bg_color, brpos, radius)

    ### Prompt box outlines and final touches

    ## 04 arcs
    # will be drawn around the round corners of the
    # volume
    tl_arc_rect, bl_arc_rect, tr_arc_rect, br_arc_rect = (
        Rect((0, 0), (40, 40)),
        Rect((0, box_height - 40), (40, 40)),
        Rect((box_width - 41, 0), (40, 40)),
        Rect((box_width - 40, box_height - 40), (40, 40)),
    )

    startangle1, startangle2, startangle3, startangle4 = pi / 2, pi, 0, (3 * pi) / 2

    endangle1, endangle2, endangle3, endangle4 = pi, (3 * pi) / 2, pi / 2, 0

    draw_arc(surf, BLACK, tl_arc_rect, startangle1, endangle1, common_width)
    draw_arc(surf, BLACK, bl_arc_rect, startangle2, endangle2, common_width)
    draw_arc(surf, BLACK, tr_arc_rect, startangle3, endangle3, common_width)
    draw_arc(surf, BLACK, br_arc_rect, startangle4, endangle4, common_width)

    # eliminating artifacts in the drawn arcs
    for i in range(3):
        tl_arc_rect.y += 1
        draw_arc(surf, BLACK, tl_arc_rect, startangle1, endangle1, 1)
    for i in range(2):
        tl_arc_rect.x += 1
        draw_arc(surf, BLACK, tl_arc_rect, startangle1, endangle1, 1)

    for i in range(3):
        bl_arc_rect.y += -1
        draw_arc(surf, BLACK, bl_arc_rect, startangle2, endangle2, 1)
    for i in range(2):
        bl_arc_rect.x += 1
        draw_arc(surf, BLACK, bl_arc_rect, startangle2, endangle2, 1)

    for i in range(3):
        tr_arc_rect.y += 1
        draw_arc(surf, BLACK, tr_arc_rect, startangle3, endangle3, 1)
    for i in range(2):
        tr_arc_rect.x += -1
        draw_arc(surf, BLACK, tr_arc_rect, startangle3, endangle3, 1)
    tr_arc_rect.x += 3
    draw_arc(surf, BLACK, tr_arc_rect, startangle3, endangle3, 1)
    tr_arc_rect.y -= 3
    draw_arc(surf, BLACK, tr_arc_rect, startangle3, endangle3, 1)

    for i in range(3):
        br_arc_rect.y += -1
        draw_arc(surf, BLACK, br_arc_rect, startangle4, endangle4, 1)
    for i in range(2):
        br_arc_rect.x += -1
        draw_arc(surf, BLACK, br_arc_rect, startangle4, endangle4, 1)

    ## 04 lines
    # will be drawn to outline the straight sections
    # of the volume
    #
    # in the end, the box will be more or less like
    # this:
    #  _______________
    # (               )
    # |               |
    # (_______________)
    #
    start1, end1 = (20, 1), (box_width - 20, 1)
    start2, end2 = ((19, box_height - 3), (box_width - 20, box_height - 3))
    start3, end3 = (1, 19), (1, box_height - 22)
    start4, end4 = ((box_width - 3, 20), (box_width - 3, box_height - 21))
    draw_line(surf, BLACK, start1, end1, common_width)
    draw_line(surf, BLACK, start2, end2, common_width)
    draw_line(surf, BLACK, start3, end3, common_width)
    draw_line(surf, BLACK, start4, end4, common_width)

    ### Blitting the text and making other adjustments

    surf.blit(text_surf, (19, 8))

    # blitting the item surfaces
    x = 19
    for item in item_list:
        surf.blit(item, (x, text_surf_height + 10))
        x += item.get_width()

    # Making everything else outside box volume transparent
    surf.set_colorkey(ARBITRARY_COLORKEY)

    prompt_pair = (interlocutor_pos, surf)

    return prompt_pair
