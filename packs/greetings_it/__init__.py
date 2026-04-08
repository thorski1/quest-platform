"""
Ciao! skill pack — Greetings & Politeness
Teaches Italian greetings, pleasantries, introductions, formality, and ordering gelato.
Guided by a warm sunset narrative through an Italian piazza.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ ___   _   ___  _
 / __|_ _| /_\ / _ \| |
| (__ | | / _ \ (_) |_|
 \___|___/_/ \_\___/(_)
"""

SKILL_PACK = SkillPack(
    id="greetings_it",
    title="Ciao!",
    subtitle="Greetings, manners, and your first Italian conversations",
    save_file_name="greetings_it_quest",
    intro_story=INTRO_STORY,
    quit_message="The piazza empties as the evening deepens -- but your progress is saved. Arrivederci!",
    name_prompt="[bold cyan]Come ti chiami, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "hello_goodbye": "greeting_star",
        "please_thank_you": "polite_speaker",
        "introductions": "introduction_master",
        "tu_vs_lei": "formality_expert",
        "at_the_gelateria": "gelato_graduate",
    },
    achievements={
        "greeting_star":       ("Greeting Star", "Mastered ciao, buongiorno, and arrivederci!"),
        "polite_speaker":      ("Polite Speaker", "Per favore, grazie, and prego -- perfetto!"),
        "introduction_master": ("Introduction Master", "Can introduce yourself in Italian!"),
        "formality_expert":    ("Formality Expert", "Knows when to use tu and when to use Lei!"),
        "gelato_graduate":     ("Gelato Graduate", "Ordered gelato like a true Italian!"),
        "no_hints":            ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":        ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="sunset",
    level_titles=[
        (1, "Straniero"),
        (6, "Conoscente"),
        (11, "Amico"),
        (16, "Compagno"),
        (21, "Confidente"),
        (26, "Italiano Onorario"),
    ],
)
