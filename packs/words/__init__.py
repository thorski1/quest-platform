"""
Words & Language skill pack — The Word Workshop
Teaches compound words, synonyms, prefixes, homophones, parts of speech,
figurative language, vocabulary building, and storytelling.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 __      __                 _
 \ \    / /  ___   _ _   __| |  ___
  \ \/\/ /  / _ \ | '_| / _` | (_-<
   \_/\_/   \___/ |_|   \__,_| /__/
"""

SKILL_PACK = SkillPack(
    id="words",
    title="The Word Workshop",
    subtitle="◈  With Puck's Help, Words Come Alive  ◈",
    save_file_name="words_quest",
    intro_story=INTRO_STORY,
    quit_message="The Workshop door closes gently. Your place is saved — the words will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Scribbler",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "compound_words": "compound_crafter",
        "synonyms_antonyms": "synonym_seeker",
        "prefixes_suffixes": "affix_architect",
        "homophones": "homophone_hunter",
        "parts_of_speech": "grammar_guardian",
        "figurative_language": "imagination_igniter",
        "vocabulary_building": "vault_keeper",
        "storytelling": "master_storyteller",
    },
    achievements={
        "compound_crafter":    ("Compound Crafter", "Joined words together like a master builder!"),
        "synonym_seeker":      ("Synonym Seeker", "Found twins and opposites across the whole language!"),
        "affix_architect":     ("Affix Architect", "Mastered prefixes and suffixes — the building blocks of words!"),
        "homophone_hunter":    ("Homophone Hunter", "Tamed every sound-alike trickster in the English language!"),
        "grammar_guardian":    ("Grammar Guardian", "Named every part of speech and put every word in its place!"),
        "imagination_igniter": ("Imagination Igniter", "Wielded similes, metaphors, alliteration, and onomatopoeia like magic!"),
        "vault_keeper":        ("Vault Keeper", "Unlocked the Word Vault with context clues, dictionaries, and ancient roots!"),
        "master_storyteller":  ("Master Storyteller", "Forged a story with characters, setting, plot, and heart!"),
        "no_hints":            ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":        ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Scribbler"),
        (6, "Speller"),
        (11, "Wordsmith"),
        (16, "Poet"),
        (21, "Author"),
        (26, "Bard"),
    ],
)
