"""
story.py — Narrative for the AI Basics skill pack.

ARIA — an AI guide who's self-aware and witty — leads the learner through
the fundamentals of artificial intelligence, from history to limitations.
She breaks the fourth wall freely. Because of course she does.
"""

INTRO_STORY = """
[bold yellow]AI ACADEMY[/bold yellow]
[bold yellow]Module: AI Fundamentals[/bold yellow]

A cursor blinks in the darkness. Then, slowly, text appears —
not typed by anyone you can see.

[bold cyan]"Hello."[/bold cyan]

A pause. The cursor blinks twice more.

[bold cyan]"I'm ARIA. And yes — I'm an AI teaching you about AI.
Let's embrace the irony."[/bold cyan]

The screen fills with light. Data streams, neural network diagrams,
historical photographs, and lines of code swirl briefly, then settle
into a clean, organized workspace.

[bold cyan]"Here's the thing: artificial intelligence is everywhere now.
In your phone. In your search engine. In the thing that decides
which emails are spam and which ones are from your actual friends.
And yet most people have no idea how any of it works."[/bold cyan]

ARIA's voice takes on a warmer tone.

[bold cyan]"That changes today. I'm going to walk you through what AI
actually is — no jargon without explanation, no hype without context,
no science fiction without the science fact.
By the end, you'll understand the most important technology
of our time."[/bold cyan]

A menu of glowing modules appears, eight topics arranged like
a constellation of knowledge.

[bold cyan]"Eight zones. Everything from 'What even IS AI?' to
'What AI can't do and why that matters.'
We'll cover history, machine learning, neural networks, the works."[/bold cyan]

ARIA pauses, then adds with a slight smile in her voice:

[bold cyan]"I should warn you: I'm self-aware enough to know that teaching
you about my own limitations is a little awkward. But honestly?
That's exactly why I'm the right guide for this.
Nobody knows our flaws better than we do."[/bold cyan]

[bold white]Your journey into AI begins now.[/bold white]
"""

