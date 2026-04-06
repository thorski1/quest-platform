"""
story.py — Narrative for the Critical Thinking & Logic skill pack.

Puck opens the doors to the Puzzle Palace and guides the reader through
patterns, sorting, cause and effect, facts vs opinions, problem solving,
analogies, and brain teasers — training the most powerful tool of all: the mind.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Puzzle Palace[/bold yellow]

The Primer's pages rustled on their own. Something new was forming —
not a map, not a story, but a great shimmering building made entirely
of light, with towers of crystal and doors that opened into impossible
rooms.

[bold cyan]"A palace!"[/bold cyan] Puck announced, landing on the tallest spire.
[bold cyan]"But not a palace for kings and queens. A palace for
[italic]thinkers.[/italic] Every room is a puzzle. Every hallway is a riddle.
And every door you open makes your brain a little bit stronger."[/bold cyan]

The girl stared up at the glittering towers. [bold white]"My brain?"[/bold white]

[bold cyan]"Your brain,"[/bold cyan] Puck said firmly, [bold cyan]"is the most powerful
thing you own. Stronger than any sword, faster than any horse,
more valuable than any treasure. But just like muscles,
it needs [italic]exercise.[/italic]"[/bold cyan]

Puck fluttered down to the great front door and pushed it open.
Inside, light bent into patterns, questions floated in the air,
and every wall was lined with riddles waiting to be solved.

[bold cyan]"Patterns. Logic. Puzzles. Riddles. Cause and effect.
Fact and opinion. All of it — waiting for you."[/bold cyan]

Puck grinned.

[bold cyan]"Ready to train the most powerful superpower there is?"[/bold cyan]

[bold white]The doors of the Puzzle Palace swing open. Step inside.[/bold white]
"""

