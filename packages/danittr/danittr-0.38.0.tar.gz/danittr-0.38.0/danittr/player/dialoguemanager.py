"""Facility for displaying and managing dialogues."""

from ..config import SCREEN
from ..common.behaviour import empty_function
from ..appcommon.autoblit import BasicObject
from ..appcommon.surf import INVISIBLE_SURF


# XXX
# Ideas for improvement:
# The way dialogue manager works is somewhat cumbersome,
# I mean, it's not flexible at all. You can only have
# 2 objects 'speaking' in the same dialogue and their
# positions should be provided in anticipation, what
# prevents the dialogue box to follow moving objects.
# Change this in the future.


class DialogueManager:
    """Display and manages dialogue boxes."""

    def __init__(self, player):
        """Initialize superclass and set variables.

        player
            A reference to the instance of player.main.Player
            class.
        """
        self.player = player
        self.dialogue = None
        self.image = INVISIBLE_SURF.copy()
        self.rect = self.image.get_rect()

    def update(self):
        """Update object state."""
        try:
            self.dialogue.update()

        ### when dialogue attribute is None, due to
        ### trying accessing update attribute
        except AttributeError:
            pass

    def draw(self):
        """Update object state."""
        try:
            self.dialogue.draw()

        ### when dialogue attribute is None, due to
        ### trying accessing draw attribute
        except AttributeError:
            pass

    def get_dialogue(self, dialogue_pairs):
        """Instantiate a dialogue box.

        dialogue_pairs
            A list containing tuples with pairs of
            information. Such information consists
            of position coordinates of whoever is speaking
            and the dialogue surface to be displayed.
            This list is generated in
            appcommon/dialoguefactory.py
        """
        self.dialogue = DialogueDisplay(self, self.player, dialogue_pairs)

    def finish_dialogue(self):
        """Set current dialogue to None."""
        self.dialogue = None

    def skip_dialoguebox(self):
        """Skip current dialoguebox."""
        if self.dialogue:
            self.dialogue.switch_sprite()


class DialogueDisplay(BasicObject):
    """Object switcher for dialogue boxes and monologues."""

    def __init__(self, manager, player, dialoguebox_pairs):
        """Initialize superclass and prepare sprites.

        manager
            The instance of
            player.dialoguemanager.DialogueManager
        player
            A reference to the player.main.Player instance.
        dialoguebox_pairs
            A list containing tuples with pairs of
            information. Such information consists
            of position coordinates of whoever is speaking
            and the dialogue surface to be displayed.
            This list is generated in
            appcommon/dialoguefactory.py
        """
        self.manager = manager
        self.player = player

        self.dialogue_setup(dialoguebox_pairs)

    def dialogue_setup(self, dialoguebox_pairs):
        """Set dialoguebox_pairs to be used.

        dialoguebox_pairs
            A list containing tuples with pairs of
            information. Such information consists
            of position coordinates of whoever is speaking
            and the dialogue surface to be displayed.
            This list is generated in
            appcommon/dialoguefactory.py
        """
        self.dialogue = iter(dialoguebox_pairs)
        self.switch_sprite()

    def update(self):
        """Update object state."""
        if self.is_following_player:
            self.adjust_position()

    def switch_sprite(self):
        """Switch to next sprite, if any, or finish."""
        try:
            dialogue_info = next(self.dialogue)
        except StopIteration:
            self.manager.finish_dialogue()
        else:
            self.image = dialogue_info[1]
            self.rect = self.image.get_rect()

            position = dialogue_info[0]
            if position == "player_pos":
                self.is_following_player = True
                self.adjust_position()
            else:
                self.is_following_player = False
                self.rect.midbottom = position

    def adjust_position(self):
        """Adjust dialoguebox position to follow player."""
        player_midtop = self.player.rect.midtop
        offset_player_midtop = (player_midtop[0], player_midtop[1] - 32)
        self.rect.midbottom = offset_player_midtop
