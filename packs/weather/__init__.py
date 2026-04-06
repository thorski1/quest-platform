"""
Weather & Seasons skill pack — The Weather Station
Teaches weather types, water cycle, clouds, severe weather, seasons,
weather tools, and forecasting.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 __      __ ___    _  _____ _  _ ___  ___
 \ \    / /| __|  /_\|_   _| || || __|| _ \
  \ \/\/ / | _|  / _ \ | | | __ || _| |   /
   \_/\_/  |___|/_/ \_\|_| |_||_||___||_|_\
"""

SKILL_PACK = SkillPack(
    id="weather",
    title="The Weather Station",
    subtitle="◈  With Puck's Help, Every Cloud Tells a Story  ◈",
    save_file_name="weather_quest",
    intro_story=INTRO_STORY,
    quit_message="The Weather Station doors close softly. Your place is saved — the sky will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "types_of_weather": "weather_watcher",
        "water_cycle_deep": "cycle_master",
        "clouds": "cloud_reader",
        "severe_weather": "storm_survivor",
        "seasons_deep": "season_scholar",
        "weather_tools": "instrument_keeper",
        "weather_forecasting": "forecaster",
    },
    achievements={
        "weather_watcher":    ("Weather Watcher", "Learned what causes every type of weather!"),
        "cycle_master":       ("Cycle Master", "Followed water on its never-ending journey!"),
        "cloud_reader":       ("Cloud Reader", "Named every cloud type and learned to read the sky!"),
        "storm_survivor":     ("Storm Survivor", "Faced the fiercest storms and learned to stay safe!"),
        "season_scholar":     ("Season Scholar", "Discovered why Earth has seasons!"),
        "instrument_keeper":  ("Instrument Keeper", "Mastered every weather tool from thermometer to satellite!"),
        "forecaster":         ("Forecaster", "Learned to predict the weather like a real meteorologist!"),
        "no_hints":           ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Cloud Watcher"),
        (6, "Rain Reader"),
        (11, "Storm Chaser"),
        (16, "Forecaster"),
        (21, "Meteorologist"),
        (26, "Weather Wizard"),
    ],
)
