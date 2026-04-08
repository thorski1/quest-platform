"""
Italian Basics skill pack — Italian Basics
Teaches the Italian alphabet, articles, pronouns, core verbs, and adjectives.
Guided by a warm sunset narrative through the Italian countryside.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___ _____  _   _    ___   _   _  _
|_ _|_   _|/ \ | |  |_ _| / \ | \| |
 | |  | | / _ \| |   | | / _ \| .` |
|___| |_|/_/ \_\___|___|/_/ \_\_|\_|
 ___   _   ___ ___ ___ ___
| _ ) /_\ / __|_ _/ __/ __|
| _ \/ _ \\__ \| | (__\__ \
|___/_/ \_\___/___\___|___/
"""

SKILL_PACK = SkillPack(
    id="basics_it",
    title="Italian Basics",
    subtitle="Build the foundation of your Italian from the ground up",
    save_file_name="basics_it_quest",
    intro_story=INTRO_STORY,
    quit_message="The Tuscan sun dips below the hills -- but your progress is saved. A domani!",
    name_prompt="[bold cyan]Come ti chiami, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "alphabet_pronunciation": "alphabet_ace",
        "articles": "article_artisan",
        "subject_pronouns": "pronoun_pro",
        "essere_avere": "verb_virtuoso",
        "common_adjectives": "adjective_artist",
    },
    achievements={
        "alphabet_ace":      ("Alphabet Ace", "Mastered Italian letters and pronunciation!"),
        "article_artisan":   ("Article Artisan", "Conquered il, la, lo, i, le, and gli!"),
        "pronoun_pro":       ("Pronoun Pro", "Knows every Italian subject pronoun!"),
        "verb_virtuoso":     ("Verb Virtuoso", "Conjugated essere and avere like a native!"),
        "adjective_artist":  ("Adjective Artist", "Paints with Italian adjectives!"),
        "no_hints":          ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="sunset",
    level_titles=[
        (1, "Principiante"),
        (6, "Studente"),
        (11, "Apprendista"),
        (16, "Conoscitore"),
        (21, "Esperto"),
        (26, "Maestro"),
    ],
)
