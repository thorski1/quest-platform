"""
Pinyin skill pack — The Sound of Chinese
Teaches the romanization system for Mandarin: tones, initials, finals, and reading.
Guided by Long Long (龙龙), a friendly dragon.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ ___ _  ___   _____ _  _
 | _ \_ _| \| \ \ / /_ _| \| |
 |  _/| || .` |\ V / | || .` |
 |_| |___|_|\_| |_| |___|_|\_|
"""

SKILL_PACK = SkillPack(
    id="pinyin",
    title="The Sound of Chinese",
    subtitle="Learn to hear, read, and speak every sound in Mandarin",
    save_file_name="pinyin_quest",
    intro_story=INTRO_STORY,
    quit_message="Long Long curls up with the tone chart. Your progress is saved -- come back to practice!",
    name_prompt="[bold cyan]What's your name, learner?[/bold cyan]",
    default_player_name="Student",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "tones": "tone_master",
        "initials": "initial_expert",
        "finals": "finals_scholar",
        "pinyin_reading": "pinyin_reader",
        "common_sounds": "sound_collector",
        "tones_in_context": "tone_shifter",
        "pinyin_typing": "digital_writer",
        "pinyin_vs_english": "sound_detective",
    },
    achievements={
        "tone_master":     ("Tone Master", "Mastered all four tones plus the neutral tone!"),
        "initial_expert":  ("Initial Expert", "Learned every initial consonant in Mandarin!"),
        "finals_scholar":  ("Finals Scholar", "Conquered simple, compound, and nasal finals!"),
        "pinyin_reader":   ("Pinyin Reader", "Can read full pinyin syllables fluently!"),
        "sound_collector": ("Sound Collector", "Practiced the most common sounds in Chinese!"),
        "tone_shifter":    ("Tone Shifter", "Understood tone sandhi and contextual tone changes!"),
        "digital_writer":  ("Digital Writer", "Learned to type pinyin on phone and computer!"),
        "sound_detective": ("Sound Detective", "Spotted every tricky difference between English and Chinese sounds!"),
        "no_hints":        ("Solo Learner", "Completed a zone without any hints!"),
        "speed_reader":    ("Quick Ear", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="medieval",
    level_titles=[
        (1, "Listener"),
        (6, "Speaker"),
        (11, "Reader"),
        (16, "Tone Dancer"),
        (21, "Sound Weaver"),
        (26, "Pinyin Sage"),
    ],
)