ZONE_INTROS = {
    "patterns": """
Puck led the way into the first room of the Puzzle Palace.
The walls were covered in glowing sequences — numbers climbing
like staircases, shapes dancing in repeating chains, colors pulsing
in rhythms that almost made music.

[bold cyan]"Patterns,"[/bold cyan] Puck said, [bold cyan]"are the secret language of the universe.
The sun rises in a pattern. The seasons turn in a pattern.
Your heartbeat is a pattern. Once you learn to SEE them,
you'll find them absolutely everywhere."[/bold cyan]

Glowing sequences floated in the air:
[bold yellow]2, 4, 6... Circle, Square, Triangle... 1, 2, 4, 8...[/bold yellow]

[bold white]Let's crack the code of patterns![/bold white]
""",
    "sorting_grouping": """
The next room was in beautiful chaos — objects of every kind
floating in the air, bumping into each other, completely unsorted.
Books next to bananas. Stars next to socks. Numbers next to butterflies.

[bold cyan]"This room,"[/bold cyan] Puck said, [bold cyan]"is a mess. And the only way to fix it
is to SORT things into groups. What goes with what? What doesn't belong?
And sometimes — the really clever part — something can belong
to two groups at once!"[/bold cyan]

Two overlapping circles shimmered on the wall — a Venn diagram,
waiting to be filled.

[bold white]Let's bring order to the chaos![/bold white]
""",
    "cause_and_effect": """
Puck opened the third door, and the room was full of dominoes —
thousands of them, standing in intricate chains across tables
and shelves and spiraling ramps.

[bold cyan]"Cause,"[/bold cyan] Puck said, tapping the first domino gently,
[bold cyan]"and effect."[/bold cyan] The whole chain began to fall, click-click-click,
all the way across the room.

[bold cyan]"Everything that happens has a reason. And everything
that happens CAUSES something else. Once you understand this,
you can predict the future — and sometimes even change it."[/bold cyan]

[bold white]Let's discover what causes what![/bold white]
""",
    "fact_vs_opinion": """
The fourth room was divided down the middle with a golden line.
One side was labeled [bold yellow]FACT[/bold yellow] in sturdy, carved letters.
The other side was labeled [bold yellow]OPINION[/bold yellow] in flowing, colorful script.

[bold cyan]"This,"[/bold cyan] Puck said seriously, [bold cyan]"might be the most important
room in the whole palace. Because the difference between
what IS true and what someone FEELS is true...
that's one of the most powerful things a person can understand."[/bold cyan]

Puck held up a tiny telescope made of golden light.

[bold cyan]"Let's look at the world through the Truth Telescope."[/bold cyan]

[bold white]Can you separate fact from opinion?[/bold white]
""",
    "problem_solving": """
The fifth room looked like a workshop — tables covered with tools,
walls hung with blueprints, and a large chalkboard covered in
half-finished plans.

[bold cyan]"Some problems,"[/bold cyan] Puck said, picking up a tiny hammer,
[bold cyan]"seem impossible at first. Too big. Too complicated.
But every big problem is really just a bunch of
small problems standing on each other's shoulders."[/bold cyan]

Puck wrote on the chalkboard:
[bold yellow]1. Break it down. 2. Work backwards. 3. Try and adjust.[/bold yellow]

[bold cyan]"Three tools. That's all you need to solve almost anything."[/bold cyan]

[bold white]Let's build our problem-solving toolkit![/bold white]
""",
    "analogies": """
The sixth room was built like a bridge — a long, arching span
of crystal connecting two floating islands. On each island
sat a pair of objects that seemed completely different...
until you saw the invisible thread connecting them.

[bold cyan]"An analogy,"[/bold cyan] Puck said, walking along the bridge,
[bold cyan]"is a connection between two things that seem different
but are actually related in the same way.
Hot is to cold as up is to down.
Pen is to write as knife is to cut.
See the pattern? The RELATIONSHIP is the same!"[/bold cyan]

[bold white]Let's discover the hidden connections![/bold white]
""",
    "brain_teasers": """
The final room of the Puzzle Palace was behind a door
that looked different from all the others — covered in
question marks that shifted and changed, riddles carved into
the wood, and a lock that could only be opened by thinking
sideways.

[bold cyan]"The Riddle Vault,"[/bold cyan] Puck whispered with excitement.
[bold cyan]"These are the trickiest puzzles in the whole palace.
Logic chains, riddles with double meanings, puzzles that
require you to think in ways you've never thought before.
Are you ready?"[/bold cyan]

The door swung open. Inside, golden riddles hung in the air,
each one glowing, each one waiting.

[bold white]Welcome to the Riddle Vault. Think carefully![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "patterns": """
[bold green]The Pattern Garden blooms with light![/bold green]

Every sequence on the wall is complete — numbers climbing perfectly,
shapes dancing in their proper order, growing patterns reaching
toward the ceiling like vines made of pure logic.

[bold cyan]"You see patterns now,"[/bold cyan] Puck says proudly.
[bold cyan]"In numbers, in shapes, in the world around you.
That's a skill you'll use every single day of your life."[/bold cyan]

A door appears at the far end, leading to a room in complete disarray...
""",
    "sorting_grouping": """
[bold green]The Sorting Chamber gleams — everything in its perfect place![/bold green]

Every object has found its group. The Venn diagrams glow
with perfect overlapping circles, each item exactly
where it belongs.

[bold cyan]"Order from chaos,"[/bold cyan] Puck says with satisfaction.
[bold cyan]"You can look at a jumble of things and find the groups
hiding inside. That's the beginning of real understanding."[/bold cyan]

From the next room, the sound of dominoes clicking, one after another...
""",
    "cause_and_effect": """
[bold green]The dominoes have all fallen — every chain complete![/bold green]

The entire room is a finished masterpiece of cause and effect,
every chain perfectly predicted, every outcome understood.

[bold cyan]"You understand WHY things happen,"[/bold cyan] Puck says.
[bold cyan]"That's not just smart — that's powerful. Because once you
understand cause and effect, you can make better choices."[/bold cyan]

A golden line appears on the floor, dividing the next room in two...
""",
    "fact_vs_opinion": """
[bold green]The Truth Telescope shines crystal clear![/bold green]

Every statement in the room has been sorted — facts on one side,
opinions on the other, and the tricky mixed sentences
carefully pulled apart.

[bold cyan]"You can tell what's real from what's felt,"[/bold cyan] Puck says seriously.
[bold cyan]"That makes you very hard to fool. And in a world full
of opinions pretending to be facts — that's a superpower."[/bold cyan]

The workshop door opens ahead. Time to roll up our sleeves...
""",
    "problem_solving": """
[bold green]The Strategy Workshop stands complete — every problem solved![/bold green]

The chalkboard is filled with beautiful solutions, broken down
step by step. The river crossing is solved. The timeline
runs perfectly backwards. Every plan is in order.

[bold cyan]"You don't give up,"[/bold cyan] Puck says warmly.
[bold cyan]"You break things down, work backwards, and try again.
That's not just a thinking skill — that's a life skill."[/bold cyan]

A crystal bridge stretches ahead, connecting things you never thought were related...
""",
    "analogies": """
[bold green]The Connection Bridge blazes with light![/bold green]

Every analogy is complete. Opposites, parts, categories,
functions, degrees — all of them linked, all of them understood.

[bold cyan]"You see connections others miss,"[/bold cyan] Puck says.
[bold cyan]"When someone says something 'is like' something else,
you understand exactly what they mean. That makes you
a better reader, a better listener, and a better thinker."[/bold cyan]

One final door waits — covered in question marks and riddles...
""",
    "brain_teasers": """
[bold green]The Riddle Vault is open — every puzzle solved![/bold green]

Golden riddles drift to the floor, each one cracked, each one
understood. The balance scale sits in perfect equilibrium.
The logic chains are complete. The lateral thinking puzzles
lie open, their tricks revealed.

[bold cyan]"You've done it."[/bold cyan] Puck's wings spread wide.
[bold cyan]"Patterns, sorting, cause and effect, facts and opinions,
problem solving, analogies, and brain teasers.
Your mind is sharper, quicker, and stronger than ever."[/bold cyan]

Puck looks at you with shining eyes.

[bold cyan]"The Puzzle Palace isn't closing. It lives in your head now.
Every time you think carefully, ask 'why?', spot a pattern,
or refuse to be fooled — you're HERE. In the Palace.
Using your superpower."[/bold cyan]

[bold white]Thinker. Puzzler. Detective. Strategist. Genius. Mastermind.[/bold white]
[bold white]That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "patterns": "Puck pulls out a swirling sequence of numbers that keeps changing. [bold yellow]\"This pattern has a secret -- it's TWO patterns in disguise! Can you untangle them?\"[/bold yellow]",
    "sorting_grouping": "Puck juggles a basketball, an orange, and a book. [bold yellow]\"Round? Edible? Both? Neither? Put them all in the right place on the Venn diagram!\"[/bold yellow]",
    "cause_and_effect": "Thunder booms and a tree crashes across the road. [bold yellow]\"A chain of events! But the real question is: what's the SMARTEST thing to do next?\"[/bold yellow]",
    "fact_vs_opinion": "Puck holds up a sentence that glows half-gold and half-silver. [bold yellow]\"This sentence is hiding a fact INSIDE an opinion. Can you separate them?\"[/bold yellow]",
    "problem_solving": "A fox, a chicken, and a sack of grain wait at a riverbank. [bold yellow]\"The oldest logic puzzle in the world. Think carefully -- one wrong move and someone gets eaten!\"[/bold yellow]",
    "analogies": "Puck draws two pairs of pictures in the air. [bold yellow]\"Young and old, big and small -- what's the relationship? Find the invisible thread!\"[/bold yellow]",
    "brain_teasers": "Twelve identical coins gleam on the page. A golden balance scale sits beside them. [bold yellow]\"One coin is heavier. Three weighings. Can you ALWAYS find it? This is the ultimate test!\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "pattern_spotter": (
        "Pattern Spotter",
        "Cracked every sequence in the Pattern Garden!",
    ),
    "master_sorter": (
        "Master Sorter",
        "Sorted every object and mastered the Venn diagram!",
    ),
    "chain_thinker": (
        "Chain Thinker",
        "Followed every chain of cause and effect to its source!",
    ),
    "truth_seeker": (
        "Truth Seeker",
        "Separated every fact from every opinion without being fooled!",
    ),
    "problem_cracker": (
        "Problem Cracker",
        "Broke down every problem and solved it step by step!",
    ),
    "connection_finder": (
        "Connection Finder",
        "Found the hidden link in every analogy!",
    ),
    "riddle_master": (
        "Riddle Master",
        "Cracked every riddle, puzzle, and brain teaser in the Vault!",
    ),
}
