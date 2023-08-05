"""Facility for interactive.main.Level class.

Interactive levels are instances of the Level class in this
module. They manage classes which are considered interactive
because the player character can interact with them directly.
This is the level used for the gameplay.
"""

from shutil import copyfile
from os.path import basename, dirname, isfile
from functools import partial, partialmethod

### third-party imports

from pygame import QUIT, KEYDOWN, K_m, K_KP0, K_KP1, K_ESCAPE

from pygame.color import THECOLORS
from pygame.time import set_timer
from pygame.key import get_pressed as get_pressed_keys
from pygame.event import get as get_events, clear as clear_events
from pygame.display import update

### local imports

from ..config import (
    GAME_REFS,
    SCREEN,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SWITCH_LEVEL_TRIGGER,
    RESTART_FROM_SAVE,
    KEYS_MAP,
)

from ..common.math import calculate_jump, unscroll_coordinates
from ..common.behaviour import CallList
from ..common.jsonhandler import load_json, save_json
from ..common.timehandler import get_isostring_datetime

from ..appcommon.task import add_task, update_task_manager, clear_task_manager
from ..appcommon.surf import render_image
from ..appcommon.dialog import clear_messages
from ..appcommon.autoblit import BlitterSet
from ..appcommon.exception import (
    QuitGameException,
    LevelSwitchException,
    RestartLevelException,
    ManagerSwitchException,
)
from ..appcommon.collision import get_objs_onscreen
from ..appcommon.overrider import prepare_script, perform_actions
from ..appcommon.loadscreen import blit_loading_screen

from .classes import get_instance, insert_level_reference, remove_level_reference

from ..player.main import Player

from ..fpsdisplay import fps_display

from .escapemenu import EscapeMenu
from .tabletmenu import TabletMenu

from .scroll import set_scroll_handles
from .groups import set_additional_groups

from ..music import MUSIC_MANAGER
from ..palette import BLACK


# XXX
# maybe in the future use a kind of 'funclist' object,
# a container of callabels whose __call__ method
# causes each callable to be executed, to group
# functionalities that are closely tied together
# like the event and input handling in this class.


