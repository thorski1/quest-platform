"""
German Basics skill pack — Die Grundlagen
Teaches the German alphabet, articles, pronouns, essential verbs, and word order.
Guided by Ritter Wolf, a noble knight of the Sprachburg.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ____    _    ____ ___ ____ ____
 | __ )  / \  / ___|_ _/ ___/ ___|
 |  _ \ / _ \ \___ \| | |   \___ \
 | |_) / ___ \ ___) | | |___ ___) |
 |____/_/   \_\____/___\____|____/
"""

SKILL_PACK = SkillPack(
    id="basics_de",
    title="German Basics",
    subtitle="Master the foundations of the German language",
    save_file_name="basics_de_quest",
    intro_story=INTRO_STORY,
    quit_message="Ritter Wolf sheathes his sword and bows. Your progress has been inscribed in the castle ledger!",
    name_prompt="[bold cyan]What is your name, brave learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "alphabet_pronunciation": "sound_scholar",
        "articles": "article_knight",
        "personal_pronouns": "pronoun_squire",
        "sein_haben": "verb_warrior",
        "word_order": "sentence_architect",
    },
    achievements={
        "sound_scholar":       ("Sound Scholar", "Mastered the German alphabet and special sounds!"),
        "article_knight":      ("Article Knight", "Conquered der, die, and das!"),
        "pronoun_squire":      ("Pronoun Squire", "Learned all the German personal pronouns!"),
        "verb_warrior":        ("Verb Warrior", "Conjugated sein and haben like a true knight!"),
        "sentence_architect":  ("Sentence Architect", "Understands German word order rules!"),
        "no_hints":            ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":        ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Peasant"),
        (6, "Apprentice"),
        (11, "Squire"),
        (16, "Knight"),
        (21, "Baron"),
        (26, "Grandmaster"),
    ],
)
