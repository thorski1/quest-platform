"""
Hangul skill pack -- The Hangul Gateway
Teaches the Korean alphabet: vowels, consonants, syllable blocks, and reading.
Guided by a mysterious alien linguist decoding Earth's most scientific writing system.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _  _   _   _  _  ___ _   _ _
 | || | /_\ | \| |/ __| | | | |
 | __ |/ _ \| .` | (_ | |_| | |__
 |_||_/_/ \_\_|\_|\___|\___/|____|
"""

SKILL_PACK = SkillPack(
    id="hangul",
    title="The Hangul Gateway",
    subtitle="Master the Korean alphabet -- the most scientific writing system on Earth",
    save_file_name="hangul_quest",
    intro_story=INTRO_STORY,
    quit_message="The alien linguist nods. Your progress is saved -- return to continue decoding Hangul.",
    name_prompt="[bold cyan]What is your name, traveler?[/bold cyan]",
    default_player_name="Traveler",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "basic_vowels": "vowel_decoder",
        "basic_consonants": "consonant_decoder",
        "syllable_blocks": "block_builder",
        "double_consonants": "double_master",
        "reading_practice": "hangul_reader",
    },
    achievements={
        "vowel_decoder":    ("Vowel Decoder", "Mastered the 10 basic Korean vowels!"),
        "consonant_decoder": ("Consonant Decoder", "Mastered the 14 basic Korean consonants!"),
        "block_builder":    ("Block Builder", "Understands how Korean syllable blocks work!"),
        "double_master":    ("Double Master", "Conquered the tricky double consonants!"),
        "hangul_reader":    ("Hangul Reader", "Can read basic Korean words in Hangul!"),
        "no_hints":         ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":     ("Quick Decoder", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="alien",
    level_titles=[
        (1, "Signal Receiver"),
        (6, "Pattern Spotter"),
        (11, "Symbol Reader"),
        (16, "Script Decoder"),
        (21, "Hangul Navigator"),
        (26, "Alphabet Master"),
    ],
)
