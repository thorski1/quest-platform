"""
Daily Life skill pack — 日常生活
Teaches morning routines, school/work, hobbies, weather, shopping,
colors, and body parts. Guided by 龙龙 (Lóng Lóng).
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___   _   ___ _   __   __  _    ___ ___ ___
 |   \ /_\ |_ _| | \ \ / / | |  |_ _| __| __|
 | |) / _ \ | || |__\ V /  | |__ | || _|| _|
 |___/_/ \_\___|____||_|   |____|___|_| |___|
"""

SKILL_PACK = SkillPack(
    id="daily_life",
    title="Daily Life — 日常生活",
    subtitle="◈  With 龙龙's Help, Live a Day in Chinese  ◈",
    save_file_name="daily_life_quest",
    intro_story=INTRO_STORY,
    quit_message="龙龙 waves goodbye. Your daily journey is saved — come back anytime!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Learner",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "morning_routine": "early_riser",
        "school_work": "diligent_scholar",
        "hobbies": "hobby_hunter",
        "weather": "weather_watcher",
        "shopping": "bargain_master",
        "colors": "color_poet",
        "body_parts": "body_scholar",
    },
    achievements={
        "early_riser":      ("Early Riser", "Mastered the Chinese morning routine from 起床 to 出门!"),
        "diligent_scholar":  ("Diligent Scholar", "Learned school and work vocabulary including the 上/下 pattern!"),
        "hobby_hunter":     ("Hobby Hunter", "Can discuss hobbies and interests in Chinese!"),
        "weather_watcher":  ("Weather Watcher", "Mastered Chinese weather vocabulary and the 雨 radical family!"),
        "bargain_master":   ("Bargain Master", "Decoded Chinese prices, discounts, and shopping phrases!"),
        "color_poet":       ("Color Poet", "Learned all the colors and their cultural meanings!"),
        "body_scholar":     ("Body Scholar", "Named every body part and discovered body radicals in Chinese!"),
        "no_hints":         ("Standing Alone", "Completed a zone without any hints!"),
        "speed_reader":     ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Newcomer"),
        (6, "Regular"),
        (11, "Local"),
        (16, "Native Speaker"),
        (21, "Street Smart"),
        (26, "Daily Master"),
    ],
)
