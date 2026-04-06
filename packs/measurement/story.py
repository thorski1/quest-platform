"""
story.py — Narrative for the Measurement & Units skill pack.

Puck opens a glowing Measuring Workshop and guides the reader through
length, weight, volume, temperature, comparisons, tools, and real-world
measurements — everything can be counted and compared!
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Measuring Workshop[/bold yellow]

Puck appeared at the edge of a new page, carrying something odd —
a tiny golden ruler in one hand, a glowing thermometer in the other,
and a measuring cup balanced on top of one wing.

[bold cyan]"Today,"[/bold cyan] Puck announced, nearly dropping the thermometer,
[bold cyan]"we open the Measuring Workshop!"[/bold cyan]

The girl tilted her head. [bold white]"What's a measuring workshop?"[/bold white]

[bold cyan]"It's the place where you learn to answer the most important
questions in the world."[/bold cyan] Puck set each tool down carefully on
the page. [bold cyan]"How long? How heavy? How hot? How much?
How far? How fast?"[/bold cyan]

A workshop appeared on the page — shelves of rulers and scales,
rows of measuring cups and thermometers, a clock ticking on the wall,
and a giant number line stretching into the distance.

[bold cyan]"Everything in the world can be measured,"[/bold cyan] Puck said,
eyes twinkling. [bold cyan]"The height of a mountain. The weight of a
feather. The temperature of a star. And once you know how to measure
things — you understand them."[/bold cyan]

Puck picked up the little golden ruler and held it out.

[bold cyan]"Ready to measure the world?"[/bold cyan]

[bold white]Your adventure in measurement begins now.[/bold white]
"""

