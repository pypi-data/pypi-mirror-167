"""Game classes management for interactive levels.

Interactive levels are instances of
gamelevel.main.Level which is located here:
gamelevel/main.py
"""

from ..backprop.backprops import StaticBackProp

from ..block.blocks import StaticBlock
from ..block.grassdirt import GrassDirtBlock

from ..middleprop.sign import Sign
from ..middleprop.middleprops import VinesLadder, SimpleDoor, CaveEntrance
from ..middleprop.mushroomplant import MushroomPlant
from ..middleprop.satellitedish import SatelliteDish

from ..actor.npc import NPC
from ..actor.rocketscorpion import RocketScorpion
from ..actor.thornshooter.main import ThornShooter

from ..frontprop.frontprops import LeafCarpet, FrozenCover
from ..frontprop.toxicpollencloud import ToxicPollenCloud


CLASS_MAP = {
    "dirt_back_prop": StaticBackProp,
    "dirt_darker_back_prop": StaticBackProp,
    "stone_darker_back_prop": StaticBackProp,
    "sand_back_prop": StaticBackProp,
    "stone_back_prop": StaticBackProp,
    "grass_and_dirt_block": GrassDirtBlock,
    "stone_block": StaticBlock,
    "dirt_block01": StaticBlock,
    "sand_block": StaticBlock,
    "simple_door": SimpleDoor,
    "cave_entrance": CaveEntrance,
    "mushroom_plant": MushroomPlant,
    "vines_climbable": VinesLadder,
    "vines_top": VinesLadder,
    "vines_grid_climbable": VinesLadder,
    "vines_grid_top": VinesLadder,
    "sign": Sign,
    "satellite_dish": SatelliteDish,
    "leaf_carpet": LeafCarpet,
    "toxic_pollen_cloud": ToxicPollenCloud,
    "frozen_cover": FrozenCover,
    "thorn_shooter": ThornShooter,
    "rocket_scorpion": RocketScorpion,
    "npc": NPC,
}

LAYER_MAP = {
    "dirt_back_prop": "back_props",
    "dirt_darker_back_prop": "back_props",
    "stone_darker_back_prop": "back_props",
    "sand_back_prop": "back_props",
    "stone_back_prop": "back_props",
    "cave_entrance": "middle_props",
    "simple_door": "middle_props",
    "mushroom_plant": "middle_props",
    "vines_climbable": "middle_props",
    "vines_top": "middle_props",
    "vines_grid_climbable": "middle_props",
    "vines_grid_top": "middle_props",
    "sign": "middle_props",
    "satellite_dish": "middle_props",
    "dirt_block01": "blocks",
    "grass_and_dirt_block": "blocks",
    "stone_block": "blocks",
    "sand_block": "blocks",
    "thorn_shooter": "actors",
    "rocket_scorpion": "actors",
    "npc": "actors",
    "leaf_carpet": "front_props",
    "toxic_pollen_cloud": "front_props",
    "frozen_cover": "front_props",
}


def insert_level_reference(level):
    """Give a level reference for each class.

    level
        An instance of gamelevel.main.Level class.
    """
    for class_key in CLASS_MAP:
        CLASS_MAP[class_key].level = level


def remove_level_reference():
    """Remove level reference for each class.

    This is done by assigning None to it.
    """
    for class_key in CLASS_MAP:
        CLASS_MAP[class_key].level = None


def get_instance(data):
    """Return game class instance according to data.

    data
        A dict with a prop_name field which tells which
        kind of object to instantiate."""
    prop_name = data["prop_name"]
    Instantiator = CLASS_MAP.get(prop_name, "dummy")
    instance = Instantiator(**data)

    return instance


def get_layer_name(prop_name):
    """Return level layer name according to provided data.

    prop_name
        A str telling the name of the prop. It is used by
        a dict to retrieve the name of layer wherein to
        put the prop.
    """
    layer_name = LAYER_MAP.get(prop_name, "dummy_layer")

    return layer_name
