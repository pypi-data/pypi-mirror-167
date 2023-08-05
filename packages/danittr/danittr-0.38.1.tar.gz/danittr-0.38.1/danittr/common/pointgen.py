"""Facility for 2d point generation for general purpose."""

# XXX
# (see edit at the end)
#
# This calculations/generations/changes have many
# different applications. I could probably make a game
# just out of the exploration of them. I should stop by
# now, but keep making notes about possibilities for
# future implementations:
#
# Spring like movement:
# Moving like a spring should be achieved by simulating
# a body 'orbiting' around a second body while this
# second body is in movement (either circular or in a
# specific direction). That is, translating the first
# body circular movement by the movement of the second.
# Also, such circular movement could also be elliptical
# instead.
#
# Spiral like movement:
# Moving in spirals should be achieved by making lots of
# circles of different radius and making a sequence of
# the first index of the innermost circle, then the second
# index of the second circle, then third index of third
# circle and so on.
#
# Spiral and spring movements might be combinable, I think,
# to simulate for instance how some fireworks spiral away
# (dangerously so); it could be useful for sparks, fireworks,
# etc.
#
# Wave movement:
# an object going up and down following another one going
# straight. If up and down speed is constant, we have a
# zig-zag:
#
# .       .       .
#  .     . .     . .
#   .   .   .   .   .
#    . .     . .     .
#     .       .       .
#
# Also, instead of translating the points per se, you could
# just do loops and parent the object to another object
# doing a different loop or moving along, which would then
# cause the other object to be translated along.
#
# All very interesting applications.
#
# edit: this should become a docstring

from math import pi, sin, cos, hypot
from collections import deque
from collections.abc import Sequence
from random import seed, shuffle, sample
from itertools import cycle
from copy import deepcopy

### local imports

from .math import invert_point, offset_point
from .indexgen import generate_indices

# XXX
# idea: use rotation matrix formula to rotate points
# around a given origin (defaulting to [0, 0])

# XXX
# idea: obtaining points from filtering existing ones
# for instance, obtaining a half-circle from filtering
# point where y > 0, etc.


### utility function (use elsewhere, may also be used here
### if needed)


def convert_items_to_tuples(point_sequence):
    """Convert items in a sequence to tuples.

    Used to convert sequences whose items represent 2d points
    into tuples. This function was created because
    pygame.Rect updates its position much quicker when
    using tuples in comparison with other types (this was
    properly profiled using standard library timeit module).
    """
    for i in range(len(point_sequence)):
        point_sequence[i] = tuple(point_sequence[i])


### main function


