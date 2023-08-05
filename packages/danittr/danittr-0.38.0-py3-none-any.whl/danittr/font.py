"""Facility to manage fonts."""

from os.path import join

### third-party imports

from pygame.font import Font
from pygame.font import init as init_font

### local imports

from .config import FONTS_DIR, FONTS_META_FILE
from .common.jsonhandler import load_json

init_font()

### create and process font path map

FONT_PATH_MAP = {
    "default": "source_sans_pro_regular.ttf",
}

for key, font_name in FONT_PATH_MAP.items():
    FONT_PATH_MAP[key] = join(FONTS_DIR, font_name)

### create a CHAR_CODE_MAP

## load fonts metadata
FONTS_META_MAP = load_json(FONTS_META_FILE)

## create map

CHAR_CODE_MAP = {
    font_key: FONTS_META_MAP[font_key] for font_key in FONT_PATH_MAP.keys()
}


### create a map to store commonly used font objects;
### that is, whenever a font object is created, it is stored
### for future usage, so no instantiation is required twice

FONT_MAP = {}

### utility function for general usage: getting fonts


def get_font(size, font_style="default"):
    """Return default font of specified size."""
    ### store arguments in tuple to use as a dictionary key
    key = (font_style, size)

    ### try returning font from font map using the key
    try:
        return FONT_MAP[key]

    ### otherwise create, store and return the new font obj
    except KeyError:

        ### retrieve font path
        font_path = FONT_PATH_MAP[font_style]

        ### instantiate font object
        font = Font(font_path, size)

        ### store it in the font map and return it

        FONT_MAP[key] = font
        return font
