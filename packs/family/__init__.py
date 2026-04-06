"""
Family & Home skill pack — 家人与家
Teaches immediate family, extended family, descriptions, ages, rooms,
pets, and relationships. Guided by 龙龙 (Lóng Lóng).
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___  _   __  __ ___ _  __   __
 | __|| | / _||  V  ||_|| | \ V /
 | _| |_|| (_ | \_/ || || |_ \ /
 |_|  |_| \__||_| |_||_||___||_|
"""

SKILL_PACK = SkillPack(
    id="family",
    title="Family & Home — 家人与家",
    subtitle="◈  With 龙龙's Help, Learn the Heart of Chinese Culture  ◈",
    save_file_name="family_quest",
    intro_story=INTRO_STORY,
    quit_message="龙龙 waves goodbye. Your family journey is saved — 家 will always be here!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Learner",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "immediate_family": "family_circle",
        "extended_family": "clan_master",
        "describing_people": "word_painter",
        "ages_birthdays": "zodiac_keeper",
        "my_house": "home_builder",
        "pets_animals": "animal_friend",
        "relationships": "social_weaver",
    },
    achievements={
        "family_circle":  ("Family Circle", "Named every immediate family member in Chinese!"),
        "clan_master":    ("Clan Master", "Mastered the complex extended family vocabulary!"),
        "word_painter":   ("Word Painter", "Described people using opposite pairs in Chinese!"),
        "zodiac_keeper":  ("Zodiac Keeper", "Learned ages, birthdays, and the 12 zodiac animals!"),
        "home_builder":   ("Home Builder", "Named every room of a Chinese home!"),
        "animal_friend":  ("Animal Friend", "Met all the pets and learned their measure words!"),
        "social_weaver":  ("Social Weaver", "Learned how to address everyone around you in Chinese!"),
        "no_hints":       ("Standing Alone", "Completed a zone without any hints!"),
        "speed_reader":   ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Newcomer"),
        (6, "Family Friend"),
        (11, "Clan Member"),
        (16, "Family Elder"),
        (21, "Patriarch"),
        (26, "Ancestor"),
    ],
)
