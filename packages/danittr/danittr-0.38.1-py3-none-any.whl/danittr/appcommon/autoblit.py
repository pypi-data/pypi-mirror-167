"""Facility with custom objects for easy blitting handling."""

from ..common.wdeque.main import WalkingDeque

### local import
from ..config import SCREEN, SCREEN_RECT


### callables to be bounded on custom containers


def update_objs(self):
    """Call the update method on all objects."""
    for obj in self:
        obj.update()


def draw_objs(self):
    """Call the draw method on all objects."""
    for obj in self:
        obj.draw()


def draw(self):
    """Blit obj.image at obj.rect coordinates.

    Naturally, it should only be used if objects have
    both an image attribute containing a pygame.Surface
    instance and a rect attribute containing a
    pygame.Rect instance.
    """
    for obj in self:
        SCREEN.blit(obj.image, obj.rect)


def draw_on_screen(self):
    """Works as self.draw, but check if obj is onscreen.

    Naturally, it should only be used if objects have
    both an image attribute containing a pygame.Surface
    instance and a rect attribute containing a
    pygame.Rect instance.
    """
    for obj in self.get_on_screen():
        SCREEN.blit(obj.image, obj.rect)


def draw_on_surf(self, surf):
    """Work as self.draw, but blit on specified surf.

    surf
        Any pygame.Surface instance. If such instance is
        also the surface returned by pygame.display.set_mode
        then it is recommended to use the self.draw
        or self.draw_on_screen method instead.
    """
    for obj in self:
        surf.blit(obj.image, obj.rect)


def draw_contained(self, rect):
    """Draw obj on screen if contained in rect.

    rect
        Any instance of pygame.Rect.
    """
    for obj in self:
        if rect.contains(obj.rect):
            SCREEN.blit(obj.image, obj.rect)


def get_on_screen(self):
    """Return iterator with all objects on screen.

    Objects on screen are those which collide with it.
    """
    return (obj for obj in self if SCREEN_RECT.colliderect(obj.rect))


def get_colliding(self, rect):
    """Return iterator of objects which collide with rect.

    rect (instance of pygame.Rect)
    """
    return (obj for obj in self if rect.colliderect(obj.rect))


def get_contained(self, rect):
    """Return iterator of objects contained in the rect.

    rect (instance of pygame.Rect)
    """
    return (obj for obj in self if rect.contains(obj.rect))


def get_unionrect(self):
    """Return union rect of all objects' rects."""
    if len(self):
        rects = [obj.rect for obj in self]
        return rects[0].unionall(rects[1:])

    else:
        raise RuntimeError("Container is empty.")


def get_top(self):
    """Return smaller top coordinate from objects rects."""
    return min(obj.rect.top for obj in self)


def get_bottom(self):
    """Return larger bottom coordinate from objects rects."""
    return max(obj.rect.bottom for obj in self)


def get_left(self):
    """Return smaller left coordinate from objects rects."""
    return min(obj.rect.left for obj in self)


def get_right(self):
    """Return larger right coordinate from objects rects."""
    return max(obj.rect.right for obj in self)


def get_width(self):
    """Return collective width."""
    return self.get_right() - self.get_left()


def get_height(self):
    """Return collective height."""
    return self.get_bottom() - self.get_top()


def move_rects(self, dx, dy):
    """Move all objects' rects in place by dx and dy.

    dx, dy
        Integers indicating how much in pixels the rect of
        each object must be moved."""
    for obj in self:
        obj.rect.move_ip(dx, dy)


def position_rects(self, attr_name, point):
    ### get the union rect
    union_rect = self.get_unionrect()

    ### copy and position union rect
    pos_union_rect = union_rect.copy()
    setattr(pos_union_rect, attr_name, point)

    ### move group objects so topleft points are the same

    start_x, start_y = union_rect.topleft
    end_x, end_y = pos_union_rect.topleft

    delta_x = end_x - start_x
    delta_y = end_y - start_y

    self.move_rects(delta_x, delta_y)


def scroll(self, x, y):
    """Call the scroll method on all objects."""
    for obj in self:
        obj.scroll(x, y)


def collide(self, to_collide):
    """Return all objects colliding with to_collide."""
    # XXX
    # This method will likely change in the near
    # future to accomodate different kinds of objects
    # by calling their own collision methods since
    # objects will now be much more dynamic/different in
    # their nature, assuming various configurations.
    colliding_objs = BlitterSet()
    for obj in self:
        if to_collide.rect.colliderect(obj.rect):
            colliding_objs.add(obj)

    return colliding_objs


def collide_any(self, to_collide):
    """Return an object of self if collides with obj."""
    # XXX
    # This method will likely change in the near
    # future to accomodate different kinds of objects
    # by calling their own collision methods since
    # objects will now be much more dynamic/different in
    # their nature, assuming various configurations.

    for obj in self:
        if to_collide.rect.colliderect(obj.rect):
            return obj

    return None


# XXX
# maybe make more functions to retrieve more position
# data from the object's rects inside containers;
# just using the union rect would be easier, but I wonder
# if it isn't quicker in some cases to just calculate the
# data you need. Must try and profile the options whenever
# convenient;

### custom containers


class BlitterSet(set):
    """Set with methods to draw/update objects."""


class BlitterList(list):
    """List with methods to draw/update objects."""


class BlitterWalkingDeque(WalkingDeque):
    """WalkingDeque with methods to draw/update objects."""


for cls in (BlitterSet, BlitterList, BlitterWalkingDeque):
    cls.update_objs = update_objs
    cls.draw = draw
    cls.draw_objs = draw_objs
    cls.draw_on_screen = draw_on_screen
    cls.draw_on_surf = draw_on_surf
    cls.draw_contained = draw_contained
    cls.get_on_screen = get_on_screen
    cls.get_colliding = get_colliding
    cls.get_contained = get_contained
    cls.get_unionrect = get_unionrect
    cls.get_left = get_left
    cls.get_right = get_right
    cls.get_width = get_width
    cls.get_top = get_top
    cls.get_bottom = get_bottom
    cls.get_height = get_height
    cls.move_rects = move_rects
    cls.position_rects = position_rects
    cls.scroll = scroll
    cls.collide = collide
    cls.collide_any = collide_any

### basic object


class BasicObject:
    """Basic object with methods for blitting."""

    def draw(self):
        """Blit itself on screen w/ image and rect attributes.

        Naturally, it should only be used if objects have
        both an image attribute containing a pygame.Surface
        instance and a rect attribute containing a
        pygame.Rect instance.
        """
        SCREEN.blit(self.image, self.rect)

    def draw_on_screen(self):
        """Works as self.draw, but check if obj is onscreen.

        Naturally, it should only be used if objects have
        both an image attribute containing a pygame.Surface
        instance and a rect attribute containing a
        pygame.Rect instance.
        """
        if SCREEN_RECT.colliderect(self.rect):
            SCREEN.blit(self.image, self.rect)

    def draw_on_surf(self, surf):
        """Work as self.draw, but blit on specified surf.

        surf
            Any pygame.Surface instance. If such instance is
            also the surface returned by
            pygame.display.set_mode then it is recommended
            to use the self.draw or self.draw_on_screen
            method instead.
        """
        surf.blit(self.image, self.rect)
