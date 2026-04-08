"""
baking_101 skill pack — Baking Fundamentals
From science to art, master the oven and everything that goes in it.
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
    id="baking_101",
    title="Baking Fundamentals",
    subtitle="Science, patience, and a very hot oven",
    save_file_name="baking_101",
    theme="sunset",
    kids_mode=False,
    intro_story=INTRO_STORY,
    quit_message="The oven cools... but the dough is still rising.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "baking_science": "science_certified",
        "bread_basics": "bread_baker",
        "cookies_bars": "cookie_master",
        "cakes_frosting": "cake_artist",
        "pastry_pies": "pastry_chef",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=r"""
  ____        _    _               _  ___  _
 | __ )  __ _| | _(_)_ __   __ _ / |/ _ \/ |
 |  _ \ / _` | |/ / | '_ \ / _` | | | | | |
 | |_) | (_| |   <| | | | | (_| | | |_| | |
 |____/ \__,_|_|\_\_|_| |_|\__, |_|\___/|_|
                            |___/
""",
    level_titles=[
        (1, "Beginner Baker"),
        (6, "Home Baker"),
        (11, "Skilled Baker"),
        (16, "Artisan Baker"),
        (21, "Master Baker"),
        (26, "Pastry Chef"),
    ],
)
