"""Facility for processing animation data."""

### local imports

## "common" subpackage

from ....common.wdeque.main import WalkingDeque
from ....common.pointgen import generate_points, convert_items_to_tuples
from ....common.indexgen import generate_indices
from ....common.tree import get_tree_values, get_tree_height

## "appcommon" subpackage

from ...surf import INVISIBLE_SURF
from ...gensurf import generate_surfaces

# animation data processing assistance

from .assist import (
    get_filled_map,
    manage_proxy_animations,
    store_anim_clock_keys,
    store_root_pos_exchange_map,
)


def process_anim_data(data):
    """Return processed animation data.

    data (dict)
        Data loaded from an .ani2d JSON file.

    The animation data is processed in several steps and
    returned as a mapping of processed data for different
    purposes.

    An explanation of the animation data model, as well as
    input, processing and output data of this preprocessing
    facility can be found in the anim_data_model.rst file
    here:

    appcommon/anim/anim_data_model.rst

    ### discussion about animation values conversion into
    ### tuples in other packages

    Different from what happens in this function
    here in the animation editor, the same function
    when implemented in the game package (should) converts
    the final animation values (including the value maps)
    into tuples. This is so because, as profiled by me and
    explained and confirmed by a prominent professional
    in the Python community (Raymond Hettinger), here:

    http://stackoverflow.com/a/22140115/10194508

    tuples have a slight boost in speed for item access (as
    well as other less important but welcome optimizations
    in other areas). It might not be a very significant
    change, but it is implemented anyway because:

    1) it wasn't costly in the point of view of management/
    maintenance (it's just one additional line of code);
    2) even not being very significant, it is expected that
    the combined speed gains of multiple solutions over the
    time, including this one, may prove to make a difference;

    However, such implementation wasn't made here in the
    animation editor. This is so because we have lots of
    read/edit/write operations, and tuples would need a lot
    of time consuming conversions to list and back into
    tuples again. Thus here in the animation editor the final
    animation value lists are never converted to tuples when
    they are processed.
    """
    ### process and post-process animation value maps

    ## create surface map and fill it with commonly used
    ## surface sequences (if the raw data in the maps
    ## is provided)

    surf_map = get_filled_map(
        {}, data, "surface_map", "surface_map_post", generate_surfaces
    )

    # also convert surface map values (lists) into tuples
    surf_map.update({key: tuple(value) for key, value in surf_map.items()})

    ## create position map and fill it with commonly used
    ## position sequences (if the raw data in the maps
    ## is provided)

    pos_map = get_filled_map(
        {}, data, "position_map", "position_map_post", generate_points
    )

    # also guarantee all points in positions lists are tuples
    # (this is also perform when processing animation values
    # further ahead)
    for position_list in pos_map.values():
        convert_items_to_tuples(position_list)

    # also convert position map values (lists) into tuples
    pos_map.update({key: tuple(value) for key, value in pos_map.items()})

    ### process animation data

    ## retrieve animation values for processing
    raw_anim_values = data["values"]

    ## create map wherein to store the results of the
    ## processed animation values (this will be be surfaces
    ## and positions mapped to node names and further
    ## mapped to animation names
    values = {}

    ## list names of the two types of values processed
    value_types_names = ["surfaces", "positions"]

    ## create map associating each type of value with its
    ## related variable map

    variables_map = {
        "surfaces": {
            "raw_data_key": "surface_data",
            "proc_data_key": "surfaces",
            "default": INVISIBLE_SURF,
            "value_map": surf_map,
            "function": generate_surfaces,
        },
        "positions": {
            "raw_data_key": "position_data",
            "proc_data_key": "positions",
            "default": (0, 0),
            "value_map": pos_map,
            "function": generate_points,
        },
    }

    ## iterate over animation values for each animation
    for anim_name, anim_data in raw_anim_values.items():

        ## create a dict to hold values for this specific
        ## animation
        values[anim_name] = {}

        ## iterate further over animation values for each
        ## node in this animation

        for node_name, node_data in anim_data.items():

            ## create a dict to hold values for this node
            ## in this animation

            node_anim_values = values[anim_name][node_name] = {}

            # use each variable map to retrieve important
            # variables and use them to process data

            for value_type in value_types_names:

                var_map = variables_map[value_type]

                raw_data_key = var_map["raw_data_key"]
                proc_data_key = var_map["proc_data_key"]
                default = var_map["default"]
                value_map = var_map["value_map"]
                func = var_map["function"]

                # try retrieving data
                try:
                    value_data = node_data[raw_data_key]

                # if absent, use default

                except KeyError:

                    node_anim_values[proc_data_key] = [default]

                    # if we are dealing with positions
                    # use the raw_data_key to assign
                    # the default value to the node
                    # data mapping as well (which is the
                    # mapping to be saved in the file)
                    if value_type == "positions":
                        node_data[raw_data_key] = [default]

                # otherwise process and store values;
                # note: in game applications we convert
                # the values container to a tuple before
                # storing them; see the docstring to know
                # more;

                else:

                    # process data into values
                    processed_values = func(value_data, value_map)

                    # if we are dealing with positions, we
                    # should convert the positions within
                    # the list into tuples

                    if raw_data_key == "position_data":

                        try:
                            convert_items_to_tuples(processed_values)

                        except TypeError:
                            pass

                    # regardless of the type of values
                    # being handled, they must be
                    # converted into tuples for quicker
                    # indexing
                    processed_values = tuple(processed_values)

                    # store values
                    node_anim_values[proc_data_key] = processed_values

    ### pre-process timing data

    ## create timing map and fill it with commonly used
    ## index sequences (if the raw data in the maps
    ## is provided)

    timing_map = get_filled_map(
        {}, data, "timing_map", "timing_map_post", generate_indices
    )

    ### process timing data

    ## retrieve timing data for processing
    raw_timing_data = data["timing"]

    ## create map wherein to store the results of the
    ## processed timing data (this will be
    ## collections.deque's subclass instances used
    ## to hold indices for surfaces and positions
    ## mapped to node names and further mapped to
    ## animation names
    timing = {}

    ## iterate over timing data for each animation
    for anim_name, anim_data in raw_timing_data.items():

        ## create dict to hold timing data for this specific
        ## animation
        timing[anim_name] = {}

        ## iterate further over timing data for each
        ## node in animation
        for node_name, node_timing_data in anim_data.items():

            ## create dict to hold timing data for this
            ## specific node in this animation
            node_timing_values = timing[anim_name][node_name] = {}

            # process data to retrieve timing values
            # for surfaces and positions
            for key in ("surface_indices", "position_indices"):

                # try retrieving data
                try:
                    timing_data = node_timing_data[key]

                # if absent, use default
                except KeyError:
                    node_timing_values[key] = WalkingDeque([0])

                    # also use the key to assign the
                    # default value to the node timing
                    # data in the file
                    node_timing_data[key] = [0]

                # otherwise, process and store values
                else:

                    # get indices
                    indices = generate_indices(timing_data, timing_map)

                    # create a walking deque with them
                    node_timing_values[key] = WalkingDeque(indices)

    ### process structure data

    structure = data["structure"]

    ## pre-assign structures from map

    # try retrieving structure mapped data
    try:
        struct_map = data["structure_map"]

    # if absent, pass
    except KeyError:
        pass

    # otherwise, retrieve data from such map and assign
    # wherever requested
    else:

        for anim_name, anim_struct_data in structure.items():

            if isinstance(anim_struct_data, str):

                key = anim_struct_data

                struct_data = struct_map[key]

                structure[anim_name] = struct_data

    ## iterate over structures processing and storing:
    ## - default ordering for updating and drawing as needed
    ## - list of nodes in the animation
    ## - the height of the animation tree

    for anim_name, anim_struct_data in structure.items():

        # retrieve tree for this animation
        tree = anim_struct_data["tree"]

        # generate and store optional order (parents first)
        optional_order = get_tree_values(tree, "name", "children")

        # assign the optional order for key, only if missing

        for order in ("updating_order", "drawing_order"):

            try:
                anim_struct_data[order]

            except KeyError:
                anim_struct_data[order] = optional_order

        # also store the optional order in a special
        # "node_names" field, because regardless of whether
        # it is or not in the same order of the other
        # ordering fields, its role is to list all nodes
        # in the animation, regardless of order
        anim_struct_data["node_names"] = optional_order

        # store height of this animation's tree
        anim_struct_data["height"] = get_tree_height(tree)

    ### process animation metadata

    ## retrieve animation metadata for processing, if any
    metadata = data.get("metadata", {})

    ## define which animations are of the proxy type,
    ## storing their names in the metadata dict;
    ## we do so by build a list of keys from the structure
    ## dict which are not present in the animation values
    ## or timing dict; such keys represent animation names
    ## of proxy type

    values_and_timing_keys = (*values, *timing)

    metadata["proxy_anim_names"] = [
        anim_name for anim_name in structure if anim_name not in values_and_timing_keys
    ]

    ## manage proxy animations and related metadata
    manage_proxy_animations(
        metadata, structure, values, timing, surf_map, pos_map, timing_map
    )

    ## generate metadata about durations
    store_anim_clock_keys(metadata, timing)

    ## generate/gather metadata about root position exchange
    store_root_pos_exchange_map(metadata, structure)

    ### process nodes data

    nodes = data["nodes"]

    # try retrieving geometry mapped data
    try:
        geometry_map = data["geometry_map"]

    # if absent, pass
    except KeyError:
        pass

    # otherwise, retrieve data from such map and assign
    # wherever requested
    else:

        for node_data in nodes.values():

            geometry_data = node_data["geometry"]

            if isinstance(geometry_data, str):
                key = geometry_data
                node_data["geometry"] = geometry_map[key]

    ### Map collections and return resulting map

    anim_data = {
        "values": values,
        "timing": timing,
        "structure": structure,
        "metadata": metadata,
        "nodes": nodes,
    }

    return anim_data
