"""
Economics skill pack — The Market Square
Teaches wants vs needs, supply & demand, jobs & careers, saving & budgeting,
and trading & the global economy. For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___  ___  ___  _  _  ___  __  __ ___ ___  ___
| __|/ __\/ _ \| \| |/ _ \|  \/  |_ _/ __|/ __|
| _|| (__| (_) | .` | (_) | |\/| || | (__ \__ \
|___|\___|\___/|_|\_|\___/|_|  |_|___\___||___/
"""

SKILL_PACK = SkillPack(
    id="economics",
    title="The Market Square",
    subtitle="◈  With Puck's Help, the Economy Makes Sense  ◈",
    save_file_name="economics_quest",
    intro_story=INTRO_STORY,
    quit_message="The Market Square quiets down for the night. Your place is saved — the stalls will be here when you return!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Trader",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "wants_vs_needs": "smart_shopper",
        "supply_and_demand": "market_analyst",
        "jobs_and_careers": "career_explorer",
        "saving_and_budgeting": "budget_builder",
        "trading_and_global": "global_trader",
    },
    achievements={
        "smart_shopper":   ("Smart Shopper", "Mastered the difference between wants and needs!"),
        "market_analyst":  ("Market Analyst", "Understood supply, demand, and how prices work!"),
        "career_explorer": ("Career Explorer", "Explored the world of jobs, skills, and careers!"),
        "budget_builder":  ("Budget Builder", "Learned to save, budget, and spend wisely!"),
        "global_trader":   ("Global Trader", "Discovered how countries trade and the global economy works!"),
        "no_hints":        ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":    ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Shopper"),
        (6, "Trader"),
        (11, "Merchant"),
        (16, "Economist"),
        (21, "Tycoon"),
        (26, "Market Master"),
    ],
)
