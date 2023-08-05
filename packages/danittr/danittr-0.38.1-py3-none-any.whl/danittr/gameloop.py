"""Facilities for Game class, the main application."""

### third party imports and setups

from pygame import init as init_pygame
from pygame.mixer import pre_init

## sound pre initialization
pre_init(44100, -16, 8, 1024)

## pygame initialization
init_pygame()

## extra pygame imports

from pygame import quit as quit_pygame, error as pygame_error

from pygame.event import clear as clear_events


### local imports and setups

from .config import CLOCK, FPS

from .music import MUSIC_MANAGER

### start music and blit a loading screen
MUSIC_MANAGER.update()

from .appcommon.exception import (
    QuitGameException,
    LevelSwitchException,
    RestartLevelException,
    ManagerSwitchException,
)
from .appcommon.behaviour.main import (
    get_level,
    load_game,
    get_custom_manager,
    reset_player_health,
)
from .appcommon.behaviour.buffer import remove_buffers

from .logconfig import APP_LOGGER

logger = APP_LOGGER.getChild(__name__)


# TODO the player probably only need to be instantiated
# once; should you do that? Also, the current level
# instance could be stored in the GAME_REFS? (in which
# case we should probably change the name of the object);
# probably instantiate player as you do with the
# music manager;

# TODO eliminate the concept of scripted level; just use
# game levels and the custom managers

# TODO since the event queue is populated even during
# level transitions (for instance, while loading assets
# when transitioning from logo screen to main menu),
# it should be a good idea to clear the event queue
# just as you begin looping throught a new level;
# could there be more objects like the fps display
# which only need to be instantiated once? think
# about it and take measures to guarantee you're not
# reinstantiating objects unnecessarily;

# TODO I must somehow prevent user from leaving screen
# after confirm saving prompt, or the game will freeze;

# XXX
# Before changing the level, the game.Game still
# finished the execution of the level manage_updates
# method, which cause a pygame.display.update to
# be executed and thus update the screen, redrawing
# what was there before. (Now that I think of it, this
# is somehow absurd, so I'll leave it here anyways but
# to describe the behaviour, not necessarily the cause,
# that is, I'm not sure of this myself,
# but this is what it seems to happen: before the
# next level starts we have a quick split second glimpse
# of screen last frame from last level).

# XXX
# task manager may very well be able to replace the current
# level switching timing feature and the restart level too
# (this last one is the one used whenever the player dies).
# Edit: this works but is a discarded idea, because since
# the task manager discards all tasks when switching
# between levels, the tasks are discarded while we are
# iterating over them.
# This must be properly archived for future reference.
# Since I don't understand completely the underlying
# workings of the "for i in iterable" block, I'm not sure
# if I can asses the situation accurately, but at least the
# current solution isn't bad at all, so it's ok. In fact,
# even if the tasks are discarded while iterating over them,
# it may be that this isn't a problem, since the iterable
# isn't changed itself, just 'unbound' from the task manager
# instance. Additionaly, the failed discarded attemp,
# even if it wasn't harmful, it was noticeable more slow,
# so the previous is the best anyway.

# XXX
# remember to eliminate the need to receive level references
# in classes that only used it to get screen references
# from its old screen attribute (not used anymore)

# XXX
# It would be great if I could change the default coordinates
# used to create objects (instead of just using
# bottomleft). See how you implement it.

# XXX
# The level switching could be done inside another
# very light update manager. This would eliminate the
# coexistence of two loaded levels at the same time
# whenever switching between them. Ponder.
#
# Edit: the temporary coexistence of two levels isn't
# as harmful as anticipated, because the surface data,
# which is the most memory consuming information, is always
# loaded in the memory. The only extra information kept
# simultaneously from both levels are regular 'object'
# subclasses and related data, which isn't memory consuming
# at all in comparison. Also, we never had any runtime
# problem related to memory, specially considering the
# machine in which the game is being developed is old and
# has only 2GB of memory, so we are very ok.

### main function


def run_game():
    """Run the game loop."""
    logger.info("Preparing to enter the game loop.")

    ### get logo screen scene
    update_manager = get_custom_manager("logo_screen.scn")

    ### create a flag to represent the game's running state
    running = True

    ### initialize the game loop
    while running:

        CLOCK.tick(FPS)

        ### try executing game loop specific methods of the
        ### update manager
        try:
            ### call the routine responsible for controlling
            ### the game
            update_manager.control()

            ### call the routines responsible for managing
            ### the game logic
            update_manager.update()
            MUSIC_MANAGER.update()

            ### call the routine responsible for drawing
            ### and updating the screen
            update_manager.draw()

        ### if either a level switch or manager switch
        ### exception is raised, assign the
        ### new_update_manager to the local variable;
        ### the exact type must be assessed though, so
        ### a proper message can be logged accordingly;

        except ManagerSwitchException as err:

            if type(err) is LevelSwitchException:
                logger.info("Switching between levels.")

            else:
                logger.info("Switching to update manager.")

            # TODO adjust code below

            manager_name = err.update_manager_name

            if isinstance(manager_name, str):
                if manager_name.endswith(".lvl"):
                    update_manager = get_level(manager_name)

                else:
                    update_manager = get_custom_manager(manager_name)

            else:
                update_manager = manager_name

            ### admin task: clear event queue
            clear_events()

        ### if a restart game exception is raised, execute
        ### the restart level function
        except RestartLevelException:

            remove_buffers()
            reset_player_health()

            update_manager = get_level(load_game())

        ### if a quit game exception is raised, trigger
        ### the exit of the game loop by assigning
        ### false to the running flag
        except QuitGameException:

            logger.info("Quitting game normally.")
            running = False

        ### general error handlinlg
        except (Exception, pygame_error) as err:
            print("here")
            logger.exception("Exitting game due to unexpected exception.")

            # XXX ponder about what to do here, there's
            # various possibilities and factors to consider
            # besides only calling quit_pygame (pygame.quit);

            quit_pygame()

            raise Exception from err

    ### remove swap files
    remove_buffers()

    ### log final call to pygame_quit and perform it

    logger.debug("pygame.quit being called.")
    quit_pygame()
