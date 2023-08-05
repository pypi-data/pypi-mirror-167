"""Facility for surface generation for general purposes."""

from itertools import cycle, chain
from collections.abc import Sequence

### third-party imports

from pygame import Surface, Rect
from pygame.transform import flip as flip_surface
from pygame.draw import line as draw_line

### local imports

from .surf import INVISIBLE_SURF, render_image
from .loadscreen import blit_resource_loading


def generate_surfaces(surf_data, surf_map={}):
    """Return surfaces list after series of operations.

    surf_data (dict or list)
        data used to generate/load/alter data recursively
        or not.
    surf_map (dict)
        contains surface lists. It is only meant to provide
        values and never be altered here.
    """
    ### process operation to
    ### retrieve/load/generate/alter surfaces
    name = surf_data["name"]

    ## retrieve from surf_map
    if name == "retrieve_from_map":
        key = surf_data["key"]
        output = surf_map[key]

    ## load from disk
    elif name == "load_from_disk":
        image_names = surf_data["image_names"]

        output = []

        for img_name in image_names:

            ### admin task: blit a loading resource message
            blit_resource_loading()

            ### load and append surf

            surf = render_image(img_name)
            output.append(surf)

    elif name == "load_spritesheet":
        img_name = surf_data["image_name"]

        ### admin task: blit a loading resource message
        blit_resource_loading()

        ### load spritesheet
        spritesheet = render_image(img_name)

        output = []

        try:
            sprite_size = surf_data["sprite_size"]

        ## use specified rects to retrieve each sprite
        except KeyError:
            rects_parameters = surf_data["rects_parameters"]
            for rect_params in rects_parameters:
                rect = Rect(rect_params)
                subsurf = spritesheet.subsurface(rect)
                output.append(subsurf)

        ## otherwise use sprite size and quantity data
        ## to retrieve each sprite by walking the
        ## spritesheet like a grid/table
        else:
            quantity = surf_data["how_many_sprites"]
            sprite_width, sprite_height = sprite_size
            spritesheet_width = spritesheet.get_width()
            sprites_per_row = spritesheet_width // sprite_width

            # create a cycle to count in which row
            # you are when iterating
            row_counter = cycle(range(sprites_per_row))

            row = next(row_counter)
            column = 0
            for _ in range(quantity):
                x = sprite_width * row
                y = sprite_height * column

                # create rect and use it to create
                # subsurf
                rect = Rect(x, y, *sprite_size)
                subsurf = spritesheet.subsurface(rect)

                # store subsurf
                output.append(subsurf)

                # get next row;
                # if it equals zero, increment column;
                row = next(row_counter)
                if row == 0:
                    column += 1

    ## use an invisible surf
    elif name == "invisible":
        output = INVISIBLE_SURF

    ## create an special surf similar to an "empty"
    ## object in blender software
    elif name == "create_empty":

        surf = Surface(surf_data["dimensions"]).convert_alpha()

        surf.fill((0, 0, 0, 0))

        rect = surf.get_rect()

        lines = [[rect.midtop, rect.midbottom], [rect.midleft, rect.midright]]

        for line in lines:
            draw_line(surf, (0, 0, 0), *line, 3)

        output = surf

    ## change surf list by slicing it
    elif name == "slice":
        surfaces = generate_surfaces(surf_data["surface_data"], surf_map)

        start = surf_data.get("start")
        stop = surf_data.get("stop")
        step = surf_data.get("step")

        output = surfaces[start:stop:step]

    ## change surf list by flipping its surfaces
    elif name == "flip":
        surfaces = generate_surfaces(surf_data["surface_data"], surf_map)

        flip_x = surf_data.get("flip_x", False)
        flip_y = surf_data.get("flip_y", False)

        output = [flip_surface(surf, flip_x, flip_y) for surf in surfaces]

    ## change surf list by deepcopying surfs
    elif name == "deepcopy":
        surfaces = generate_surfaces(surf_data["surface_data"], surf_map)

        output = [surf.copy() for surf in surfaces]

    ## concatenate lists of surfaces
    elif name == "concatenate":

        # retrieve list of surface sequences data
        surface_sequences = surf_data["surface_sequences"]

        # generate a list of surfaces for each surface data

        lists = [
            generate_surfaces(surface_data, surf_map)
            for surface_data in surface_sequences
        ]

        # finally concatenate all lists into a single one
        output = list(chain.from_iterable(lists))

    ### make sure return value is a sequence

    if isinstance(output, Sequence):
        return output

    else:
        return [output]
