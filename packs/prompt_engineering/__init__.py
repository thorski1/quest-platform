"""
Prompt Engineering skill pack — The Prompt Playbook
Teaches the art of speaking to AI: clarity, roles, examples, reasoning,
system prompts, advanced techniques, and debugging.
Guided by ARIA.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___  ___  ___  __  __ ___ _____
| _ \| _ \/ _ \|  \/  | _ \_   _|
|  _/|   / (_) | |\/| |  _/ | |
|_|  |_|_\\___/|_|  |_|_|   |_|
"""

SKILL_PACK = SkillPack(
    id="prompt_engineering",
    title="The Prompt Playbook",
    subtitle="◈  Master the Art of Talking to AI  ◈",
    save_file_name="prompt_engineering_quest",
    intro_story=INTRO_STORY,
    quit_message="The terminal dims softly. Your progress is saved — ARIA will be here when you return.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Prompter",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "what_is_a_prompt": "first_contact",
        "clarity_and_specificity": "precision_crafter",
        "role_prompting": "persona_director",
        "few_shot_examples": "pattern_teacher",
        "chain_of_thought": "logic_chainer",
        "system_prompts": "system_architect",
        "advanced_techniques": "power_user",
        "prompt_debugging": "debug_master",
    },
    achievements={
        "first_contact":     ("First Contact", "Understood how prompts, tokens, and context windows work!"),
        "precision_crafter":  ("Precision Crafter", "Mastered clarity, specificity, and the power of constraints!"),
        "persona_director":   ("Persona Director", "Learned to assign roles and frame expert perspectives!"),
        "pattern_teacher":    ("Pattern Teacher", "Used few-shot examples to teach the AI by demonstration!"),
        "logic_chainer":      ("Logic Chainer", "Guided the AI through step-by-step reasoning!"),
        "system_architect":   ("System Architect", "Configured system prompts and behavioral guardrails!"),
        "power_user":         ("Power User", "Wielded temperature, JSON mode, and meta-prompting!"),
        "debug_master":       ("Debug Master", "Diagnosed prompt failures and defended against injection!"),
        "no_hints":           ("Self-Sufficient", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Beginner"),
        (6, "Prompter"),
        (11, "Crafter"),
        (16, "Architect"),
        (21, "Whisperer"),
        (26, "Master"),
    ],
)
