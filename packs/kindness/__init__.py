"""
Kindness skill pack — The Art of Being Kind
Teaches feelings, kindness, friendship, and solving problems.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _  ___ _  _ ___  _  _ ___ ___ ___
 | |/ __| \| |   \| \| | __/ __/ __|
 | | (__| .` | |) | .` | _|\__ \__ \
 |_|\___|_|\_|___/|_|\_|___|___/___/
"""

SKILL_PACK = SkillPack(
    id="kindness",
    title="The Art of Being Kind",
    subtitle="◈  With Puck's Help, Learn the Most Important Skill of All  ◈",
    save_file_name="kindness_quest",
    intro_story=INTRO_STORY,
    quit_message="The garden rests gently. Come back whenever you're ready.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "feelings_garden": "feeling_finder",
        "kindness_actions": "kind_actor",
        "being_a_good_friend": "true_friend",
        "solving_problems": "problem_solver",
        "listening_skills": "deep_listener",
        "helping_community": "community_helper",
        "handling_hard_feelings": "feelings_champion",
        "friendship_bridge": "bridge_builder",
        "gratitude_practice": "gratitude_keeper",
        "respecting_differences": "difference_celebrator",
        "digital_kindness": "digital_guardian",
    },
    achievements={
        "feeling_finder": ("Feeling Finder", "Named and understood every emotion!"),
        "kind_actor": ("Kind Actor", "Chose kindness in every situation!"),
        "true_friend": ("True Friend", "Learned what good friendship really means!"),
        "problem_solver": ("Problem Solver", "Handled hard moments with grace!"),
        "deep_listener": ("Deep Listener", "Discovered the superpower of truly listening!"),
        "community_helper": ("Community Helper", "Learned how to take care of each other!"),
        "feelings_champion": ("Feelings Champion", "Handled the biggest feelings with courage and kindness!"),
        "bridge_builder": ("Bridge Builder", "Learned the deepest skills of true friendship!"),
        "gratitude_keeper": ("Gratitude Keeper", "Discovered the power of a thankful heart!"),
        "difference_celebrator": ("Difference Celebrator", "Learned to see every person's uniqueness as a gift!"),
        "digital_guardian": ("Digital Guardian", "Mastered kindness and safety in the online world!"),
        "no_hints": ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader": ("Quick Thinker", "Answered a question in under 10 seconds!"),
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
