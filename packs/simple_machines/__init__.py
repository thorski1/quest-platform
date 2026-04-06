"""
Simple Machines skill pack — The Inventor's Workshop
Teaches levers, wheels, pulleys, ramps, wedges, and compound machines.
For ages 5-12, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ ___ __  __ ___ _    ___   __  __   _   ___ _  _ ___ _  _ ___ ___
 / __|_ _|  \/  | _ \ |  | __| |  \/  | /_\ / __| || |_ _| \| | __/ __|
 \__ \| || |\/| |  _/ |__| _|  | |\/| |/ _ \ (__| __ || || .` | _|\__ \
 |___/___|_|  |_|_| |____|___| |_|  |_/_/ \_\___|_||_|___|_|\_|___|___/
"""

SKILL_PACK = SkillPack(
    id="simple_machines",
    title="The Inventor's Workshop",
    subtitle="Discover levers, pulleys, wheels, and how machines make work easier!",
    save_file_name="simple_machines_quest",
    intro_story=INTRO_STORY,
    quit_message="The workshop rests. Your inventions are saved. Come back soon!",
    name_prompt="[bold cyan]What's your name, inventor?[/bold cyan]",
    default_player_name="Inventor",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "levers_and_fulcrums": "lever_master",
        "wheels_and_axles": "wheel_wright",
        "pulleys_and_gears": "pulley_pro",
        "inclined_planes_and_wedges": "ramp_builder",
        "compound_machines": "grand_inventor",
    },
    achievements={
        "lever_master":   ("Lever Master", "Mastered levers, fulcrums, and the power to move the world!"),
        "wheel_wright":   ("Wheel Wright", "Discovered why the wheel changed everything!"),
        "pulley_pro":     ("Pulley Pro", "Learned how pulleys and gears lift the impossible!"),
        "ramp_builder":   ("Ramp Builder", "Conquered inclined planes, wedges, and screws!"),
        "grand_inventor": ("Grand Inventor", "Combined all simple machines into compound inventions!"),
        "no_hints":       ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":   ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Tinker"),
        (6, "Builder"),
        (11, "Mechanic"),
        (16, "Engineer"),
        (21, "Inventor"),
        (26, "Master Inventor"),
    ],
)
