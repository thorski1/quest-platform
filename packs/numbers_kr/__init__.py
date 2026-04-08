"""
Numbers skill pack -- Korean Numbers
Teaches the dual number system: Sino-Korean and Native Korean,
counters, telling time, and money/shopping.
Guided by an alien economist analyzing Earth's number systems.
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
    id="numbers_kr",
    title="Korean Numbers",
    subtitle="Master Korea's dual number system -- Sino-Korean and Native Korean",
    save_file_name="numbers_kr_quest",
    intro_story=INTRO_STORY,
    quit_message="The alien economist saves your data. Your progress is preserved -- return to continue counting.",
    name_prompt="[bold cyan]What is your name, traveler?[/bold cyan]",
    default_player_name="Traveler",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "sino_korean": "sino_counter",
        "native_korean": "native_counter",
        "counters": "counter_master",
        "telling_time": "time_keeper",
        "money_shopping": "market_navigator",
    },
    achievements={
        "sino_counter":      ("Sino Counter", "Mastered the Sino-Korean number system!"),
        "native_counter":    ("Native Counter", "Mastered the Native Korean number system!"),
        "counter_master":    ("Counter Master", "Knows which counters go with which numbers!"),
        "time_keeper":       ("Time Keeper", "Can tell time in Korean using both systems!"),
        "market_navigator":  ("Market Navigator", "Can handle money and shopping in Korean!"),
        "no_hints":          ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Calculator", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="alien",
    level_titles=[
        (1, "Zero Point"),
        (6, "Single Digit"),
        (11, "Double Digit"),
        (16, "Calculator"),
        (21, "Mathematician"),
        (26, "Number Sage"),
    ],
)
