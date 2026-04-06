"""
Brain Lab skill pack — The Brain Lab
Teaches neurons, senses, memory, emotions, and brain health.
For ages 5-12, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___  ___    _   _  _  _
| _ )| _ \  /_\ | || \| |
| _ \|   / / _ \| || .` |
|___/|_|_\/_/ \_\___|_|\_|
"""

SKILL_PACK = SkillPack(
    id="brain",
    title="The Brain Lab",
    subtitle="◈  With Puck's Help, Explore the Most Amazing Organ  ◈",
    save_file_name="brain_quest",
    intro_story=INTRO_STORY,
    quit_message="The Brain Lab dims gently. Your place is saved — your brain will keep working while you rest!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "how_your_brain_works": "neuron_navigator",
        "the_five_senses": "sense_master",
        "memory_and_learning": "memory_champion",
        "emotions_and_the_brain": "feelings_expert",
        "taking_care_of_your_brain": "brain_guardian",
    },
    achievements={
        "neuron_navigator":  ("Neuron Navigator", "Mapped neurons, signals, and the two halves of the brain!"),
        "sense_master":      ("Sense Master", "Explored sight, hearing, touch, taste, and smell!"),
        "memory_champion":   ("Memory Champion", "Unlocked the secrets of short-term, long-term, and muscle memory!"),
        "feelings_expert":   ("Feelings Expert", "Understood the amygdala, happiness chemicals, and every emotion!"),
        "brain_guardian":    ("Brain Guardian", "Learned how sleep, exercise, food, and water keep the brain healthy!"),
        "no_hints":          ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Neuron"),
        (6, "Synapse"),
        (11, "Thinker"),
        (16, "Scientist"),
        (21, "Neurologist"),
        (26, "Brain Master"),
    ],
)
