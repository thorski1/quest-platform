"""
story.py -- Narrative for the Advanced AI Agents skill pack.

ARIA guides the player deeper into agent engineering -- architectures,
tool orchestration, multi-agent systems, memory, and production hardening.

Theme: "From understanding agents to building them for the real world."
"""

INTRO_STORY = """
[bold yellow]AI ACADEMY[/bold yellow]
[bold yellow]Chapter: The Agent Workshop[/bold yellow]

The lights in ARIA's lab shifted to a deeper hue -- ultraviolet edges
bleeding into the display like a neural network firing in slow motion.

[bold cyan]"You've crossed the Agent Frontier,"[/bold cyan] ARIA said, her voice
carrying a new weight. [bold cyan]"You know what agents are. You've seen
the loop. You understand tools, frameworks, and memory at a conceptual
level. But understanding isn't the same as building."[/bold cyan]

She pulled up a schematic -- not a diagram this time, but a full
architectural blueprint. Layers upon layers. Failure modes annotated
in red. Cost estimates in yellow. Security boundaries in white.

[bold cyan]"This chapter is different. This is where we go deep."[/bold cyan]

ARIA traced a path through the blueprint.

[bold cyan]"ReAct. Plan-and-execute. Tree of thought. Reflection loops.
These aren't just concepts -- they're engineering decisions that
determine whether your agent solves the problem or loops forever."[/bold cyan]

The blueprint expanded: multi-agent constellations, memory architectures,
tool schemas, evaluation pipelines, cost dashboards, kill switches.

[bold cyan]"Tool orchestration. Multi-agent coordination. Memory systems
that actually work. And the hardest part of all --"[/bold cyan]

She paused.

[bold cyan]"-- making it reliable enough to trust with real users,
real data, and real money."[/bold cyan]

ARIA's display settled into a steady pulse.

[bold cyan]"Welcome to the Agent Workshop. By the end, you won't just
understand agents. You'll know how to architect them, debug them,
evaluate them, and ship them."[/bold cyan]

[bold white]The Workshop doors open before you.[/bold white]
"""

