"""
Dinosaurs & Prehistoric Life skill pack — The Time Machine
Teaches dinosaurs, fossils, extinction, prehistoric sea/sky creatures, and evolution basics.
For ages 7-10, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___  _  _  _  _  ___  ___   _   _   _  ___  ___
 |   \| || \| |/ _ \/ __| /_\ | | | | | _ \/ __|
 | |) | || .` | (_) \__ \/ _ \| |_| | |   /\__ \
 |___/|_||_|\_|\___/|___/_/ \_\___/  |_|_\\|___/
"""

SKILL_PACK = SkillPack(
    id="dinosaurs",
    title="The Time Machine",
    subtitle="◈  With Puck's Help, Travel Back to Meet the Dinosaurs  ◈",
    save_file_name="dinosaurs_quest",
    intro_story=INTRO_STORY,
    quit_message="The Time Machine powers down gently. Your place is saved — the dinosaurs will wait for you!",
    name_prompt="[bold cyan]What's your name, Time Traveler?[/bold cyan]",
    default_player_name="Explorer",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "what_are_dinosaurs": "mesozoic_scholar",
        "famous_dinosaurs": "dino_spotter",
        "herbivores_vs_carnivores": "food_chain_master",
        "fossils": "fossil_finder",
        "flying_and_swimming": "sky_sea_explorer",
        "extinction": "extinction_expert",
        "after_dinosaurs": "time_traveler",
    },
    achievements={
        "mesozoic_scholar":   ("Mesozoic Scholar", "Learned when dinosaurs lived and what made them special!"),
        "dino_spotter":       ("Dino Spotter", "Met the most famous dinosaurs and learned their secrets!"),
        "food_chain_master":  ("Food Chain Master", "Understood the difference between herbivores and carnivores!"),
        "fossil_finder":      ("Fossil Finder", "Discovered how fossils form and how paleontologists study them!"),
        "sky_sea_explorer":   ("Sky & Sea Explorer", "Met the amazing pterosaurs, plesiosaurs, and other prehistoric reptiles!"),
        "extinction_expert":  ("Extinction Expert", "Learned the truth about the asteroid and which animals survived!"),
        "time_traveler":      ("Time Traveler", "Journeyed from the Ice Age to early humans — the whole story of life!"),
        "no_hints":           ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Fossil Hunter"),
        (6, "Digger"),
        (11, "Paleontologist"),
        (16, "Time Traveler"),
        (21, "Dino Expert"),
        (26, "Professor"),
    ],
)
