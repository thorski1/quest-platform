"""
history skill pack — The Time Traveler's Primer
Teaches world history, great explorers, inventors, wars, and leaders who changed the world.
For ages 8-11.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _   _ ___ ____ _____ ___  ______   __
 | | | |_ _/ ___|_   _/ _ \|  _ \ \ / /
 | |_| || |\___ \ | || | | | |_) \ V /
 |  _  || | ___) || || |_| |  _ < | |
 |_| |_|___|____/ |_| \___/|_| \_\|_|
"""

SKILL_PACK = SkillPack(
    id="history",
    title="The Time Traveler's Primer",
    subtitle="◈  With Puck's Help, the Past Comes Alive  ◈",
    save_file_name="history_quest",
    intro_story=INTRO_STORY,
    quit_message="The history book closes gently. Your place is saved — the past will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "ancient_civilizations":    "civilization_keeper",
        "explorers_and_discoveries": "voyage_maker",
        "inventions_and_inventors": "inventor_mind",
        "world_wars":               "peace_keeper",
        "american_history":         "freedom_scholar",
        "world_leaders_and_change": "courage_keeper",
        "ancient_wonders":          "wonder_seeker",
        "indigenous_peoples":       "first_peoples_scholar",
        "science_history":          "science_historian",
        "rights_and_revolutions":  "rights_champion",
        "women_in_history":        "hidden_no_more",
    },
    achievements={
        "civilization_keeper":    ("Civilization Keeper", "Traveled through Egypt, Greece, Rome, and Mesopotamia!"),
        "voyage_maker":           ("Voyage Maker", "Followed the greatest explorers across the globe!"),
        "inventor_mind":          ("Inventor Mind", "Remembered every invention that changed the world!"),
        "peace_keeper":           ("Peace Keeper", "Studied the World Wars and understood why peace matters!"),
        "freedom_scholar":        ("Freedom Scholar", "Learned American history from 1776 to the Civil Rights Movement!"),
        "courage_keeper":         ("Courage Keeper", "Honored the leaders who changed the world through courage!"),
        "wonder_seeker":          ("Wonder Seeker", "Explored the Seven Wonders and the greatest ancient structures!"),
        "first_peoples_scholar":  ("First Peoples Scholar", "Honored the Indigenous peoples of every continent!"),
        "science_historian":      ("Science Historian", "Remembered Newton, Curie, Einstein, and the hidden figures!"),
        "rights_champion":        ("Rights Champion", "Learned how ordinary people changed the world through courage!"),
        "hidden_no_more":         ("Hidden No More", "Honored the women who changed history but were often left out of it!"),
        "no_hints":               ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":           ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1,  "Seedling"),
        (6,  "Sprout"),
        (11, "Bloom"),
        (16, "Star"),
        (21, "Wonder"),
        (26, "Sage"),
    ],
)
