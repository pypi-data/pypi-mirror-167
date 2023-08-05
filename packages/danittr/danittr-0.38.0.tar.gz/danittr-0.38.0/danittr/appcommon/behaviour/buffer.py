"""Facility for application specific behaviours."""

from os import listdir, remove
from os.path import join

### local imports

from ...logconfig import APP_LOGGER

from ...config import GAME_REFS, SAVES_DIR


### instantiate local logger
logger = APP_LOGGER.getChild(__name__)


def remove_buffers():
    """Remove existing buffers.

    This happens whenever the player quits to main menu
    or game, abandoning the current state/level data,
    present in the buffers. This just means all buffer
    files will be erased (if any).
    """
    logger.debug("Buffers being removed.")

    ### get the current name of the folder representing
    ### the game slot used
    try:
        save_dir = GAME_REFS.dirname

    ### if it is missing, return earlier
    except AttributeError:
        return

    ### Get and remove all buffers (.swp files) in current
    ### save dir

    full_save_dir = join(SAVES_DIR, save_dir)

    buffers = [
        join(SAVES_DIR, save_dir, item)
        for item in listdir(full_save_dir)
        if item.endswith(".swp")
    ]

    for item in buffers:
        remove(item)
