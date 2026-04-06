"""
Food & Drink skill pack — The Japanese Kitchen
Teaches common foods, drinks, ordering, tastes, chopstick etiquette, and food culture.
Guided by 先生 (Sensei) — a wise, patient Japanese teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___  ___   ___  ___
 | __|| _ \ / _ \|   \
 | _| |  _/| (_) | |) |
 |_|  |_|   \___/|___/
"""

SKILL_PACK = SkillPack(
    id="food_jp",
    title="The Japanese Kitchen",
    subtitle="Master the language of Japanese food, drink, and dining culture",
    save_file_name="food_jp_quest",
    intro_story=INTRO_STORY,
    quit_message="Sensei puts down the chopsticks. Your progress is saved -- return when you're hungry for more.",
    name_prompt="[bold cyan]What is your name, student?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "common_foods": "food_explorer",
        "drinks": "drink_connoisseur",
        "ordering": "order_master",
        "tastes": "taste_expert",
        "chopstick_etiquette": "chopstick_artist",
        "food_culture": "food_culturist",
    },
    achievements={
        "food_explorer":      ("Food Explorer", "Learned the names of essential Japanese foods!"),
        "drink_connoisseur":  ("Drink Connoisseur", "Mastered Japanese drink vocabulary!"),
        "order_master":       ("Order Master", "Can order food and drinks in Japanese!"),
        "taste_expert":       ("Taste Expert", "Knows how to describe flavors in Japanese!"),
        "chopstick_artist":   ("Chopstick Artist", "Learned proper chopstick etiquette!"),
        "food_culturist":     ("Food Culturist", "Understands Japanese dining customs and rituals!"),
        "no_hints":           ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Taster", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="ocean",
    level_titles=[
        (1, "Hungry Traveler"),
        (6, "Chopstick Novice"),
        (11, "Home Cook"),
        (16, "Ramen Regular"),
        (21, "Sushi Connoisseur"),
        (26, "Kitchen Sage"),
    ],
)
