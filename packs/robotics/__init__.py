"""
Robotics skill pack — The Robot Factory
Teaches robotics concepts through analogy, logic, and real-world examples.
No actual hardware required — just ideas, curiosity, and understanding.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ____   ___  ____   ___  _____
|  _ \ / _ \| __ ) / _ \|_   _|
| |_) | | | |  _ \| | | | | |
|  _ <| |_| | |_) | |_| | | |
|_| \_\\___/|____/ \___/  |_|
"""

SKILL_PACK = SkillPack(
    id="robotics",
    title="The Robot Factory",
    subtitle="◈  With Puck's Help, Machines Come Alive  ◈",
    save_file_name="robotics_quest",
    intro_story=INTRO_STORY,
    quit_message="The factory powers down quietly. Come back whenever you're ready.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Engineer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "what_is_a_robot": "robot_spotter",
        "robot_parts": "master_builder",
        "programming_robots": "robot_programmer",
        "robots_in_the_real_world": "world_explorer",
        "future_of_robots": "future_thinker",
    },
    achievements={
        "robot_spotter":     ("Robot Spotter",     "Learned what makes a robot a robot!"),
        "master_builder":    ("Master Builder",    "Understood motors, sensors, grippers, and batteries!"),
        "robot_programmer":  ("Robot Programmer",  "Mastered step-by-step instructions, loops, and sensor logic!"),
        "world_explorer":    ("World Explorer",    "Discovered robots in factories, hospitals, space, and the ocean!"),
        "future_thinker":    ("Future Thinker",    "Explored self-driving cars, drones, swarms, and robot ethics!"),
        "no_hints":          ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker",     "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Tinker"),
        (6, "Mechanic"),
        (11, "Engineer"),
        (16, "Inventor"),
        (21, "Visionary"),
        (26, "Robot Sage"),
    ],
)
