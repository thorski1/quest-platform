"""
Shopping & Money skill pack — Numbers, Counters, Currency, Store Phrases,
Polite Requests, Bargaining, and Receipts.
Teaches practical shopping vocabulary and cultural etiquette for navigating
Japanese markets and stores.
Guided by Umi (海) — a calm ocean guide.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___ _  _  ___  ___ ___ ___ _  _  ___   ___   __  __  ___  _  _ _____   __
/ __| || |/ _ \| _ \ _ \_ _| \| |/ __| / / | |  \/  |/ _ \| \| | __\ \ / /
\__ \ __ | (_) |  _/  _/| || .` | (_ |/ /| |_| |\/| | (_) | .` | _| \ V /
|___/_||_|\___/|_| |_| |___|_|\_|\___|_/  \___/_|  |_|\___/|_|\_|___| |_|
"""

SKILL_PACK = SkillPack(
    id="shopping_jp",
    title="Shopping & Money",
    subtitle="Master counters, currency, store phrases, polite requests, and bargaining",
    save_file_name="shopping_jp_quest",
    intro_story=INTRO_STORY,
    quit_message="Umi waves from the market. Your progress is saved -- return to continue your shopping adventure.",
    name_prompt="[bold cyan]What is your name, shopper?[/bold cyan]",
    default_player_name="Shopper",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "numbers_counters": "counter_expert",
        "money": "money_wise",
        "at_the_store": "store_navigator",
        "polite_requests": "courtesy_master",
        "bargaining_receipts": "bargain_hunter",
    },
    achievements={
        "counter_expert":    ("Counter Expert", "Mastered Japanese counters for every shape!"),
        "money_wise":        ("Money Wise", "Knows yen, change, and tax like a local!"),
        "store_navigator":   ("Store Navigator", "Can find and buy anything in a Japanese store!"),
        "courtesy_master":   ("Courtesy Master", "Speaks with the politeness of a seasoned shopper!"),
        "bargain_hunter":    ("Bargain Hunter", "Reads discount signs and calculates sale prices!"),
        "no_hints":          ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="ocean",
    level_titles=[
        (1, "Window Shopper"),
        (6, "Coin Counter"),
        (11, "Market Regular"),
        (16, "Polite Customer"),
        (21, "Deal Finder"),
        (26, "Shopping Master"),
    ],
)
