"""
Electricity skill pack — The Spark Lab
Teaches atoms, circuits, conductors, magnets, and electricity in daily life.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ _    ___ ___ _____ ___ ___ ___ ___ _______   __
 | __| |  | __/ __|_   _| _ \_ _/ __|_ _|_   _\ \ / /
 | _|| |__| _| (__  | | |   /| | (__ | |  | |  \   /
 |___|____|___\___| |_| |_|_\___\___|___| |_|   |_|
"""

SKILL_PACK = SkillPack(
    id="electricity",
    title="The Spark Lab",
    subtitle="~  With Puck's Help, Every Spark Tells a Story  ~",
    save_file_name="electricity_quest",
    intro_story=INTRO_STORY,
    quit_message="The lab powers down. Your discoveries are saved. Come back soon!",
    name_prompt="[bold cyan]What's your name, explorer?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "what_is_electricity": "spark_finder",
        "circuits_and_batteries": "circuit_builder",
        "conductors_and_insulators": "material_tester",
        "magnets_and_electromagnets": "magnet_master",
        "electricity_in_daily_life": "power_guardian",
    },
    achievements={
        "spark_finder": ("Spark Finder", "Discovered atoms, electrons, and the secret of static electricity!"),
        "circuit_builder": ("Circuit Builder", "Mastered open, closed, series, and parallel circuits!"),
        "material_tester": ("Material Tester", "Learned which materials conduct electricity and which block it!"),
        "magnet_master": ("Magnet Master", "Uncovered the hidden link between magnets and electricity!"),
        "power_guardian": ("Power Guardian", "Understood how electricity powers the world and how to keep it safe!"),
        "no_hints": ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader": ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Spark"),
        (6, "Wire"),
        (11, "Circuit"),
        (16, "Dynamo"),
        (21, "Volt"),
        (26, "Tesla"),
    ],
)
