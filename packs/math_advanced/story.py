"""
story.py — Narrative for the Math Advanced skill pack.

Puck leads the player through the golden door to the Math Academy,
where numbers float in the air and reveal their deepest secrets.
"""

INTRO_STORY = """
[bold yellow]THE MATH ACADEMY[/bold yellow]

Puck appeared at the edge of the Primer's page, wings flickering with excitement.

[bold cyan]"You've counted. You've added and subtracted."[/bold cyan] Puck hovered
in front of a tall door made of solid gold, covered in glowing numbers.
[bold cyan]"But numbers go [italic]much[/italic] deeper than that."[/bold cyan]

[bold white]"What's through the door?"[/bold white]

[bold cyan]"The Math Academy."[/bold cyan] Puck's voice dropped to an awed hush.
[bold cyan]"Where numbers reveal their real power. Multiplication —
one of the great shortcuts of the universe. Division —
the art of sharing equally. Geometry — shapes with secrets.
And things called decimals, and percentages, and even
[italic]numbers below zero.[/italic]"[/bold cyan]

The golden door swung open on its own.

Inside, numbers floated in the air like glowing sparks.
Equations drifted past like leaves on water.
Shapes rotated slowly overhead, their angles glinting.

[bold cyan]"This,"[/bold cyan] Puck said proudly, stepping inside,
[bold cyan]"is where math stops being just counting
and starts being [italic]thinking.[/italic]"[/bold cyan]

[bold white]The Math Academy is waiting. Let's go in.[/bold white]
"""

