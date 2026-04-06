"""
Maps & Navigation skill pack — The Map Room
Teaches reading maps, compass directions, types of maps, coordinates,
navigation skills, famous maps, and digital maps.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 __  __    _    ___  ___
|  \/  |  /_\  | _ \/ __|
| |\/| | / _ \ |  _/\__ \
|_|  |_|/_/ \_\|_|  |___/
"""

SKILL_PACK = SkillPack(
    id="maps",
    title="The Map Room",
    subtitle="◈  With Puck's Help, Every Line Leads to Adventure  ◈",
    save_file_name="maps_quest",
    intro_story=INTRO_STORY,
    quit_message="The Map Room door closes softly. Your place is saved — the maps will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Navigator",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "reading_maps": "map_reader",
        "compass_directions": "compass_master",
        "types_of_maps": "map_collector",
        "coordinates": "coordinate_finder",
        "map_skills": "navigator",
        "famous_maps": "map_historian",
        "digital_maps": "digital_explorer",
    },
    achievements={
        "map_reader":        ("Map Reader", "Learned to read symbols, legends, scale bars, and titles on any map!"),
        "compass_master":    ("Compass Master", "Mastered all four cardinal directions and the compass rose!"),
        "map_collector":     ("Map Collector", "Explored every kind of map — from road maps to satellite images!"),
        "coordinate_finder": ("Coordinate Finder", "Learned latitude, longitude, and grid references to find any place on Earth!"),
        "navigator":         ("Navigator", "Mastered route planning, distance measuring, and real-world map use!"),
        "map_historian":     ("Map Historian", "Explored maps from ancient Babylon to Mars and the ocean floor!"),
        "digital_explorer":  ("Digital Explorer", "Discovered GPS, satellites, navigation apps, and the future of maps!"),
        "no_hints":          ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Scout"),
        (6, "Navigator"),
        (11, "Explorer"),
        (16, "Cartographer"),
        (21, "Captain"),
        (26, "World Mapper"),
    ],
)
