"""
html_css skill pack - HTML & CSS Foundations
A cyberpunk RPG for learning markup and styles, guided by ARIA.
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
    id="html_css",
    title="HTML & CSS Foundations",
    subtitle="</>  ARIA Protocol -- Rebuild the Document Layer  </>",
    save_file_name="html_css_foundations",
    intro_story=INTRO_STORY,
    quit_message="The Metaframe dims... but the DOM remembers.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "html_elements": "element_master",
        "forms_inputs": "form_builder",
        "css_selectors": "selector_sage",
        "flexbox_grid": "layout_lord",
        "responsive_design": "responsive_ace",
    },
    achievements=ACHIEVEMENT_DESCRIPTIONS,
    kids_mode=False,
    category="webdev",
)
