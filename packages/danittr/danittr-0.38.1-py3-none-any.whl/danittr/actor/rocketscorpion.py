"""Facility for the rocket scorpion actor class."""

from ..appcommon.anim.player.main import AnimationPlayer


class RocketScorpion(object):
    """A stinger launcher scorpion."""

    level = None

    def __init__(self, prop_name, coordinates):
        """Initialize superclass and variables.

        prop_name
            A string representing the prop name.
        coordinates
            List or tuple of x and y coordinates representing
            the desired bottomleft coordinates for the
            rect attribute.
        """
        self.prop_name = prop_name

        self.anim_player = AnimationPlayer(
            self,
            prop_name,
            coordinates_name="bottomleft",
            coordinates_value=coordinates,
        )

        self.anim_player.play()

    def update(self):
        """Update animation."""
        self.anim_player.update()

    def draw(self):
        """Draw animation."""
        self.anim_player.draw()

    def scroll(self, x, y):
        """Scroll by x and y in respective axis.
        x
            Integer indicating scrolling in x axis.
        y
            Integer indicating scrolling in y axis.
        """
        self.rect.move_ip(x, y)
