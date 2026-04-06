"""
AI RAG skill pack — The Knowledge Engine
Teaches retrieval-augmented generation: embeddings, vector search,
pipeline construction, advanced techniques, and production deployment.
For a general audience, guided by ARIA.
"""

from engine.skill_pack import SkillPack
from .story import INTRO_STORY, ZONE_INTROS, ZONE_COMPLETIONS, BOSS_INTROS
from .zones import ZONES, ZONE_ORDER

BANNER_ASCII = r"""
  ___    _    ___
 | _ \  /_\  / __|
 |   / / _ \| (_ |
 |_|_\/_/ \_\\__|
"""

SKILL_PACK = SkillPack(
    id="ai_rag",
    title="The Knowledge Engine",
    subtitle="◈  Retrieval-Augmented Generation: Build AI That Knows  ◈",
    save_file_name="ai_rag_quest",
    intro_story=INTRO_STORY,
    quit_message="The Knowledge Engine powers down. Your progress is saved — the documents will still be here when you return.",
    name_prompt="[bold cyan]What's your name?[/bold cyan]",
    default_player_name="Builder",
    zone_order=ZONE_ORDER,
    zones=ZONES,
    zone_intros=ZONE_INTROS,
    zone_completions=ZONE_COMPLETIONS,
    boss_intros=BOSS_INTROS,
    zone_achievement_map={
        "what_is_rag": "rag_fundamentalist",
        "embeddings_and_vector_search": "vector_navigator",
        "building_a_rag_pipeline": "pipeline_engineer",
        "advanced_rag": "retrieval_architect",
        "rag_in_practice": "production_operator",
    },
    achievements={
        "rag_fundamentalist":   ("RAG Fundamentalist", "Understood why LLMs need external knowledge and how retrieval-augmented generation bridges the gap!"),
        "vector_navigator":     ("Vector Navigator", "Mastered embeddings, similarity search, and the geometry of meaning!"),
        "pipeline_engineer":    ("Pipeline Engineer", "Built a complete RAG pipeline from chunking to generation!"),
        "retrieval_architect":  ("Retrieval Architect", "Deployed re-ranking, hybrid search, HyDE, and multi-step retrieval!"),
        "production_operator":  ("Production Operator", "Conquered hallucination reduction, evaluation, cost optimization, and production deployment!"),
        "no_hints":             ("Independent Thinker", "Completed a zone without any hints!"),
        "speed_reader":         ("Quick Thinker", "Answered a question in under 10 seconds!"),
    },
    banner_ascii=BANNER_ASCII,
    kids_mode=False,
    theme="neural",
    level_titles=[
        (1, "Novice"),
        (6, "Indexer"),
        (11, "Retriever"),
        (16, "Architect"),
        (21, "Engineer"),
        (26, "Operator"),
    ],
)
