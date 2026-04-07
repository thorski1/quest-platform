"""
Weather & Seasons skill pack — Weather Words, Seasons, Temperature & Climate,
Weather Forecasts, and Making Plans with Weather.
Teaches essential vocabulary for Japanese weather and seasonal life.
Guided by Umi (海) — a calm ocean guide.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 _    _ _____  ___ _____ _   _ _____ ____     ___   ____  _____ ___  ____   ___  _   _ ____
| |  | | ____|/ _ \_   _| | | | ____|  _ \   / / | / ___|| ____/ _ \/ ___| / _ \| \ | / ___|
| |  | |  _| | |_| || | | |_| |  _| | |_) | / /| |\___ \|  _|| |_| \___ \| | | |  \| \___ \
| |/\| | |___|  _  || | |  _  | |___|  _ < / / | | ___) | |__|  _  |___) | |_| | |\  |___) |
\_/\_/|_____|_| |_||_| |_| |_|_____|_| \_/_/  |_||____/|_____|_| |_|____/ \___/|_| \_|____/
"""

SKILL_PACK = SkillPack(
    id="weather_jp",
    title="Weather & Seasons",
    subtitle="Master weather vocabulary, seasons, temperature, forecasts, and weather-based planning",
    save_file_name="weather_jp_quest",
    intro_story=INTRO_STORY,
    quit_message="Umi watches the horizon. Your progress is saved -- return to continue your weather adventure.",
    name_prompt="[bold cyan]What is your name, weather watcher?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "weather_words": "weather_spotter",
        "seasons": "season_keeper",
        "temperature_climate": "climate_analyst",
        "weather_forecasts": "forecast_reader",
        "plans_with_weather": "weather_planner",
    },
    achievements={
        "weather_spotter":   ("Weather Spotter", "Can name every weather condition from sun to snow!"),
        "season_keeper":     ("Season Keeper", "Knows all four seasons and their cultural traditions!"),
        "climate_analyst":   ("Climate Analyst", "Masters temperature, humidity, and climate vocabulary!"),
        "forecast_reader":   ("Forecast Reader", "Can decode any Japanese weather forecast!"),
        "weather_planner":   ("Weather Planner", "Makes plans that work rain or shine!"),
        "no_hints":          ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="ocean",
    level_titles=[
        (1, "Newcomer"),
        (6, "Cloud Watcher"),
        (11, "Storm Tracker"),
        (16, "Season Walker"),
        (21, "Forecast Reader"),
        (26, "Weather Master"),
    ],
)
