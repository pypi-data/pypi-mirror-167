"""Game launching."""

### local imports

# XXX maybe wrap the run_game import in a try/exception
# clause, since though rare sometimes refactoring
# errors may occur; ponder

from .logconfig import APP_LOGGER


### instantiating local logger
logger = APP_LOGGER.getChild(__name__)


def main():

    logger.info("Launching game.")
    from .gameloop import run_game

    run_game()


### brief instructions for module execution

if __name__ == "__main__":
    main()
