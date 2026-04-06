"""
story.py — Narrative for the Letters skill pack.

Nell discovers the Primer and learns to read with the help of a
friendly companion named Puck, a small glowing creature who lives
inside the book and guides her through the world of letters and words.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]

Once upon a time, a little girl found a very special book.

The cover was the color of midnight blue, with tiny golden stars that
[italic]actually sparkled[/italic] when she tilted it toward the light.
When she opened the first page, a small glowing creature floated up
from between the words — no bigger than a firefly, but much friendlier.

[bold cyan]"Hello!"[/bold cyan] it said. [bold cyan]"My name is Puck. I've been waiting for you!"[/bold cyan]

The girl blinked. [bold white]"A talking book?"[/bold white]

[bold cyan]"Not just any book,"[/bold cyan] Puck said, spinning in a happy circle. [bold cyan]"THE book.
The one that will teach you everything — starting with the most
important skill of all. The one that unlocks all the others."[/bold cyan]

[bold white]"What's that?"[/bold white]

[bold cyan]"Reading, of course!"[/bold cyan]

Puck landed on the first page and pointed to a big golden letter.

[bold cyan]"Every story ever told, every adventure ever had,
every secret ever discovered — they're all waiting for you,
right here in these marks on the page. Once you know what
they say, [italic]no door will ever be closed to you.[/italic]"[/bold cyan]

The girl sat down, pulled the book onto her lap, and looked at
the letter Puck was pointing to.

[bold white]She was ready to begin.[/bold white]

[bold cyan]Are you ready too?[/bold cyan]
"""

