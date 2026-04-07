"""
Earth Science skill pack — The Earth Explorer
Teaches rocks, volcanoes, the water cycle, soil, and natural resources.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___   _   ___ _____ _  _
 | __| /_\ | _ \_   _| || |
 | _| / _ \|   / | | | __ |
 |___/_/ \_\_|_\ |_| |_||_|
  ___  ___ ___ ___ _  _  ___ ___
 / __|/ __|_ _| __| \| |/ __| __|
 \__ \ (__ | || _|| .` | (__| _|
 |___/\___|___|___|_|\_|\___|___|
"""

SKILL_PACK = SkillPack(
    id="earth_science",
    title="The Earth Explorer",
    subtitle="◈  With Puck's Help, Every Rock Tells a Story  ◈",
    save_file_name="earth_science_quest",
    intro_story=INTRO_STORY,
    quit_message="The Earth rests beneath your feet. Your discoveries are saved. Come back soon!",
    name_prompt="[bold cyan]What's your name, explorer?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "rocks_and_minerals": "rock_collector",
        "volcanoes_and_earthquakes": "quake_survivor",
        "water_cycle": "water_wanderer",
        "soil_and_erosion": "ground_keeper",
        "natural_resources": "resource_guardian",
    },
    achievements={
        "rock_collector": ("Rock Collector", "Mastered igneous, sedimentary, and metamorphic rocks!"),
        "quake_survivor": ("Quake Survivor", "Explored volcanoes, earthquakes, and tectonic plates!"),
        "water_wanderer": ("Water Wanderer", "Followed water through its endless cycle!"),
        "ground_keeper": ("Ground Keeper", "Uncovered the secrets of soil, erosion, and fossils!"),
        "resource_guardian": ("Resource Guardian", "Learned to protect Earth's renewable and nonrenewable treasures!"),
        "no_hints": ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader": ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Pebble"),
        (6, "Boulder"),
        (11, "Geode"),
        (16, "Crystal"),
        (21, "Diamond"),
        (26, "Geologist"),
    ],
)
