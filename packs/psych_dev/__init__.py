"""
psych_dev skill pack — Developmental Psychology
A neural-themed RPG exploring human development from conception
to old age, guided by ARIA through the lifespan.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ____  ______   _______ _  _
|  _ \/ ___\ \ / / ____| || |
| |_) \___ \\ V /|  _| | || |_
|  __/ ___) || | | |___|__   _|
|_|   |____/ |_| |_____|  |_|
  ____  _______     __
 |  _ \| ____\ \   / /
 | | | |  _|  \ \ / /
 | |_| | |___  \ V /
 |____/|_____|  \_/
"""

SKILL_PACK = SkillPack(
    id="psych_dev",
    title="Developmental Psychology",
    subtitle="◈  The Architecture of Growth Across the Lifespan  ◈",
    save_file_name="psych_dev_quest",
    intro_story=INTRO_STORY,
    quit_message="The developmental timeline pauses. Your progress is saved — growth continues when you return.",
    name_prompt="[bold cyan]What's your name, explorer?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "prenatal_development": "genesis_scholar",
        "piagets_stages": "stage_theorist",
        "attachment_theory": "bond_analyst",
        "adolescence": "identity_navigator",
        "aging_lifespan": "lifespan_sage",
    },
    achievements={
        "genesis_scholar":     ("Genesis Scholar", "Traced human development from a single cell to a newborn ready to breathe!"),
        "stage_theorist":      ("Stage Theorist", "Mastered Piaget's cognitive stages from sensorimotor to formal operations!"),
        "bond_analyst":        ("Bond Analyst", "Decoded attachment theory and the lasting power of early relationships!"),
        "identity_navigator":  ("Identity Navigator", "Navigated the turbulent waters of adolescent development and identity formation!"),
        "lifespan_sage":       ("Lifespan Sage", "Explored aging, wisdom, and the full arc of human development!"),
        "no_hints":            ("Independent Thinker", "Completed a zone without any hints!"),
        "speed_reader":        ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Novice"),
        (6, "Student"),
        (11, "Analyst"),
        (16, "Researcher"),
        (21, "Scholar"),
        (26, "Developmentalist"),
    ],
)
