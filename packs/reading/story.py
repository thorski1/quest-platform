"""
story.py — Narrative for The Reading Room skill pack.

Puck opens The Reading Room — a magical library inside the Primer where
stories come alive, words reveal their secrets, and every book is a door
to a new world. The reader learns context clues, story elements,
main idea and details, fact vs opinion, and reading for fun.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Reading Room[/bold yellow]

Puck appeared sitting on top of a very tall stack of books — so tall
that the top book wobbled dangerously whenever Puck shifted.

[bold cyan]"Books,"[/bold cyan] Puck said, patting the cover of the topmost one.

A single page fluttered open, and a tiny dragon flew out of it,
circled the room once, and landed on Puck's shoulder.

[bold cyan]"Books are doors. Every single one. Open a book
and you might step into a castle, or a spaceship,
or a jungle, or someone else's life.
You might meet a pirate or a president
or a penguin who solves mysteries."[/bold cyan]

More pages fluttered open. Characters and creatures of every kind
drifted out — knights and scientists, talking animals and brave children —
until the air was filled with stories swirling like snow.

[bold cyan]"But here's the secret,"[/bold cyan] Puck whispered, leaning close.
[bold cyan]"Reading isn't just about the words on the page.
It's about what you DO with those words.
You look for clues. You make guesses.
You find the big idea hiding inside.
You figure out what's true and what's just
someone's opinion. And THEN..."[/bold cyan]

Puck grinned and pushed open an enormous door
that hadn't been there a moment ago.
Behind it was a room filled with books — floor to ceiling,
wall to wall — each one glowing softly.

[bold yellow]THE READING ROOM[/bold yellow]
[italic]Where Every Book Is a Door[/italic]

[bold cyan]"Ready to become a real reader?"[/bold cyan]

[bold white]Your reading adventure begins now.[/bold white]
"""

