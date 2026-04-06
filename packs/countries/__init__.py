"""
Countries skill pack — The Passport Office
Teaches flags, capitals, continents, landmarks, and languages of the world.
For ages 5-12, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___  ___  _   _  _  _  _____  ___  ___  ___  ___
 / __|| _ \| | | || \| ||_   _|| _ \|_ _|| __|| __|
| (__ |   /| |_| || .  |  | |  |   / | | | _| |__ \
 \___||_|_\ \___/ |_|\_|  |_|  |_|_\|___||___||___/
"""

SKILL_PACK = SkillPack(
    id="countries",
    title="The Passport Office",
    subtitle="◈  With Puck's Help, Stamp Your Way Around the World  ◈",
    save_file_name="countries_quest",
    intro_story=INTRO_STORY,
    quit_message="The passport closes gently. Your stamps are saved — the world will wait for you!",
    name_prompt="[bold cyan]What's your name, traveler?[/bold cyan]",
    default_player_name="Traveler",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "flags_of_the_world": "flag_expert",
        "capital_cities": "capital_expert",
        "continents_deep_dive": "continent_scholar",
        "famous_landmarks": "landmark_explorer",
        "countries_and_languages": "language_explorer",
    },
    achievements={
        "flag_expert":        ("Flag Expert", "Recognized flags from countries all around the world!"),
        "capital_expert":     ("Capital Expert", "Matched countries to their capital cities — even the tricky ones!"),
        "continent_scholar":  ("Continent Scholar", "Discovered deep facts about all seven continents!"),
        "landmark_explorer":  ("Landmark Explorer", "Visited the world's greatest buildings and monuments!"),
        "language_explorer":  ("Language Explorer", "Discovered the amazing languages spoken around the world!"),
        "no_hints":           ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Tourist"),
        (6, "Explorer"),
        (11, "Navigator"),
        (16, "Ambassador"),
        (21, "World Traveler"),
        (26, "Globe Master"),
    ],
)
