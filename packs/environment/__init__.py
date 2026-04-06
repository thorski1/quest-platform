"""
Environment & Ecology skill pack — The Green Pages
Teaches ecosystems, the water cycle, climate, recycling, endangered habitats,
renewable energy, and how kids can help the planet.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___  _  _ __   __ ___  ___   ___  _  _  __  __  ___  _  _  _____
| __|| \| |\ \ / /|_ _|| _ \ / _ \| \| ||  \/  || __|| \| ||_   _|
| _| | .` | \ V /  | | |   /| (_) | .` || |\/| || _| | .` |  | |
|___||_|\_|  \_/  |___||_|_\ \___/|_|\_||_|  |_||___||_|\_|  |_|
"""

SKILL_PACK = SkillPack(
    id="environment",
    title="The Green Pages",
    subtitle="◈  With Puck's Help, We Protect Our Planet  ◈",
    save_file_name="environment_quest",
    intro_story=INTRO_STORY,
    quit_message="The green pages close softly. Your place is saved — the planet will be here when you return!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Eco-Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "ecosystems": "ecosystem_expert",
        "water_cycle": "water_wizard",
        "climate_and_weather": "climate_scholar",
        "recycling": "recycling_champion",
        "endangered_earth": "habitat_defender",
        "renewable_energy": "energy_pioneer",
        "what_you_can_do": "eco_hero",
    },
    achievements={
        "ecosystem_expert":    ("Ecosystem Expert", "Explored food webs, producers, consumers, and the balance of nature!"),
        "water_wizard":        ("Water Wizard", "Traced every drop through the water cycle!"),
        "climate_scholar":     ("Climate Scholar", "Learned the difference between climate and weather and how seasons work!"),
        "recycling_champion":  ("Recycling Champion", "Mastered reduce, reuse, recycle — and composting too!"),
        "habitat_defender":    ("Habitat Defender", "Stood up for forests, oceans, coral reefs, and endangered places!"),
        "energy_pioneer":      ("Energy Pioneer", "Discovered solar, wind, and hydro power — the energy of the future!"),
        "eco_hero":            ("Eco Hero", "Learned how one kid can make a real difference for the planet!"),
        "no_hints":            ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":        ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Seedling"),
        (6, "Sprout"),
        (11, "Guardian"),
        (16, "Ranger"),
        (21, "Champion"),
        (26, "Earth Hero"),
    ],
)
