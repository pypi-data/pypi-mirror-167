game

This project adheres loosely to Semantic Versioning (see: http://semver.org/spec/v2.0.0.html)

The changelog is loosely based on principles found here: http://keepachangelog.com/en/1.0.0/

Types of changes
================

Added
    for new features.
Changed
    for changes in existing functionality.
Tests
    for anything related to automated tests.
Deprecated
    for soon-to-be removed features.
Removed
    for now removed features.
Fixed
    for any bug fixes.
Security
    in case of vulnerabilities.


Unreleased features
===================

- Add option to choose between windowed or fullscreen
- Replace 'ladder' substring with 'climbable' in
  object which allow climbing
- Also use 'portal' as part of portal names
- Maybe change prop_name to class_name
- Coordinating animation for death
  (using the overrider)
- Coordinating animation for entering
  portal (using the overrider)


Current Working Branch
======================


Changes
=======


[0.38.0] - 2019-02-21 - No more "scripted level", new scene player class
************************************************************************

Changed
-------
- too many changes to list; a major change was the implementation of an object called GAME_REFS to hold other objects and values used throughout the package, instead of having those objects passed around as arguments when instantiating objects; this allows such objects and values to reach new modules more easily, reducing the unnecessary complexity of managing/storing/passing them through many objects;
- made a lot of art related UI changes so game is more beautiful, much more to come in the near future;

Added
-----
- A new ScenePlayer class with a custom data model to describe and display scenes populated with static and animated objects with timed actions;

Removed
-------
- all code related to template loading and setup; this was done because the .ani2d interface is flexible enough to cover the functionality provided by the template feature; this ways we can do the same with less code; simpler and more elegant;
- also remove all get_message methods and their usage throughout the package; it seemed like a good idea, and in fact it worked ok, but it isn't necessary, it is just more unneeded complexity;
- eliminated the concept of scripted level of the entire game, including the Slideshow class;


[0.37.0] - 2019-02-18 - Redesigning package for simplicity
**********************************************************

Changed
-------
- this branch had more changes than it is possible to track; this is because the changes made had too much dependencies across the entire package; everything went ok, though; the changes were made with the goal of making common game services (save game, load game, restart level and many others) available to all the package, instead of passing around the objects responsible for those services as arguments, as previously done. As a result, the package is much simpler and easier to manager and extend now; still, there's the imperative need of refactoring, which will be performed in the next branch.


[0.36.0] - 2019-02-14 - Separated update and drawing logic
**********************************************************

Changed
-------
- interactive level loop was changed so that update and drawing logic were separated. All dependencies on game classes were updated to comply; contrary to my beliefs, such changes didn't have any significant impact on the FPS, which was a great surprise, even though I thought whatever decrease in the FPS were to happen, it wouldn't be much anyways (but it turned out to be even less than anticipated, to the point of being insignificant);
- also rellocated several modules from the assethandling module to the top level directory; those modules were font.py, music.py, sound.py and palette.py;


[0.35.0] - 2019-02-12 - Modernizing code
****************************************

I pasted and adjusted code from other packages, containing months of improvements and extra features. It took roughly two weeks, mostly updating animation data. Fixing bugs and improving the code here and on the animation editor package also took a good amount of that time. There's a lot of docstrings and comments to update yet, though, and a lot of refactoring needed to improved the more dated part of the pre-existing game package code.

Fixed
-----
- fixed a small important detail in the "first frame skipping" feature in the animation player; instead of skipping the update altogether, it now updates, but without any arguments, making the nodes to used the animation values for the first frame; this is important because before, when we didn't update, if we changed to position of the rect of the game object the nodes wouldn't have their positions updated accordingly, which would case objects to look like they were "warping" from a point to the other on the screen (which in fact was happening); now it is fixed, and the function and its dependencies were refactored and had their names changed to reflect the new behaviour (since the update is not being skipped, it is just that the "walking" of the animation values is being omitted);
- changed how position exchange data between different roots are stored on the metadata map and how it is processed and used in its dependencies throughout the application; this was needed because the previous solution had a bug which makes the application crash because in some instances it was storing non serializable json data in the .ani2d file; this also required me to change how the metadata is loaded from the .ani2d file, though very slightly (just had to add one line of code in the appcommon/anim/proc/main.py module, and add another); that is, instead of using the dict.get method to retrieve the metadata dict, it is now retrieving the value directly and, if crashing, it creates the key in .ani2d file data; before the change the "get" method mentioned wasn't creating any key on the .ani2d file, which meant metadata was never saved there. This is not a problem for animation playback/edition/management, but having data stored in the file makes it a lot easier for users to update such data, since default versions of it are created automatically for them (just as it is done with drawing order in the "structure" dict);

Added
-----
- pasted a lot of code from the animation editor package into this package since the equivalent portion of the system here was outdated compared to the many improvements made in the level editor and more recently in the animation editor package; there's still code which I want to add, but what I managed to add and adjust up to this point was enough to maintain the functionality intact; my goal here isn't to add whatever I can from the animation editor, but to add whatever I need or whatever can improve the code in this package;

Removed
-------
- a lot of the pasted code was removed because they were portions of the code which had no application in this package; my goal in merging code from other packages is to use what is needed and can improve the design/efficiency of this package, not to mirror the same class exactly; thus, whatever doesn't fit, we cut out; even when a class has the same application and name across multiple packages, each one of them must be considered unique, since they work in different context, even when the problems are similar; for instance, I removed entire subpackages related to animation management, because that portion of the code, which was brought from the animation editor package, was developed in order to edit the animation data, which isn't needed in the game package (the game package must concern itself with processing and playing the game data, not editing it);

Changed
-------
- following the principle described in the "Removed" section above, I also changed much of the code I pasted from the animation editor; I also changed code already previously present in this package, that is, dependencies;
- the animations for the game objects, the .ani2d files, were also updated to conform to the improved .ani2d interface;


[0.34.2] - 2018-07-16
*********************

Changed
-------
- Improved data checkups on
  pygamecustom/object/dataproc/assist.py


[0.34.1] - 2018-07-13
*********************

Fixed
-----
- Improved KeyError catching while switching
  animations in pygamecustom/animationplayer.py

Changed
-------
- Improved data checkups on
  pygamecustom/object/dataproc/assist.py
- Changed order in which methods of
  pygamecustom.animationplayer.AnimationPlayer
  were laid out, for clarity;
- Animation player has a new method which is a
  variation of draw_objects_and_col_rect which
  draws regular rects instead (called bounding
  rects): the method is called
  draw_objects_and_bounding_rects;

for more context, check changelog for
object data viewer package, version 1.11.1

[0.34.0] - 2018-06-18
*********************
cross implementation branch: implementing changes in the
.gameobj api from the object data viewer package

Added
-----
- New generation facilities on commontools: indexgen
  and pointgen, for indices and point list generation.
  The point list represent positions in a path.
  Also surfgen, for generating surfaces on the
  pygamecustom facility, though it's very basic.

Changed
-------
- .gameobj api undertook a lot of changes. Mostly
  related to data generation for animations (indices
  and position lists). Better structure for objects
  under parent so they can be positioned like trees.
- Reallocation and division of tools in commontools
  facility: some commontools functions related to
  mathematical operations were gathered in a new
  commontools.math module.
- Instead of populating the object data map in
  the assetmanagement/objectdata.py module,
  each object is loaded individually and the process
  is wrapped inside a try/except block.

[0.33.0] - 2018-06-18
*********************

Added
-----
- Added a new climbable object

[0.32.3] - 2018-06-16
*********************
refactoring push

Added
-----
- Lots of small changes to improve readability
  and skimmability

Changed
-------
- refactored modules/subpackages:
  - assetmanagement/objectdata.py
  - assetmanagement/templatedata.py
  - pygamecustom/object.py is now a subpackage
    entitle pygamecustom/object and the module
    contents were split into:
    - pygamecustom/object/dataprocessing.py
    - pygamecustom/object/setup.py

removed
-------
- removed sequence setting feature and all related
  tools from animation player. It was unnecessary,
  since all needed functionality could already
  be produced from without it and the feature was
  only being used to satisfy a single use case.
- animation player toggle draw routine was divided
  into two different commands on get_message api
  to set either one behaviour or the other.


[0.32.1] - 2018-06-14
*********************

Added
-----
- Support for templates (with special folder
  entitled "templates" added to package
- Window now has game title caption and also an
  icon representing the game.

Changed
-------
- Game object data pipeline had API changed to
  allow objects with multiple structures: different
  masters and different combinations of objects
  per animation. Lots of dependencies were changed.
- commontools.common generated two new modules
  in the same level: jsonhandler and timehandler,
  just to separate things better and prevent some
  cross-import issues
- since gameobj now support multiple object structures
  player can now crouch.

Removed
-------
- assetmanagement/decorativeclasses.py was removed

[0.31.1] - 2018-06-11
*********************

Changed
-------
- eliminated unneeded copy step during game saving
- eliminated usage of lambda expressions
- fixed misbehaviour of climbing in some specific
  extreme case
- simplified behaviour assignement by using CallList
  custom object where needed.

[0.31.0] - 2018-06-05
*********************

Added
-----
- Player now can climb objects, moving in
  all directions (just need to animate the
  movement)

Changed
-------
- set_object_pos method surrogates now
  accept a (0, 0) default value for their
  first parameter after self so objects
  which weren't positioned explicitly
  now automatically have their center
  aligned with the master object center


[0.30.1] - 2018-06-05
*********************

Changed
-------
- Puppeteer was renamed to ControlOverrider
  to help identify its usage (though it was
  already good named, to be honest,
  but I believe it is a little better now
  and the puppeteer analogy stil applies
  to help explain its behaviour).
- Refactored to simplify and better document
  the ControlOverrider as well as the
  animation player and the pygamecustom.object
  module

[0.30.0] - 2018-06-04
*********************

Added
-----
- New Puppeteer class was added to control
  event and action generation and can be
  used to execute actions;

Changed
-------
- Metadata is now generated about animations
  helping store what would otherwise be
  resource intense calculation (even if they are
  relatively simple ones); such metadata is
  used to determine largest "subanimation" from
  each animation, so that said subanimation is
  used for retrieving loop state and other
  related data.
- AnimationPlayer also change to reflect the
  changes above in the data generated for objects.

[0.29.1] - 2018-06-02
*********************

Changed
-------
- Save slots now have thumbnails


[0.29.0] - 2018-06-01
*********************

Changed
-------
- Saving progress is now result of the
  interaction with a new objects which
  should be place in several special spots.
- Position data from gameobj files can now
  be copied from an animation to other
  (instead of the more common inversion
  option)
- Very tiny removal of redundant/unused code

Added
-----
- The satellite dish object, used to save
  the game as described above.


Changelog
=========

[0.28.0] - 2018-05-29
*********************

Changed
-------
- Adjusted style and behaviours of various
  mainmenu widgets. Better feedback, too.
- Refactored main subpackage and its
  packages

Added
-----
- Mouse support to mainmenu widgets.
- Message Screen manager to show
  messages (errors and others).

[0.27.1] - 2018-05-26
*********************

Changed
-------
- Adjusted style and behaviours or various
  mainmenu widgets.

Added
-----
- Associated sound with many actions on
  main menu and related.


[0.27.0] - 2018-05-25
*********************

Added
-----
- Options menu now features an input mapping
  submenu where user can change controls.

[0.26.1] - 2018-05-24
*********************

Added
-----
- New restore defaults button in options menu.

[0.26.0] - 2018-05-24
*********************

Added
-----
- New options menu was implemented. You can now
  change music and sfx volume. A config.json
  file keeps the settings stored.

[0.25.0] - 2018-05-22
*********************

Added
-----
- Sound support: sound objects are created,
  grouped in a mapping and can be referenced
  throught the package, that is, used for
  actions. Just need to add more sounds now.

[0.24.1] - 2018-05-22
*********************

Changed
-------
- assetmanagement.music.DJ was slightly change
  to not have a DJ.moods class attribute, since
  it wasn't used anywhere. The relevant information
  was instead kept in the docstring.
- the title screen music was replaced for the new one I
  composed.

[0.24.0] - 2018-05-18
*********************

Changed
-------
- pygamecustom.object.get_object_data function
  and related json api now accept spritesheets.

[0.23.1] - 2018-05-17
*********************

Changed
-------
- Just a quick change a made on a whim. Instead of
  a single color the background is now a slight
  gradient from the sky background blue to white.
  It looks better now.
- While make the change mentioned above I fixed a bug
  which was making the game crash whenever I tried to
  hide the fps display or switch between showing/hiding
  the scroll barriers (just changed the methods, since
  they were from the old Sprite/Group iteration, instead
  of the new GamingSet object (a 'set' subclass).

[0.23.0] - 2018-05-17
*********************

Added
-----
- parallax_mountain group in interactive level
- mountain/mountains.py containing mountain class with parallax
  scrolling.

Changed
-------
- the task manager now have all task execution
  wrapped in try/except clauses. This helps preventing
  some execution errors that were happening when switching
  levels while toxic pollens were disappearing. This will
  also help to prevent casual future execution errors linked to
  the task manager. Of course, aside from catching the errors,
  the except clauses also log them so problems can be investigated
  and dealt whenever needed.

[0.22.0] - 2018-05-14
*********************

Added
-----
- parallax_clouds group in interactive level
- cloud/clouds.py containing cloud classes with parallax
  scrolling.

Changed
-------
- Minor refactoring pass.
- function to set objects data just need the basename
  of the file now. All path joining is done inside
  the pygamecustom.object module.
- interactivelevel.tools was divided into
  interactivelevel.scroll and
  interactivelevel.groups for better division and
  easier management.
- the task manager now accepts tasks which execute
  themselves indefinitely by passing 'cyclic=True'
  to the call to add_task function from
  pygamecustom.task.

[0.21.2] - 2018-05-07
*********************

Changed
-------
- All statemanager modules were removed. They might be
  used again here and there if necessary. For now, it's not.

[0.21.1] - 2018-05-07
*********************

Added
-----
- Game objects can optionally have a special
  pre_saving_routine method which is always executed
  before saving the game, so setups can be performed
  like saving time dependent states for instance.

Changed
-------
- Minor refactoring pass
- specialmanager.slideshow is now scriptedlevel.slideshow
  so it doesn't cause confusion (specialmanager subpackage
  don't exist anymore).

[0.21.0] - 2018-05-07
*********************

Added
-----
- Thornshooter now has a healthbar, can be defeated and
  is revived automatically after a certain amount of time
  which is starts from where it stopped when switching back
  to the level.

Changed
-------
- Task manager is managed in the level classes now, and in
  the interactive level is only updated when the game is being
  played, that is, outside menus that pause the game.

[0.20.0] - 2018-04-28
*********************

Changed
-------
- Major redesign: package don't rely in pygame.sprite
  anymore. We don't use their classes (Sprite, Group, etc.)
  nor functions. Instead, we use regular Python objects for
  game classes and a custom made GamingSet class for
  game instances grouping.

[0.19.0] - 2018-04-24
*********************

Changed
-------
- screen surface isn't passed around as an attribute anymore.
  Instead, it now is just imported into any module needed as
  screen.SCREEN. This means less attribute management.

[0.18.1] - 2018-04-23
*********************

Changed
-------
- ToxicPollenCloud now conforms to new API (state manager
  + animation player + get_message).
- Some very small refactoring.

[0.17.0] - 2018-04-23
*********************

Added
-----
- check_resource function added on pygamecustom/sprite.py to
  track and report resorces not used on sprite data from
  .spt files. Used old check_resource function from old API as
  base.

Changed
-------
- MushroomPlant now conforms to new API
  (state manager + animation player
  + get_message). Except it doesn't use
  an animation player since it isn't an
  animated sprite.

[0.16.0] - 2018-04-21
*********************

Changed
-------
- Mushroom now conforms to new API (state manager + animation player
  + get_message).

[0.15.0] - 2018-04-20
*********************

Changed
-------
- Player now conforms to new API (state manager + animation player
  + get_message).

[0.14.0] - 2018-04-19
*********************

Added
-----
- Task manager was added. Timed tasks can be
  added and removed any time.

Changed
-------
- Grass art and behaviour were both improved and implemented in the
  newest state management API.

[0.13.1] - 2018-04-16
*********************

Changed
-------

- DJ object is now instantiated by the game object and updated there on the
  while loop of the run method; the class is much simpler and handles it's update
  without needing custom events as before.


[0.12.10] - 2018-04-16
**********************

Changed
-------

- Lots of recurrent general refactoring passes

[0.12.1] - 2018-04-05
*********************

Added
-----

- Better documentation


[0.12.0] - 2018-04-05
*********************

Added
-----
- new sprite data model which assists in animation and
  in making compounding sprites (sprites made of multiple
  "child" sprites). Uses json.
  - this includes a sprite factory which automatically makes
    all needed instantiations and attribute assignments
  - also includes an animation player able to use the data
    processed and produced by the sprite factory to play
    animations with lots of flexibility



[0.11.0] - 2018-03-12
*********************

Changed
-------
- refactored interactive level to be more efficient


[0.10.0] - 2018-03-12
*********************

Changed
-------
- The package now has a new animation feature using JSON to load surfaces and frame-dependent timing data


Previous
========
(need to document previous changes)
