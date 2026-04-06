"""
Insects skill pack — The Bug Safari
Teaches insect anatomy, butterflies & moths, ants & bees,
creepy crawlies, and insects' role in the environment.
For ages 5-12, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ _  _ ____  ___  ___ _____ ____
 |_ _| \| / ___|| __|/ __|_   _/ ___|
  | || .` \___ \| _|| (__  | | \___ \
 |___|_|\_|____/|___|\___|_|_| |____/
"""

SKILL_PACK = SkillPack(
    id="insects",
    title="The Bug Safari",
    subtitle="◈  With Puck's Help, Every Bug Has a Story  ◈",
    save_file_name="insects_quest",
    intro_story=INTRO_STORY,
    quit_message="The Primer closes softly. The insects rest — they'll be here when you come back!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "what_makes_an_insect": "anatomy_ace",
        "butterflies_and_moths": "wing_watcher",
        "ants_and_bees": "colony_keeper",
        "creepy_crawlies": "crawly_champion",
        "insects_and_environment": "eco_guardian",
    },
    achievements={
        "anatomy_ace":       ("Anatomy Ace", "Learned the three rules of insects — six legs, three body parts, exoskeleton!"),
        "wing_watcher":      ("Wing Watcher", "Followed the metamorphosis from caterpillar to butterfly!"),
        "colony_keeper":     ("Colony Keeper", "Explored the civilisations of ants and bees!"),
        "crawly_champion":   ("Crawly Champion", "Met spiders, beetles, dragonflies, and discovered they're incredible!"),
        "eco_guardian":      ("Eco Guardian", "Understood how insects power the planet — pollination, decomposition, and food chains!"),
        "no_hints":          ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Larva"),
        (6, "Nymph"),
        (11, "Forager"),
        (16, "Pollinator"),
        (21, "Entomologist"),
        (26, "Bug Champion"),
    ],
)
