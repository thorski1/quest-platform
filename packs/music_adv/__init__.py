"""
Music Advanced skill pack — The Concert Hall
Teaches reading music, genres, composers, world music, and making music.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
   ____                          _     _   _       _ _
  / ___|___  _ __   ___ ___ _ __| |_  | | | | __ _| | |
 | |   / _ \| '_ \ / __/ _ \ '__| __| | |_| |/ _` | | |
 | |__| (_) | | | | (_|  __/ |  | |_  |  _  | (_| | | |
  \____\___/|_| |_|\___\___|_|   \__| |_| |_|\__,_|_|_|
"""

SKILL_PACK = SkillPack(
    id="music_adv",
    title="The Concert Hall",
    subtitle="◈  Deeper Into the World of Music With Puck  ◈",
    save_file_name="music_adv_quest",
    intro_story=INTRO_STORY,
    quit_message="The Concert Hall dims softly as you leave. Your place is saved — the music will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Musician",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "reading_music": "notation_master",
        "musical_genres": "genre_explorer",
        "famous_composers": "composer_historian",
        "world_music": "global_listener",
        "making_music": "music_creator",
    },
    achievements={
        "notation_master":     ("Notation Master", "Mastered treble clef, bass clef, time signatures, and the grand staff!"),
        "genre_explorer":      ("Genre Explorer", "Explored rock, jazz, classical, hip-hop, country, and electronic music!"),
        "composer_historian":   ("Composer Historian", "Discovered the lives and masterpieces of Mozart, Beethoven, Bach, and Tchaikovsky!"),
        "global_listener":     ("Global Listener", "Heard the music of Africa, India, Japan, and the Celtic lands!"),
        "music_creator":       ("Music Creator", "Learned about bands, orchestras, singing, and songwriting!"),
        "no_hints":            ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":        ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Audience Member"),
        (6, "Music Student"),
        (11, "Performer"),
        (16, "Concert Master"),
        (21, "Virtuoso"),
        (26, "Maestro"),
    ],
)
