"""
Emotions & Mindfulness skill pack — The Heart Room
Teaches naming feelings, coping with big emotions, empathy, mindful breathing,
gratitude, friendship skills, and self-confidence.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___  __  __  ___  _____  ___  ___  _  _  ___
| __||  \/  |/ _ \|_   _||_ _|/ _ \| \| |/ __|
| _| | |\/| | (_) | | |   | || (_) | .` |\__ \
|___||_|  |_|\___/  |_|  |___|\___/|_|\_||___/
"""

SKILL_PACK = SkillPack(
    id="emotions",
    title="The Heart Room",
    subtitle="◈  With Puck's Help, Feelings Become Your Superpower  ◈",
    save_file_name="emotions_quest",
    intro_story=INTRO_STORY,
    quit_message="The Heart Room dims gently. Your place is saved — your feelings will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Feeler",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "naming_feelings": "feeling_finder",
        "big_emotions": "storm_weatherer",
        "empathy": "empathy_reader",
        "mindful_breathing": "breath_keeper",
        "gratitude": "gratitude_grower",
        "friendship_skills": "bridge_builder",
        "self_confidence": "mirror_master",
    },
    achievements={
        "feeling_finder":   ("Feeling Finder", "Named and identified all six core emotions!"),
        "storm_weatherer":  ("Storm Weatherer", "Learned what to do when feelings get really big!"),
        "empathy_reader":   ("Empathy Reader", "Learned to understand how others feel through faces and body language!"),
        "breath_keeper":    ("Breath Keeper", "Mastered breathing and mindfulness techniques!"),
        "gratitude_grower": ("Gratitude Grower", "Learned to notice and appreciate the good things in life!"),
        "bridge_builder":   ("Bridge Builder", "Mastered sharing, conflict resolution, and true friendship!"),
        "mirror_master":    ("Mirror Master", "Discovered positive self-talk, growth mindset, and inner strength!"),
        "no_hints":         ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":     ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Feeler"),
        (6, "Empath"),
        (11, "Listener"),
        (16, "Healer"),
        (21, "Sage"),
        (26, "Heart Master"),
    ],
)
