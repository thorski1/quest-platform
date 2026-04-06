"""
Body & Health skill pack — Body & Health
Teaches Chinese body parts, feelings and emotions, medical vocabulary,
exercise and sports, and describing people. Guided by Long Long (龙龙), a friendly dragon.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ____            _         ___    _   _            _ _   _
 | __ )  ___   __| |_   _  ( _ )  | | | | ___  __ _| | |_| |__
 |  _ \ / _ \ / _` | | | | / _ \  | |_| |/ _ \/ _` | | __| '_ \
 | |_) | (_) | (_| | |_| || (_) | |  _  |  __/ (_| | | |_| | | |
 |____/ \___/ \__,_|\__, | \___/  |_| |_|\___|\__,_|_|\__|_| |_|
                    |___/
"""

SKILL_PACK = SkillPack(
    id="body_health",
    title="Body & Health",
    subtitle="Master body parts, feelings, medical terms, sports, and descriptions in Chinese",
    save_file_name="body_health_quest",
    intro_story=INTRO_STORY,
    quit_message="Long Long waves goodbye -- your body and health progress is saved!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "body_parts": "body_scholar",
        "feelings_emotions": "heart_speaker",
        "at_the_doctor": "healer_apprentice",
        "exercise_sports": "fitness_champion",
        "describing_people": "portrait_painter",
    },
    achievements={
        "body_scholar":       ("Body Scholar", "Mastered essential Chinese body part vocabulary!"),
        "heart_speaker":      ("Heart Speaker", "Can express feelings and emotions in Chinese!"),
        "healer_apprentice":  ("Healer's Apprentice", "Learned medical vocabulary for visiting the doctor!"),
        "fitness_champion":   ("Fitness Champion", "Mastered exercise and sports vocabulary in Chinese!"),
        "portrait_painter":   ("Portrait Painter", "Can describe people's appearance in Chinese!"),
        "no_hints":           ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Eye", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Health Novice"),
        (6, "Body Apprentice"),
        (11, "Feeling Seeker"),
        (16, "Healer Knight"),
        (21, "Fitness Sage"),
        (26, "Wellness Dragon"),
    ],
)
