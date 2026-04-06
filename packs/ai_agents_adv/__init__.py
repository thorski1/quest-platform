"""
AI Agents Advanced skill pack -- The Agent Workshop
Deep dive into agent architectures, tool orchestration, multi-agent
systems, memory engineering, and production hardening.
Assumes The Agent Frontier chapter completed.
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
    _    ____  _____ _   _ _____  __        _____  ____  _  ______  _   _  ___  ____
   / \  / ___|| ____| \ | |_   _| \ \      / / _ \|  _ \| |/ / ___|| | | |/ _ \|  _ \
  / _ \| |  _ |  _| |  \| | | |    \ \ /\ / / | | | |_) | ' /\___ \| |_| | | | | |_) |
 / ___ \ |_| || |___| |\  | | |     \ V  V /| |_| |  _ <| . \ ___) |  _  | |_| |  __/
/_/   \_\____||_____|_| \_| |_|      \_/\_/  \___/|_| \_\_|\_\____/|_| |_|\___/|_|
"""

SKILL_PACK = SkillPack(
    id="ai_agents_adv",
    title="The Agent Workshop",
    subtitle="◈  Advanced Agent Engineering  ◈",
    save_file_name="ai_agents_adv_quest",
    intro_story=INTRO_STORY,
    quit_message="The workshop powers down... but the blueprints remain.",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "agent_architectures": "blueprint_master",
        "tool_use_function_calling": "forge_keeper",
        "multi_agent_systems": "collective_architect",
        "memory_and_state": "memory_engineer",
        "production_agents": "production_veteran",
    },
    achievements={
        "blueprint_master":     ("Blueprint Master", "Mastered ReAct, plan-and-execute, reflection, and tree of thought!"),
        "forge_keeper":         ("Forge Keeper", "Conquered structured output, tool schemas, parallel calls, and MCP!"),
        "collective_architect": ("Collective Architect", "Designed orchestrator-worker, crew, and swarm multi-agent systems!"),
        "memory_engineer":      ("Memory Engineer", "Built layered memory: short-term, long-term, episodic, and RAG!"),
        "production_veteran":   ("Production Veteran", "Shipped agents with error handling, eval, security, and cost management!"),
        "no_hints":             ("Self-Sufficient", "Completed a zone without any hints!"),
        "speed_reader":         ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Apprentice"),
        (6, "Engineer"),
        (11, "Architect"),
        (16, "Principal"),
        (21, "Distinguished"),
        (26, "Workshop Master"),
    ],
)
