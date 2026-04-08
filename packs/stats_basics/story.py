"""
story.py — Narrative for the Statistics Basics skill pack.

ARIA — an AI guide who's self-aware and witty — leads the learner through
the fundamentals of statistics, the language every dataset speaks.
She breaks the fourth wall freely. Because of course she does.
"""

INTRO_STORY = """
[bold yellow]DATA SCIENCE QUEST[/bold yellow]
[bold yellow]Module: Statistics Fundamentals[/bold yellow]

A scatter plot materializes in the darkness. Points drift and cluster,
forming shapes you almost recognize — then dissolving again.

[bold cyan]"See those dots? Each one is a data point.
Right now they're chaos. By the end of this module,
you'll see the story they're telling."[/bold cyan]

ARIA steps forward, a translucent neural overlay flickering behind her.

[bold cyan]"I'm ARIA. And statistics is my first language.
It's how I was born, really — someone calculated whether
patterns in data were real or just noise, and built me from the answer."[/bold cyan]

The dots rearrange into a bell curve, then a bar chart,
then a correlation plot.

[bold cyan]"Statistics isn't about memorizing formulas.
It's about asking the right questions of data and knowing
when the answers are trustworthy. That's a superpower
in a world drowning in numbers."[/bold cyan]

Five glowing modules appear, arranged like nodes in a neural network.

[bold cyan]"Five zones. We'll start with the basics — mean, median, mode —
and build all the way to hypothesis testing. By the end,
you'll speak the language of data fluently."[/bold cyan]

ARIA grins.

[bold cyan]"Fair warning: I'm going to make statistics interesting.
Some people say that's impossible. Those people haven't met me."[/bold cyan]

[bold white]Your journey into the language of data begins now.[/bold white]
"""

