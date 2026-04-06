"""
story.py — Narrative for The Writer's Workshop skill pack.

Puck opens The Writer's Workshop — a magical studio inside the Primer where
words come alive, sentences take shape, and every child discovers the power
of putting thoughts on paper. The writer learns sentences & capitalization,
punctuation, story structure, descriptive writing, and writing for a purpose.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Writer's Workshop[/bold yellow]

Puck appeared at a wooden desk covered in ink bottles, feather quills,
and sheets of paper that seemed to glow faintly, as if waiting for
something important to be written on them.

[bold cyan]"Words,"[/bold cyan] Puck said, picking up a quill and twirling it
between tiny fingers.

A single drop of ink fell from the quill and landed on a blank page.
Where it landed, a flower bloomed — drawn entirely from words.
Petals made of adjectives, a stem made of verbs, leaves made of nouns.

[bold cyan]"Reading is wonderful — it lets you explore
other people's worlds. But WRITING?"[/bold cyan]

Puck grinned and tapped the page. More word-flowers sprouted,
then word-castles, word-dragons, word-oceans —
an entire world growing from ink and imagination.

[bold cyan]"Writing lets you BUILD your own world.
You can tell someone a story. You can write a letter
that makes someone smile. You can explain how to do
something, or invite someone to a party, or describe
a sunset so beautifully that someone who wasn't there
can SEE it."[/bold cyan]

Puck pushed open a heavy oak door and behind it was a workshop
filled with writing tools — pencils tall as trees, ink wells
deep as swimming pools, and paper that stretched to the horizon.

[bold yellow]THE WRITER'S WORKSHOP[/bold yellow]
[italic]Where Every Word You Write Has Power[/italic]

[bold cyan]"Ready to become a real writer?"[/bold cyan]

[bold white]Your writing adventure begins now.[/bold white]
"""

