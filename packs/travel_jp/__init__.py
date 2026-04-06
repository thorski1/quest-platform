"""
Travel skill pack — Traveling in Japan
Teaches transportation, directions, hotels, asking for help, sightseeing, and emergencies.
Guided by 先生 (Sensei) — a wise, patient Japanese teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 _____ ___    _ __   __ ___  _
|_   _| _ \  /_\\ \ / /| __|| |
  | | |   / / _ \\ V / | _| | |__
  |_| |_|_\/_/ \_\\_/  |___||____|
"""

SKILL_PACK = SkillPack(
    id="travel_jp",
    title="Traveling in Japan",
    subtitle="Navigate Japan with confidence -- trains, hotels, directions, and emergencies",
    save_file_name="travel_jp_quest",
    intro_story=INTRO_STORY,
    quit_message="Sensei hands you a rail pass. Your progress is saved -- the journey continues when you return.",
    name_prompt="[bold cyan]What is your name, student?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "transportation": "train_rider",
        "directions": "navigator",
        "hotel": "guest_master",
        "asking_help": "help_seeker",
        "sightseeing": "sightseer",
        "emergencies": "crisis_handler",
    },
    achievements={
        "train_rider":    ("Train Rider", "Mastered Japanese transportation vocabulary!"),
        "navigator":      ("Navigator", "Can ask for and understand directions in Japanese!"),
        "guest_master":   ("Guest Master", "Knows how to navigate hotels and accommodation in Japanese!"),
        "help_seeker":    ("Help Seeker", "Can ask for help politely in Japanese!"),
        "sightseer":      ("Sightseer", "Learned sightseeing vocabulary in Japanese!"),
        "crisis_handler": ("Crisis Handler", "Prepared for emergencies with Japanese survival phrases!"),
        "no_hints":       ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":   ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="ocean",
    level_titles=[
        (1, "Tourist"),
        (6, "Backpacker"),
        (11, "Traveler"),
        (16, "Explorer"),
        (21, "Globetrotter"),
        (26, "Travel Sage"),
    ],
)
