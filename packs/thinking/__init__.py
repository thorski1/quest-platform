"""
Critical Thinking & Logic skill pack — The Puzzle Palace
Teaches patterns, sorting, cause & effect, fact vs opinion,
problem solving, analogies, and brain teasers.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___  _   _  ___  ___  _     ___
| _ \| | | ||_  ||_  || |   | __|
|  _/| |_| | / /  / / | |__ | _|
|_|   \___/ /___\/___\|____||___|
 ___  _   _     _    ___  ___
| _ \/_\ | |   /_\  / __|| __|
|  _/ _ \| |__/ _ \| (__ | _|
|_|/_/ \_\____/_/ \_\\___||___|
"""

SKILL_PACK = SkillPack(
    id="thinking",
    title="The Puzzle Palace",
    subtitle="◈  With Puck's Help, Your Brain Becomes a Superpower  ◈",
    save_file_name="thinking_quest",
    intro_story=INTRO_STORY,
    quit_message="The Puzzle Palace doors close softly. Your place is saved — the riddles will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Thinker",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "patterns": "pattern_spotter",
        "sorting_grouping": "master_sorter",
        "cause_and_effect": "chain_thinker",
        "fact_vs_opinion": "truth_seeker",
        "problem_solving": "problem_cracker",
        "analogies": "connection_finder",
        "brain_teasers": "riddle_master",
    },
    achievements={
        "pattern_spotter":   ("Pattern Spotter", "Cracked every sequence in the Pattern Garden!"),
        "master_sorter":     ("Master Sorter", "Sorted every object and mastered the Venn diagram!"),
        "chain_thinker":     ("Chain Thinker", "Followed every chain of cause and effect to its source!"),
        "truth_seeker":      ("Truth Seeker", "Separated every fact from every opinion without being fooled!"),
        "problem_cracker":   ("Problem Cracker", "Broke down every problem and solved it step by step!"),
        "connection_finder": ("Connection Finder", "Found the hidden link in every analogy!"),
        "riddle_master":     ("Riddle Master", "Cracked every riddle, puzzle, and brain teaser in the Vault!"),
        "no_hints":          ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Thinker"),
        (6, "Puzzler"),
        (11, "Detective"),
        (16, "Strategist"),
        (21, "Genius"),
        (26, "Mastermind"),
    ],
)
