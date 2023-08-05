"""Custom exceptions."""


class ManagerSwitchException(Exception):
    """Raised when the update manager is switched.

    The update manager is any object whose reference
    is stored in the local variable of the gameloop.run_game
    function.
    """

    def __init__(self, update_manager_name):
        """Store the new update manager."""
        self.update_manager_name = update_manager_name
        super().__init__("Switching update manager.")


class LevelSwitchException(ManagerSwitchException):
    """Raised when switching between levels."""


class RestartLevelException(Exception):
    """Raise when player dies to restart level."""


class QuitGameException(Exception):
    """Raised to quit the game loop."""
