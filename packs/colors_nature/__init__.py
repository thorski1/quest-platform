"""
Colors & Nature skill pack — Colors, Nature, and Scenic Description
Teaches basic colors, color adjective grammar, nature words, seasons,
and how to describe scenery using adjective + noun patterns.
Guided by Umi (海) — a calm nature guide.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ ___  _    ___  ___  ___   ___   _  _   _ _____ _   _ ___ ___
 / __/ _ \| |  / _ \| _ \/ __| / / | | \| | /_\_   _| | | | _ \ __|
| (_| (_) | |_| (_) |   /\__ \/ /| |_| .` |/ _ \| | | |_| |   / _|
 \___\___/|____\___/|_|_\|___/_/  \___/_|\_/_/ \_\_|  \___/|_|_\___|
"""

SKILL_PACK = SkillPack(
    id="colors_nature",
    title="Colors & Nature",
    subtitle="Master colors, nature vocabulary, seasons, and scenic description",
    save_file_name="colors_nature_quest",
    intro_story=INTRO_STORY,
    quit_message="Umi waves gently. Your progress is saved -- return to continue exploring nature's colors.",
    name_prompt="[bold cyan]What is your name, traveler?[/bold cyan]",
    default_player_name="Traveler",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "basic_colors": "color_basics",
        "i_na_adjectives": "adjective_master",
        "nature_words": "nature_explorer",
        "seasons": "season_traveler",
        "describing_scenery": "scenery_painter",
    },
    achievements={
        "color_basics":      ("Color Basics", "Learned the six essential Japanese colors!"),
        "adjective_master":  ("Adjective Master", "Understands i-adjective and na-adjective color grammar!"),
        "nature_explorer":   ("Nature Explorer", "Knows the kanji for mountains, oceans, flowers, and more!"),
        "season_traveler":   ("Season Traveler", "Journeyed through all four Japanese seasons!"),
        "scenery_painter":   ("Scenery Painter", "Can describe beautiful scenery in Japanese!"),
        "no_hints":          ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="ocean",
    level_titles=[
        (1, "Observer"),
        (6, "Color Spotter"),
        (11, "Nature Walker"),
        (16, "Season Keeper"),
        (21, "Landscape Poet"),
        (26, "Scenery Master"),
    ],
)
