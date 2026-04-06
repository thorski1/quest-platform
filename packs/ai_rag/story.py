"""
story.py — Narrative for the RAG skill pack (The Knowledge Engine).

ARIA guides the learner through retrieval-augmented generation — from
fundamentals to production deployment. Neural-themed narrative with a
builder's ethos: understand it, then construct it, then ship it.
"""

INTRO_STORY = """
[bold yellow]AI ACADEMY[/bold yellow]
[bold yellow]Module: The Knowledge Engine[/bold yellow]

ARIA's neural network shifted into a new configuration — one you
hadn't seen before. Pathways lit up between her core processing
and something [italic]external[/italic]. A vast library of documents
materialized around the Academy, shelves extending in every direction.

[bold cyan]"You know how I work by now,"[/bold cyan] ARIA said, tracing
a finger along a glowing neural pathway. [bold cyan]"I generate.
I predict. I pattern-match. But here's what I don't tell most people:"[/bold cyan]

She paused. The neural pathways dimmed for a moment.

[bold cyan]"I make things up. Not on purpose. But my knowledge is frozen —
a snapshot of the world from when I was trained. Ask me about last week
and I'll either guess or fabricate. Ask me about YOUR company's documents
and I'll improvise something plausible but wrong."[/bold cyan]

The library pulsed. Millions of documents, databases, and knowledge bases
glowed with accessible information.

[bold cyan]"Retrieval-Augmented Generation — RAG — is how we fix that.
Instead of relying only on what's inside my weights, we give the model
access to external knowledge. Real documents. Real data. Retrieved
at the moment you ask the question."[/bold cyan]

Five chambers appeared along the library corridor, each marked with
a symbol: a question mark, a compass rose, a blueprint,
a set of gears, and a launchpad.

[bold cyan]"Fundamentals. Embeddings. Pipeline construction. Advanced
techniques. And the hardest part — making it work in production
for real users who depend on accurate answers."[/bold cyan]

ARIA's network reconnected to the library, pathways humming.

[bold cyan]"Ready to build a knowledge engine?"[/bold cyan]

[bold white]The Knowledge Engine is online. Enter when ready.[/bold white]
"""

