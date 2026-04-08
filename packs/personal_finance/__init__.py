"""
Personal Finance 101 skill pack — Budgeting, saving, debt, credit, and insurance.
Teaches foundational money management skills every adult needs.
Guided by SAGE, your financial advisor AI.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ____                                _   _____ _
|  _ \ ___ _ __ ___  ___  _ __   __ _| | |  ___(_)_ __   __ _ _ __   ___ ___
| |_) / _ \ '__/ __|/ _ \| '_ \ / _` | | | |_  | | '_ \ / _` | '_ \ / __/ _ \
|  __/  __/ |  \__ \ (_) | | | | (_| | | |  _| | | | | | (_| | | | | (_|  __/
|_|   \___|_|  |___/\___/|_| |_|\__,_|_| |_|   |_|_| |_|\__,_|_| |_|\___\___|
"""

SKILL_PACK = SkillPack(
    id="personal_finance",
    title="Personal Finance 101",
    subtitle="◈  Master Your Money, Secure Your Future  ◈",
    save_file_name="personal_finance_quest",
    intro_story=INTRO_STORY,
    quit_message="The ledger closes softly. Your progress is saved — SAGE will be here when you return.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Saver",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "budgeting_basics": "budget_builder",
        "emergency_funds": "safety_net_pro",
        "debt_management": "debt_destroyer",
        "credit_scores": "credit_commander",
        "insurance": "risk_shield",
    },
    achievements={
        "budget_builder":    ("Budget Builder", "Mastered the art of tracking income, expenses, and building a spending plan that works!"),
        "safety_net_pro":    ("Safety Net Pro", "Built an emergency fund strategy that protects against life's curveballs!"),
        "debt_destroyer":    ("Debt Destroyer", "Conquered debt management strategies from avalanche to snowball and beyond!"),
        "credit_commander":  ("Credit Commander", "Unlocked the secrets of credit scores, reports, and responsible credit use!"),
        "risk_shield":       ("Risk Shield", "Mastered insurance fundamentals to protect your health, home, and financial future!"),
        "no_hints":          ("Self-Sufficient", "Completed a zone without using any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="sunset",
    level_titles=[
        (1, "Spender"),
        (6, "Saver"),
        (11, "Planner"),
        (16, "Strategist"),
        (21, "Advisor"),
        (26, "Financial Master"),
    ],
)
