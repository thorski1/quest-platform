"""
Reading skill pack — The Reading Room
Teaches context clues, predictions, story elements, main idea & details,
fact vs opinion, genres, book parts, and library skills.
For ages 5-12, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ____                 _  _
|  _ \  ___  __ _  __| |(_) _ __    __ _
| |_) |/ _ \/ _` |/ _` || || '_ \  / _` |
|  _ <|  __/ (_| | (_| || || | | || (_| |
|_| \_\\___|\__,_|\__,_||_||_| |_| \__, |
                                    |___/
"""

SKILL_PACK = SkillPack(
    id="reading",
    title="The Reading Room",
    subtitle="◈  With Puck's Help, Every Book Is a Door  ◈",
    save_file_name="reading_quest",
    intro_story=INTRO_STORY,
    quit_message="The Reading Room door closes gently. Your place is saved — the books will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Page Turner",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "reading_clues": "clue_cracker",
        "story_elements": "story_builder",
        "main_idea_details": "idea_finder",
        "fact_vs_opinion": "truth_teller",
        "reading_for_fun": "reading_champion",
    },
    achievements={
        "clue_cracker":     ("Clue Cracker", "Decoded every mystery word using context clues and predictions!"),
        "story_builder":    ("Story Builder", "Mastered characters, settings, plots, and story structure!"),
        "idea_finder":      ("Idea Finder", "Found the main idea and supporting details in every passage!"),
        "truth_teller":     ("Truth Teller", "Separated facts from opinions like a pro!"),
        "reading_champion": ("Reading Champion", "Explored every genre and mastered all book and library skills!"),
        "no_hints":         ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":     ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Page Turner"),
        (6, "Bookworm"),
        (11, "Story Spotter"),
        (16, "Idea Finder"),
        (21, "Truth Teller"),
        (26, "Reading Champion"),
    ],
)
