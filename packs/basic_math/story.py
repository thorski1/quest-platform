"""
story.py — Narrative for the Basic Math skill pack.

Nell and Puck explore a magical playground where math comes alive.
"""

INTRO_STORY = """
[bold yellow]THE MATH PLAYGROUND[/bold yellow]

The Primer's pages fluttered open to something new.

[bold cyan]"Ready for an adventure?"[/bold cyan] Puck asked, bouncing excitedly.

[bold white]"Always,"[/bold white] Nell said.

[bold cyan]"Good! Because this place is all about [italic]math.[/italic]
Not the boring kind — the kind that helps you figure things out.
How many pizza slices to share. How many days until your birthday.
How to split treasure with your friends."[/bold cyan]

The page turned to reveal an enormous playground stretching
to the horizon — slides shaped like plus signs, swings that
counted as they swung, seesaws balanced with numbers,
and a great golden castle at the far end.

[bold cyan]"The Math Playground,"[/bold cyan] Puck said proudly. [bold cyan]"Every ride
teaches you something new. By the time we reach that castle,
you'll be able to solve problems that would stump a grown-up!"[/bold cyan]

Nell looked at the playground and smiled.

[bold white]Let's play.[/bold white]
"""

ZONE_INTROS = {
    "addition_fun": """
Puck led the way to a meadow full of bright flowers, where numbers
floated gently in the breeze like butterflies.

[bold cyan]"Addition is where it all starts,"[/bold cyan] Puck said cheerfully.
[bold cyan]"When you put things together — cookies on a plate,
friends at a party, stars in the sky — you're adding.
It's the friendliest math there is."[/bold cyan]

Two groups of flowers drifted together and became one bigger group.

[bold white]Put the numbers together. See what you get![/bold white]
""",
    "subtraction_station": """
A train station appeared, but instead of passengers, numbers
were getting on and off the train cars.

[bold cyan]"Subtraction is addition's partner,"[/bold cyan] Puck explained.
[bold cyan]"When something goes away — a balloon pops, you eat a cookie,
a friend goes home — subtraction tells you what's left.
It's just as important as adding."[/bold cyan]

Numbers hopped off a train car, and the total on the side
ticked down with each one.

[bold white]Take some away. How many remain?[/bold white]
""",
    "multiplication_tables": """
The path led to a garden of mirrors, where every number
reflected itself again and again.

[bold cyan]"Multiplication,"[/bold cyan] Puck said with a grin, [bold cyan]"is a shortcut.
Instead of adding 5 + 5 + 5 + 5, you can just say 4 times 5.
Same answer, way faster! Once you know your times tables,
you'll feel like a math wizard."[/bold cyan]

Groups of flowers arranged themselves into perfect rows and columns.

[bold white]Learn the patterns. They'll stick with you forever![/bold white]
""",
    "division_basics": """
Puck floated over to a big round table where a pile of gems
sat in the center, glittering.

[bold cyan]"Division,"[/bold cyan] Puck said, [bold cyan]"is the art of sharing fairly.
If you have a pile of things and a group of friends,
division tells you exactly how many each person gets.
No arguing, no guessing — just math."[/bold cyan]

The gems began sorting themselves into equal little piles.

[bold white]Share them equally. Everyone gets the same![/bold white]
""",
    "word_problems": """
The playground opened into a bustling little town — a bakery,
a toy store, a lemonade stand, and a garden.

[bold cyan]"This is the real test,"[/bold cyan] Puck said, flying ahead.
[bold cyan]"Word problems are math hiding inside stories.
You have to read carefully, figure out what the question
is really asking, and then pick the right tool —
add, subtract, multiply, or divide."[/bold cyan]

Nell looked around at all the little shops and smiled.

[bold white]Read the story. Find the math. Solve it![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "addition_fun": """
[bold green]The meadow bursts with color![/bold green]

Every flower blooms twice as bright, and the numbers
dance together in the air.

[bold cyan]"You can add!"[/bold cyan] Puck cheers, doing a little flip.
[bold cyan]"Single digits, double digits — you put them together
like a pro. Next stop: taking things away!"[/bold cyan]

[bold white]Addition: mastered. Onward to subtraction![/bold white]
""",
    "subtraction_station": """
[bold green]The train whistle blows in celebration![/bold green]

Every car is perfectly balanced, and the station
hums with satisfaction.

[bold cyan]"Adding and subtracting — you've got both now,"[/bold cyan]
Puck says proudly. [bold cyan]"You can put things together
AND take them apart. That's powerful.
The multiplication garden is just ahead!"[/bold cyan]

[bold white]Two tools in your belt. Time for a third![/bold white]
""",
    "multiplication_tables": """
[bold green]The mirror garden sparkles![/bold green]

Every reflection shows a perfect times table,
and the rows of flowers bloom in unison.

[bold cyan]"Times tables!"[/bold cyan] Puck exclaims. [bold cyan]"You've got them!
2s, 3s, 5s, 7s, 8s, 9s, 10s — all of them.
Do you know what that means? You can count
[italic]anything[/italic] in groups now."[/bold cyan]

[bold white]Multiplication: unlocked. Division awaits![/bold white]
""",
    "division_basics": """
[bold green]The gems are perfectly shared![/bold green]

Every pile is equal, every friend is happy,
and the round table glows with golden light.

[bold cyan]"Four operations,"[/bold cyan] Puck says quietly. [bold cyan]"Add, subtract,
multiply, divide. You know them all now.
But knowing them separately is one thing.
Using them together? That's the real magic."[/bold cyan]

[bold white]One more zone. The word problems are waiting.[/bold white]
""",
    "word_problems": """
[bold green]The whole town celebrates![/bold green]

The bakery, the toy store, the lemonade stand —
everyone cheers as Nell walks through.

[bold cyan]"You did it,"[/bold cyan] Puck says softly. [bold cyan]"You didn't just learn
math — you learned to [italic]use[/italic] math. To read a story,
find the hidden numbers, and solve the puzzle.
That's what math is for. That's the real magic."[/bold cyan]

The golden castle at the end of the playground
opens its doors.

[bold white]The Math Playground is yours. You solved every puzzle![/bold white]
""",
}

BOSS_INTROS = {
    "addition_fun": "The biggest flowers in the meadow merge together in a burst of petals. [bold yellow]\"One last addition — the biggest numbers yet! You've got this!\"[/bold yellow]",
    "subtraction_station": "The train's final car carries the trickiest subtraction yet. [bold yellow]\"Borrowing from the tens — the ultimate subtraction move! Think carefully!\"[/bold yellow]",
    "multiplication_tables": "The largest mirror in the garden flashes with a golden equation. [bold yellow]\"The trickiest times table fact of all — can you crack it?\"[/bold yellow]",
    "division_basics": "A treasure chest opens to reveal one final sharing challenge. [bold yellow]\"Divide this one and you're a true division champion!\"[/bold yellow]",
    "word_problems": "The golden castle door displays a multi-step puzzle carved in stone. [bold yellow]\"The ultimate word problem — use everything you've learned!\"[/bold yellow]",
}
