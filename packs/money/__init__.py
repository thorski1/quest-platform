"""
Money & Economics skill pack — The Treasure Chest
Teaches the story of money, earning, saving, spending, banks, entrepreneurship,
giving, and global currencies. For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 __  __  ___  _  _ _____   __
|  \/  |/ _ \| \| | __\ \ / /
| |\/| | (_) | .` | _| \ V /
|_|  |_|\___/|_|\_|___| |_|
"""

SKILL_PACK = SkillPack(
    id="money",
    title="The Treasure Chest",
    subtitle="◈  With Puck's Help, Money Makes Sense  ◈",
    save_file_name="money_quest",
    intro_story=INTRO_STORY,
    quit_message="The treasure chest closes gently. Your place is saved — the coins will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Saver",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "what_is_money": "money_historian",
        "earning_and_saving": "smart_saver",
        "spending_wisely": "budget_master",
        "banks_and_interest": "vault_keeper",
        "entrepreneurship": "young_entrepreneur",
        "sharing_and_giving": "generous_heart",
        "global_money": "world_trader",
    },
    achievements={
        "money_historian":    ("Money Historian", "Traced the story of money from bartering to paper bills!"),
        "smart_saver":        ("Smart Saver", "Learned how to earn money and save it patiently!"),
        "budget_master":      ("Budget Master", "Mastered needs vs. wants and the art of budgeting!"),
        "vault_keeper":       ("Vault Keeper", "Opened the vault and understood banks and interest!"),
        "young_entrepreneur": ("Young Entrepreneur", "Built a lemonade stand and calculated real profit!"),
        "generous_heart":     ("Generous Heart", "Discovered the power of charity, taxes, and community!"),
        "world_trader":       ("World Trader", "Explored currencies and exchange rates around the globe!"),
        "no_hints":           ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Penny"),
        (6, "Saver"),
        (11, "Banker"),
        (16, "Investor"),
        (21, "Tycoon"),
        (26, "Mogul"),
    ],
)
