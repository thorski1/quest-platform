"""
Music skill pack — The Music Room
Teaches notes, rhythm, instruments, singing, world music, composers,
emotions in music, and making music.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  __  __  _   _  ___  ___  ___
 |  \/  || | | |/ __||_ _|/ __|
 | |\/| || | | |\__ \ | || (__
 |_|  |_| \___/ |___/|___|\___|
"""

SKILL_PACK = SkillPack(
    id="music",
    title="The Music Room",
    subtitle="◈  With Puck's Help, the World Begins to Sing  ◈",
    save_file_name="music_quest",
    intro_story=INTRO_STORY,
    quit_message="The Music Room hums softly as you leave. Your place is saved — the music will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Listener",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "musical_notes": "note_reader",
        "rhythm_and_beat": "rhythm_keeper",
        "instruments_orchestra": "orchestra_guide",
        "singing_and_voice": "voice_explorer",
        "music_around_world": "world_listener",
        "famous_composers": "composer_scholar",
        "music_and_feelings": "emotion_conductor",
        "making_music": "music_maker",
    },
    achievements={
        "note_reader":        ("Note Reader", "Learned the musical alphabet, the staff, and how to read notes!"),
        "rhythm_keeper":      ("Rhythm Keeper", "Mastered beats, tempo, time signatures, and rests!"),
        "orchestra_guide":    ("Orchestra Guide", "Met all four instrument families and the conductor!"),
        "voice_explorer":     ("Voice Explorer", "Discovered how the human voice makes music!"),
        "world_listener":     ("World Listener", "Heard the music of Africa, India, Japan, Ireland, and the Caribbean!"),
        "composer_scholar":   ("Composer Scholar", "Met Mozart, Beethoven, Bach, and Tchaikovsky!"),
        "emotion_conductor":  ("Emotion Conductor", "Learned how music speaks to the heart through keys and dynamics!"),
        "music_maker":        ("Music Maker", "Took the first steps on your own musical journey!"),
        "no_hints":           ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Listener"),
        (6, "Humming Bird"),
        (11, "Melody Maker"),
        (16, "Maestro"),
        (21, "Virtuoso"),
        (26, "Composer"),
    ],
)
