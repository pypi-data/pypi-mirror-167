"""Mushroom item class facility."""

from ..logconfig import APP_LOGGER
from ..appcommon.anim.player.main import AnimationPlayer
from ..appcommon.collision import does_touch_screen
from ..frontprop.toxicpollencloud import ToxicPollenCloud


logger = APP_LOGGER.getChild(__name__)


class Mushroom:
    """A mushroom equipabble item.

    It's a projectile item whose orientation (left or right)
    is controlled by the player orientation.

    It is thrown a little over the player head and its
    trajectory is controlled by the gravity, making it
    form arc like trajectory.

    Whenever it hits a block or actor it bursts into a
    circular-shaped cloud which deals a little damage
    in touching actors.

    It uses an update_manager analogy to manage different
    scenarios: mushroom on plant vs mushroom being used.
    When on inventory, the object doesn't have its state
    updated on each loop, just stays there not being updated
    until it is finally used, switching to the proper state.
    """

    def __init__(self, prop_name, coordinates, level, plant=None):
        """Initialize superclass and variables.

        prop_name
            A string representing the prop name.
        coordinates
            List or tuple of x and y coordinates
            representing the desired topleft coordinates
            for the rect attribute.
        level
            Instance of gamelevel.main.Level class.
        plant
            If the mushroom was instantiated on a mushroom
            plant, then a reference to the plant instance
            must be provided.
        """
        self.prop_name = prop_name

        self.anim_player = AnimationPlayer(
            self,
            prop_name,
            coordinates_name="bottomleft",
            coordinates_value=coordinates,
        )

        self.level = level
        self.plant = plant
        self.set_operation_structure()

    def set_operation_structure(self):
        """Set other important operational structures.

        Those include atributes, methods and other objects."""
        self.top_speed = 10
        self.x_speed = 0
        self.x_acceleration = 1

        self.y_speed = 0
        self.gravity_accel = 2

        self.facing_right = True
        self.is_burst = False

        self.toxic_pollen_cloud = ToxicPollenCloud(
            "toxic_pollen_cloud", self.rect.topleft, self.level
        )
        self.anim_player.play()

    def prepare_for_plant(self):
        """Make it mushroom plant-ready."""
        self.rect.x += 6
        self.rect.y += 56

        self.anim_player.switch_animation("growing")
        self.update_method = self.update_on_plant

    def prepare_for_usage(self, player):
        """Make it usage ready.

        player
            An instance of player.main.Player class.
        """
        if player.facing_right:
            self.facing_right = True
            self.x_speed = 10
            self.anim_player.switch_animation("thrown")
            self.rect.bottomleft = player.rect.topright

        else:
            self.facing_right = False
            self.x_speed = -10
            self.anim_player.switch_animation("thrown_reverse")
            self.rect.bottomright = player.rect.topleft

        self.y_speed = -26
        self.update_method = self.update_for_usage

    def update(self):
        """Execute method stored in update_method."""
        self.update_method()
        self.manage_animations()
        self.anim_player.update()

    def draw(self):
        """Draw animation."""
        self.anim_player.draw()

    ### XXX
    ### entire class needs refactoring, but specially these
    ### two methods below and their dependencies

    def update_on_plant(self):
        """Do nothing."""

    def update_for_usage(self):
        """Update item when being used by player."""
        self.move_x()
        self.move_y()

    def manage_animations(self):
        """Select specific animation based on state."""
        # XXX
        # Maybe turn this kind of animation branching
        # into a mini language that can be used to set
        # custom behaviours by giving sequences of
        # animations to animation player;
        # push the matter further, it could even be
        # implemented on the .gameobj file too, maybe.

        anim_name = self.anim_player.anim_name

        if anim_name == "growing":

            loops_no = self.anim_player.peek_next_loops_no()

            if loops_no >= 1:
                self.anim_player.switch_animation("idle")
                self.plant.choose_interaction_method()

        elif anim_name == "bursting":

            loops_no = self.anim_player.peek_after_next_loops_no()

            if loops_no >= 1:
                self.spawn_pollen_cloud()
                self.level.remove_obj_from_group(self, "equippable_items", True)

    def move_x(self):
        """Calculate and perform movement in x axis."""
        if self.is_burst:
            return

        self.rect.x += self.x_speed

        for group_name in ("blocks", "actors"):
            collided_prop = self.level.onscreen_map[group_name].collide_any(self)
            if collided_prop:
                self.burst()
                break

        if not self.is_burst:
            if self.rect.colliderect(self.level.player.rect):
                self.burst()

        if not self.is_burst:
            if not does_touch_screen(self):
                self.burst()

    def move_y(self):
        """Calculate and perform movement in y axis."""
        if self.is_burst:
            return

        self.apply_gravity_pull()
        self.rect.y += self.y_speed

        for group_name in ("blocks", "actors"):
            collided_prop = self.level.onscreen_map[group_name].collide_any(self)
            if collided_prop:
                self.burst()
                break

        if not self.is_burst:
            if self.rect.colliderect(self.level.player.rect):
                self.burst()

        if not self.is_burst:
            if not does_touch_screen(self):
                self.burst()

    def apply_gravity_pull(self):
        """Move player according to gravity force."""
        will_traverse_floor = self.y_speed > self.rect.height

        if not will_traverse_floor:
            self.y_speed += self.gravity_accel

    def grow(self):
        """Set the current state to 'growing'."""
        self.anim_player.switch_animation("growing")

    def burst(self):
        """Burst the item."""
        self.is_burst = True
        self.anim_player.switch_animation("bursting")

    def spawn_pollen_cloud(self):
        """Insert toxic pollen cloud into level."""
        self.toxic_pollen_cloud.prepare_to_enter(self)

        self.level.add_obj_to_group(self.toxic_pollen_cloud, "front_props")

    def scroll(self, x, y):
        """Scroll by x and y in respective axis.
        x
            Integer indicating scrolling in x axis.
        y
            Integer indicating scrolling in y axis.
        """
        self.rect.move_ip(x, y)
