"""
Cyber Basics skill pack — Cyber Fundamentals
The foundation of cybersecurity: CIA triad, threat landscape, social engineering,
password security, and network basics.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
   ___ _   _ ___ ___ ___   ___ _   _ _  _ ___   _   __  __ ___ _  _ _____  _   _    ___
  / __| \ | | _ ) __| _ \ | __| | | | \| |   \ /_\ |  \/  | __| \| |_   _|/ \ | |  / __|
 | (__| |\ | _ \ _||   / | _|| |_| | .` | |) / _ \| |\/| | _|| .` | | | / _ \| |__\__ \
  \___|_| \_|___/___|_|_\ |_|  \___/|_|\_|___/_/ \_\_|  |_|___|_|\_| |_|/_/ \_\____|___/
"""

SKILL_PACK = SkillPack(
    id="cyber_basics",
    title="Cyber Fundamentals",
    subtitle="<<  Jack In. Learn the Grid.  >>",
    save_file_name="cyber_basics_quest",
    intro_story=INTRO_STORY,
    quit_message="Connection hibernated. Neural state cached. Jack back in when ready.",
    name_prompt="[bold cyan]Hacker alias:[/bold cyan]",
    default_player_name="Recruit",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "cia_triad":          "triad_initiate",
        "common_threats":     "threat_mapper",
        "social_engineering": "mind_shield",
        "password_security":  "key_forger",
        "network_basics":     "grid_runner",
    },
    achievements={
        "triad_initiate":  ("Triad Initiate",  "Internalized Confidentiality, Integrity, and Availability."),
        "threat_mapper":   ("Threat Mapper",    "Cataloged malware, ransomware, phishing, and zero-days."),
        "mind_shield":     ("Mind Shield",      "Detected pretexting, baiting, tailgating, and phishing lures."),
        "key_forger":      ("Key Forger",       "Mastered hashing, salting, MFA, and passphrase entropy."),
        "grid_runner":     ("Grid Runner",      "Navigated TCP/IP, DNS, firewalls, and packet analysis."),
        "no_hints":        ("Ghost Protocol",   "Completed a zone without any hints."),
        "speed_reader":    ("Reflex Hack",      "Answered a challenge in under 10 seconds."),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Script Kiddie"),
        (6,  "Byte Runner"),
        (11, "Net Diver"),
        (16, "Cipher Punk"),
        (21, "Grid Architect"),
        (26, "Zero-Day Hunter"),
    ],
)
