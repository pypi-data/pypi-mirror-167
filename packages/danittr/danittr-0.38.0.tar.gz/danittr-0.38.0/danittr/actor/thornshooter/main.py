"""Facility for the actors layer."""

from ...appcommon.task import add_task, add_sendoff_task
from ...appcommon.anim.player.main import AnimationPlayer

from .healthbar import HealthBar
from .thornbullet import ThornBullet


# XXX
# I still can't figure out how exactly json data is updated
# real time. I should schedule some experimentation so I
# can understand how everything works.
# edit: Now I understand it: I thought that by simply changing
# json data dict store as an attribute in the game objects
# the swap file were automatically updated. This isn't so.
# Changing the dict values changes the level_data dictionary
# which is an attribute of the level instance. What happens
# is that the level data is then saved before switching levels.
# The only change needed was making sure that the data in the
# json data attribute was changed before being saved in
# the swap file on disk.


class ThornShooter(object):
    """A thorn-shooting static plant."""

    level = None

    def __init__(self, prop_name, coordinates, health, revive_countdown):
        """Assign variables. and perform setups."""
        self.prop_name = prop_name

        self.anim_player = AnimationPlayer(
            self,
            prop_name,
            coordinates_name="bottomleft",
            coordinates_value=coordinates,
        )

        self.anim_player.play()

        self.health = health
        self.revive_countdown = revive_countdown

        self.set_operation_structure()

    def set_operation_structure(self):
        """Set other important operational structutes.

        Those include attributes and other setups.
        """

        self.healthbar = HealthBar(self)

        self.bullet = ThornBullet(self.rect.center, self.level)

        add_sendoff_task(self.store_data)
        self.pre_saving_routine = self.store_data

        if not self.health:
            self.revive_task = add_task(self.revive, self.revive_countdown)

    def update(self):
        """Update object state."""
        if self.health:
            self.bullet.update()

        self.anim_player.update()

    def draw(self):
        """Update object state."""
        if self.health:
            self.bullet.draw()

        self.anim_player.draw()
        self.healthbar.draw()

    def scroll(self, x, y):
        """Scroll by x and y in respective axis.
        x
            Integer indicating scrolling in x axis.
        y
            Integer indicating scrolling in y axis.
        """
        self.rect.move_ip(x, y)

    def die(self):
        """Perform death setups."""
        # XXX
        # some audio/visual feedback code should be here

        self.json_data["revive_countdown"] = self.revive_countdown = 10000
        self.revive_task = add_task(self.revive, self.json_data["revive_countdown"])

    def revive(self):
        """Revive the object."""
        # XXX
        # some audio/visual feedback
        # here
        self.json_data["health"] = self.health = 100
        self.json_data["revive_countdown"] = self.revive_countdown = 0
        self.healthbar.revive()
        self.bullet.reset_position()

    def store_data(self):
        """Store relevant json data."""
        self.json_data["health"] = self.health

        if not self.health:
            self.json_data["revive_countdown"] = self.revive_task.get_remaining()

        else:
            self.json_data["revive_countdown"] = 0

    def suffer_damage(self, damage):
        """Subtract damage from player healthbar."""
        # XXX
        # some audible and visual feedback is desired
        self.healthbar.update_width(-damage)
