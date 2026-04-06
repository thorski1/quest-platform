"""
Body Explorer skill pack — The Body Explorer
Teaches bones, muscles, heart, lungs, brain, digestion, exercise,
immunity, and growing up. For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___   ___  ___  __   __
| _ ) / _ \|   \ \ \ / /
| _ \| (_) | |) | \ V /
|___/ \___/|___/   |_|
"""

SKILL_PACK = SkillPack(
    id="body",
    title="The Body Explorer",
    subtitle="◈  With Puck's Help, Discover the Amazing You  ◈",
    save_file_name="body_quest",
    intro_story=INTRO_STORY,
    quit_message="The body map folds gently closed. Your place is saved — your body will keep working while you rest!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "bones_and_muscles": "skeleton_scholar",
        "heart_and_blood": "heart_hero",
        "lungs_and_breathing": "breath_master",
        "brain_and_nerves": "brain_explorer",
        "digestion": "digestion_guide",
        "exercise_and_fitness": "fitness_champion",
        "germs_and_immunity": "immunity_warrior",
        "growing_up": "growth_guru",
    },
    achievements={
        "skeleton_scholar":  ("Skeleton Scholar", "Named every bone, joint, and muscle challenge in the body!"),
        "heart_hero":        ("Heart Hero", "Followed the blood from heart to body and back again!"),
        "breath_master":     ("Breath Master", "Understood lungs, oxygen, and the mighty diaphragm!"),
        "brain_explorer":    ("Brain Explorer", "Mapped the brain, the senses, and the lightning-fast nerves!"),
        "digestion_guide":   ("Digestion Guide", "Followed food on its incredible nine-metre journey!"),
        "fitness_champion":  ("Fitness Champion", "Mastered cardio, strength, flexibility, and the power of sleep!"),
        "immunity_warrior":  ("Immunity Warrior", "Defeated germs and discovered the body's amazing defences!"),
        "growth_guru":       ("Growth Guru", "Explored how bodies grow, change, and become uniquely amazing!"),
        "no_hints":          ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Cell"),
        (6, "Student"),
        (11, "Medic"),
        (16, "Doctor"),
        (21, "Surgeon"),
        (26, "Professor"),
    ],
)
