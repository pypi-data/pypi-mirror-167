"""Facility for action controlling during gameplay."""

from pygame.event import pump


class ControlOverrider:
    """An object to control and/or record gameplay actions.

    It should be used to control game objects actions
    for various purposes.

    E.g.: to create in-game cutscenes; or to record
    action sequences for playtesting or to simulate
    AI/animate objects.

    By now it can only play predefined scripts, but
    the goal is to make it read custom formated data
    either provided by the user or recorded from
    object actions.

    The mechanism used is fairly simple. The
    gamelevel.main.Level instance let's the
    overrider override it's event handling/key input
    handling methods, accepting actions performed by
    the overrider. The rest of the game objects behaves
    either naturally by their own update mechanisms or
    they also may have such mechanisms overridden by
    the overrider, depending on your need of control.

    Control swap between the level instance and overrider
    may be performed by the overrider itself or by other
    objects depending on conditions or timing. The class
    already works, but it is too 'green' yet and there's
    still other user cases to be implement. Thus, this class
    must be expected to change a lot while I incrementally
    develop/redesign it over and over, along with its
    dependencies.
    """

    def __init__(self):
        """Create object."""
        self.actions_map = {}

    def register_actions(self, key, actions):
        """Store actions in the action map."""
        self.actions_map[key] = actions

    def define_script(self, script):
        """Define a script (detailed steps) for execution.

        Such script must explain the actions to be performed
        from the moment the overrider takes over until it
        gives control back to the level.

        The control switching isn't necessarily present
        in the instruction set and may be performed by
        other objects, specially when events are 'chained'
        together (the execution of one is only triggered
        after the execution of a previous one), in which
        case providing a step by step 'guide' isn't needed,
        just the first one is enough (since it will
        automatically call further steps).

        script
            Either a string hinting predefined actions or
            all actions to be performed. For now only the
            string case is being treated.
        """
        if script == "stand_still":
            self.keys = ("player", "stop")

    def prepare_script(self):
        """Store action in the execute script attribute."""
        key1, key2 = self.keys
        self.execute_script = self.actions_map[key1][key2]

    def perform_actions(self):
        """Perform scripted actions.

        Such actions consist of the execution of
        instance methods of the objects the overrider is
        controlling according to a script (script as in
        performance/plays, not as in programming).
        """
        ### Administrative task to keep event queue "healthy"
        pump()
        self.execute_script()


OVERRIDER = ControlOverrider()

register_actions = OVERRIDER.register_actions
define_script = OVERRIDER.define_script
prepare_script = OVERRIDER.prepare_script
perform_actions = OVERRIDER.perform_actions


# XXX
# When the class expands enough,
# remember to clear its "cache" whenever
# switching levels.