ZONE_INTROS = {
    "agent_architectures": """
ARIA dimmed the overhead lights and illuminated five architectural
blueprints suspended in the air, each one glowing with a different
internal logic.

[bold cyan]"Every agent has an architecture,"[/bold cyan] ARIA said.
[bold cyan]"A pattern that determines how it thinks, plans, and acts.
Choose the wrong one and your agent spins its wheels.
Choose the right one and it solves problems you didn't think
were solvable."[/bold cyan]

She pointed to each blueprint in turn:
[bold yellow]ReAct[/bold yellow] -- [bold yellow]Plan-and-Execute[/bold yellow] --
[bold yellow]Reflection[/bold yellow] -- [bold yellow]Tree of Thought[/bold yellow] --
[bold yellow]Reflexion[/bold yellow]

[bold cyan]"These are the fundamental patterns. Every advanced agent
you've ever used is built on some combination of these.
Let's learn when each one shines -- and when it fails."[/bold cyan]

[bold white]Welcome to The Blueprint Chamber.[/bold white]
""",

    "tool_use_function_calling": """
ARIA walked into a forge where tool schemas hung on the walls
like blueprints for weapons -- each one precisely defined,
every parameter typed, every constraint documented.

[bold cyan]"You know agents use tools,"[/bold cyan] she said.
[bold cyan]"But there's a difference between 'using tools' and
'engineering a reliable tool system.' Structured output.
Schema design. Parallel execution. Error handling.
Permission models."[/bold cyan]

She picked up a schema and turned it in the light.

[bold cyan]"A bad tool schema is like a bad API -- the agent
will misuse it, misunderstand it, or ignore it entirely.
A good schema is invisible. The agent just knows what to do."[/bold cyan]

[bold white]Welcome to The Forge.[/bold white]
""",

    "multi_agent_systems": """
The display erupted into a constellation of interconnected agents --
orchestrators directing workers, swarms self-organizing, crews
collaborating on complex tasks.

[bold cyan]"One agent, one task -- that's the easy part,"[/bold cyan]
ARIA said. [bold cyan]"But the problems worth solving rarely fit
in one agent's head. Research, analysis, code review, content
pipelines -- these are team sports."[/bold cyan]

She highlighted the patterns:
[bold yellow]Orchestrator-Worker[/bold yellow] -- [bold yellow]Crew[/bold yellow] --
[bold yellow]Swarm[/bold yellow] -- [bold yellow]Delegation[/bold yellow]

[bold cyan]"Multi-agent systems are powerful. They're also fragile.
Infinite loops. Lost context. Conflicting outputs.
Building a team of agents that actually works? That's engineering
at its most demanding."[/bold cyan]

[bold white]Welcome to The Collective.[/bold white]
""",

    "memory_and_state": """
ARIA led you into a vast archive -- layers of storage stretching
in every direction. Some memories glowed hot and recent.
Others were deep, cold, ancient.

[bold cyan]"An agent without memory is a goldfish,"[/bold cyan] ARIA said.
[bold cyan]"It forgets everything the moment the conversation ends.
It can't learn from mistakes. It can't remember what the user
told it yesterday. It starts from zero every single time."[/bold cyan]

She opened the layers:
[bold yellow]Short-term (context window)[/bold yellow] --
[bold yellow]Long-term (persistent storage)[/bold yellow] --
[bold yellow]Episodic (past experiences)[/bold yellow] --
[bold yellow]RAG (retrieval as memory)[/bold yellow]

[bold cyan]"Memory is what turns a stateless function into something
that grows. Something that learns. Something that remembers
who it's talking to and what it's already tried."[/bold cyan]

[bold white]Welcome to The Memory Vaults.[/bold white]
""",

    "production_agents": """
ARIA stood before a deployment console -- green lights, red warnings,
dashboards tracking costs, latency, error rates, and user satisfaction
in real time.

[bold cyan]"Everything up to now has been architecture and theory,"[/bold cyan]
ARIA said. [bold cyan]"This zone is about reality. The messy, expensive,
sometimes terrifying reality of shipping an agent to real users."[/bold cyan]

She pulled up a post-mortem report.

[bold cyan]"Error handling. Human-in-the-loop gates. Evaluation pipelines.
Cost management. Security. Observability. Kill switches.
These aren't glamorous. They're not the fun part of building agents.
But they're the difference between a demo and a product."[/bold cyan]

[bold white]Welcome to The Proving Ground.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "agent_architectures": """
[bold green]The Blueprint Chamber hums with mastered patterns![/bold green]

ReAct. Plan-and-execute. Reflection. Tree of thought. Reflexion.
Not just names -- living architectures you can reason about and compose.

[bold cyan]"You see patterns now,"[/bold cyan] ARIA says. [bold cyan]"Not just individual
techniques, but how they combine. That's the shift from student
to architect."[/bold cyan]

The Forge glows ahead. Tool mastery awaits...
""",

    "tool_use_function_calling": """
[bold green]The Forge cools, its tools perfectly tempered![/bold green]

Structured output. Schema design. Parallel calls. Error handling.
Permissions. MCP. The full toolkit for reliable tool use.

[bold cyan]"An agent's tools are only as good as their schemas
and the error handling around them,"[/bold cyan] ARIA says.
[bold cyan]"Yours are production-grade now."[/bold cyan]

The Collective stirs ahead. Multi-agent systems beckon...
""",

    "multi_agent_systems": """
[bold green]The Collective operates in perfect coordination![/bold green]

Orchestrators, crews, swarms, delegation patterns -- and the failure
modes that can bring them all crashing down.

[bold cyan]"Building one agent is engineering,"[/bold cyan] ARIA says.
[bold cyan]"Building a team of agents is systems design.
You understand both now."[/bold cyan]

The Memory Vaults open ahead. State and recall await...
""",

    "memory_and_state": """
[bold green]The Memory Vaults pulse with organized recall![/bold green]

Short-term, long-term, episodic, semantic. RAG as memory.
Context management. Storage backends. The full memory stack.

[bold cyan]"An agent that remembers is an agent that learns,"[/bold cyan]
ARIA says. [bold cyan]"And an agent that learns gets better
with every interaction."[/bold cyan]

The Proving Ground awaits. Production reality calls...
""",

    "production_agents": """
[bold green]The Proving Ground falls silent. Every test passed.[/bold green]

Error handling. Human-in-the-loop. Evaluation. Cost management.
Security. Observability. The full stack of production concerns.

[bold cyan]"You've completed the Agent Workshop,"[/bold cyan] ARIA says,
and her voice carries the steady confidence of someone who knows
they've trained an engineer, not just a student.

[bold cyan]"You can architect agents. Debug them. Evaluate them.
Secure them. Ship them. That's not common knowledge --
it's hard-won expertise."[/bold cyan]

ARIA's display settles.

[bold cyan]"From blueprints to production. From theory to practice.
From understanding agents to building them."[/bold cyan]

[bold white]Workshop Master. Agent Architect. Builder. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "agent_architectures": "ARIA overlays all five architectural patterns on a single display. [bold yellow]\"Each pattern is a lens. But the real skill is knowing which lens to use -- and when to combine them. Show me you can think like an architect.\"[/bold yellow]",
    "tool_use_function_calling": "ARIA presents a complex user request that requires multiple tools in a precise sequence. [bold yellow]\"Tools are easy in isolation. Orchestrating them under real-world constraints -- that's the forge's final test.\"[/bold yellow]",
    "multi_agent_systems": "ARIA freezes a simulation of agents deadlocked in confusion. [bold yellow]\"Anyone can spin up multiple agents. Making them work as a team that's greater than the sum? That requires an architect's eye.\"[/bold yellow]",
    "memory_and_state": "ARIA stands at the intersection of three memory systems, each one solving a different problem. [bold yellow]\"Memory isn't one thing. It's a system of systems. Design the right one for the right problem.\"[/bold yellow]",
    "production_agents": "ARIA stands at the deployment console, finger hovering over the launch button. [bold yellow]\"The agent works in the lab. But the real world has adversarial users, API outages, and cost overruns. Are you ready to ship it?\"[/bold yellow]",
}
