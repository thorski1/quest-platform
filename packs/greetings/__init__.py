"""
Greetings skill pack — First Words
Teaches basic Chinese greetings, introductions, and polite expressions.
Guided by Long Long (龙龙), a friendly dragon.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ ___ ___ ___ _____ ___ _  _  ___ ___
 / __| _ \ __| __|_   _|_ _| \| |/ __/ __|
| (_ |   / _|| _|  | |  | || .` | (_ \__ \
 \___|_|_\___|___| |_| |___|_|\_|\___|___/
"""

SKILL_PACK = SkillPack(
    id="greetings",
    title="First Words",
    subtitle="Your first conversations in Mandarin Chinese",
    save_file_name="greetings_quest",
    intro_story=INTRO_STORY,
    quit_message="Long Long waves goodbye -- but not for long. Your progress is saved!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "hello_goodbye": "greeting_star",
        "introductions": "introduction_master",
        "how_are_you": "wellbeing_checker",
        "please_thanks": "polite_speaker",
        "yes_no": "yes_no_expert",
        "common_phrases": "phrase_collector",
        "polite_expressions": "courtesy_keeper",
    },
    achievements={
        "greeting_star":       ("Greeting Star", "Mastered hello, goodbye, and basic politeness!"),
        "introduction_master": ("Introduction Master", "Can introduce yourself in Chinese!"),
        "wellbeing_checker":   ("Wellbeing Checker", "Knows how to ask and answer 'How are you?'!"),
        "polite_speaker":      ("Polite Speaker", "Please, thank you, and sorry -- all mastered!"),
        "yes_no_expert":       ("Yes/No Expert", "Understands the three ways to say yes and no!"),
        "phrase_collector":    ("Phrase Collector", "Learned essential everyday phrases!"),
        "courtesy_keeper":     ("Courtesy Keeper", "Understands formal vs informal Chinese politeness!"),
        "no_hints":            ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":        ("Quick Ear", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Stranger"),
        (6, "Acquaintance"),
        (11, "Conversationalist"),
        (16, "Social Butterfly"),
        (21, "Diplomat"),
        (26, "Cultural Ambassador"),
    ],
)
