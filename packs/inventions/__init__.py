"""
Inventions & Technology skill pack — The Workshop of Wonders
Teaches simple machines, great inventions, how things work, computers,
transportation, communication, and future technologies.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___ _  ___   _____ _  _ _____ ___ ___  _  _ ___
|_ _| \| \ \ / / __| \| |_   _|_ _/ _ \| \| / __|
 | || .` |\ V /| _|| .` | | |  | | (_) | .` \__ \
|___|_|\_| \_/ |___|_|\_| |_| |___\___/|_|\_|___/
"""

SKILL_PACK = SkillPack(
    id="inventions",
    title="The Workshop of Wonders",
    subtitle="◈  With Puck's Help, Every Invention Tells a Story  ◈",
    save_file_name="inventions_quest",
    intro_story=INTRO_STORY,
    quit_message="The workshop doors close gently. Your tools are saved — the inventions will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Inventor",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "simple_machines": "machine_master",
        "great_inventions": "invention_scholar",
        "how_things_work": "circuit_builder",
        "computers_basics": "digital_thinker",
        "transportation_history": "speed_historian",
        "communication_history": "message_keeper",
        "future_inventions": "future_visionary",
    },
    achievements={
        "machine_master":     ("Machine Master", "Understood all six simple machines!"),
        "invention_scholar":  ("Invention Scholar", "Met the inventors who changed the world!"),
        "circuit_builder":    ("Circuit Builder", "Mastered electricity, magnets, and circuits!"),
        "digital_thinker":    ("Digital Thinker", "Learned how computers work — down to binary!"),
        "speed_historian":    ("Speed Historian", "Traced transportation from horse to rocket!"),
        "message_keeper":     ("Message Keeper", "Followed communication from smoke to screen!"),
        "future_visionary":   ("Future Visionary", "Explored the inventions of tomorrow!"),
        "no_hints":           ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Curious"),
        (6, "Tinkerer"),
        (11, "Builder"),
        (16, "Inventor"),
        (21, "Visionary"),
        (26, "Da Vinci"),
    ],
)
