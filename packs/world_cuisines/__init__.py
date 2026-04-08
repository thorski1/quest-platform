"""
world_cuisines skill pack — World Cuisines
A culinary tour across five legendary food traditions.
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
    id="world_cuisines",
    title="World Cuisines",
    subtitle="Travel the globe through flavor, technique, and tradition",
    save_file_name="world_cuisines",
    theme="sunset",
    kids_mode=False,
    intro_story=INTRO_STORY,
    quit_message="The journey pauses... but the world's kitchens never close.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "italian_cooking": "italian_master",
        "mexican_cooking": "mexican_master",
        "japanese_cooking": "japanese_master",
        "indian_cooking": "indian_master",
        "french_cooking": "french_master",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    banner_ascii=r"""
 __        __         _     _    ____      _     _
 \ \      / /__  _ __| | __| |  / ___|   _(_)___(_)_ __   ___  ___
  \ \ /\ / / _ \| '__| |/ _` | | |  | | | | / __| | '_ \ / _ \/ __|
   \ V  V / (_) | |  | | (_| | | |__| |_| | \__ \ | | | |  __/\__ \
    \_/\_/ \___/|_|  |_|\__,_|  \____\__,_|_|___/_|_| |_|\___||___/
""",
    level_titles=[
        (1, "Tourist"),
        (6, "Traveler"),
        (11, "Explorer"),
        (16, "Connoisseur"),
        (21, "Ambassador"),
        (26, "World Chef"),
    ],
)
