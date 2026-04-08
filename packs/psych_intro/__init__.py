"""
psych_intro skill pack — Introduction to Psychology
A neural-themed RPG covering the foundations of psychology,
guided by ARIA through the architecture of the mind.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ____  ______   _______ _  _
|  _ \/ ___\ \ / / ____| || |
| |_) \___ \\ V /|  _| | || |_
|  __/ ___) || | | |___|__   _|
|_|   |____/ |_| |_____|  |_|
  ___ _   _ _____ ____   ___
 |_ _| \ | |_   _|  _ \ / _ \
  | ||  \| | | | | |_) | | | |
  | || |\  | | | |  _ <| |_| |
 |___|_| \_| |_| |_| \_\\___/
"""

SKILL_PACK = SkillPack(
    id="psych_intro",
    title="Introduction to Psychology",
    subtitle="◈  Explore the Architecture of Mind and Behavior  ◈",
    save_file_name="psych_intro_quest",
    intro_story=INTRO_STORY,
    quit_message="The neural pathways dim. Your progress is saved — the mind will be here when you return.",
    name_prompt="[bold cyan]What's your name, explorer?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "what_is_psychology": "mind_mapper",
        "research_methods": "empiricist",
        "brain_nervous_system": "neuroscientist",
        "sensation_perception": "perceiver",
        "states_of_consciousness": "dream_walker",
    },
    achievements={
        "mind_mapper":    ("Mind Mapper", "Charted the landscape of psychology from its philosophical roots to modern science!"),
        "empiricist":     ("Empiricist", "Mastered the scientific method as it applies to human behavior!"),
        "neuroscientist": ("Neuroscientist", "Navigated the brain and nervous system from neuron to cortex!"),
        "perceiver":      ("Perceiver", "Decoded how raw sensation becomes meaningful perception!"),
        "dream_walker":   ("Dream Walker", "Explored the spectrum of consciousness from waking to dreaming!"),
        "no_hints":       ("Independent Thinker", "Completed a zone without any hints!"),
        "speed_reader":   ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Novice"),
        (6, "Student"),
        (11, "Analyst"),
        (16, "Researcher"),
        (21, "Scholar"),
        (26, "Psychologist"),
    ],
)
