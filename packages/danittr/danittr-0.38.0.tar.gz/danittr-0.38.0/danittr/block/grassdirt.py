"""Facility for grass and dirt block sprite."""

from functools import partial
from random import seed, randint
from types import SimpleNamespace

from ..appcommon.anim.player.main import AnimationPlayer
from ..appcommon.task import add_task
from ..common.math import get_straight_distance


seed()

### utility function

# pygame don't handle lambdas well, so using this
def get_distance(pos, item):
    """Return straight distance relative to pos."""
    return get_straight_distance(item.rect.midtop, pos)


### class definition


class GrassDirtBlock:
    """A block with dirt and grass.

    The grass responds to player movement when walking
    over it."""

    level = None

    def __init__(self, prop_name, coordinates):
        """Initialize superclass and variables."""
        self.prop_name = prop_name

        self.anim_player = AnimationPlayer(
            self,
            prop_name,
            coordinates_name="bottomleft",
            coordinates_value=coordinates,
        )

        self.perform_setups()

    def perform_setups(self):
        """Perform extra setups.

        Those setups are either extra processing done
        to embellish in game stuff or controls, like
        flags to keep track of states.
        """
        self.patch_task = SimpleNamespace(finished=True)

        # XXX
        # in the future, this could have a larger range,
        # but I'd need more surfaces. The grass would be
        # more varied and beautiful.
        steps_no = randint(0, 1)

        obj_name_list = [
            obj.name for obj in self.anim_player.get_nodes(exclude_root=True)
        ]

        self.anim_player.update_nodes(steps_no, obj_name_list)

        ### store the nodes representing the grass patches

        self.patches = [
            obj
            for obj in self.anim_player.get_nodes()
            if obj.name.startswith("grass_patch")
        ]

    def update(self):
        """Update animation."""
        self.anim_player.update()

    def draw(self):
        """Draw animation."""
        self.anim_player.draw()

    def select_stomped_grass(self, pos):
        """Return name of grass patch closer to position.

        This is used to change the surface of the grass
        to make it appear as if it were stomped and thus
        changed shape slightly.

        pos
            midbottom position of player rect.
        """
        func = partial(get_distance, pos)
        self.patches.sort(key=func)
        return self.patches[0].name

    def grass_walking(self, player, pos):
        """Trigger grass movement if player walks over."""
        if player.x_speed and self.patch_task.finished:
            self.set_grass_moving(pos)

    def set_grass_moving(self, pos):
        """Set grass moving near position.

        pos
            midbottom position of player rect.
        """
        obj_name = self.select_stomped_grass(pos)

        callable_task = partial(self.anim_player.update_nodes, 1, [obj_name])

        self.patch_task = add_task(callable_task, 25)

    def scroll(self, x, y):
        """Scroll by x and y in respective axis.
        x
            Integer indicating scrolling in x axis.
        y
            Integer indicating scrolling in y axis.
        """
        self.rect.move_ip(x, y)
