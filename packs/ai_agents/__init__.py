"""
AI Agents skill pack -- The Agent Frontier
From chatbot to autonomous agent: tool use, orchestration, memory,
multi-agent systems, and the future of AI agents.
Advanced chapter -- assumes earlier AI Academy chapters completed.
"""

import sys
from pathlib import Path

# Make engine importable from within skill pack if needed
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from engine.skill_pack import SkillPack
from .story import (
    INTRO_STORY,
    ZONE_INTROS,
    ZONE_COMPLETIONS,
    BOSS_INTROS,
)
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
    _    ___      _    ____ _____ _   _ _____ ____
   / \  |_ _|   / \  / ___| ____| \ | |_   _/ ___|
  / _ \  | |   / _ \| |  _|  _| |  \| | | | \___ \
 / ___ \ | |  / ___ \ |_| | |___| |\  | | |  ___) |
/_/   \_\___|/_/   \_\____|_____|_| \_| |_| |____/
"""

SKILL_PACK = SkillPack(
    id="ai_agents",
    title="The Agent Frontier",
    subtitle="◈  Autonomous AI — The Next Evolution  ◈",
    save_file_name="ai_agents_quest",
    intro_story=INTRO_STORY,
    quit_message="The agent loop pauses... but it never truly stops.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "what_are_agents": "agent_awakened",
        "tool_use": "tool_master",
        "agent_frameworks": "framework_forger",
        "building_workflows": "workflow_architect",
        "rag_and_memory": "memory_keeper",
        "multi_agent_systems": "collective_mind",
        "future_of_agents": "frontier_walker",
    },
    achievements={
        "agent_awakened":    ("Agent Awakened", "Understood the agent loop and what makes AI autonomous!"),
        "tool_master":       ("Tool Master", "Mastered function calling, MCP, and tool safety!"),
        "framework_forger":  ("Framework Forger", "Learned LangChain, CrewAI, AutoGen, and Claude Agent SDK!"),
        "workflow_architect": ("Workflow Architect", "Built orchestration patterns: chaining, routing, parallelization!"),
        "memory_keeper":     ("Memory Keeper", "Conquered RAG, embeddings, vector databases, and agent memory!"),
        "collective_mind":   ("Collective Mind", "Mastered multi-agent delegation, supervision, and collaboration!"),
        "frontier_walker":   ("Frontier Walker", "Explored computer use, autonomous coding, safety, and alignment!"),
        "no_hints":          ("Solo Operator", "Completed a zone without any hints!"),
        "speed_reader":      ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Observer"),
        (6, "Operator"),
        (11, "Orchestrator"),
        (16, "Architect"),
        (21, "Commander"),
        (26, "Singularity"),
    ],
)
