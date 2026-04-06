"""
AI Basics skill pack — AI Fundamentals
Teaches what AI is, how it works, and what its limitations are.
For adults new to AI, guided by ARIA.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
    _    ___   ____            _
   / \  |_ _| | __ )  __ _ ___(_) ___ ___
  / _ \  | |  |  _ \ / _` / __| |/ __/ __|
 / ___ \ | |  | |_) | (_| \__ \ | (__\__ \
/_/   \_\___| |____/ \__,_|___/_|\___|___/
"""

SKILL_PACK = SkillPack(
    id="ai_basics",
    title="AI Fundamentals",
    subtitle="◈  What AI Really Is — And What It Isn't  ◈",
    save_file_name="ai_basics_quest",
    intro_story=INTRO_STORY,
    quit_message="ARIA waves goodbye. Your progress is saved — the knowledge will be here when you return.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Learner",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "what_is_ai": "ai_demystifier",
        "history_of_ai": "history_scholar",
        "machine_learning": "pattern_finder",
        "neural_networks": "network_navigator",
        "large_language_models": "llm_whisperer",
        "computer_vision": "vision_decoder",
        "ai_in_daily_life": "hidden_ai_spotter",
        "ai_limitations": "critical_thinker",
    },
    achievements={
        "ai_demystifier":    ("AI Demystifier", "Separated AI fact from AI fiction!"),
        "history_scholar":   ("History Scholar", "Traced AI from Turing's dream to today's breakthroughs!"),
        "pattern_finder":    ("Pattern Finder", "Mastered supervised, unsupervised, and reinforcement learning!"),
        "network_navigator": ("Network Navigator", "Understood nodes, layers, weights, and the black box problem!"),
        "llm_whisperer":     ("LLM Whisperer", "Learned how large language models really work under the hood!"),
        "vision_decoder":    ("Vision Decoder", "Discovered how machines learn to see and where they fail!"),
        "hidden_ai_spotter": ("Hidden AI Spotter", "Found the AI hiding in everyday apps and services!"),
        "critical_thinker":  ("Critical Thinker", "Understood AI's limitations, biases, and the responsibility question!"),
        "no_hints":          ("Independent Learner", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Curious"),
        (6, "Informed"),
        (11, "Literate"),
        (16, "Fluent"),
        (21, "Expert"),
        (26, "Sage"),
    ],
)
