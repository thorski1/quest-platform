"""
Cooking & Nutrition skill pack — The Kitchen Adventure
Teaches food groups, vitamins, labels, kitchen safety, cooking basics,
world foods, and healthy choices.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ ___   ___  _  _____ _  _  ___
 / __/ _ \ / _ \| |/ /_ _| \| |/ __|
| (_| (_) | (_) | ' < | || .` | (_ |
 \___\___/ \___/|_|\_\___|_|\_|\___|
"""

SKILL_PACK = SkillPack(
    id="cooking",
    title="The Kitchen Adventure",
    subtitle="◈  With Puck's Help, Food Becomes an Adventure  ◈",
    save_file_name="cooking_quest",
    intro_story=INTRO_STORY,
    quit_message="The kitchen lights dim gently. Your place is saved — the recipes will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Chef",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "food_groups": "food_group_master",
        "vitamins_and_nutrients": "nutrient_hunter",
        "reading_labels": "label_detective",
        "kitchen_safety": "safety_star",
        "cooking_basics": "junior_chef",
        "foods_around_world": "world_taster",
        "healthy_choices": "wise_eater",
    },
    achievements={
        "food_group_master":  ("Food Group Master", "Learned what all five food groups do for your body!"),
        "nutrient_hunter":    ("Nutrient Hunter", "Discovered the vitamins and minerals hidden inside your food!"),
        "label_detective":    ("Label Detective", "Learned to read nutrition labels like a pro!"),
        "safety_star":        ("Safety Star", "Mastered every kitchen safety rule!"),
        "junior_chef":        ("Junior Chef", "Learned measuring, mixing, and the basics of cooking!"),
        "world_taster":       ("World Taster", "Tasted your way around the globe — from sushi to tacos!"),
        "wise_eater":         ("Wise Eater", "Learned to make balanced, healthy choices every day!"),
        "no_hints":           ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Taster"),
        (6, "Helper"),
        (11, "Sous Chef"),
        (16, "Chef"),
        (21, "Master Chef"),
        (26, "Iron Chef"),
    ],
)
