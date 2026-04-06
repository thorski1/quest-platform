"""
Weather & Time skill pack — Weather & Time
Teaches Chinese weather vocabulary, seasons, telling time,
days and months, and making weather-based plans. Guided by Long Long (龙龙), a friendly dragon.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 __      __        _   _               ___   _____ _
 \ \    / /__ __ _| |_| |_  ___ _ _   / __| |_   _(_)_ __  ___
  \ \/\/ / -_) _` |  _| ' \/ -_) '_| | (_ |   | | | | '  \/ -_)
   \_/\_/\___\__,_|\__|_||_\___|_|    \___|   |_| |_|_|_|_\___|
"""

SKILL_PACK = SkillPack(
    id="weather_time",
    title="Weather & Time",
    subtitle="Master weather, seasons, time, and making plans in Chinese",
    save_file_name="weather_time_quest",
    intro_story=INTRO_STORY,
    quit_message="Long Long waves goodbye -- your weather and time progress is saved!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "weather_words": "weather_watcher",
        "seasons": "season_keeper",
        "telling_time": "time_lord",
        "days_months": "calendar_commander",
        "making_plans": "master_planner",
    },
    achievements={
        "weather_watcher":      ("Weather Watcher", "Mastered essential Chinese weather vocabulary!"),
        "season_keeper":        ("Season Keeper", "Learned all four seasons and their weather!"),
        "time_lord":            ("Time Lord", "Can tell time fluently in Chinese!"),
        "calendar_commander":   ("Calendar Commander", "Mastered days, months, and years in Chinese!"),
        "master_planner":       ("Master Planner", "Can make weather-based plans in Chinese like a native!"),
        "no_hints":             ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":         ("Quick Eye", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Weather Novice"),
        (6, "Season Seeker"),
        (11, "Time Apprentice"),
        (16, "Calendar Knight"),
        (21, "Planning Sage"),
        (26, "Chrono Dragon"),
    ],
)
