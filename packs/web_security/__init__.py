"""
Web Security skill pack — Web Security
OWASP Top 10, XSS, SQL Injection, CSRF, and authentication vulnerabilities —
harden the application layer.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
 __      _____ ___   ___ ___ ___ _   _ ___ ___ _______   __
 \ \    / / __| _ ) / __| __/ __| | | | _ \_ _|_   _\ \ / /
  \ \/\/ /| _|| _ \ \__ \ _| (__| |_| |   /| |  | |  \   /
   \_/\_/ |___|___/ |___/___\___|\___/|_|_\___| |_|   |_|
"""

SKILL_PACK = SkillPack(
    id="web_security",
    title="Web Security",
    subtitle="<<  Harden the Application Layer  >>",
    save_file_name="web_security_quest",
    intro_story=INTRO_STORY,
    quit_message="Session tokens rotated. Connection state cached. Jack back in when ready.",
    name_prompt="[bold cyan]Hacker alias:[/bold cyan]",
    default_player_name="Analyst",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "owasp_top_10":     "owasp_sentinel",
        "xss_attacks":      "xss_neutralizer",
        "sql_injection":    "injection_blocker",
        "csrf":             "csrf_defender",
        "auth_vulns":       "auth_architect",
    },
    achievements={
        "owasp_sentinel":    ("OWASP Sentinel",     "Mapped and mitigated the OWASP Top 10 vulnerability classes."),
        "xss_neutralizer":   ("XSS Neutralizer",    "Identified and neutralized reflected, stored, and DOM-based XSS."),
        "injection_blocker": ("Injection Blocker",   "Sealed every SQL injection vector with parameterized queries."),
        "csrf_defender":     ("CSRF Defender",       "Enforced anti-CSRF tokens and SameSite cookie policies."),
        "auth_architect":    ("Auth Architect",      "Hardened session management, OAuth flows, and JWT validation."),
        "no_hints":          ("Stealth Audit",       "Completed a zone without any hints."),
        "speed_reader":      ("Rapid Patch",         "Answered a challenge in under 10 seconds."),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    level_titles=[
        (1,  "Page Viewer"),
        (6,  "Form Tester"),
        (11, "Bug Hunter"),
        (16, "Pen Tester"),
        (21, "AppSec Lead"),
        (26, "Web Fortress Architect"),
    ],
)
