"""
AI Ethics skill pack — The Ethics Engine
Teaches critical thinking about AI bias, hallucinations, copyright,
deepfakes, privacy, jobs, and responsible use.
For teens and adults, guided by ARIA.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ _____ _  _ ___ ___ ___
 | __|_   _| || |_ _/ __/ __|
 | _|  | | | __ || | (__\__ \
 |___| |_| |_||_|___\___|___/
"""

SKILL_PACK = SkillPack(
    id="ai_ethics",
    title="The Ethics Engine",
    subtitle="◈  Think Critically About What AI Can — and Should — Do  ◈",
    save_file_name="ai_ethics_quest",
    intro_story=INTRO_STORY,
    quit_message="The Ethics Engine powers down gently. Your progress is saved — the hard questions will wait for you.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Thinker",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "bias_in_ai": "bias_detective",
        "hallucinations": "truth_seeker",
        "copyright_and_ip": "rights_scholar",
        "deepfakes_and_misinfo": "reality_anchor",
        "privacy_and_data": "data_guardian",
        "ai_and_jobs": "future_navigator",
        "responsible_use": "ethics_guardian",
    },
    achievements={
        "bias_detective":    ("Bias Detective", "Traced AI bias back to its roots in training data!"),
        "truth_seeker":      ("Truth Seeker", "Learned to spot hallucinations and verify AI output!"),
        "rights_scholar":    ("Rights Scholar", "Navigated the tangled world of AI and copyright!"),
        "reality_anchor":    ("Reality Anchor", "Confronted deepfakes and the crisis of trust!"),
        "data_guardian":     ("Data Guardian", "Understood data collection, consent, and privacy rights!"),
        "future_navigator":  ("Future Navigator", "Separated automation panic from economic reality!"),
        "ethics_guardian":   ("Ethics Guardian", "Embraced the responsibility that comes with powerful tools!"),
        "no_hints":          ("Independent Thinker", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Aware"),
        (6, "Questioning"),
        (11, "Critical"),
        (16, "Principled"),
        (21, "Guardian"),
        (26, "Philosopher"),
    ],
)
