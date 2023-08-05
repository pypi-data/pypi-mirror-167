from os import listdir, remove, mkdir
from os.path import join
from shutil import copyfile

### local imports

from ...logconfig import APP_LOGGER

from ...config import GAME_REFS, SAVES_DIR, STATE_FILE_NAME

from ...common.jsonhandler import load_json


logger = APP_LOGGER.getChild(__name__)


def load_game():
    """Return level name from the current save slot used."""
    logger.info("Loading a new save.")

    save_state_data = load_json(join(SAVES_DIR, GAME_REFS.dirname, STATE_FILE_NAME))

    last_level_name = save_state_data["last_level"]

    return last_level_name
