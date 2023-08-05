"""HealthBar class facility for player health management."""

### third-party imports

from pygame import Rect
from pygame.draw import rect as draw_rect

### local imports

from ..config import SCREEN
from ..palette import BLACK
from ..common.behaviour import empty_function
from ..appcommon.surf import render_rect


class HealthBar:
    """A health display bar."""

    def __init__(self, player):
        """Initialize superclass and set variables.

        player
            A reference to player.main.Player instance.
        """
        self.player = player

        self.image = render_rect(200, 20)
        self.image.fill((255, 90, 40))

        self.rect = self.image.get_rect()
        self.topleft = (160, 60)

        outline_x, outline_y = (self.topleft[0] - 2, self.topleft[1] - 2)
        self.outline_rect = Rect((outline_x, outline_y), (204, 24))

        self.max_health = 100
        self.min_health = 0

        self.is_dead = False

        self.update_width()

        self.update = empty_function

    def update_width(self, amount=0):
        """Increase or decrease health by amount.

        It also updates size according to current health.

        amount (defaults to 0)
            An integer expressing the amount to add or
            subtract (if it is negative) from health.
        """
        self.player.health += amount
        self.player.health = max(
            min(self.player.health, self.max_health), self.min_health
        )
        self.rect.width = self.player.health * 2

        if not self.player.health and not self.is_dead:
            self.player.die()
            self.is_dead = True

    def draw(self):
        """Update object state."""
        # XXX
        # It is better to later change this to use a
        # mechanism similar to thornshooter healthbar,
        # (that is, the stencil-like feature)
        # since this current area rect feature was
        # implemented before I fully understood it. I don't
        # find it elegant/simple anymore.
        SCREEN.blit(self.image, self.topleft, self.rect)
        draw_rect(SCREEN, BLACK, self.outline_rect, 4)
