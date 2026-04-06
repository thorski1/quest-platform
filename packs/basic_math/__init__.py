"""
Basic Math skill pack — The Math Playground
Teaches addition, subtraction, multiplication, division, and word problems.
For kids ages 5-12 building core math fluency.
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
  __  __   _ _____ _  _
 |  \/  | /_\_   _| || |
 | |\/| |/ _ \| | | __ |
 |_|  |_/_/ \_\_| |_||_|
"""

SKILL_PACK = SkillPack(
    id="basic_math",
    title="The Math Playground",
    subtitle="◈  With Puck's Help, Every Problem Has a Solution  ◈",
    save_file_name="basic_math_quest",
    intro_story=INTRO_STORY,
    quit_message="The playground rests. Your progress is saved. Come back soon!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "addition_fun": "addition_ace",
        "subtraction_station": "subtraction_star",
        "multiplication_tables": "multiplication_master",
        "division_basics": "division_champ",
        "word_problems": "problem_solver",
    },
    achievements={
        "addition_ace": ("Addition Ace", "Added single and double-digit numbers like a pro!"),
        "subtraction_star": ("Subtraction Star", "Mastered taking away at the Subtraction Station!"),
        "multiplication_master": ("Multiplication Master", "Conquered the times tables from 2x to 10x!"),
        "division_champ": ("Division Champion", "Shared and divided with perfect fairness!"),
        "problem_solver": ("Problem Solver", "Solved real-world word problems using all four operations!"),
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
