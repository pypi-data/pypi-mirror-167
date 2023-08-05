"""Facility for a options widgets."""

from functools import partialmethod

### third-party imports

from pygame.mouse import get_pos as get_mouse_pos, get_pressed as get_mouse_pressed
from pygame.draw import rect as draw_rect, line as draw_line

### local imports

from ...config import SCREEN

from ...common.behaviour import empty_function

from ...appcommon.style import give_depth_finish
from ...appcommon.text.main import render_text
from ...appcommon.surf import render_rect

from ...palette import BLACK, WHITE


def get_button(text, topleft, command):
    """Return a button-like object that can be invoked."""
    button = render_text(
        text, 32, return_obj=True, coordinates_value=topleft, foreground_color=WHITE
    )

    button.invoke = command
    button.image = give_depth_finish(button.image)

    # XXX rethink the design in the code below

    # pygame don't handle lambdas well, so using this
    def blit_button():
        """Simple function to blit button."""
        SCREEN.blit(button.image, button.rect)

    button.draw = blit_button
    button.update = empty_function

    return button


class VolumeScale(object):
    """A custom scale widgets from 0.0 to 1.0."""

    def __init__(self, mapping, field, topleft, update_command, feedback_command=None):
        """Assign variables and perform setups.

        mapping
            A dict whose specific field must be updated.
        field
            A string representing a field in a dict which
            must be update.
        topleft
            Topleft attribute for object rect.
        update_command
            Callable to be executed when updating the value.
        feedback_command
            A command to be executed after updating the value.
            Used to provide feedback. Defaults to None
        """
        self.mapping = mapping
        self.field = field
        self.update_command = update_command
        if feedback_command:
            self.feedback_command = feedback_command
        else:
            self.feedback_command = empty_function

        surf = render_rect(540, 50, BLACK)
        self.image = give_depth_finish(surf)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft

        draw_line(self.image, WHITE, (20, 25), (520, 25), 3)
        self.handle = render_rect(16, 16, WHITE, return_obj=True)
        self.place_handle()
        self.mouse_pressed = False

    def place_handle(self):
        """Place handle according to current value."""
        value = self.mapping[self.field]
        int_value = int(value * 100)
        offset_value = int_value * 5

        x = self.rect.x + 20 + offset_value
        y = self.rect.centery
        self.handle.rect.center = (x, y)

    def update(self):
        """Update object state."""
        self.check_handle()

    def draw(self):
        """Draw surfaces."""
        SCREEN.blit(self.image, self.rect)
        SCREEN.blit(self.handle.image, self.handle.rect)

    def check_handle(self):
        """Check if handle is being changed."""
        ### Assigning useful variables
        x, y = get_mouse_pos()
        widget_collided = self.rect.collidepoint(x, y)

        ### Checking scenarios with varying mouse states
        ### Remember: self.mouse_pressed is the state
        ### from previous frame
        if self.mouse_pressed and not widget_collided:
            self.update_value()

            # if mouse cursor leaves widget, even if it
            # is pressed, it must be considered released
            self.mouse_pressed = False
            return

        elif not self.mouse_pressed and not widget_collided:
            return

        # XXX the middle and right variables should be
        # assigned to '_' to indicate they won't be used.

        ### Get current mouse state and assign other variables
        left, middle, right = get_mouse_pressed()

        ### Branching different scenarios and their outcomes
        ### according to mouse state before and now.
        ### nomenclature: scenario -> outcome
        if self.mouse_pressed:
            self.mouse_pressed = left
            if self.mouse_pressed:
                ## pressed before and now -> position handle
                self.handle_to_x(x)
            else:
                ## pressed before and not now -> update value
                self.update_value()

        else:
            self.mouse_pressed = left
            if self.mouse_pressed:
                ## not before, pressed now -> position handle
                self.handle_to_x(x)

        # XXX
        # maybe the no/no scenario could have
        # the handle animated

    def handle_to_x(self, mouse_x):
        """Position handle according to mouse x coordinate.

        mouse_x
            Integer. Mouse x coordinate relative to screen
            and constrained to it.
        """
        left_edge = self.rect.x + 20
        right_edge = self.rect.x + self.rect.w - 20
        if left_edge <= mouse_x <= right_edge:
            self.handle.rect.centerx = mouse_x
        elif mouse_x > right_edge:
            self.handle.rect.centerx = self.rect.x + self.rect.w - 20
        elif mouse_x < left_edge:
            self.handle.rect.centerx = self.rect.x + 20

    def update_value(self):
        """Update mapping[field] using handle position."""
        offset = self.handle.rect.centerx - (self.rect.x + 20)
        value = offset / 500
        self.mapping[self.field] = value
        self.update_command()
        self.feedback_command()

    def increment_amount(self, amount):
        """Increment value according to amount.

        amount
            Any number that can be added to the volume value.
            The result will be clamped to the allowed
            interval [0.0, 1.0] (math notation).
        """
        value = self.mapping[self.field]
        new_value = value + amount
        clamped_value = max(0.0, min(1.0, new_value))
        self.mapping[self.field] = clamped_value
        self.place_handle()
        self.update_value()

    increase = partialmethod(increment_amount, 0.05)
    decrease = partialmethod(increment_amount, -0.05)
