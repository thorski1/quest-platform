"""
Hobbies & Free Time skill pack — 爱好与休闲
Teaches sports, music & art, reading & media, outdoor activities,
and talking about hobbies. Guided by 龙龙 (Lóng Lóng).
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _  _  ___  ___  ___ ___ ___ ___
 | || |/ _ \| _ )| _ )_ _| __/ __|
 | __ | (_) | _ \| _ \| || _|\__ \
 |_||_|\___/|___/|___/___|___|___/
"""

SKILL_PACK = SkillPack(
    id="hobbies",
    title="Hobbies & Free Time — 爱好与休闲",
    subtitle="◈  With 龙龙's Help, Master Chinese Hobby Talk  ◈",
    save_file_name="hobbies_quest",
    intro_story=INTRO_STORY,
    quit_message="龙龙 waves goodbye from the Hall of Pastimes. Your hobby journey is saved — come back anytime!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Learner",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "sports_exercise": "arena_champion",
        "music_art": "tower_bard",
        "reading_media": "library_lord",
        "outdoor_activities": "wild_warden",
        "talking_about_hobbies": "grand_councilor",
    },
    achievements={
        "arena_champion":  ("Arena Champion", "Mastered all five sports and the 打 vs. 踢 pattern!"),
        "tower_bard":      ("Tower Bard", "Learned every art form and discovered the 琴 instrument family!"),
        "library_lord":    ("Library Lord", "Catalogued all media hobbies and the versatile 看 pattern!"),
        "wild_warden":     ("Wild Warden", "Explored every outdoor activity and the 步 step pattern!"),
        "grand_councilor": ("Grand Councilor", "Can discuss hobbies, preferences, and reasons in Chinese!"),
        "no_hints":        ("Standing Alone", "Completed a zone without any hints!"),
        "speed_reader":    ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Hobbyist"),
        (6, "Enthusiast"),
        (11, "Aficionado"),
        (16, "Devotee"),
        (21, "Connoisseur"),
        (26, "Grandmaster of Pastimes"),
    ],
)
