"""Facility for scene playing."""

from os.path import join

### third-party imports

from pygame import QUIT, KEYDOWN, K_SPACE

from pygame.display import update
from pygame.event import get as get_events
from pygame.time import set_timer

### local imports

from ..config import GAME_REFS, SCENES_DIR, SCREEN, SCREEN_RECT, SWITCH_LEVEL_TRIGGER

from ..common.jsonhandler import load_json

from ..appcommon.task import update_task_manager, clear_task_manager
from ..appcommon.surf import render_rect
from ..appcommon.dialog import clear_messages
from ..appcommon.autoblit import BlitterSet
from ..appcommon.exception import QuitGameException, ManagerSwitchException

from ..appcommon.behaviour.switch import set_level_switching

from ..music import MUSIC_MANAGER
from ..palette import BLACK

from .simple import SimpleObject
from .animated import AnimatedObject

from ..logconfig import APP_LOGGER

logger = APP_LOGGER.getChild(__name__)


class ScenePlayer:
    """An update manager which displays timed media.

    This is a generic update manager for sections of the
    game which only require showing and hiding media in given
    intervals (for instance, logo screen, etc.).
    """

    def __init__(self, scene_filename):
        """Assign variables and perform setups.

        scene_filename (string)
            Used to retrieve data about the scene.
        """
        scene_path = join(SCENES_DIR, scene_filename)
        self.scene_data = load_json(scene_path)

        self.set_scene()

    def set_scene(self):
        """Set flags, create objects, set events."""
        ### set flag to (dis)allow skipping scene
        self.can_skip = self.scene_data.get("can_skip")

        ### set music

        mood = self.scene_data.get("mood", "casual")
        MUSIC_MANAGER.cue(mood)

        ### set background

        background_color = self.scene_data.get("background_color", BLACK)

        self.background = render_rect(*SCREEN_RECT.size, background_color)

        ### set objects
        self.set_objects()

        ### set events
        self.set_events()

    def set_objects(self):
        """Set objects."""
        self.objects = BlitterSet()

        for obj_data in self.scene_data["objects"]:

            ### get obj type
            obj_type = obj_data["obj_type"]

            ### store condition
            is_simple = obj_type.lower() == "simple"

            ### pick proper class according to condition
            instantiator = SimpleObject if is_simple else AnimatedObject

            ### retrieve keyword arguments
            kwargs = obj_data["kwargs"]

            ### instantiate and add object

            obj = instantiator(**kwargs)

            self.objects.add(obj)

    def set_events(self):
        """Set events on a timer."""

        # TODO instead of calling set_level_switching
        # here, which uses milliseconds, create a
        # partial with the values and add it as a
        # task in the task manager (with an small delay
        # of half a second, maybe)
        # This is better than relying on the milliseconds
        # count which might be off if the CPU delays
        # execution (for instance, due to many apps
        # open at the same time); the time in milliseconds,
        # when present, could be converted into frames and
        # be added as a task the same way;

        for event in self.scene_data["events"]:

            if event["name"].lower() == "switch_level":

                milliseconds = event["milliseconds"]
                level_name = event["level_name"]

                set_level_switching(milliseconds, level_name)

    def control(self):
        """Update manager based on event_queue."""
        for event in get_events():

            if event.type == QUIT:
                raise QuitGameException

            elif event.type == SWITCH_LEVEL_TRIGGER:
                self.switch_level()

            elif event.type == KEYDOWN:
                if event.key == K_SPACE and self.can_skip:
                    self.switch_level()

    def update(self):
        """Update menu objects."""
        self.objects.update_objs()
        update_task_manager()

    def draw(self):
        """Draw objects and update screen."""
        SCREEN.blit(self.background, (0, 0))
        self.objects.draw_objs()

        update()

    def switch_level(self):
        """Switch to next level."""
        set_timer(SWITCH_LEVEL_TRIGGER, 0)

        clear_task_manager()
        clear_messages()

        level_name = GAME_REFS.next_level
        del GAME_REFS.next_level

        raise ManagerSwitchException(level_name)
