"""Facility for time related custom pygame tools."""

from ..logconfig import APP_LOGGER
from ..config import MILLISECS_PER_FRAME


logger = APP_LOGGER.getChild(__name__)


class TaskManager(object):
    """Manages task objects between differents levels."""

    def __init__(self):
        """Assign variables."""
        self.tasks = []
        self.sendoff_tasks = []

    def clear(self):
        """Set defaults and perform setups."""
        self.tasks.clear()

        for task in self.sendoff_tasks:
            try:
                task()
            except Exception as err:
                err_msg = str(err)
                print(err_msg)
                logger.exception(err_msg)

        self.sendoff_tasks.clear()

    def update(self):
        """Update tasks."""
        finished_tasks = []
        for task in self.tasks:
            try:
                task.update()
            except Exception as err:
                err_msg = str(err)
                print(err_msg)
                logger.exception(err_msg)

                task.finished = True

            if task.finished:
                finished_tasks.append(task)

        for task in finished_tasks:
            self.tasks.remove(task)

    def add_task(self, callable_task, delta_t, unit="milliseconds", cyclic=False):
        """Instantiate and store task. Also return it.

        callable_task
            Callable to be executed when delta_t is reached.
        delta_t
            Milliseconds or frames until execution of
            callable.
        unit
            String hinting if time interval (delta_t) is
            measured in milliseconds or frames.
            Defaults to 'milliseconds'.
        cyclic
            Boolean. If True, the task will execute
            indefinitely, until either its "finished"
            attribute is manually changed to True or
            the task is cleared off the task manager's
            'tasks' attribute. Defaults to False.
        """
        task = TimedTask(callable_task, delta_t, unit, cyclic)
        self.tasks.append(task)

        return task

    def add_sendoff_task(self, callable_task):
        """Store a callable to call before leaving level.

        callable_task
            A callable to be called before exiting a level.
            Callables are executed in the self.clear method.
        """
        self.sendoff_tasks.append(callable_task)


TASK_MANAGER = TaskManager()
add_task = TASK_MANAGER.add_task
add_sendoff_task = TASK_MANAGER.add_sendoff_task
clear_task_manager = TASK_MANAGER.clear
update_task_manager = TASK_MANAGER.update


class TimedTask(object):
    """A task which executes after a time interval.

    Tasks are scheduled either in milliseconds or in frames.
    They can be executed only once or repeatedly.
    """

    # XXX
    # Instead of changing the update method,
    # just change the line where time is incremented
    # by creating a self.increment attribute
    # which is either MILLISECS_PER_FRAME or 1.
    #
    # Also do the same for the execute method, just
    # isolate the line where the finished state is
    # determined.
    #
    # Also, for unit selections use elif unit == "frames";
    # the else option should raise and error

    def __init__(self, callable_task, delta_t, unit="milliseconds", cyclic=False):
        """Assign variables.

        callable_task
            Callable to be executed when delta_t is reached.
        delta_t
            Time interval measured in milliseconds or frames.
        unit
            String hinting if time interval (delta_t) is
            measured in milliseconds or frames.
            Defaults to 'milliseconds'.
        cyclic
            Boolean. If True, the task will execute
            indefinitely, until either its "finished"
            attribute is manually changed to True or
            the level ends. Defaults to False.
        """
        self.finished = False

        self.delta_t = delta_t
        self.invoke = callable_task

        self.start = 0

        if unit == "milliseconds":
            self.update = self.count_milliseconds
        else:
            self.update = self.count_frames

        if cyclic:
            self.execute = self.execute_cycle
        else:
            self.execute = self.execute_once

    def count_milliseconds(self):
        """Count milliseconds to execute task."""
        if self.start >= self.delta_t:
            self.execute()

        self.start += MILLISECS_PER_FRAME

    def count_frames(self):
        """Count frames to execute task."""
        if self.start >= self.delta_t:
            self.execute()

        self.start += 1

    def get_remaining(self):
        """Get remaining time."""
        if not self.finished:
            return self.delta_t - round(self.start)

        else:
            return 0

    def execute_once(self):
        """Execute and finish task."""
        self.invoke()
        self.finished = True

    def execute_cycle(self):
        """Execute and restart another cycle."""
        self.invoke()
        self.start = 0


# XXX
# Future tasks which executes based on conditions
# could be cyclic too. In fact, depending on the
# design it could be possible to generate a great
# amount of possibilities by combining the parameters
# of each kind of task. Ponder.