ZONE_INTROS = {
    "punctuation_plaza": """
Puck pointed to a cheerful street where every sign was decorated
with tiny dots, curls, and squiggles.

[bold cyan]"These marks,"[/bold cyan] Puck said, [bold cyan]"are the traffic signals of writing.
Without them, words would all rush into each other
and no one would know where one thought ended
and another began."[/bold cyan]

A period glittered on the nearest sign. A question mark
curled elegantly above a doorway.

[bold white]Learn the marks. Learn what they mean.[/bold white]
""",
    "letter_garden": """
Puck flew to a beautiful garden, where each flower had a letter
written on it in bright colors.

[bold cyan]"This is the Letter Garden,"[/bold cyan] Puck said. [bold cyan]"Every letter has its own
sound. Once you know all twenty-six of them, you can read
[italic]any word in the world![/italic]"[/bold cyan]

The flowers swayed gently. The letters waited.

[bold white]What sound does each letter make?[/bold white]
Let's find out together!
""",
    "vowel_pond": """
Puck led the way to a shimmering pond.

[bold cyan]"These are the Vowel Fish,"[/bold cyan] Puck said. [bold cyan]"They're special — only five
letters, but they appear in almost every single word. Their sounds
can change depending on what's around them!"[/bold cyan]

Five glowing fish leaped up from the water:
[bold yellow]A, E, I, O, U[/bold yellow]

[bold white]Short sounds and long sounds — can you tell them apart?[/bold white]
""",
    "blend_bridge": """
Puck pointed to a bridge made of letter blocks.

[bold cyan]"When two letters stand together, they often blend their sounds,"[/bold cyan]
Puck explained. [bold cyan]"Like friends holding hands — they each keep
their own sound, but they say it SO fast it sounds like one thing."[/bold cyan]

[italic]BR, ST, PL, TR...[/italic]

[bold white]Cross the bridge! Put the sounds together![/bold white]
""",
    "word_workshop": """
[bold cyan]"Now,"[/bold cyan] said Puck, [bold cyan]"we build!"[/bold cyan]

In a cozy workshop, letters floated in the air like pieces of a puzzle.
Put them in the right order, and they became words.
Put the words together, and they became [italic]meaning.[/italic]

[bold white]Take letters. Build words. Discover what they say.[/bold white]
""",
    "sentence_city": """
Puck spread wings wide as Nell looked out over a city made entirely
of words — buildings that were sentences, streets that were paragraphs.

[bold cyan]"A sentence is a complete thought,"[/bold cyan] Puck said. [bold cyan]"It has someone
doing something. Everything in this city is a thought someone wanted
to share. Can you read what they wrote?"[/bold cyan]

[bold white]Read the sentences. Understand the thoughts.[/bold white]
""",
    "rhyming_river": """
Puck dipped a tiny wing into a sparkling river.

[bold cyan]"Listen,"[/bold cyan] Puck said. [bold cyan]"Do you hear that? The river has a sound —
and some words sound just like it. Cat, hat, bat, mat — they all
flow together because they share the same ending."[/bold cyan]

The water rippled with words, all rhyming in soft little waves.

[bold white]Find the words that sound the same at the end.[/bold white]
""",
    "sight_word_station": """
Puck zipped to a little train station with words on all the signs.

[bold cyan]"These,"[/bold cyan] Puck said proudly, [bold cyan]"are the magic words. Every reader
knows them by heart — without even sounding them out! The, and,
is, it, in, on, was, are... they show up in almost every sentence,
like old friends."[/bold cyan]

[bold white]Learn these magic words. Your eyes will recognize them forever.[/bold white]
""",
    "reading_full_sentences": """
Puck opened a cozy door into a warm reading room.

[bold cyan]"You've learned the letters. You've built the words."[/bold cyan] Puck settled
onto a small cushion. [bold cyan]"Now we put it all together. A sentence
tells you something real — who is there, what they're doing,
and where it's all happening. Read it, and the whole picture
comes alive in your mind."[/bold cyan]

[bold white]Read carefully. Every word is a clue.[/bold white]
""",
    "word_building": """
Puck flew to a cozy little workbench covered in letter tiles.

[bold cyan]"Here's where the magic really happens,"[/bold cyan] Puck said with a grin.
[bold cyan]"Take a letter here, snap it onto a piece there — and suddenly
you have a [italic]word![/italic] A real thing with a real meaning."[/bold cyan]

A little [bold yellow]S[/bold yellow] tile glowed invitingly on the bench.

[bold white]Snap the letters together. What words can you build?[/bold white]
""",
    "story_time": """
The Primer's pages began to glow, and a tiny stage rose up
from the center of the book — red curtains, a little spotlight,
everything.

[bold cyan]"Welcome to Story Time Theater!"[/bold cyan] Puck announced, doing a small bow.
[bold cyan]"A story is more than just words on a page. It's a picture
in your mind — characters, places, things happening.
Read carefully, and you'll know everything."[/bold cyan]

The curtain opened. A little story waited.

[bold white]Read every word. The answers are in there![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "punctuation_plaza": """
[bold green]The plaza signs glow with every mark in place![/bold green]

Periods, question marks, exclamation marks, commas —
they all shine in their rightful spots.

[bold cyan]"Now your sentences have voices,"[/bold cyan] Puck says happily.
[bold cyan]"A period says [italic]I'm done.[/italic]
A question mark says [italic]I'm wondering.[/italic]
An exclamation mark says [italic]I feel it![/italic]
And a comma says [italic]wait just a moment...[/italic]"[/bold cyan]

[bold white]Punctuation is yours now, forever.[/bold white]
""",
    "letter_garden": """
[bold green]The Letter Garden glows![/bold green]

Every flower stands bright and tall. You know what each letter says.

[bold cyan]"You've done it!"[/bold cyan] Puck cheers. [bold cyan]"Twenty-six letters. Twenty-six sounds.
That's the whole alphabet — yours now, forever!"[/bold cyan]

The letters hum happily as you walk through the garden.
A new path has opened, leading toward the sparkling pond...
""",
    "vowel_pond": """
[bold green]The Vowel Fish leap with joy![/bold green]

The five vowels spin in joyful circles around you.

[bold cyan]"Now you know the special ones,"[/bold cyan] Puck says. [bold cyan]"A-E-I-O-U.
Short sounds. Long sounds. They're yours!"[/bold cyan]

The pond shimmers. The bridge ahead comes into view...
""",
    "blend_bridge": """
[bold green]The bridge is crossed![/bold green]

The letter blocks cheer as you reach the other side.

[bold cyan]"Look at that!"[/bold cyan] Puck says. [bold cyan]"You can hear the blend now, can't you?
BR and ST and TR — your ear is getting so sharp!"[/bold cyan]

The workshop is just ahead, and the letters are ready to be built into words...
""",
    "word_workshop": """
[bold green]The Workshop is buzzing![/bold green]

Words float around you like friendly butterflies — words you made!

[bold cyan]"You built real words,"[/bold cyan] Puck says proudly. [bold cyan]"CAT. TREE. JUMP. BLUE.
Each one means something. Each one is a little key that opens
a little door in the world of understanding."[/bold cyan]

The city glows on the horizon. Time to read what's written there!
""",
    "sentence_city": """
[bold green]The City is alive with your reading![/bold green]

Buildings light up as you read each sentence. The whole city buzzes.

[bold cyan]"You did it,"[/bold cyan] Puck says quietly. [bold cyan]"You read. Real sentences.
Real thoughts that real people wanted to share with you.
This is what it means to be a reader."[/bold cyan]

A door has opened — with a bigger adventure waiting on the other side.
""",
    "rhyming_river": """
[bold green]The river rings with rhymes![/bold green]

Words drift by in matching pairs — cat and hat, run and fun,
dog and log — all flowing happily together.

[bold cyan]"Your ear is tuned now,"[/bold cyan] Puck says with delight.
[bold cyan]"Once you hear rhymes, you hear them everywhere — in songs,
in poems, in your own thoughts! The Sight Word Station is next."[/bold cyan]
""",
    "sight_word_station": """
[bold green]The signs all glow![/bold green]

Every word on every sign is bright and clear.
The, and, is, it, was — you know them all by heart now.

[bold cyan]"Those words live in your eyes now,"[/bold cyan] Puck says happily.
[bold cyan]"Every time you see them on a page, your brain will
recognize them in a blink. That's what makes reading fast!"[/bold cyan]

The Reading Room door swings open just ahead...
""",
    "reading_full_sentences": """
[bold green]The Reading Room fills with light![/bold green]

Every sentence on the walls glows warmly.

[bold cyan]"You did something wonderful today,"[/bold cyan] Puck says softly.
[bold cyan]"You read sentences. You understood stories.
Who was there. What they did. Where they were.
You're a reader — truly and completely."[/bold cyan]

[bold white]Every book in the world is waiting for you now.[/bold white]
""",
    "word_building": """
[bold green]The workshop sparks with new words![/bold green]

Letter tiles float up from the bench and arrange themselves
into a glowing banner of words — SUN, HAT, BIG, MAT, PLOP, SAT.

[bold cyan]"Look at all those words,"[/bold cyan] Puck says, a little misty-eyed.
[bold cyan]"You built every single one. Letters into words —
that's the first step of all writing, all reading,
all stories ever told."[/bold cyan]

[bold white]The theater stage is ready. A story is waiting![/bold white]
""",
    "story_time": """
[bold green]The curtain falls to wild applause![/bold green]

The tiny stage is bright with the warmth of all the stories told.

[bold cyan]"Do you feel that?"[/bold cyan] Puck asks quietly. [bold cyan]"That's what it feels like
to truly understand what you read. Not just the words —
but the [italic]meaning[/italic] behind them. Who was there, what they did,
why it happened."[/bold cyan]

[bold white]You are a reader. A true, real, wonderful reader.[/bold white]
""",
}

BOSS_INTROS = {
    "punctuation_plaza": "The last sign on the street is blank at the end. [bold yellow]\"One sentence needs its mark — which one belongs there? You know this!\"[/bold yellow]",
    "letter_garden": "Puck floats to the tallest flower. [bold yellow]\"The hardest letters are waiting at the center of the garden. You're ready for them!\"[/bold yellow]",
    "vowel_pond": "The biggest fish surfaces. [bold yellow]\"This one can make both a short sound AND a long sound. Can you tell which is which?\"[/bold yellow]",
    "blend_bridge": "A giant block with three letters stands in the middle of the bridge. [bold yellow]\"Three letters, all blending together! Listen carefully and you'll hear all three.\"[/bold yellow]",
    "word_workshop": "The letters rearrange into a long word. [bold yellow]\"This one has many pieces — but you know each piece already. Sound it out!\"[/bold yellow]",
    "sentence_city": "The tallest building in the city is covered in words. [bold yellow]\"One long sentence, all the way to the top. Read it — and the whole city celebrates!\"[/bold yellow]",
    "rhyming_river": "Puck hovers over a ripple where two words float side by side. [bold yellow]\"Can you complete the rhyme? Think about the ending sound!\"[/bold yellow]",
    "sight_word_station": "The last sign at the station flickers. [bold yellow]\"This sentence is full of sight words — read it and prove you know them all!\"[/bold yellow]",
    "reading_full_sentences": "A little framed story hangs on the reading room wall. [bold yellow]\"Read every sentence. Then answer the question — the answer is in there somewhere!\"[/bold yellow]",
    "word_building": "A pile of letter tiles on the workbench begins to glow. [bold yellow]\"The trickiest word of all — every letter has to go in just the right place!\"[/bold yellow]",
    "story_time": "The spotlight on the tiny stage brightens and a longer story appears. [bold yellow]\"Read the whole thing carefully — then I'll ask you the most important question of all!\"[/bold yellow]",
}