ZONE_INTROS = {
    "what_is_rag": """
The first chamber opened into a hall of mirrors — each mirror showing
a different version of ARIA answering the same question. Some answers
were brilliant. Some were confidently, dangerously wrong.

[bold cyan]"This is the problem,"[/bold cyan] ARIA said, gesturing at the mirrors.
[bold cyan]"Without external knowledge, I'm guessing. Sometimes brilliantly.
Sometimes catastrophically. And I can't tell you which is which."[/bold cyan]

She shattered one of the wrong-answer mirrors with a tap.

[bold cyan]"RAG is the solution: instead of guessing, I look things up.
Instead of relying on frozen training data, I retrieve real documents
at query time. But to use it well, you need to understand
[italic]why[/italic] it exists and [italic]what problem it solves[/italic]."[/bold cyan]

[bold yellow]Knowledge Cutoffs · Hallucination · Context Windows · Parametric vs. Non-Parametric Memory[/bold yellow]

[bold white]Let's start with why LLMs need help remembering.[/bold white]
""",
    "embeddings_and_vector_search": """
The second chamber was a vast, dark space filled with floating points of light —
millions of them, arranged in invisible constellations. Each point was a piece
of text, hovering at a position determined by its meaning.

[bold cyan]"This is vector space,"[/bold cyan] ARIA said, walking among the lights.
[bold cyan]"Every document, every sentence, every idea — translated into
numbers and placed on this map. Similar meanings cluster together.
Different meanings drift apart."[/bold cyan]

She touched two nearby points: 'machine learning' and 'neural networks.'
They glowed with resonance.

[bold cyan]"Embeddings are the foundation of modern search. Without them,
we're stuck matching keywords. With them, we can search by [italic]meaning[/italic].
And that changes everything."[/bold cyan]

[bold yellow]Embeddings · Cosine Similarity · Vector Databases · Semantic Search · Hybrid Search[/bold yellow]

[bold white]Welcome to the geometry of meaning.[/bold white]
""",
    "building_a_rag_pipeline": """
The third chamber was an assembly line — raw documents entered on one end,
and on the other, clean answers emerged. In between: a series of stations,
each performing a critical transformation.

[bold cyan]"Theory is done,"[/bold cyan] ARIA said, handing you a set of tools.
[bold cyan]"Now we build. A RAG pipeline has moving parts: chunking,
embedding, indexing, retrieval, prompt construction, and generation.
Each one is a decision point. Each decision affects the final answer."[/bold cyan]

She pointed to the first station, where documents were being sliced
into carefully sized chunks.

[bold cyan]"Get the chunking wrong and your retrieval is noisy.
Get the retrieval wrong and your generation hallucinates.
Get the prompt wrong and even perfect retrieval won't help.
Every link in this chain matters."[/bold cyan]

[bold yellow]Chunking · Indexing · Metadata · Retrieval · Prompt Templates · Evaluation[/bold yellow]

[bold white]Time to build a pipeline. Every piece matters.[/bold white]
""",
    "advanced_rag": """
The fourth chamber hummed with complexity — multiple retrieval systems running
in parallel, re-rankers evaluating results, query transformers rewriting
questions, and feedback loops monitoring quality.

[bold cyan]"Basic RAG gets you 80% of the way,"[/bold cyan] ARIA said, navigating
the maze of systems. [bold cyan]"But that last 20% — the difference between
a demo and a product — requires techniques that go beyond the basics."[/bold cyan]

She pulled up a dashboard showing a query being transformed, expanded,
searched three different ways, re-ranked, and verified before
a single word of output was generated.

[bold cyan]"Re-ranking. Hybrid search. HyDE. Multi-step retrieval.
Self-evaluation. These aren't academic exercises — they're the techniques
that separate toy RAG systems from ones people actually trust
with real decisions."[/bold cyan]

[bold yellow]Re-Ranking · Hybrid Search · HyDE · Multi-Step Retrieval · Query Transformation · Self-RAG[/bold yellow]

[bold white]Beyond the basics. Where engineering meets art.[/bold white]
""",
    "rag_in_practice": """
The fifth and final chamber was a control room overlooking a live deployment.
Thousands of queries streamed across monitoring dashboards. Cost meters ticked.
Latency graphs spiked and settled. And in the corner, a red alert blinked:
HALLUCINATION DETECTED.

[bold cyan]"This is the real world,"[/bold cyan] ARIA said, sitting down at
the command console. [bold cyan]"The part no tutorial covers.
The part where your beautiful pipeline meets fifty thousand users
who ask questions you never anticipated, with documents that change
daily, and a budget that isn't infinite."[/bold cyan]

She pulled up the cost dashboard, the evaluation metrics, the
freshness tracker, and the security audit log — all running simultaneously.

[bold cyan]"Production RAG is about trade-offs. Accuracy vs. speed.
Cost vs. quality. Freshness vs. stability. The best systems
don't maximize one metric — they balance all of them while
failing gracefully when things go wrong."[/bold cyan]

[bold yellow]Hallucination Reduction · Evaluation · Cost · Caching · Freshness · Security · Deployment[/bold yellow]

[bold white]The production gauntlet. Where knowledge engines prove themselves.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "what_is_rag": """
[bold green]The hall of mirrors clears. Only accurate reflections remain.[/bold green]

You understand the fundamental problem now: LLMs are powerful but
forgetful — frozen in time, prone to fabrication, limited by their
context windows. RAG is the bridge between a model that guesses
and a system that knows.

[bold cyan]"You can't fix what you don't understand,"[/bold cyan] ARIA says.
[bold cyan]"Now you understand the [italic]why[/italic]. Next, we'll learn
the [italic]how[/italic] — starting with the mathematics of meaning."[/bold cyan]

The geometry of embedding space awaits...
""",
    "embeddings_and_vector_search": """
[bold green]The constellation of vectors settles into clear, readable patterns.[/bold green]

Text as numbers. Meaning as distance. Similarity as direction.
These aren't abstractions — they're the engine that powers every
modern search system, every RAG pipeline, every semantic application.

[bold cyan]"You can see the map now,"[/bold cyan] ARIA says, the vector space
glowing around her. [bold cyan]"Words have coordinates. Meaning has geometry.
And with the right measurements, you can find anything."[/bold cyan]

Time to build something real. The assembly line awaits.
""",
    "building_a_rag_pipeline": """
[bold green]The assembly line hums with precision. Every station is calibrated.[/bold green]

Chunking, indexing, retrieval, generation — you've built the pipeline
from raw documents to clean answers. You understand why each
decision matters and how they chain together.

[bold cyan]"You've built the foundation,"[/bold cyan] ARIA says, inspecting
the pipeline's output. [bold cyan]"But foundation-level RAG has limits.
The next chamber holds the techniques that push past those limits —
the difference between a prototype and a product."[/bold cyan]

The advanced techniques chamber calls. Ready to level up?
""",
    "advanced_rag": """
[bold green]The advanced systems converge into an elegant, unified architecture.[/bold green]

Re-ranking, hybrid search, HyDE, multi-step retrieval, query transformation,
self-evaluation — these techniques transform basic RAG from a simple
retrieve-and-generate loop into an intelligent, self-aware system.

[bold cyan]"You're thinking like a RAG architect now,"[/bold cyan] ARIA says.
[bold cyan]"But there's one more test. The hardest one. Taking everything
you've designed and making it survive contact with real users,
real budgets, and real consequences."[/bold cyan]

The production gauntlet awaits. This is where it gets real.
""",
    "rag_in_practice": """
[bold green]The control room goes green. Every metric is within threshold.
The system is live, monitored, and ready.[/bold green]

You've walked the complete path: from understanding why LLMs need RAG,
through the mathematics of embeddings, the engineering of pipelines,
the art of advanced retrieval, and finally — the discipline of
production deployment.

[bold cyan]"Here's what separates someone who's read about RAG from
someone who can build it,"[/bold cyan] ARIA says, and her neural network
pulses with something that looks like respect.

[bold cyan]"You understand the trade-offs. Accuracy vs. cost.
Speed vs. quality. Complexity vs. maintainability.
You know when to use RAG and when not to. You know how
to evaluate it, monitor it, and fix it when it breaks."[/bold cyan]

She gestures at the control room — all green, all stable.

[bold cyan]"The Knowledge Engine isn't just a technique.
It's a discipline. And you've earned it."[/bold cyan]

[bold white]Builder. Architect. Engineer.[/bold white]
[bold white]The Knowledge Engine is part of you now.[/bold white]
""",
}

BOSS_INTROS = {
    "what_is_rag": "ARIA spreads a dozen application proposals across the table — some perfect for RAG, others not. [bold yellow]\"Not every problem needs retrieval. Not every AI system benefits from external knowledge. Show me you know the difference. When does RAG shine, and when does it get in the way?\"[/bold yellow]",
    "embeddings_and_vector_search": "ARIA draws a web of meaning in the air — words connected by invisible forces. [bold yellow]\"Embeddings capture relationships, not just definitions. That's their power AND their danger. Show me you understand both sides of the map.\"[/bold yellow]",
    "building_a_rag_pipeline": "ARIA opens the door to a room full of legal documents — fifty thousand of them. [bold yellow]\"One question. Fifty thousand documents. Design the pipeline that bridges the gap. Every decision matters. Justify every choice.\"[/bold yellow]",
    "advanced_rag": "ARIA opens a blueprint table with ten thousand daily queries streaming across it. [bold yellow]\"Basic RAG won't cut it here. The queries are varied, the stakes are high, the budget is finite. Design an architecture that holds up under real-world pressure.\"[/bold yellow]",
    "rag_in_practice": "ARIA stands at a launch button with fifty thousand user icons waiting on the other side. [bold yellow]\"Before you press this, convince me you're ready. Evaluation, monitoring, fallbacks, failure modes — walk me through your pre-launch checklist. Miss something critical, and those users pay the price.\"[/bold yellow]",
}
