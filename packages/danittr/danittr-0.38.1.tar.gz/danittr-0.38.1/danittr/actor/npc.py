"""Facility for the NPC (non-playable character) class."""

from ..appcommon.autoblit import BasicObject
from ..appcommon.dialoguefactory import dialoguebox_factory
from ..common.math import unscroll_coordinates
from ..common.behaviour import empty_function
from ..appcommon.surf import render_image


class NPC(BasicObject):
    """A non-playable character."""

    level = None

    prop_map = {"npc": render_image("npc.png")}

    def __init__(self, prop_name, coordinates, dialogue=None):
        """Assign variables."""
        self.prop_name = prop_name

        self.image = NPC.prop_map[prop_name]

        self.rect = self.image.get_rect()

        self.rect.bottomleft = coordinates

        if dialogue:
            object_screen_midtop = unscroll_coordinates(self.rect.midtop)
            offset_screen_midtop = (
                object_screen_midtop[0],
                object_screen_midtop[1] - 32,
            )
            self.dialogue = dialoguebox_factory(dialogue.copy(), offset_screen_midtop)

        else:
            self.dialogue = []

        self.update = empty_function

    def receive_interaction(self, player):
        """Send dialogue to player state manager."""
        player.send_dialogue(self.dialogue)

    def scroll(self, x, y):
        """Scroll by x and y in respective axis.
        x
            Integer indicating scrolling in x axis.
        y
            Integer indicating scrolling in y axis.
        """
        self.rect.move_ip(x, y)
