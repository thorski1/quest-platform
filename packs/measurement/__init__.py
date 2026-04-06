"""
Measurement & Units skill pack — The Measuring Workshop
Teaches length, weight, volume, temperature, comparing, tools, and real-world measurements.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 __  __ ___   _   ___ _   _ ___ ___
|  \/  | __| /_\ / __| | | | _ \ __|
| |\/| | _| / _ \\__ \ |_| |   / _|
|_|  |_|___/_/ \_\___/\___/|_|_\___|
"""

SKILL_PACK = SkillPack(
    id="measurement",
    title="The Measuring Workshop",
    subtitle="◈  With Puck's Help, Everything Can Be Measured  ◈",
    save_file_name="measurement_quest",
    intro_story=INTRO_STORY,
    quit_message="The workshop closes gently. Your place is saved — the measurements will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Measurer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "length": "length_master",
        "weight": "weight_master",
        "volume": "volume_master",
        "temperature": "temperature_master",
        "comparing": "comparison_expert",
        "tools": "tool_expert",
        "real_world": "real_world_master",
    },
    achievements={
        "length_master":      ("Length Master", "Measured everything from inches to meters with confidence!"),
        "weight_master":      ("Weight Master", "Weighed everything from paperclips to elephants!"),
        "volume_master":      ("Volume Master", "Measured cups, liters, and gallons like a pro!"),
        "temperature_master": ("Temperature Master", "Explored the whole thermometer from freezing to boiling!"),
        "comparison_expert":  ("Comparison Expert", "Compared sizes, weights, and lengths like a scientist!"),
        "tool_expert":        ("Tool Expert", "Knows exactly which measuring tool to use for every job!"),
        "real_world_master":  ("Real World Master", "Measured miles, buildings, whales, and everything in between!"),
        "no_hints":           ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Counter"),
        (6, "Measurer"),
        (11, "Calculator"),
        (16, "Engineer"),
        (21, "Scientist"),
        (26, "Einstein"),
    ],
)
