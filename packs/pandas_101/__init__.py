"""
Pandas 101 skill pack — Pandas Mastery
Teaches the pandas library for data manipulation and analysis.
For adults learning data science, guided by ARIA.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ____                  _            ___ ___  _
|  _ \ __ _ _ __   __| | __ _ ___ / _ \_ _|/ |
| |_) / _` | '_ \ / _` |/ _` / __| | | | | | |
|  __/ (_| | | | | (_| | (_| \__ \ |_| | | | |
|_|   \__,_|_| |_|\__,_|\__,_|___/\___/___|_|
"""

SKILL_PACK = SkillPack(
    id="pandas_101",
    title="Pandas Mastery",
    subtitle="◈  Wrangle, Shape & Transform Data  ◈",
    save_file_name="pandas_101_quest",
    intro_story=INTRO_STORY,
    quit_message="ARIA commits your DataFrame to memory. Your progress is saved — the data will be here when you return.",
    name_prompt="[bold cyan]What's your name, data wrangler?[/bold cyan]",
    default_player_name="Wrangler",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "dataframes": "frame_builder",
        "selection_filtering": "data_slicer",
        "groupby_aggregation": "aggregation_ace",
        "merging_joining": "merge_master",
        "data_cleaning": "clean_machine",
    },
    achievements={
        "frame_builder":     ("Frame Builder", "Created, inspected, and understood the DataFrame — pandas' core structure!"),
        "data_slicer":       ("Data Slicer", "Mastered loc, iloc, and boolean indexing — surgical data selection!"),
        "aggregation_ace":   ("Aggregation Ace", "Grouped, aggregated, and transformed — turning rows into insights!"),
        "merge_master":      ("Merge Master", "Joined DataFrames like a relational database pro!"),
        "clean_machine":     ("Clean Machine", "Tamed missing values, duplicates, and messy data types!"),
        "no_hints":          ("Independent Wrangler", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Query", "Answered a question in under 10 seconds!"),
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
