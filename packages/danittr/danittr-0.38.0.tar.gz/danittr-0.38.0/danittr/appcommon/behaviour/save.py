from os import listdir, mkdir
from os.path import join
from shutil import copyfile

### local imports

from ...logconfig import APP_LOGGER

from ...config import (
    GAME_REFS,
    SAVES_DIR,
    STATE_FILE_NAME,
    DEFAULT_STATE_DATA,
    IMAGES_DIR,
)

from ...common.timehandler import get_isostring_datetime
from ...common.jsonhandler import save_json


### instantiate local logger
logger = APP_LOGGER.getChild(__name__)


def save_game():
    """Save game by copying buffer to original files.

    All changes made in the game and levels are
    store in buffers whenever the player switch levels,
    progresses, etc. Saving the game just means copying
    those buffers to the original files, so they can
    be loaded with the progres/changes applied.
    """
    logger.info("Saving game")

    save_dir = GAME_REFS.dirname

    ### Saving state

    state_path = join(SAVES_DIR, save_dir, STATE_FILE_NAME)

    state_swap_path = state_path + ".swp"

    try:
        copyfile(state_swap_path, state_path)

    except FileNotFoundError as err:
        msg = "Didn't found state swap file" + " in " + save_dir + " save."
        logger.exception(msg)
        raise err

    ### Saving levels

    levels_dir = join(SAVES_DIR, save_dir)

    level_files = [
        join(SAVES_DIR, save_dir, item)
        for item in listdir(levels_dir)
        if item.endswith(".lvl")
    ]

    for level_path in level_files:

        level_swap_path = "{}.swp".format(level_path)

        try:
            copyfile(level_swap_path, level_path)

        except FileNotFoundError as err:

            # don't raise this error, it must only be logged,
            # since it is natural; not all levels
            # will have a swap version (when the player
            # saves elsewhere and don't visit there again),
            # that's why some of them cause the
            # file not found error to be raised.

            # XXX
            # This error can happen when there's no
            # swap file because I saved it (so swaps
            # were eliminated). However, I'm somehow
            # dissatisfied with how I'm logging it,
            # it isn't clear. Solve this.

            msg = (
                "Didn't found level swap path"
                + " called "
                + level_swap_path
                + " in "
                + save_dir
                + " save."
            )

            logger.exception(msg)


def setup_new_save(directory_name):
    """Setup all files for a new game save/slot."""
    logger.info("Setting up a new save")

    new_save_dir = join(SAVES_DIR, directory_name)
    mkdir(new_save_dir)

    state_data = DEFAULT_STATE_DATA.copy()
    state_data["last_played_datetime"] = get_isostring_datetime()

    state_filepath = join(new_save_dir, STATE_FILE_NAME)
    save_json(state_data, state_filepath)

    thumb_file = join(IMAGES_DIR, "new_save_thumb.png")
    thumb_destination = join(new_save_dir, "thumb.png")
    copyfile(thumb_file, thumb_destination)
