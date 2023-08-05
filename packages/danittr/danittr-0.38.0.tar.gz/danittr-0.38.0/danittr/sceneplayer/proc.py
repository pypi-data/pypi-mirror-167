"""Task processment facility for the scene player."""

from functools import partial

### local import
from ..appcommon.task import add_task


# TODO finish this


def process_tasks(obj, tasks):
    """Add tasks to the update manager related to the object.

    obj (either a sceneplayer.simple.SimpleObject or a
         sceneplayer.animated.AnimatedObject instance)

    tasks (list)
        each item contain data to create a task.
    """
    for data in tasks:

        ### create executable according to task name

        name = data["name"]

        if name == "visibility_on":
            callable_ = obj.visibility_on

        elif name == "visibility_off":
            callable_ = obj.visibility_off

        elif name == "switch_anim":

            anim_name = data["anim_name"]

            callable_ = partial(obj.anim_player.switch_animation, anim_name)

        ### add task with proper time unit

        try:
            delta_t = data["milliseconds"]
            unit = "milliseconds"

        except KeyError:
            delta_t = data["frames"]
            unit = "frames"

        add_task(callable_, delta_t, unit)
