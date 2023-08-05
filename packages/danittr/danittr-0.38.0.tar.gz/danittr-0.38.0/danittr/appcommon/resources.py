"""Facility for game resource gathering and distribution."""

from os.path import join

### local imports

from ..config import ANIMATIONS_DIR

from ..common.jsonhandler import load_json

from .anim.proc.main import process_anim_data


### gather animation resources

ANIM_DATA_MAP = {}


anim_files_map = {
    "dani": "dani.ani2d",
    "cloud": "cloud.ani2d",
    "mushroom": "mushroom.ani2d",
    "indie_python_logo": "indie_python_logo.ani2d",
    "thorn_shooter": "thorn_shooter.ani2d",
    "satellite_dish": "satellite_dish.ani2d",
    "rocket_scorpion": "rocket_scorpion.ani2d",
    "toxic_pollen_cloud": "toxic_pollen_cloud.ani2d",
    "grass_and_dirt_block": "grass_and_dirt_block.ani2d",
}


for key, filename in anim_files_map.items():

    json_data = load_json(join(ANIMATIONS_DIR, filename))

    try:
        ANIM_DATA_MAP[key] = process_anim_data(json_data)

    except Exception as err:

        print("Error while processing {} file.".format(filename))
        raise Exception from err
