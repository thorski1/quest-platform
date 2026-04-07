"""
Ocean Explore skill pack — The Deep Dive
Teaches ocean zones, coral reefs, deep-sea creatures,
ocean conservation, and underwater technology.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___   ___ ___   _   _  _
 / _ \ / __| __| /_\ | \| |
| (_) | (__| _| / _ \| .` |
 \___/ \___|___/_/ \_\_|\_|
 ___ _  _ ___ _    ___  ___ ___
| __\ \/ | _ | |  / _ \| _ | __|
| _| >  <|  _| |_| (_) |   | _|
|___/_/\_|_| |____\___/|_|_|___|
"""

SKILL_PACK = SkillPack(
    id="ocean_explore",
    title="The Deep Dive",
    subtitle="◈  With Puck's Help, Explore Every Secret of the Ocean  ◈",
    save_file_name="ocean_explore_quest",
    intro_story=INTRO_STORY,
    quit_message="The research vessel surfaces gently. Your place is saved — the ocean will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "ocean_zones": "zone_explorer",
        "coral_reefs": "reef_scholar",
        "deep_sea_creatures": "abyss_navigator",
        "ocean_conservation": "ocean_protector",
        "underwater_technology": "tech_pioneer",
    },
    achievements={
        "zone_explorer":    ("Zone Explorer", "Mapped every layer of the ocean from sunlight to hadal trench!"),
        "reef_scholar":     ("Reef Scholar", "Understood coral reefs — their beauty, their builders, and their battles!"),
        "abyss_navigator":  ("Abyss Navigator", "Met the strangest and most wonderful creatures of the deep!"),
        "ocean_protector":  ("Ocean Protector", "Learned how to protect the ocean — and promised to try!"),
        "tech_pioneer":     ("Tech Pioneer", "Mastered the machines that take us into the deep unknown!"),
        "no_hints":         ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":     ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Snorkeler"),
        (6, "Diver"),
        (11, "Explorer"),
        (16, "Navigator"),
        (21, "Captain"),
        (26, "Admiral"),
    ],
)
