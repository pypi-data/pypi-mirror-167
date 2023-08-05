"""Facility for single line updateable text object."""

from string import ascii_letters, digits, punctuation
from random import seed, choice

### third-party import
from pygame import Rect, error as pygame_error

### local imports

from ....common.behaviour import empty_function

from ...surf import render_rect
from ...autoblit import BasicObject
from ..main import render_text

from ....font import CHAR_CODE_MAP
from ....palette import BLACK

# TODO implement recent changes here and in the autolabel
# regarding the custom coordinates arguments and how they
# are automatically set in the __init__ and set methods
# of this label class in the respective classes from the
# animation editor; remember to take into account the
# auto position correction on update image when the labels
# are offset by hide switch objects (on the animation editor
# package)

seed()

###### constant definitions

CHAR_DATA_MAP = {}

COMMON_CHARS = ascii_letters + digits + punctuation + " " + "áàãâêéèẽîíìôóòõûúùñç"

##### utility functions


def safe_text_render(char, render_kwargs):
    """Render char with extra except clause for safety."""
    try:
        return render_text(char, padding=0, **render_kwargs)

    ### errors raised by pygame.font.Font.render:
    ### some values aren't accepted in pygame (they are
    ### called null values) and raise value errors (until
    ### now, only chr(0) caused this, maybe it's the only
    ### one?);
    ### a pygame error sometimes is also raised saying
    ### "Text has zero width" (until now, only chr(13)
    ### caused this, maybe it's the only one?);
    ### those problems vary depending on the font; such
    ### errors where actually found in another codebase;
    except (ValueError, pygame_error):
        pass


# XXX consider a better name for this function; it is
# difficult because it does many things, but at the same
# time I don't think the current name is appropriate;
def create_char_maps(render_kwargs, args_key):
    """Create and store maps for character data."""
    ### get available codes for the font used
    valid_codes = CHAR_CODE_MAP[render_kwargs["font_style"]]

    ### create surface map with commonly used chars if
    ### they are available in the font used; a width map
    ### with width of corresponding surfaces is also
    ### created;

    surf_map = {}
    width_map = {}

    for char in COMMON_CHARS:

        ## only consider char whose unicode value is within
        ## valid codes
        if ord(char) in valid_codes:

            ## then trying generating surf and filling the
            ## maps
            try:
                surf = safe_text_render(char, render_kwargs)

                width_map[char] = surf.get_width()
                surf_map[char] = surf

            ## if the surf wasn't generated, then the surf
            ## is None and will trigger an attribute error
            ## when trying to execute surf.get_width in the
            ## 'try' block, in which case the code for the
            ## char must be removed from the valid codes
            ## list
            except AttributeError:
                valid_codes.remove(ord(char))

    ### store maps and valid char codes list in the
    ### CHAR_DATA_MAP, referenced by the json configuration
    ### string
    CHAR_DATA_MAP[args_key] = (surf_map, width_map, valid_codes)


### class definition


