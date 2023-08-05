"""General utilities for the animation player."""

from abc import ABC
from functools import partial, partialmethod
from operator import attrgetter

### local import
from ....common.behaviour import empty_function, get_nested_value


class Utilities(ABC):
    """Provides utilities for the animation manager."""

    def jump_to_frame(self, frame_index):
        """Jump animation to frame_index by rotating values.

        frame_index (integer)
            Represents the frame to which we want to jump.
            Can be any value, but it will be clamped to the
            animation length range.

        Jumps to an specific frame, regardless of whether
        the animation is being played or paused.
        """
        ### clamp index to allowed range
        # (obs.: if needed elsewhere, turn this section into
        # its own method)

        max_index = self.get_animation_length() - 1
        clamped_index = max(min(max_index, frame_index), 0)

        ### calculate the difference between the desired
        ### frame (the clamped frame index) and the current
        ### frame number; such difference represents
        ### the number of steps to walk
        steps = clamped_index - self.get_current_frame()

        ### finally update the animation values in the nodes
        ### after the specified number of steps
        ### calculated above, that is, until reaching the
        ### desired values; the equivalent of jumping to
        ### the desired frame;
        self.update_nodes(steps)

    def get_animation_length(self):
        """Return length of current animation."""
        return self.anim_clock.length

    def get_current_frame(self):
        """Return current frame of animation clock."""
        return self.anim_clock.get_index_of_first()

    def get_current_loops_no(self):
        """Return number of loops performed."""
        return self.anim_clock.loops_no

    def peek_loops_no(self, steps):
        """Return loops number after temporary rotation.

        steps (integer)
            Number of rotations to go back or forth
            (depending on signal) before peeking.

        We do so by calling an eponymous method in the
        in the animation clock and returning its return
        value.
        """
        return self.anim_clock.peek_loops_no(steps)

    peek_next_loops_no = partialmethod(peek_loops_no, 1)
    peek_after_next_loops_no = partialmethod(peek_loops_no, 2)

    def ensure_animation(self, animation_name):
        """Only switch if given animation != current one.

        Also return the value returned by the
        switch_animation method, which is True when
        the operation succeeds.

        animation_name (string)
            represents the unique name of an animation.
        """
        if animation_name != self.anim_name:
            return self.switch_animation(animation_name)

    ### frame playback options

    def play(self):
        """Start playing animation.

        This is done by setting the step_forth method
        into the update attribute. This is usually the
        desired behaviour, since it will keep looping the
        current animation indefinitely.
        """
        self.update = self.step_forth

    def pause(self):
        """Pause the animation.

        This is done by setting the update_nodes method
        into the update attribute. This means the
        animation will be updated with the same values
        every frame instead of successively walk through
        the animation values, which will make the animation
        appear frozen since we just assign the same values
        again and again, for both surfaces and positions.
        """
        self.update = self.update_nodes

    def is_paused(self):
        """Return True if animation is paused.

        That is, if update attribute is set to
        the update_nodes method.
        """
        return self.update == self.update_nodes

    def toggle_play(self):
        """Toggle behaviour between play/pause state."""
        if self.is_paused():
            self.play()
        else:
            self.pause()

    ### drawing related options

    def check_walking_skipping(self):
        """Check need to prevent walking on first frame.

        When we switch to a new animation when not paused,
        the first execution of the update routine would
        naturally cause the animation values of the first
        frame to be skipped when the timing indices rotate
        using the WalkingDeque.walk method.

        To prevent that, we check if it is the case here
        (the animation is not paused) and if so we set a
        special method, called skip_walking, in lieu of the
        current update routine. Such special method prevents
        the undesired behaviour described above.

        One additional condition, though, is that the
        special method must not be set yet, since setting
        the special method again would cause another
        undesired effect described in the is_skipping
        method.

        Once the conditions above are met, before setting
        the special method, we store a reference to the
        current udpate routine, so it can be restored later.
        """
        ### if not paused nor skipping, store current update
        ### routine and assign the skip_walking in its place
        if not self.is_paused() and not self.is_skipping():

            self.previous_update_routine = self.update

            self.update = self.skip_walking

    def is_skipping(self):
        """Return True if skip_walking is set.

        This is used to prevent trying to set the
        skip_walking method again when it is already set.

        Since the skip_walking method automatically sets the
        update routine to its previous value, if the
        previous value of the update routine was itself,
        the routine would keep setting itself as the update
        routine indefinitely.
        """
        return self.update == self.skip_walking

    def skip_walking(self):
        """Update w/out walking and revert update routine."""
        self.update_nodes()
        self.update = self.previous_update_routine

    def stop(self):
        """Pause and walk to the beginning of animation."""
        self.pause()
        self.go_to_beginning()

    def go_to_beginning(self):
        """Clear rotation and update node values.

        By doing so, it has the same effect as having the
        animation go to the beginning (regardless of whether
        its paused or not).
        """
        self.clear_rotations()
        self.update_nodes()

    def set_draw_routine(self, routine_name):
        """Set drawing routine, return True if succeed.

        routine_name (string)
            Attribute name of the draw routine. It should
            have one of the following values:

            - 'draw_nodes'
                Set the draw_routine to draw only nodes.
                This is the default behaviour.
            - 'draw_nodes_and_bounding_rect'
                Set the draw routine to draw both the
                nodes and also their bounding rects.
            - 'draw_nodes_and_col_rect'
                Set the draw routine to draw both the
                nodes and also their collision rects,
                if they have them.
        """
        ### routine_name value checking

        if routine_name in (
            "draw_nodes",
            "draw_nodes_and_bounding_rect",
            "draw_nodes_and_col_rect",
        ):

            ## routine assignment
            self.draw = getattr(self, routine_name)

            ## indicate success
            return True

    ### data queries

    def get_nodes(self, exclude_root=False, order="node_names", reverse=False):
        """Return nodes for current animation.

        exclude_root (boolean - default is False)
            whether root should be excluded or not in the
            nodes returned.
        order (string - default is 'node_names')
            represents the order in which node references
            must be arranged.
        reverse (boolean - default is False)
            wether to keep the chosen ordering or reverse it.
        """
        ### order value checking

        legal_values = ("node_names", "updating_order", "drawing_order")

        if order in legal_values:

            ### create slice object according to need of
            ### reversing order or not

            last_param = -1 if reverse else None
            slice_obj = slice(None, None, last_param)

            ### retrieve attribute using order and slice
            order = getattr(self, order)[slice_obj]

            ### get the node references
            nodes = map(self.node_map.__getitem__, order)

            ### return nodes with/without root depending on
            ### exclude_root parameter

            if exclude_root:
                return (node for node in nodes if node is not self.root)

            else:
                return nodes

        else:
            raise ValueError("order must be in one of: " + str(legal_values))
