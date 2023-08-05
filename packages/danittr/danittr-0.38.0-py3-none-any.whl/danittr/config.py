"""Configuration file."""

from os import environ

from types import SimpleNamespace
from pathlib import Path

### third-party imports

from pygame import USEREVENT

from pygame.display import set_mode, set_icon, set_caption
from pygame.image import load as load_image
from pygame.time import Clock

### local imports

from .common.jsonhandler import save_json, load_json

from .palette import ARBITRARY_COLORKEY
from .keymapping import DEFAULT_KEYS_MAP


### locations

data_dir = Path(__file__).parent / "data"

MUSIC_DIR = str(data_dir / "music")
LEVELS_DIR = str(data_dir / "levels")
SOUNDS_DIR = str(data_dir / "sounds")
SCENES_DIR = str(data_dir / "scenes")
ANIMATIONS_DIR = str(data_dir / "animations")

IMAGES_DIR = str(data_dir / "images")
IMAGES_META_FILE = str(data_dir / "images_meta_file.json")

FONTS_DIR = str(data_dir / "fonts")
FONTS_META_FILE = str(data_dir / "fonts_meta_file.json")

### defining path to config file

if "APPDATA" in environ:
    config_dir = Path(environ["APPDATA"])

elif "XDG_CONFIG_HOME" in environ:
    config_dir = Path(environ["XDG_CONFIG_HOME"])

else:
    config_dir = Path(environ["HOME"]) / ".config"


APP_CONFIG_DIR = config_dir / "danittr"

if not APP_CONFIG_DIR.exists():
    APP_CONFIG_DIR.mkdir(parents=True)

## create a "saves" directory if it doesn't exist

SAVES_DIR = APP_CONFIG_DIR / "saves"

if not SAVES_DIR.exists():
    SAVES_DIR.mkdir(parents=True)

SAVES_DIR = str(SAVES_DIR)

### Gamewide constants

## object to carry references to important data throughout
## the game run
GAME_REFS = SimpleNamespace()

## time related objects/constants

CLOCK = Clock()

FPS = 30
MILLISECS_PER_FRAME = (1 / FPS) * 1000

### Custom events

SWITCH_LEVEL_TRIGGER = USEREVENT + 1
RESTART_FROM_SAVE = USEREVENT + 2

### Other data

STATE_FILE_NAME = "state.stt"
DEFAULT_STATE_DATA = {
    "last_level": "level01.lvl",
    "last_played_datetime": None,
    "health": 100,
}

### Custom settings

CONFIG_FILE = str(APP_CONFIG_DIR / "config.json")

DEFAULT_SETTINGS = {
    "music_volume": 0.2,
    "sound_volume": 0.2,
    "keys_map": DEFAULT_KEYS_MAP,
}


try:
    USER_SETTINGS = load_json(CONFIG_FILE)
except Exception as err:
    print(str(err))
    USER_SETTINGS = DEFAULT_SETTINGS
    save_json(USER_SETTINGS, CONFIG_FILE)

KEYS_MAP = USER_SETTINGS["keys_map"]

### pygame setups and constants

## Set caption and icon for window
set_caption("Dani to The Rescue", "DtTR")
ICON = load_image(str(data_dir / "game_icon.png"))
ICON.set_colorkey(ARBITRARY_COLORKEY)
set_icon(ICON)

## Set the screen and screen rect

# XXX must load fullscreen setting

### Defining constants and performing screen setup (set_mode)
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FLAG = 0
DEPTH = 32

SCREEN = set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FLAG, DEPTH)

SCREEN_RECT = SCREEN.get_rect()
