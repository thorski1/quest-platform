"""
Katakana skill pack — The Script of the World
Teaches all katakana characters for reading loanwords and foreign names.
Guided by 先生 (Sensei) — a wise, patient Japanese teacher.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _  __   _ _____  _   _  __   _  _  _   _
 | |/ /  /_\_   _|/_\ | |/ /  /_\| \| | /_\
 | ' <  / _ \| | / _ \| ' <  / _ \ .` |/ _ \
 |_|\_\/_/ \_\_|/_/ \_\_|\_\/_/ \_\_|\_/_/ \_\
"""

SKILL_PACK = SkillPack(
    id="katakana",
    title="The Script of the World",
    subtitle="Master katakana — the script for loanwords, foreign names, and emphasis",
    save_file_name="katakana_quest",
    intro_story=INTRO_STORY,
    quit_message="Sensei closes the foreign-word dictionary. Your progress is saved -- return anytime.",
    name_prompt="[bold cyan]What is your name, student?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "vowels_kata": "kata_vowel_master",
        "ka_sa_rows": "kata_ka_sa_scholar",
        "ta_na_rows": "kata_ta_na_scholar",
        "ha_ma_rows": "kata_ha_ma_scholar",
        "ya_ra_wa_n": "kata_final_scholar",
        "long_vowels_special": "kata_special_master",
        "reading_loanwords": "loanword_reader",
    },
    achievements={
        "kata_vowel_master":   ("Katakana Vowel Master", "Mastered all five katakana vowels: アイウエオ!"),
        "kata_ka_sa_scholar":  ("Ka-Sa Scholar", "Learned katakana ka-row and sa-row!"),
        "kata_ta_na_scholar":  ("Ta-Na Scholar", "Learned katakana ta-row and na-row!"),
        "kata_ha_ma_scholar":  ("Ha-Ma Scholar", "Learned katakana ha-row and ma-row!"),
        "kata_final_scholar":  ("Final Scholar", "Learned ya-row, ra-row, wa-row, and ン!"),
        "kata_special_master": ("Special Sounds Master", "Mastered long vowels and special katakana sounds!"),
        "loanword_reader":     ("Loanword Reader", "Can read loanwords written in katakana!"),
        "no_hints":            ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":        ("Quick Reader", "Answered a question in under 10 seconds!"),
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
        (26, "Katakana Sage"),
    ],
)
