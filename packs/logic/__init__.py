"""
The Puzzle Palace skill pack.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

SKILL_PACK = SkillPack(
    id="logic",
    title="The Puzzle Palace",
    subtitle="◈  Guided by Puck  ◈",
    save_file_name="logic_quest",
    intro_story=INTRO_STORY,
    quit_message="The Primer closes softly. See you next time!",
    name_prompt="[bold cyan]What\'s your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={},
    achievements={},
    kids_mode=True,
    level_titles=[
        (1, "Beginner"),
        (6, "Learner"),
        (11, "Thinker"),
        (16, "Expert"),
        (21, "Master"),
        (26, "Genius"),
    ],
)
