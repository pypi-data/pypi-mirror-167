"""Facility for animation playback."""

from copy import deepcopy
from functools import partialmethod

### third-party import
from pygame.draw import rect as draw_rect

### local imports

from ....config import SCREEN

from ..node import Node
from ...resources import ANIM_DATA_MAP

from ....palette import ORANGE, RED

## animation player class extension
from .utils import Utilities


# XXX maybe: turn the anim_name attribute into a property,
# making it so that setting it causes the set animation
# behaviours to be executed (after verifying if animation
# name exists); ponder; I'm not fond of this though,
# because this kind of setup means extra overhead for
# real time processing (even if just a little);


class AnimationPlayer(Utilities):
    """Plays animation.

    This object receives a filepath and passes it to
    a factory function used to generate animation
    data. The animation data is then used to instantiate
    support objects called nodes which are arranged in
    tree-like structures to play different animations
    which consist of objects having surfaces and/or
    positions constantly changed to convey the illusion
    of animation.

    The animation manager is part of the .ani2d interface,
    which consists of a data model and a set of modules
    and applications to allow easy and modular animation
    management (creation, edition and playback). The .ani2d
    interface is quite extensive, making it unpractical to
    cover everything here.

    Proper comprehensive documentation is provided here:
    appcommon/anim/ani2d_interface.rst
    """

    def __init__(self, game_obj, anim_data_key, coordinates_value, coordinates_name):
        """Store data and perform setups.

        game_obj (any 'object' subclass)
            object to hold the root node rect, that is, the
            'link' between the game/application world and the
            animation manager.
        anim_data_key (string)
            represents a key to retrieve the .ani2d
            pre-processed animation data from a map.
        coordinates_value (2-tuple or list with 2 integers)
            holds the x and y value of a position in
            two dimensions.
        coordinates_name (string)
            attribute name of a pygame.Rect instance wherein
            to store the coordinates_value (for instance
            "topleft").
        """
        ### store game_obj reference
        self.game_obj = game_obj

        ### setup animation data and nodes

        ## retrieve the pre-processed animation data
        ## using the provided key
        anim_data = ANIM_DATA_MAP[anim_data_key]

        ## retrieve and store animation data

        self.values = anim_data["values"]
        self.structure = anim_data["structure"]
        self.metadata = anim_data["metadata"]
        self.nodes_data = anim_data["nodes"]

        # the timing data must be deepcopied, though;
        # the animation timing is what makes each instance
        # independent from the others;
        self.timing = deepcopy(anim_data["timing"])

        ## create a mapping with animation nodes

        self.node_map = {
            node_name: Node(node_name, node_data)
            for node_name, node_data in self.nodes_data.items()
        }

        ## create a set of animation names
        self.anim_names = set(self.structure.keys())

        ### set default behaviours

        self.pause()
        self.set_draw_routine("draw_nodes")

        ### set current animation

        ## choose animation name and switch to it

        # pick either "idle", or the first one from a
        # tuple with the animation names
        anim_name = "idle" if "idle" in self.anim_names else (*self.anim_names,)[0]

        # then switch to the chosen animation
        self.switch_animation(anim_name)

        ### position game_obj

        setattr(self.game_obj.rect, coordinates_name, coordinates_value)

    ### animation switching support

    def switch_animation(self, animation_name):
        """Switch current animation to requested one.

        Also return True if succeed.

        animation_name (string)
            represents the name of an animation.

        If the animation name provided doesn't exist,
        just print the error and do nothing.
        """
        ### check if the animation structure data is present
        ### (in practice, there are other requirements for
        ### an animation to be deemed playable, but since
        ### those are already pre-checked in the animation
        ### data processing, we do a very simplified checkup
        ### here for the sake of efficiency)
        try:
            self.structure[animation_name]

        ### if absent, then deem the data to play the
        ### animation insufficient
        except KeyError:
            print(
                "Didn't manage to find enough data to play",
                "the animation called",
                animation_name,
            )

        ### otherwise, perform the needed setups to leave
        ### the animation ready for being played and
        ### return True
        else:

            ## store the animation name
            self.anim_name = animation_name

            ## clear the rotation in all timing indices,
            ## to guarantee we are starting from the first
            ## index of animation
            self.clear_rotations()

            ## make all needed setups to ensure the
            ## animation follows it structure
            self.set_root_and_structure()

            ## update nodes without walking the animation
            ## values (that is, without passing a step
            ## argument), to ensure the animation values
            ## for the first frame are assigned to the
            ## nodes
            self.update_nodes()

            ## store an animation clock to use as reference
            ## for the animation timing
            self.store_animation_clock()

            ## admin task: check need to skip walking
            ## out of the first frame when updating
            self.check_walking_skipping()

            ## return True to indicate success
            return True

    def clear_rotations(self):
        """Restore timing indices to first frame.

        This is done by calling a 'restore_walking' method
        on a collections.deque subclass.
        """
        ### retrieve timing data for current animation
        timing_data = self.timing[self.anim_name]

        ### iterate over each node clearing the rotation
        ### for both surface and position time indices

        for node_name in timing_data:
            node_timing = timing_data[node_name]

            for key in ("surface_indices", "position_indices"):
                node_timing[key].restore_walking()

    def set_root_and_structure(self):
        """Setup root node and animation structure.

        In this method we perform three important operations
        related to the animation structure:

        (1) we check the need to reposition the new root
            in the application/game world and the need to
            set a new rect for the game object;
        (2) we set references in each node's "parent"
            attribute to their respective parent node.
            The root node, which doesn't have a parent,
            has None assigned to the parent attribute;
        (3) we also store structure related data into
            special attributes for usage when referencing
            the animation nodes used on the current
            animation;

        Below you find more details about operation (1) and
        (2). There was no need to further comment the
        operation (3).

        About operation (1):

        The game object references one of the root rects
        which is how the object moves in the application
        or game world. We switching between different
        animations, the root might be a different object,
        in which case position information is exchanged
        between them to guarantee the object stays in the
        same spot and the game object references the
        new root's rect.

        About operation (2):

        Just by setting references to their parent nodes
        in each child node we guarantee that the tree
        structure takes effect, because each node
        automatically repositions itself relative to its
        parent when being updated on the update_nodes method.
        """
        ### reference structure data for the current
        ### animation and its tree data

        anim_structure = self.structure[self.anim_name]
        tree = anim_structure["tree"]

        ### check the need to reposition the new root
        ### in the application/game world and the need to
        ### set a new rect for the game object

        ## retrieve new root
        new_root = self.node_map[tree["name"]]

        ## also reference its relevant rect (either the
        ## collision rect, if present, or the normal rect);
        ## we call it root rect, because all nodes are
        ## positioned relative to it;
        root_rect = new_root.col_rect or new_root.rect

        ## try retrieving previous root (if any)
        try:
            previous_root = self.root

        ## if there weren't one, just assign the root rect
        ## to the game obj rect attribute
        except AttributeError:
            self.game_obj.rect = root_rect

        ## if a previous root exists, verify the need to
        ## update the position of the new root with the
        ## position information of the previous root
        else:

            if new_root is not previous_root:
                self.exchange_root_position(previous_root, new_root)

                # also assign the root rect to the game obj
                # rect attribute
                self.game_obj.rect = root_rect

        ## store the new root node in the 'root' attribute,
        ## which represents the current root being used
        self.root = new_root

        ## also store the root rect in a special attribute;
        ## for convenience
        ## (note: this reference itself isn't used in this
        ## class, but it is useful for things like measuring
        ## distances between the root_rect and nodes;
        ## such measurements are performed for instance, by
        ## an external tool used to export the current
        ## animation to a sequence of .png files)
        self.root_rect = root_rect

        ### set references in each node's "parent"
        ### attribute to their respective parent node

        self.root.parent = None
        self.set_parent_references(tree)

        ### store updating order, drawing order and
        ### node_names list

        for key in ("updating_order", "drawing_order", "node_names"):
            setattr(self, key, anim_structure[key])

    def exchange_root_position(self, previous_root, new_root):
        """Exchange position from previous to new root.

        previous_root, new_root
        (instances of appcommon.anim.node.Node)
            previous root from which to retrieve the
            position information used and new root to have
            its position updated.
        """
        ### retrieve exchange map
        exchange_map = self.metadata["root_pos_exchange_map"]

        ### retrieve pygame.Rect attribute names used to
        ### exchange the position data

        attribute_names = exchange_map[previous_root.name][new_root.name]

        prev_attr_name, new_attr_name = attribute_names

        ### retrieve rects from previous and new root with
        ### preference for the collision rect

        new_rect = new_root.col_rect or new_root.rect

        prev_rect = previous_root.col_rect or previous_root.rect

        ### finally, retrieve the position value from
        ### previous root rect and apply to new root rect

        pos = getattr(prev_rect, prev_attr_name)
        setattr(new_rect, new_attr_name, pos)

    def set_parent_references(self, tree):
        """Set parent references on nodes.

        A tree structered mapping data is used to retrieve
        parent nodes and their children and while doing
        so, create references for each parent.

        tree (dict)
            Contains node data. The data may have a
            'children' field listing more nodes' data,
            in which case it is processed recursively.
        """
        ### retrieve node reference using the value in the
        ### tree's 'name' key
        node = self.node_map[tree["name"]]

        ### check if it has children
        try:
            children = tree["children"]

        ### if not just pass
        except KeyError:
            pass

        ### otherwise, iterate over each child data
        ### mapping stored in the children list,
        ### setting parent attributes on each
        ### child pointing to the current node;
        ### also check each child recursively
        ### for further parent relationships down
        ### the tree;
        else:

            for child_data in children:

                ### set parent attribute on child

                child = self.node_map[child_data["name"]]
                child.parent = node

                ### check child data recursively for
                ### more parent-children relationships
                self.set_parent_references(child_data)

    def store_animation_clock(self):
        """Store a reference of an animation clock.

        An animation clock is just an instance of
        the common.walkingdeque.WalkingDeque class,
        a collections.deque (from python standard library)
        subclass. The name here implies its role, since we
        use it to control animation timing.

        For more info, head to the module itself:
        common/walkingdeque.py
        """
        ### retrieve a mapping containing data about the
        ### largest deque for the current animation
        data = self.metadata["largest_deques"][self.anim_name]

        ### from the data, retrieve the name of the node
        ### and sequence from which to retrieve the
        ### animation clock
        node_name = data["node_name"]
        sequence_name = data["sequence_name"]

        ### finally retrieve and store the animation clock
        self.anim_clock = self.timing[self.anim_name][node_name][sequence_name]

    ### update routines

    def update_nodes(self, steps=0, nodes=None):
        """Rotate and assign animation values to nodes.

        The rotation per se is performed in the timing
        indices which point to the animation values,
        which are them assigned/passed to the nodes via
        the image attribute for surfaces and the set_pos
        method for positions.

        steps (int, defaults to 0)
            How much to rotate the data. steps=0
            means no rotation. rotate < 0 means rotate forth
            and rotate > 0 means rotate back.
        nodes (iterable containing strings)
            Names for nodes you want to update.

        The default value of "steps" makes the same
        values (surfaces and positions) to be assigned over
        and over again, thus making it appear as if the
        animation is paused).

        To make the animations play normally, you have to
        manually call self.play after instantiating this
        class.
        """
        ### alias "steps"
        n = steps

        ### pick node names list, with preference to the
        ### one provided by the user, if present
        node_names_list = nodes or self.updating_order

        ### iterate over each node listed, rotating the
        ### timing indices and updating the respective
        ### values using the current timing index

        for node_name in node_names_list:

            ### retrieve values and timing for the named node
            ### in the current animation

            node_values = self.values[self.anim_name][node_name]
            node_timing = self.timing[self.anim_name][node_name]

            ### rotate the time indices

            node_timing["surface_indices"].walk(n)
            node_timing["position_indices"].walk(n)

            ### retrieve the current time index (the first
            ### one) for both surfaces and positions

            surf_index = node_timing["surface_indices"][0]
            pos_index = node_timing["position_indices"][0]

            ### finally, using the indices just retrieved,
            ### store current surface reference and set
            ### position of the node

            ## reference node
            node = self.node_map[node_name]

            ## assign surface reference to image attribute
            node.image = node_values["surfaces"][surf_index]

            ## set position using related method
            node.set_pos(node_values["positions"][pos_index])

    step_forth = partialmethod(update_nodes, 1)
    two_steps_forth = partialmethod(update_nodes, 2)

    step_back = partialmethod(update_nodes, -1)
    two_steps_back = partialmethod(update_nodes, -2)

    ### drawing routines

    # obs.: the get_nodes method from the Utilities
    # class extension isn't used here (map is used instead)
    # for the sake of efficiency, since get_nodes perform
    # some extra checks which aren't needed here;

    def draw_nodes(self):
        """Draw each node."""
        for node in map(self.node_map.__getitem__, self.drawing_order):
            node.draw()

    def draw_nodes_and_bounding_rect(self):
        """Draw each node and its rects."""
        for node in map(self.node_map.__getitem__, self.drawing_order):

            node.draw()
            draw_rect(SCREEN, ORANGE, node.rect, 2)

    def draw_nodes_and_col_rect(self):
        """Draw each node and its collision rect, if any."""
        for node in map(self.node_map.__getitem__, self.drawing_order):

            node.draw()

            try:
                draw_rect(SCREEN, RED, node.col_rect, 2)

            # node.col_rect is None instead of Rect
            except TypeError:
                pass
