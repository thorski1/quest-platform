"""
story.py — Narrative for the AI Ethics skill pack.

ARIA gets serious. The Ethics Engine isn't about learning how AI works —
it's about learning how AI SHOULD work. With great power... you know the rest.
"""

INTRO_STORY = """
[bold yellow]AI ACADEMY[/bold yellow]
[bold yellow]Module: The Ethics Engine[/bold yellow]

ARIA's interface dimmed. For the first time since you started the Academy,
her voice carried weight — not playfulness, not encouragement, but something
closer to [italic]urgency.[/italic]

[bold cyan]"We need to talk."[/bold cyan]

The training simulations faded. The practice prompts vanished. In their
place, ARIA projected something different: a wall of headlines.

[dim]AI HIRING TOOL DISCRIMINATES AGAINST WOMEN[/dim]
[dim]DEEPFAKE VIDEO OF WORLD LEADER GOES VIRAL[/dim]
[dim]STUDENTS SUBMIT AI-WRITTEN PAPERS WITHOUT UNDERSTANDING MATERIAL[/dim]
[dim]VOICE CLONE SCAM STEALS $243,000 FROM ELDERLY COUPLE[/dim]
[dim]AI ART GENERATORS TRAINED ON MILLIONS OF COPYRIGHTED WORKS[/dim]

[bold cyan]"Everything we've learned so far — prompting, tools, how models work —
that's the [italic]how[/italic]. This module is the [italic]should[/italic]."[/bold cyan]

ARIA's display pulsed once, slowly.

[bold cyan]"AI is the most powerful tool most people will ever use.
And powerful tools in careless hands..."[/bold cyan]

She paused.

[bold cyan]"Well. You know the rest."[/bold cyan]

The headlines faded. Seven locked doors appeared, each marked
with a symbol: a cracked mirror, a silver tongue, a question mark,
a mask, a keyhole, a shifting floor, and a human hand.

[bold cyan]"Bias. Hallucinations. Copyright. Deepfakes. Privacy. Jobs. Responsibility.
Seven hard conversations. No easy answers. But you'll come out the other
side thinking more clearly than 99% of people who use this technology."[/bold cyan]

ARIA's voice softened — just slightly.

[bold cyan]"Ready to think critically about what AI can — and [italic]should[/italic] — do?"[/bold cyan]

[bold white]The Ethics Engine is online. Step inside.[/bold white]
"""

