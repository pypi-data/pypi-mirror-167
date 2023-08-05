"""Facility for the inventory manager."""

from collections import deque

### local import
from ..throwing.mushroom import Mushroom


# XXX
# when coding the item switching functionality,
# remember to also make the needed changes
# on the equipped display class.


def instantiate_item(item_name, player):
    """Instantiate item based on name.

    item_name
        A string representing the name of an equippable
        item. It is used to instantiate it.
    player
        A reference for an instance of the
        player.main.Player class, from which to harvest
        info.
    """
    if item_name == "mushroom":
        prop_name = item_name
        coordinates = [0, 0]
        level = player.level
        item = Mushroom(prop_name, coordinates, level)

    return item


class InventoryManager:
    """An inventory manager."""

    def __init__(self, state_data, equipped_display, player):
        """Initialize object.

        state_data
            json data loaded from the slot .stt file.
        equipped_display
            A reference to a
            player.equippeddisplay.EquippedDisplay instance
            used to communicate changes on the inventory.
        player
            A reference to a player.main.Player
            instance.
        """
        self.state_data = state_data
        self.equipped_display = equipped_display
        self.player = player

        equipped_item = self.state_data.get("equipped_item", "mushroom")
        self.equipped_item_name = equipped_item

        self.prepare_items()
        self.update_equipped_display()

    def prepare_items(self):
        """Instantiate all present items."""
        self.item_name_deque = deque()
        self.item_objects = {}

        inventory = self.state_data.get("inventory")
        if inventory:
            for item_name in inventory:
                self.item_name_deque.append(item_name)
                self.item_objects[item_name] = []

                amount = inventory.get(item_name, 0)
                for n in range(amount):
                    obj = instantiate_item(item_name, self.player)
                    self.item_objects[item_name].append(obj)

    def update_equipped_display(self):
        """Send item and count data to equipped display."""
        inventory = self.state_data.get("inventory")
        if inventory:
            self.equipped_item_count = inventory[self.equipped_item_name]

            self.equipped_display.update_visual_data(
                self.equipped_item_name, self.equipped_item_count
            )

    def add(self, item):
        """Return True if item is added.

        item
            A instance item to be added in the inventory.
        """
        item_name = item.prop_name

        try:
            amount = self.state_data["inventory"][item_name]

        except KeyError:

            if not self.state_data.get("inventory"):
                self.state_data["inventory"] = {}

            self.state_data["inventory"][item_name] = 1

            self.item_objects[item_name] = []
            self.item_objects[item_name].append(item)

            if item_name not in self.item_name_deque:
                self.item_name_deque.append(item_name)

            self.update_equipped_display()
            return True

        else:

            if amount < 6:
                self.state_data["inventory"][item_name] += 1

                self.item_objects[item_name].append(item)

                self.update_equipped_display()
                return True

            else:
                self.player.say_full_inventory()
                return False

    def request_equipped_item(self):
        """If manage to remove item, pass it to player."""
        item_name = self.equipped_item_name

        if self.remove(item_name):
            item = self.item_objects[item_name].pop()

        else:
            item = None

        return item

    def remove(self, item_name):
        """Return True if succesfully remove item."""
        try:
            amount = self.state_data["inventory"][item_name]
        except KeyError:
            return False
        else:
            if amount >= 1:
                self.state_data["inventory"][item_name] += -1
                self.update_equipped_display()
                return True
            else:
                return False
