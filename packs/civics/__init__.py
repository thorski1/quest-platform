"""
Civics skill pack — The Citizen's Handbook
Teaches community helpers, rules and laws, government, maps,
holidays, rights and responsibilities, and world cultures.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ ___ ___ ___ ___ ___
 / __||_ _|| _ \/ __||_ _|/ __|
| (__ | | |   /\__ \ | | \__ \
 \___||___||_|_\|___/|___||___/
"""

SKILL_PACK = SkillPack(
    id="civics",
    title="The Citizen's Handbook",
    subtitle="◈  With Puck's Help, You Learn How the World Works Together  ◈",
    save_file_name="civics_quest",
    intro_story=INTRO_STORY,
    quit_message="The Handbook closes gently. Your place is saved — the world will wait for you!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Citizen",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "community_helpers": "community_champion",
        "rules_and_laws": "rule_keeper",
        "government_basics": "democracy_scholar",
        "maps_and_globes": "map_navigator",
        "holidays_traditions": "tradition_keeper",
        "rights_responsibilities": "citizen_hero",
        "world_cultures": "culture_explorer",
    },
    achievements={
        "community_champion":  ("Community Champion", "Learned about all the helpers who keep our neighborhoods safe and strong!"),
        "rule_keeper":         ("Rule Keeper", "Understood why rules and laws keep the world fair and safe!"),
        "democracy_scholar":   ("Democracy Scholar", "Learned how government works and why every vote counts!"),
        "map_navigator":       ("Map Navigator", "Read maps, found continents, and located capital cities!"),
        "tradition_keeper":    ("Tradition Keeper", "Explored holidays and traditions from around the world!"),
        "citizen_hero":        ("Citizen Hero", "Understood what rights and responsibilities mean for everyone!"),
        "culture_explorer":    ("Culture Explorer", "Explored languages, foods, and celebrations from every corner of the globe!"),
        "no_hints":            ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":        ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Citizen"),
        (6, "Helper"),
        (11, "Leader"),
        (16, "Ambassador"),
        (21, "Senator"),
        (26, "President"),
    ],
)
