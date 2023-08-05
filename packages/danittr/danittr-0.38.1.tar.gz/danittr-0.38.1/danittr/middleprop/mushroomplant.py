"""Facility for the mushroom plant middle prop class."""

from types import SimpleNamespace

from ..config import SCREEN
from ..common.math import unscroll_coordinates
from ..appcommon.surf import render_image
from ..appcommon.autoblit import BasicObject
from ..appcommon.promptfactory import prompt_factory
from ..appcommon.dialoguefactory import dialoguebox_factory
from ..appcommon.task import add_task, add_sendoff_task
from ..throwing.mushroom import Mushroom


class MushroomPlant(BasicObject):
    """A plant parasited by mushrooms."""

    level = None

    prop_map = {"mushroom_plant": render_image("mushroom_plant.png")}

    def __init__(self, prop_name, coordinates, has_mushroom):
        """Initialize superclass and variables.

        prop_name
            A string representing the prop name.
        coordinates
            List or tuple of x and y coordinates representing
            the desired bottomleft coordinates for the
            rect attribute.
        has_mushroom
            Boolean to flag if the plant has 'spawned' a
            throwing.mushroom.Mushroom
            object.
        """
        self.prop_name = prop_name

        self.image = MushroomPlant.prop_map[prop_name]

        self.rect = self.image.get_rect()
        self.rect.bottomleft = coordinates

        self.has_mushroom = has_mushroom
        self.set_operation_structure()

    def set_operation_structure(self):
        """Set other important operational structures.

        Those include atributes, methods and other objects."""
        ## prepare prompt
        self.object_screen_midtop = unscroll_coordinates(self.rect.midtop)
        # XXX
        # This offset should be made inside the
        # dialogue/prompt mechanism. Ponder. This tied to
        # the notion that dialogue/prompt feature should
        # have references to the objects instead of
        # receiving their position.
        offset_screen_midtop = (
            self.object_screen_midtop[0],
            self.object_screen_midtop[1] - 32,
        )

        # must come after defining self.object_screen_midtop
        self.instantiate_mushroom()

        item_list = []

        # XXX
        # This originally got a reference inside the
        # Mushroom animation_map class attribute.
        # Maybe in the future I might set a feature to
        # return a reference to a specific surface there
        surface = render_image("mushroom_topleft.png")

        item_list.append(surface)

        prompt_pair = prompt_factory(
            "Should I take the item?", offset_screen_midtop, item_list
        )
        prompt_action = self.give_item
        self.prompt = (prompt_pair, prompt_action)

        ## Prepare dialogue
        dialogue = [{"player": "It seems there's no usable mushroom here."}]
        self.dialogue = dialoguebox_factory(dialogue, offset_screen_midtop)

        ## Pick suitable method
        self.choose_interaction_method()

        ## Simple task control
        self.growth_task = SimpleNamespace(finished=True)

    def instantiate_mushroom(self):
        """Instantiate and store a mushroom."""
        self.mushroom = Mushroom(
            "mushroom", self.object_screen_midtop, self.level, self
        )

        self.mushroom.prepare_for_plant()

    def choose_interaction_method(self):
        """Alocate method to use for interactions."""
        if self.has_mushroom:
            self.receive_interaction = self.deliver_prompt

        else:
            self.receive_interaction = self.deliver_dialogue

    def update(self):
        """Update object state."""
        if self.has_mushroom:
            self.mushroom.update()

        else:
            self.set_growth_task()

    def draw(self):
        """Update object state."""
        if self.has_mushroom:
            self.mushroom.draw()

        super().draw()

    def set_growth_task(self):
        """Set growth task if needed."""
        if self.growth_task.finished:
            self.growth_task = add_task(self.set_mushroom_growth, 5000)

    def deliver_prompt(self, player):
        """Send prompt to player.

        player
            The instance of player.main.Player.
        """
        player.send_prompt(self.prompt)

    def deliver_dialogue(self, player):
        """Send dialogue to player.

        player
            The instance of player.main.Player.
        """
        player.send_dialogue(self.dialogue)

    def set_mushroom_growth(self):
        """Make a mushroom grow on plant."""
        self.has_mushroom = True
        self.mushroom.grow()
        self.json_data["has_mushroom"] = True

    def give_item(self):
        """Give item to player and clean variables."""
        try:
            player = self.level.player

        except AttributeError as err:
            # XXX
            # filter this better
            print(err)

        else:
            player.get_item(self.mushroom, self)

    def got_item(self):
        """Make arrangements for itemless state."""
        self.has_mushroom = False

        self.instantiate_mushroom()
        self.json_data["has_mushroom"] = False
        self.choose_interaction_method()

    def scroll(self, x, y):
        """Scroll by x and y in respective axis.
        x
            Integer indicating scrolling in x axis.
        y
            Integer indicating scrolling in y axis.
        """
        self.rect.move_ip(x, y)
