"""
Letters skill pack — The Letter Garden
Teaches phonics, vowels, blends, words, and simple sentences.
For a 7-year-old learning to read.
"""

from engine.skill_pack import SkillPack
from .story import (
    INTRO_STORY,
    ZONE_INTROS,
    ZONE_COMPLETIONS,
    BOSS_INTROS,
)
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___     _  _     ___   __  __  ___ ___
 | _ \_ _(_)| |___ | _ \ \ \/ / |_ _|   \
 |  _/ '_| || / -_)|   /  >  <   | || |) |
 |_| |_| |_||_\___||_|_\ /_/\_\ |___|___/
"""

SKILL_PACK = SkillPack(
    id="letters",
    title="The Letter Garden",
    subtitle="◈  With Puck's Help, Every Word Unlocks a World  ◈",
    save_file_name="letters_quest",
    intro_story=INTRO_STORY,
    quit_message="The book closes gently. Your place is saved. Come back soon!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "letter_garden": "alphabet_keeper",
        "vowel_pond": "vowel_voice",
        "blend_bridge": "sound_weaver",
        "word_workshop": "word_builder",
        "sentence_city": "story_reader",
        "rhyming_river": "rhyme_swimmer",
        "sight_word_station": "sight_word_star",
        "reading_full_sentences": "true_reader",
        "word_building": "word_crafter",
        "story_time": "story_keeper",
        "punctuation_plaza": "punctuation_pro",
    },
    achievements={
        "alphabet_keeper": ("Alphabet Keeper", "Learned every letter in the garden!"),
        "vowel_voice": ("Vowel Voice", "Mastered the five special vowels!"),
        "sound_weaver": ("Sound Weaver", "Crossed the Blend Bridge without falling!"),
        "word_builder": ("Word Builder", "Built real words in the workshop!"),
        "story_reader": ("Story Reader", "Read full sentences in Sentence City!"),
        "rhyme_swimmer": ("Rhyme Swimmer", "Rode the rhyming river all the way down!"),
        "sight_word_star": ("Sight Word Star", "Learned the magic words every reader knows!"),
        "true_reader": ("True Reader", "Read full sentences and understood every one!"),
        "word_crafter": ("Word Crafter", "Snapped letters together to build real words!"),
        "story_keeper": ("Story Keeper", "Read stories and understood every one!"),
        "punctuation_pro": ("Punctuation Pro", "Mastered the marks that give writing its voice!"),
        "no_hints": ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader": ("Speed Reader", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Seedling"),
        (6, "Sprout"),
        (11, "Bloom"),
        (16, "Star"),
        (21, "Wonder"),
        (26, "Sage"),
    ],
)
