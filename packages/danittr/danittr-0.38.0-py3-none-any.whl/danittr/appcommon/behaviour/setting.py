from ...config import USER_SETTINGS, CONFIG_FILE

from ...common.jsonhandler import save_json

from ...music import MUSIC_MANAGER
from ...sound import set_sounds_volume


def apply_user_settings():
    """Apply user settings from USER_SETTINGS."""
    MUSIC_MANAGER.set_volume(USER_SETTINGS["music_volume"])
    set_sounds_volume(USER_SETTINGS["sound_volume"])
    save_json(USER_SETTINGS, CONFIG_FILE)