class Label(BasicObject):
    """A text widget with automatic surface updating.

    It works similar to tkinter.Label objects since they
    can have text set and reset any time.
    """

    def __init__(
        self,
        text="",
        *,
        font_size=22,
        font_style="default",
        foreground_color=BLACK,
        background_color=(*BLACK, 0),
        coordinates_name="topleft",
        coordinates_value=(0, 0)
    ):
        """Perform setups and assign data for reuse.

        text
            string providing text to update surface.
        font_size
            Integer indicating desired font size.
        font_style
            String. Either 'default' for default font or
            'mono' for monospace font.
        foreground_color
        background_color
            A tuple or list of r, g, b values which are
            integers ranging from 0 to 255. The background
            color can be None, though, in which case the
            background is rendered transparent. For the
            background color, an optional fourth value can
            be passed, which is an integer in the same range
            as the others, representing the image opacity
            (0 for full transparency and 255 for full
            opacity).
        coordinates_name
            String representing attribute name of rect
            wherein to store the position information from
            the coordinates value parameter.
        coordinates_value
            Position information in the form of a tuple or
            list containing 2 integers representing
            positions in the x and y axes, respectively.
        """
        ### convert the colors passed into tuples for
        ### simplicity (since colors can appear in other
        ### classes like pygame.Color and builtin lists too)

        background_color = tuple(background_color)
        foreground_color = tuple(foreground_color)

        ### process the arguments so the data needed to
        ### manage the label is properly generated or
        ### retrieved

        ## the background is handled apart from the other
        ## arguments, so we just store it in its own
        ## attribute (since it is handled apart, notice we'll
        ## ommit it from the arguments in the next steps);
        self.bg_color = background_color

        ## the other arguments are gathered in a dict
        ## so they can be used as keyword arguments to
        ## render characters

        self.render_kwargs = {
            "font_size": font_size,
            "font_style": font_style,
            "foreground_color": foreground_color,
        }

        ## a tuple with the arguments is also created
        ## to be used as a key representing the specific
        ## combination of arguments; this way the data
        ## related to each different setting will never
        ## be generated more than once

        args_key = (font_size, font_style, foreground_color)

        ## the CHAR_DATA_MAP holds all the data needed to
        ## manage labels, for each different combination
        ## of arguments used;
        ## if said map lacks the data we need for our
        ## specific combination of arguments (the key we
        ## just put together), we create such data:
        if args_key not in CHAR_DATA_MAP:
            create_char_maps(self.render_kwargs, args_key)

        ## finally, we retrieve and assign the data we need
        ## from the CHAR_DATA_MAP using the key
        self.surf_map, self.width_map, self.valid_codes = CHAR_DATA_MAP[args_key]

        # TODO this step of storing the height shouldn't be
        # repeated every time an instance is created
        # (probably include it on the if block above)
        ### store the height of a random character
        self.height = choice(list(self.surf_map.values())).get_height()

        ### create and position rect

        self.rect = Rect((0, 0), (0, self.height))

        setattr(self.rect, coordinates_name, coordinates_value)

        ### also store the coordinate information

        self.coordinates_name = coordinates_name
        self.coordinates_value = coordinates_value

        ### create an attribute with a string to store the
        ### text of the label
        self.contents = ""

        ### add text the text passed as argument (this is also
        ### needed in order to create an image attribute and
        ### thus prevent errors)
        self.add_text(text)

        ### define update behaviour
        self.update = empty_function

    def get(self):
        """Return text content of widget."""
        return self.contents

    def set(self, text):
        """Set obj text.

        text (string)
            value to be used as label text.
        """
        ### return earlier if text is already set
        if text == self.contents:
            return

        ### otherwise "clear" contents and add text

        self.contents = ""
        self.add_text(text)

    def add_text(self, text):
        """Add text.

        text
            Any string obj.
        """
        ### only keep valid characters (present on map)
        filtered_text = "".join(list(filter(self.filter_char, text)))

        ### extend content with filtered text
        self.contents += filtered_text

        ### update image
        self.update_image()

    def filter_char(self, char):
        """Return True if a surf is available for char."""
        ### only proceed if code for char is valid
        ### (present on font)
        if ord(char) in self.valid_codes:

            ## if a surface was already generated for the
            ## char, them return True
            if char in self.surf_map:
                return True

            ## otherwise generate said surf and populate it
            ## the respective values in the surf map and
            ## width map
            else:

                # try generating surf and populating the
                # maps
                try:
                    surf = safe_text_render(char, self.render_kwargs)

                    self.width_map[char] = surf.get_width()
                    self.surf_map[char] = surf
                    return True

                # if the surf wasn't generated, then the
                # surf is None and will trigger an attribute
                # error when trying to execute
                # surf.get_width in the 'try' block, in
                # which case the code for the char must be
                # removed from the valid codes list
                except AttributeError:
                    self.valid_codes.remove(ord(char))

    def update_image(self):
        """Update image surface attribute."""
        ### create new surface for image attribute

        ## calculate width
        ## (if there are no contents, width might even be
        ## zero at this point)
        width = sum(map(self.width_map.get, self.contents))

        ## store dimensions with extra space for padding
        size = (width + 10, self.height + 10)

        ## generate and store surface
        self.image = render_rect(*size, self.bg_color)

        ### iterate over contents blitting surfaces

        ## define a starting x and y for blitting characters;
        ## notice they start with 5, to give the surface a
        ## small padding
        x = y = 5

        ## blit characters while incrementing the x position

        for char in self.contents:

            # blit surf
            self.image.blit(self.surf_map[char], (x, y))

            # increment x
            x += self.width_map[char]

        ### admin task: update rect dimensions and position

        self.rect.size = self.image.get_size()

        setattr(self.rect, self.coordinates_name, self.coordinates_value)
