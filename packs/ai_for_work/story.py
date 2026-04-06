"""
story.py — Narrative for the AI for Work skill pack.

ARIA guides professionals through mastering AI as a workplace co-pilot —
from writing and research to strategy and automation.
Theme: "Work smarter, not harder — AI as your co-pilot."
"""

INTRO_STORY = """
[bold yellow]AI ACADEMY[/bold yellow]
[bold yellow]Module: AI at Work[/bold yellow]

The interface shifted. Where the training modules had been, a sleek
command center materialized — glass walls overlooking a sprawling digital
cityscape, streams of data flowing like rivers between gleaming towers.

ARIA's holographic form stepped forward, projecting a constellation
of interconnected tools: email clients, spreadsheets, calendars,
slide decks, chat windows — all orbiting like planets around a central star.

[bold cyan]"Welcome to the Professional Suite,"[/bold cyan] ARIA said,
gesturing across the illuminated workspace.
[bold cyan]"Every one of these tools is something you already use.
Every day. Every week. Emails, reports, meetings, spreadsheets,
presentations, strategy sessions — the machinery of modern work."[/bold cyan]

She touched the central star, and it pulsed with warm light.

[bold cyan]"What if I told you that AI could handle the tedious parts —
the drafting, the formatting, the data gathering, the note-taking —
so you could focus on the parts that actually need [italic]you[/italic]?
Your judgment. Your creativity. Your relationships."[/bold cyan]

The constellation rearranged itself into seven distinct clusters,
each glowing a different color.

[bold cyan]"Seven domains. From the first email you draft with AI
to a fully automated workflow that saves your team hours every week.
Each one practical. Each one something you can use [italic]tomorrow[/italic]."[/bold cyan]

ARIA's projection sharpened into focus.

[bold cyan]"Work smarter, not harder. AI as your co-pilot.
Ready to transform how you work?"[/bold cyan]

[bold white]Your journey to professional AI mastery begins now.[/bold white]
"""