ZONE_INTROS = {
    "length": """
Puck pulled a golden ruler from the workshop shelf and held it up.

[bold cyan]"Length,"[/bold cyan] Puck said, [bold cyan]"is how long something is —
from one end to the other. We measure it in inches and feet,
or centimeters and meters. A bug is a few centimeters.
A basketball court is almost 29 meters. And the distance
to the Moon? About 384,400 kilometers!"[/bold cyan]

The ruler began to glow, stretching longer and longer across the page.

[bold white]Let's learn to measure how long things are![/bold white]
""",
    "weight": """
Puck flew over to a shining brass scale sitting on the workshop bench.

[bold cyan]"Weight,"[/bold cyan] Puck said, placing a tiny feather on one side,
[bold cyan]"is how heavy something is. A feather weighs less than a gram.
A watermelon weighs about ten pounds. And a blue whale?
Over three hundred thousand pounds!"[/bold cyan]

The scale tipped and swayed as Puck added tiny glowing weights.

[bold white]Let's find out what things weigh![/bold white]
""",
    "volume": """
Puck carefully carried a set of measuring cups to the center of the page.

[bold cyan]"Volume,"[/bold cyan] Puck said, [bold cyan]"tells you how much space
something takes up — especially liquids! A teaspoon, a cup,
a liter, a gallon — each one holds a different amount."[/bold cyan]

Glowing blue water poured from one cup to the next,
filling them up to perfect lines.

[bold cyan]"Bakers, scientists, and doctors all need to measure
liquids perfectly. And now — so will you!"[/bold cyan]

[bold white]Let's learn about cups, liters, and gallons![/bold white]
""",
    "temperature": """
Puck held up a tall, slender thermometer. The red line inside
climbed up and down as the page shifted from icy blue to warm gold.

[bold cyan]"Temperature,"[/bold cyan] Puck said, [bold cyan]"measures how hot or cold
something is. Water freezes at 32 degrees Fahrenheit — that's
zero Celsius. Your body stays at 98.6 Fahrenheit. And water
boils at 212 Fahrenheit — a hundred Celsius!"[/bold cyan]

Snowflakes drifted on one side of the page. Steam rose on the other.

[bold white]Let's explore the world of hot and cold![/bold white]
""",
    "comparing": """
Puck set two objects side by side on the page — a marble and a bowling ball.

[bold cyan]"Measuring isn't just about numbers,"[/bold cyan] Puck said.
[bold cyan]"It's about comparing. Which is longer? Which is heavier?
Which is bigger? Sometimes you don't even need a tool —
just a good eye and a smart brain!"[/bold cyan]

The marble and bowling ball began to glow, inviting comparison.

[bold cyan]"Estimation is a superpower. Let's practice it!"[/bold cyan]

[bold white]Time to compare, estimate, and think like a scientist![/bold white]
""",
    "tools": """
Puck opened a glowing toolbox, and out floated five shining instruments:
a ruler, a scale, a measuring cup, a thermometer, and a clock.

[bold cyan]"A carpenter wouldn't use a thermometer to measure wood,"[/bold cyan]
Puck said with a grin. [bold cyan]"And a baker wouldn't use a ruler
to measure flour! Every measurement has the right tool —
and knowing which one to pick is half the battle."[/bold cyan]

The five tools arranged themselves in a circle, each one glowing softly.

[bold white]Let's learn which tool to use and when![/bold white]
""",
    "real_world": """
Puck flew high above the workshop — so high that the page stretched
into a vast landscape of buildings, roads, animals, and mountains.

[bold cyan]"Now for the fun part,"[/bold cyan] Puck called down.
[bold cyan]"How far is a mile? How heavy is a car? How tall
is the Statue of Liberty? How fast does an airplane fly?
The real world is FULL of amazing measurements —
and once you know them, you'll never look at
the world the same way again!"[/bold cyan]

The landscape glowed with tiny labels and numbers everywhere.

[bold white]Let's measure the real world![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "length": """
[bold green]The golden ruler glows with pride![/bold green]

Inches, feet, centimeters, meters — you know them all now.
The ruler on the workshop wall shines with a warm light.

[bold cyan]"You can measure length!"[/bold cyan] Puck says happily.
[bold cyan]"From a tiny bug to a tall building — you know
how to describe how long things are."[/bold cyan]

The brass scale gleams on the next shelf. Weight is calling...
""",
    "weight": """
[bold green]The scale balances perfectly![/bold green]

Ounces, pounds, grams, kilograms — heavy and light,
big and small, you understand them all.

[bold cyan]"You've mastered weight!"[/bold cyan] Puck says, lifting a tiny dumbbell.
[bold cyan]"Now you know what things weigh — from a paperclip
to an elephant!"[/bold cyan]

The measuring cups are lined up and ready. Volume is next...
""",
    "volume": """
[bold green]The measuring cups are full to the brim![/bold green]

Cups, liters, gallons — you know how much things hold
and how to measure liquids perfectly.

[bold cyan]"Volume — mastered!"[/bold cyan] Puck says, pouring a perfect cup.
[bold cyan]"You could bake a cake, fill a fish tank,
or measure medicine — all with confidence!"[/bold cyan]

The thermometer begins to glow. Temperature awaits...
""",
    "temperature": """
[bold green]The thermometer glows from bottom to top![/bold green]

Freezing, boiling, body temperature, weather —
you understand the whole scale now.

[bold cyan]"Hot and cold have no secrets from you,"[/bold cyan] Puck says.
[bold cyan]"Fahrenheit or Celsius — you speak both languages!"[/bold cyan]

Two objects appear side by side on the page. Time to compare...
""",
    "comparing": """
[bold green]Your estimation skills are sharp as a tack![/bold green]

Bigger, smaller, heavier, lighter — you can compare
anything and make smart guesses about size and weight.

[bold cyan]"Estimation,"[/bold cyan] Puck says with admiration,
[bold cyan]"is what separates a good measurer from a great one.
And you're becoming great!"[/bold cyan]

The toolbox opens wide. Time to learn the instruments...
""",
    "tools": """
[bold green]Every tool in the workshop glows![/bold green]

Rulers for length. Scales for weight. Measuring cups for volume.
Thermometers for temperature. Clocks for time.
You know exactly which tool to reach for.

[bold cyan]"The right tool for the right job,"[/bold cyan] Puck says proudly.
[bold cyan]"That's the mark of a true measurer!"[/bold cyan]

The workshop doors open wide. The real world is waiting...
""",
    "real_world": """
[bold green]The whole world glows with measurements![/bold green]

Miles and feet, tons and pounds, stories and speeds —
the real world is full of numbers, and now you know them.

[bold cyan]"You've done it!"[/bold cyan] Puck's wings spread wide with pride.
[bold cyan]"Length, weight, volume, temperature, comparisons, tools,
and real-world measurements — you've measured it all.
The Measuring Workshop is yours now, every shelf of it."[/bold cyan]

Puck closes the golden toolbox gently.

[bold white]Counter. Measurer. Calculator. Engineer. Scientist.[/bold white]
[bold white]That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "length": "Puck stands beside a glowing door frame, ruler in hand. [bold yellow]\"Every door you walk through is a measurement! Can you guess how tall this one is?\"[/bold yellow]",
    "weight": "Puck stands on a giant scale, arms stretched wide. [bold yellow]\"Here's a tricky one — how much does someone YOUR age weigh? Think about what you know!\"[/bold yellow]",
    "volume": "Puck sits on the rim of a glowing bathtub, feet dangling in the water. [bold yellow]\"This is the biggest container in most houses! How many gallons do you think it holds?\"[/bold yellow]",
    "temperature": "Puck holds four thermometers at once, each showing a different number. [bold yellow]\"Some of these are Fahrenheit, some are Celsius. Which one is the COLDEST? Think carefully!\"[/bold yellow]",
    "comparing": "Puck lines up pictures of a grape, a cat, a person, and an elephant. [bold yellow]\"Put them in order from lightest to heaviest! Use everything you've learned!\"[/bold yellow]",
    "tools": "Puck floats next to a fish tank with all the measuring tools spread out. [bold yellow]\"You need to check if there's enough water. Which tool do you grab first?\"[/bold yellow]",
    "real_world": "Puck flies to the top of the glowing Statue of Liberty. [bold yellow]\"Lady Liberty is 305 feet tall. Can you figure out what that compares to? Think in stories!\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "length_master": (
        "Length Master",
        "Measured everything from inches to meters with confidence!",
    ),
    "weight_master": (
        "Weight Master",
        "Weighed everything from paperclips to elephants!",
    ),
    "volume_master": (
        "Volume Master",
        "Measured cups, liters, and gallons like a pro!",
    ),
    "temperature_master": (
        "Temperature Master",
        "Explored the whole thermometer from freezing to boiling!",
    ),
    "comparison_expert": (
        "Comparison Expert",
        "Compared sizes, weights, and lengths like a scientist!",
    ),
    "tool_expert": (
        "Tool Expert",
        "Knows exactly which measuring tool to use for every job!",
    ),
}
