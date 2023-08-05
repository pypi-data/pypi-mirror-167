"""Facility for funcs to assist in anim data processing."""

### standard library

from types import SimpleNamespace
from operator import attrgetter
from itertools import permutations
from collections import defaultdict

### local imports

from ....common.tree import get_tree_values
from ....common.behaviour import get_nested_value


### quick utility
length_getter = attrgetter("length")

### functions


def get_filled_map(mapping, data, raw_data_key, post_process_key, func):
    """Return mapping after filling it with processed data.

    mapping (dict)
        mapping to hold the processed data.
    data (dict)
        mapping from which to retrieve the raw data for
        processing.
    raw_data_key, post_process_key (strings)
        they represent keys used to retrieve maps within the
        'data' argument. Such maps contain raw data to be
        processed and instructions to post-process the raw
        data processed from the first key respectively.
    func (callable)
        function to process the raw data.
    """
    for map_key in (raw_data_key, post_process_key):

        ### try retrieving raw data for processing
        try:
            retrieved_map = data[map_key]

        ### if absent, just break out of the for loop
        ### since the existence of both maps is
        ### optional and the absence of a map makes the
        ### presence of the next one unnecessary (if there's
        ### no data to process, then having post-process
        ### instructions has no meaning);
        except KeyError:
            break

        ### otherwise, process raw data
        else:
            for key, raw_data in retrieved_map.items():

                ## get processed data
                processed = func(raw_data, mapping)

                ## store the processed data in the mapping;

                ## note: in game applications we convert the
                ## processed data into a tuple before storing
                ## it; not here in the animation editor
                ## though, because if we did so editing live
                ## data would take much time due to
                ## numerous conversions from and to tuples;

                mapping[key] = processed

    return mapping


def manage_proxy_animations(
    metadata, structure, values, timing, surf_map, pos_map, timing_map
):
    """Setup proxy animations and related metadata.

    metadata (dict)
        stores animation metadata.
    structure (dict)
        contains structure information for each animation.
    values (dict)
        contains animation values for each animation and
        their respective nodes.
    timing (dict)
        contains timing information for each animation and
        their respective nodes.
    surf_map, pos_map, timing_map (dicts)
        contain animations value for surfaces, positions
        and animation timing, respectively.

    Proxy animations are animations produced by combining
    multiple pre-existent animation values and timing
    together. Such animation don't have animation data
    per se, except for structural data (which node is the
    parent/children of which).

    Thus, an animation is considered a proxy animation if
    there's no data for it in the values dict nor the
    timing dict.

    What we do here is:

        - Retrieve the proxy animations' names so we can
          reference them

        - If there are indeed proxy animations:
          - Reference the animation values and timing to
            which each node in the tree points (for the
            timing we actually generating a proxy-like/
            view-like object whose content is linked with
            the original walking deque but has independent
            walking; this is the ideal solutions, otherwise,
            if more than one node in the proxy animation
            were to reference the same timing deque, such
            deque would walk the animation value more than
            once per loop; for more information, visit the
            common/walkingdeque.py module);
    """
    ### retrieve the proxy animations' names
    proxy_names = metadata["proxy_anim_names"]

    ### store key names for different types of animation
    ### values and timing to use when building the proxy
    ### animations

    values_keys = ("surface_data", "position_data")
    indices_keys = ("surface_indices", "position_indices")

    ### store a map which associates raw values keys to
    ### their respective processed data ones

    processed_values_keys = ("surfaces", "positions")

    key_to_proc = dict(zip(values_keys, processed_values_keys))

    ### store map which associates values keys with their
    ### respective data map

    values_maps = (surf_map, pos_map)

    key_to_map = dict(zip(values_keys, values_maps))

    ### iterate over proxy animations (if there are any)
    ### referencing animation data from other animations
    ### for each node

    for anim_name in proxy_names:

        ## reference the tree structure and use it to
        ## retrieve the data for references for each kind
        ## of data

        tree = structure[anim_name]["tree"]

        refs_data = get_tree_values(tree, "reference_data", "children")

        ## iterate over each node and its respective
        ## referenced animation, creating references
        ## for animation values and timing

        # create mappings for proxy values and timing

        values[anim_name] = proxy_values = {}
        timing[anim_name] = proxy_timing = {}

        # reference node names of the proxy animation
        node_names = structure[anim_name]["node_names"]

        # finally iterate

        for node_name, ref_data in zip(node_names, refs_data):

            # create mappings for node anim values and timing

            proxy_values[node_name] = {}
            proxy_timing[node_name] = {}

            # assign value references

            for key in values_keys:

                # get data used to reference the values
                values_ref_data = ref_data[key]

                # get respective processed value key
                proc_key = key_to_proc[key]

                # if the reference data is a list, then it
                # must have length == 2; it contains the
                # names of animation and node referenced
                # respectively

                if isinstance(values_ref_data, list) and len(values_ref_data) == 2:

                    # unpack values into names of the
                    # referenced animation and node
                    ref_anim, ref_node_name = values_ref_data

                    # retrieve values using those names
                    retrieved_values = get_nested_value(
                        values, ref_anim, ref_node_name, proc_key
                    )

                # otherwise if the reference data is a
                # string, then it is a key to retrieve the
                # needed data in the respective value map

                elif isinstance(values_ref_data, str):

                    # retrieve specific value map for key
                    values_map = key_to_map[key]

                    # retrieve values using the reference
                    # data as key
                    retrieved_values = values_map[values_ref_data]

                # finally assign the values to the proxy
                # animation for the node in the proper key
                proxy_values[node_name][proc_key] = retrieved_values

            # assign timing "content content views"
            # (see common/wdeque/main.py for info on
            # content views)

            for key in indices_keys:

                # get data used to reference the timing
                timing_ref_data = ref_data[key]

                # if the reference data is a list, then it
                # must have length == 2; it contains the
                # names of animation and node referenced
                # respectively

                if isinstance(timing_ref_data, list) and len(timing_ref_data) == 2:

                    # unpack values into names of the
                    # referenced animation and node
                    ref_anim, ref_node_name = timing_ref_data

                    # retrieve timing view using those names
                    timing_view = get_nested_value(
                        timing, ref_anim, ref_node_name, key
                    ).get_content_view()

                # otherwise if the reference data is a
                # string, then it is a key to retrieve the
                # needed data in the timing map

                elif isinstance(timing_ref_data, str):

                    # retrieve walking deque from timing
                    # map
                    walking_deque = timing_map[timing_ref_data]

                    # retrieve the timing view
                    timing_view = walking_deque.get_content_view()

                # XXX add a function on sibling module
                # checks.py to ensure there's never a
                # scenario different from the if/elif blocks
                # above

                proxy_timing[node_name][key] = timing_view


