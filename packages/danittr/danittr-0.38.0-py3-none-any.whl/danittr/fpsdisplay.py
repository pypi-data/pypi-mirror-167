"""FPS display facility to assist in game development."""

### local imports

from .config import SCREEN_RECT, CLOCK
from .palette import BLACK, WHITE

from .appcommon.text.label.autolabel import AutoLabel

### define function to get current frames per second
### custom formatted


def custom_formatted_fps():
    """Retrieve, format and return frames/second rate."""
    rounded_fps = round(CLOCK.get_fps())

    custom_formatted_fps = str(rounded_fps).rjust(2, "0")

    return custom_formatted_fps


### create autolabel

fps_display = AutoLabel(
    custom_formatted_fps,
    "FPS: ",
    "",
    text="30",
    font_size=18,
    foreground_color=WHITE,
    background_color=BLACK,
    coordinates_name="topright",
    coordinates_value=SCREEN_RECT.topright,
)
