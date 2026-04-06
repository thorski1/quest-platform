"""
Time & Calendar skill pack — The Clock Tower
Teaches telling time, AM/PM, days, months, seasons, elapsed time,
calendars, and time zones around the world.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___  _     ___   ___  _  __  _____  ___  _    _  ___  ___
 / __|| |   / _ \ / __|| |/ / |_   _|/ _ \| |  | || __|| _ \
| (__ | |_ | (_) || (__ |   <    | | | (_) || |/\| || _| |   /
 \___||___| \___/  \___||_|\_\   |_|  \___/ \_/\_/ |___||_|_\
"""

SKILL_PACK = SkillPack(
    id="telling_time",
    title="The Clock Tower",
    subtitle="◈  With Puck's Help, Time Makes Sense  ◈",
    save_file_name="telling_time_quest",
    intro_story=INTRO_STORY,
    quit_message="The Clock Tower falls quiet. Your place is saved — time will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "telling_time": "clock_reader",
        "am_and_pm": "day_night_knower",
        "days_of_week": "week_walker",
        "months_and_seasons": "season_keeper",
        "elapsed_time": "time_mathematician",
        "calendars": "calendar_master",
        "time_around_world": "world_clock_keeper",
    },
    achievements={
        "clock_reader":       ("Clock Reader", "Read the hour hand, minute hand, and every position on the clock face!"),
        "day_night_knower":   ("Day & Night Knower", "Mastered AM and PM, noon and midnight!"),
        "week_walker":        ("Week Walker", "Learned all seven days and their perfect order!"),
        "season_keeper":      ("Season Keeper", "Named every month and matched them to their seasons!"),
        "time_mathematician": ("Time Mathematician", "Calculated elapsed time like a true clockmaker!"),
        "calendar_master":    ("Calendar Master", "Read calendars, found dates, and counted days with ease!"),
        "world_clock_keeper": ("World Clock Keeper", "Understood time zones and why the world ticks at different hours!"),
        "no_hints":           ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Second"),
        (6, "Minute"),
        (11, "Hour"),
        (16, "Clockmaker"),
        (21, "Time Keeper"),
        (26, "Time Lord"),
    ],
)
