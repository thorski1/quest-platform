"""
kitchen_basics skill pack — Kitchen Fundamentals
A warm culinary journey through essential cooking skills.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from engine.skill_pack import SkillPack
from .story import (
    INTRO_STORY,
    ZONE_INTROS,
    ZONE_COMPLETIONS,
    BOSS_INTROS,
    ACHIEVEMENT_DESCRIPTIONS,
)
from .zones import ZONES, ZONE_ORDER

SKILL_PACK = SkillPack(
    id="kitchen_basics",
    title="Kitchen Fundamentals",
    subtitle="Master the foundations every great cook needs",
    save_file_name="kitchen_basics",
    theme="sunset",
    kids_mode=False,
    intro_story=INTRO_STORY,
    quit_message="The kitchen cools... but the flame is never truly out.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "kitchen_safety": "safety_certified",
        "knife_skills": "blade_master",
        "measuring_temps": "precision_cook",
        "cooking_methods": "method_master",
        "seasoning_spices": "flavor_architect",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=r"""
 _  ___ _       _                 ____            _
| |/ (_) |_ ___| |__   ___ _ __ | __ )  __ _ ___(_) ___ ___
| ' /| | __/ __| '_ \ / _ \ '_ \|  _ \ / _` / __| |/ __/ __|
| . \| | || (__| | | |  __/ | | | |_) | (_| \__ \ | (__\__ \
|_|\_\_|\__\___|_| |_|\___|_| |_|____/ \__,_|___/_|\___|___/
""",
    level_titles=[
        (1, "Apprentice"),
        (6, "Line Cook"),
        (11, "Station Chef"),
        (16, "Sous Chef"),
        (21, "Head Chef"),
        (26, "Executive Chef"),
    ],
)
