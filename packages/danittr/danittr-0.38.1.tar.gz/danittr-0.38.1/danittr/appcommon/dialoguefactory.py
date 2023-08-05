"""Facility for dialogue generation."""

from math import pi

### third-party imports

from pygame import Rect
from pygame.draw import rect as draw_rect
from pygame.draw import circle as draw_circle
from pygame.draw import line as draw_line
from pygame.draw import arc as draw_arc
from pygame.draw import polygon as draw_polygon

### local imports

from ..palette import BLACK, ARBITRARY_COLORKEY, DIALOGUEBOX_BACKGROUND, has_same_rgb
from .surf import render_rect
from .text.main import render_text


# XXX
# Make the box adjust height too,
# so you're able to change font size
# and the box would adjust  accordingly.
# Use a fixture for that. Then maybe
# feature toggle.


def dialoguebox_factory(
    dialogue, object_pos=None, background_color=DIALOGUEBOX_BACKGROUND
):
    """Return a list of interlocutor/surface pairs.

    ### ASCII art: generated surfaces take this final form:
     _______________     ____________________
    (               )   (                    )
    | Hello, world! |   | Hello, world! Bye! |
    (______  _______)   (_________  _________)
           \/                     \/

    Notice the length is automatically adjusted to
    comprise the text surface.

    dialogue
        A list of dicts. Each dict contains a single field
        which specifies the interlocutor and whose values
        consists of its spoken line.

    object_pos (defaults to None)
        Position of interlocutor when it isn't the pc.

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
    if object_pos is None:
        for line in dialogue:
            for key in line:
                if key != "player":
                    msg = (
                        "object_pos must be provided "
                        + "an interlocutor other than "
                        + "player speaks."
                    )
                    raise ValueError(msg)

    if has_same_rgb(background_color, ARBITRARY_COLORKEY):
        msg = "'background_color' can't be equal to" + " 'ARBITRARY_COLORKEY' constant."
        raise ValueError(msg)

    bg_color = background_color
    common_width = 4

    dialogue_boxes = []
    for textline in dialogue:
        ### Initial surf to be used as a canvas
        interlocutor, line_str = textline.copy().popitem()

        if interlocutor == "self":
            interlocutor_pos = object_pos
        else:
            interlocutor_pos = "player_pos"

        text_surf = render_text(
            line_str, font_size=22, foreground_color=BLACK, padding=0
        )

        box_width = text_surf.get_size()[0] + 40

        surf = render_rect(box_width, 65)
        surf.fill(ARBITRARY_COLORKEY)

        ### Dialoguebox volume (blocking)

        ## 02 rects
        #
        #    rect1
        # |---------------|
        #     _________      _
        #  __|         |__   |
        # |__           __|  |  rect2
        #    |_________|     |
        #
        #
        rect1 = Rect((0, 20), (box_width, 5))
        rect2 = Rect((20, 0), (box_width - 40, 45))
        draw_rect(surf, bg_color, rect1)
        draw_rect(surf, bg_color, rect2)

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
            (20, 25),
            (box_width - 20, 25),
        )
        radius = 20
        draw_circle(surf, bg_color, tlpos, radius)
        draw_circle(surf, bg_color, trpos, radius)
        draw_circle(surf, bg_color, blpos, radius)
        draw_circle(surf, bg_color, brpos, radius)

        ### Dialogue box outlines and final touches

        # 04 arc
        # will be drawn around the round corners of the
        # volume
        arc_rect1 = Rect((0, 0), (40, 40))
        arc_rect2 = Rect((0, 8), (40, 40))
        arc_rect3 = Rect((box_width - 41, 0), (40, 40))
        arc_rect4 = Rect((box_width - 40, 8), (40, 40))

        startangle1, startangle2, startangle3, startangle4 = pi / 2, pi, 0, (3 * pi) / 2

        endangle1, endangle2, endangle3, endangle4 = pi, (3 * pi) / 2, pi / 2, 0

        draw_arc(surf, BLACK, arc_rect1, startangle1, endangle1, common_width)
        draw_arc(surf, BLACK, arc_rect2, startangle2, endangle2, common_width)
        draw_arc(surf, BLACK, arc_rect3, startangle3, endangle3, common_width)
        draw_arc(surf, BLACK, arc_rect4, startangle4, endangle4, common_width)

        # eliminating artifacts in the drawn arcs
        square = Rect((box_width - 22, 48), (4, 4))
        draw_rect(surf, ARBITRARY_COLORKEY, square)

        for i in range(3):
            arc_rect1.y += 1
            draw_arc(surf, BLACK, arc_rect1, startangle1, endangle1, 1)
        for i in range(2):
            arc_rect1.x += 1
            draw_arc(surf, BLACK, arc_rect1, startangle1, endangle1, 1)

        for i in range(3):
            arc_rect2.y += -1
            draw_arc(surf, BLACK, arc_rect2, startangle2, endangle2, 1)
        for i in range(2):
            arc_rect2.x += 1
            draw_arc(surf, BLACK, arc_rect2, startangle2, endangle2, 1)

        for i in range(3):
            arc_rect3.y += 1
            draw_arc(surf, BLACK, arc_rect3, startangle3, endangle3, 1)
        for i in range(2):
            arc_rect3.x += -1
            draw_arc(surf, BLACK, arc_rect3, startangle3, endangle3, 1)
        arc_rect3.x += 3
        draw_arc(surf, BLACK, arc_rect3, startangle3, endangle3, 1)
        arc_rect3.y -= 3
        draw_arc(surf, BLACK, arc_rect3, startangle3, endangle3, 1)

        for i in range(3):
            arc_rect4.y += -1
            draw_arc(surf, BLACK, arc_rect4, startangle4, endangle4, 1)
        for i in range(2):
            arc_rect4.x += -1
            draw_arc(surf, BLACK, arc_rect4, startangle4, endangle4, 1)

        # 04 lines
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
        start2, end2 = (19, 45), (box_width - 20, 45)
        start3, end3 = (1, 19), (1, 27)
        start4, end4 = (box_width - 3, 20), (box_width - 3, 27)
        draw_line(surf, BLACK, start1, end1, common_width)
        draw_line(surf, BLACK, start2, end2, common_width)
        draw_line(surf, BLACK, start3, end3, common_width)
        draw_line(surf, BLACK, start4, end4, common_width)

        # triangle
        #  _______________
        # (               )
        # |               |
        # (______  _______)
        #        \/ <--this triangle here
        #
        # It will be drawn over the outline of the volume
        # so that it appear to be part of the box.
        mid = round(box_width / 2)
        pointlist = ((mid, 64), (mid - 20, 44), (mid + 20, 44))
        draw_polygon(surf, bg_color, pointlist)

        # then we outline the part of the triangle
        # outside the volume
        start1, end1 = (mid - 20, 44), (mid, 64)
        start2, end2 = (mid + 20, 44), (mid, 64)
        draw_line(surf, BLACK, start1, end1, common_width)
        draw_line(surf, BLACK, start2, end2, common_width)

        ### Blitting the text and making other adjustments

        surf.blit(text_surf, (19, 8))

        # Making everything else outside box transparent
        surf.set_colorkey(ARBITRARY_COLORKEY)

        dialogue_pair = (interlocutor_pos, surf)
        dialogue_boxes.append(dialogue_pair)

    return dialogue_boxes


# XXX
# Ideas for improvement:
# - I don't know if the circle drawing algorithm generate the
#   same noise the arcs generate when using thick lines, if
#   if they don't, then arcs could be produced from circles
#   with some parts hidden by 'colorkeyed' areas.
