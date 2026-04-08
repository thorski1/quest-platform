"""
Basics skill pack — French Basics
Teaches the French alphabet, articles, pronouns, key verbs, and common adjectives.
Guided by Marie, a patient and enthusiastic French teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ ___    _   _  _  ___ _  _
 | __| _ \  /_\ | \| |/ __| || |
 | _||   / / _ \| .` | (__| __ |
 |_| |_|_\/_/ \_\_|\_|\___|_||_|
"""

SKILL_PACK = SkillPack(
    id="basics_fr",
    title="French Basics",
    subtitle="Master the building blocks of the French language",
    save_file_name="basics_fr_quest",
    intro_story=INTRO_STORY,
    quit_message="Marie smiles gently. A bientot -- your progress is saved!",
    name_prompt="[bold cyan]Comment tu t'appelles?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "alphabet_pronunciation": "phonetic_star",
        "articles": "article_ace",
        "subject_pronouns": "pronoun_pro",
        "etre_avoir": "verb_virtuoso",
        "common_adjectives": "adjective_artist",
    },
    achievements={
        "phonetic_star":     ("Phonetic Star", "Mastered French pronunciation and the alphabet!"),
        "article_ace":       ("Article Ace", "Knows le, la, les, un, une like a native!"),
        "pronoun_pro":       ("Pronoun Pro", "Can use all French subject pronouns with confidence!"),
        "verb_virtuoso":     ("Verb Virtuoso", "Conjugates etre and avoir without hesitation!"),
        "adjective_artist":  ("Adjective Artist", "Describes the world beautifully in French!"),
        "no_hints":          ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="unicorn",
    level_titles=[
        (1, "Beginner"),
        (6, "Apprentice"),
        (11, "Speaker"),
        (16, "Conversant"),
        (21, "Fluent Thinker"),
        (26, "Language Sage"),
    ],
)
