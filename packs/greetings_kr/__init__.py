"""
Greetings skill pack -- Korean Greetings
Teaches essential Korean greetings, self-introduction, and polite expressions.
Guided by an alien diplomat studying Earth's social protocols.
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
    id="greetings_kr",
    title="Korean Greetings",
    subtitle="Master essential Korean greetings, introductions, and polite expressions",
    save_file_name="greetings_kr_quest",
    intro_story=INTRO_STORY,
    quit_message="The alien diplomat bows. Your progress is saved -- return to practice your greetings.",
    name_prompt="[bold cyan]What is your name, traveler?[/bold cyan]",
    default_player_name="Traveler",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "hello_goodbye": "greeting_master",
        "thank_sorry": "polite_speaker",
        "self_intro": "intro_master",
        "polite_casual": "formality_navigator",
        "common_phrases": "phrase_collector",
    },
    achievements={
        "greeting_master":      ("Greeting Master", "Mastered hello, goodbye, and daily greetings!"),
        "polite_speaker":       ("Polite Speaker", "Knows how to thank, apologize, and be polite!"),
        "intro_master":         ("Introduction Master", "Can introduce yourself in Korean!"),
        "formality_navigator":  ("Formality Navigator", "Understands polite vs casual speech levels!"),
        "phrase_collector":     ("Phrase Collector", "Learned essential everyday Korean phrases!"),
        "no_hints":             ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":         ("Quick Speaker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="alien",
    level_titles=[
        (1, "Stranger"),
        (6, "Acquaintance"),
        (11, "Greeter"),
        (16, "Conversant"),
        (21, "Diplomat"),
        (26, "Social Sage"),
    ],
)
