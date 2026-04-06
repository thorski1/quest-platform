"""
Numbers skill pack — The Number Dragon
Teaches Chinese numbers, counting, measure words, money, time, and dates.
Guided by Long Long (龙龙), a friendly dragon.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 _  _ _   _ __  __ ___ ___ ___  ___
| \| | | | |  \/  | _ ) __| _ \/ __|
| .` | |_| | |\/| | _ \ _||   /\__ \
|_|\_|\___/|_|  |_|___/___|_|_\|___/
"""

SKILL_PACK = SkillPack(
    id="numbers_chinese",
    title="The Number Dragon",
    subtitle="Count, measure, pay, and tell time in Mandarin",
    save_file_name="numbers_chinese_quest",
    intro_story=INTRO_STORY,
    quit_message="Long Long tallies your progress on the abacus. Your numbers are saved!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "numbers_1_10": "basic_counter",
        "numbers_11_99": "double_digit_master",
        "numbers_100_plus": "big_number_expert",
        "counting_words": "measure_word_master",
        "money": "money_handler",
        "time": "timekeeper",
        "dates": "calendar_keeper",
    },
    achievements={
        "basic_counter":        ("Basic Counter", "Counted from one to ten in Chinese!"),
        "double_digit_master":  ("Double Digit Master", "Mastered numbers 11 through 99!"),
        "big_number_expert":    ("Big Number Expert", "Handled hundreds, thousands, and ten-thousands!"),
        "measure_word_master":  ("Measure Word Master", "Learned the essential Chinese measure words!"),
        "money_handler":        ("Money Handler", "Can talk about prices and money in Chinese!"),
        "timekeeper":           ("Timekeeper", "Can tell time in Mandarin!"),
        "calendar_keeper":      ("Calendar Keeper", "Mastered dates, days, and months in Chinese!"),
        "no_hints":             ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":         ("Quick Counter", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Abacus Novice"),
        (6, "Counter"),
        (11, "Calculator"),
        (16, "Number Sage"),
        (21, "Math Dragon"),
        (26, "Grand Accountant"),
    ],
)