class GameLevel(object):
    """A interactive level class."""

    def __init__(self, level_filepath, save_state_filepath, destination=None):
        """Set variables and perform setups.

        level_filepath
            The path of the current level being loaded.
        save_state_filepath
            Filepath for the state.stt json file, which
            contains information of the slot being used
            and other game states and player info/stats.
        destination (defaults to None)
            The bottomleft coordinates wherein to place the
            player when s/he enters a level via some
            kind of entrance. If None, the player will
            be either put on the center of the first screen
            or on the last spot where s/he saved the game.
        """
        self.level_filepath = level_filepath
        self.save_state_filepath = save_state_filepath

        self.level_name = basename(level_filepath)
        self.destination = destination

        self.perform_level_data_setup()
        self.initialize_level()

    # XXX explain why it is important to always use swap
    # files in the docstring below
    def perform_level_data_setup(self):
        """Prepare level and state data structures.

        Here we check for the existence of swap files for
        the level and state file. If they exist, we load
        them, if they don't, we create them. Whichever the
        case, we always work with swap files.
        """
        ### Handle level swap file

        self.level_swap_path = "{}.swp".format(self.level_filepath)

        if not isfile(self.level_swap_path):
            copyfile(self.level_filepath, self.level_swap_path)

        self.level_data = load_json(self.level_swap_path)

        ### Handle state swap file

        self.state_swap_path = "{}.swp".format(self.save_state_filepath)

        if not isfile(self.state_swap_path):
            copyfile(self.save_state_filepath, self.state_swap_path)

        self.save_state_data = load_json(self.state_swap_path)

    def initialize_level(self):
        """Set all variables and instantiate objects.

        This sets all needed data as well as populate
        the level with the needed objects."""
        ### Initial setup

        blit_loading_screen()

        self.horizontal_scroll = self.vertical_scroll = 0

        self.background = render_image("sky_background.png")

        ### Setting game objects grouping

        self.objs_to_scroll = BlitterSet()
        self.huds_group = BlitterSet()

        self.group_names = [
            "back_props",
            "middle_props",
            "actors",
            "equippable_items",
            "blocks",
            "front_props",
        ]

        self.group_map = {}
        self.onscreen_map = {}

        for group_name in self.group_names:

            self.group_map[group_name] = BlitterSet()
            self.onscreen_map[group_name] = BlitterSet()

        insert_level_reference(self)

        for group in self.group_map:
            self.set_group(group)

        set_additional_groups(self)

        ### Setting other objects

        self.set_escape_menu()
        self.set_tablet_menu()

        set_scroll_handles(self)

        self.fps_display = fps_display

        if not self.destination:
            self.scroll(
                self.level_data.get("horizontal_scroll", 0),
                self.level_data.get("vertical_scroll", 0),
            )

        self.set_player()

        MUSIC_MANAGER.cue(self.level_data.get("mood", "casual"))

        ### Store event handling method references

        self.normal_event_handling = CallList(
            [self.act_on_events, self.act_on_key_input]
        )

        ### Assign methods to action routines
        self.get_control()

    def set_group(self, group_name):
        """Configure props in group.

        group_name
            A string representing the name of the group being
            set. This name is defined in the body of the
            initialize_level method.
        """
        group = self.group_map[group_name]
        for obj_data in self.level_data.get(group_name, set()):
            obj = get_instance(obj_data)
            obj.json_data = obj_data
            group.add(obj)

        self.objs_to_scroll |= group

    def add_obj_to_group(self, obj, group_name, at_end=False):
        """Add obj in level relevant groups.

        obj
            Any gaming object.
        group_name
            The name of any gaming set group create in
            self.initialize_level method.
        at_end
            Boolean indicating if the operation should be
            done at the end of the loop or not. Default is
            False so the changes are made immediatelly.
            True should be passed when an object inside
            an specific group wants to add another one
            in the same group in order to prevent the
            group to be changed while we iterate over it.
        """
        if at_end:

            callables = (
                self.group_map[group_name].add,
                self.onscreen_map[group_name].add,
                self.objs_to_scroll.add,
            )

            for callable_task in callables:
                callable_partial = partial(callable_task, obj)
                add_task(callable_partial, 0)

        else:

            self.group_map[group_name].add(obj)
            self.onscreen_map[group_name].add(obj)
            self.objs_to_scroll.add(obj)

    def remove_obj_from_group(self, obj, group_name, at_end=False):
        """Remove obj in level relevant groups.

        obj
            Any gaming object.
        group_name
            The name of any gaming set group create in
            self.initialize_level method.
        at_end
            Boolean indicating if the operation should be
            done at the end of the loop or not. Default is
            False so the changes are made immediatelly.
            True should be passed when an object inside
            an specific group wants to add another one
            in the same group in order to prevent the
            group to be changed while we iterate over it.
        """
        if at_end:

            callables = (
                self.group_map[group_name].remove,
                self.onscreen_map[group_name].remove,
                self.objs_to_scroll.remove,
            )

            for callable_task in callables:
                callable_partial = partial(callable_task, obj)
                add_task(callable_partial, 0)

        else:
            self.group_map[group_name].remove(obj)
            self.onscreen_map[group_name].remove(obj)
            self.objs_to_scroll.remove(obj)

    def set_escape_menu(self):
        """Set an escape menu for system options."""
        self.escape_menu = EscapeMenu(self)

    def set_tablet_menu(self):
        """Set a tablet menu, a gameplay display object.

        The tablet menu as the name implies represents an
        electronic tablet and is as a convenience for
        players to remember gameplay data, check inventory and
        read past disclosed information, etc.
        It isn't absolutely needed in gameplay.
        """
        self.tablet_menu = TabletMenu(self)

    def set_player(self):
        """Configure player.

        The player might need to be placed in a more general
        or specific position, depending on whether
        destination coordinates were provided on the
        __init__ constructor.
        """
        if self.destination:

            for prop in self.group_map["middle_props"]:

                try:
                    if prop.portal_name == self.destination:
                        start_position = prop.rect.bottomleft

                except AttributeError:
                    pass

        else:

            start_position = self.level_data.get("player_position", (640, 360))

        health = self.save_state_data.get("health", 100)
        self.player = Player(
            unscroll_coordinates(start_position),
            level=self,
            state_data=self.save_state_data,
            health=health,
        )

        if self.destination:
            x_scrolling, y_scrolling = calculate_jump(start_position)
            self.scroll(x_scrolling, y_scrolling)

    def get_onscreen_data(self):
        """Separate sprites on the screen.

        This is done whenever the player 'enters' a new
        screen, that is, whenever s/he reaches the edges
        of the screen to enter a new one.

        By separating the sprites on the screen from the
        ones outside we optimize resources by only
        update sprites on the screen (since it doesn't
        make any difference to update sprites we don't
        see, well, in most cases at least).
        """
        for group in self.onscreen_map.values():
            group.clear()

        for group_name in self.group_map:
            group = self.group_map[group_name]
            onscreen_objs = get_objs_onscreen(group)
            self.onscreen_map[group_name] |= onscreen_objs

    def give_up_control(self):
        """Give control to overrider."""
        prepare_script()
        self.control = perform_actions

    def get_control(self):
        """Setup control routines.

        Used when constructing the instance and also when
        getting control back from overrider.
        """
        clear_events()
        self.control = self.normal_event_handling

    def update(self):
        """Update objects in level instance.

        When an instance of this class is the update manager,
        this method will be called. It is responsible for
        updating level objects. However, only those on the
        screen are update in reality to save resources."""
        for group_name in self.group_names:
            self.onscreen_map[group_name].update_objs()
            if group_name == "actors":
                self.player.update()

        self.huds_group.update_objs()

        update_task_manager()

    def draw(self):
        """Draw objects."""
        SCREEN.blit(self.background, (0, 0))

        for group_name in self.group_names:
            self.onscreen_map[group_name].draw_objs()
            if group_name == "actors":
                self.player.draw()

        self.huds_group.draw_objs()

        update()

    def act_on_events(self):
        """Perform actions based on events."""
        for event in get_events():

            if event.type == QUIT:
                raise QuitGameException

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    raise ManagerSwitchException(self.escape_menu)

                elif event.key == KEYS_MAP["advance_deny"]:
                    self.player.skip_interactions()

                elif event.key == KEYS_MAP["accept_prompt"]:
                    self.player.confirm_prompt()

                elif event.key == K_KP0:

                    if self.fps_display in self.huds_group:
                        self.huds_group.remove(self.fps_display)
                    else:
                        self.huds_group.add(self.fps_display)

                elif event.key == K_KP1:

                    if self.scroll_barriers.issubset(self.huds_group):

                        for item in self.scroll_barriers:
                            self.huds_group.remove(item)

                    else:
                        self.huds_group.update(self.scroll_barriers)

                elif event.key == KEYS_MAP["interact"]:
                    self.player.interact()

                elif event.key == KEYS_MAP["fire_item"]:
                    self.player.use_equipped_item()
                # XXX
                # this works, but let's omit it's usage
                # by now.
                # elif event.key == K_m:
                #    raise ManagerSwitchException(
                #                           self.tablet_menu)

                elif event.key == KEYS_MAP["jump"]:
                    self.player.jump()

            elif event.type == SWITCH_LEVEL_TRIGGER:
                self.switch_level()

            elif event.type == RESTART_FROM_SAVE:
                set_timer(RESTART_FROM_SAVE, 0)
                raise RestartLevelException

    def act_on_key_input(self):
        """Perform actions based on key input."""
        key_input = get_pressed_keys()

        player_left, player_right = (
            key_input[KEYS_MAP["player_left"]],
            key_input[KEYS_MAP["player_right"]],
        )

        player_up = key_input[KEYS_MAP["player_up"]]
        player_down = key_input[KEYS_MAP["player_down"]]

        if player_left and not player_right:
            self.player.go_left()

        elif player_right and not player_left:
            self.player.go_right()

        else:
            self.player.stop()

        if player_up and not player_down:
            self.player.up_action()

        elif player_down and not player_up:
            self.player.down_action()

        elif not player_up and not player_down:
            self.player.stand_up()

    def scroll(self, dx, dy):
        """Scroll all objects in x and y amounts.

        dx, dy
            Integers representing scrolling in x and y
            axes, respectively.
        """
        try:
            self.player.finish_dialogue()

        except AttributeError:
            pass

        self.horizontal_scroll += dx
        self.vertical_scroll += dy

        self.objs_to_scroll.scroll(dx, dy)
        self.get_onscreen_data()

    scroll_left = partialmethod(scroll, SCREEN_WIDTH, 0)
    scroll_right = partialmethod(scroll, -SCREEN_WIDTH, 0)
    scroll_up = partialmethod(scroll, 0, SCREEN_HEIGHT)
    scroll_down = partialmethod(scroll, 0, -SCREEN_HEIGHT)

    def switch_level(self):
        """Switch to next level."""
        set_timer(SWITCH_LEVEL_TRIGGER, 0)

        clear_task_manager()
        clear_messages()

        self.save_states_buffer()
        remove_level_reference()

        level_name = GAME_REFS.next_level
        del GAME_REFS.next_level

        raise LevelSwitchException(level_name)

    def pre_saving_routine(self):
        """Execute pre-saving routines on game objects."""
        for obj in self.objs_to_scroll:

            try:
                obj.pre_saving_routine()

            except AttributeError:
                pass

    def save_states_buffer(self):
        """Save level and game states on buffer."""
        ### Level states

        self.level_data["player_position"] = self.player.rect.bottomleft
        self.level_data["horizontal_scroll"] = self.horizontal_scroll
        self.level_data["vertical_scroll"] = self.vertical_scroll

        save_json(self.level_data, self.level_swap_path)

        ### Game states

        self.save_state_data["last_level"] = self.level_name
        self.save_state_data["last_played_datetime"] = get_isostring_datetime()
        self.save_state_data["health"] = self.player.health

        save_json(self.save_state_data, self.state_swap_path)
