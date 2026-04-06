"""
Hiragana skill pack — The Foundation of Japanese
Teaches all 46 basic hiragana characters through systematic rows.
Guided by 先生 (Sensei) — a wise, patient Japanese teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _  _ ___ ___    _    ___   _   _  _   _
 | || |_ _| _ \  /_\  / __| /_\ | \| | /_\
 | __ || ||   / / _ \| (_ |/ _ \| .` |/ _ \
 |_||_|___|_|_\/_/ \_\\___/_/ \_\_|\_/_/ \_\
"""

SKILL_PACK = SkillPack(
    id="hiragana",
    title="The Foundation of Japanese",
    subtitle="Master the 46 hiragana characters that unlock all of Japanese",
    save_file_name="hiragana_quest",
    intro_story=INTRO_STORY,
    quit_message="Sensei rolls up the calligraphy scroll. Your progress is saved -- return when you are ready to continue.",
    name_prompt="[bold cyan]What is your name, student?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "vowels": "vowel_master",
        "ka_row": "ka_scholar",
        "sa_row": "sa_scholar",
        "ta_row": "ta_scholar",
        "na_row": "na_scholar",
        "ha_ma_row": "ha_ma_scholar",
        "ya_ra_wa_n": "ya_ra_scholar",
        "reading_practice": "hiragana_reader",
    },
    achievements={
        "vowel_master":   ("Vowel Master", "Mastered all five Japanese vowels: あいうえお!"),
        "ka_scholar":     ("Ka Scholar", "Learned the entire ka-row: かきくけこ!"),
        "sa_scholar":     ("Sa Scholar", "Learned the entire sa-row: さしすせそ!"),
        "ta_scholar":     ("Ta Scholar", "Learned the entire ta-row: たちつてと!"),
        "na_scholar":     ("Na Scholar", "Learned the entire na-row: なにぬねの!"),
        "ha_ma_scholar":  ("Ha-Ma Scholar", "Learned the ha-row and ma-row!"),
        "ya_ra_scholar":  ("Ya-Ra Scholar", "Learned ya-row, ra-row, wa-row, and ん!"),
        "hiragana_reader": ("Hiragana Reader", "Can read complete words in hiragana!"),
        "no_hints":       ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":   ("Quick Reader", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="ocean",
    level_titles=[
        (1, "Beginner"),
        (6, "Apprentice"),
        (11, "Reader"),
        (16, "Scribe"),
        (21, "Calligrapher"),
        (26, "Hiragana Sage"),
    ],
)
