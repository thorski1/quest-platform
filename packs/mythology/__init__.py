"""
mythology skill pack — The Hall of Legends
Teaches world mythology: Greek, Norse, Egyptian, Asian legends, and mythical creatures.
For ages 8-11.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  __  ____   _______ _   _  ___  _     ___   ______   __
 |  \/  \ \ / /_   _| | | |/ _ \| |   / _ \ / ___\ \ / /
 | |\/| |\ V /  | | | |_| | | | | |  | | | | |  _ \ V /
 | |  | | | |   | | |  _  | |_| | |__| |_| | |_| | | |
 |_|  |_| |_|   |_| |_| |_|\___/|_____\___/ \____| |_|
"""

SKILL_PACK = SkillPack(
    id="mythology",
    title="The Hall of Legends",
    subtitle="◈  With Puck's Help, the Myths Come Alive  ◈",
    save_file_name="mythology_quest",
    intro_story=INTRO_STORY,
    quit_message="The book of legends closes gently. Your place is saved — the myths will wait for you!",
    name_prompt="[bold cyan]What's your name, young hero?[/bold cyan]",
    default_player_name="Hero",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "greek_mythology":    "olympian_scholar",
        "norse_mythology":    "rune_keeper",
        "egyptian_mythology": "pyramid_sage",
        "asian_legends":      "eastern_wisdom",
        "mythical_creatures": "bestiary_master",
    },
    achievements={
        "olympian_scholar":   ("Olympian Scholar", "Mastered the myths of Zeus, Athena, Hercules, and all of ancient Greece!"),
        "rune_keeper":        ("Rune Keeper", "Unlocked the secrets of Thor, Odin, Loki, and the nine worlds of Yggdrasil!"),
        "pyramid_sage":       ("Pyramid Sage", "Journeyed through the Egyptian afterlife with Ra, Anubis, and Isis!"),
        "eastern_wisdom":     ("Eastern Wisdom", "Discovered the dragons, kami, and gods of Asian mythology!"),
        "bestiary_master":    ("Bestiary Master", "Met every mythical creature from unicorns to krakens!"),
        "no_hints":           ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1,  "Seedling"),
        (6,  "Sprout"),
        (11, "Bloom"),
        (16, "Star"),
        (21, "Wonder"),
        (26, "Sage"),
    ],
)
