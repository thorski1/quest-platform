"""
Japanese Culture skill pack — festivals, martial arts, tea ceremony, anime, seasons, etiquette.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ _   _ _  _____ _   _ ___ ___
 / __| | | | ||_   _| | | | _ \ __|
| (__| |_| | |__| | | |_| |   / _|
 \___|\___/|____|_|  \___/|_|_\___|
"""

SKILL_PACK = SkillPack(
    id="culture_jp",
    title="日本文化 — Japanese Culture",
    subtitle="◈  Discover the Heart and Soul of Japan  ◈",
    save_file_name="culture_jp_quest",
    intro_story=INTRO_STORY,
    quit_message="The tea grows cold, but the journey awaits your return.",
    name_prompt="What is your name, student?",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "festivals": "festival_master",
        "martial_arts": "martial_artist",
        "tea_ceremony": "tea_master",
        "anime_manga": "otaku",
        "seasons": "season_poet",
        "etiquette": "etiquette_expert",
    },
    achievements={
        "festival_master": ("Festival Master", "Learned about Japan's greatest celebrations!"),
        "martial_artist": ("Martial Artist", "Explored the way of Japanese martial arts!"),
        "tea_master": ("Tea Master", "Discovered the art of the Japanese tea ceremony!"),
        "otaku": ("Otaku Scholar", "Dove into the world of anime and manga!"),
        "season_poet": ("Season Poet", "Experienced the beauty of Japan's four seasons!"),
        "etiquette_expert": ("Etiquette Expert", "Mastered the art of Japanese manners!"),
        "no_hints": ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader": ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="ocean",
    level_titles=[
        (1, "Tourist"),
        (6, "Visitor"),
        (11, "Explorer"),
        (16, "Culturist"),
        (21, "Scholar"),
        (26, "Sensei"),
    ],
)