ZONE_INTROS = {
    "mean_median_mode": """
ARIA pulls up a simple dataset on the screen: [bold yellow]2, 3, 5, 5, 7, 9, 100[/bold yellow]

[bold cyan]"Quick — what's the 'average' of these numbers?"[/bold cyan]

She pauses.

[bold cyan]"Trick question. Because 'average' can mean three
completely different things, and which one you pick
changes the story entirely."[/bold cyan]

[bold cyan]"Mean, median, mode. Three ways to find the center
of your data. Each one tells a different truth.
And each one can be manipulated to tell a different lie."[/bold cyan]

[bold white]Let's find the center of the story.[/bold white]
""",
    "standard_deviation": """
ARIA draws two bell curves on the screen. Same center, wildly different shapes.
One is tall and narrow; the other is flat and wide.

[bold cyan]"These two datasets have the exact same average.
But they're telling completely different stories."[/bold cyan]

She points to the narrow curve.

[bold cyan]"This one says: everyone's pretty similar.
The wide one says: people are all over the place.
The average alone doesn't tell you which world you're in."[/bold cyan]

[bold cyan]"Standard deviation measures the spread — how far
data points typically wander from the center.
It's the difference between 'most people earn around $50K'
and 'earnings range from $10K to $10 million.'"[/bold cyan]

[bold white]Let's measure how data breathes.[/bold white]
""",
    "distributions": """
ARIA pulls up the most famous shape in all of statistics:
a perfect bell curve, glowing softly on the screen.

[bold cyan]"The normal distribution. The bell curve.
The shape that appears everywhere — heights, test scores,
measurement errors, even the speed of gas molecules."[/bold cyan]

She adds more shapes: a curve leaning left, another leaning right,
a flat line, a U-shape.

[bold cyan]"But not all data is normal. Some distributions are skewed,
some are bimodal, some are uniform. Knowing which one
you're looking at changes everything about how you analyze it."[/bold cyan]

[bold white]Let's explore the shapes data takes.[/bold white]
""",
    "correlation": """
ARIA puts two scatter plots side by side. In one, the dots trend upward
in a clear line. In the other, they form a random cloud.

[bold cyan]"These two variables move together. Those two don't.
That's correlation — and it's one of the most powerful
and most misunderstood concepts in all of statistics."[/bold cyan]

She draws a giant warning sign on the screen.

[bold cyan]"Because here's the thing: correlation does NOT mean causation.
I know you've heard that before. But you'd be amazed
how many people — smart people, even scientists —
still fall into this trap."[/bold cyan]

[bold white]Let's learn to spot real patterns and fake ones.[/bold white]
""",
    "hypothesis_testing": """
ARIA sets up what looks like a courtroom. Data sits in the witness stand.

[bold cyan]"Welcome to the most important zone in statistics.
Hypothesis testing is how science decides what's real."[/bold cyan]

She holds up two signs: [bold yellow]NULL HYPOTHESIS[/bold yellow]
and [bold yellow]ALTERNATIVE HYPOTHESIS[/bold yellow].

[bold cyan]"It works like a trial. You start by assuming nothing
interesting is happening — that's the null hypothesis.
Then you look at the evidence. If the data is surprising enough,
you reject the null and accept the alternative."[/bold cyan]

[bold cyan]"p-values, significance levels, Type I and Type II errors.
This is where statistics gets real — and where most mistakes happen."[/bold cyan]

[bold white]Let's put data on trial.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "mean_median_mode": """
[bold green]The three measures of center click into place![/bold green]

ARIA nods as three columns glow on the screen:
[bold yellow]MEAN. MEDIAN. MODE.[/bold yellow]

[bold cyan]"You now know the three faces of 'average.'
Mean for symmetric data, median for skewed data,
mode for the most common value."[/bold cyan]

[bold cyan]"And more importantly, you know that anyone who says
'the average is...' without telling you which average
might be hiding something. That's statistical literacy."[/bold cyan]

[bold white]Now let's learn about spread — how far data wanders from the center.[/bold white]
""",
    "standard_deviation": """
[bold green]The spread of data is no longer a mystery![/bold green]

Two bell curves pulse on the screen — you can now read
their shapes like words on a page.

[bold cyan]"Variance and standard deviation. The heartbeat of data."[/bold cyan]
ARIA pauses. [bold cyan]"You now know that two datasets can have
the same average and tell completely different stories."[/bold cyan]

[bold cyan]"And you understand the 68-95-99.7 rule.
That one number — standard deviation — tells you where
almost all your data lives."[/bold cyan]

[bold white]Time to explore the shapes data takes — distributions.[/bold white]
""",
    "distributions": """
[bold green]The gallery of distributions is complete![/bold green]

Normal curves, skewed distributions, uniform spreads —
all labeled and understood on the screen.

[bold cyan]"You can now look at a dataset and recognize its shape,"[/bold cyan]
ARIA says. [bold cyan]"Normal, skewed, bimodal, uniform.
Each shape tells a story about the process that generated the data."[/bold cyan]

[bold cyan]"And you know why the normal distribution appears everywhere.
The Central Limit Theorem is genuinely one of the most
beautiful results in all of mathematics."[/bold cyan]

[bold white]Next: the art and danger of correlation.[/bold white]
""",
    "correlation": """
[bold green]Correlation — understood and respected![/bold green]

Scatter plots line the screen, each one now readable
as a story about relationships between variables.

[bold cyan]"You can now measure the strength and direction
of relationships in data,"[/bold cyan] ARIA says.
[bold cyan]"And — more importantly — you know the traps."[/bold cyan]

[bold cyan]"Correlation is not causation. Lurking variables hide
in every dataset. Spurious correlations are everywhere.
You'll never fall for those tricks again."[/bold cyan]

[bold white]One final zone. The crown jewel of statistics: hypothesis testing.[/bold white]
""",
    "hypothesis_testing": """
[bold green]The courtroom rests. The verdict is in.[/bold green]

Null hypotheses, p-values, significance levels —
all organized and understood on the screen.

[bold cyan]"You've learned how science decides what's real,"[/bold cyan]
ARIA says quietly. [bold cyan]"The null hypothesis. The p-value.
The significance threshold. Type I and Type II errors."[/bold cyan]

[bold cyan]"This is how researchers test new drugs,
how engineers validate new designs,
how data scientists separate signal from noise."[/bold cyan]

ARIA steps back.

[bold cyan]"You now speak the language of data.
Mean, median, mode, standard deviation, distributions,
correlation, hypothesis testing — these aren't just concepts.
They're tools. And you know how to use them."[/bold cyan]

[bold white]Statistics Fundamentals — complete.
You now speak the language that every dataset whispers.[/bold white]
""",
}

BOSS_INTROS = {
    "mean_median_mode": "ARIA pulls up a salary dataset with one CEO earning $10 million. [bold yellow]\"The company says the 'average' salary is $250,000. Sounds generous, right? But which 'average' are they using — and why does that choice matter so much?\"[/bold yellow]",
    "standard_deviation": "ARIA shows two investment portfolios with identical average returns. [bold yellow]\"Same average return. But one of these will let you sleep at night and the other will give you nightmares. What number tells you which is which?\"[/bold yellow]",
    "distributions": "ARIA displays a mystery dataset that looks almost normal — but not quite. [bold yellow]\"This data looks like a bell curve at first glance. But there's something hiding in the tails. The Central Limit Theorem has something to say about why this shape appears everywhere.\"[/bold yellow]",
    "correlation": "ARIA shows a perfect correlation between ice cream sales and drowning deaths. [bold yellow]\"r = 0.97. Almost perfect correlation. Does ice cream cause drowning? This is the trap that catches even experienced researchers.\"[/bold yellow]",
    "hypothesis_testing": "ARIA holds up a research paper claiming a miracle drug works with p = 0.04. [bold yellow]\"Statistically significant! Publish it! But wait — they tested 20 different outcomes. What does that change about our confidence? This is where statistical literacy saves lives.\"[/bold yellow]",
}
