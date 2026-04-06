"""
Science skill pack — The World of Wondering
Teaches living things, weather, the human body, and how things work.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___  ___ ___ ___ _  _  ___ ___
 / __|/ __|_ _| __| \| |/ __| __|
 \__ \ (__ | || _|| .` | (__| _|
 |___/\___|___|___|_|\_|\___|___|
"""

SKILL_PACK = SkillPack(
    id="science",
    title="The World of Wondering",
    subtitle="◈  With Puck's Help, Every Why Has an Answer  ◈",
    save_file_name="science_quest",
    intro_story=INTRO_STORY,
    quit_message="The garden rests. Your discoveries are saved. Come back soon!",
    name_prompt="[bold cyan]What's your name, explorer?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "living_things": "life_watcher",
        "sky_and_weather": "sky_reader",
        "body_basics": "body_explorer",
        "how_things_work": "wonder_worker",
        "simple_machines": "machine_master",
        "earth_and_space": "stargazer",
        "matter_and_energy": "matter_explorer",
        "weather_watch": "weather_watcher",
        "animal_world": "animal_explorer",
        "the_human_body": "body_scientist",
        "ecosystems_and_food_chains": "ecosystem_keeper",
    },
    achievements={
        "life_watcher": ("Life Watcher", "Discovered what makes things alive!"),
        "sky_reader": ("Sky Reader", "Learned the secrets of weather and the sky!"),
        "body_explorer": ("Body Explorer", "Understood your own amazing body!"),
        "wonder_worker": ("Wonder Worker", "Figured out how things work!"),
        "machine_master": ("Machine Master", "Mastered the six simple machines that built civilization!"),
        "stargazer": ("Stargazer", "Learned the secrets of Earth, the Moon, and the stars!"),
        "matter_explorer": ("Matter Explorer", "Explored the three states of matter and how they transform!"),
        "weather_watcher": ("Weather Watcher", "Read the sky and understood clouds, wind, seasons, and storms!"),
        "animal_explorer": ("Animal Explorer", "Explored the animal kingdom and discovered what makes each creature amazing!"),
        "body_scientist": ("Body Scientist", "Mastered the organs, systems, and science of the human body!"),
        "ecosystem_keeper": ("Ecosystem Keeper", "Understood how every living thing depends on every other!"),
        "no_hints": ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader": ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Seedling"),
        (6, "Sprout"),
        (11, "Bloom"),
        (16, "Star"),
        (21, "Wonder"),
        (26, "Sage"),
    ],
)
