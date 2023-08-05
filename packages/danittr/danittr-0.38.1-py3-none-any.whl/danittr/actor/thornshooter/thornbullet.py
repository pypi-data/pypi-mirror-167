"""Facility for the thorn shooter bullet."""

from math import hypot

from ...appcommon.autoblit import BasicObject
from ...appcommon.surf import render_rect
from ...appcommon.collision import does_touch_screen
from ...common.math import unscroll_coordinates


class ThornBullet(BasicObject):
    """A moderately slow thorn bullet."""

    def __init__(self, center, level):
        """Initialize superclass and variables."""
        self.level = level
        self.image = render_rect(5, 5, (255, 0, 0))
        self.rect = self.image.get_rect()

        unscrolled_center = unscroll_coordinates(center)
        self.rect.center = self.center = unscrolled_center

        self.speed = 7  # px/frame
        self.power = 10

        self.is_targeting = False

    def update(self):
        """Update object state."""
        if not self.is_targeting:
            self.acquire_target()
            self.is_targeting = True

        self.move()

    def acquire_target(self):
        """Get player direction.

        Obs.: though part of the calculations could be
        performed by get_straight_distance function in
        common.behaviour, we need access to distance
        x and y, which said function don't provide. So
        this is good as it is."""
        self.target_x, self.target_y = self.level.player.rect.center
        x_distance = self.target_x - self.rect.x
        y_distance = self.target_y - self.rect.y

        diagonal_distance = hypot(x_distance, y_distance)

        time_in_frames = diagonal_distance / self.speed

        self.x_speed = round(x_distance / time_in_frames)
        self.y_speed = round(y_distance / time_in_frames)

    def move(self):
        """Perform movement in x and y direction."""
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        collided_platform = self.level.onscreen_map["blocks"].collide_any(self)

        if collided_platform:
            self.reset_position()
            return

        is_on_screen = does_touch_screen(self)

        if not is_on_screen:
            self.reset_position()
            return

        hit_player = self.rect.colliderect(self.level.player.rect)

        if hit_player:

            self.reset_position()

            try:
                self.level.player.suffer_damage(self.power)

            except AttributeError:
                pass

            return

    def reset_position(self):
        """Reset bullet position."""
        self.rect.center = self.center
        self.is_targeting = False
