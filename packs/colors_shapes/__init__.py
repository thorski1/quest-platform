"""
Colors & Shapes skill pack — Colors & Shapes
Teaches Chinese color words, shape vocabulary, color-noun patterns,
and the cultural significance of colors. Guided by Long Long (龙龙), a friendly dragon.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ ___  _    ___  ___  ___    ___   ___ _  _   _   ___ ___ ___
 / __/ _ \| |  / _ \| _ \/ __|  / __| / __| || | /_\ | _ \ __/ __|
| (_| (_) | |_| (_) |   /\__ \ | _. | \__ \ __ |/ _ \|  _/ _|\__ \
 \___\___/|____\___/|_|_\|___/  \___| |___/_||_/_/ \_\_| |___|___/
"""

SKILL_PACK = SkillPack(
    id="colors_shapes",
    title="Colors & Shapes",
    subtitle="Master colors, shapes, and their cultural meanings in Chinese",
    save_file_name="colors_shapes_quest",
    intro_story=INTRO_STORY,
    quit_message="Long Long waves goodbye -- your colorful progress is saved!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "basic_colors": "color_novice",
        "more_colors": "palette_expander",
        "shapes": "shape_sage",
        "describing_with_colors": "description_artist",
        "colors_in_culture": "cultural_scholar",
    },
    achievements={
        "color_novice":        ("Color Novice", "Mastered the six basic Chinese colors!"),
        "palette_expander":    ("Palette Expander", "Learned extended colors and shade modifiers!"),
        "shape_sage":          ("Shape Sage", "Can name all common shapes in Chinese!"),
        "description_artist":  ("Description Artist", "Combines colors and nouns like a native speaker!"),
        "cultural_scholar":    ("Cultural Scholar", "Understands the deep cultural meanings of Chinese colors!"),
        "no_hints":            ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":        ("Quick Eye", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Colorblind"),
        (6, "Tint Seeker"),
        (11, "Hue Apprentice"),
        (16, "Palette Knight"),
        (21, "Chromatic Sage"),
        (26, "Rainbow Dragon"),
    ],
)
