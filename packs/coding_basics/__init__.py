"""
Coding Basics skill pack — The Code Garden
Teaches coding concepts through analogy and logical thinking.
No actual coding required — just ideas, patterns, and understanding.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___  ___  ___  ___   ___  _  _
 / __||/ _ \|   \| __| / __|| \| |
| |   | (_) | |) | _|  | (_ || .  |
|_|    \___/|___/|___|  \___||_|\_|
"""

SKILL_PACK = SkillPack(
    id="coding_basics",
    title="The Code Garden",
    subtitle="◈  With Puck's Help, Instructions Come Alive  ◈",
    save_file_name="coding_basics_quest",
    intro_story=INTRO_STORY,
    quit_message="The workshop rests quietly. Come back whenever you're ready.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "what_is_coding": "code_awakened",
        "sequences_loops": "loop_master",
        "conditionals": "decision_maker",
        "variables": "memory_keeper",
        "functions": "function_wizard",
        "creative_computing": "dream_coder",
        "debugging": "bug_hunter",
        "data_and_lists": "data_keeper",
        "the_internet":            "net_navigator",
        "artificial_intelligence": "ai_thinker",
        "algorithms_all_around":   "algorithm_ace",
    },
    achievements={
        "code_awakened":  ("Code Awakened",  "Discovered what coding really is!"),
        "loop_master":    ("Loop Master",    "Understood sequences and loops!"),
        "decision_maker": ("Decision Maker", "Mastered if/then thinking!"),
        "memory_keeper":  ("Memory Keeper",  "Learned how variables store the world!"),
        "function_wizard":("Function Wizard","Understood the magic of reusable instructions!"),
        "dream_coder":    ("Dream Coder",    "Explored the creative world of computing!"),
        "bug_hunter":     ("Bug Hunter",     "Found and understood syntax errors, logic errors, and debugging strategies!"),
        "data_keeper":    ("Data Keeper",    "Mastered lists, booleans, sorting, and how programs store information!"),
        "net_navigator":  ("Net Navigator",  "Explored the internet, servers, HTML, HTTPS, and digital safety!"),
        "ai_thinker":     ("AI Thinker",     "Understood how AI learns, where it's used, and when to think critically about it!"),
        "algorithm_ace":  ("Algorithm Ace",  "Discovered algorithms everywhere — sorting, searching, GPS, and beyond!"),
        "no_hints":       ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":   ("Quick Thinker",  "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Seedling"),
        (6, "Sprout"),
        (11, "Bloom"),
        (16, "Star"),
        (21, "Wonder"),
        (26, "Sage"),
    ],
)
