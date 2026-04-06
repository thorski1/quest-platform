"""
Plants skill pack — The Secret Garden
Teaches plant anatomy, growth, photosynthesis, trees & forests,
and the plants we eat.
For ages 5-12, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 _____ _            ____                     _
|_   _| |__   ___  / ___|  ___  ___ _ __ ___| |_
  | | | '_ \ / _ \ \___ \ / _ \/ __| '__/ _ \ __|
  | | | | | |  __/  ___) |  __/ (__| | |  __/ |_
  |_| |_| |_|\___| |____/ \___|\___|_|  \___|\__|
  ____               _
 / ___| __ _ _ __ __| | ___ _ __
| |  _ / _` | '__/ _` |/ _ \ '_ \
| |_| | (_| | | | (_| |  __/ | | |
 \____|\__,_|_|  \__,_|\___|_| |_|
"""

SKILL_PACK = SkillPack(
    id="plants",
    title="The Secret Garden",
    subtitle="◈  With Puck's Help, Every Seed Has a Story  ◈",
    save_file_name="plants_quest",
    intro_story=INTRO_STORY,
    quit_message="The Primer closes softly. The garden rests — the seeds will be waiting when you come back!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Gardener",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "parts_of_a_plant": "plant_anatomist",
        "how_plants_grow": "green_thumb",
        "photosynthesis": "light_catcher",
        "trees_and_forests": "forest_guardian",
        "plants_we_eat": "garden_chef",
    },
    achievements={
        "plant_anatomist": ("Plant Anatomist", "Learned what roots, stems, leaves, flowers, and fruits do!"),
        "green_thumb":     ("Green Thumb", "Discovered how seeds germinate and plants grow strong!"),
        "light_catcher":   ("Light Catcher", "Understood photosynthesis — how plants make food from sunlight!"),
        "forest_guardian":  ("Forest Guardian", "Explored deciduous and evergreen trees, rainforests, and ancient giants!"),
        "garden_chef":     ("Garden Chef", "Discovered the fruits, vegetables, grains, and herbs that feed the world!"),
        "no_hints":        ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":    ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Seedling"),
        (6, "Sprout"),
        (11, "Sapling"),
        (16, "Gardener"),
        (21, "Botanist"),
        (26, "Grove Keeper"),
    ],
)
