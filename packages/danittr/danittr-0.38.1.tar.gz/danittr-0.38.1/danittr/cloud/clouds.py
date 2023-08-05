"""Facility for cloud classes.

Used as parallax decorative elements.
"""

from random import seed, randint
from functools import partial

from ..appcommon.anim.player.main import AnimationPlayer
from ..appcommon.task import add_task


MOVE_TIME = 9000
ANIM_TIME = 12000


class Cloud:
    """A simple cloud."""

    def __init__(self, prop_name, bottomleft, anim_name):
        """Position and perform setups.

        prop_name
            String representing the name of the prop.
        bottomleft
            Bottomleft coordinates for a pygame.Rect instance.
        anim_name
            String representing name of the animation to
            use.
        """
        self.prop_name = prop_name
        self.anim_player = AnimationPlayer(
            self, prop_name, coordinates_name="bottomleft", coordinates_value=bottomleft
        )

        self.anim_player.switch_animation(anim_name)

        move_task = partial(self.rect.move_ip, 1, 1)
        add_task(move_task, MOVE_TIME, cyclic=True)

        anim_task = self.anim_player.step_forth

        seed()

        # XXX it is better to move only once by the
        # amount you pick, instead of multiple times
        # moving single units
        for i in range(randint(0, 15)):
            anim_task()

        add_task(anim_task, ANIM_TIME, cyclic=True)

    def scroll(self, dx, dy):
        """Scroll by dx and dy in respective axis.

        dx
            Integer indicating scrolling in x axis.
        dy
            Integer indicating scrolling in y axis.
        """
        self.rect.move_ip(dx / 80, dy / 80)

    def update(self):
        """Update animation."""
        self.anim_player.update()

    def draw(self):
        """Draw animation."""
        self.anim_player.draw()
