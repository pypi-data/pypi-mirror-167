"""Facility for the back_props layer."""

from os.path import join, dirname

### third-party imports

from pygame.draw import rect as draw_rect
from pygame.image import save as save_image
from pygame.transform import scale as scale_surface

### local imports

from ..config import SCREEN

from ..appcommon.surf import INVISIBLE_SURF
from ..appcommon.task import add_task
from ..appcommon.overrider import define_script
from ..appcommon.promptfactory import prompt_factory
from ..appcommon.behaviour.save import save_game
from ..appcommon.anim.player.main import AnimationPlayer

from ..common.math import unscroll_coordinates

from ..palette import BLACK


# XXX
# This class animation uses repeated unnecessarily
# pre-created surfaces (like transparent ones),
# repeating them too. Fix this.


class SatelliteDish:
    """A satellite dish which performs progress saving."""

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

        self.set_operational_structure()

    def set_operational_structure(self):
        """Set additional objects with which to work."""
        ## prepare prompt
        object_screen_midtop = unscroll_coordinates(self.rect.midtop)

        offset_screen_midtop = (object_screen_midtop[0], object_screen_midtop[1] - 32)
        item_list = [INVISIBLE_SURF]
        prompt_pair = prompt_factory(
            "Should I save my progress?", offset_screen_midtop, item_list
        )
        prompt_action = self.trigger_game_saving
        self.prompt = (prompt_pair, prompt_action)

    def update(self):
        """Update object state."""
        self.manage_animations()
        self.anim_player.update()

    def draw(self):
        """Draw animation."""
        self.anim_player.draw()

    def manage_animations(self):
        """Select suitable animation according to state."""
        anim_name = self.anim_player.anim_name
        loops_no = self.anim_player.peek_next_loops_no()

        if anim_name == "activating":

            if loops_no >= 1:
                self.anim_player.switch_animation("activated")

        elif anim_name == "activated":

            if loops_no >= 3:

                self.save_game()

                # XXX
                # Before this must play deactivating anim
                # maybe should also make player say
                # something like "great, now my progress is
                # saved!"
                # Also add sounds etc. in the method where
                # needed.
                self.anim_player.switch_animation("idle")
                self.level.get_control()

    def scroll(self, x, y):
        """Scroll by x and y in respective axis.
        x
            Integer indicating scrolling in x axis.
        y
            Integer indicating scrolling in y axis.
        """
        self.rect.move_ip(x, y)

    def receive_interaction(self, player):
        """Send prompt to player state manager."""
        player.send_prompt(self.prompt)

    def trigger_game_saving(self):
        """Setup a game saving script and execute it."""
        define_script("stand_still")

        self.level.give_up_control()
        self.anim_player.switch_animation("activating")

    def save_game(self):
        """Save game and level states and give feedback."""
        self.level.pre_saving_routine()
        self.level.save_states_buffer()

        save_game()

        add_task(self.store_thumbnail, 0, unit="frames")

        print("The game was saved.")

    def store_thumbnail(self):
        """Stores a thumbnail in the save directory."""
        save_dir = dirname(self.level.save_state_filepath)
        thumb_path = join(save_dir, "thumb.png")

        thumb = scale_surface(SCREEN, (640, 360))
        draw_rect(thumb, BLACK, thumb.get_rect(), 5)
        save_image(thumb, thumb_path)
