"""
AI Business skill pack — The AI Boardroom
Teaches AI strategy, data strategy, team building, responsible AI,
and future trends for business leaders and executives.
Guided by ARIA.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
    _   ___   ___                  _
   /_\ |_ _| | _ ) ___  __ _ _ __| |_ _ _  ___  ___ _ __
  / _ \ | |  | _ \/ _ \/ _` | '__| __| '_|/ _ \/ _ \ '  \
 /_/ \_\___| |___/\___/\__,_|_|  |__|_|  \___/\___/_|_|_|
"""

SKILL_PACK = SkillPack(
    id="ai_business",
    title="The AI Boardroom",
    subtitle="◈  Lead AI Strategy, Don't Just Adopt It  ◈",
    save_file_name="ai_business_quest",
    intro_story=INTRO_STORY,
    quit_message="The boardroom dims gently. Your progress is saved — ARIA will be here when you return.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Executive",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "ai_strategy": "strategy_master",
        "data_strategy": "data_architect",
        "ai_team_building": "talent_builder",
        "responsible_ai_biz": "ethics_guardian",
        "ai_trends_future": "horizon_scanner",
    },
    achievements={
        "strategy_master":   ("Strategy Master", "Mastered build-vs-buy, ROI frameworks, pilot design, and competitive AI response!"),
        "data_architect":    ("Data Architect", "Built data governance, pipelines, and strategy to fuel enterprise AI!"),
        "talent_builder":    ("Talent Builder", "Designed AI teams with the right roles, structure, and hiring strategy!"),
        "ethics_guardian":   ("Ethics Guardian", "Established responsible AI frameworks with bias audits, model cards, and governance!"),
        "horizon_scanner":   ("Horizon Scanner", "Mapped AI trends from foundation models to agentic workflows and prepared for multiple futures!"),
        "no_hints":          ("Self-Sufficient", "Completed a zone without using any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Analyst"),
        (6, "Manager"),
        (11, "Director"),
        (16, "VP"),
        (21, "SVP"),
        (26, "Chief AI Officer"),
    ],
)
