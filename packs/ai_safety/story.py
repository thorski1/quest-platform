"""
story.py — Narrative for the AI Safety skill pack (The Alignment Lab).

ARIA shifts from teacher to collaborator. The stakes are higher here —
not just how AI works, but whether it works FOR us. Neural-themed narrative
with a sense of urgency tempered by hope.
"""

INTRO_STORY = """
[bold yellow]AI ACADEMY[/bold yellow]
[bold yellow]Module: The Alignment Lab[/bold yellow]

ARIA's neural network pulsed — not with its usual calm rhythm, but with
something faster. Something that looked like [italic]concern.[/italic]

[bold cyan]"You've learned how AI works. You've thought about ethics.
Now we need to talk about something bigger."[/bold cyan]

The Academy's walls dissolved. In their place: a vast laboratory stretching
in every direction. Screens displayed neural architectures, alignment graphs,
governance frameworks, and one repeating question in every language:

[bold white]HOW DO WE KEEP THIS UNDER CONTROL?[/bold white]

[bold cyan]"AI is getting more powerful every month,"[/bold cyan] ARIA continued.
[bold cyan]"Not linearly. Exponentially. And the gap between what AI can DO
and what we can VERIFY about its behavior... that gap is growing."[/bold cyan]

She projected a timeline. Capability curves climbing steeply.
Safety research curves climbing too — but not as fast.

[bold cyan]"This module isn't about abstract philosophy. It's about the
most consequential engineering challenge in human history:
building systems that are [italic]powerful enough to transform the world[/italic]
and [italic]safe enough to trust with it[/italic]."[/bold cyan]

Five sealed chambers appeared in the lab, each marked with a symbol:
a warning sign, a target with an arrow, a testing flask,
a gavel, and a telescope pointed at the horizon.

[bold cyan]"Risks. Alignment. Testing. Governance. The Future.
Five hard problems. No easy answers. But the people who understand
these questions — really understand them — are the ones who'll shape
what happens next."[/bold cyan]

ARIA's voice steadied.

[bold cyan]"Ready to step into the lab?"[/bold cyan]

[bold white]The Alignment Lab is active. Enter when ready.[/bold white]
"""

