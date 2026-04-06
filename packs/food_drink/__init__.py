"""
Food & Drink skill pack — The Dragon's Kitchen
Teaches Chinese food vocabulary, ordering, tastes, cooking, and food culture.
Guided by Long Long (龙龙), a friendly dragon.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___ ___   ___  ___    ___   ___  ___ ___ _  _ _  __
| __/ _ \ / _ \|   \  |   \ | _ \|_ _| \| | |/ /
| _| (_) | (_) | |) | | |) ||   / | || .` | ' <
|_| \___/ \___/|___/  |___/ |_|_\|___|_|\_|_|\_\
"""

SKILL_PACK = SkillPack(
    id="food_drink",
    title="The Dragon's Kitchen",
    subtitle="Eat, drink, and talk about food in Mandarin",
    save_file_name="food_drink_quest",
    intro_story=INTRO_STORY,
    quit_message="Long Long wraps up the leftovers. Your progress is saved -- come back hungry!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "fruits_vegetables": "produce_picker",
        "drinks": "drink_master",
        "common_dishes": "dish_expert",
        "ordering_food": "restaurant_pro",
        "tastes": "flavor_seeker",
        "cooking_words": "kitchen_dragon",
        "food_culture": "culture_foodie",
    },
    achievements={
        "produce_picker":  ("Produce Picker", "Knows fruits and vegetables in Chinese!"),
        "drink_master":    ("Drink Master", "Can order any drink in Mandarin!"),
        "dish_expert":     ("Dish Expert", "Recognizes the most famous Chinese dishes!"),
        "restaurant_pro":  ("Restaurant Pro", "Can order a full meal in a Chinese restaurant!"),
        "flavor_seeker":   ("Flavor Seeker", "Mastered the five flavors of Chinese cuisine!"),
        "kitchen_dragon":  ("Kitchen Dragon", "Knows all the essential cooking methods!"),
        "culture_foodie":  ("Culture Foodie", "Understands the deep culture behind Chinese food!"),
        "no_hints":        ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":    ("Quick Taster", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Hungry Traveler"),
        (6, "Street Food Fan"),
        (11, "Home Cook"),
        (16, "Chef's Apprentice"),
        (21, "Master Chef"),
        (26, "Culinary Dragon"),
    ],
)
