"""
Numbers skill pack — The World of Japanese Numbers
Teaches counting, counters, time, and money in Japanese.
Guided by 先生 (Sensei) — a wise, patient Japanese teacher.
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
    id="numbers_jp",
    title="The World of Japanese Numbers",
    subtitle="Master counting, counters, time, and money in Japanese",
    save_file_name="numbers_jp_quest",
    intro_story=INTRO_STORY,
    quit_message="Sensei closes the abacus. Your progress is saved -- the numbers will wait for you.",
    name_prompt="[bold cyan]What is your name, student?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "one_to_ten": "basic_counter",
        "eleven_to_99": "number_builder",
        "hundreds_plus": "big_number_master",
        "counters": "counter_expert",
        "time": "time_teller",
        "money": "money_master",
    },
    achievements={
        "basic_counter":     ("Basic Counter", "Counted from いち to じゅう!"),
        "number_builder":    ("Number Builder", "Constructed numbers from 11 to 99!"),
        "big_number_master": ("Big Number Master", "Mastered hundreds, thousands, and ten-thousands!"),
        "counter_expert":    ("Counter Expert", "Used つ, 人, 本, and 枚 correctly!"),
        "time_teller":       ("Time Teller", "Can tell time in Japanese!"),
        "money_master":      ("Money Master", "Handles yen like a pro!"),
        "no_hints":          ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Calculator", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="ocean",
    level_titles=[
        (1, "Counter"),
        (6, "Calculator"),
        (11, "Mathematician"),
        (16, "Accountant"),
        (21, "Number Sage"),
        (26, "Grand Master"),
    ],
)