def store_anim_clock_keys(metadata, timing):
    """Store keys to retrieve an animation clock.

    metadata
        Dictionary to store animation metadata.
    timing
        Dictionary containing timing information about
        animations for each node.

    For each animation, we measure the length of all
    timing sequences. The ones with the largest length
    for each animation have the node name and sequence
    name stored so that such sequence can be retrieved later.

    Such 'sequence' is in fact an instance of
    a collections.deque subclass defined on
    common/wdeque/main.py module.

    The largest one among them is called an animation clock,
    because we can use it to infer data like the
    current frame being played, how much frames it will
    take for the animation to complete the current loop
    and how many loops the animation performed (including
    backwards, if it is the case).

    Storing a reference to the deque itself would
    work too, but since all timing sequences are meant
    to be 'deepcopied' on the game package, we use the
    alternative approach of storing the keys instead.
    """
    metadata["largest_deques"] = largest_deques = {}

    length_zero_obj = SimpleNamespace(length=0)

    sequence_names = ["surface_indices", "position_indices"]

    for anim_name in timing:
        anim_timing_values = timing[anim_name]

        ### create map to store keys for the largest deque
        ### in the current animation
        largest_deques[anim_name] = anim_largest = {}

        ### Assign dummy as current largest deque
        largest_deque = length_zero_obj

        ### iterate over nodes' deques to find largest one
        for node_name in timing[anim_name]:
            node_sequences_map = anim_timing_values[node_name]

            ## group time deques together
            ## and retrieve largest

            deques = [largest_deque]

            for key in sequence_names:
                deques.append(node_sequences_map[key])

            largest_deque = max(deques, key=length_getter)

            ## If a deque from the node end up being
            ## the largest one, store the keys

            for key in sequence_names:
                if largest_deque == node_sequences_map[key]:
                    anim_largest["node_name"] = node_name
                    anim_largest["sequence_name"] = key


def store_root_pos_exchange_map(metadata, structure):
    """Generate/gather and store root position exchange map.

    metadata (dict)
        Storage for animation metadata.
    structure (dict)
        Contains structure information for each animation.

    A root position exchange map is a map which maps
    strings other dicts. Each string represents the name
    of a different root node in the animation (if the
    animations in the file have different root nodes).
    The dicts to which each string points contain the
    name of other root nodes pointing to a list of
    pygame.Rect attribute names.

    For instance:

    {
      "root_a": {
        "root_b": ["center", "center"]
      },
      "root_b": {
        "root_a": ["midbottom", "midbottom"]
      }
    }

    This map exists in order to prevent conflicts when
    exchanging positions between rects of different root
    nodes in the game/application space, specially when
    such nodes have rects of different sizes.
    """
    ### retrieve all root names and create pairs from the
    ### permutations between them

    root_names = {struct_data["tree"]["name"] for struct_data in structure.values()}

    pairs = permutations(root_names, 2)

    ### create the root pos exchange map using the pairs
    ### as nested keys and attributing the default value to
    ### each of them

    ## create a default dict
    root_pos_exchange_map = defaultdict(dict)

    ## iterate over pairs creating nested records of
    ## root position exchange data; such records are maps
    ## associating which position of root_a is used to
    ## which position of root_b; here position means the
    ## name of the pygame.Rect attribute from wherein to
    ## find/assign the position

    for root_a, root_b in pairs:
        root_pos_exchange_map[root_a][root_b] = ["center", "center"]

    ### update root pos exchange map values using values
    ### provided by the user, if any

    ## try retrieving user provided data
    try:
        root_pos_exchange_data = metadata["root_pos_exchange_map"]

    ## if not present, just pass
    except KeyError:
        pass

    ## otherwise, update values in the existing map
    else:
        root_pos_exchange_map.update(root_pos_exchange_data)

    ### finally store the exchange map in the metadata map
    metadata["root_pos_exchange_map"] = root_pos_exchange_map
