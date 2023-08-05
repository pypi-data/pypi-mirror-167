"""Mushroom item class facility."""

from ..logconfig import APP_LOGGER
from ..appcommon.anim.player.main import AnimationPlayer


class ToxicPollenCloud:
    """A circular-shaped toxic cloud of pollen.

    It deals a little damage in touching actors or player.
    It exists as an attribute of a Mushroom instance until
    said instance hits the ground as a projectile. When this
    happens, this pollen cloud enters the game world
    via the level method 'add_obj_to_group'.
    """

    level = None

    def __init__(self, prop_name, coordinates, level):
        """Initialize object."""
        self.prop_name = prop_name
        self.anim_player = AnimationPlayer(
            self, prop_name, coordinates_name="topleft", coordinates_value=coordinates
        )

        self.set_operation_structure()

    def set_operation_structure(self):
        """Set other important operational structures.

        Those include atributes, methods and other objects."""
        self.damage = 1
        self.facing_right = True

        self.anim_player.switch_animation("appearing")
        self.anim_player.play()

    def prepare_to_enter(self, mushroom):
        """Make it so it's ready to enter game world."""
        self.rect.center = mushroom.rect.center
        self.facing_right = mushroom.facing_right

    def update(self):
        """Execute current update_method method."""
        self.manage_animations()
        self.anim_player.update()
        if self.anim_player.anim_name in ("idle", "idle_reverse"):
            self.damage_live_objects()

    def draw(self):
        """Draw animation."""
        self.anim_player.draw()

    def manage_animations(self):
        """Select suitable animation according to state."""
        anim_name = self.anim_player.anim_name

        if anim_name == "appearing":

            loops_no = self.anim_player.peek_next_loops_no()

            if loops_no >= 1:

                if self.facing_right:
                    self.anim_player.switch_animation("idle")
                else:
                    self.anim_player.switch_animation("idle_reverse")

        elif anim_name in ("idle", "idle_reverse"):
            loops_no = self.anim_player.peek_next_loops_no()
            if loops_no >= 3:
                self.anim_player.switch_animation("disappearing")

        elif anim_name == "disappearing":
            loops_no = self.anim_player.peek_after_next_loops_no()
            if loops_no >= 1:
                self.level.remove_obj_from_group(self, "front_props", True)

    def damage_live_objects(self):
        """Damage close objects."""
        colliding_sprites = []

        colliding_actors_onscreen = self.level.onscreen_map["actors"].collide(self)
        colliding_sprites.extend(colliding_actors_onscreen)

        player = self.level.player
        if self.rect.colliderect(player.rect):
            colliding_sprites.append(player)

        for sprite in colliding_sprites:

            try:
                sprite.suffer_damage(self.damage)

            except AttributeError:
                # XXX
                # filter this better for the abovementioned
                # method. Also add logging (maybe?!).
                pass

    def scroll(self, x, y):
        """Scroll by x and y in respective axis.
        x
            Integer indicating scrolling in x axis.
        y
            Integer indicating scrolling in y axis.
        """
        self.rect.move_ip(x, y)
