"""
Numbers skill pack — The Counting Kingdom
Teaches counting, addition, subtraction, shapes, and time.
For a 7-year-old learning math.
"""

from engine.skill_pack import SkillPack
from .story import (
    INTRO_STORY,
    ZONE_INTROS,
    ZONE_COMPLETIONS,
    BOSS_INTROS,
)
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _  _ _   _ __  __ ___  ___ ___  ___
 | \| | | | |  \/  | _ )| __| _ \/ __|
 | .` | |_| | |\/| | _ \| _||   /\__ \
 |_|\_|\___/|_|  |_|___/|___|_|_\|___/
"""

SKILL_PACK = SkillPack(
    id="numbers",
    title="The Counting Kingdom",
    subtitle="◈  With Puck's Help, Every Number Tells a Story  ◈",
    save_file_name="numbers_quest",
    intro_story=INTRO_STORY,
    quit_message="The kingdom rests. Your numbers are saved. Come back soon!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "counting_hills": "hill_counter",
        "addition_meadow": "meadow_adder",
        "subtraction_valley": "valley_keeper",
        "shape_forest": "shape_finder",
        "time_tower": "time_keeper",
        "skip_counting_grove": "grove_hopper",
        "measurement_meadow": "master_measurer",
        "money_market": "coin_counter",
        "shapes_and_patterns": "pattern_spotter",
        "telling_time": "clockwork_reader",
        "fractions_forest": "fraction_finder",
    },
    achievements={
        "hill_counter": ("Hill Counter", "Counted all the way to 100!"),
        "meadow_adder": ("Meadow Adder", "Added numbers in the golden meadow!"),
        "valley_keeper": ("Valley Keeper", "Mastered subtraction in the valley!"),
        "shape_finder": ("Shape Finder", "Named every shape in the forest!"),
        "time_keeper": ("Time Keeper", "Learned to read the great clock tower!"),
        "grove_hopper": ("Grove Hopper", "Skipped through the counting grove by 2s, 5s, and 10s!"),
        "master_measurer": ("Master Measurer", "Measured everything in the meadow!"),
        "coin_counter": ("Coin Counter", "Counted every coin in the market!"),
        "pattern_spotter": ("Pattern Spotter", "Spotted shapes and patterns all through the garden!"),
        "clockwork_reader": ("Clockwork Reader", "Learned to read the Clockwork Tower!"),
        "fraction_finder": ("Fraction Finder", "Explored the Fractions Forest and understood equal parts!"),
        "no_hints": ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader": ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Seedling"),
        (6, "Sprout"),
        (11, "Bloom"),
        (16, "Star"),
        (21, "Wonder"),
        (26, "Sage"),
    ],
)
