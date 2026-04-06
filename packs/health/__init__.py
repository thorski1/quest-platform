"""
Health skill pack — The Healthy Hero
Teaches germs & handwashing, healthy eating, exercise & sleep,
going to the doctor, and mental health. For ages 5-12, guided by Puck.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 _  _ ___   _   _  _____ _  _
| || | __| /_\ | ||_   _| || |
| __ | _| / _ \| |_ | | | __ |
|_||_|___/_/ \_\___||_| |_||_|
"""

SKILL_PACK = SkillPack(
    id="health",
    title="The Healthy Hero",
    subtitle="◈  With Puck's Help, Become a Champion of Wellness  ◈",
    save_file_name="health_quest",
    intro_story=INTRO_STORY,
    quit_message="The health map folds gently closed. Your place is saved — keep taking care of yourself while you rest!",
    name_prompt="[bold cyan]What's your name, hero?[/bold cyan]",
    default_player_name="Hero",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "germs_and_handwashing": "germ_buster",
        "healthy_eating": "fuel_master",
        "exercise_and_sleep": "energy_champion",
        "going_to_the_doctor": "healers_friend",
        "mental_health": "feelings_guardian",
    },
    achievements={
        "germ_buster":      ("Germ Buster", "Defeated every germ and mastered the art of handwashing!"),
        "fuel_master":       ("Fuel Master", "Learned the food groups, vitamins, and the power of water!"),
        "energy_champion":   ("Energy Champion", "Discovered the secrets of exercise, sleep, and endless energy!"),
        "healers_friend":    ("Healer's Friend", "Conquered check-ups, vaccines, and the dentist's chair!"),
        "feelings_guardian":  ("Feelings Guardian", "Explored every feeling and learned the courage to ask for help!"),
        "no_hints":          ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Seedling"),
        (6, "Helper"),
        (11, "Guardian"),
        (16, "Champion"),
        (21, "Hero"),
        (26, "Legend"),
    ],
)
