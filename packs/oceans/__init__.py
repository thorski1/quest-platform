"""
Ocean Explorers skill pack — The Deep Dive
Teaches ocean zones, marine mammals, coral reefs, deep-sea creatures,
ocean currents, sharks and rays, and ocean conservation.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___   ___ ___   _   _  _  ___
 / _ \ / __| __| /_\ | \| |/ __|
| (_) | (__| _| / _ \| .` |\__ \
 \___/ \___|___/_/ \_\_|\_||___/
"""

SKILL_PACK = SkillPack(
    id="oceans",
    title="The Deep Dive",
    subtitle="◈  With Puck's Help, the Ocean Reveals Its Secrets  ◈",
    save_file_name="oceans_quest",
    intro_story=INTRO_STORY,
    quit_message="The submarine surfaces gently. Your place is saved — the ocean will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "ocean_zones": "zone_mapper",
        "marine_mammals": "mammal_watcher",
        "coral_reefs": "reef_guardian",
        "deep_sea": "abyss_diver",
        "ocean_currents": "current_rider",
        "sharks_and_rays": "shark_scholar",
        "ocean_conservation": "ocean_guardian",
    },
    achievements={
        "zone_mapper":     ("Zone Mapper", "Explored every layer of the ocean from sunlight to abyss!"),
        "mammal_watcher":  ("Mammal Watcher", "Met every warm-blooded creature in the cold ocean!"),
        "reef_guardian":    ("Reef Guardian", "Understood coral reefs — their beauty and their fragility!"),
        "abyss_diver":     ("Abyss Diver", "Explored the strangest creatures in the deepest darkness!"),
        "current_rider":   ("Current Rider", "Rode the invisible rivers that shape our planet's climate!"),
        "shark_scholar":    ("Shark Scholar", "Met the ocean's most ancient and misunderstood predators!"),
        "ocean_guardian":   ("Ocean Guardian", "Learned how to protect the ocean — and promised to try!"),
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
