"""
Family & Home skill pack — Family Members, Polite vs Casual Terms,
Rooms in the House, Daily Routines, and Describing Your Family.
Teaches essential vocabulary for Japanese family life and home.
Guided by Umi (海) — a calm ocean guide.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___  _   __  __ ___ _  __   __   ___   _  _  ___  __  __ ___
| __|/ \ |  \/  |_ _| | \ \ / /  / / | | |/ _ \|  \/  | __|
| _/| o || |\/| || || |__\ V /  / /| |_| | (_) | |\/| | _|
|_| |_n_||_|  |_|___|____|_|  /_/  \___/ \___/|_|  |_|___|
"""

SKILL_PACK = SkillPack(
    id="family_jp",
    title="Family & Home",
    subtitle="Master family members, polite forms, home vocabulary, daily routines, and family descriptions",
    save_file_name="family_jp_quest",
    intro_story=INTRO_STORY,
    quit_message="Umi waves from the doorway. Your progress is saved -- return to continue your family adventure.",
    name_prompt="[bold cyan]What is your name, family explorer?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "family_members": "family_expert",
        "polite_casual_family": "politeness_master",
        "rooms_in_house": "home_navigator",
        "daily_routines": "routine_pro",
        "describing_family": "family_storyteller",
    },
    achievements={
        "family_expert":      ("Family Expert", "Knows every family member from grandparents to siblings!"),
        "politeness_master":  ("Politeness Master", "Navigates humble and polite family terms with ease!"),
        "home_navigator":     ("Home Navigator", "Can name every room in a Japanese house!"),
        "routine_pro":        ("Routine Pro", "Masters the daily rhythm of Japanese home life!"),
        "family_storyteller": ("Family Storyteller", "Can describe their entire family in natural Japanese!"),
        "no_hints":           ("Self-Reliant", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="ocean",
    level_titles=[
        (1, "Newcomer"),
        (6, "Family Friend"),
        (11, "Household Member"),
        (16, "Home Keeper"),
        (21, "Family Elder"),
        (26, "Family Master"),
    ],
)
