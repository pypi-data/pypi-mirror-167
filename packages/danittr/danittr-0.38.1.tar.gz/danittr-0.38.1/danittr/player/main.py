"""Player class facility."""

from types import SimpleNamespace
from random import seed, choice

# third-party imports
from pygame.time import set_timer

# local imports
from ..config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_RECT, RESTART_FROM_SAVE

from ..logconfig import APP_LOGGER

from ..common.math import get_straight_distance
from ..common.behaviour import CallList, empty_function

from ..appcommon.task import add_task
from ..appcommon.overrider import register_actions
from ..appcommon.dialoguefactory import dialoguebox_factory
from ..appcommon.anim.player.main import AnimationPlayer
from ..appcommon.behaviour.switch import set_level_switching

from ..sound import SOUNDS_MAP, set_sounds_volume

from .healthbar import HealthBar
from .dialoguemanager import DialogueManager
from .promptmanager import PromptManager
from .inventorymanager import InventoryManager
from .headsprite import Head
from .equippeddisplay import EquippedDisplay


logger = APP_LOGGER.getChild(__name__)


class Player:
    """The main character in the game: Dani."""

    def __init__(self, start_position, level, state_data, health=100):
        """Initialize superclass and variables."""
        self.anim_player = AnimationPlayer(
            self,
            "dani",
            coordinates_name="bottomleft",
            coordinates_value=start_position,
        )

        self.anim_player.play()

        self.level = level
        self.state_data = state_data
        self.health = health

        self.set_operation_structure()

    def set_operation_structure(self):
        """Set other important operational structures.

        Those include atributes, methods and other objects."""
        ### Instantiate assisting objects

        self.equipped_display = EquippedDisplay()
        self.inventory_manager = InventoryManager(
            self.state_data, self.equipped_display, self
        )

        self.healthbar = HealthBar(self)
        self.player_head = Head()

        ## Send relevant ones to heads-up display

        self.level.huds_group.update(
            [self.healthbar, self.player_head, self.equipped_display]
        )

        ### Define variables for control

        self.x_speed = 0
        self.x_accel = 1
        self.max_walk_speed = 10

        self.y_speed = 0
        self.gravity_accel = 2

        self.climb_speed = 5

        self.facing_right = True

        self.portal_holder = None

        ### Instantiate and setup additional managers

        self.dialogue_manager = DialogueManager(self)
        self.prompt_manager = PromptManager(self)

        ## Send additional managers to heads-up display

        self.level.huds_group.update([self.dialogue_manager, self.prompt_manager])

        dialogue = [
            {"player": "Oh, my bag don't support" " more than six of each item."}
        ]

        self.full_inventory_dialogue = dialoguebox_factory(dialogue)

        ### Set sounds

        seed()
        self.jump_sounds = [SOUNDS_MAP["player_jump01"], SOUNDS_MAP["player_jump02"]]

        ### Set movement routine (behaviour/physics)

        self.default_physics = CallList([self.move_x, self.move_y])

        self.climb_physics = CallList(
            [self.climb_x, self.climb_y, self.check_touching_ladder]
        )

        self.movement_routine = self.default_physics

        ### Set cooldown mechanisms
        self.ladder_to_ground_cooldown = SimpleNamespace(finished=True)

        ### send actions to control overrider to be
        ### referenced when needed
        self.map_actions()

    def update(self):
        """Update player states."""
        self.movement_routine()
        self.manage_animations()
        self.anim_player.update()

    def draw(self):
        """Draw animation."""
        self.anim_player.draw()

    def move_x(self):
        """Calculate and perform movement in x axis."""
        self.rect.x += self.x_speed

        self.check_handle_collision_x()
        self.check_block_collision_x()

    def move_y(self):
        """Calculate and perform movement in y axis."""
        self.apply_gravity_pull()
        self.rect.y += self.y_speed

        self.check_handle_collision_y()
        self.check_block_collision_y()

    def check_handle_collision_x(self):
        """Check for handle collision in x axis."""
        collided_handle = self.level.horizontal_barriers.collide_any(self)

        if collided_handle:
            self.warp_scroll_player(collided_handle)

    def check_handle_collision_y(self):
        """Check for handle collision in y axis."""
        collided_handle = self.level.vertical_barriers.collide_any(self)

        if collided_handle:
            self.warp_scroll_player(collided_handle)

    def check_block_collision_x(self):
        """Check for block collision in x axis."""
        collided_platform = self.level.onscreen_map["blocks"].collide_any(self)

        if collided_platform:
            is_going_right = self.x_speed > 0
            if is_going_right:
                self.rect.right = collided_platform.rect.left
            else:
                self.rect.left = collided_platform.rect.right
            self.x_speed = 0

    def check_block_collision_y(self):
        """Check for block collision in y axis."""
        collided_platform = self.level.onscreen_map["blocks"].collide_any(self)

        if collided_platform:
            # XXX
            # this test probably won't work though if a block
            # hits player's head. Maybe it's better to
            # determine if is hitting ground by the
            # difference between player's and block's topleft
            # rect position. Or maybe I'm just worrying too
            # much, since I don't plan to have blocks falling
            # on the stage.
            hit_ground = self.y_speed > 0

            if hit_ground:
                self.rect.bottom = collided_platform.rect.top

                try:
                    collided_platform.grass_walking(self, self.rect.midbottom)

                except AttributeError:
                    pass

            else:
                self.rect.top = collided_platform.rect.bottom

            self.y_speed = 0

    def climb_x(self):
        """Calculate and perform climbing in x axis."""
        if self.x_speed:
            self.rect.x += self.climb_speed if self.x_speed > 0 else -self.climb_speed

        self.check_handle_collision_x()
        self.check_block_collision_x()
        # must set to 0 only after block collision,
        # since collision mechanism in x axis rely on x_speed
        self.x_speed = 0

    def climb_y(self):
        """Calculate and perform climbing in y axis."""
        if self.y_speed:
            increment = self.climb_speed if self.y_speed > 0 else -self.climb_speed
            self.rect.y += increment
            if self.is_touching_ground():
                self.rect.y -= increment
                self.assign_default_physics()
                if self.ladder_to_ground_cooldown.finished:
                    self.ladder_to_ground_cooldown = add_task(empty_function, 100)

        self.check_handle_collision_y()
        self.check_block_collision_y()
        # must set to 0 only after block collision,
        # since collision mechanism in y axis rely on y_speed
        self.y_speed = 0

    def assign_climbing(self):
        """Check climbing state and assign if needed."""
        if self.movement_routine != self.climb_physics:
            self.movement_routine = self.climb_physics

    def assign_default_physics(self):
        """Check climbing state and assign if needed."""
        if self.movement_routine != self.default_physics:
            self.movement_routine = self.default_physics

    def check_touching_ladder(self):
        """Check if still touching ladders.

        Otherwise revert back to default physics.
        """
        if self.is_touching_ladder():
            pass
        else:
            self.assign_default_physics()

    def warp_scroll_player(self, handle):
        """Warp player according to scroll orientation.

        handle
            An sprite object whose collision is used to
            detect when to scroll the screen. Such
            scrolling is triggered by invoking a special
            method in the handle (but first we warp the
            player)."""
        if handle.rect.midtop == SCREEN_RECT.midtop:
            self.rect.y = SCREEN_HEIGHT - handle.rect.height - self.rect.height

        elif handle.rect.midbottom == SCREEN_RECT.midbottom:
            self.rect.y = handle.rect.height

        elif handle.rect.midright == SCREEN_RECT.midright:
            self.rect.x = handle.rect.width

        elif handle.rect.midleft == SCREEN_RECT.midleft:
            self.rect.x = SCREEN_WIDTH - handle.rect.width - self.rect.width
        handle.invoke()

    def apply_gravity_pull(self):
        """Move player according to gravity force."""
        will_traverse_floor = self.y_speed > self.rect.height

        if not will_traverse_floor:
            self.y_speed += self.gravity_accel

    ### animation management

    def manage_animations(self):
        """Change animation according to states."""
        if not self.is_touching_ground():

            if self.facing_right:
                self.anim_player.ensure_animation("jump")

            else:
                self.anim_player.ensure_animation("jump_reverse")
        else:
            if self.x_speed:

                if self.facing_right and self.x_speed > 0:
                    self.anim_player.ensure_animation("walk")

                elif not self.facing_right and self.x_speed < 0:
                    self.anim_player.ensure_animation("walk_reverse")

                elif self.facing_right and self.x_speed < 0:
                    self.anim_player.ensure_animation("decelerate_reverse")
                else:
                    self.anim_player.ensure_animation("decelerate")

            else:
                if self.is_crouched():
                    pass

                else:
                    if self.facing_right:
                        self.anim_player.ensure_animation("idle")
                    else:
                        self.anim_player.ensure_animation("idle_reverse")

    ### user controlled behaviour
    ### (there's more on interaction section when indicated)

    def go_left(self):
        """Accelerate player to the left."""
        self.facing_right = False
        if self.x_speed > -self.max_walk_speed:
            self.x_speed += -self.x_accel

    def go_right(self):
        """Accelerate player to the right."""
        self.facing_right = True
        if self.x_speed < self.max_walk_speed:
            self.x_speed += self.x_accel

    def stop(self):
        """Decelerate player on x axis."""
        if self.x_speed > 0:
            self.x_speed -= 1
        elif self.x_speed < 0:
            self.x_speed += 1

    def jump(self):
        """Move player contrary to gravity if on ground."""
        if self.is_touching_ground() or self.is_climbing():
            self.assign_default_physics()
            self.y_speed = -26
            # XXX
            # create a container to manage this
            # automatically and also verify
            # busy states to prevent underruns
            # errors (probably? need to know more)
            # The automation part is desired anyway,
            # since this kind of setup should be used
            # lots of times
            choice(self.jump_sounds).play()

    def use_equipped_item(self):
        """Request item to inventory and use if available."""
        item = self.inventory_manager.request_equipped_item()

        if item:

            item.prepare_for_usage(self)
            self.level.add_obj_to_group(item, "equippable_items")

    ### Interaction methods (usually refer other objects)

    def up_action(self):
        """Check for possible actions using up movement.

        Options available depending on conditions:
        - Enter a door/cave/entrance to another level.
        - Climb ladders
        """
        if self.is_touching_ladder():
            self.assign_climbing()
            if not self.is_leaving_ladder():
                self.y_speed = -self.climb_speed
        elif self.is_touching_portal():
            # XXX
            # After entrance animation is timed
            # use said time here before changing level
            # so user see the entrance animation
            # before 'entering'
            portal = self.portal_holder.pop()
            self.portal_holder = None
            after_milliseconds = 100
            distance = get_straight_distance(self.rect.midbottom, portal.rect.midbottom)

            # 38 is arbitrary, just means it's close.
            if distance <= 38 and self.health and self.is_touching_ground():
                set_level_switching(
                    after_milliseconds, portal.next_level, portal.destination
                )

    def down_action(self):
        """Check for possible actions using up movement.

        Options available depending on conditions:
        - Crouch
        - Climb ladders
        """
        if self.is_touching_ground() and not self.x_speed:
            if self.facing_right:
                self.anim_player.ensure_animation("crouched_idle")
            else:
                self.anim_player.ensure_animation("crouched_idle_reverse")

        elif self.is_touching_ladder() and self.ladder_to_ground_cooldown.finished:
            self.assign_climbing()
            self.y_speed = self.climb_speed

    def suffer_damage(self, damage):
        """Subtract damage from player healthbar."""
        # XXX
        # pc should scream lightly but convincingly
        # when taking damage, to inspire sympathy and
        # not scare the player.
        self.healthbar.update_width(-damage)

    # also controlled by user
    def interact(self):
        """Trigger interactions if available.

        This method detects interactive objects near the
        player and trigger whatever interaction they
        may have. Such interactions may include
        dialogues, monologues, getting items, etc."""
        actors_onscreen = self.level.onscreen_map["actors"]
        middle_props_onscreen = self.level.onscreen_map["middle_props"]
        props = []
        props.extend(actors_onscreen)
        props.extend(middle_props_onscreen)

        if props:
            # XXX
            # Change this to not just probe the closest
            # prop, but to keep probing them until it finds
            # one which has interactions (in case the first
            # don't have).
            sprite_distance_pairs = []
            for prop in props:
                distance = get_straight_distance(prop.rect.center, self.rect.center)
                if distance < 128:
                    sprite_distance_pairs.append((prop, distance))

            closer_prop_pair = min(
                sprite_distance_pairs, default=None, key=lambda seq: seq[1]
            )

            if closer_prop_pair:

                closer_prop = closer_prop_pair[0]

                try:
                    closer_prop.receive_interaction(self)
                except AttributeError as err:

                    if "receive_interaction" in str(err):
                        msg = "Expected AttributeError" + " was silenced."
                        logger.info(msg)

                    else:
                        msg = "Unexpected Attribute Error"
                        logger.exception(msg)
                        raise err

    def send_dialogue(self, dialogue):
        """Send dialogue to dialogue_manager."""
        self.dialogue_manager.get_dialogue(dialogue)

    def send_prompt(self, prompt):
        """Send dialogue to dialogue_manager."""
        self.prompt_manager.get_prompt(prompt)

    def confirm_prompt(self):
        """Confirm current prompt, if any."""
        self.prompt_manager.confirm()

    def finish_dialogue(self):
        """Skip entire dialogue."""
        self.dialogue_manager.finish_dialogue()

    def get_item(self, item, report_to=None):
        """Add item on inventory.

        item
            An instance of whichever class can be used as
            an item by player.
        report_to
            A reference to a instance of a class that
            needs to have the execution of this get_item
            method reported. If not provided, we'll
            report the execution to the item itself,
            so it can execute any administrative tasks
            as needed.
        """
        if self.inventory_manager.add(item):

            if report_to:
                report_to.got_item()
            else:
                item.got_item()

    def say_full_inventory(self):
        """Play a 'full inventory' dialogue."""
        self.send_dialogue(self.full_inventory_dialogue)

    ### Support methods

    def is_touching_ground(self):
        """Return True if touching ground."""
        self.rect.y += 2
        platform_bellow = self.level.onscreen_map["blocks"].collide_any(self)
        self.rect.y += -2

        if platform_bellow:
            return True
        else:
            return False

    def is_leaving_ladder(self):
        """Return True if leaving a ladder by going up."""
        self.rect.y += -self.climb_speed
        leaving_ladder = not self.is_touching_ladder()
        self.rect.y += self.climb_speed
        return leaving_ladder

    def is_touching_ladder(self):
        """Return True if touching a ladder."""
        touching_ladder = False

        middle_props = self.level.onscreen_map["middle_props"].collide(self)

        if middle_props:
            touching_ladder = [
                obj for obj in middle_props if "climbable" in obj.prop_name
            ]

        return touching_ladder

    def is_touching_portal(self):
        """Return True if touching a portal."""
        touching_portal = False

        middle_props = self.level.onscreen_map["middle_props"].collide(self)

        # XXX
        # use portal substring to indicate a portal
        # or use a better way if you think of any
        if middle_props:
            touching_portal = [
                obj
                for obj in middle_props
                if obj.prop_name in ("simple_door", "cave_entrance")
            ]
            self.portal_holder = touching_portal

        return touching_portal

    def is_climbing(self):
        """Return True if playing is climbing."""
        return self.movement_routine == self.climb_physics

    def is_crouched(self):
        """Return True if player is crouched."""
        return self.anim_player.anim_name in ("crouched_idle", "crouched_idle_reverse")

    def die(self):
        """Start a death animation and cue level restart.

        Also play a death SFX."""
        # XXX
        # 2018-01-26 06:58:57
        # Death animation trigger here in the future
        # Also adjust milliseconds to allow animation
        # to play through and display some text on screen
        # like "you died", etc.

        # XXX
        # 2018-01-26 06:59:30
        # Death SFX trigger here in the future
        print("Died")
        milliseconds = 2000
        set_timer(RESTART_FROM_SAVE, milliseconds)

    def stand_up(self):
        """Ensures player stand up stance if on ground."""
        if self.is_touching_ground():

            if self.x_speed:

                if self.facing_right:
                    self.anim_player.ensure_animation("walk")

                else:
                    self.anim_player.ensure_animation("walk_reverse")
            else:

                if self.facing_right:
                    self.anim_player.ensure_animation("idle")

                else:
                    self.anim_player.ensure_animation("idle_reverse")

    def skip_interactions(self):
        self.dialogue_manager.skip_dialoguebox()
        self.prompt_manager.finish_prompt()

    def map_actions(self):
        """Create map and pass to control overrider.

        This map may be used by the control overrider class
        to control player behaviour.
        """
        actions = {
            "advance_deny": self.skip_interactions,
            "interact": self.interact,
            "fire_item": self.use_equipped_item,
            "jump": self.jump,
            "player_left": self.go_left,
            "player_right": self.go_right,
            "stop": self.stop,
        }

        register_actions("player", actions)
