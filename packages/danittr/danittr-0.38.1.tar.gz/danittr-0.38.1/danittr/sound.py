"""Facility for sounds keeping."""

from os.path import join

### third-party import
from pygame.mixer import Sound

### local import
from .config import SOUNDS_DIR, USER_SETTINGS

### utility function


def sound_from_name(filename):
    """Create and return a Sound object.

    Locate it using its name.

    filename (string)
        represents the basename of the sound file.
    """
    return Sound(join(SOUNDS_DIR, filename))


### sounds map

SOUNDS_MAP = {
    "player_jump01": sound_from_name("player_jump_groan01.ogg"),
    "player_jump02": sound_from_name("player_jump_groan02.ogg"),
    "gui_step": sound_from_name("gui_step.ogg"),
    "game_start": sound_from_name("game_start.ogg"),
    "error": sound_from_name("error.ogg"),
    "key_typing01": sound_from_name("key_typing01.ogg"),
    "key_typing02": sound_from_name("key_typing02.ogg"),
}


def set_sounds_volume(volume):
    """Set the volume for all sounds in SOUNDS_MAP.

    volume (float)
        Float from 0.0 to 1.0.
    """
    for sound in SOUNDS_MAP.values():
        sound.set_volume(volume)


def get_sounds_volume():
    """Return the volume for any sound in SOUNDS_MAP."""
    SOUNDS_MAP[0].get_volume()


set_sounds_volume(USER_SETTINGS["sound_volume"])
