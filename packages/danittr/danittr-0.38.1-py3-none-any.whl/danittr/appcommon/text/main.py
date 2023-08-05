"""Facility for text related utilities."""

### third-party imports
from pygame import Surface

### local imports

from ..autoblit import BasicObject
from ...palette import BLACK
from ...font import get_font


# XXX maybe create a BasicObject subclass with extra
# text processing capabilities, like auto update its
# image attribute; there's already at least one or two
# cases where this would be useful.


def get_text_size(text, font_size=22, font_style="default", padding=5):
    """Return surf size of text as if it were rendered.

    text
        Any string.
    font_size
        Integer indicating desired font size.
    font_style
        String. Either 'default' for default font or
        'mono' for monospace font.
    padding
        The horizontal and vertical padding for the text
        in pixels.
    """
    font = get_font(font_size, font_style)
    width, height = font.size(text)
    increment = 2 * padding
    padded_size = width + increment, height + increment
    return padded_size


def fit_text(text, font, max_width, ommit_direction):
    """Return optimal text to fit max_width passed."""
    ### if text as it fits width, then return earlier
    if not font.size(text)[0] > max_width:
        return text

    if ommit_direction == "left":
        slice_obj = slice(1, None)
    else:
        slice_obj = slice(None, -1)

    for _ in range(len(text)):
        text = text[slice_obj]
        if not font.size(text)[0] > max_width:
            break

    if ommit_direction == "left":
        text = "..." + text[3:]
    else:
        text = text[:-3] + "..."

    return text


def render_text(
    text,
    font_size=22,
    foreground_color=BLACK,
    background_color=(*BLACK, 0),
    antialiased=True,
    font_style="default",
    padding=5,
    max_width=0,
    ommit_direction="right",
    return_obj=False,
    coordinates_name="topleft",
    coordinates_value=(0, 0),
):
    """Return surface or object representing rendered text.

    text
        Any string.
    font_size
        Integer indicating desired font size.
    foreground_color
    background_color
        A tuple or list of r, g, b values which are
        integers ranging from 0 to 255. The background
        color can be None, though, in which case the
        background is rendered transparent. For the
        background color, an optional fourth value can
        be passed, which is an integer in the same range
        as the others, representing the image opacity (0 for
        full transparency and 255 for full opacity).
    antialiased
        Boolean indicating whether or not the text on
        the surface should be antialiased.
    font_style
        String. Either 'default' for default font or
        'mono' for monospace font.
    padding
        The horizontal and vertical padding for the text
        in pixels.
    max_width
        If provided, the text surf won't assume a width
        larger than max width.
    ommit_direction
        Part of the text to ommit in case its width surpass
        the max_width (if applicable).
    return_obj
        Boolean indicating whether or not a
        appcommon.autoblit.BasicObject instance should be
        returned. Default is False, and causes a
        pygame.Surface instance to be returned instead.
        In case this parameter is True, the coordinates_name
        and coordinates_value parameters are used.
    coordinates_name
        String representing attribute name of rect wherein
        to store the position information from the
        coordinates value parameter.
    coordinates_value
        Position information in the form of a tuple or list
        containing 2 integers representing positions
        in the x and y axes, respectively.
    """
    font = get_font(font_size, font_style)

    if max_width:
        max_width = abs(max_width)
        text = fit_text(text, font, max_width, ommit_direction)

    ### define background alpha for next operations

    try:
        has_transparency = background_color[3] < 255
    except IndexError:
        has_transparency = False

    ### render and adjust text surface according to
    ### background alpha

    text_surf = font.render(text, antialiased, foreground_color).convert_alpha()

    if has_transparency:

        bg = Surface(text_surf.get_size()).convert_alpha()
        bg.fill(background_color)
        bg.blit(text_surf, (0, 0))
        surf = bg

    else:
        surf = font.render(
            text, antialiased, foreground_color, background_color
        ).convert()

    ### apply padding if requested

    if padding:

        padding = abs(padding)

        ## calculate final width
        width, height = surf.get_size()
        new_width, new_height = (width + (2 * padding), height + (2 * padding))

        ## create new background surface with appropriate
        ## color according to presence of transparency
        if has_transparency:
            new_bg = Surface((new_width, new_height)).convert_alpha()

        else:
            new_bg = Surface((new_width, new_height)).convert()

        new_bg.fill(background_color)

        ## blit text on new background and reference as
        ## surf surf

        new_bg.blit(text_surf, (padding, padding))
        surf = new_bg

    if return_obj:
        obj = BasicObject()
        obj.image = surf

        obj.rect = obj.image.get_rect()
        setattr(obj.rect, coordinates_name, coordinates_value)

        return obj

    else:
        return surf


def get_str_slices(text, font_size, max_width):
    """Return list of string complying with maximum width.

    The str provided is divided into slices which once
    rendered into text surfaces will comply with the
    maximum width requirement. The str slices are word
    wrapped.

    text
        Any string.
    font_size
        Integer indicating desired font size.
    max_width
        Integer representing maximum width in pixels the
        text surfaces would have if str slices were
        rendered.
    """
    ### create container and alias
    str_slices = []

    ### iterate over text, trimming out words until the
    ### remaining text fits the maximum width and is stored
    ### in str_slices list, then do the same with the
    ### trimmed out text until nothing is left.

    trimmed = ""
    while text:
        width, _ = get_text_size(text, font_size)

        ## if don't fit max width, trim text
        if width > max_width:

            ## trim last word from text and stack on 'trimmed'

            lsi = text.rfind(" ")  # lsi = last_space_index
            text, trimmed = text[:lsi], text[lsi:] + trimmed

        ## otherwise store text lstripped text
        ## and get trimmed text, if any;
        ## (when trimmed is empty, the loop will exit
        ## automatically)
        else:
            str_slices.append(text.lstrip())
            text, trimmed = trimmed, ""

    return str_slices
