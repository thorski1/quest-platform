"""
Greetings skill pack — The Art of Japanese Greetings
Teaches essential greetings, self-introduction, and polite expressions.
Guided by 先生 (Sensei) — a wise, patient Japanese teacher.
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
    id="greetings_jp",
    title="The Art of Japanese Greetings",
    subtitle="Master essential greetings, introductions, and polite expressions",
    save_file_name="greetings_jp_quest",
    intro_story=INTRO_STORY,
    quit_message="Sensei bows politely. Your progress is saved -- return to practice your greetings.",
    name_prompt="[bold cyan]What is your name, student?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "hello_goodbye": "greeting_master",
        "self_intro": "intro_master",
        "thanks_sorry": "polite_speaker",
        "counting_people": "people_counter",
        "classroom": "classroom_speaker",
        "keigo_basics": "keigo_beginner",
    },
    achievements={
        "greeting_master":   ("Greeting Master", "Mastered hello, goodbye, and daily greetings!"),
        "intro_master":      ("Introduction Master", "Can introduce yourself in Japanese!"),
        "polite_speaker":    ("Polite Speaker", "Knows how to thank, apologize, and be polite!"),
        "people_counter":    ("People Counter", "Learned to count and address people correctly!"),
        "classroom_speaker": ("Classroom Speaker", "Mastered classroom and everyday phrases!"),
        "keigo_beginner":    ("Keigo Beginner", "Took the first steps into polite Japanese speech!"),
        "no_hints":          ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Speaker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="ocean",
    level_titles=[
        (1, "Stranger"),
        (6, "Acquaintance"),
        (11, "Greeter"),
        (16, "Conversant"),
        (21, "Diplomat"),
        (26, "Social Sage"),
    ],
)
