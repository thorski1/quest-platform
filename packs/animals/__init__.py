"""
Animals skill pack — The Animal Kingdom
Teaches animal groups, habitats, food chains, baby animals, superpowers,
endangered species, pets, and ocean creatures.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
    _   _  _ ___ __  __   _   _    ___
   /_\ | \| |_ _|  \/  | /_\ | |  / __|
  / _ \| .` || || |\/| |/ _ \| |__\__ \
 /_/ \_\_|\_|___|_|  |_/_/ \_\____|___/
"""

SKILL_PACK = SkillPack(
    id="animals",
    title="The Animal Kingdom",
    subtitle="◈  With Puck's Help, Every Creature Has a Story  ◈",
    save_file_name="animals_quest",
    intro_story=INTRO_STORY,
    quit_message="The Primer closes softly. The animals rest — they'll be here when you come back!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "animal_groups": "family_keeper",
        "habitats": "habitat_explorer",
        "food_chains": "chain_tracker",
        "baby_animals": "nursery_keeper",
        "animal_superpowers": "power_spotter",
        "endangered_species": "conservation_hero",
        "pets_and_care": "pet_guardian",
        "ocean_creatures": "deep_diver",
    },
    achievements={
        "family_keeper":     ("Family Keeper", "Learned what makes mammals, birds, reptiles, amphibians, fish, and insects special!"),
        "habitat_explorer":  ("Habitat Explorer", "Explored rainforests, deserts, oceans, arctic ice, and grasslands!"),
        "chain_tracker":     ("Chain Tracker", "Followed the food chain from producers to apex predators!"),
        "nursery_keeper":    ("Nursery Keeper", "Discovered how baby animals are born, grow, and transform!"),
        "power_spotter":     ("Power Spotter", "Uncovered nature's most incredible superpowers!"),
        "conservation_hero": ("Conservation Hero", "Learned about endangered species and how to help save them!"),
        "pet_guardian":      ("Pet Guardian", "Understood the joy and responsibility of caring for pets!"),
        "deep_diver":        ("Deep Diver", "Dove into the ocean world — from blue whales to bioluminescent creatures!"),
        "no_hints":          ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Cub"),
        (6, "Tracker"),
        (11, "Ranger"),
        (16, "Whisperer"),
        (21, "Guardian"),
        (26, "Naturalist"),
    ],
)
