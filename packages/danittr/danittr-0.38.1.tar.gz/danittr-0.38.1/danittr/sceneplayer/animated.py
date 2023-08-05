"""Facility for simple object display."""

### local imports

from ..config import SCREEN_RECT

from ..common.behaviour import empty_function

from ..appcommon.surf import INVISIBLE_SURF, render_image

from ..appcommon.anim.player.main import AnimationPlayer

from .proc import process_tasks


class AnimatedObject:
    """Animated object to hold animation."""

    def __init__(
        self,
        anim_data_key,
        tasks,
        exchange_pos_attrs=("center", "center"),
        offset=(0, 0),
    ):
        """Create attributes."""
        ### retrieve coordinates name and value for
        ### animated object

        rect_attr, screen_rect_attr = exchange_pos_attrs

        pos_value = getattr(SCREEN_RECT.move(offset), screen_rect_attr)

        ### instantiate animation player

        self.anim_player = AnimationPlayer(
            self, anim_data_key, coordinates_value=pos_value, coordinates_name=rect_attr
        )

        self.anim_player.play()

        ### process tasks
        process_tasks(self, tasks)

    def update(self):
        """Update animation player."""
        self.anim_player.update()

    def draw(self):
        """Call animation player draw method."""
        self.anim_player.draw()
