"""
Safety & First Aid skill pack — The Shield of Safety
Teaches home safety, road safety, water safety, stranger awareness,
internet safety, basic first aid, and emergency preparedness.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___   _   ___ ___ _______   __
/ __| /_\ | __| __|_   _\ \ / /
\__ \/ _ \| _|| _|  | |  \ V /
|___/_/ \_\_| |___| |_|   |_|
"""

SKILL_PACK = SkillPack(
    id="safety",
    title="The Shield of Safety",
    subtitle="◈  With Puck's Help, You Learn to Stay Safe  ◈",
    save_file_name="safety_quest",
    intro_story=INTRO_STORY,
    quit_message="The shield dims gently. Your place is saved — safety never sleeps, and neither does your knowledge!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Protector",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "home_safety": "home_guardian",
        "road_safety": "street_scholar",
        "water_safety": "water_wise",
        "stranger_safety": "trust_keeper",
        "internet_safety": "digital_defender",
        "basic_first_aid": "young_healer",
        "emergency_numbers": "emergency_ready",
    },
    achievements={
        "home_guardian":    ("Home Guardian", "Mastered fire safety, poison awareness, and home hazard rules!"),
        "street_scholar":   ("Street Scholar", "Learned every rule of the road — crosswalks, helmets, and seatbelts!"),
        "water_wise":       ("Water Wise", "Learned to respect the water and swim safely every time!"),
        "trust_keeper":     ("Trust Keeper", "Learned who to trust, how to say no, and when to tell an adult!"),
        "digital_defender": ("Digital Defender", "Mastered the rules of online safety and privacy!"),
        "young_healer":     ("Young Healer", "Learned first aid for cuts, bumps, burns, stings, and nosebleeds!"),
        "emergency_ready":  ("Emergency Ready", "Knows when and how to call 911, and what to say!"),
        "no_hints":         ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":     ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Aware"),
        (6, "Prepared"),
        (11, "First Responder"),
        (16, "Guardian"),
        (21, "Protector"),
        (26, "Safety Hero"),
    ],
)
