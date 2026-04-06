"""
Cultures of the World skill pack — The World Festival
Teaches children about celebrations, foods, clothing, languages, and homes
from cultures around the globe.
For ages 5-12, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 _____ _  _ ___  __      _____  ___ _    ___    ___ ___ ___ _____ _____   ___   _
|_   _| || | __| \ \    / / _ \| _ \ |  |   \  | __| __/ __|_   _|_ _\ \ / /_\ | |
  | | | __ | _|   \ \/\/ / (_) |   / |__| |) | | _|| _|\__ \ | |  | | \ V / _ \| |__
  |_| |_||_|___|   \_/\_/ \___/|_|_\____|___/  |_| |___|___/ |_| |___| \_/_/ \_\____|
"""

SKILL_PACK = SkillPack(
    id="cultures",
    title="The World Festival",
    subtitle="◈  With Puck's Help, Discover How People Live Around the World  ◈",
    save_file_name="cultures_quest",
    intro_story=INTRO_STORY,
    quit_message="The World Festival grows quiet. Your place is saved — the world will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "celebrations": "festival_explorer",
        "traditional_foods": "global_chef",
        "traditional_clothing": "fashion_scholar",
        "languages": "word_traveller",
        "homes": "world_architect",
    },
    achievements={
        "festival_explorer": ("Festival Explorer", "Discovered how people celebrate around the world!"),
        "global_chef":       ("Global Chef", "Tasted the traditional foods of every continent!"),
        "fashion_scholar":   ("Fashion Scholar", "Learned about the beautiful clothing of different cultures!"),
        "word_traveller":    ("Word Traveller", "Explored the incredible variety of the world's languages!"),
        "world_architect":   ("World Architect", "Visited the amazing homes people build around the world!"),
        "no_hints":          ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Explorer"),
        (6, "Traveller"),
        (11, "Student"),
        (16, "Ambassador"),
        (21, "Citizen of the World"),
        (26, "Cultural Legend"),
    ],
)
