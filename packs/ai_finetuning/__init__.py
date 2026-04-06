"""
AI Fine-Tuning skill pack — The Training Ground
Teaches model fine-tuning: fundamentals, training data, techniques (LoRA/QLoRA/PEFT),
evaluation, and production deployment.
For a general audience, guided by ARIA.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ _            _____          _
 | __(_)_ _  ___  |_   _|  _ _ _(_)_ _  __ _
 | _|| | ' \/ -_)   | || || | ' \ | ' \/ _` |
 |_| |_|_||_\___|   |_| \_,_|_||_|_|_||_\__, |
                                         |___/
"""

SKILL_PACK = SkillPack(
    id="ai_finetuning",
    title="The Training Ground",
    subtitle="◈  Fine-Tuning: Forge Specialists from Generalists  ◈",
    save_file_name="ai_finetuning_quest",
    intro_story=INTRO_STORY,
    quit_message="The Training Ground powers down. Your progress is saved — the weights will still be here when you return.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Builder",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "what_is_finetuning": "finetuning_fundamentalist",
        "training_data": "data_refiner",
        "finetuning_techniques": "technique_master",
        "evaluation_and_testing": "evaluation_expert",
        "deployment_and_cost": "production_deployer",
    },
    achievements={
        "finetuning_fundamentalist": ("Fine-Tuning Fundamentalist", "Understood pre-training vs fine-tuning, transfer learning, and when customization matters!"),
        "data_refiner":              ("Data Refiner", "Mastered training data quality, labeling, formats, and the art of dataset curation!"),
        "technique_master":          ("Technique Master", "Conquered LoRA, QLoRA, full fine-tuning, and parameter-efficient methods!"),
        "evaluation_expert":         ("Evaluation Expert", "Built rigorous evaluation plans with benchmarks, loss curves, and human review!"),
        "production_deployer":       ("Production Deployer", "Navigated serving, quantization, distillation, cost optimization, and production monitoring!"),
        "no_hints":                  ("Independent Thinker", "Completed a zone without any hints!"),
        "speed_reader":              ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Novice"),
        (6, "Apprentice"),
        (11, "Practitioner"),
        (16, "Specialist"),
        (21, "Architect"),
        (26, "Master"),
    ],
)
