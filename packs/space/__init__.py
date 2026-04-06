"""
Space skill pack — The Book of Stars
Teaches the Solar System, stars, the Moon, space exploration, seasons, and more.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ ___  _   ___ ___
 / __| _ \/_\ / __| __|
 \__ \  _/ _ \ (__| _|
 |___/_|/_/ \_\___|___|
"""

SKILL_PACK = SkillPack(
    id="space",
    title="The Book of Stars",
    subtitle="◈  With Puck's Help, the Universe Opens Up  ◈",
    save_file_name="space_quest",
    intro_story=INTRO_STORY,
    quit_message="The star map folds gently closed. Your place is saved — the Universe will wait for you!",
    name_prompt="[bold cyan]What's your name, Stargazer?[/bold cyan]",
    default_player_name="Stargazer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "our_solar_system": "solar_system_scholar",
        "the_sun_and_stars": "stargazer",
        "the_moon": "moon_watcher",
        "planets_up_close": "planet_expert",
        "space_exploration": "mission_controller",
        "day_night_seasons": "sky_reader",
        "comets_and_asteroids": "comet_chaser",
    },
    achievements={
        "solar_system_scholar": ("Solar System Scholar", "Named and described all eight planets!"),
        "stargazer":            ("Stargazer", "Learned about stars, constellations, and what they really are!"),
        "moon_watcher":         ("Moon Watcher", "Explored the Moon's phases, tides, and human landings!"),
        "planet_expert":        ("Planet Expert", "Discovered what makes every planet unique!"),
        "mission_controller":   ("Mission Controller", "Followed space exploration from Gagarin to Mars rovers!"),
        "sky_reader":           ("Sky Reader", "Understood why day, night, and seasons happen!"),
        "comet_chaser":         ("Comet Chaser", "Tracked comets, asteroids, and the wanderers of the Solar System!"),
        "no_hints":             ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":         ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1,  "Earthling"),
        (6,  "Moonwalker"),
        (11, "Astronaut"),
        (16, "Star Pilot"),
        (21, "Galaxy Guide"),
        (26, "Cosmic Sage"),
    ],
)
