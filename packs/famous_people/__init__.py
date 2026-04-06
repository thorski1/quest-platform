"""
Famous People & Biographies skill pack — The Hall of Heroes
Teaches children about scientists, inventors, leaders, artists, explorers,
athletes, and modern heroes who changed the world.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 _  _   _   _    _      ___  ___   _  _ ___ ___  ___  ___ ___
| || | /_\ | |  | |    / _ \| __| | || | __| _ \/ _ \| __/ __|
| __ |/ _ \| |__| |__ | (_) | _|  | __ | _||   / (_) | _|\__ \
|_||_/_/ \_\____|____| \___/|_|   |_||_|___|_|_\\___/|___|___/
"""

SKILL_PACK = SkillPack(
    id="famous_people",
    title="The Hall of Heroes",
    subtitle="◈  With Puck's Help, Meet the People Who Changed the World  ◈",
    save_file_name="famous_people_quest",
    intro_story=INTRO_STORY,
    quit_message="The Hall of Heroes dims gently. Your place is saved — the heroes will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "scientists": "science_star",
        "inventors": "invention_spark",
        "leaders": "voice_of_change",
        "artists": "creative_soul",
        "explorers": "trailblazer",
        "athletes": "champion_spirit",
        "modern_heroes": "future_maker",
    },
    achievements={
        "science_star":     ("Science Star", "Met the scientists who unlocked the secrets of the universe!"),
        "invention_spark":  ("Invention Spark", "Discovered the inventors who built the modern world!"),
        "voice_of_change":  ("Voice of Change", "Learned about leaders who fought for justice and freedom!"),
        "creative_soul":    ("Creative Soul", "Explored the artists who filled the world with beauty!"),
        "trailblazer":      ("Trailblazer", "Followed the explorers who ventured into the unknown!"),
        "champion_spirit":  ("Champion Spirit", "Celebrated the athletes who showed what the human body can do!"),
        "future_maker":     ("Future Maker", "Met the modern heroes shaping tomorrow's world!"),
        "no_hints":         ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":     ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Fan"),
        (6, "Student"),
        (11, "Scholar"),
        (16, "Historian"),
        (21, "Biographer"),
        (26, "Legend"),
    ],
)
