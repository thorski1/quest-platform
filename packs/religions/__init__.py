"""
World Religions & Beliefs skill pack — The Book of Many Voices
Teaches world religions, belief systems, and the importance of respect.
For ages 7-10, guided by Puck.

NOTE: This skill pack is respectful, educational, and presents all
religions and belief systems equally. No proselytizing.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 ___  ___ _    ___ ___ ___ ___  _  _ ___
| _ \| __| |  |_ _/ __|_ _/ _ \| \| / __|
|   /| _|| |__ | | (_ || | (_) | .` \__ \
|_|_\|___|____|___\___|___\___/|_|\_|___/
"""

SKILL_PACK = SkillPack(
    id="religions",
    title="The Book of Many Voices",
    subtitle="◈  With Puck's Help, Every Belief Has a Story Worth Hearing  ◈",
    save_file_name="religions_quest",
    intro_story=INTRO_STORY,
    quit_message="The Book of Many Voices closes gently. Your place is saved — every voice will wait for you.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Listener",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "what_is_religion": "foundation_seeker",
        "christianity": "christian_listener",
        "islam": "islamic_listener",
        "judaism": "jewish_listener",
        "hinduism": "hindu_listener",
        "buddhism": "buddhist_listener",
        "other_beliefs": "bridge_builder",
    },
    achievements={
        "foundation_seeker":  ("Foundation Seeker", "Discovered what religion means and why people believe!"),
        "christian_listener": ("Christian Listener", "Heard the story of Jesus, the Bible, and the Golden Rule!"),
        "islamic_listener":   ("Islamic Listener", "Learned about Muhammad, the Quran, and the Five Pillars!"),
        "jewish_listener":    ("Jewish Listener", "Explored the Torah, Shabbat, and 3,500 years of wisdom!"),
        "hindu_listener":     ("Hindu Listener", "Met Brahma, Vishnu, and Shiva, and learned about karma and Diwali!"),
        "buddhist_listener":  ("Buddhist Listener", "Sat with the Buddha and learned about compassion and the quiet mind!"),
        "bridge_builder":     ("Bridge Builder", "Listened to every voice in the Book — and respected them all!"),
        "no_hints":           ("Standing on Your Own", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=True,
    level_titles=[
        (1, "Listener"),
        (6, "Learner"),
        (11, "Scholar"),
        (16, "Bridge Builder"),
        (21, "Peacemaker"),
        (26, "Sage"),
    ],
)
