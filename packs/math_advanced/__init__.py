"""
Math Advanced skill pack — The Math Academy
Teaches multiplication, division, word problems, geometry, decimals/percents,
and negative numbers.
For ages 8-11.
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
 __  __   _  _____ _   _   _   ___   ___
|  \/  | / \|_   _| | | | / \ |   \ \ \ \
| |\/| |/ _ \ | | | |_| |/ _ \| |_) | > > >
|_|  |_/_/ \_\|_|  \___//_/ \_\____/ /_/_/
"""

SKILL_PACK = SkillPack(
    id="math_advanced",
    title="The Math Academy",
    subtitle="◈  With Puck's Help, Numbers Reveal Their Secrets  ◈",
    save_file_name="math_advanced_quest",
    intro_story=INTRO_STORY,
    quit_message="The Academy rests. Your progress is saved. Come back soon!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "multiplication":       "multiplication_master",
        "division":             "division_expert",
        "word_problems":        "problem_solver",
        "geometry":             "geometry_sage",
        "decimals_percents":    "decimal_pro",
        "negative_numbers":     "number_explorer",
        "time_and_calendars":   "time_keeper",
        "patterns_and_sequences": "pattern_finder",
        "fractions_and_ratios":   "fraction_forest_cleared",
        "probability_and_chance": "chance_master",
        "algebra_intro":          "variable_solver",
    },
    achievements={
        "multiplication_master":  ("Multiplication Master",  "Conquered the times tables in the Multiplication Kingdom!"),
        "division_expert":        ("Division Expert",        "Solved every puzzle in the Division Workshop!"),
        "problem_solver":         ("Problem Solver",         "Worked through every story problem in the Café!"),
        "geometry_sage":          ("Geometry Sage",          "Measured shapes and angles in the Shape Lab!"),
        "decimal_pro":            ("Decimal Pro",            "Tended every flower in the Decimal Garden!"),
        "number_explorer":        ("Number Explorer",        "Journeyed through the Number Line Underground!"),
        "time_keeper":            ("Time Keeper",            "Mastered clocks, calendars, and elapsed time!"),
        "pattern_finder":         ("Pattern Finder",         "Decoded sequences, rules, and the Fibonacci mystery!"),
        "fraction_forest_cleared":("Fraction Forest Cleared","Mastered fractions, equivalent fractions, ratios, and mixed numbers!"),
        "chance_master":          ("Chance Master",          "Measured probability with fractions and the complement rule!"),
        "variable_solver":        ("Variable Solver",        "Cracked the Variable Vault and solved two-step algebra equations!"),
        "no_hints":               ("Standing on Your Own",   "Completed a zone without any hints!"),
        "speed_reader":           ("Quick Thinker",          "Answered a question in under 10 seconds!"),
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
