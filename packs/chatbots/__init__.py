"""
Chatbots skill pack — The Chatbot Field Guide
Know your AI assistants inside and out: ChatGPT, Claude, Gemini, Llama,
and everything that makes them tick.
Guided by ARIA — an AI with self-aware humor about teaching you to use other AIs.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___ _  _   _ _____ ___  ___ _____ ___
 / __| || | /_\_   _| _ )/ _ \_   _/ __|
| (__| __ |/ _ \| | | _ \ (_) || | \__ \
 \___|_||_/_/ \_\_| |___/\___/ |_| |___/
"""

SKILL_PACK = SkillPack(
    id="chatbots",
    title="The Chatbot Field Guide",
    subtitle="◈  Know Your AI Assistants Inside and Out  ◈",
    save_file_name="chatbots_quest",
    intro_story=INTRO_STORY,
    quit_message="ARIA dims to standby. Your progress is saved — the field guide will be here when you return.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Operator",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "chatbot_landscape": "landscape_surveyor",
        "how_chatbots_work": "mechanics_expert",
        "effective_conversations": "conversation_artist",
        "chatgpt_deep_dive": "gpt_specialist",
        "claude_deep_dive": "claude_specialist",
        "open_source_models": "open_source_advocate",
        "choosing_the_right_tool": "ai_strategist",
    },
    achievements={
        "landscape_surveyor":    ("Landscape Surveyor", "Mapped every major chatbot and the companies behind them!"),
        "mechanics_expert":      ("Mechanics Expert", "Understood tokens, context windows, temperature, and how LLMs generate text!"),
        "conversation_artist":   ("Conversation Artist", "Mastered multi-turn dialogue, role prompting, and iterative refinement!"),
        "gpt_specialist":        ("GPT Specialist", "Explored ChatGPT's full ecosystem: GPT-4o, DALL-E, browsing, code interpreter, and custom GPTs!"),
        "claude_specialist":     ("Claude Specialist", "Explored Claude's strengths: long context, safety, Artifacts, Projects, and Claude Code!"),
        "open_source_advocate":  ("Open Source Advocate", "Understood open-weight models, Ollama, local inference, and the freedom of self-hosted AI!"),
        "ai_strategist":         ("AI Strategist", "Learned to choose the right chatbot for any task based on capability, cost, and privacy!"),
        "no_hints":              ("Solo Operator", "Completed a zone without using any hints!"),
        "speed_reader":          ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Observer"),
        (6, "User"),
        (11, "Power User"),
        (16, "Evaluator"),
        (21, "Strategist"),
        (26, "Oracle"),
    ],
)
