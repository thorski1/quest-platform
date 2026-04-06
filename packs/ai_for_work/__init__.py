"""
AI for Work skill pack — AI at Work: Your AI Co-Pilot for Everything Professional
Teaches practical AI applications across writing, research, presentations,
data analysis, meetings, strategy, and workflow automation.
Guided by ARIA.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
    _   ___    _  _     __      __       _
   /_\ |_ _|  | || |    \ \    / /__ _ _| |__
  / _ \ | |   |___ |     \ \/\/ / _ \ '_| / /
 /_/ \_\___|  |_||_|      \_/\_/\___/_| |_\_\
"""

SKILL_PACK = SkillPack(
    id="ai_for_work",
    title="AI at Work",
    subtitle="◈  Your AI Co-Pilot for Everything Professional  ◈",
    save_file_name="ai_for_work_quest",
    intro_story=INTRO_STORY,
    quit_message="The command center dims gently. Your progress is saved — your AI co-pilot will be here when you return.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Professional",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "ai_for_writing": "writing_master",
        "ai_for_research": "research_ace",
        "ai_for_presentations": "presentation_pro",
        "ai_for_data": "data_wizard",
        "ai_for_meetings": "meeting_transformer",
        "ai_for_strategy": "strategy_architect",
        "ai_workflow_automation": "automation_engineer",
    },
    achievements={
        "writing_master":        ("Writing Master", "Mastered AI-assisted drafting, editing, and tone for every professional context!"),
        "research_ace":          ("Research Ace", "Leveraged AI for summarization, fact-checking, and rigorous competitive analysis!"),
        "presentation_pro":      ("Presentation Pro", "Built compelling decks with AI-powered structure, talking points, and audience adaptation!"),
        "data_wizard":           ("Data Wizard", "Unlocked AI-driven formulas, analysis, visualization, and dashboard design!"),
        "meeting_transformer":   ("Meeting Transformer", "Turned meetings into action with AI transcription, follow-ups, and decision logs!"),
        "strategy_architect":    ("Strategy Architect", "Applied AI to brainstorming, SWOT, scenario planning, and decision frameworks!"),
        "automation_engineer":   ("Automation Engineer", "Built AI-powered workflows that connect tools and eliminate recurring busywork!"),
        "no_hints":              ("Self-Sufficient", "Completed a zone without using any hints!"),
        "speed_reader":          ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Intern"),
        (6, "Associate"),
        (11, "Specialist"),
        (16, "Director"),
        (21, "VP"),
        (26, "Chief AI Officer"),
    ],
)
