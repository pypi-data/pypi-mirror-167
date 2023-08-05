"""Facility for index sequences generation."""

### standard library imports

from collections import deque
from collections.abc import Sequence
from random import seed, shuffle

### local import
from .wdeque.main import WalkingDeque


# XXX
# idea: implement progressions in indices generation
# that is, geometric progression, etc.
# maybe fibonacci too


def generate_indices(index_data, index_map={}):
    """Return indices list after generating/changing them.

    index_data (dict or list)
        data used to retrieve/load/generate/alter
        indices recursively or not.
    index_map (dict)
        contains indices lists. It is only meant to provide
        values and never be altered here.
    """
    ### if data provided is a sequence, then you don't
    ### need to process anything; just return it
    if isinstance(index_data, Sequence):
        return index_data

    ### process operation to
    ### retrieve/load/generate/alter surfaces

    name = index_data["name"]

    ## just add provided indices
    if name == "retrieve_from_map":
        key = index_data["key"]
        output = index_map[key]

    ## generate indices from range objects
    elif name == "range":
        start = index_data.get("start", 0)
        stop = index_data["stop"]
        step = index_data.get("step", 1)

        output = list(range(start, stop, step))

    ## generate indices by repeating indices
    elif name == "repeat":
        indices = generate_indices(index_data["sequence"], index_map)

        how_many_times = index_data["how_many_times"]

        output = indices * how_many_times

    ## generate indices by executing pre-defined
    ## operation
    elif name == "back_and_forth":
        length = index_data["original_length"]

        first_half = list(range(length))
        last_half = list(range(length)[::-1][1:-1])

        if index_data.get("is_eased", False):
            first_half = generate_indices(
                {"name": "easing", "index_data": first_half}, index_map
            )

            last_half = generate_indices(
                {"name": "easing", "index_data": last_half}, index_map
            )

        output = first_half + last_half

    ## change indices by multiplying existing ones
    elif name == "multiply":
        indices = generate_indices(index_data["sequence"], index_map)

        multiplier = index_data.get("multiplier", False)

        output = []

        ## multiply all indices
        if multiplier:
            for item in indices:
                seq = [
                    item,
                ] * multiplier
                output.extend(seq)

        ## multiply only specified indices
        else:
            multiplier_map = index_data["multiplier_map"]
            for item in indices:
                multiplier = multiplier_map.get(str(item), 1)
                seq = [
                    item,
                ] * multiplier

                output.extend(seq)

    ## change indices by slicing existing ones
    elif name == "slice":
        indices = generate_indices(index_data["index_data"], index_map)

        start = index_data.get("start")
        stop = index_data.get("stop")
        step = index_data.get("step")

        output = indices[start:stop:step]

        # note: collections.deque can't be sliced; the
        # walking deque, which is a subclass probably
        # can't too.

    ## change indices by rotating existing ones using
    ## deque
    elif name == "deque_rotate":
        indices = generate_indices(index_data["index_data"], index_map)

        rotation_amount = index_data["rotation_amount"]

        indices_deque = deque(indices)
        indices_deque.rotate(rotation_amount)

        output = list(indices_deque)

    ## get a walking deque from the indices
    elif name == "get_walking_deque":

        # get indices

        indices = generate_indices(index_data["index_data"], index_map)

        # create walking deque with them
        output = WalkingDeque(indices)

    ## change indices by executing pre-defined operation
    elif name == "easing":
        ## create an easing effect on values in the edges
        indices = generate_indices(index_data["index_data"], index_map)

        length = len(indices)
        output = []

        if length % 2:
            levels = length // 2

            ## iterate from center to first index
            for n, i in enumerate(range(levels, -1, -1), 1):
                seq = [i] * n
                output = seq + output

            ## iterate from center to last index
            for n, i in enumerate(range(levels, length), 1):
                if n == 1:
                    continue
                seq = [i] * n
                output += seq
        else:
            right = length // 2
            left = right - 1

            for n, i in enumerate(range(left, -1, -1), 1):
                seq = [i] * n
                output = seq + output
            for n, i in enumerate(range(right, length), 1):
                seq = [i] * n
                output += seq

        output = list(map(indices.__getitem__, output))

    ## change indices by executing pre-defined operation
    elif name == "shuffle":
        indices = generate_indices(index_data["index_data"], index_map)

        seed()
        shuffle(indices)

        output = indices

    ## concatenate multiple sequences
    elif name == "concatenate":
        output = []
        for sequence_data in index_data["sequences"]:
            output += generate_indices(sequence_data, index_map)

    ### make sure return value is a sequence

    if isinstance(output, Sequence):
        return output

    else:
        return [output]
