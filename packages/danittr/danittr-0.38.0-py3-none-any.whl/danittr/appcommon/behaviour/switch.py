### third-party import
from pygame.time import set_timer

### local imports

from ...logconfig import APP_LOGGER

from ...config import GAME_REFS, SWITCH_LEVEL_TRIGGER


def set_level_switching(after, level_name, destination=None):
    """Set a level switching event. Store level name, too.

    after (integer)
        number of milliseconds after which to generate
        the event.
    level_name
        the basename of the next level to be loaded.
    """
    GAME_REFS.next_level = level_name
    if destination:
        GAME_REFS.destination = destination

    milliseconds = after
    set_timer(SWITCH_LEVEL_TRIGGER, milliseconds)
