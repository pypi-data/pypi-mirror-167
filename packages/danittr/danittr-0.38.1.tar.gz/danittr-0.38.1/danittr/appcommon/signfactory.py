"""Facility for sign surface generation."""

from pygame import Rect
from pygame.draw import rect as draw_rect, polygon as draw_polygon

from ..palette import BLACK, ARBITRARY_COLORKEY, SIGN_POLE_COLOR, has_same_rgb
from .surf import render_rect
from .text.main import render_text


# XXX
# art: make signs just a bit more smaller,
# to be more proportional to the player
# and npcs bodies.

# XXX
# Make the box adjust height too,
# so you're able to change font size
# and the box would adjust  accordingly.
# Use a fixture for that. Then maybe
# feature toggle. Signs could use surfaces
# too.


def sign_factory(text, fg_color, bg_color, signpost_height=0, direction=None):
    """Return a sign or signpost surface.

    text
        A string representing the message on the sign.

    fg_color
    bg_color
        A tuple or list of r, g, b values which are
        integers ranging from 0 to 255. This color will
        be in several pygame.draw drawing calls.

        fg_color defines the foreground color while
        bg_color defines the background color.

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

    signpost_height (defaults to 0)
        An integer describing the height of a pole to
        support the sign, if you want one. If not provided
        or 0 (the default), the sign won't have a post and
        it will be as if it were put on the wall.

    direction (defaults to None)
        If None the sign will be a rectangle. If one
        of ('n', 's', 'e' or 'w') is provided than
        the sign will be an arrow pointing in the
        specified direction. 'n' stands for north,
        's' for south, 'e' for east and 'w' for west.
    """

    # about function below:
    #
    # generated surfaces take this final form:
    #
    #    rectangular,            arrow-shaped,
    #        no post                  no post
    #                                             |\
    #     _______________      ___________________| \
    #    |               |    |                      \
    #    |               |    |                       \
    #    | Factory exit  |    | City entrance ahead    .
    #    |               |    |                       /
    #    |_______________|    |____________________  /
    #                                             | /
    #                                             |/
    #
    #     rectangular,           arrow-shaped,
    #        has post                has post     |\
    #     _______________      ___________________| \
    #    |               |    |                      \
    #    |               |    |                       \
    #    | Fancy lodging |    | Frozen waterfalls II   .
    #    |               |    |                       /
    #    |_______________|    |____________________  /
    #           |  |                   |  |       | /
    #           |  |                   |  |       |/
    #           |  |                   |  |
    #           |__|                   |__|
    #
    #    Notice the length is automatically adjusted to
    #    comprise the text surface. The sign can take a
    #    rectangular form or be shaped like an arrow pointing
    #    into specific directions. The sign can have an optional
    #    post.

    if has_same_rgb(fg_color, ARBITRARY_COLORKEY):
        msg = "'fg_color' can't be equal to" + " 'ARBITRARY_COLORKEY' constant."
        raise ValueError(msg)
    elif has_same_rgb(bg_color, ARBITRARY_COLORKEY):
        msg = "'bg_color' can't be equal to" + " 'ARBITRARY_COLORKEY' constant."
        raise ValueError(msg)

    directions = ("n", "s", "e", "w")
    if direction not in directions:
        shape = "rectangular"
    else:
        shape = "arrow"

    text_surf = render_text(text, font_size=22, foreground_color=fg_color, padding=0)

    text_width = text_surf.get_size()[0]

    if shape == "rectangular":
        sign_surf = render_rect(text_width + 20, 35)
        sign_surf.fill(bg_color)

        outline_rect = sign_surf.get_rect()
        outline_rect.width += -1
        outline_rect.height += -1
        draw_rect(sign_surf, BLACK, outline_rect, 4)

        sign_surf.blit(text_surf, (10, 3))
        sign_surf_width, sign_surf_height = sign_surf.get_size()

        if not signpost_height:
            offset = 5
            holder_surf = render_rect(
                sign_surf_width + offset, sign_surf_height + offset
            )
            holder_surf.fill(ARBITRARY_COLORKEY)

            shadow_rect = sign_surf.get_rect()
            shadow_rect.x += offset
            shadow_rect.y += offset
            draw_rect(holder_surf, BLACK, shadow_rect, 0)

            holder_surf.blit(sign_surf, (0, 0))

            # this eliminates an artifact
            final_touch_rect = Rect((sign_surf_width - 2, sign_surf_height - 2), (4, 4))
            draw_rect(holder_surf, BLACK, final_touch_rect, 0)

        elif signpost_height:
            height_offset = sign_surf_height + 20
            signpost_offset_height = signpost_height + height_offset
            pole_width = 18
            pole_surf = render_rect(pole_width, signpost_offset_height)
            pole_surf.fill(SIGN_POLE_COLOR)

            pole_outline_rect = pole_surf.get_rect()
            pole_outline_rect.width += -1
            pole_outline_rect.height += -1
            draw_rect(pole_surf, BLACK, pole_outline_rect, 4)

            triangle = [
                (0, height_offset),
                (40, height_offset),
                (40, height_offset + 40),
            ]
            draw_polygon(pole_surf, BLACK, triangle, 0)

            holder_surf = render_rect(sign_surf_width, signpost_offset_height)
            holder_surf.fill(ARBITRARY_COLORKEY)

            pole_x = round(sign_surf_width / 2) - round(pole_width / 2)
            holder_surf.blit(pole_surf, (pole_x, 0))
            holder_surf.blit(sign_surf, (0, 20))

    elif shape == "arrow":
        # arrow and its points
        #             . (f)
        #  (a)        |\
        #  ._ _ _ _ _.| \
        #  |        (g)  \
        #  |              \
        #  |               . (e)
        #  |              /
        #  ._ _ _ _ _ .  /
        #  (b)     (c)| /
        #             |/
        #             . (d)

        a, b = (0, 10), (0, 40)

        padx = 10
        padx_text_width = text_width + (padx * 2)
        c, g = ((padx_text_width, b[1]), (padx_text_width, a[1]))
        f, d = (g[0], 0), (c[0], c[1] + 10)

        x_distance_e_to_d = 25
        e = (c[0] + x_distance_e_to_d, a[1] + 15)

        arrow = [a, b, c, d, e, f, g]

        sign_surf = render_rect(e[0], d[1])
        sign_surf.fill(ARBITRARY_COLORKEY)

        draw_polygon(sign_surf, bg_color, arrow, 0)
        draw_polygon(sign_surf, BLACK, arrow, 3)

        if not signpost_height:
            shadow_surf = render_rect(*sign_surf.get_size())
            shadow_surf.fill(ARBITRARY_COLORKEY)
            draw_polygon(shadow_surf, BLACK, arrow, 0)
            shadow_surf.set_colorkey(ARBITRARY_COLORKEY)

        if direction == "e":
            sign_surf.blit(text_surf, (10, 10))

            if not signpost_height:
                offset = 5
                temp_width, temp_height = sign_surf.get_size()
                holder_surf = render_rect(temp_width + offset, temp_height + offset)
                holder_surf.fill(ARBITRARY_COLORKEY)
                sign_surf.set_colorkey(ARBITRARY_COLORKEY)
                holder_surf.blit(shadow_surf, (offset, offset))
                holder_surf.blit(sign_surf, (0, 0))

        elif direction == "w":
            sign_surf = flip(sign_surf, True, False)
            sign_surf.blit(text_surf, (60, 10))

            if not signpost_height:
                shadow_surf = flip(shadow_surf, True, False)
                offset = 5
                temp_width, temp_height = sign_surf.get_size()
                holder_surf = render_rect(temp_width + offset, temp_height + offset)
                holder_surf.fill(ARBITRARY_COLORKEY)
                sign_surf.set_colorkey(ARBITRARY_COLORKEY)
                holder_surf.blit(shadow_surf, (offset, offset))
                holder_surf.blit(sign_surf, (0, 0))

        elif direction in ("n", "s"):
            angle = 90 if direction == "n" else -90
            sign_surf.blit(text_surf, (10, 10))
            sign_surf = rotate(sign_surf, angle)

            if not signpost_height:
                shadow_surf = rotate(shadow_surf, angle)
                offset = 5
                temp_width, temp_height = sign_surf.get_size()
                holder_surf = render_rect(temp_width + offset, temp_height + offset)
                holder_surf.fill(ARBITRARY_COLORKEY)
                sign_surf.set_colorkey(ARBITRARY_COLORKEY)
                holder_surf.blit(shadow_surf, (offset, offset))
                holder_surf.blit(sign_surf, (0, 0))

        if signpost_height:
            sign_surf_width, sign_surf_height = sign_surf.get_size()
            height_offset = sign_surf_height
            signpost_offset_height = signpost_height + height_offset

            pole_width = 22
            pole_surf = render_rect(pole_width, signpost_offset_height)
            pole_surf.fill(SIGN_POLE_COLOR)

            pole_outline_rect = pole_surf.get_rect()
            pole_outline_rect.width += -1
            pole_outline_rect.height += -1

            # triangle used as a shadow cast on pole
            # just below the sign
            if direction in ("e", "w"):
                triangle = [
                    (0, height_offset - 10),
                    (40, height_offset - 10),
                    (40, height_offset + 30),
                ]
            elif direction == "n":
                triangle = [
                    (0, height_offset + 5),
                    (40, height_offset + 5),
                    (40, height_offset + 45),
                ]
            else:
                triangle = [
                    (0, height_offset - 25),
                    (40, height_offset - 25),
                    (40, height_offset + 15),
                ]

            draw_rect(pole_surf, BLACK, pole_outline_rect, 4)
            draw_polygon(pole_surf, BLACK, triangle, 0)

            holder_surf = render_rect(sign_surf_width, signpost_offset_height)
            holder_surf.fill(ARBITRARY_COLORKEY)

            pole_x = round(sign_surf_width / 2) - round(pole_width / 2)
            if direction == "e":
                pole_x += -10
            elif direction == "w":
                pole_x += 10

            holder_surf.blit(pole_surf, (pole_x, 0))
            sign_surf.set_colorkey(ARBITRARY_COLORKEY)
            holder_surf.blit(sign_surf, (0, 5))

    holder_surf.set_colorkey(ARBITRARY_COLORKEY)
    sign_surf = holder_surf

    return sign_surf
