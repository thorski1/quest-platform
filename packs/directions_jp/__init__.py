"""
Directions & Places skill pack — Basic Directions, Places in Town,
Asking for Directions, Transportation, and Describing Locations.
Teaches practical navigation vocabulary and phrases for getting around
in Japanese towns and cities.
Guided by Umi (海) — a calm ocean guide.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___ ___ ___ ___ ___ _____ ___ ___  _  _ ___   ___   ___ _      _   ___ ___ ___
|   \_ _| _ \ __/ __|_   _|_ _/ _ \| \| / __| / / | | _ \ |    /_\ / __| __/ __|
| |) | ||   / _| (__  | |  | | (_) | .` \__ \/ /| |_|  _/ |__ / _ \ (__| _|\__ \
|___/___|_|_\___\___| |_| |___\___/|_|\_|___/_/  \___/_| |____/_/ \_\___|___|___/
"""

SKILL_PACK = SkillPack(
    id="directions_jp",
    title="Directions & Places",
    subtitle="Master directions, places, asking for help, transportation, and location descriptions",
    save_file_name="directions_jp_quest",
    intro_story=INTRO_STORY,
    quit_message="Umi waves from the harbor. Your progress is saved -- return to continue your navigation adventure.",
    name_prompt="[bold cyan]What is your name, navigator?[/bold cyan]",
    default_player_name="Navigator",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "basic_directions": "compass_reader",
        "places_in_town": "town_explorer",
        "asking_for_directions": "polite_asker",
        "transportation": "transit_rider",
        "describing_locations": "location_describer",
    },
    achievements={
        "compass_reader":     ("Compass Reader", "Mastered right, left, straight, and turn!"),
        "town_explorer":      ("Town Explorer", "Knows every important place in a Japanese town!"),
        "polite_asker":       ("Polite Asker", "Can ask for directions with perfect courtesy!"),
        "transit_rider":      ("Transit Rider", "Navigates trains, buses, and taxis with ease!"),
        "location_describer": ("Location Describer", "Describes positions like a local guide!"),
        "no_hints":           ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="ocean",
    level_titles=[
        (1, "Lost Tourist"),
        (6, "Street Reader"),
        (11, "Town Walker"),
        (16, "Direction Giver"),
        (21, "Local Navigator"),
        (26, "Wayfinding Master"),
    ],
)
