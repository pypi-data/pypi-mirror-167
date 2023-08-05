"""Facility for level additional groups and related setups.

Those groups are usually used for decorative purposes.
"""

from random import seed, choice, sample

### local imports

from ..appcommon.autoblit import BlitterSet

from ..cloud.clouds import Cloud
from ..mountain.mountains import Mountain


def set_additional_groups(level):
    """Set additional groups in game group maps.

    Such groups contain decorative objects, animals and
    plants which aren't part of the gameplay, but
    contribute to the aesthetics of the gaem.

    level
        Instance of gamelevel.main.Level.
    """
    seed()

    ### set mountains

    level.group_names.insert(0, "parallax_mountains")
    level.group_map["parallax_mountains"] = BlitterSet()
    level.onscreen_map["parallax_mountains"] = BlitterSet()

    mountain = Mountain()
    level.group_map["parallax_mountains"].add(mountain)
    level.objs_to_scroll.add(mountain)

    ### Set clouds

    level.group_names.insert(1, "parallax_clouds")
    level.group_map["parallax_clouds"] = BlitterSet()
    level.onscreen_map["parallax_clouds"] = BlitterSet()

    # XXX
    # The group insertion above could be a level's method,
    # since it's used repeatedly. Maybe not.

    # values chosen arbitrarily based on better
    # aesthetical composition
    cloud_bottomlefts = [[x, y] for x in (-160, 240, 640, 1040) for y in (-64, 192)]

    x_offsets = range(-20, 21, 5)
    y_offsets = range(-60, 61, 20)
    for item in cloud_bottomlefts:
        item[0] += choice(x_offsets)
        item[1] += choice(y_offsets)

    cloud_anim_names = ["idle{}".format(str(n).rjust(2, "0")) for n in range(1, 21)]

    random_cloud_anims = sample(cloud_anim_names, 8)

    cloud_data_pairs = zip(cloud_bottomlefts, random_cloud_anims)

    instances = [
        Cloud("cloud", bottomleft, cloud_anim_name)
        for bottomleft, cloud_anim_name in cloud_data_pairs
    ]

    level.group_map["parallax_clouds"].update(instances)
    level.objs_to_scroll.update(instances)

    #
    #    ### set trees
    #    level.group_names.insert(2, "parallax_trees")
    #    level.group_map["parallax_trees"]    = BlitterSet()
    #    level.onscreen_map["parallax_trees"] = BlitterSet()
    #
    #    ### set flora
    #    level.group_names.insert(5, "flora")
    #    level.group_map["animals"]    = BlitterSet()
    #    level.onscreen_map["animals"] = BlitterSet()
    #
    #    ### set fauna
    #    level.group_names.insert(6, "fauna")
    #    level.group_map["fauna"]    = BlitterSet()
    #    level.onscreen_map["fauna"] = BlitterSet()
    #
    #    ### set foreground
    #    level.group_names.append("parallax_fg")
    #    level.group_map["parallax_fg"]    = BlitterSet()
    #    level.onscreen_map["parallax_fg"] = BlitterSet()
    #
    ### get objects touching screen
    level.get_onscreen_data()