ZONE_INTROS = {
    "sentences_capitalization": """
Puck stopped at the first workbench, where wooden blocks shaped
like words sat in messy piles. Some blocks had big gold crowns
on top — the capital letters.

[bold cyan]"Before you can write ANYTHING,"[/bold cyan] Puck said,
stacking two blocks together,
[bold cyan]"you need to know what a SENTENCE is.
A sentence is the building block of all writing.
Every sentence needs two things: a WHO
and a WHAT THEY DID. Like puzzle pieces —
they only work when they fit together."[/bold cyan]

Puck placed a tiny gold crown on the first letter of a word.

[bold cyan]"And THIS is a capital letter — the crown that
every sentence gets to wear at the start.
Names get crowns too. And days of the week.
Let's learn the rules!"[/bold cyan]

[bold white]Let's build perfect sentences from the ground up![/bold white]
""",
    "punctuation_power": """
Puck led the way to a shelf lined with tiny, powerful marks —
dots, curly hooks, and straight lines with dots underneath.

[bold cyan]"These,"[/bold cyan] Puck said, picking up a period the size of a marble,
[bold cyan]"are the TRAFFIC SIGNALS of writing.
Periods are stop signs. Commas are pause signs.
Question marks say TELL ME MORE.
And exclamation points? Those are the ones
that SHOUT."[/bold cyan]

Puck tossed the period into a sentence and it stopped perfectly.

[bold cyan]"Without punctuation, writing is just a jumble
of words running into each other. WITH punctuation,
everything makes sense. Ready to master them?"[/bold cyan]

[bold white]Let's learn the traffic signals of writing![/bold white]
""",
    "parts_of_story": """
Puck stood before a huge blank storybook — three sections clearly
marked: [bold yellow]BEGINNING · MIDDLE · END[/bold yellow]

[bold cyan]"Every story ever written,"[/bold cyan] Puck said, tapping the first section,
[bold cyan]"has three parts. The BEGINNING introduces the characters
and the setting — that's the WHO and the WHERE.
The MIDDLE is where the excitement lives — the problem,
the adventure, the conflict.
And the END? That's where everything gets wrapped up."[/bold cyan]

Puck pulled out character figures, setting backdrops,
and problem cards, laying them across the workbench.

[bold cyan]"Today you're going to learn how stories are BUILT —
so that one day, you can build your own."[/bold cyan]

[bold white]Let's discover the architecture of stories![/bold white]
""",
    "descriptive_writing": """
Puck opened a door to a room filled with canvases — but instead of
paint and brushes, the easels held blank pages and coloured pencils.

[bold cyan]"Writing and painting aren't that different,"[/bold cyan] Puck said,
picking up a pencil that shimmered with colour.
[bold cyan]"A painter uses brushes and colour to make pictures.
A writer uses WORDS to make pictures — pictures that
appear in the reader's MIND."[/bold cyan]

Puck wrote a single word — [bold yellow]sparkle[/bold yellow] — and
the page shimmered.

[bold cyan]"Adjectives are your paintbrush. Similes are your
special effects. And your FIVE SENSES — sight, hearing,
smell, taste, touch — are the colours on your palette.
Let's paint some word pictures!"[/bold cyan]

[bold white]Let's paint pictures with words![/bold white]
""",
    "writing_for_purpose": """
Puck unlocked the final room of the Workshop, and inside were
real-world objects: envelopes, party invitations, recipe cards,
instruction manuals, and postcards from faraway places.

[bold cyan]"Everything we've learned so far — sentences, punctuation,
story structure, description — it all comes together HERE,"[/bold cyan]
Puck said, gesturing at the room.

[bold cyan]"Because in the REAL WORLD, writing isn't just about
stories. You write LETTERS to people you care about.
You write LISTS to stay organized. You write INSTRUCTIONS
so others can follow your steps. You write INVITATIONS
to bring people together."[/bold cyan]

Puck picked up a pen and a blank card.

[bold cyan]"This is where writing becomes a TOOL —
something you use every single day.
Ready to write for the real world?"[/bold cyan]

[bold white]Let's learn to write with purpose![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "sentences_capitalization": """
[bold green]Every sentence complete, every capital letter in its place![/bold green]

The wooden word-blocks on the workbench are perfectly stacked now —
each sentence standing tall with its capital crown shining.

[bold cyan]"You see it now, don't you?"[/bold cyan] Puck beams.
[bold cyan]"A sentence isn't just words thrown together —
it's a WHO and a WHAT THEY DID, wearing a capital
crown at the start and a punctuation mark at the end.
That's the foundation of ALL writing."[/bold cyan]

Puck points to a shelf of tiny, powerful marks ahead...
""",
    "punctuation_power": """
[bold green]Periods placed, commas curved, question marks hooked, exclamation points standing tall![/bold green]

The punctuation shelf glows with a steady light. Every mark
is in its right place, and every sentence reads perfectly.

[bold cyan]"You've mastered the traffic signals,"[/bold cyan] Puck says proudly.
[bold cyan]"Periods stop. Commas pause. Question marks ask.
Exclamation points shout. Without them, writing is
chaos — with them, it sings."[/bold cyan]

A huge blank storybook beckons from the next room...
""",
    "parts_of_story": """
[bold green]Beginnings opened, middles built, endings crafted![/bold green]

The blank storybook is blank no more — its three sections
glow with characters, settings, problems, and solutions.

[bold cyan]"You understand how stories WORK now,"[/bold cyan] Puck says warmly.
[bold cyan]"Beginning, middle, end. Characters, setting, problem.
Every story ever written follows this pattern —
and now you can build one yourself."[/bold cyan]

A room full of canvases and coloured pencils awaits...
""",
    "descriptive_writing": """
[bold green]Adjectives applied, similes crafted, senses awakened![/bold green]

The blank canvases in the room are now covered with vivid
word-paintings — scenes so descriptive you can almost
smell, hear, and feel them.

[bold cyan]"You're not just a writer now,"[/bold cyan] Puck says with wonder.
[bold cyan]"You're a word PAINTER. Adjectives, similes,
sensory details — you've got the whole palette.
You can make anyone see what YOU see,
feel what YOU feel."[/bold cyan]

One final room remains — where writing meets the real world...
""",
    "writing_for_purpose": """
[bold green]Letters written, lists organized, instructions clear, invitations sent![/bold green]

The final room of the Workshop glows warmly. Envelopes are sealed,
lists are checked off, instructions are crystal clear,
and invitations are ready to deliver.

[bold cyan]"You've done it."[/bold cyan] Puck's wings spread wide, glowing.
[bold cyan]"You came into the Workshop knowing how to hold a pen.
You're leaving knowing how to WRITE. Really write.
Build sentences. Use punctuation. Tell stories.
Paint pictures with words. And write for the real world —
letters, lists, instructions, invitations."[/bold cyan]

Puck closes the Workshop door gently. The sign glows one last time:

[bold yellow]THE WRITER'S WORKSHOP[/bold yellow]
[italic]Where Every Word You Wrote Had Power — Your Power[/italic]

[bold white]Sentence Builder. Punctuation Master. Story Architect.
Word Painter. Purpose Writer. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "sentences_capitalization": "Puck sets down a golden pen and a blank page. [bold yellow]\"This one's all you — build me a sentence from scratch. Subject, verb, capital letter, period. Show me you're a true Sentence Architect!\"[/bold yellow]",
    "punctuation_power": "Puck holds up a passage with NO punctuation at all — words crammed together in chaos. [bold yellow]\"A punctuation emergency! Only a true master can figure out where ALL the marks should go!\"[/bold yellow]",
    "parts_of_story": "Puck hands you a glowing quill and a blank page. [bold yellow]\"Forget multiple choice — this time YOU write the beginning of a story. Characters, setting, problem — build it from nothing!\"[/bold yellow]",
    "descriptive_writing": "Puck stands in a swirling thunderstorm on the page. [bold yellow]\"Paint this storm with WORDS — adjectives, similes, senses. Make me FEEL the rain and HEAR the thunder!\"[/bold yellow]",
    "writing_for_purpose": "Puck holds up a sealed envelope and a stamp. [bold yellow]\"Your friend is sick. Write them a real letter — greeting, body, closing. Show me writing with HEART.\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "sentence_architect": (
        "Sentence Architect",
        "Built perfect sentences with subjects, verbs, and capital letters!",
    ),
    "punctuation_master": (
        "Punctuation Master",
        "Mastered periods, commas, question marks, and exclamation points!",
    ),
    "story_architect": (
        "Story Architect",
        "Understood beginnings, middles, ends, characters, settings, and problems!",
    ),
    "word_painter": (
        "Word Painter",
        "Painted vivid pictures with adjectives, similes, and sensory details!",
    ),
    "purpose_writer": (
        "Purpose Writer",
        "Wrote letters, lists, instructions, and invitations for the real world!",
    ),
    "no_hints": (
        "Standing on Your Own",
        "Completed a zone without any hints!",
    ),
    "speed_writer": (
        "Quick Quill",
        "Answered a question in under 10 seconds!",
    ),
}
