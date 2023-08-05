"""Facility for specialized label for value monitoring."""

### local imports

from .main import Label

from ....palette import BLACK


class AutoLabel(Label):
    """A label with custom autoupdating ability."""

    def __init__(
        self,
        monitor_routine,
        prefix="",
        suffix="",
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

        Extends appcommon.text.label.main.Label.__init__

        monitor_routine (callable)
            to be executed every loop to check for changes
            in its return value.
        prefix, suffix (string)
            text to be prepended/appended to the label text
            respectively.
        text (string)
            provides text to update surface.
        font_size (integer)
            indicates desired font size.
        font_style (string)
            Either 'default' for default font or 'mono' for
            a monospace font.
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
        ### store variables for reuse

        self.monitor_routine = monitor_routine

        self.prefix = prefix
        self.suffix = suffix

        ### prepend prefix and append suffix to text
        text = self.prefix + text + self.suffix

        ### initialize superclass
        super().__init__(
            text,
            font_size=font_size,
            font_style=font_style,
            foreground_color=foreground_color,
            background_color=background_color,
            coordinates_name=coordinates_name,
            coordinates_value=coordinates_value,
        )

        ### override update behaviour from Label superclass
        self.update = self.monitor_content

        ### execute the update method, so the contents
        ### are update with the prefix and suffix if needed
        self.update()

    def monitor_content(self):
        """Pass input from monitor routine to Label.set.

        Uses appcommon.text.label.main.Label.set, which only
        updates the contents of the label if they have
        changed.
        """
        text = self.prefix + self.monitor_routine() + self.suffix

        self.set(text)
