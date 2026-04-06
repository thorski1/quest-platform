"""
Planets skill pack — The Telescope (Solar System Deep Dive)
Goes deep into each planet — far beyond the basics.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___  _      _   _  _  ___ _____  ___
| _ \| |    /_\ | \| || __|_   _|/ __|
|  _/| |__ / _ \| .` || _|  | |  \__ \
|_|  |____/_/ \_\_|\_||___| |_|  |___/
"""

SKILL_PACK = SkillPack(
    id="planets",
    title="The Telescope",
    subtitle="◈  With Puck's Help, Every Planet Reveals Its Secrets  ◈",
    save_file_name="planets_quest",
    intro_story=INTRO_STORY,
    quit_message="The telescope retracts gently. Your place among the stars is saved — the planets will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Stargazer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "mercury_venus": "scorched_worlds_explorer",
        "earth_moon_deep": "earth_moon_expert",
        "mars_deep": "mars_rover_driver",
        "jupiter_saturn_deep": "gas_giant_navigator",
        "ice_giants": "ice_giant_pioneer",
        "dwarf_planets": "dwarf_planet_hunter",
        "space_missions": "mission_commander",
    },
    achievements={
        "scorched_worlds_explorer": ("Scorched Worlds Explorer", "Survived Mercury's extremes and Venus's greenhouse inferno!"),
        "earth_moon_expert":        ("Earth & Moon Expert", "Explored Earth's layers, magnetic shield, and the Moon's fiery origin!"),
        "mars_rover_driver":        ("Mars Rover Driver", "Climbed Olympus Mons, crossed Valles Marineris, and drove the rovers!"),
        "gas_giant_navigator":      ("Gas Giant Navigator", "Explored Jupiter's storms, Europa's ocean, Saturn's rings, and Titan!"),
        "ice_giant_pioneer":        ("Ice Giant Pioneer", "Discovered diamond rain, sideways planets, and supersonic winds!"),
        "dwarf_planet_hunter":      ("Dwarf Planet Hunter", "Met Pluto's heart, Haumea's spin, and the icy Kuiper Belt!"),
        "mission_commander":        ("Mission Commander", "Celebrated every great mission from Voyager to Artemis!"),
        "no_hints":                 ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":             ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Stargazer"),
        (6, "Astronaut"),
        (11, "Mission Control"),
        (16, "Planet Hunter"),
        (21, "Astrophysicist"),
        (26, "Carl Sagan"),
    ],
)
