"""
Investing Fundamentals skill pack — Stocks, bonds, ETFs, risk, and diversification.
Teaches the core principles every new investor needs to start building wealth.
Guided by SAGE, your financial advisor AI.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___                     _   _               ___ ___  _
|_ _|_ ___   _____  ___| |_(_)_ __   __ _  / _ \_ _|/ |
 | || '_ \ \ / / _ \/ __| __| | '_ \ / _` || | | || || |
 | || | | \ V /  __/\__ \ |_| | | | | (_| || |_| || || |
|___|_| |_|\_/ \___||___/\__|_|_| |_|\__, | \___/|___|_|
                                      |___/
"""

SKILL_PACK = SkillPack(
    id="investing_101",
    title="Investing Fundamentals",
    subtitle="◈  Build Wealth Through Smart Investing  ◈",
    save_file_name="investing_101_quest",
    intro_story=INTRO_STORY,
    quit_message="The trading floor dims. Your progress is saved — SAGE will be here when you return.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Investor",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "stocks_basics": "stock_picker",
        "bonds_fixed_income": "bond_analyst",
        "index_funds_etfs": "index_advocate",
        "risk_and_return": "risk_manager",
        "portfolio_diversification": "portfolio_architect",
    },
    achievements={
        "stock_picker":        ("Stock Picker", "Mastered the fundamentals of stocks, shares, and equity ownership!"),
        "bond_analyst":        ("Bond Analyst", "Understood bonds, yields, and the role of fixed income in a portfolio!"),
        "index_advocate":      ("Index Advocate", "Learned why index funds and ETFs are the backbone of smart investing!"),
        "risk_manager":        ("Risk Manager", "Grasped the relationship between risk and return and how to manage both!"),
        "portfolio_architect": ("Portfolio Architect", "Built a diversified portfolio strategy tailored to your goals and timeline!"),
        "no_hints":            ("Self-Sufficient", "Completed a zone without using any hints!"),
        "speed_reader":        ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="sunset",
    level_titles=[
        (1, "Observer"),
        (6, "Beginner Investor"),
        (11, "Active Investor"),
        (16, "Strategist"),
        (21, "Portfolio Manager"),
        (26, "Market Sage"),
    ],
)
