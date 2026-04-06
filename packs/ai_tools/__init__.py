"""
AI Tools skill pack — The AI Toolkit
Teaches AI image generation, writing tools, coding tools, AI search,
audio/video AI, productivity tools, and how to choose the right AI tools.
Guided by ARIA.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
    _   ___   _____ ___   ___  _    ___
   /_\ |_ _| |_   _/ _ \ / _ \| |  / __|
  / _ \ | |    | || (_) | (_) | |__\__ \
 /_/ \_\___|   |_| \___/ \___/|____|___/
"""

SKILL_PACK = SkillPack(
    id="ai_tools",
    title="The AI Toolkit",
    subtitle="◈  The Right Tool for Every Job  ◈",
    save_file_name="ai_tools_quest",
    intro_story=INTRO_STORY,
    quit_message="The workbench powers down gently. Your place is saved — the tools will be here when you return.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Builder",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "ai_image_generation": "pixel_forger",
        "ai_writing_tools": "wordsmith",
        "ai_coding_tools": "code_forger",
        "ai_search": "search_navigator",
        "ai_audio_video": "studio_master",
        "ai_productivity": "efficiency_engineer",
        "choosing_ai_tools": "tool_architect",
    },
    achievements={
        "pixel_forger":       ("Pixel Forger", "Mastered AI image generation — from diffusion to negative prompts!"),
        "wordsmith":          ("Wordsmith", "Explored every AI writing tool — from grammar to brainstorming!"),
        "code_forger":        ("Code Forger", "Understood AI pair programming across every major coding tool!"),
        "search_navigator":   ("Search Navigator", "Navigated AI search — from Perplexity to RAG!"),
        "studio_master":      ("Studio Master", "Explored AI voice, music, and video creation!"),
        "efficiency_engineer": ("Efficiency Engineer", "Automated workflows and mastered AI productivity tools!"),
        "tool_architect":     ("Tool Architect", "Learned to evaluate, choose, and build a personal AI stack!"),
        "no_hints":           ("Solo Builder", "Completed a zone without any hints!"),
        "speed_reader":       ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Browser"),
        (6, "Tinkerer"),
        (11, "Builder"),
        (16, "Integrator"),
        (21, "Architect"),
        (26, "Wizard"),
    ],
)
