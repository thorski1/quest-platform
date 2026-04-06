"""
AI Safety skill pack — The Alignment Lab
Teaches AI risks, alignment, responsible development, governance,
and frontier safety challenges. For a general audience, guided by ARIA.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___   _    ___ ___ _______   __
 / __| /_\  | __| __|_   _\ \ / /
 \__ \/ _ \ | _|| _|  | |  \   /
 |___/_/ \_\|_| |___| |_|   |_|
"""

SKILL_PACK = SkillPack(
    id="ai_safety",
    title="The Alignment Lab",
    subtitle="◈  Can We Build AI That's Powerful Enough to Trust?  ◈",
    save_file_name="ai_safety_quest",
    intro_story=INTRO_STORY,
    quit_message="The Alignment Lab powers down. Your progress is saved — the hard questions will still be here when you return.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Researcher",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "ai_risks_and_misuse": "threat_analyst",
        "alignment_and_control": "alignment_researcher",
        "responsible_development": "safety_engineer",
        "ai_governance": "policy_architect",
        "future_of_ai_safety": "frontier_guardian",
    },
    achievements={
        "threat_analyst":        ("Threat Analyst", "Mapped the AI threat surface from deepfakes to autonomous weapons!"),
        "alignment_researcher":  ("Alignment Researcher", "Confronted reward hacking, mesa-optimization, and the specification problem!"),
        "safety_engineer":       ("Safety Engineer", "Mastered red teaming, evaluations, and the art of building safety cases!"),
        "policy_architect":      ("Policy Architect", "Designed governance frameworks for the most powerful technology in history!"),
        "frontier_guardian":     ("Frontier Guardian", "Explored interpretability, constitutional AI, and the long-term future of safety!"),
        "no_hints":              ("Independent Thinker", "Completed a zone without any hints!"),
        "speed_reader":          ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Observer"),
        (6, "Analyst"),
        (11, "Researcher"),
        (16, "Architect"),
        (21, "Guardian"),
        (26, "Sentinel"),
    ],
)
