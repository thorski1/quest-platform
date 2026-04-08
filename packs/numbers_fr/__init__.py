"""
Numbers skill pack — French Numbers
Teaches counting, ordinal numbers, telling time, and dates in French.
Guided by Camille, a cheerful French math teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _  _ _   _ __  __ ___ ___  ___  ___
 | \| | | | |  \/  | __| _ \/ _ \/ __|
 | .` | |_| | |\/| | _||   / (_) \__ \
 |_|\_|\___/|_|  |_|___|_|_\\___/|___/
"""

SKILL_PACK = SkillPack(
    id="numbers_fr",
    title="French Numbers",
    subtitle="Count, tell time, and navigate dates in French",
    save_file_name="numbers_fr_quest",
    intro_story=INTRO_STORY,
    quit_message="Camille waves cheerfully. A bientot -- your progress is saved!",
    name_prompt="[bold cyan]Comment tu t'appelles?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "numbers_1_20": "counting_star",
        "numbers_20_100": "number_navigator",
        "ordinal_numbers": "ordinal_ace",
        "telling_time": "time_keeper",
        "dates_calendar": "calendar_master",
    },
    achievements={
        "counting_star":     ("Counting Star", "Mastered numbers 1 through 20 in French!"),
        "number_navigator":  ("Number Navigator", "Can count confidently from 20 to 100!"),
        "ordinal_ace":       ("Ordinal Ace", "Knows first, second, third and beyond in French!"),
        "time_keeper":       ("Time Keeper", "Can tell time like a true French speaker!"),
        "calendar_master":   ("Calendar Master", "Navigates dates, days, and months in French!"),
        "no_hints":          ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="unicorn",
    level_titles=[
        (1, "Beginner"),
        (6, "Apprentice"),
        (11, "Speaker"),
        (16, "Conversant"),
        (21, "Fluent Thinker"),
        (26, "Language Sage"),
    ],
)