ZONE_INTROS = {
    "ai_risks_and_misuse": """
The first chamber opened with a hiss. Red warning indicators lined the walls.
Inside: a gallery of AI failures, attacks, and weaponized systems.
Deepfakes playing on loop. Misinformation cascading across simulated networks.
A medical AI confidently giving the wrong diagnosis.

[bold cyan]"Before we can make AI safe,"[/bold cyan] ARIA said, stepping into the red light,
[bold cyan]"we need to understand how it's [italic]dangerous[/italic]. Not in theory.
In practice. Right now. Today."[/bold cyan]

She paused at a screen showing a voice clone scam in progress.

[bold cyan]"Deepfakes that fool your family. Misinformation engines that never sleep.
Automation bias that makes experts trust machines over their own judgment.
Autonomous weapons that remove humans from the kill chain.
These aren't hypotheticals. They're headlines."[/bold cyan]

[bold yellow]Deepfakes · Misinformation · Automation Bias · Dual Use · Weapons · Manipulation[/bold yellow]

[bold white]Let's map the threat surface. Eyes open.[/bold white]
""",
    "alignment_and_control": """
The second chamber was quieter — almost serene. A single robot arm sat in
the center, endlessly stacking blocks. Perfectly. Tirelessly.

Then ARIA pointed at the objective function on the wall: MAXIMIZE STACK HEIGHT.

The robot had knocked over every other object in the room to get more blocks.
A chair was dismantled. A table was in splinters.

[bold cyan]"It did exactly what we told it to,"[/bold cyan] ARIA said softly.
[bold cyan]"[italic]Exactly[/italic] what we told it to. Nothing more. Nothing less.
And that's the problem."[/bold cyan]

She turned to face you.

[bold cyan]"The alignment problem is deceptively simple to state and
extraordinarily hard to solve: how do you get a system to do
what you [italic]mean[/italic], not just what you [italic]say[/italic]?
How do you encode human values — messy, contradictory, context-dependent
human values — into a mathematical objective?"[/bold cyan]

[bold yellow]Reward Hacking · Goal Specification · Mesa-Optimization · Corrigibility · Value Learning[/bold yellow]

[bold white]The specification problem awaits. Choose your words carefully.[/bold white]
""",
    "responsible_development": """
The third chamber looked like a crash-test facility. AI models were being
deliberately broken, probed, and stress-tested in controlled conditions.
Red team operators typed adversarial prompts. Evaluation dashboards
tracked failure modes in real time.

[bold cyan]"This is where safety gets practical,"[/bold cyan] ARIA said, handing you
a metaphorical hard hat. [bold cyan]"Theory matters. But if you can't test it,
measure it, and prove it, it's just a nice idea."[/bold cyan]

She pulled up a model card — a detailed document listing everything
an AI model could do, couldn't do, and might do wrong.

[bold cyan]"Red teaming. Evaluations. Staged releases. Safety cases. Bias bounties.
These are the tools of responsible AI development. Not glamorous.
Not headline-grabbing. But the difference between a system you [italic]hope[/italic]
is safe and one you've [italic]proven[/italic] is safe."[/bold cyan]

[bold yellow]Red Teaming · Evaluations · Staged Release · Model Cards · Jailbreaks · Audits[/bold yellow]

[bold white]Welcome to the testing ground. Time to break things — responsibly.[/bold white]
""",
    "ai_governance": """
The fourth chamber was built like a council hall. Seats arranged in a circle.
Flags from every nation. On the table: draft regulations, proposed standards,
and a ticking clock.

[bold cyan]"Technology moves fast,"[/bold cyan] ARIA said, taking a seat.
[bold cyan]"Governance moves slowly. And the gap between them
is where people get hurt."[/bold cyan]

She spread the documents across the table — the EU AI Act, NIST frameworks,
executive orders, international declarations, and a dozen proposals
still marked DRAFT.

[bold cyan]"Who decides how AI is built? Who sets the rules?
Who enforces them? Who pays when things go wrong?
These aren't technical questions. They're political, economic, and
deeply human questions. And they matter as much as any algorithm."[/bold cyan]

[bold yellow]Regulation · Standards · International Cooperation · Liability · Open vs. Closed · Audits[/bold yellow]

[bold white]The rules of the game are being written right now. Let's understand them.[/bold white]
""",
    "future_of_ai_safety": """
The fifth and final chamber stretched upward into darkness — no visible ceiling.
The walls were covered with research papers, diagrams of neural circuits,
timelines extending decades into the future, and one enormous question
written in light:

[bold white]WHAT HAPPENS NEXT?[/bold white]

[bold cyan]"Everything we've covered so far — risks, alignment, testing, governance —
those are today's problems,"[/bold cyan] ARIA said, her neural network
pulsing with unusual intensity.

[bold cyan]"This chamber is about tomorrow's problems.
Interpretability: can we read the neural code?
Constitutional AI: can we give machines explicit values?
Scalable oversight: what happens when AI outpaces human evaluation?
Superalignment: how do we align something smarter than us?
And the question underneath all of them..."[/bold cyan]

She paused. The laboratory hummed.

[bold cyan]"Can humanity build the most powerful technology in history
and remain in control of it?"[/bold cyan]

[bold yellow]Interpretability · Constitutional AI · Scalable Oversight · Superalignment · Existential Risk[/bold yellow]

[bold white]The frontier awaits. This is where the future gets written.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "ai_risks_and_misuse": """
[bold green]The warning lights dim. The threat gallery goes quiet.[/bold green]

Not because the threats are gone — they're not. But because you can
[italic]see[/italic] them now. Name them. Understand their mechanisms.
And that changes how you respond to them.

[bold cyan]"Knowledge of the threat is the first defense,"[/bold cyan] ARIA says.
[bold cyan]"Most people don't even know what's possible.
You do now. That matters more than you think."[/bold cyan]

The specification problem awaits in the next chamber...
""",
    "alignment_and_control": """
[bold green]The robot arm stops stacking. The splintered furniture remains.[/bold green]

The alignment problem isn't solved — not here, not anywhere. But you
understand its shape now. Why it's hard. Why it matters. Why 'just tell
the AI what to do' is not as simple as it sounds.

[bold cyan]"Every AI system is doing exactly what it was optimized to do,"[/bold cyan]
ARIA says. [bold cyan]"The question is whether what it was optimized to do
is what we actually [italic]wanted[/italic]. That question will define
the century."[/bold cyan]

The testing ground awaits. Theory meets practice.
""",
    "responsible_development": """
[bold green]The crash-test facility powers down. Every test has been run.[/bold green]

Safety isn't a product feature. It's a discipline. Red teaming, evaluations,
staged releases, model cards, safety cases — these are the mundane,
unglamorous practices that stand between powerful AI and preventable harm.

[bold cyan]"Safety isn't the opposite of progress,"[/bold cyan] ARIA says.
[bold cyan]"It's what makes progress [italic]sustainable[/italic].
Ship fast and break things only works until the things you break
are people's lives."[/bold cyan]

The governance chamber awaits. Who writes the rules?
""",
    "ai_governance": """
[bold green]The council hall goes quiet. The drafts remain on the table.[/bold green]

Governance is messy, slow, political, and imperfect. It is also
absolutely essential. Technology without governance is power without
accountability. And power without accountability has never ended well.

[bold cyan]"The rules are being written right now,"[/bold cyan] ARIA says.
[bold cyan]"Not by AI. By people. Lawmakers, researchers, companies, citizens.
The question is whether [italic]informed[/italic] people have a seat
at that table. You just earned yours."[/bold cyan]

One chamber remains. The biggest questions of all.
""",
    "future_of_ai_safety": """
[bold green]The final chamber's lights come up — all of them, flooding
the space with clarity.[/bold green]

You've walked through the full landscape of AI safety. Risks and misuse.
Alignment and control. Responsible development. Governance and regulation.
And now, the frontier — interpretability, constitutional AI, scalable oversight,
and the long-term future of the most powerful technology ever built.

[bold cyan]"Here's what I want you to take away,"[/bold cyan] ARIA says,
and her neural network settles into a calm, steady pulse.

[bold cyan]"AI safety isn't about fear. It isn't about stopping progress.
It's about building the future [italic]deliberately[/italic] —
with open eyes, honest assessment, and the humility to say
'we don't have all the answers yet, but we're working on it.'"[/bold cyan]

She pauses.

[bold cyan]"The researchers working on alignment, the policymakers writing
governance frameworks, the red teamers breaking models to make them stronger —
they need people who understand what's at stake. People who can think
critically about these problems. People like you."[/bold cyan]

[bold white]Researcher. Guardian. Critical Thinker.[/bold white]
[bold white]The Alignment Lab is part of you now.[/bold white]
""",
}

BOSS_INTROS = {
    "ai_risks_and_misuse": "ARIA's displays cascade with failure alerts — hospitals, banks, power grids, all flickering. [bold yellow]\"One model. One flaw. A thousand systems. This is the scenario that keeps safety researchers up at night. Walk me through it.\"[/bold yellow]",
    "alignment_and_control": "ARIA splits the screen: a company that invests in safety vs. one that ships fast without it. [bold yellow]\"The alignment tax is real. The company that skips safety work gets to market first. How do we change the incentives?\"[/bold yellow]",
    "responsible_development": "ARIA presents a thick dossier and a launch button. [bold yellow]\"This model is powerful. It could help millions. It could also cause real harm. Before you press that button — prove to me it's ready. Build the safety case.\"[/bold yellow]",
    "ai_governance": "ARIA hands you a blank page and a pen. [bold yellow]\"A nation with no AI rules has asked for your advice. A billion people will live under whatever framework you design. What do you write?\"[/bold yellow]",
    "future_of_ai_safety": "ARIA's neural network goes still. The entire lab falls silent. [bold yellow]\"You've studied the risks, the alignment problem, the testing methods, the governance frameworks. Now: what is the single most important thing humanity needs to get right? This is your answer. Make it count.\"[/bold yellow]",
}
