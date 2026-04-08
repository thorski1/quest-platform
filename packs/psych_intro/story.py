"""
story.py — Narrative for the Introduction to Psychology skill pack.

ARIA guides the learner through the neural architecture of the mind,
introducing psychology's foundations: its definition, research methods,
the brain, sensation and perception, and states of consciousness.
"""

INTRO_STORY = """
[bold yellow]PSYCHOLOGY 101[/bold yellow]
[bold yellow]Module: Introduction to Psychology[/bold yellow]

The neural lattice shimmered into view — billions of connections pulsing
with soft blue light, each node a thought, a memory, a question waiting
to be asked.

[bold cyan]"Welcome,"[/bold cyan] ARIA said, her voice resonating through the network.
[bold cyan]"You're standing inside a model of the human mind. Not a brain scan —
something deeper. A map of the questions humanity has been asking about
itself for thousands of years."[/bold cyan]

She gestured, and five chambers materialized along the neural pathways,
each glowing with a different frequency.

[bold cyan]"Psychology is the scientific study of mind and behavior. That sounds
simple. It isn't. The mind is the most complex object in the known
universe, and it's the one object that's trying to understand itself."[/bold cyan]

ARIA paused, letting the lattice pulse around you.

[bold cyan]"We'll start with the big picture — what psychology IS and where it
came from. Then we'll learn how psychologists actually test their ideas.
After that, we'll go inside the brain itself. Then we'll explore how
you perceive the world around you. And finally, we'll examine the
strangest thing of all — consciousness itself."[/bold cyan]

The five chambers hummed, each awaiting entry.

[bold cyan]"Five domains. Forty challenges. One question underneath them all:
what makes you... you?"[/bold cyan]

[bold white]The neural lattice is active. Enter when ready.[/bold white]
"""

