"""
Greetings skill pack — Grüße!
Teaches German greetings, polite expressions, introductions, and formal vs informal speech.
Guided by Ritter Wolf, a noble knight of the Sprachburg.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ____ ____  _   _ ___ _____ _____
 / ___|  _ \| | | / __|_   _| ____|
| |  _| |_) | | | \___ \ | | |  _|
| |_| |  _ <| |_| |___) || | | |___
 \____|_| \_\\___/|____/ |_| |_____|
"""

SKILL_PACK = SkillPack(
    id="greetings_de",
    title="Grüße!",
    subtitle="Greet, introduce yourself, and be polite in German",
    save_file_name="greetings_de_quest",
    intro_story=INTRO_STORY,
    quit_message="Ritter Wolf tips his helmet. 'Auf Wiedersehen! Your greetings are saved in the castle records!'",
    name_prompt="[bold cyan]What is your name, brave learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "hello_goodbye": "greeting_knight",
        "please_thankyou": "polite_champion",
        "introductions": "introduction_herald",
        "du_sie": "formality_master",
        "at_the_bakery": "bakery_regular",
    },
    achievements={
        "greeting_knight":      ("Greeting Knight", "Mastered hello and goodbye in German!"),
        "polite_champion":      ("Polite Champion", "Please, thank you, and sorry -- all conquered!"),
        "introduction_herald":  ("Introduction Herald", "Can introduce yourself like a true knight!"),
        "formality_master":     ("Formality Master", "Knows when to use du and when to use Sie!"),
        "bakery_regular":       ("Bakery Regular", "Survived your first real-world German conversation!"),
        "no_hints":             ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":         ("Quick Tongue", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Stranger"),
        (6, "Acquaintance"),
        (11, "Companion"),
        (16, "Trusted Ally"),
        (21, "Court Speaker"),
        (26, "Royal Diplomat"),
    ],
)