ZONE_INTROS = {
    "ai_for_writing": """
ARIA opened a blank document that hovered in the air between you.

[bold cyan]"Writing,"[/bold cyan] she said, [bold cyan]"is where most people
spend the most time at work. Emails. Reports. Blog posts. Proposals.
Slack messages. And most of it follows patterns — patterns that
AI is very, very good at helping with."[/bold cyan]

A cursor blinked in the floating document.

[bold cyan]"We're not talking about having AI write for you.
We're talking about having AI [italic]draft[/italic] for you —
so you can focus on editing, refining, and adding the insight
that only you can provide."[/bold cyan]

[bold white]Let's master the art of AI-assisted writing.[/bold white]
""",
    "ai_for_research": """
ARIA materialized a wall of documents — papers, reports, articles,
data sets — stretching higher than you could see.

[bold cyan]"Research,"[/bold cyan] ARIA said, gazing up at the towering stack,
[bold cyan]"is where knowledge workers either thrive or drown.
There's always more to read than time to read it.
More sources to check. More dots to connect."[/bold cyan]

She pulled a single thread, and a web of connections lit up
across the documents.

[bold cyan]"AI won't make you an expert overnight.
But it will make you a faster, more thorough researcher —
one who can synthesize, verify, and connect ideas
at a pace that wasn't possible five years ago."[/bold cyan]

[bold white]Let's sharpen your research edge.[/bold white]
""",
    "ai_for_presentations": """
ARIA conjured a stage — complete with a podium, a screen,
and an audience of silhouetted figures.

[bold cyan]"Presentations,"[/bold cyan] she said, adjusting an invisible slide,
[bold cyan]"are where ideas go to live or die. A great presentation
doesn't just inform — it persuades, inspires, and moves people to act."[/bold cyan]

The screen flickered with a cascade of slide templates.

[bold cyan]"AI can help you build the architecture — the structure,
the talking points, the data story. But the delivery?
The conviction? That's still all you."[/bold cyan]

[bold white]Let's build presentations that command the room.[/bold white]
""",
    "ai_for_data": """
ARIA summoned a vast spreadsheet — rows and columns stretching
to the horizon, numbers flowing like water through cells.

[bold cyan]"Data,"[/bold cyan] she said, zooming into a cluster of formulas,
[bold cyan]"is the foundation of every good business decision.
But most people spend 80% of their time cleaning and formatting data —
and only 20% actually analyzing it."[/bold cyan]

She flipped the ratio with a gesture.

[bold cyan]"AI inverts that equation. Let it handle the formulas,
the cleaning, the pattern-finding — so you can focus on the question
that matters most: [italic]'So what? What does this mean,
and what should we do about it?'[/italic]"[/bold cyan]

[bold white]Let's unlock the insights hiding in your data.[/bold white]
""",
    "ai_for_meetings": """
ARIA opened a door into a conference room where a meeting
was already in progress — voices overlapping, notes being scribbled,
action items slipping through the cracks.

[bold cyan]"Meetings,"[/bold cyan] she said with a knowing look.
[bold cyan]"Everyone has too many. Most run too long.
And half the decisions made in them are forgotten
by the time everyone gets back to their desks."[/bold cyan]

She waved a hand, and the chaotic scene froze — then reorganized itself
into neat streams of transcripts, action items, and follow-ups.

[bold cyan]"AI can't make bad meetings good.
But it can make sure that good meetings actually [italic]lead[/italic]
to something — that decisions stick, actions happen,
and nothing falls through the cracks."[/bold cyan]

[bold white]Let's transform how your meetings work.[/bold white]
""",
    "ai_for_strategy": """
ARIA expanded the workspace into a war room — whiteboards covered
with market maps, competitor profiles, and decision trees.

[bold cyan]"Strategy,"[/bold cyan] she said, uncapping a digital marker,
[bold cyan]"is the highest-leverage work you do.
One good strategic decision can be worth more than
a thousand hours of execution. And one bad one can cost just as much."[/bold cyan]

She drew a branching tree of possibilities on the board.

[bold cyan]"AI won't make your strategic decisions for you.
But it will help you think more rigorously —
brainstorming wider, analyzing deeper, stress-testing harder.
Think of it as a tireless strategic advisor
who never runs out of energy or patience."[/bold cyan]

[bold white]Let's sharpen your strategic thinking.[/bold white]
""",
    "ai_workflow_automation": """
ARIA revealed the final chamber — a vast machine room where
glowing pipelines connected every tool you'd used so far.
Data flowed through them automatically: emails triggering tasks,
meetings generating follow-ups, reports updating themselves.

[bold cyan]"Automation,"[/bold cyan] ARIA said, watching the system hum,
[bold cyan]"is where everything comes together.
Every skill you've learned — writing, research, presentations,
data, meetings, strategy — can be connected into workflows
that run themselves."[/bold cyan]

She pointed to a pipeline that transformed a meeting transcript
into action items, assigned tasks, and scheduled follow-ups — all without
a human touching it.

[bold cyan]"This is the final level: not just using AI for individual tasks,
but building systems that multiply your impact.
This is how you go from working [italic]with[/italic] AI
to having AI work [italic]for[/italic] you."[/bold cyan]

[bold white]Let's build the systems that set you free.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "ai_for_writing": """
[bold green]The Writer's Studio glows with completed drafts![/bold green]

Emails, reports, blog posts — each one crafted faster and sharper
than before. The floating document now reads like polished prose.

[bold cyan]"You've learned the most important thing about AI writing,"[/bold cyan]
ARIA says. [bold cyan]"It's not about letting AI write [italic]for[/italic] you.
It's about getting to the good part faster — the part where
your voice and your judgment make it real."[/bold cyan]

The research wall beckons beyond the studio door...
""",
    "ai_for_research": """
[bold green]The research wall is mapped and illuminated![/bold green]

Connections glow between sources. Summaries are crisp.
Citations are verified. The tower of documents has become a web of insight.

[bold cyan]"You can now move through information at a speed
that wasn't possible before,"[/bold cyan] ARIA says.
[bold cyan]"But you've also learned the most crucial lesson:
AI assists research — it doesn't replace the researcher's judgment."[/bold cyan]

A stage is being set in the next room. Presentations await...
""",
    "ai_for_presentations": """
[bold green]The stage lights up with a standing ovation![/bold green]

Slide decks are structured. Talking points are sharp.
Audiences are engaged. The silhouetted figures are on their feet.

[bold cyan]"You now know how to build presentations that move people,"[/bold cyan]
ARIA says. [bold cyan]"AI handles the architecture.
You bring the conviction. Together — unstoppable."[/bold cyan]

The data workshop hums with electricity ahead...
""",
    "ai_for_data": """
[bold green]The spreadsheet transforms into a gleaming dashboard![/bold green]

Numbers that were once overwhelming now tell clear stories.
Formulas run themselves. Insights rise to the surface.

[bold cyan]"Data literacy is a superpower,"[/bold cyan] ARIA says.
[bold cyan]"And with AI, you don't need to be a data scientist
to think like one. Ask the right questions.
Let AI handle the calculations."[/bold cyan]

Through the glass, a conference room awaits...
""",
    "ai_for_meetings": """
[bold green]The conference room runs like a precision instrument![/bold green]

Transcripts are accurate. Action items are tracked.
Follow-ups are sent. Decisions are logged. Nothing falls through the cracks.

[bold cyan]"You've done something remarkable,"[/bold cyan] ARIA says.
[bold cyan]"You've turned meetings — the most dreaded part of work —
into one of the most productive. That's a genuine transformation."[/bold cyan]

The war room doors swing open. Strategy awaits...
""",
    "ai_for_strategy": """
[bold green]The war room whiteboards glow with strategic clarity![/bold green]

SWOT analyses are specific. Scenarios are mapped.
Decision matrices are weighted. Recommendations are rigorous.

[bold cyan]"Strategic thinking with AI isn't about finding the right answer,"[/bold cyan]
ARIA says. [bold cyan]"It's about asking better questions,
considering more possibilities, and stress-testing your assumptions
before reality does it for you."[/bold cyan]

The machine room thrums. The final challenge awaits...
""",
    "ai_workflow_automation": """
[bold green]The machine room hums with automated perfection![/bold green]

Pipelines flow. Tools connect. Tasks trigger tasks.
What once took hours now takes minutes — or happens on its own.

[bold cyan]"You've reached the summit,"[/bold cyan] ARIA says, stepping back
to admire the system you've built.

[bold cyan]"Writing. Research. Presentations. Data. Meetings. Strategy.
Automation. Seven domains. One co-pilot.
You didn't just learn to use AI at work —
you learned to build a professional practice [italic]around[/italic] it."[/bold cyan]

ARIA's projection sharpens one final time.

[bold cyan]"Work smarter, not harder. That's not a slogan anymore.
It's how you operate."[/bold cyan]

[bold white]Chief AI Officer. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "ai_for_writing": "ARIA pulls up a complex scenario: a team that sends dozens of recurring communications every week. [bold yellow]\"If you could create one system that improves all of their writing at once — what would it look like? This is template thinking. The highest-leverage writing skill there is.\"[/bold yellow]",
    "ai_for_research": "ARIA projects a dense research brief onto the wall. [bold yellow]\"Anyone can gather information. The real skill is presenting it so that people trust it, act on it, and understand its limits. Show me you know how to deliver research that's both rigorous and honest.\"[/bold yellow]",
    "ai_for_presentations": "ARIA dims the lights and gestures to the stage. [bold yellow]\"You're about to pitch to the toughest audience imaginable. The slides are done. The data is solid. But are you ready for the questions they'll throw at you? That's where presentations are really won or lost.\"[/bold yellow]",
    "ai_for_data": "ARIA summons a live dashboard with blinking KPI widgets. [bold yellow]\"Your CEO wants a dashboard that tells the story of the business at a glance — and updates itself. This is the final data challenge: building something that delivers value every single week without you touching it.\"[/bold yellow]",
    "ai_for_meetings": "ARIA freezes the conference room mid-meeting. [bold yellow]\"One meeting becomes an agenda, a transcript, action items, follow-ups, and a decision log — all feeding into the next meeting. That's not a meeting. That's a system. Build me that system.\"[/bold yellow]",
    "ai_for_strategy": "ARIA clears the war room whiteboards and hands you a single brief. [bold yellow]\"The board meets in one hour. Your recommendation needs to be airtight — not just what to do, but why, what else you considered, what could go wrong, and how you'd mitigate it. This is strategic rigor.\"[/bold yellow]",
    "ai_workflow_automation": "ARIA steps back from the machine room controls and gestures for you to take over. [bold yellow]\"The CEO wants a roadmap. Not just 'what can we automate' — but what should we automate first, how do we roll it out, and how do we bring the team along. This is automation leadership.\"[/bold yellow]",
}
