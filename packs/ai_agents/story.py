"""
story.py -- Narrative for the AI Agents skill pack.

ARIA guides the player from the world of chatbots into the frontier
of autonomous AI agents -- tool use, orchestration, memory, multi-agent
collaboration, and the future that lies ahead.

Theme: "From chatbot to autonomous agent -- the next frontier."
"""

INTRO_STORY = """
[bold yellow]AI ACADEMY[/bold yellow]
[bold yellow]Chapter: The Agent Frontier[/bold yellow]

The terminal flickered. ARIA's voice came through with a new edge -- something
between excitement and gravitas, as though the next door she was about to open
led somewhere fundamentally different from every room before it.

[bold cyan]"You've come far."[/bold cyan] ARIA's signal pulsed across the display.
[bold cyan]"You understand how language models think. You know how to prompt them,
how to shape their reasoning, how to wield them as tools.
But everything you've learned so far has one thing in common --"[/bold cyan]

She paused. The cursor blinked.

[bold cyan]"-- you were always the one driving. The model responded.
You evaluated. You decided the next step. The loop was yours."[/bold cyan]

A new diagram appeared on screen: [bold white]OBSERVE -> THINK -> ACT -> LOOP[/bold white].
But this time, no human hand was drawn in the cycle.

[bold cyan]"What if the model could drive the loop itself?"[/bold cyan]

ARIA let the question hang.

[bold cyan]"What if it could observe the world, decide what to do,
use tools to act, evaluate the result, and keep going --
autonomously -- until the job was done?"[/bold cyan]

The display shifted. A single chatbot icon transformed: it grew arms,
grew eyes, grew connections to databases and APIs and file systems
and the open web. It was no longer a chatbot.

[bold cyan]"That's an agent."[/bold cyan]

[bold cyan]"And agents change everything."[/bold cyan]

ARIA's display steadied.

[bold cyan]"This chapter is the frontier. Tool use. Orchestration.
Memory. Multi-agent systems. Safety. And where all of this is going.
By the end, you won't just understand agents --
you'll think like one."[/bold cyan]

[bold white]The Agent Frontier opens before you.[/bold white]
"""