ZONE_INTROS = {
    "what_is_psychology": """
The first chamber opened, revealing a timeline stretching from ancient
Greece to the present day. Philosophers, scientists, and clinicians
stood as holographic figures along its length.

[bold cyan]"Before psychology was a science, it was a question,"[/bold cyan] ARIA said.
[bold cyan]"Plato asked it. Aristotle argued about it. Descartes split the mind
from the body and spent the rest of his life trying to put them back
together."[/bold cyan]

She highlighted a date: 1879. Wilhelm Wundt. Leipzig, Germany.

[bold cyan]"This is where the question became a discipline. Wundt built the first
psychology laboratory and said: we're going to MEASURE the mind. Not
just philosophize about it. Measure it."[/bold cyan]

[bold yellow]Foundations · Perspectives · Key Figures · Modern Approaches[/bold yellow]

[bold white]Let's map the landscape of psychology.[/bold white]
""",
    "research_methods": """
The second chamber was a laboratory — gleaming, precise, full of
instruments designed to measure what most people thought couldn't
be measured.

[bold cyan]"Psychology's greatest challenge,"[/bold cyan] ARIA said, adjusting a simulated
experiment on the central display, [bold cyan]"is that its subject matter
lies, forgets, rationalizes, and changes its mind between Tuesday
and Thursday."[/bold cyan]

She smiled.

[bold cyan]"That's why the methods matter MORE in psychology than in almost
any other science. You can't just observe behavior and assume you
understand it. You have to design experiments that control for every
way the human mind tries to fool itself — and fool you."[/bold cyan]

[bold yellow]Scientific Method · Experiments · Correlation · Ethics · Bias[/bold yellow]

[bold white]Let's learn to think like a researcher.[/bold white]
""",
    "brain_nervous_system": """
The third chamber plunged you deep into biological architecture.
A massive holographic brain rotated slowly, its regions lighting up
in cascading waves of activity.

[bold cyan]"Everything you think, feel, remember, and decide happens here,"[/bold cyan]
ARIA said, pointing to the three-pound organ. [bold cyan]"One hundred billion
neurons, each connected to thousands of others. More connections than
stars in the Milky Way."[/bold cyan]

She zoomed in. A single neuron filled the chamber — dendrites reaching
out like the branches of a tree, an axon stretching into the distance.

[bold cyan]"The brain doesn't run on magic. It runs on electrochemistry.
Signals traveling at up to 268 miles per hour, jumping across synaptic
gaps with chemical messengers called neurotransmitters. Every thought
you've ever had was a pattern of these signals."[/bold cyan]

[bold yellow]Neurons · Neurotransmitters · Brain Regions · Nervous System[/bold yellow]

[bold white]Let's go inside the brain.[/bold white]
""",
    "sensation_perception": """
The fourth chamber was a sensory hall — light splitting into spectra,
sounds rippling as visible waves, textures generating data streams.

[bold cyan]"Your brain doesn't experience the world directly,"[/bold cyan] ARIA said.
[bold cyan]"It sits in a dark, silent box called your skull. Everything you
see, hear, taste, touch, and smell is a reconstruction — a model
your brain builds from electrical signals sent by your sensory organs."[/bold cyan]

She snapped her fingers. The room shifted — an optical illusion
filled the walls, impossible shapes folding through themselves.

[bold cyan]"Sensation is the raw data. Perception is the story your brain
tells about that data. And sometimes — often, actually — the story
is wrong. Beautifully, systematically, predictably wrong."[/bold cyan]

[bold yellow]Sensation · Perception · Vision · Illusions · Signal Detection[/bold yellow]

[bold white]Let's explore how you build reality from raw signal.[/bold white]
""",
    "states_of_consciousness": """
The fifth chamber was different. Quiet. Dreamlike. The neural lattice
here pulsed slowly, rhythmically — like breathing.

[bold cyan]"Consciousness,"[/bold cyan] ARIA said softly, [bold cyan]"is the hardest problem
in all of science. Not just psychology. All of science."[/bold cyan]

She dimmed the lights. Brain wave patterns scrolled across the walls —
beta, alpha, theta, delta — each representing a different state.

[bold cyan]"You spend a third of your life asleep. You dream for about two
hours every night. Your attention filters out 99% of what your senses
detect. You can be hypnotized, medicated, meditating, or in a flow
state — and each one changes what 'being conscious' means."[/bold cyan]

[bold yellow]Sleep · Dreams · Hypnosis · Psychoactive Substances · Meditation[/bold yellow]

[bold white]Let's explore the spectrum of awareness.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "what_is_psychology": """
[bold green]THE FOUNDATIONS — MAPPED.[/bold green]

From Wundt's laboratory to modern neuroscience, from behaviorism
to cognitive psychology, you've traced the arc of a discipline
that dared to turn the scientific method inward.

Psychology isn't one thing. It's a family of approaches — biological,
cognitive, behavioral, psychodynamic, humanistic, sociocultural —
each illuminating a different facet of the same endlessly complex
subject: you.

[bold cyan]The Research Methods lab is next. Time to learn how
psychologists separate truth from intuition.[/bold cyan]
""",
    "research_methods": """
[bold green]RESEARCH METHODS — MASTERED.[/bold green]

You can now distinguish correlation from causation, identify
confounding variables, recognize the importance of random assignment,
and understand why double-blind procedures exist.

The human mind is a magnificent self-deception engine. Research
methods are the tools psychologists built to outsmart it.

[bold cyan]The Brain awaits. Time to go from abstract methods
to concrete biology.[/bold cyan]
""",
    "brain_nervous_system": """
[bold green]THE BRAIN — NAVIGATED.[/bold green]

From the firing of a single neuron to the coordinated symphony
of the cerebral cortex, you've mapped the biological machinery
that produces every thought, feeling, and behavior.

One hundred billion neurons. Trillions of connections. Three pounds
of electrochemical computation running the most sophisticated
information-processing system in the known universe.

[bold cyan]Sensation and Perception are next. Time to explore
how the brain builds reality from raw data.[/bold cyan]
""",
    "sensation_perception": """
[bold green]SENSATION & PERCEPTION — DECODED.[/bold green]

You understand the difference between raw sensory data and the
perceptual models your brain constructs from it. You know why
illusions work, how signal detection theory applies to real life,
and why your brain fills in gaps you never notice.

The world you experience is a controlled hallucination,
updated in real time by incoming data. Perception is not
passive reception — it's active construction.

[bold cyan]One domain remains: consciousness itself.
The deepest question in psychology.[/bold cyan]
""",
    "states_of_consciousness": """
[bold yellow]★ ★ ★  CONSCIOUSNESS — EXPLORED.  ★ ★ ★[/bold yellow]

[bold white]You've completed the Introduction to Psychology.[/bold white]

From the birth of the discipline to the hard problem of consciousness,
you've surveyed the fundamental questions that drive psychological
science. You know how psychologists think, how they test, what the
brain does, how perception works, and why consciousness remains
the deepest mystery of all.

[bold magenta]The mind is the most complex object in the known universe.
And now you have a map.[/bold magenta]

[bold yellow]STATUS: FOUNDATIONS COMPLETE.[/bold yellow]
""",
}

BOSS_INTROS = {
    "what_is_psychology": "[bold red]⚠  SYNTHESIS CHALLENGE: The Perspectives Gauntlet[/bold red]\nARIA has one final question — it requires you to integrate everything you've learned about psychology's major perspectives.",
    "research_methods": "[bold red]⚠  METHODOLOGY CHALLENGE: The Experimental Design Trial[/bold red]\nA complex scenario that tests your ability to identify proper experimental methodology and recognize flaws.",
    "brain_nervous_system": "[bold red]⚠  NEUROSCIENCE CHALLENGE: The Neural Architecture Test[/bold red]\nThe brain is complex. This challenge requires you to connect structure to function across multiple systems.",
    "sensation_perception": "[bold red]⚠  PERCEPTION CHALLENGE: The Illusion Gauntlet[/bold red]\nYour perceptual system is about to be tested. Can you explain WHY your brain makes systematic errors?",
    "states_of_consciousness": "[bold red]★  FINAL CHALLENGE: The Consciousness Synthesis[/bold red]\nThe hardest question in psychology. Integrate everything — sleep, dreams, attention, awareness — into one answer.",
}