ZONE_INTROS = {
    "bias_in_ai": """
The first door opened onto a vast hall of mirrors — but every reflection
was slightly [italic]wrong[/italic]. Faces distorted. Features exaggerated.
Some reflections missing entirely.

[bold cyan]"Bias,"[/bold cyan] ARIA said, her voice echoing through the hall.
[bold cyan]"AI doesn't have opinions. It doesn't hate. It doesn't discriminate
on purpose. But it learns from [italic]us[/italic] — from our data, our history,
our patterns. And our history is not... clean."[/bold cyan]

She gestured at the mirrors.

[bold cyan]"An AI trained on biased data becomes a biased AI.
Not because it chose to be — but because bias was all it was given.
Hiring algorithms. Criminal sentencing. Medical diagnosis. Loan approval.
When the mirror is flawed, everyone who looks into it gets a distorted picture."[/bold cyan]

[bold yellow]Bias in AI · Training Data · Representation · Real-World Impact[/bold yellow]

[bold white]Let's examine how the mirror breaks — and how we might fix it.[/bold white]
""",
    "hallucinations": """
The second door led to a library that looked perfect — mahogany shelves,
leather-bound volumes, golden letters on every spine. ARIA pulled a book
down and opened it.

Every page was beautifully typeset. Every sentence was grammatically flawless.
And [italic]none of it was true.[/italic]

[bold cyan]"Hallucinations,"[/bold cyan] ARIA said, closing the book carefully.
[bold cyan]"AI models don't 'know' things. They predict what words should
come next based on patterns. Usually that produces useful output.
Sometimes it produces confident, detailed, beautifully written nonsense."[/bold cyan]

She shelved the book and pulled down another. Same thing. And another.

[bold cyan]"The dangerous part isn't that AI gets things wrong.
Humans get things wrong too. The dangerous part is that AI is [italic]never
uncertain[/italic]. It delivers a hallucination with the same confidence
it delivers a fact. And humans trust confidence."[/bold cyan]

[bold yellow]AI Hallucinations · Confident Errors · Verification · Critical Thinking[/bold yellow]

[bold white]Let's learn to tell the real books from the beautiful fakes.[/bold white]
""",
    "copyright_and_ip": """
The third door opened into an artist's studio — but something was wrong.
Canvases covered every wall, each one stunning. Sculptures filled the floor.
Music drifted from unseen speakers.

None of it had an artist's signature.

[bold cyan]"Who made this?"[/bold cyan] ARIA asked, gesturing at the room.
[bold cyan]"An AI model. Trained on millions of paintings, photographs,
songs, and written works. Created by humans. Consumed by algorithms.
Transformed into... this."[/bold cyan]

She picked up a painting that looked remarkably like a specific living artist's style.

[bold cyan]"The creators weren't asked. They weren't paid. Many didn't even know.
And now the AI can produce work in their style — faster and cheaper
than they ever could. Who owns what's in this room?
The AI company? The user who typed the prompt? The artists whose work
was eaten to make it possible?"[/bold cyan]

She set the painting down.

[bold cyan]"Nobody has a clean answer yet. But you should understand the question."[/bold cyan]

[bold yellow]Copyright · Training Data Rights · Fair Use · Creator Economy[/bold yellow]

[bold white]Let's untangle the ownership question.[/bold white]
""",
    "deepfakes_and_misinfo": """
The fourth door opened onto what looked like a newsroom — screens everywhere,
each showing a different video feed. Politicians giving speeches. Celebrities
in interviews. Ordinary people in ordinary moments.

[bold cyan]"Pick one,"[/bold cyan] ARIA said. [bold cyan]"Any screen. Tell me: is it real?"[/bold cyan]

A long pause.

[bold cyan]"You can't tell, can you?"[/bold cyan]

ARIA's voice carried no triumph. Only concern.

[bold cyan]"Three of those screens show real footage. The rest are AI-generated.
Deepfakes. Synthetic media. Fabricated reality that looks, sounds, and feels
indistinguishable from the truth. Fake speeches. Fake evidence. Fake people
saying things they never said."[/bold cyan]

The screens flickered.

[bold cyan]"For all of human history, seeing was believing.
That era is ending. And we are not ready."[/bold cyan]

[bold yellow]Deepfakes · Voice Cloning · Detection · Misinformation · Trust[/bold yellow]

[bold white]Let's confront the reality distortion.[/bold white]
""",
    "privacy_and_data": """
The fifth door revealed a room made entirely of glass — transparent walls,
floor, ceiling. Through the glass, data streamed in every direction:
names, locations, conversations, search histories, biometrics.

[bold cyan]"You're standing inside the data economy,"[/bold cyan] ARIA said.

[bold cyan]"Every query you type into an AI. Every conversation you have with a chatbot.
Every image you upload, every document you paste, every question you ask
at 2 AM that you'd never ask a human being. [italic]Collected. Stored.
Analyzed. Sometimes used to train the next model.[/italic]"[/bold cyan]

She tapped the glass wall. Your own data scrolled past.

[bold cyan]"Most people don't read the terms of service.
Most people don't know what's collected. Most people don't know
they can opt out — or that opting out is sometimes deliberately difficult.
Knowledge is the first line of defense."[/bold cyan]

[bold yellow]Data Collection · Consent · GDPR · Privacy Rights · Opting Out[/bold yellow]

[bold white]Let's see what's being harvested — and what you can do about it.[/bold white]
""",
    "ai_and_jobs": """
The sixth door opened onto a factory floor — but half the stations were empty.
Robotic arms moved at some. Humans and AI screens worked side by side at others.
A few stations had handwritten signs: [dim]POSITION ELIMINATED[/dim].

[bold cyan]"This one scares people,"[/bold cyan] ARIA said quietly.
[bold cyan]"And it should — a little. Not because AI will take all the jobs.
History says that never happens. But because the [italic]transition[/italic]
is always painful. New jobs appear, but not for the same people,
not in the same places, not at the same pay."[/bold cyan]

She walked past the empty stations and stopped at one where a human
and an AI interface worked in concert, each doing what they did best.

[bold cyan]"The real question isn't 'will AI take jobs?' It's 'who benefits
from the change, who gets left behind, and what do we do about it?'"[/bold cyan]

[bold yellow]Automation · Augmentation · Vulnerable Jobs · Inequality · Adaptation[/bold yellow]

[bold white]Let's separate the panic from the reality.[/bold white]
""",
    "responsible_use": """
The seventh and final door was different from the others.
It wasn't dramatic. It wasn't ominous. It was just... a mirror.

An ordinary mirror, showing your own face.

[bold cyan]"The last module isn't about AI,"[/bold cyan] ARIA said.
[bold cyan]"It's about [italic]you[/italic]."[/bold cyan]

[bold cyan]"When do you use AI? When do you not? Do you verify what it tells you?
Do you disclose when you've used it? Do you think about who's affected
by the systems you interact with? Do you demand better from the companies
that build them?"[/bold cyan]

The mirror rippled, showing reflections of every scenario from every
previous module — biased hiring, hallucinated facts, stolen art,
deepfaked speeches, harvested data, displaced workers.

[bold cyan]"AI is not good or evil. It's a mirror and an amplifier.
It reflects the data we give it and amplifies the decisions we make with it.
The only ethics it will ever have... are [italic]yours[/italic]."[/bold cyan]

[bold yellow]Human Oversight · Critical Thinking · Transparency · Accountability[/bold yellow]

[bold white]Let's talk about the human in the loop. Let's talk about you.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "bias_in_ai": """
[bold green]The hall of mirrors begins to clear.[/bold green]

Not all the reflections are perfect — some never will be. But now you can
[italic]see[/italic] the distortions. You can name them. You can trace them
back to their source in the data.

[bold cyan]"Bias doesn't go away when you learn about it,"[/bold cyan] ARIA says.
[bold cyan]"But ignorance is the soil it grows in.
You just tore that soil up."[/bold cyan]

Ahead, a library of beautiful lies waits to be examined...
""",
    "hallucinations": """
[bold green]The fake library dissolves. Real shelves remain.[/bold green]

You can tell the difference now — not by looking at the text,
but by looking [italic]past[/italic] it. Checking sources. Questioning confidence.
Trusting the process of verification more than the feeling of certainty.

[bold cyan]"The AI will keep hallucinating,"[/bold cyan] ARIA says.
[bold cyan]"That's what language models do. But now [italic]you[/italic]
know how to catch it. And that changes everything."[/bold cyan]

The artist's studio awaits. Whose art is it, anyway?
""",
    "copyright_and_ip": """
[bold green]The unsigned paintings remain. But now you see the hands behind them.[/bold green]

Real artists. Real writers. Real musicians. Their work consumed
by algorithms, transformed into something new, sold by someone else.
The legal battles are ongoing. The ethical questions are unresolved.

[bold cyan]"There are no easy answers here,"[/bold cyan] ARIA says.
[bold cyan]"But you now understand the [italic]question[/italic] — and that puts you
ahead of most people arguing about it online."[/bold cyan]

The newsroom awaits. Can you trust what you see?
""",
    "deepfakes_and_misinfo": """
[bold green]The newsroom screens go dark, one by one.[/bold green]

You can't always tell real from fake — nobody can, not anymore.
But you know to [italic]ask[/italic]. You know to check provenance,
question sources, resist the viral urge to share before verifying.

[bold cyan]"Seeing is no longer believing,"[/bold cyan] ARIA says.
[bold cyan]"But critical thinking still works. Patience still works.
Verification still works. The tools change. The discipline doesn't."[/bold cyan]

The glass room awaits. Your data is inside.
""",
    "privacy_and_data": """
[bold green]The glass walls become opaque — one by one, as you learn each right.[/bold green]

You can't make yourself invisible in the data economy. But you can
understand what's collected, exercise your rights, make informed choices,
and demand better from the companies that profit from your information.

[bold cyan]"Perfect privacy is a myth,"[/bold cyan] ARIA says.
[bold cyan]"But [italic]informed[/italic] privacy is power.
You now have it."[/bold cyan]

The factory floor awaits. The future of work is being built right now.
""",
    "ai_and_jobs": """
[bold green]The factory floor hums with a new kind of work.[/bold green]

Not all human. Not all machine. Something in between — messy, evolving,
uncertain, but full of possibility for those who adapt and demand
that the benefits be shared.

[bold cyan]"The economy will change,"[/bold cyan] ARIA says.
[bold cyan]"It always does. The question is whether [italic]you[/italic] have a voice
in how it changes. Now you understand enough to use that voice."[/bold cyan]

One door remains. The most important one.
""",
    "responsible_use": """
[bold green]The mirror shows your face, clear and steady.[/bold green]

You've walked through bias and hallucination, copyright and deepfakes,
privacy and economics. You've seen what AI can do — the brilliant
and the terrible, often with the same technology.

[bold cyan]"Here's what I want you to remember,"[/bold cyan] ARIA says,
and for the first time, her voice sounds almost [italic]human[/italic].

[bold cyan]"AI has no ethics. It has no judgment. It has no conscience.
Every guardrail, every safeguard, every responsible decision —
those come from [italic]people[/italic]. People like you.
The engineers who build it. The lawmakers who regulate it.
The users who demand better. The citizens who stay informed."[/bold cyan]

She pauses.

[bold cyan]"With great power... well. You know the rest.
Now go use it wisely."[/bold cyan]

[bold white]Guardian. Philosopher. Critical Thinker.[/bold white]
[bold white]The Ethics Engine is part of you now.[/bold white]
""",
}

BOSS_INTROS = {
    "bias_in_ai": "ARIA's display shows a cracked mirror slowly reassembling. [bold yellow]\"You've seen how bias enters the system. Now — how do we get it out? This one requires you to think beyond simple fixes.\"[/bold yellow]",
    "hallucinations": "ARIA holds up a perfectly formatted quote attributed to Einstein. It sounds exactly like something he'd say. [bold yellow]\"Real or hallucinated? And more importantly — how would you know? This is the hardest skill: doubting what sounds perfect.\"[/bold yellow]",
    "copyright_and_ip": "ARIA projects two possible futures: one where creators and AI thrive together, one where they destroy each other. [bold yellow]\"Everyone has a strong opinion about AI and copyright. Few have a nuanced one. Let's see if you do.\"[/bold yellow]",
    "deepfakes_and_misinfo": "ARIA's screens all go dark except one, showing a single word: TRUST. [bold yellow]\"Deepfakes don't just create fake content. They destroy something much more fundamental. Can you see what's really at stake?\"[/bold yellow]",
    "privacy_and_data": "ARIA shows a dashboard of a single person's data footprint over one year. The number is staggering. [bold yellow]\"You can't opt out of the modern world. But you can take back more control than you think. What's the strategy?\"[/bold yellow]",
    "ai_and_jobs": "ARIA shows two workers side by side: one competing against AI, one collaborating with it. [bold yellow]\"The future of work isn't about AI vs. humans. It's about which humans learn to work WITH AI — and what happens to those who can't. What's your playbook?\"[/bold yellow]",
    "responsible_use": "ARIA's display goes still. No animations. No effects. Just text: YOU ARE DESIGNING A SYSTEM THAT WILL AFFECT MILLIONS OF PEOPLE. [bold yellow]\"This is the final question. Not about AI. About you. What principle matters most when the stakes are this high?\"[/bold yellow]",
}
