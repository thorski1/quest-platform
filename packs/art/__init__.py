"""
Art skill pack — The Art Studio
Colors, shapes, famous artwork, art elements, and artists.
For ages 7-11, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  _   ___  _____   ___ _____ _   _ ___  ___ ___
 /_\ | _ \|_   _| / __|_   _| | | |   \|_ _/ _ \
/ _ \|   /  | |   \__ \ | | | |_| | |) || | (_) |
/_/ \_\_|_\  |_|   |___/ |_|  \___/|___/___\___/
"""

SKILL_PACK = SkillPack(
    id="art",
    title="The Art Studio",
    subtitle="◈  Colors, Shapes, and the Stories That Art Tells  ◈",
    save_file_name="art_quest",
    intro_story=INTRO_STORY,
    quit_message="The studio will be here when you return. Puck is keeping your easel ready!",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Artist",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "colors_and_mixing": "color_mixer",
        "shapes_and_patterns": "pattern_maker",
        "art_tools": "studio_ready",
        "famous_artwork": "gallery_guide",
        "art_elements": "critical_eye",
        "famous_artists": "art_historian",
        "art_styles_through_history": "time_traveler_artist",
        "music_and_rhythm": "rhythm_keeper",
        "photography_and_film": "lens_master",
        "dance_and_theater": "stage_star",
        "architecture_and_design": "master_builder",
    },
    achievements={
        "color_mixer": ("Color Mixer", "Mastered primary colors, secondary colors, and color mixing!"),
        "pattern_maker": ("Pattern Maker", "Discovered shapes, symmetry, and tessellations!"),
        "studio_ready": ("Studio Ready", "Learned the tools and materials of the artist's craft!"),
        "gallery_guide": ("Gallery Guide", "Can name and describe the world's most famous artworks!"),
        "critical_eye": ("Critical Eye", "Identified the elements of art in any painting!"),
        "art_historian": ("Art Historian", "Knows the stories behind history's greatest artists!"),
        "time_traveler_artist": ("Time Traveler", "Journeyed from cave paintings to modern street art!"),
        "rhythm_keeper": ("Rhythm Keeper", "Discovered music, notes, instruments, and legendary composers!"),
        "lens_master": ("Lens Master", "Explored photography, pixels, film, and the art of the camera!"),
        "stage_star": ("Stage Star", "Explored dance, theater, and the performing arts!"),
        "master_builder": ("Master Builder", "Discovered architecture, design, and the art of building!"),
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
