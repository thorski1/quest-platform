"""
story.py — Narrative for the Numbers skill pack.

Nell and Puck venture into a magical counting kingdom to learn math.
"""

INTRO_STORY = """
[bold yellow]THE COUNTING KINGDOM[/bold yellow]

Puck zipped to a new page in the Primer.

[bold cyan]"Now that you can read the words,"[/bold cyan] Puck said, [bold cyan]"it's time
to learn the other language. The one that describes how many,
how much, how far, how long."[/bold cyan]

[bold white]"Numbers?"[/bold white]

[bold cyan]"Numbers!"[/bold cyan] Puck spun in a happy circle. [bold cyan]"Numbers are everywhere —
every time you count cookies, read a clock, save up money,
or figure out if your backpack is too heavy. Understanding
numbers means understanding [italic]how things work.[/italic]"[/bold cyan]

The page turned to reveal a bright, colorful kingdom.
Rolling hills covered in giant numbered stones.
A river counting off the seconds.
A town where every shop had a sign with a number on it.

[bold cyan]"The Counting Kingdom,"[/bold cyan] Puck said proudly. [bold cyan]"I built it myself.
Well — the Primer did. But I helped."[/bold cyan]

Nell looked out at the numbered hills and took a deep breath.

[bold white]Here we go.[/bold white]
"""

