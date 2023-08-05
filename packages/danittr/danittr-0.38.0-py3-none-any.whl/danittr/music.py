"""Facility for managing music playback."""

from os import listdir
from os.path import join

### third-party import
from pygame.mixer import music

### local import
from .config import MUSIC_DIR, USER_SETTINGS


# TODO eliminate the "mood" feature. Always choose the
# music by name

# TODO export music manager methods individually, as done
# with the TASK_MANAGER


class MusicManager(object):
    """Manages music playback."""

    mood_to_music = {
        "casual": join(MUSIC_DIR, "caketown.ogg"),
        "tense": join(MUSIC_DIR, "title_screen_theme.ogg"),
    }

    def __init__(self, mood="tense"):
        """Assign variables and perform setups.

        mood (defaults to 'casual')
            A mood from DJ.moods.
        """
        if mood not in self.mood_to_music:
            raise ValueError("mood not listed in cls.mood_to_music")
        self.mood = mood

        self.play_mood()
        self.set_volume(USER_SETTINGS["music_volume"])

    def update(self):
        """Update object state.

        Do so by verifying if any music is being played
        and start playing if not."""
        busy = music.get_busy()
        if busy:
            pass
        else:
            self.play_mood()

    def cue(self, mood):
        """If needed, change music to match mood.

        mood
            A mood from DJ.moods."""
        if mood not in self.mood_to_music:
            raise ValueError("mood not listed in cls.mood_to_music")

        if self.mood == mood:
            pass
        else:
            self.mood = mood

            milliseconds = 1000
            music.fadeout(milliseconds)

    def play_mood(self):
        """Play the music for current mood."""
        music.load(self.mood_to_music[self.mood])

        loops = -1  # -1 means loop indefinitely
        music.play(loops)

    def get_volume(self):
        """Return music volume."""
        return music.get_volume()

    def set_volume(self, volume):
        """Set volume of music.

        volume
            Float from 0.0 to 1.0.
        """
        music.set_volume(volume)


MUSIC_MANAGER = MusicManager()