ZONE_INTROS = {
    "multiplication": """
The first hall of the Academy glowed with a warm golden light.
Numbers arranged themselves on the walls in neat rows and columns.

[bold cyan]"Multiplication,"[/bold cyan] Puck announced, [bold cyan]"is the great shortcut.
Instead of adding 7 over and over eight times, you just say:
[italic]seven times eight.[/italic] One step, same answer."[/bold cyan]

A grid of numbers lit up — the times tables, row by row.

[bold cyan]"Learn these, and you'll have a superpower.
Most calculations in the real world use multiplication
every single day."[/bold cyan]

[bold white]The times tables are waiting. Let's conquer them![/bold white]
""",
    "division": """
A door opened into a workshop full of gears, scales, and sorting trays.

[bold cyan]"Division,"[/bold cyan] Puck said, [bold cyan]"is multiplication's partner.
If multiplication means putting groups together,
division means splitting them back apart — equally."[/bold cyan]

Puck picked up a small pile of glowing marbles and divided them
into four even groups.

[bold cyan]"Sharing fairly. Splitting evenly. Finding out how many
fit inside. Division is all of those things."[/bold cyan]

[bold white]Enter the workshop. Split carefully![/bold white]
""",
    "word_problems": """
A cozy café appeared, with little tables and menus written in equations.

[bold cyan]"Story problems,"[/bold cyan] Puck said, pulling out a chair,
[bold cyan]"are where math meets real life. Apples in bags.
Trains going distances. Friends sharing stickers.
These aren't just math — they're [italic]thinking.[/italic]"[/bold cyan]

Puck tapped the menu.

[bold cyan]"Read carefully. Figure out what you know
and what you need to find. Then choose your operation."[/bold cyan]

[bold white]The Café is open. Order your thinking![/bold white]
""",
    "geometry": """
The Shape Lab glimmered with light bouncing off every angle.
Triangles, circles, rectangles, and squares hung in the air,
rotating slowly so every side could be seen.

[bold cyan]"Geometry,"[/bold cyan] Puck said, stepping carefully between them,
[bold cyan]"is math you can [italic]see.[/italic] Shapes have rules —
angles that must add up, sides that have lengths,
areas that can be measured exactly."[/bold cyan]

A ruler and protractor floated over.

[bold cyan]"Architects use this to build houses. Artists use it
to draw perspective. Engineers use it to make bridges hold."[/bold cyan]

[bold white]The Lab is ready. Measure everything![/bold white]
""",
    "decimals_percents": """
A beautiful garden stretched out, flowers growing in precise rows.
But these flowers had unusual names — [bold yellow]0.25[/bold yellow], [bold yellow]0.5[/bold yellow],
[bold yellow]75%[/bold yellow], [bold yellow]1.75[/bold yellow] — written on little tags in the soil.

[bold cyan]"Decimals and percents,"[/bold cyan] Puck said, kneeling by a flower labeled [bold yellow]0.5[/bold yellow],
[bold cyan]"are just fractions wearing different clothes.
Half a dollar, half a pizza, half a chance —
they're all the same idea, just written differently."[/bold cyan]

Puck stood and smiled.

[bold cyan]"Sales, recipes, test scores, bank accounts —
decimals and percents are [italic]everywhere.[/italic]"[/bold cyan]

[bold white]Tend the garden. Learn the language of parts![/bold white]
""",
    "negative_numbers": """
A staircase led downward into a glowing underground passage.
The number line was painted on the wall — and it stretched
not just to the right, but far to the left, below zero.

[bold cyan]"Negative numbers,"[/bold cyan] Puck said, stepping down,
[bold cyan]"are the numbers below zero. They exist
wherever something can be [italic]less than nothing.[/italic]
Cold temperatures. Floors below ground. Debts."[/bold cyan]

The air felt cool down here. Numbers glimmered on the walls.

[bold cyan]"Once you understand negative numbers,
you understand the [italic]full[/italic] number line —
in both directions, forever."[/bold cyan]

[bold white]Step down. Explore below zero![/bold white]
""",
    "time_and_calendars": """
The Academy's tallest tower stretched upward, its walls covered
in clocks — grandfather clocks, pocket watches, digital displays,
sundials — all ticking in perfect sync.

[bold cyan]"Time,"[/bold cyan] Puck said, sitting on the hour hand of a giant clock,
[bold cyan]"is something you use every single day, all your life.
And yet most people never learn [italic]why[/italic] we have
sixty seconds in a minute, or why some years have
an extra day."[/bold cyan]

The big clock face showed hands and numbers.
A calendar page fluttered nearby.

[bold cyan]"Clocks. Calendars. Elapsed time. Leap years.
Once you understand time, you can plan, measure,
and never be late again."[/bold cyan]

[bold white]The Clock Tower is open. What time is it?[/bold white]
""",
    "patterns_and_sequences": """
The final hall of the Academy was unlike the others.
Numbers floated in spirals. Shapes arranged themselves
in rows. A pinecone sat under a spotlight.

[bold cyan]"Patterns,"[/bold cyan] Puck said quietly, [bold cyan]"are the heartbeat
of mathematics. Numbers don't just sit there —
they [italic]dance.[/italic] They repeat. They grow.
They follow rules."[/bold cyan]

Puck pointed to the pinecone.

[bold cyan]"Did you know the spirals in a pinecone
follow the same number sequence as galaxies?
It's called the Fibonacci sequence —
and you're about to discover it."[/bold cyan]

[bold white]Enter the Pattern Palace. Find the rules![/bold white]
""",
    "fractions_and_ratios": """
Deep in the Fraction Forest, the trees were each divided
into different numbers of equal pieces.

One tree split into 2 halves.
Another into 4 quarters.
A third into 8 eighths.

[bold cyan]"They look different,"[/bold cyan] Puck said, sitting on a branch,
[bold cyan]"but half of a tree is the same amount of tree
whether you call it 1/2, 2/4, or 4/8.
That's the magic of fractions — same value, different names."[/bold cyan]

Somewhere deeper in the forest, a recipe card fluttered past
with ratios for the most delicious cake imaginable.

[bold white]Into the Fraction Forest! Parts, wholes, and ratios await.[/bold white]
""",
    "probability_and_chance": """
[bold yellow]◈  THE CHANCE CHAMBER  ◈[/bold yellow]

[bold cyan]Puck steps into a room filled with dice, coins, spinners, and colourful bags of balls.[/bold cyan]

[bold yellow]"What if I told you we could MEASURE chance?"[/bold yellow]

A coin flips in the air — heads? tails? A die rolls across the floor.
A ball gets pulled from a bag without looking.

[bold cyan]Puck catches the coin and holds it up:
"Every one of these has a probability. A fraction. A number between 0 and 1.
Zero means impossible. One means certain. And everything in between
tells you exactly how likely something is."[/bold cyan]

[bold white]Into the Chance Chamber! Dice, coins, and the science of likelihood await![/bold white]
""",
    "algebra_intro": """
[bold yellow]◈  THE VARIABLE VAULT  ◈[/bold yellow]

[bold cyan]Puck opens a heavy vault door. Inside, symbols float in the air — x, y, n, a.[/bold cyan]

[bold yellow]"These aren't just letters. They're mystery numbers waiting to be solved."[/bold yellow]

An equation appears on the vault wall: x + 5 = 12.
The x glows softly, asking to be found.

[bold cyan]Puck pulls out a tiny balance scale:
"Think of every equation as a balance. Both sides are always equal.
Whatever you do to one side, you do to the other.
That's the whole secret of algebra — and it's simpler than it looks."[/bold cyan]

[bold white]Into the Variable Vault! Unknowns, equations, and the art of solving await![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "multiplication": """
[bold green]The Multiplication Kingdom glows with mastered facts![/bold green]

Every times table lights up on the walls, row by row.
The great multiplication grid shines like a constellation.

[bold cyan]"You know them,"[/bold cyan] Puck says quietly. [bold cyan]"The times tables
aren't just memorized facts — they're a new speed for your brain.
Calculations that used to take minutes now take seconds."[/bold cyan]

[bold white]The Division Workshop is just ahead — let's split some numbers![/bold white]
""",
    "division": """
[bold green]The Division Workshop hums with satisfied gears![/bold green]

Every tray is sorted. Every group is equal. Every answer is exact.

[bold cyan]"Division,"[/bold cyan] Puck says, [bold cyan]"is how we make things fair.
Equal groups, equal shares, exact fits.
You've got it — and that means you understand
multiplication from [italic]both directions.[/italic]"[/bold cyan]

The Story Problem Café is just around the corner, warm and welcoming...
""",
    "word_problems": """
[bold green]Every problem on the café menu is solved![/bold green]

The little chalkboard by the door fills up with ticked-off problems.
The café owner nods approvingly.

[bold cyan]"Word problems,"[/bold cyan] Puck says, [bold cyan]"are why we learn math in the first place.
Real life doesn't say '6 × 7'. It says 'six baskets, seven apples each.'
You translated the story into math — and back again.
[italic]That[/italic] is a powerful skill."[/bold cyan]

The Shape Lab sparkles in the distance...
""",
    "geometry": """
[bold green]The Shape Lab rings with perfectly measured shapes![/bold green]

Every angle accounted for. Every area calculated. Every perimeter walked.

[bold cyan]"Geometry,"[/bold cyan] Puck says proudly, [bold cyan]"is how humans build the world.
Every building, bridge, and window began as shapes on paper,
measured and calculated exactly the way you just did."[/bold cyan]

A soft glow from the Decimal Garden floats nearby, smelling of flowers...
""",
    "decimals_percents": """
[bold green]The Decimal Garden is in full bloom![/bold green]

Every flower tends itself. Fractions, decimals, and percents
stand side by side, showing they're all the same family.

[bold cyan]"You'll use this,"[/bold cyan] Puck says softly, [bold cyan]"every single day.
Prices. Recipes. Grades. Weather percentages.
The world speaks in decimals, and now you speak it too."[/bold cyan]

Below, the staircase to the Number Line Underground gleams...
""",
    "negative_numbers": """
[bold green]The Number Line Underground is fully explored![/bold green]

The great number line stretches in both directions now —
left past zero into the negatives, right past zero into the positives.
The full picture.

[bold cyan]"There it is,"[/bold cyan] Puck says, looking at the whole line.
[bold cyan]"The complete number line. You understand
every integer — above zero, at zero, and below zero.
Most people never truly picture it. You do."[/bold cyan]

The Fraction Forest glimmers in the distance...
""",
    "fractions_and_ratios": """
[bold green]The Fraction Forest is fully explored![/bold green]

Every tree divided perfectly. Equivalents matched.
Numerators added. Denominators held steady.
Ratios scaled without losing their balance.

[bold cyan]"Two more rooms remain,"[/bold cyan] Puck says.
[bold cyan]"Chance. And the unknown. Let's go."[/bold cyan]
""",
    "probability_and_chance": """
[bold green]The Chance Chamber is solved![/bold green]

Impossible and certain. Fractions as probability.
Equally likely outcomes. The complement rule.

[bold cyan]Puck holds up a die and a coin:[/bold cyan]
[bold cyan]"You can measure chance now. That's a superpower."[/bold cyan]

The Variable Vault glows in the distance...
""",
    "algebra_intro": """
[bold green]The Variable Vault is cracked![/bold green]

Variables. Equations. Balance scales. Two-step solutions.

[bold cyan]"You've done it,"[/bold cyan] Puck says, wings spread wide.
[bold cyan]"The Math Academy: multiplication, division, word problems,
geometry, decimals, negatives, time, patterns, fractions,
probability — and now algebra.
You understand numbers in every form they take."[/bold cyan]

[bold white]The Math Academy is fully conquered. Numbers hold no more mysteries.[/bold white]
""",
}

BOSS_INTROS = {
    "multiplication": "The Eleven Champion floats down from the ceiling, trailing sparks. [bold yellow]\"Eleven times eleven — the square of eleven! Can you find the answer?\"[/bold yellow]",
    "division": "A massive number, 144, hangs in the air, glowing fiercely. [bold yellow]\"One hundred and forty-four, divided by twelve. The famous square — can you divide it?\"[/bold yellow]",
    "word_problems": "The café owner sets down the hardest problem of all. [bold yellow]\"Eight classes, twenty-eight students each. What's the total? Show me you can think big!\"[/bold yellow]",
    "geometry": "A triangle hovers in the center of the lab, rotating slowly. [bold yellow]\"You've done rectangles and squares — but what's the area of a triangle? Do you know the secret formula?\"[/bold yellow]",
    "decimals_percents": "A price tag flutters down from the ceiling: $20, with 25% OFF. [bold yellow]\"If the toy is twenty-five percent off, what do you actually pay? Work it out!\"[/bold yellow]",
    "negative_numbers": "The thermometer on the wall reads -4°C and the temperature is rising. [bold yellow]\"Nine degrees warmer than minus four — what temperature is that? Cross zero carefully!\"[/bold yellow]",
    "fractions_and_ratios": "A pizza sits on the counter, cut into 8 equal slices. Puck grins. [bold yellow]\"You have 3/8. Your friend gives you 2/8 more. You eat 1/8. How much is left? And what does it simplify to?\"[/bold yellow]",
    "probability_and_chance": "Puck holds up a bag with balls in three colours. [bold yellow]\"2 red, 3 blue, 5 green. What is the probability of picking one that is NOT red? Use the complement method if you know it!\"[/bold yellow]",
    "algebra_intro": "A glowing equation appears: 2x + 4 = 14. [bold yellow]\"Two steps. Subtract first, then divide. Show me x — and don't forget to CHECK your answer!\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "multiplication_master": "You memorized the times tables and conquered the Multiplication Kingdom!",
    "division_expert": "You mastered equal sharing and solved every puzzle in the Division Workshop!",
    "problem_solver": "You translated real-world stories into math and back again at the Story Problem Café!",
    "geometry_sage": "You measured shapes, calculated areas, and unlocked the secrets of the Shape Lab!",
    "decimal_pro": "You tended every flower in the Decimal Garden and mastered fractions, decimals, and percents!",
    "number_explorer": "You ventured below zero and mapped the full number line in the Underground!",
}
