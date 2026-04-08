"""
Greetings skill pack — Bonjour!
Teaches French greetings, politeness, introductions, tu vs vous, and cafe culture.
Guided by Pierre, a friendly Parisian cafe owner.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___  ___  _  _    _  ___  _   _ ___
 | _ )/ _ \| \| |_ | |/ _ \| | | | _ \
 | _ \ (_) | .` | || | (_) | |_| |   /
 |___/\___/|_|\_|\__/ \___/ \___/|_|_\
"""

SKILL_PACK = SkillPack(
    id="greetings_fr",
    title="Bonjour!",
    subtitle="Greet, introduce yourself, and navigate French politeness",
    save_file_name="greetings_fr_quest",
    intro_story=INTRO_STORY,
    quit_message="Pierre tips his beret. A bientot -- your progress is saved!",
    name_prompt="[bold cyan]Comment vous appelez-vous?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "hello_goodbye": "greeting_star",
        "please_thank_you": "polite_soul",
        "self_introduction": "introduction_pro",
        "tu_vs_vous": "register_master",
        "at_the_cafe": "cafe_connoisseur",
    },
    achievements={
        "greeting_star":      ("Greeting Star", "Mastered bonjour, au revoir, and every French greeting!"),
        "polite_soul":        ("Polite Soul", "Knows s'il vous plait, merci, and all polite expressions!"),
        "introduction_pro":   ("Introduction Pro", "Can introduce yourself confidently in French!"),
        "register_master":    ("Register Master", "Understands when to use tu vs vous!"),
        "cafe_connoisseur":   ("Cafe Connoisseur", "Can order and converse at a French cafe!"),
        "no_hints":           ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
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