def generate_points(pos_data, pos_map={}):
    """Return points list after generating/changing them.

    pos_data (dict or list)
        Data used to retrieve/load/generate/alter
        data recursively or not.
    pos_map (dict)
        contains list of positions (2d points/vectors).
        It is only meant to provide values and never be
        altered here.
    """

    ### if data provided is list, then you don't need to
    ### process anything; just return it
    if isinstance(pos_data, list):
        return pos_data

    ### process operation to
    ### retrieve/load/generate/alter points
    name = pos_data["name"]

    ## retrieve point list from pos_map
    if name == "retrieve_from_map":
        key = pos_data["key"]
        output = pos_map[key]

    ## generate point list for a line
    elif name == "line":
        quantity = pos_data["how_many_points"]
        start_point = pos_data.get("start_point", (0, 0))
        end_point = pos_data["end_point"]

        distance_x = end_point[0] - start_point[0]
        distance_y = end_point[1] - start_point[1]

        # compesate range starting in 1
        range_offset = 1
        # discount presence of start and end point
        existing_discount = -2

        offset_quantity = quantity + range_offset + existing_discount

        x_step = distance_x / offset_quantity
        y_step = distance_y / offset_quantity

        output = []
        output.append(start_point)

        for i in range(1, offset_quantity):
            amount_x = i * x_step
            amount_y = i * y_step
            x = round(start_point[0] + amount_x)
            y = round(start_point[1] + amount_y)
            output.append((x, y))

        output.append(end_point)

    ## generate point list for a circle
    elif name == "circle":

        quantity = pos_data["how_many_points"]
        radius = pos_data["radius"]

        output = []
        for k in range(quantity):
            value = (k * 2 * pi) / quantity
            x = round(radius * cos(value))
            y = round(radius * sin(value))
            point = (x, y)
            output.append(point)

    ## generate point list by mapping sequence to another
    ## (translating points of 1st one according to 2nd one)
    elif name == "sequence_to_path":
        ### process sequence content
        sequence = generate_points(pos_data["sequence"], pos_map)

        ### process path content
        path = generate_points(pos_data["path"], pos_map)

        ### generate points

        output = []
        cyclic_sequence = cycle(sequence)

        for point in path:
            translated_point = generate_points(
                {
                    "name": "translate",
                    "sequence": [next(cyclic_sequence)],
                    "sequence2": [point],
                }
            ).pop()

            output.append(translated_point)

    ## generate point list by repeating points
    elif name == "repeat":
        how_many_times = pos_data["how_many_times"]
        sequence = generate_points(pos_data["sequence"], pos_map)

        output = sequence * how_many_times

    ## generate point list by simulating accel. movement
    elif name == "from_accelerated_movement":
        start_point = pos_data.get("start_point", [0, 0])
        speed = pos_data.get("speed", [0, 0])
        acceleration = pos_data.get("acceleration", [0, 0])
        quantity = pos_data.get("how_many_points", 0)

        x, y = start_point
        speed_x, speed_y = speed
        accel_x, accel_y = acceleration

        output = []
        for i in range(quantity):
            x += speed_x
            y += speed_y

            point = (x, y)
            output.append(point)

            speed_x += accel_x
            speed_y += accel_y

    ## generate point list by movement simulation
    elif name == "spiral":
        quantity = pos_data["how_many_points"]
        resolution = pos_data["resolution"]
        radius_incr = pos_data["radius_increment"]

        cyclic_indices = cycle(range(resolution))

        output = []
        for i in range(quantity):
            radius = i * radius_incr
            circle = generate_points(
                {"name": "circle", "how_many_points": resolution, "radius": radius},
                pos_map,
            )
            point = circle[next(cyclic_indices)]
            output.append(point)

    ## generate point list by zipping two indice lists
    # XXX
    # more possibilities:
    # permutation and combination with itertools
    elif name == "zip_sequences":
        indices_x = generate_indices(pos_data["indices_x"])
        indices_y = generate_indices(pos_data["indices_y"])

        output = [(x, y) for x, y in zip(indices_x, indices_y)]

    ## generate points from cartesian product of indices
    elif name == "product":
        indices = generate_indices(pos_data["indices"])
        try:
            indices2 = pos_data["indices2"]
        except KeyError:
            indices2 = indices
        else:
            indices2 = generate_indices(indices2)

        output = [(x, y) for x in indices for y in indices2]

    ## generate random point list from points inside rect
    elif name == "random_from_rect":

        rect_size = pos_data["size"]
        quantity = pos_data["how_many_points"]

        width, height = rect_size

        population = [(x, y) for x in range(width) for y in range(height)]

        seed()
        output = sample(population, quantity)

    ## generate random point list from points inside circle
    elif name == "random_from_circle":
        radius = pos_data["radius"]
        quantity = pos_data["how_many_points"]

        population = [
            (x, y)
            for x in range(-radius, radius + 1)
            for y in range(-radius, radius + 1)
            if hypot(x, y) <= radius
        ]

        seed()
        output = sample(population, quantity)

    ## deepcopy a list of positions
    elif name == "deepcopy":
        sequence = generate_points(pos_data["sequence"], pos_map)

        output = deepcopy(sequence)

    ## change point list by mirroring
    elif name == "mirror":
        sequence = generate_points(pos_data["sequence"], pos_map)

        use_last = pos_data.get("use_last", True)

        mirror_x = pos_data.get("mirror_x", True)
        mirror_y = pos_data.get("mirror_y", True)

        ### either use last or first point
        if use_last:
            mirror_point = sequence[-1]
        else:
            mirror_point = sequence[0]
        m_point_x, m_point_y = mirror_point

        ### sort temp list according to 'use_last'
        iterable = sequence[::-1] if use_last else sequence

        ### generate new points
        output = []
        for point in iterable:
            x, y = point
            if x == m_point_x and (y == m_point_y):
                # ignore if it is the mirror point
                continue
            else:
                # increments are either zero or
                # double inverted distance
                # depending on axes set to be mirrored
                x_incr = 2 * (m_point_x - x) if mirror_x else 0

                y_incr = 2 * (m_point_y - y) if mirror_y else 0

                new_x = x + x_incr
                new_y = y + y_incr
                new_point = (new_x, new_y)
                output.append(new_point)

        ### append or prepend according to 'use_last'
        if use_last:
            sequence.extend(output)
            output = sequence
        else:
            output.reverse()
            output.extend(points)

    ## change point list by repeating it
    elif name == "repeat_existing":
        sequence = generate_points(pos_data["sequence"], pos_map)
        how_many_times = pos_data["how_many_times"]
        output = sequence * how_many_times

    ## change point list by executing pre-defined operation
    elif name == "back_and_forth_from_existing":
        sequence = generate_points(pos_data["sequence"], pos_map)
        first_half = sequence[:]
        last_half = sequence[::-1][1:-1]

        output = first_half + last_half

    ## change point list by multiplying existing ones
    elif name == "multiply":
        sequence = generate_points(pos_data["sequence"], pos_map)

        multiplier = pos_data.get("multiplier", False)

        output = []
        if multiplier:
            ## multiply all points by multiplier
            for item in sequence:
                seq = [
                    item,
                ] * multiplier
                output.extend(seq)

        else:
            ## else multiply points according to map

            # for simplification, instead of multiplicands,
            # the fields are indices representing point
            # position in sequence
            multiplier_map = pos_data["multiplier_map"]
            for index, item in enumerate(sequence):
                multiplier = multiplier_map.get(str(index), 1)
                seq = [
                    item,
                ] * multiplier

                output.extend(seq)

    ## change point list by slicing it
    elif name == "slice":
        sequence = generate_points(pos_data["sequence"], pos_map)
        start = pos_data.get("start")
        stop = pos_data.get("stop")
        step = pos_data.get("step")

        output = sequence[start:stop:step]

    ## change point list by inverting them
    elif name == "invert":
        sequence = generate_points(pos_data["sequence"], pos_map)

        invert_x = pos_data.get("invert_x", False)
        invert_y = pos_data.get("invert_y", False)

        # XXX the comprehension below produces a list of
        # tuples (which represent points); should we
        # convert such points into lists?

        output = [invert_point(point, invert_x, invert_y) for point in sequence]

    ## change point list by translating it
    elif name == "translate":

        sequence = generate_points(pos_data["sequence"], pos_map)

        try:
            sequence2 = pos_data["sequence2"]

        except KeyError:
            delta_x = pos_data.get("delta_x", 0)
            delta_y = pos_data.get("delta_y", 0)

            offset = (delta_x, delta_y)

            translated_points = []
            for point in sequence:
                new_point = offset_point(point, offset)
                translated_points.append(new_point)

        else:

            sequence2 = generate_indices(sequence2)
            translated_points = []

            for point, offset in zip(sequence, sequence2):
                new_point = offset_point(point, offset)
                translated_points.append(new_point)

        output = translated_points

    ## change point list by deque rotating existing ones
    elif name == "deque_rotate":
        sequence = generate_points(pos_data["sequence"], pos_map)

        rotation_amount = pos_data["rotation_amount"]

        points_deque = deque(sequence)
        points_deque.rotate(rotation_amount)

        output = list(points_deque)

    ## change point list by shuffling them
    elif name == "shuffle":
        sequence = generate_points(pos_data["sequence"], pos_map)
        seed()
        shuffle(sequence)

        output = sequence

    ### make sure return value is a sequence

    if isinstance(output, Sequence):
        return output

    else:
        return [output]
