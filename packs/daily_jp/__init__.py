"""
Daily Life skill pack — Everyday Japanese
Teaches morning routine, school/work, hobbies, weather, shopping, and body/health.
Guided by 先生 (Sensei) — a wise, patient Japanese teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___   _   ___ _  __   __
 |   \ /_\ |_ _| | \ \ / /
 | |) / _ \ | || |__\ V /
 |___/_/ \_\___|____|_|_|
"""

SKILL_PACK = SkillPack(
    id="daily_jp",
    title="Everyday Japanese",
    subtitle="Master the language of daily life in Japan",
    save_file_name="daily_jp_quest",
    intro_story=INTRO_STORY,
    quit_message="Sensei waves goodbye. Your progress is saved -- return to continue your daily practice.",
    name_prompt="[bold cyan]What is your name, student?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "morning_routine": "morning_person",
        "school_work": "diligent_worker",
        "hobbies": "hobby_enthusiast",
        "weather": "weather_watcher",
        "shopping": "smart_shopper",
        "body_health": "health_conscious",
    },
    achievements={
        "morning_person":     ("Morning Person", "Mastered the vocabulary of a Japanese morning routine!"),
        "diligent_worker":    ("Diligent Worker", "Learned school and work vocabulary in Japanese!"),
        "hobby_enthusiast":   ("Hobby Enthusiast", "Can talk about hobbies and interests in Japanese!"),
        "weather_watcher":    ("Weather Watcher", "Knows how to discuss weather in Japanese!"),
        "smart_shopper":      ("Smart Shopper", "Can navigate shopping in Japanese!"),
        "health_conscious":   ("Health Conscious", "Learned body parts and health vocabulary in Japanese!"),
        "no_hints":           ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="ocean",
    level_titles=[
        (1, "Newcomer"),
        (6, "Resident"),
        (11, "Local"),
        (16, "Neighbor"),
        (21, "Community Member"),
        (26, "Daily Life Sage"),
    ],
)