ZONE_INTROS = {
    "fractions_forest": """
Puck led the way into a forest where every tree was split
perfectly down the middle — two equal halves, side by side.

[bold cyan]"Sometimes things come in pieces,"[/bold cyan] Puck said.
[bold cyan]"And that's where fractions come in.
A fraction tells you how many pieces something has
and how many of those pieces you're talking about."[/bold cyan]

A glowing [bold yellow]1/2[/bold yellow] floated between two halves of a great oak.

[bold white]Step into the forest. The pieces are waiting.[/bold white]
""",
    "counting_hills": """
Puck landed on the first hill, which had a big stone [bold yellow]1[/bold yellow] on top.

[bold cyan]"Counting seems simple,"[/bold cyan] Puck said, [bold cyan]"but it's the foundation of
everything else. Once you can count to 100, you can understand
[italic]any[/italic] amount of anything."[/bold cyan]

Numbers stretched across the hills as far as Nell could see.

[bold white]Count carefully. Don't skip any![/bold white]
""",
    "addition_meadow": """
Two paths through a meadow joined into one.

[bold cyan]"Addition,"[/bold cyan] Puck said, [bold cyan]"is just counting two groups together.
You don't need anything fancy — if you can count, you can add.
And once you can add, you can [italic]build[/italic] things."[/bold cyan]

[bold white]What happens when we put groups together?[/bold white]
""",
    "subtraction_valley": """
Puck led the way into a valley where numbers shrank as you walked.

[bold cyan]"Subtraction is addition's twin,"[/bold cyan] Puck said. [bold cyan]"When you add,
you combine. When you subtract, you take away. Both are
ways of understanding change."[/bold cyan]

[bold white]Take away carefully — how much is left?[/bold white]
""",
    "shape_forest": """
The trees in this forest all had shapes — triangles, squares,
circles, rectangles, hexagons — some shining like stained glass.

[bold cyan]"Shapes are everywhere,"[/bold cyan] Puck said. [bold cyan]"Every building, every piece
of food, every window — all shapes. Once you name them,
you'll see them in everything."[/bold cyan]

[bold white]Name the shapes. Count their sides.[/bold white]
""",
    "time_tower": """
A great clock tower rose from the center of the kingdom.

[bold cyan]"Time,"[/bold cyan] Puck said solemnly, [bold cyan]"is the most important number of all.
Everyone gets the same amount of it each day — twenty-four hours.
Understanding the clock means understanding your day."[/bold cyan]

The clock hands ticked. The numbers waited.

[bold white]Can you read the time?[/bold white]
""",
    "skip_counting_grove": """
Puck led the way into a grove of tall trees, each one a different number.

[bold cyan]"We don't have to count every single number,"[/bold cyan] Puck said cheerfully.
[bold cyan]"Sometimes we can HOP — skip right over some, and count faster!
By 2s, by 5s, by 10s — each pattern is a shortcut."[/bold cyan]

The trees waited, their numbers glowing in the dappled light.

[bold white]Find the pattern. Skip your way through![/bold white]
""",
    "measurement_meadow": """
The meadow stretched in all directions — tall flowers, wide ponds,
heavy stones, and warm sunshine.

[bold cyan]"Everything in the world can be measured,"[/bold cyan] Puck said,
floating alongside a ruler that hovered in the air.
[bold cyan]"How long, how heavy, how much, how hot.
Measurement turns vague feelings into exact facts!"[/bold cyan]

[bold white]Measure carefully. Every number tells you something real.[/bold white]
""",
    "money_market": """
A cheerful market square appeared, full of little stalls with price tags.

[bold cyan]"Money!"[/bold cyan] Puck announced happily. [bold cyan]"Every coin has a value — a number
that tells you what it's worth. Once you know the coins,
you can count how much you have and figure out if you have enough."[/bold cyan]

Coins glinted in the light: copper pennies, silver nickels, tiny dimes,
big quarters.

[bold white]Learn the coins. Count your treasure![/bold white]
""",
    "shapes_and_patterns": """
Puck led the way through a little gate into the most beautiful garden.

Flowers grew in triangles and circles. The stone path was laid in a
perfect repeating pattern — square, round, square, round, all the way
to the fountain.

[bold cyan]"Shapes and patterns are hiding everywhere,"[/bold cyan] Puck said happily.
[bold cyan]"In tiles, in flowers, in windows, in fences. Once your eye
knows what to look for — you'll see them [italic]everywhere.[/italic]"[/bold cyan]

[bold white]Look closely. Name the shapes. Finish the patterns.[/bold white]
""",
    "telling_time": """
Puck pointed up at a tall stone tower at the edge of the kingdom.
At the very top was the most magnificent clock — gold hands, bright
numbers, tick-tocking in the sunshine.

[bold cyan]"Learning to tell time,"[/bold cyan] Puck said, [bold cyan]"is like learning
a secret language that everyone uses. Once you can read
a clock, you always know where you are in your day."[/bold cyan]

The big hand moved. The little hand waited.

[bold white]Read the clock. Know your time.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "fractions_forest": """
[bold green]The forest glows as every tree becomes whole again![/bold green]

The halves and quarters and thirds shimmer with golden light.

[bold cyan]"You understand fractions now,"[/bold cyan] Puck says with delight.
[bold cyan]"Top number, bottom number — what you have,
and how many pieces there are.
Half, quarter, third — the language of sharing
and dividing the world fairly."[/bold cyan]

[bold white]Fractions are yours. The world just got more precise![/bold white]
""",
    "counting_hills": """
[bold green]The hills are counted![/bold green]

Every numbered stone glows as Nell walks past. One, two, three...
all the way up the hills and back down.

[bold cyan]"You've got it,"[/bold cyan] Puck cheers. [bold cyan]"Counting is in your bones now!
The meadow is next — let's see what happens when we
put groups together."[/bold cyan]
""",
    "addition_meadow": """
[bold green]The meadow blooms![/bold green]

The two paths are one now, and the flowers are twice as bright.

[bold cyan]"Addition!"[/bold cyan] Puck does a little spin. [bold cyan]"3 + 4 = 7. 6 + 8 = 14.
You know it now — it lives in your head, ready whenever you need it."[/bold cyan]

The valley below calls. Something is about to be taken away...
""",
    "subtraction_valley": """
[bold green]The valley balances![/bold green]

Addition and subtraction sit on opposite sides of Nell, both nodding.

[bold cyan]"Add and subtract,"[/bold cyan] Puck says. [bold cyan]"Two sides of the same idea.
You now understand both. The forest of shapes is ahead —
and shapes have [italic]sides[/italic] too!"[/bold cyan]
""",
    "shape_forest": """
[bold green]The forest glows with shapes![/bold green]

Every tree shows off its shape: 3 sides, 4 sides, 6 sides!
Circles with no sides at all, just endless curve.

[bold cyan]"Geometry!"[/bold cyan] Puck announces proudly. [bold cyan]"Shapes are just math
you can see. And now you can see them everywhere."[/bold cyan]

The clock tower stands ahead, its hands still moving...
""",
    "time_tower": """
[bold green]The clock tower chimes![/bold green]

The big bell rings out the hour, and Nell reads it perfectly.

[bold cyan]"You can read the clock,"[/bold cyan] Puck says quietly. [bold cyan]"Do you know what
that means? It means you're in charge of your own time now.
You know when things start, when they end, and how long
you have."[/bold cyan]

[bold white]That is a powerful thing to know.[/bold white]
""",
    "skip_counting_grove": """
[bold green]The grove is alive with patterns![/bold green]

Every other tree lights up — 2, 4, 6, 8...
Then every fifth — 5, 10, 15, 20...
Then every tenth — 10, 20, 30...

[bold cyan]"You've got the skip in your step now,"[/bold cyan] Puck cheers.
[bold cyan]"Counting by 2s, 5s, and 10s — those shortcuts will help you
[italic]every single day.[/italic] The meadow is just ahead!"[/bold cyan]
""",
    "measurement_meadow": """
[bold green]The meadow is measured![/bold green]

Every flower has a ruler next to it. Every stone has a weight.
Everything in this meadow is understood.

[bold cyan]"Measurement,"[/bold cyan] Puck says proudly, [bold cyan]"means you never have to
just guess. Now you can know — exactly how long, exactly how
heavy, exactly how much. That's powerful!"[/bold cyan]

The money market is just around the corner, coins shining...
""",
    "money_market": """
[bold green]The market rings with coins![/bold green]

Every stall is happy — Nell counted exactly right,
and even figured out the change.

[bold cyan]"Look at you!"[/bold cyan] Puck says. [bold cyan]"Pennies, nickels, dimes, quarters —
you know them all. You can count money. You can make change.
The whole kingdom of numbers is yours now."[/bold cyan]

[bold white]Every coin, every number, every pattern — you've learned them all.[/bold white]
""",
    "shapes_and_patterns": """
[bold green]The garden blooms with every shape![/bold green]

Triangles, squares, circles, and rectangles glow in the sunshine.
The path's pattern stretches perfectly into the distance.

[bold cyan]"You see them now, don't you?"[/bold cyan] Puck says softly. [bold cyan]"Shapes
and patterns in everything around you. The world is full
of mathematics, just waiting to be noticed."[/bold cyan]

[bold white]The Clockwork Tower is ahead — time to learn the time![/bold white]
""",
    "telling_time": """
[bold green]The Clockwork Tower chimes![/bold green]

The great golden bell rings, and the sound rolls across
the whole kingdom. You read the clock — perfectly.

[bold cyan]"There it is,"[/bold cyan] Puck says proudly. [bold cyan]"You can tell the time now.
That means you're in charge of your own day. You know when
things start, how long you have, and when to be ready."[/bold cyan]

[bold white]That is one of the most useful things you will ever learn.[/bold white]
""",
}

BOSS_INTROS = {
    "fractions_forest": "A ribbon hangs between two trees, glowing. [bold yellow]\"One last fraction puzzle — you'll need to think carefully, but everything you've learned will help you!\"[/bold yellow]",
    "counting_hills": "The biggest hill has a stone with [bold yellow]100[/bold yellow] on it. [bold yellow]\"Count all the way to here — without skipping!\"[/bold yellow]",
    "addition_meadow": "Two large groups of flowers merge in a big burst of color. [bold yellow]\"Bigger numbers now! Can you add them?\"[/bold yellow]",
    "subtraction_valley": "A large pile shrinks quickly. [bold yellow]\"How much is left when you take a big number away?\"[/bold yellow]",
    "shape_forest": "A many-sided shape hovers in the air, sparkling. [bold yellow]\"Count every side — what shape is this?\"[/bold yellow]",
    "time_tower": "The clock shows a tricky time. [bold yellow]\"Read the clock — what time is it exactly?\"[/bold yellow]",
    "skip_counting_grove": "The tallest tree in the grove glows with an even number. [bold yellow]\"Is it a multiple of 2? Think carefully!\"[/bold yellow]",
    "measurement_meadow": "Puck holds up two containers side by side. [bold yellow]\"Which one holds more? Think about the units!\"[/bold yellow]",
    "money_market": "A price tag flutters in the breeze. [bold yellow]\"Can you figure out the change? Subtract carefully!\"[/bold yellow]",
    "shapes_and_patterns": "The flowers in the center of the garden arrange themselves into a long pattern. [bold yellow]\"The trickiest pattern of all — look carefully and find what comes next!\"[/bold yellow]",
    "telling_time": "The clock tower's hands begin to spin. [bold yellow]\"One last tricky time to figure out — think carefully and you'll get it!\"[/bold yellow]",
}
