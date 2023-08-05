"""Facility for application specific behaviours."""

from os.path import join
from shutil import copyfile

### local imports

from ...logconfig import APP_LOGGER

from ...config import GAME_REFS, LEVELS_DIR, SAVES_DIR, STATE_FILE_NAME

from ...common.jsonhandler import load_json, save_json

from .load import load_game
from .buffer import remove_buffers

from ...mainmenu.main import MainMenu
from ...gamelevel.main import GameLevel
from ...sceneplayer.main import ScenePlayer


### instantiate local logger
logger = APP_LOGGER.getChild(__name__)


### functions


def get_level(level_name):
    """Return a new GameLevel instance.

    level_name (string)
        represents the basename of the level file. As level
        files are designed now, that string will end with
        the '.lvl' extension.
    """
    save_dir = GAME_REFS.dirname

    # destination, when present, holds a string with the
    # name of a portal in the level whose coordinates
    # are used to position the player. Whenever
    # entering a new level via a portal a specific
    # portal destination will be provided.

    try:
        destination = GAME_REFS.destination
    except AttributeError:
        destination = None
    else:
        del GAME_REFS.destination

    msg = "Level named '{}' being loaded.".format(level_name)

    logger.debug(msg)

    level_filepath = join(SAVES_DIR, save_dir, level_name)

    state_filepath = join(SAVES_DIR, save_dir, STATE_FILE_NAME)

    try:
        new_level = GameLevel(level_filepath, state_filepath, destination)

    except FileNotFoundError:

        backup_level_filepath = join(LEVELS_DIR, level_name)

        copyfile(backup_level_filepath, level_filepath)

        new_level = GameLevel(level_filepath, state_filepath, destination)

    return new_level


def get_custom_manager(manager_name):
    """Return custom update manager instance."""
    if manager_name.endswith(".scn"):
        return ScenePlayer(manager_name)

    elif manager_name == "main_menu":
        return MainMenu()

    else:
        raise Exception("This block should never be executed.")


def reset_player_health():
    """Reset player health from save_dir slot.

    Designed to be used after player dies,
    before reloading the last save/state in current
    slot.
    """
    logger.info("Health reset.")

    save_dir = GAME_REFS.dirname

    state_path = join(SAVES_DIR, save_dir, STATE_FILE_NAME)

    state_data = load_json(state_path)
    state_data["health"] = 100
    save_json(state_data, state_path)
