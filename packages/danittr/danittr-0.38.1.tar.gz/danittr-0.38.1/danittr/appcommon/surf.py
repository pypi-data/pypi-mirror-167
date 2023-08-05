"""Facility for resource loading.

Functions and tools to easily create objects
and surfaces.
"""
from os.path import join

### third-party imports

from pygame import Surface
from pygame.image import load as load_image
from pygame.display import update

### local imports

from ..config import IMAGES_DIR, IMAGES_META_FILE

from ..common.jsonhandler import load_json
from .autoblit import BasicObject

from ..palette import BLACK


INVISIBLE_SURF = Surface((0, 0)).convert()

IMAGES_MAP = {}

IMAGE_NAME_TO_ALPHA_MAP = load_json(IMAGES_META_FILE)

### functions for general usage


def render_image(
    img_name, return_obj=False, coordinates_name="topleft", coordinates_value=(0, 0)
):
    """Return a surface or object representing an image.

    img_name (string)
        The basename of an image to be loaded.
    return_obj (boolean)
        Boolean indicating whether or not a
        appcommon.autoblit.BasicObject instance should be
        returned. Default is False, and causes a
        pygame.Surface instance to be returned instead.
        In case this parameter is True, the coordinates_name
        and coordinates_value parameters are used.
    coordinates_name
        A string specifying which of the rect attributes
        should be used to assign the coordinates value.
    coordinates_value
        A 2-tuple of integers representing a point to be
        assigned to one of the rects coordinates.
    """
    try:
        surf = IMAGES_MAP[img_name]

    except KeyError:

        ### join dir and image name and convert to string to
        ### form path
        img_path = join(IMAGES_DIR, img_name)

        ### load surface using appropriate method according
        ### to presence of per pixel alphas
        if IMAGE_NAME_TO_ALPHA_MAP[img_name]:
            surf_method = Surface.convert_alpha

        else:
            surf_method = Surface.convert

        surf = surf_method(load_image(img_path))

        IMAGES_MAP[img_name] = surf

    ### return either the surface or a customized object
    ### containing it

    if return_obj:

        ## instantiate object and set its attributes

        obj = BasicObject()
        obj.image = surf
        obj.rect = obj.image.get_rect()

        ## position its rect
        setattr(obj.rect, coordinates_name, coordinates_value)

        return obj

    else:
        return surf


def render_rect(
    width,
    height,
    color=BLACK,
    return_obj=False,
    coordinates_name="topleft",
    coordinates_value=(0, 0),
):
    """Return surface or object representing a filled rect.

    width
        Int indicating the desired width of the generated
        surface.
    height
        Int indicating the desired height of the generated
        surface.
    color
        A tuple or list of r, g, b values which are
        integers ranging from 0 to 255. Used to fill the
        generated surface. An optional fourth value can be
        passed, which is an integer in the same range as the
        others, representing the image opacity (0 for full
        transparency and 255 for full opacity).
    return_obj
        Boolean indicating whether or not a
        appcommon.autoblit.BasicObject instance should be
        returned. Default is False, and causes a
        pygame.Surface instance to be returned instead.
        In case this parameter is True, the coordinates_name
        and coordinates_value parameters are used.
    coordinates_name
        A string specifying which of the rect attributes
        should be used to assign the coordinates value.
    coordinates_value
        A 2-tuple of integers representing a point to be
        assigned to one of the rects coordinates.
    """
    ### instantiate surface taking transparency into account

    try:
        has_transparency = color[3] < 255
    except IndexError:
        has_transparency = False
    finally:

        if has_transparency:
            surf = Surface((width, height)).convert_alpha()

        else:
            surf = Surface((width, height)).convert()

    surf.fill(color)

    ### return either the surface or a customized object
    ### containing it

    if return_obj:

        ## instantiate object and set its attributes

        obj = BasicObject()
        obj.image = surf
        obj.rect = obj.image.get_rect()

        ## position its rect
        setattr(obj.rect, coordinates_name, coordinates_value)

        return obj

    else:
        return surf


# XXX maybe raise a ValueError if at least one dimension
# of the original surf is larger than the required
# dimensions? Ponder.
def enlarge_surf(surf, width, height, background_color=(*BLACK, 0)):
    """Blit current surf on bigger one to enlarge it.

    width
        Int indicating the final desired width of the
        generated surface.
    height
        Int indicating the final desired height of the
        generated surface.
    background_color
        A tuple or list of r, g, b values which are
        integers ranging from 0 to 255. Used to fill the
        generated surface.
    """
    ### instantiate surface taking transparency into account

    ## alias background color
    bg_color = background_color

    try:
        has_transparency = bg_color[3] < 255

    except IndexError:
        has_transparency = False

    finally:

        if has_transparency:
            bg_surf = Surface((width, height)).convert_alpha()

        else:
            bg_surf = Surface((width, height)).convert()

    bg_surf.fill(bg_color)

    bg_surf.blit(surf, (0, 0))

    return bg_surf


## XXX
## About using colorkey:
## Ideally, all images that need transparency
## would use colorkey, but though its technically
## good, it is artistically/aesthetically bad
## for what I want to achieve, because edges
## become jagged/serrated. Maybe I'll find a
## workaround in the future.
