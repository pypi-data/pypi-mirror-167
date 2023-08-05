"""Facility for displaying and managing prompts."""

### local imports

from ..common.behaviour import empty_function
from ..appcommon.autoblit import BasicObject
from ..appcommon.surf import INVISIBLE_SURF


class PromptManager:
    """Display and manages prompt boxes."""

    def __init__(self, player):
        """Initialize superclass and set variables.

        player
            A reference to a player.main.Player instance.
        """
        self.player = player

        self.image = INVISIBLE_SURF
        self.rect = self.image.get_rect()

        self.prompt_display = None

        self.update = empty_function

    def draw(self):
        """Draw prompt display if available."""
        try:
            self.prompt_display.draw()

        ### attribute error due to prompt_display being
        ### None and this object lacking a draw method
        except AttributeError:
            pass

    def get_prompt(self, prompt):
        """Instantiate a prompt box.

        prompt
            A tuple containing a pair of data. The
            first item includes the position where a surface
            should appear and said surface. The second one
            is an action to be executed should the player
            confirm the prompt.
        """
        prompt_pair = prompt[0]
        prompt_action = prompt[1]
        self.prompt_display = PromptDisplay(
            self, self.player, prompt_pair, prompt_action
        )

    def finish_prompt(self):
        """Set current prompt to None."""
        self.prompt_display = None

    def confirm(self):
        """Execute prompt action."""
        if self.prompt_display:
            self.prompt_display.confirm()
            self.prompt_display = None


class PromptDisplay(BasicObject):
    """Object for prompt."""

    def __init__(self, manager, player, prompt_pair, prompt_action):
        """Initialize superclass and prepare sprites.

        manager
            The instance of the player.PromptManager class.
        player
            A reference to a player.main.Player instance.
        prompt_pair
            A tuple containing a pair of data. The
            first item includes the position where a surface
            should appear and the second one said surface.
        prompt_action
            A callable to be executed should the player
            confirm the prompt.
        """
        self.manager = manager
        self.player = player

        self.image = prompt_pair[1]

        self.rect = self.image.get_rect()
        self.rect.midbottom = prompt_pair[0]

        self.confirm = prompt_action

        self.update = empty_function