ZONE_INTROS = {
    "reading_clues": """
Puck stopped at a shelf labelled [bold yellow]MYSTERY WORDS[/bold yellow] and pulled
out a book. Some of the words inside were glowing — but they were words
the reader had never seen before.

[bold cyan]"Don't worry,"[/bold cyan] Puck said with a wink.
[bold cyan]"You don't need a dictionary for these.
The SECRET is that the other words in the sentence
are whispering the answer to you. They're called
context clues — little hints hiding in plain sight."[/bold cyan]

Puck also held up a crystal ball.

[bold cyan]"And THIS is for predictions — using clues
to guess what happens NEXT in a story.
Detectives do it. Scientists do it.
And now YOU'RE going to do it."[/bold cyan]

[bold white]Let's learn to read between the lines![/bold white]
""",
    "story_elements": """
Puck led the way to a workshop in the back of the Reading Room.
On the workbench were three glowing building blocks, each labelled:
[bold yellow]CHARACTER · SETTING · PLOT[/bold yellow]

[bold cyan]"Every story ever told,"[/bold cyan] Puck said, stacking the blocks,
[bold cyan]"is built from these three things.
Characters are the WHO — the people or creatures the story is about.
Setting is the WHERE and WHEN — the place and time.
And plot is the WHAT — the events that happen."[/bold cyan]

Puck snapped the blocks together and a tiny story sprang to life
on the workbench — characters moving through a setting, facing a problem.

[bold cyan]"Take a story apart, and you'll understand how
EVERY story works. Ready?"[/bold cyan]

[bold white]Let's discover the building blocks of stories![/bold white]
""",
    "main_idea_details": """
Puck stood before a giant painting on the wall of the Reading Room.
From far away, it showed a beautiful mountain landscape.
But up close, it was made of thousands of tiny details —
trees, rivers, animals, clouds, flowers.

[bold cyan]"Reading is like this painting,"[/bold cyan] Puck said.
[bold cyan]"Every passage has a BIG IDEA — that's the whole picture,
the mountain you see from far away. And it has DETAILS —
the tiny pieces that make up the picture."[/bold cyan]

Puck stepped back and spread both wings wide.

[bold cyan]"A great reader can see BOTH — the big picture
AND the tiny details. That's what we're going to learn."[/bold cyan]

[bold white]Let's find the big ideas and the details that support them![/bold white]
""",
    "fact_vs_opinion": """
Puck set up two boxes on a table — one labelled [bold green]FACT[/bold green]
and one labelled [bold magenta]OPINION[/bold magenta].

[bold cyan]"Here's something REALLY important,"[/bold cyan] Puck said seriously.
[bold cyan]"Not everything you read is true.
Some sentences are FACTS — things that can be proven.
'Water freezes at zero degrees.' You can test that!
But some sentences are OPINIONS — things someone
believes or feels. 'Winter is the best season.'
You can't prove that — it's just what someone thinks."[/bold cyan]

Puck held up a newspaper, a website, and a book review.

[bold cyan]"The real world is FULL of facts and opinions
mixed together. Your job is to sort them out.
Ready to become a truth detective?"[/bold cyan]

[bold white]Let's learn to separate facts from opinions![/bold white]
""",
    "reading_for_fun": """
Puck threw open the biggest doors in the Reading Room,
revealing an enormous hall filled with shelves stretching
to the ceiling — each one labelled with a different genre.

[bold yellow]FANTASY · MYSTERY · SCIENCE FICTION · BIOGRAPHY
NON-FICTION · POETRY · HISTORICAL FICTION · FAIRY TALES[/bold yellow]

[bold cyan]"This,"[/bold cyan] Puck said, spinning with delight,
[bold cyan]"is the BEST part of reading. CHOOSING what to read!
Every genre is like a different flavour of ice cream.
Fantasy is magical. Mystery is thrilling. Science fiction
is mind-blowing. Biography is inspiring."[/bold cyan]

Puck landed on a shelf and pulled out a book.

[bold cyan]"You'll also learn how books are built —
tables of contents, glossaries, indexes — and how
libraries are organized so you can find ANYTHING.
Because the best readers know how to find their next
favourite book."[/bold cyan]

[bold white]Let's explore the world of reading![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "reading_clues": """
[bold green]Every mystery word decoded, every prediction spot-on![/bold green]

The glowing words on the shelf have dimmed — because they're
no longer mysterious. You know them all.

[bold cyan]"You see it now, don't you?"[/bold cyan] Puck beams.
[bold cyan]"The clues were there all along — hiding in the
sentences around the tricky words. And your predictions?
Sharp as a detective's."[/bold cyan]

Puck points to a workshop door up ahead, labelled
CHARACTER · SETTING · PLOT...
""",
    "story_elements": """
[bold green]Characters, settings, and plots — you've mastered them all![/bold green]

The building blocks on the workbench glow with a steady light.
Every story that springs from them makes perfect sense now.

[bold cyan]"You can take ANY story apart,"[/bold cyan] Puck says proudly.
[bold cyan]"Who's in it? Where does it happen? What's the problem?
How does it end? You see the skeleton of every story now.
That's a real reader's superpower."[/bold cyan]

A giant painting on the wall beckons. The big picture awaits...
""",
    "main_idea_details": """
[bold green]Big ideas found, supporting details lined up perfectly![/bold green]

The painting on the wall shimmers — you can see both
the grand mountain AND every tiny tree, river, and flower.

[bold cyan]"Main idea and details,"[/bold cyan] Puck says warmly.
[bold cyan]"The umbrella and the raindrops. The mountain and the trees.
You'll never read a paragraph the same way again —
you'll always see the big picture AND the small pieces."[/bold cyan]

Two boxes sit on a table ahead — one green, one purple.
Truth-sorting awaits...
""",
    "fact_vs_opinion": """
[bold green]Every fact checked, every opinion spotted![/bold green]

The FACT box and OPINION box are both full and perfectly sorted.
Not a single one in the wrong place.

[bold cyan]"This might be the most important skill of all,"[/bold cyan]
Puck says quietly. [bold cyan]"Out in the real world — in news,
in advertisements, in things people say — facts and opinions
are mixed together ALL the time. But not for you.
Not anymore. You can see the difference."[/bold cyan]

Enormous doors swing open ahead, revealing shelves that stretch to the sky...
""",
    "reading_for_fun": """
[bold green]Genres explored, book parts mastered, library skills unlocked![/bold green]

The hall of shelves glows warmly. Every genre sign is lit up,
every book part understood, and the library holds no more mysteries.

[bold cyan]"You've done it."[/bold cyan] Puck's wings spread wide, glowing.
[bold cyan]"You came into the Reading Room knowing how to read words.
You're leaving knowing how to READ. Really read.
Find clues. Understand stories. Spot the big idea.
Tell fact from opinion. And find your next favourite book
in any library in the world."[/bold cyan]

Puck closes the Reading Room door gently. The sign glows one last time:

[bold yellow]THE READING ROOM[/bold yellow]
[italic]Where Every Book Became a Door — For You[/italic]

[bold white]Page Turner. Story Spotter. Idea Finder. Truth Teller. Reading Champion.
That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "reading_clues": "Puck shines a flashlight into a dark passage full of unfamiliar words. [bold yellow]\"This one needs ALL your clue skills — context clues AND your own knowledge combined. Think like a detective!\"[/bold yellow]",
    "story_elements": "Puck opens a storybook that's all jumbled up — characters mixed with settings, plots out of order. [bold yellow]\"Only a true Story Builder can untangle this one. Look at every detail — what characters DO and what they FEEL!\"[/bold yellow]",
    "main_idea_details": "Puck stands before a glowing pyramid made of words — details at the bottom, the main idea shining at the top. [bold yellow]\"This passage is tricky — the main idea isn't obvious. You'll need to connect ALL the details to find it!\"[/bold yellow]",
    "fact_vs_opinion": "Puck holds up a magnifying glass labelled TRUTH and a passage full of facts and opinions mixed together. [bold yellow]\"The real world does this ALL the time — mixes facts and opinions in the same paragraph. Can you count them correctly?\"[/bold yellow]",
    "reading_for_fun": "Puck closes a book with a satisfied grin and opens it to a passage about a reader using EVERY book skill at once. [bold yellow]\"Table of contents, glossary, index — Mia used them all. Can you track the order? Only a true Reading Champion can!\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "clue_cracker": (
        "Clue Cracker",
        "Decoded every mystery word using context clues and predictions!",
    ),
    "story_builder": (
        "Story Builder",
        "Mastered characters, settings, plots, and story structure!",
    ),
    "idea_finder": (
        "Idea Finder",
        "Found the main idea and supporting details in every passage!",
    ),
    "truth_teller": (
        "Truth Teller",
        "Separated facts from opinions like a pro!",
    ),
    "reading_champion": (
        "Reading Champion",
        "Explored every genre and mastered all book and library skills!",
    ),
    "no_hints": (
        "Standing on Your Own",
        "Completed a zone without any hints!",
    ),
    "speed_reader": (
        "Quick Thinker",
        "Answered a question in under 10 seconds!",
    ),
}
