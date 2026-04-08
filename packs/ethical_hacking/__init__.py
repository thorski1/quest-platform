"""
Ethical Hacking skill pack — Ethical Hacking
Reconnaissance, scanning, exploitation, post-exploitation, and reporting —
learn to think like an attacker to defend like an architect.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ _____ _  _ ___ ___   _   _      _  _   _   ___ _  _____ _  _  ___
 | __|_   _| || |_ _/ __| /_\ | |    | || | /_\ / __| |/ /_ _| \| |/ __|
 | _|  | | | __ || | (__ / _ \| |__  | __ |/ _ \ (__| ' < | || .` | (_ |
 |___| |_| |_||_|___\___/_/ \_\____| |_||_/_/ \_\___|_|\_\___|_|\_|\___|
"""

SKILL_PACK = SkillPack(
    id="ethical_hacking",
    title="Ethical Hacking",
    subtitle="<<  Think Like an Attacker. Defend Like an Architect.  >>",
    save_file_name="ethical_hacking_quest",
    intro_story=INTRO_STORY,
    quit_message="Exploit toolkit secured. Session state encrypted. Resume your operation when ready.",
    name_prompt="[bold cyan]Operator callsign:[/bold cyan]",
    default_player_name="Operator",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "reconnaissance":       "recon_ghost",
        "scanning_enumeration": "port_mapper",
        "exploitation_basics":  "exploit_crafter",
        "post_exploitation":    "shadow_walker",
        "reporting_ethics":     "white_hat",
    },
    achievements={
        "recon_ghost":      ("Recon Ghost",      "Mapped targets with OSINT, DNS, WHOIS, and passive reconnaissance."),
        "port_mapper":      ("Port Mapper",       "Scanned networks, enumerated services, and fingerprinted systems."),
        "exploit_crafter":  ("Exploit Crafter",   "Understood vulnerability exploitation, payloads, and privilege escalation."),
        "shadow_walker":    ("Shadow Walker",     "Maintained persistence, pivoted through networks, and exfiltrated data."),
        "white_hat":        ("White Hat",         "Documented findings professionally and upheld ethical hacking principles."),
        "no_hints":         ("Silent Op",         "Completed a zone without any hints."),
        "speed_reader":     ("Quick Draw",        "Answered a challenge in under 10 seconds."),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Trainee"),
        (6,  "Recon Specialist"),
        (11, "Exploit Developer"),
        (16, "Penetration Tester"),
        (21, "Red Team Lead"),
        (26, "Offensive Security Architect"),
    ],
)
