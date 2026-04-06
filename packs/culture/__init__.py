"""
Culture skill pack — 中国文化
Teaches festivals, zodiac, calligraphy, tea, martial arts, modern tech,
and four-character idioms (成语). Guided by 龙龙 (Lóng Lóng).
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ _   _ _  _____ _   _ ___ ___
 / __| | | | ||_   _| | | | _ \ __|
| (__| |_| | |__| | | |_| |   / _|
 \___|\___/|____|_|  \___/|_|_\___|
"""

SKILL_PACK = SkillPack(
    id="culture",
    title="Culture — 中国文化",
    subtitle="◈  With 龙龙's Help, Discover 5,000 Years of Wisdom  ◈",
    save_file_name="culture_quest",
    intro_story=INTRO_STORY,
    quit_message="龙龙 rolls up the culture scroll. Your journey is saved — 5,000 years of wisdom will wait for you!",
    name_prompt="[bold cyan]What's your name, culture explorer?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "chinese_festivals": "festival_dancer",
        "zodiac": "zodiac_master",
        "calligraphy": "brush_artist",
        "tea_culture": "tea_sage",
        "martial_arts": "warrior_scholar",
        "modern_china": "digital_native",
        "idioms_chengyu": "chengyu_sage",
    },
    achievements={
        "festival_dancer":  ("Festival Dancer", "Celebrated all four great Chinese festivals!"),
        "zodiac_master":    ("Zodiac Master", "Mastered all 12 animals, traits, and compatibility!"),
        "brush_artist":     ("Brush Artist", "Explored calligraphy tools, strokes, and scripts!"),
        "tea_sage":         ("Tea Sage", "Steeped in the art, history, and ceremony of Chinese tea!"),
        "warrior_scholar":  ("Warrior Scholar", "Understood kung fu, tai chi, and martial arts philosophy!"),
        "digital_native":   ("Digital Native", "Decoded WeChat, Alipay, and China's tech revolution!"),
        "chengyu_sage":     ("Chengyu Sage", "Mastered four-character idioms and used them in context!"),
        "no_hints":         ("Standing Alone", "Completed a zone without any hints!"),
        "speed_reader":     ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Curious Outsider"),
        (6, "Culture Seeker"),
        (11, "Tradition Learner"),
        (16, "Culture Bearer"),
        (21, "Wisdom Keeper"),
        (26, "Culture Master"),
    ],
)
