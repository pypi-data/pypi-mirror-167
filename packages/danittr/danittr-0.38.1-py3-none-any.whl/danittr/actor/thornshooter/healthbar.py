"""Facility for healthbar and health management."""

from pygame import Rect

from pygame.draw import rect as draw_rect

from ...config import SCREEN
from ...common.behaviour import empty_function
from ...common.math import unscroll_coordinates
from ...appcommon.surf import render_rect
from ...appcommon.autoblit import BasicObject
from ...palette import BLACK, ARBITRARY_COLORKEY


class HealthBar(BasicObject):
    """A healthbar for the thorn shooter."""

    def __init__(self, thorn_shooter):
        """Initialize superclass and perform setups."""
        self.thorn_shooter = thorn_shooter
        self.fill_color = (255, 90, 40)

        self.image = render_rect(100, 10, self.fill_color)
        self.rect = self.image.get_rect()
        self.rect.midbottom = unscroll_coordinates(self.thorn_shooter.rect.midtop)
        self.rect.y += -10

        self.image.set_colorkey(ARBITRARY_COLORKEY)
        self.stencil = render_rect(*self.image.get_size(), ARBITRARY_COLORKEY)

        self.set_operational_structures()

    def set_operational_structures(self):
        """Define more data and perform additional setups."""
        x, y = self.rect.topleft
        outline_x = x - 2
        outline_y = y - 2

        width, height = self.image.get_size()
        outline_width = width + 2
        outline_height = height + 2

        self.outline_rect = Rect(
            (outline_x, outline_y), (outline_width, outline_height)
        )
        self.max_health = 100
        self.min_health = 0

        self.update_width()

        if self.thorn_shooter.health:
            self.draw = self.draw_alive

        else:
            self.draw = empty_function

    def update_width(self, amount=0):
        """Increase or decrease health by amount.

        It also updates size according to current health.

        amount (defaults to 0)
            An integer expressing the amount to add or
            subtract (if it is negative) from health.
        """
        if not self.thorn_shooter.health:
            return

        self.thorn_shooter.health += amount
        self.thorn_shooter.health = max(
            min(self.thorn_shooter.health, self.max_health), self.min_health
        )

        self.image.fill(self.fill_color)
        self.image.blit(self.stencil, (self.thorn_shooter.health, 0))

        if not self.thorn_shooter.health:
            self.thorn_shooter.die()
            self.draw = empty_function

    def draw_alive(self):
        """Draw healthbar (used only when alive."""
        super().draw()
        draw_rect(SCREEN, BLACK, self.outline_rect, 2)

    def revive(self):
        """Resets healthbar state to alive."""
        self.draw = self.draw_alive
        self.update_width()
