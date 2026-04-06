"""
Geography skill pack — The Atlas of Wonders
Teaches continents, oceans, capitals, maps, landforms, and world wonders.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___  ___  ___   ___  ___    _   ___  _  _
 / __|| __|| _ \ / __|| _ \  /_\ | _ \| || |
| (_ || _| |   || (_ ||   / / _ \|  _/| __ |
 \___||___||_|_\ \___||_|_\/_/ \_\|_|  |_||_|
"""

SKILL_PACK = SkillPack(
    id="geography",
    title="The Atlas of Wonders",
    subtitle="◈  With Puck's Help, the Whole World Opens Up  ◈",
    save_file_name="geography_quest",
    intro_story=INTRO_STORY,
    quit_message="The atlas closes gently. Your place is saved — the world will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "continents": "continent_keeper",
        "oceans_and_seas": "ocean_navigator",
        "countries_capitals": "capital_scholar",
        "maps_and_directions": "map_reader",
        "landforms": "landform_explorer",
        "world_wonders": "wonder_keeper",
        "weather_and_climate": "climate_watcher",
        "flags_and_symbols": "flag_reader",
        "peoples_and_cultures": "culture_bridge",
        "rivers_and_lakes": "river_keeper",
        "animals_and_habitats": "habitat_explorer",
    },
    achievements={
        "continent_keeper":  ("Continent Keeper", "Named and located all seven continents!"),
        "ocean_navigator":   ("Ocean Navigator", "Sailed through every ocean and sea!"),
        "capital_scholar":   ("Capital Scholar", "Matched every country to its capital city!"),
        "map_reader":        ("Map Reader", "Read a map like a true explorer!"),
        "landform_explorer": ("Landform Explorer", "Named mountains, rivers, and deserts from around the world!"),
        "wonder_keeper":     ("Wonder Keeper", "Discovered the greatest wonders Earth has ever made!"),
        "climate_watcher":   ("Climate Watcher", "Explored climate zones, seasons, and the great monsoon rains!"),
        "flag_reader":       ("Flag Reader", "Recognised flags and national symbols from around the world!"),
        "culture_bridge":    ("Culture Bridge", "Explored languages, populations, and cultures across every continent!"),
        "river_keeper":      ("River Keeper", "Explored the world's greatest rivers and lakes!"),
        "habitat_explorer":  ("Habitat Explorer", "Discovered where animals live all around the world!"),
        "no_hints":          ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Seedling"),
        (6, "Sprout"),
        (11, "Bloom"),
        (16, "Star"),
        (21, "Wonder"),
        (26, "Sage"),
    ],
)
