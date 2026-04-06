"""
Writing skill pack — The Writer's Workshop
Teaches sentences & capitalization, punctuation, parts of a story,
descriptive writing, and writing for a purpose.
For ages 5-12, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 __        __    _  _    _
 \ \      / / __(_)| |_ (_) _ __    __ _
  \ \ /\ / / / _` || __|| || '_ \  / _` |
   \ V  V / | |  | || |_ | || | | || (_| |
    \_/\_/   \__|_| \__||_||_| |_| \__, |
                                    |___/
"""

SKILL_PACK = SkillPack(
    id="writing",
    title="The Writer's Workshop",
    subtitle="◈  With Puck's Help, Every Word Has Power  ◈",
    save_file_name="writing_quest",
    intro_story=INTRO_STORY,
    quit_message="The Workshop door closes gently. Your place is saved — the quills will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Word Weaver",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "sentences_capitalization": "sentence_architect",
        "punctuation_power": "punctuation_master",
        "parts_of_story": "story_architect",
        "descriptive_writing": "word_painter",
        "writing_for_purpose": "purpose_writer",
    },
    achievements={
        "sentence_architect":  ("Sentence Architect", "Built perfect sentences with subjects, verbs, and capital letters!"),
        "punctuation_master":  ("Punctuation Master", "Mastered periods, commas, question marks, and exclamation points!"),
        "story_architect":     ("Story Architect", "Understood beginnings, middles, ends, characters, settings, and problems!"),
        "word_painter":        ("Word Painter", "Painted vivid pictures with adjectives, similes, and sensory details!"),
        "purpose_writer":      ("Purpose Writer", "Wrote letters, lists, instructions, and invitations for the real world!"),
        "no_hints":            ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_writer":        ("Quick Quill", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Word Weaver"),
        (6, "Sentence Builder"),
        (11, "Punctuation Pro"),
        (16, "Story Architect"),
        (21, "Word Painter"),
        (26, "Writing Champion"),
    ],
)
