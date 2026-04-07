"""
School & Education skill pack — 学校与教育
Teaches school subjects, classroom objects, school actions,
talking about school, and school life. Guided by 龙龙 (Lóng Lóng).
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___  ___ _  _  ___   ___  _
 / __|/ __| || |/ _ \ / _ \| |
 \__ \ (__| __ | (_) | (_) | |__
 |___/\___|_||_|\___/ \___/|____|
"""

SKILL_PACK = SkillPack(
    id="school",
    title="School & Education — 学校与教育",
    subtitle="◈  With 龙龙's Help, Master Chinese School Life  ◈",
    save_file_name="school_quest",
    intro_story=INTRO_STORY,
    quit_message="龙龙 waves goodbye from the academy gates. Your school journey is saved — come back anytime!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Learner",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "school_subjects": "subject_scholar",
        "classroom_objects": "equipped_learner",
        "school_actions": "daily_grinder",
        "talking_about_school": "opinion_holder",
        "school_life": "campus_expert",
    },
    achievements={
        "subject_scholar":  ("Subject Scholar", "Named all five school subjects and discovered the 学 pattern!"),
        "equipped_learner": ("Equipped Learner", "Identified every classroom object and the 电 word family!"),
        "daily_grinder":    ("Daily Grinder", "Mastered every school action and the 上/下 pattern!"),
        "opinion_holder":   ("Opinion Holder", "Can discuss favorites, difficulty, and reasons in Chinese!"),
        "campus_expert":    ("Campus Expert", "Knows the people and places of school life and the 馆 pattern!"),
        "no_hints":         ("Standing Alone", "Completed a zone without any hints!"),
        "speed_reader":     ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "New Student"),
        (6, "Apprentice"),
        (11, "Scholar"),
        (16, "Honor Student"),
        (21, "Valedictorian"),
        (26, "Academy Master"),
    ],
)
