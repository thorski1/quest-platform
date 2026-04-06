"""
Transport skill pack — Getting Around
Teaches Chinese transportation vocabulary, buying tickets, asking directions,
navigating stations, and travel conversations. Guided by Long Long (龙龙), a friendly dragon.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ____      _   _   _                _                           _
 / ___| ___| |_| |_(_)_ __   __ _  / \   _ __ ___  _   _ _ __  __| |
| |  _ / _ \ __| __| | '_ \ / _` |/ _ \ | '__/ _ \| | | | '_ \ / _` |
| |_| |  __/ |_| |_| | | | | (_| / ___ \| | | (_) | |_| | | | | (_| |
 \____|\___|\__|\__|_|_| |_|\__, /_/   \_\_|  \___/ \__,_|_| |_|\__,_|
                             |___/
"""

SKILL_PACK = SkillPack(
    id="transport",
    title="Getting Around",
    subtitle="Master transportation, tickets, directions, and travel talk in Chinese",
    save_file_name="transport_quest",
    intro_story=INTRO_STORY,
    quit_message="Long Long waves goodbye -- your transport progress is saved!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "transportation_words": "vehicle_master",
        "buying_tickets": "ticket_expert",
        "asking_directions": "pathfinder",
        "at_the_station": "station_navigator",
        "travel_conversations": "road_warrior",
    },
    achievements={
        "vehicle_master":      ("Vehicle Master", "Mastered essential Chinese transportation vocabulary!"),
        "ticket_expert":       ("Ticket Expert", "Can buy any ticket in Chinese with confidence!"),
        "pathfinder":          ("Pathfinder", "Can ask for and understand directions in Chinese!"),
        "station_navigator":   ("Station Navigator", "Can navigate any train or subway station in Chinese!"),
        "road_warrior":        ("Road Warrior", "Can hold real travel conversations in Chinese!"),
        "no_hints":            ("Solo Traveler", "Completed a zone without any hints!"),
        "speed_reader":        ("Quick Eye", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Travel Novice"),
        (6, "Ticket Seeker"),
        (11, "Direction Apprentice"),
        (16, "Station Knight"),
        (21, "Conversation Sage"),
        (26, "Transport Dragon"),
    ],
)