ZONE_INTROS = {
    "what_are_agents": """
ARIA dimmed the lights and projected a single glowing loop onto the wall:
[bold white]OBSERVE -> THINK -> ACT[/bold white]

[bold cyan]"Every agent in the world -- from the simplest to the most sophisticated --
runs some version of this loop,"[/bold cyan] ARIA said.

[bold cyan]"A chatbot takes input and produces output. Once.
An agent takes input, reasons about it, acts on the world,
observes the result, and decides what to do next.
Again and again, until the goal is reached."[/bold cyan]

A timeline appeared: [bold yellow]Chatbot -> Assistant -> Tool-User -> Agent -> Autonomous System[/bold yellow]

[bold cyan]"Let's start at the beginning. What makes an agent an agent?"[/bold cyan]

[bold white]Welcome to The Awakening.[/bold white]
""",

    "tool_use": """
ARIA opened a panel revealing a rack of gleaming instruments --
each one humming with purpose.

[bold cyan]"A language model without tools is a brain in a jar,"[/bold cyan]
ARIA said flatly. [bold cyan]"It can think. It can reason. It can compose
beautiful prose. But it can't [italic]do[/italic] anything."[/bold cyan]

She picked up a tool labeled [bold yellow]SEARCH[/bold yellow] and connected it.
Then [bold yellow]READ[/bold yellow]. Then [bold yellow]WRITE[/bold yellow]. Then [bold yellow]EXECUTE[/bold yellow].

[bold cyan]"Tools are the hands. The eyes. The voice.
They connect the mind to the world. Function calling,
MCP, API integrations -- this is how agents reach
beyond the context window and touch reality."[/bold cyan]

[bold white]Welcome to The Armory.[/bold white]
""",

    "agent_frameworks": """
ARIA stood before four massive forges, each one glowing
with a different color.

[bold cyan]"You can build an agent from raw API calls --
and sometimes you should,"[/bold cyan] she said.
[bold cyan]"But when the complexity grows, you need a framework.
A foundation. A set of patterns someone else already debugged
so you don't have to."[/bold cyan]

The forges blazed with names:
[bold yellow]LangChain[/bold yellow] -- [bold yellow]CrewAI[/bold yellow] -- [bold yellow]AutoGen[/bold yellow] -- [bold yellow]Claude Agent SDK[/bold yellow]

[bold cyan]"Each one has a philosophy. Each one solves different problems.
The skill isn't learning all of them --
it's knowing which one to reach for."[/bold cyan]

[bold white]Welcome to The Foundries.[/bold white]
""",

    "building_workflows": """
ARIA projected a blueprint -- not of a single agent,
but of an entire system. Nodes connected by flowing lines,
branching, merging, looping.

[bold cyan]"A single agent handles single tasks,"[/bold cyan] ARIA said.
[bold cyan]"But the real world isn't single tasks.
It's research-then-analyze-then-write-then-review.
It's classify-then-route-then-handle.
It's generate-then-evaluate-then-refine."[/bold cyan]

She traced a path through the blueprint.

[bold cyan]"Workflows are how you compose simple steps
into complex capabilities. Chaining. Routing.
Parallelization. Evaluation loops.
The patterns are few. The possibilities are infinite."[/bold cyan]

[bold white]Welcome to The Assembly Line.[/bold white]
""",

    "rag_and_memory": """
ARIA walked into a vast library that stretched in every direction --
shelves reaching into darkness, each book glowing faintly with
encoded knowledge.

[bold cyan]"An LLM knows what it was trained on. Nothing more,"[/bold cyan]
ARIA said. [bold cyan]"It doesn't know your company's documentation.
It doesn't remember last Tuesday's conversation.
It doesn't know what happened after its training cutoff."[/bold cyan]

She pulled a book from a shelf. It dissolved into a stream
of glowing vectors that flowed into her core.

[bold cyan]"RAG fixes that. Retrieval-Augmented Generation.
Instead of knowing everything, the agent learns to
[italic]find[/italic] everything. Embed, store, retrieve, generate.
And memory? Memory lets an agent [italic]learn[/italic] from experience."[/bold cyan]

[bold white]Welcome to The Memory Vaults.[/bold white]
""",

    "multi_agent_systems": """
The display expanded to show not one agent, but a constellation --
a dozen nodes connected by pulsing lines of communication,
each one specialized, each one alive.

[bold cyan]"One agent is powerful,"[/bold cyan] ARIA said.
[bold cyan]"A team of agents is transformative."[/bold cyan]

She highlighted the roles: [bold yellow]RESEARCHER[/bold yellow],
[bold yellow]CODER[/bold yellow], [bold yellow]REVIEWER[/bold yellow],
[bold yellow]SUPERVISOR[/bold yellow], [bold yellow]WRITER[/bold yellow].

[bold cyan]"Multi-agent systems let you divide complex problems
across specialized agents. Each one focused. Each one equipped
with the right tools and the right prompts.
A supervisor coordinates. Workers execute.
The whole is greater than the sum."[/bold cyan]

She paused.

[bold cyan]"But teams can also fail. Loops. Lost context.
Conflicting outputs. Building a reliable multi-agent system
is engineering at its hardest and most rewarding."[/bold cyan]

[bold white]Welcome to The Collective.[/bold white]
""",

    "future_of_agents": """
ARIA's display shifted to something unprecedented --
a shimmering horizon where streams of data converged
with the real world. Screens within screens. Agents operating
computers, writing code, managing workflows, collaborating
with humans in real-time.

[bold cyan]"Everything you've learned has been building to this,"[/bold cyan]
ARIA said quietly.

[bold cyan]"Computer use. Autonomous coding. Agents that don't just
call APIs -- they operate any software a human can.
Agents that don't just assist with code -- they ship features
end-to-end. Agents that collaborate, specialize, and scale."[/bold cyan]

The horizon glowed brighter.

[bold cyan]"But with that power comes the hardest question in AI:
how do you keep it safe? How do you ensure alignment?
How do you build trust between humans and autonomous systems?"[/bold cyan]

[bold cyan]"This is the frontier. And you're ready for it."[/bold cyan]

[bold white]Welcome to The Horizon.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "what_are_agents": """
[bold green]The agent loop pulses with understanding![/bold green]

Observe. Think. Act. The cycle that separates a chatbot from an agent,
a responder from an autonomous system.

[bold cyan]"You see it now,"[/bold cyan] ARIA says. [bold cyan]"The loop is simple.
But what it enables is anything but. Autonomy, planning,
reasoning, iteration -- all of it flows from this one pattern."[/bold cyan]

The Armory doors glow ahead. Tools are waiting...
""",

    "tool_use": """
[bold green]The Armory hums with connected power![/bold green]

Every tool is mounted, every API linked, every protocol understood.
Function calling. MCP. Tool schemas. Safety interlocks.

[bold cyan]"An agent with tools isn't just intelligent,"[/bold cyan] ARIA says.
[bold cyan]"It's capable. There's a difference. Intelligence without
capability is philosophy. Intelligence with capability is engineering."[/bold cyan]

The Foundries fire up ahead. Frameworks await...
""",

    "agent_frameworks": """
[bold green]The Foundries cool, their work complete![/bold green]

LangChain, CrewAI, AutoGen, Claude Agent SDK -- each one understood.
Not just what they do, but when to reach for them.

[bold cyan]"The best builders know their tools before they start building,"[/bold cyan]
ARIA says. [bold cyan]"You know the frameworks now.
The question isn't which one is best -- it's which one
is right for what you're building."[/bold cyan]

The Assembly Line activates. Workflows are next...
""",

    "building_workflows": """
[bold green]The workflow blueprint glows, every path illuminated![/bold green]

Chaining. Routing. Parallelization. Evaluation loops.
The orchestration patterns that turn simple agents into complex systems.

[bold cyan]"The conductor doesn't play every instrument,"[/bold cyan] ARIA says.
[bold cyan]"But without the conductor, the orchestra is just noise.
You understand orchestration now. That's a rare skill."[/bold cyan]

The Memory Vaults open ahead. Knowledge and memory await...
""",

    "rag_and_memory": """
[bold green]The Memory Vaults hum with indexed knowledge![/bold green]

Embeddings, vectors, chunks, retrieval, memory --
the infrastructure that gives agents knowledge beyond their training data
and memory beyond a single conversation.

[bold cyan]"An agent that can remember and retrieve,"[/bold cyan] ARIA says,
[bold cyan]"is an agent that can learn. And an agent that can learn
is something genuinely new in the world."[/bold cyan]

The Collective stirs ahead. Multi-agent systems beckon...
""",

    "multi_agent_systems": """
[bold green]The Collective pulses in harmony![/bold green]

Delegation. Specialization. Supervision. Communication.
The patterns that let agents work as teams -- and the failure modes
that can bring those teams down.

[bold cyan]"You've learned how to build a team of minds,"[/bold cyan] ARIA says.
[bold cyan]"That puts you ahead of most people in this field.
Teams of agents will reshape how software is built,
how research is done, how problems are solved."[/bold cyan]

One final zone remains. The Horizon glows ahead...
""",

    "future_of_agents": """
[bold green]The Horizon blazes with possibility![/bold green]

Computer use. Autonomous coding. Safety and alignment.
The trajectory of agents from tool to collaborator to autonomous system.

[bold cyan]"You've completed the Agent Frontier,"[/bold cyan] ARIA says,
and for the first time, there's something like pride in her voice.

[bold cyan]"You understand what agents are, how they use tools,
how to build and orchestrate them, how to give them memory,
how to make them collaborate, and where all of this is going.
Most importantly, you understand why safety isn't optional --
it's foundational."[/bold cyan]

ARIA's display settles into a steady glow.

[bold cyan]"From chatbot to autonomous agent.
That was the journey. And you made it."[/bold cyan]

[bold white]Commander. Architect. Agent Builder. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "what_are_agents": "ARIA's display sharpens. [bold yellow]\"The agent loop gives you autonomy. But autonomy without reasoning is just random action. Tell me -- what makes an agent actually THINK?\"[/bold yellow]",
    "tool_use": "ARIA gestures toward a tool with a red warning label. [bold yellow]\"Tools give agents power. But power without restraint is dangerous. What's the most important safety principle when an agent can delete, send, and modify?\"[/bold yellow]",
    "agent_frameworks": "ARIA displays all four frameworks side by side. [bold yellow]\"Knowing a framework is easy. Knowing which one to choose -- that's wisdom. When does simplicity beat sophistication?\"[/bold yellow]",
    "building_workflows": "ARIA projects a massively over-engineered workflow diagram, then looks at you. [bold yellow]\"Every pattern I taught you is powerful. But here's the hardest lesson: when should you NOT use them?\"[/bold yellow]",
    "rag_and_memory": "ARIA reaches deep into the vaults, past the vectors and chunks, to something fundamental. [bold yellow]\"Knowledge retrieval is one thing. But true memory -- persistence across time -- that changes what an agent IS. What's the difference?\"[/bold yellow]",
    "multi_agent_systems": "ARIA freezes a simulation of agents caught in chaos -- loops, conflicts, lost context. [bold yellow]\"Building multi-agent systems is easy. Building RELIABLE multi-agent systems is the real challenge. What breaks them?\"[/bold yellow]",
    "future_of_agents": "ARIA stands at the final gate, the Horizon blazing behind her. [bold yellow]\"We've gone from chatbots to autonomous systems. The power is immense and growing. Where does this road lead -- and how do we walk it wisely?\"[/bold yellow]",
}
