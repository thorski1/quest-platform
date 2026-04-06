"""
AI Coding skill pack — AI-Powered Coding
Teaches AI pair programming, code generation, debugging, review, testing,
refactoring, and best practices for AI-assisted development.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
    _   ___    ____          _ _
   / \ |_ _|  / ___|___   __| (_)_ __   __ _
  / _ \ | |  | |   / _ \ / _` | | '_ \ / _` |
 / ___ \| |  | |__| (_) | (_| | | | | | (_| |
/_/   \_\___|  \____\___/ \__,_|_|_| |_|\__, |
                                        |___/
"""

SKILL_PACK = SkillPack(
    id="ai_coding",
    title="AI-Powered Coding",
    subtitle="◈  Code Faster, Debug Smarter, Ship Sooner  ◈",
    save_file_name="ai_coding_quest",
    intro_story=INTRO_STORY,
    quit_message="The terminal saves your session. Your AI pair programmer will be here when you return.",
    name_prompt="[bold cyan]What's your handle, developer?[/bold cyan]",
    default_player_name="Developer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "ai_pair_programming": "pair_programmer",
        "writing_code_with_ai": "code_writer",
        "debugging_with_ai": "bug_hunter",
        "code_review_with_ai": "code_reviewer",
        "testing_with_ai": "test_engineer",
        "refactoring_with_ai": "refactorer",
        "ai_coding_best_practices": "best_practices_master",
    },
    achievements={
        "pair_programmer":        ("Pair Programmer", "Mastered AI pair programming tools and interaction modes!"),
        "code_writer":            ("Code Writer", "Learned to describe, iterate, and review AI-generated code!"),
        "bug_hunter":             ("Bug Hunter", "Debugged with AI — stack traces, rubber ducks, and all!"),
        "code_reviewer":          ("Code Reviewer", "Used AI for security, performance, and code smell reviews!"),
        "test_engineer":          ("Test Engineer", "Generated tests, found edge cases, and mocked the world!"),
        "refactorer":             ("Refactorer", "Simplified, extracted, modernized, and knew when to stop!"),
        "best_practices_master":  ("Best Practices Master", "Learned the golden rules of AI-assisted development!"),
        "no_hints":               ("Solo Debugger", "Completed a zone without any hints!"),
        "speed_reader":           ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Script Kiddie"),
        (6, "Junior Dev"),
        (11, "Developer"),
        (16, "Senior Dev"),
        (21, "Architect"),
        (26, "10x Engineer"),
    ],
)