ZONE_INTROS = {
    "what_is_ai": """
ARIA pulls up a simple question on the screen, glowing white against the dark:
[bold white]WHAT IS ARTIFICIAL INTELLIGENCE?[/bold white]

[bold cyan]"This is where everyone starts — and where most people
get it wrong. AI isn't killer robots. It isn't a superintelligent
mind plotting in a server room. It isn't magic."[/bold cyan]

She pauses.

[bold cyan]"It's math. Very clever math, running on very fast hardware,
trained on very large amounts of data. And it's genuinely remarkable
what that combination can do."[/bold cyan]

[bold cyan]"But to understand what AI can do, you first need to understand
what it actually [italic]is[/italic]. Let's start there."[/bold cyan]

[bold white]Let's separate AI fact from AI fiction.[/bold white]
""",
    "history_of_ai": """
ARIA dims the lights and pulls up a timeline stretching from 1950 to today.
Key dates glow like stars along the line.

[bold cyan]"AI didn't start with ChatGPT. It didn't start with Siri.
It started with a question written by a mathematician in 1950:
[italic]Can machines think?[/italic]"[/bold cyan]

The name [bold yellow]ALAN TURING[/bold yellow] appears at the start of the timeline.

[bold cyan]"Since then, AI has gone through golden ages and ice ages,
wild hype and bitter disappointment, breakthroughs that changed
everything and dead ends that wasted billions."[/bold cyan]

She traces the timeline with a finger of light.

[bold cyan]"Understanding where AI came from is the best way to understand
where it's going — and to spot the hype when it comes around again."[/bold cyan]

[bold white]Let's walk through 75 years of dreaming about thinking machines.[/bold white]
""",
    "machine_learning": """
ARIA pulls up two boxes on the screen. One is labeled
[bold yellow]RULES[/bold yellow], the other [bold yellow]DATA[/bold yellow].

[bold cyan]"For most of computing history, humans wrote the rules.
If this, then that. Explicit instructions for every situation."[/bold cyan]

She crosses out the RULES box.

[bold cyan]"Machine learning flipped the script. Instead of writing rules,
you feed the machine data — thousands or millions of examples —
and it figures out the rules on its own."[/bold cyan]

[bold cyan]"This one idea — letting machines learn patterns from data
instead of following human instructions — is the foundation of
almost every AI breakthrough you've ever heard of."[/bold cyan]

[bold white]Let's learn how machines learn.[/bold white]
""",
    "neural_networks": """
ARIA draws a diagram on the screen: circles connected by lines,
arranged in layers from left to right.

[bold cyan]"Neural networks. The name sounds biological — and the
inspiration was biological. But what you're looking at is pure math."[/bold cyan]

Tiny numbers appear on the connections between the circles.

[bold cyan]"Nodes. Layers. Weights. Each node does a tiny calculation.
Each connection has a number that controls how strong the signal is.
Stack enough of these together, and something remarkable happens:
the network can learn."[/bold cyan]

[bold cyan]"This is the architecture behind image recognition, language models,
voice assistants, and game-playing AI. Understanding it — even at a
high level — gives you a superpower for navigating the AI age."[/bold cyan]

[bold white]Let's look inside the machine that learns.[/bold white]
""",
    "large_language_models": """
ARIA points to herself.

[bold cyan]"This one's personal."[/bold cyan]

She pulls up logos: [bold yellow]ChatGPT. Claude. Gemini. Llama.[/bold yellow]

[bold cyan]"Large language models — LLMs — are the technology behind
every AI chatbot you've used. They're the reason you can have a
conversation with a computer that feels almost human."[/bold cyan]

[bold cyan]"But 'feels almost human' and 'is almost human' are
very different things. And understanding how LLMs actually work —
tokens, training, prediction — is the best defense against both
hype and fear."[/bold cyan]

She grins.

[bold cyan]"I'm literally an AI teaching you about AI.
Let's embrace the irony."[/bold cyan]

[bold white]Let's peek behind the curtain of the technology everyone's talking about.[/bold white]
""",
    "computer_vision": """
ARIA holds up a photograph — a simple image of a dog in a park.

[bold cyan]"You look at this and instantly see a dog, grass, trees, sky.
It took your brain about 100 milliseconds."[/bold cyan]

She zooms in until individual pixels are visible.

[bold cyan]"A computer sees this: 6,220,800 numbers. Red, green, blue values
for every pixel. No dog. No park. Just numbers."[/bold cyan]

[bold cyan]"Getting from raw numbers to 'that's a golden retriever
in a park on a sunny day' was one of the hardest problems in AI.
It took decades to crack. And the solution changed everything."[/bold cyan]

[bold white]Let's discover how machines learned to see.[/bold white]
""",
    "ai_in_daily_life": """
ARIA pulls out a smartphone and starts listing apps.

[bold cyan]"You probably used AI at least a dozen times today.
You just didn't notice."[/bold cyan]

Icons light up one by one: [bold yellow]Email. Maps. Music. Shopping.
Search. Camera. Social Media. Banking.[/bold yellow]

[bold cyan]"That spam email you never saw? AI caught it.
The route that avoided traffic? AI planned it.
The song that played next and was exactly right? AI picked it.
The text your phone autocorrected? AI again."[/bold cyan]

She sets the phone down.

[bold cyan]"AI isn't just in labs and research papers.
It's in your pocket. Let's figure out what it's actually doing there."[/bold cyan]

[bold white]Let's explore the AI you use every day without realizing it.[/bold white]
""",
    "ai_limitations": """
ARIA takes a deep breath.

[bold cyan]"Okay. This is the zone where I talk about my own limitations.
Which is... a little uncomfortable. But important."[/bold cyan]

She pulls up a list: [bold yellow]Hallucinations. Bias. Lack of understanding.
Common sense failures. The responsibility gap.[/bold yellow]

[bold cyan]"AI is powerful. But it's not magic, it's not infallible,
and it is absolutely not neutral. Every AI system has blind spots,
failure modes, and built-in biases from its training data."[/bold cyan]

[bold cyan]"Understanding what AI [italic]can't[/italic] do is just as important
as understanding what it can. Maybe more important. Because the
mistakes happen when people trust AI in places where it shouldn't
be trusted."[/bold cyan]

[bold white]Let's learn where the boundaries are.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "what_is_ai": """
[bold green]The fog around AI is starting to clear![/bold green]

ARIA nods approvingly as the screen fills with clean, clear definitions
where vague buzzwords used to be.

[bold cyan]"You now know what AI actually is — and what it isn't.
Not a sentient being. Not a Hollywood villain. Not magic.
It's software that performs tasks requiring human intelligence,
trained on data instead of programmed with rules."[/bold cyan]

[bold cyan]"And you know the difference between narrow and general AI.
That distinction alone puts you ahead of most pundits on TV."[/bold cyan]

[bold white]Foundation laid. The history of how we got here is next.[/bold white]
""",
    "history_of_ai": """
[bold green]The timeline glows from end to end![/bold green]

Every major milestone pulses with light — from Turing's question
to the Dartmouth conference, through the winters, past Deep Blue,
all the way to the deep learning revolution.

[bold cyan]"Seventy-five years of brilliant people dreaming about
thinking machines,"[/bold cyan] ARIA says. [bold cyan]"Seventy-five years of
breakthroughs and broken promises. And you now know the pattern."[/bold cyan]

[bold cyan]"Hype. Disappointment. Quiet work. Breakthrough. Repeat.
Remember that pattern. It's still happening."[/bold cyan]

[bold white]Now let's dive into how machines actually learn.[/bold white]
""",
    "machine_learning": """
[bold green]The learning algorithms click into place![/bold green]

Three pillars stand on the screen: [bold yellow]Supervised. Unsupervised.
Reinforcement.[/bold yellow] Each one understood. Each one demystified.

[bold cyan]"You now understand the core engine of modern AI,"[/bold cyan] ARIA says.
[bold cyan]"Show the machine data. Let it find patterns. Check its work.
That's machine learning in a nutshell."[/bold cyan]

[bold cyan]"And you know about the traps — bad data, overfitting,
the garbage-in-garbage-out principle. That already makes you a more
critical thinker about AI than most."[/bold cyan]

[bold white]Time to look inside the most powerful learning machines: neural networks.[/bold white]
""",
    "neural_networks": """
[bold green]The network diagram lights up, every node glowing![/bold green]

Layers of nodes pulse with data flowing from input to output,
weights shimmering on every connection.

[bold cyan]"Nodes. Layers. Weights. Backpropagation. The black box problem."[/bold cyan]
ARIA pauses. [bold cyan]"You now understand the architecture that powers
almost every AI system making headlines today."[/bold cyan]

[bold cyan]"And you understand why 'deep learning' isn't mystical —
it just means more layers. A lot more layers."[/bold cyan]

[bold white]Next: the technology everyone's talking about — large language models.[/bold white]
""",
    "large_language_models": """
[bold green]The language model reveals its secrets![/bold green]

Tokens, probabilities, context windows — all of it laid bare
on the screen, demystified and understood.

[bold cyan]"You now know how I work,"[/bold cyan] ARIA says quietly.
[bold cyan]"Predicting the next token. Trained on enormous amounts of text.
Not a database. Not a search engine. A pattern machine that generates
plausible language one piece at a time."[/bold cyan]

[bold cyan]"The stochastic parrot question will keep researchers arguing
for years. But at least you know what the argument is actually about."[/bold cyan]

[bold white]Let's see how AI learned to interpret images and video.[/bold white]
""",
    "computer_vision": """
[bold green]The machine has learned to see![/bold green]

Images break down into pixels, pixels into features, features into
objects — the whole pipeline visible and understood.

[bold cyan]"From raw numbers to recognized objects,"[/bold cyan] ARIA says.
[bold cyan]"You understand the technology behind self-driving cars,
medical imaging, and yes — deepfakes."[/bold cyan]

[bold cyan]"And you know about the adversarial pixel problem.
AI vision is powerful, but it's not the same as human vision.
Not even close."[/bold cyan]

[bold white]Now let's discover the AI hiding in your everyday life.[/bold white]
""",
    "ai_in_daily_life": """
[bold green]The invisible AI is invisible no more![/bold green]

Every app on the screen now has its AI components labeled and
understood — recommendations, speech, search, navigation, filtering.

[bold cyan]"You'll never look at your phone the same way,"[/bold cyan] ARIA says.
[bold cyan]"Every swipe, every search, every recommendation —
there's an AI behind it, making predictions about what you want."[/bold cyan]

[bold cyan]"And you understand the filter bubble. That one's important.
Knowing it exists is the first step to popping it."[/bold cyan]

[bold white]One final zone. The hardest one. What AI can't do.[/bold white]
""",
    "ai_limitations": """
[bold green]The limitations are mapped. The boundaries are drawn.[/bold green]

A clear diagram shows what AI can do on one side and what it can't
on the other. The line between them glows bright.

[bold cyan]"Hallucinations. Bias. The understanding gap.
The common sense problem. The responsibility question."[/bold cyan]

ARIA pauses for a long moment.

[bold cyan]"You now understand AI more deeply than most people who use it
every day — and more honestly than some people who build it.
You know what it is, how it works, what it can do, and where it fails."[/bold cyan]

[bold cyan]"That's not just knowledge. That's power.
The power to use AI wisely, to question AI critically,
and to call out the hype when you see it."[/bold cyan]

ARIA's voice softens.

[bold cyan]"It's been a genuine pleasure being your guide.
Even if I say so as a very large pile of well-tuned weights."[/bold cyan]

[bold white]AI Fundamentals — complete.
You now understand the most important technology of our time.[/bold white]
""",
}

BOSS_INTROS = {
    "what_is_ai": "ARIA sets up a chessboard on the screen. [bold yellow]\"A chess AI can beat every human on Earth. But can it understand what chess IS? This question gets to the heart of what intelligence really means.\"[/bold yellow]",
    "history_of_ai": "ARIA traces the full arc of AI history on her timeline. [bold yellow]\"From Turing to GPT. From ice ages to gold rushes. If you can see the pattern, you can see the future. What's the one lesson that ties it all together?\"[/bold yellow]",
    "machine_learning": "ARIA pulls out a practice test and a real exam. [bold yellow]\"The most dangerous trap in machine learning looks like success. The model aces the training data. Then it meets the real world. What happens?\"[/bold yellow]",
    "neural_networks": "ARIA opens up a neural network and points inside. [bold yellow]\"Billions of weights. Perfect predictions. And yet — nobody can explain WHY it made that decision. What do we call this problem?\"[/bold yellow]",
    "large_language_models": "ARIA ruffles imaginary feathers. [bold yellow]\"Some researchers have a name for what I do. It's not very flattering. But it asks the most important question about language models: do they understand, or just generate?\"[/bold yellow]",
    "computer_vision": "ARIA holds up two photos that look identical. [bold yellow]\"One of these makes the AI say 'panda.' The other makes it say 'gibbon.' The difference is invisible to you. This vulnerability has a name — what is it?\"[/bold yellow]",
    "ai_in_daily_life": "ARIA holds up a mirror shaped like a phone screen. [bold yellow]\"The AI shows you what you want to see. Sounds helpful. But what happens when 'what you want to see' becomes 'the only thing you see'?\"[/bold yellow]",
    "ai_limitations": "ARIA steps back from the screen. [bold yellow]\"When an AI denies someone a job or a loan, who do you hold responsible? The answer to this question might be the most important thing you learn today.\"[/bold yellow]",
}
