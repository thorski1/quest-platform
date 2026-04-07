"""
Python Kids skill pack — The Python Playground
Teaches real Python coding to kids ages 8-12.
5 zones, 40 challenges, Puck-narrated.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ____  _  _  _____  _   _   ___   _  _
|  _ \| || ||_   _|| | | | / _ \ | \| |
| |_) | || |_ | |  | |_| || (_) ||    |
|  __/|__   _|| |  |  _  | \___/ | |\ |
|_|      |_|  |_|  |_| |_|       |_| \_|
"""

SKILL_PACK = SkillPack(
    id="python_kids",
    title="The Python Playground",
    subtitle="◈  With Puck's Help, Write Real Code  ◈",
    save_file_name="python_kids_quest",
    intro_story=INTRO_STORY,
    quit_message="The Playground hums softly. Come back whenever you're ready to code!",
    name_prompt="[bold cyan]What's your name, coder?[/bold cyan]",
    default_player_name="Coder",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "hello_world": "first_words",
        "variables_math": "number_smith",
        "lists_loops": "loop_rider",
        "if_else_adventures": "logic_hero",
        "fun_projects": "game_maker",
    },
    achievements={
        "first_words":   ("First Words",   "Mastered print, strings, and input!"),
        "number_smith":  ("Number Smith",  "Conquered variables and math operations!"),
        "loop_rider":    ("Loop Rider",    "Tamed lists, for loops, and while loops!"),
        "logic_hero":    ("Logic Hero",    "Mastered if, else, elif, and logical operators!"),
        "game_maker":    ("Game Maker",    "Built mad libs, guessing games, calculators, and dice rollers!"),
        "no_hints":      ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":  ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Beginner"),
        (6, "Apprentice"),
        (11, "Coder"),
        (16, "Hacker"),
        (21, "Wizard"),
        (26, "Pythonista"),
    ],
)
