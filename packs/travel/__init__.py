"""
Travel skill pack — 旅行
Teaches transportation, directions, hotels, airports, sightseeing,
and emergency phrases. Guided by 龙龙 (Lóng Lóng).
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _____ ___    _   __   __ ___ _
 |_   _| _ \  /_\ \ \ / /| __| |
   | | |   / / _ \ \ V / | _|| |__
   |_| |_|_\/_/ \_\ \_/  |___|____|
"""

SKILL_PACK = SkillPack(
    id="travel",
    title="Travel — 旅行",
    subtitle="◈  With 龙龙's Help, Navigate China with Confidence  ◈",
    save_file_name="travel_quest",
    intro_story=INTRO_STORY,
    quit_message="龙龙 tucks the map away. Your travel progress is saved — the journey continues next time!",
    name_prompt="[bold cyan]What's your name, traveler?[/bold cyan]",
    default_player_name="Traveler",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "transportation": "road_warrior",
        "directions": "compass_reader",
        "at_the_hotel": "hotel_guest",
        "asking_directions": "pathfinder",
        "at_the_airport": "jet_setter",
        "sightseeing": "culture_explorer",
        "emergencies": "safety_first",
    },
    achievements={
        "road_warrior":      ("Road Warrior", "Mastered every mode of Chinese transportation!"),
        "compass_reader":    ("Compass Reader", "Learned all directions including 东南西北!"),
        "hotel_guest":       ("Hotel Guest", "Can check in, get WiFi, and check out — all in Chinese!"),
        "pathfinder":        ("Pathfinder", "Can ask for and follow directions in Chinese!"),
        "jet_setter":        ("Jet Setter", "Navigated the airport from passport to customs!"),
        "culture_explorer":  ("Culture Explorer", "Visited China's greatest landmarks in Chinese!"),
        "safety_first":      ("Safety First", "Learned all emergency phrases and numbers for China!"),
        "no_hints":          ("Standing Alone", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Tourist"),
        (6, "Backpacker"),
        (11, "Explorer"),
        (16, "Navigator"),
        (21, "Globe-Trotter"),
        (26, "World Traveler"),
    ],
)
