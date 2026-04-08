"""
Statistics Basics skill pack — Statistics Fundamentals
Teaches core statistical concepts from central tendency to hypothesis testing.
For adults learning data science, guided by ARIA.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ____  _        _         ____            _
/ ___|| |_ __ _| |_ ___  | __ )  __ _ ___(_) ___ ___
\___ \| __/ _` | __/ __| |  _ \ / _` / __| |/ __/ __|
 ___) | || (_| | |_\__ \ | |_) | (_| \__ \ | (__\__ \
|____/ \__\__,_|\__|___/ |____/ \__,_|___/_|\___|___/
"""

SKILL_PACK = SkillPack(
    id="stats_basics",
    title="Statistics Fundamentals",
    subtitle="◈  The Language of Data  ◈",
    save_file_name="stats_basics_quest",
    intro_story=INTRO_STORY,
    quit_message="ARIA saves your progress to the dataset. The numbers will be here when you return.",
    name_prompt="[bold cyan]What's your name, analyst?[/bold cyan]",
    default_player_name="Analyst",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "mean_median_mode": "center_finder",
        "standard_deviation": "spread_master",
        "distributions": "curve_navigator",
        "correlation": "pattern_detective",
        "hypothesis_testing": "hypothesis_hero",
    },
    achievements={
        "center_finder":      ("Center Finder", "Mastered mean, median, and mode — the three faces of average!"),
        "spread_master":      ("Spread Master", "Understood variance and standard deviation — how data breathes!"),
        "curve_navigator":    ("Curve Navigator", "Navigated normal distributions, skew, and kurtosis!"),
        "pattern_detective":  ("Pattern Detective", "Learned to spot correlations — and the traps they hide!"),
        "hypothesis_hero":    ("Hypothesis Hero", "Conquered p-values, null hypotheses, and statistical significance!"),
        "no_hints":           ("Independent Analyst", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Calculator", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Curious"),
        (6, "Informed"),
        (11, "Literate"),
        (16, "Fluent"),
        (21, "Expert"),
        (26, "Sage"),
    ],
)
