"""
Astronomy skill pack — The Star Observatory
Covers stars, the Moon, galaxies, space exploration, and astronaut life.
For ages 5-12, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _   ___ _____ ___  ___  _  _  ___  __  ____   __
 /_\ / __|_   _| _ \/ _ \| \| |/ _ \|  \/  \ \ / /
/ _ \\__ \ | | |   / (_) | .` | (_) | |\/| |\ V /
/_/ \_\___/ |_| |_|_\\___/|_|\_|\___/|_|  |_| |_|
"""

SKILL_PACK = SkillPack(
    id="astronomy",
    title="The Star Observatory",
    subtitle="◈  With Puck's Help, Every Star Reveals Its Story  ◈",
    save_file_name="astronomy_quest",
    intro_story=INTRO_STORY,
    quit_message="The observatory dome closes gently. Your place among the stars is saved — the cosmos will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Stargazer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "stars_constellations": "constellation_mapper",
        "the_moon": "lunar_scholar",
        "galaxies_universe": "galaxy_voyager",
        "space_exploration": "mission_specialist",
        "astronauts_space_life": "space_cadet",
    },
    achievements={
        "constellation_mapper": ("Constellation Mapper", "Charted the stars — from red giants to supernovae to the North Star!"),
        "lunar_scholar":        ("Lunar Scholar", "Mastered the Moon — phases, eclipses, tides, and craters!"),
        "galaxy_voyager":       ("Galaxy Voyager", "Journeyed through the Milky Way, Andromeda, and the Big Bang!"),
        "mission_specialist":   ("Mission Specialist", "Explored every great mission from Hubble to James Webb to Artemis!"),
        "space_cadet":          ("Space Cadet", "Learned what it takes to live and work in the void of space!"),
        "no_hints":             ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":         ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Stargazer"),
        (6, "Sky Watcher"),
        (11, "Astronomer"),
        (16, "Astrophysicist"),
        (21, "Cosmologist"),
        (26, "Carl Sagan"),
    ],
)
