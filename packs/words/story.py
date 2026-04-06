"""
story.py — Narrative for the Words & Language skill pack.

Puck opens the Word Workshop — a magical place inside the Primer where
letters dance, words combine, and language itself comes alive. The reader
learns compound words, synonyms, prefixes, homophones, parts of speech,
figurative language, vocabulary roots, and storytelling.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Word Workshop[/bold yellow]

Puck appeared on a blank page — completely blank, not a single word
anywhere. But Puck was grinning, which usually meant something
extraordinary was about to happen.

[bold cyan]"Words,"[/bold cyan] Puck said, tapping the empty page with one wing.

A single letter — [bold yellow]A[/bold yellow] — rose from the paper, glowing.

[bold cyan]"Words are the most powerful tools in the world.
With them, you can tell someone you love them.
You can describe a dragon. You can make someone laugh
or cry or think about something they've never thought before."[/bold cyan]

More letters floated up: [bold yellow]B, C, D, E...[/bold yellow]
They swirled and rearranged themselves into WORDS,
then the words linked together into SENTENCES,
and the sentences built themselves into a tiny, shimmering STORY
that hovered in the air.

[bold cyan]"But to use words well,"[/bold cyan] Puck said, catching a letter
and holding it up, [bold cyan]"you need to understand how they work.
How they fit together. How little pieces change their meaning.
How they sound, and how they trick you, and how they
paint pictures in your mind."[/bold cyan]

The blank page was blank no longer. A door had appeared —
a workshop door, covered in letters and punctuation marks,
with a sign that read:

[bold yellow]THE WORD WORKSHOP[/bold yellow]
[italic]Where Language Comes Alive[/italic]

Puck pushed it open. Light spilled out.

[bold cyan]"Ready to step inside?"[/bold cyan]

[bold white]Your adventure with words begins now.[/bold white]
"""

ZONE_INTROS = {
    "compound_words": """
Puck led the way to a workbench covered in word-tiles — hundreds of them,
each with a single word printed in bright ink.

[bold cyan]"Some words,"[/bold cyan] Puck said, picking up two tiles,
[bold cyan]"are actually TWO words stuck together.
'Sun' and 'flower' make 'sunflower'.
'Rain' and 'bow' make 'rainbow'.
We call them compound words — and they're everywhere!"[/bold cyan]

Puck slid the tiles together with a satisfying CLICK.
A tiny sunflower sprouted from the page.

[bold white]Let's learn to build compound words![/bold white]
""",
    "synonyms_antonyms": """
Puck opened a cabinet full of word-pairs — some glowing the same colour,
some glowing opposite colours.

[bold cyan]"Some words mean the same thing,"[/bold cyan] Puck said,
holding up 'happy' and 'joyful' — both glowing gold.
[bold cyan]"We call those synonyms."[/bold cyan]

Then Puck held up 'hot' and 'cold' — one red, one blue.

[bold cyan]"And some words mean the opposite.
Those are antonyms. Knowing both makes you a
word wizard — you'll always find exactly the right word."[/bold cyan]

[bold white]Let's explore the twins and the opposites![/bold white]
""",
    "prefixes_suffixes": """
Puck pulled out a box of tiny word-pieces — each one just two or three
letters long. Some were labelled 'FRONT' and some were labelled 'BACK'.

[bold cyan]"These,"[/bold cyan] Puck said proudly, [bold cyan]"are the building blocks of words.
Stick 'un-' on the front of 'happy' and you get 'unhappy'.
Stick '-ful' on the end of 'hope' and you get 'hopeful'.
These tiny pieces — prefixes at the front, suffixes at the back —
can change the meaning of ANY word."[/bold cyan]

Puck snapped a prefix onto a word. It transformed instantly!

[bold white]Let's learn the building blocks![/bold white]
""",
    "homophones": """
Puck held up three cards that all said the same thing — or did they?

[bold cyan]"Their. There. They're."[/bold cyan] Puck read each one aloud.
[bold cyan]"They sound exactly the same. But they mean
completely different things! English is full of these
sound-alike tricksters. They're called homophones —
'homo' means 'same' and 'phone' means 'sound'."[/bold cyan]

Puck shuffled the cards like a magician.

[bold cyan]"Mix them up, and your sentences go haywire.
Learn to tell them apart, and your writing will
be sharper than a knight's sword."[/bold cyan]

[bold white]Can you outsmart the homophones?[/bold white]
""",
    "parts_of_speech": """
Puck gathered a handful of words and laid them on the workbench
in a neat row.

[bold cyan]"Every word,"[/bold cyan] Puck said, [bold cyan]"has a JOB.
Nouns are the things: dragon, castle, dream.
Verbs are the actions: fly, build, imagine.
Adjectives describe the things: fierce, tall, wild.
Adverbs describe the actions: quickly, bravely, softly."[/bold cyan]

Each word lifted off the bench and put on a tiny hat
with its job title.

[bold cyan]"When every word does its job, the sentence sings."[/bold cyan]

[bold white]Let's find out what each word does![/bold white]
""",
    "figurative_language": """
Puck led the way to a room filled with impossible things —
a river made of music, clouds shaped like laughter,
and a tree whose leaves were made of stories.

[bold cyan]"This,"[/bold cyan] Puck said, spreading wings wide,
[bold cyan]"is where language stops being plain and starts
being MAGICAL. Similes compare things: 'brave as a lion'.
Metaphors transform things: 'the world is a stage'.
Alliteration makes sounds dance: 'Peter Piper picked'.
And onomatopoeia? CRASH! BANG! SIZZLE!"[/bold cyan]

The whole room vibrated with sound and colour.

[bold white]Welcome to the Imagination Engine![/bold white]
""",
    "vocabulary_building": """
Puck stood before an enormous vault door, covered in ancient
Greek and Latin letters.

[bold cyan]"Behind this door,"[/bold cyan] Puck whispered,
[bold cyan]"are all the words you haven't learned yet.
But here's the secret: you don't need to memorise every one.
You just need three keys."[/bold cyan]

Three golden keys floated in the air:
[bold yellow]Context Clues · Dictionary Skills · Word Roots[/bold yellow]

[bold cyan]"Context clues help you guess a word's meaning from
the sentence around it. A dictionary gives you the exact definition.
And word roots — ancient Greek and Latin pieces —
unlock thousands of words at once."[/bold cyan]

[bold white]Let's unlock the Word Vault![/bold white]
""",
    "storytelling": """
Puck led the way to the very last room in the Word Workshop —
and it was magnificent. A great forge blazed at its centre,
and molten words flowed like rivers of gold.

[bold cyan]"Everything you've learned,"[/bold cyan] Puck said softly,
[bold cyan]"has been leading here. Compound words. Synonyms.
Prefixes. Parts of speech. Figurative language. Vocabulary.
All of it was training for this moment."[/bold cyan]

Puck looked up with shining eyes.

[bold cyan]"Because NOW — you're going to learn to tell STORIES.
Every story needs characters, a setting, a problem, and a plot.
Every story needs a beginning, a middle, and an end.
And every story needs a storyteller."[/bold cyan]

Puck pointed a wing directly at the reader.

[bold cyan]"That's you."[/bold cyan]

[bold white]Welcome to the Story Forge![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "compound_words": """
[bold green]The word-tiles glow and lock together — every compound word complete![/bold green]

Sunflower, rainbow, butterfly, bookworm, toothbrush —
all shining on the workbench in a row.

[bold cyan]"You see it now, don't you?"[/bold cyan] Puck beams.
[bold cyan]"Two small words, joined together, making something new.
English is FULL of these — and now you'll spot them everywhere."[/bold cyan]

The next cabinet opens, filled with twins and opposites...
""",
    "synonyms_antonyms": """
[bold green]Every synonym glows gold. Every antonym glows in opposite colours![/bold green]

Happy and joyful. Hot and cold. Brave and cowardly.
Ancient and modern. The whole cabinet is organized and gleaming.

[bold cyan]"You've got a bigger word-bank now,"[/bold cyan] Puck says.
[bold cyan]"When you write, you'll never be stuck using the same
word twice. You've got CHOICES — and choices are power."[/bold cyan]

A box of tiny word-pieces rattles eagerly. Prefixes and suffixes are next...
""",
    "prefixes_suffixes": """
[bold green]The building blocks snap into place — every prefix and suffix mastered![/bold green]

Un-, re-, pre- on the left. -ful, -less, -ness on the right.
And in the middle, ordinary words waiting to be transformed.

[bold cyan]"You can change ANY word now,"[/bold cyan] Puck says proudly.
[bold cyan]"Make it opposite. Make it happen again. Make it
full of something or without something.
That's real word power."[/bold cyan]

Three identical-sounding cards float out of the next drawer. The tricksters await...
""",
    "homophones": """
[bold green]Every homophone sorted, every trickster tamed![/bold green]

Their / there / they're — filed correctly.
To / too / two — each in its place.
Its / it's — no more confusion.

[bold cyan]"You've beaten the tricksters!"[/bold cyan] Puck cheers.
[bold cyan]"Most grown-ups STILL get these wrong, you know.
But not you. Not anymore."[/bold cyan]

Words in the next room are putting on tiny hats. The Word Jobs are calling...
""",
    "parts_of_speech": """
[bold green]Every word has its hat on — every job assigned![/bold green]

Nouns wear blue. Verbs wear red. Adjectives wear gold. Adverbs wear green.
Every word in the workshop knows exactly where it belongs.

[bold cyan]"You understand the grammar of English now,"[/bold cyan] Puck says warmly.
[bold cyan]"When you read a sentence, you can see its skeleton —
which word is the thing, which is the action, which is the description.
That's a real superpower."[/bold cyan]

Strange and wonderful sounds come from the next room. The Imagination Engine awaits...
""",
    "figurative_language": """
[bold green]The Imagination Engine roars and shimmers with colour![/bold green]

Similes sparkle. Metaphors blaze. Alliteration ripples like a river.
Onomatopoeia pops and crackles. Personification makes the walls dance.

[bold cyan]"Language isn't just information,"[/bold cyan] Puck says quietly.
[bold cyan]"It's art. It's music. It's painting with words.
And you've just learned to paint."[/bold cyan]

A great vault door looms ahead, covered in ancient letters. The Word Vault awaits...
""",
    "vocabulary_building": """
[bold green]The Vault swings open — thousands of words glitter inside![/bold green]

Context clues, dictionary skills, and word roots — all three keys
in your pocket. Latin and Greek letters glow warmly: aqua, tele, bio, graph.

[bold cyan]"You'll never be stopped by a word you don't know,"[/bold cyan]
Puck says. [bold cyan]"You have the tools to figure out ANY word
you meet — in any book, any article, any conversation.
That's what real readers do."[/bold cyan]

A forge blazes ahead. The final room. The Story Forge awaits...
""",
    "storytelling": """
[bold green]The Story Forge blazes with golden light![/bold green]

Beginning, middle, end. Characters, setting, plot, conflict.
Every tool of storytelling — learned, practised, and ready to use.

[bold cyan]"You've done it."[/bold cyan] Puck's wings spread wide, glowing.
[bold cyan]"You came into the Word Workshop knowing how to read.
You're leaving knowing how to WRITE. How to build words,
choose words, understand words, and weave them into stories."[/bold cyan]

Puck closes the Workshop door gently. The sign glows one last time:

[bold yellow]THE WORD WORKSHOP[/bold yellow]
[italic]Where Language Came Alive — For You[/italic]

[bold white]Scribbler. Speller. Wordsmith. Poet. Author. Bard.
That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "compound_words": "Puck pulls out a giant hammer labelled 'SMASH' and sets two tricky word-tiles on the anvil. [bold yellow]\"Not every pair of words makes a compound word! Can you spot the REAL one?\"[/bold yellow]",
    "synonyms_antonyms": "Puck shuffles a deck of word-cards and fans them out. [bold yellow]\"Three of these pairs are synonyms — words that mean the SAME. But one pair is antonyms — opposites! Find the odd one out!\"[/bold yellow]",
    "prefixes_suffixes": "Puck stacks three word-blocks on the workbench — prefix, root, and suffix. [bold yellow]\"Let's build one BIG word from three pieces. Think carefully about what each piece means!\"[/bold yellow]",
    "homophones": "Puck sets up an obstacle course of homophone traps — every wrong word triggers a buzzer! [bold yellow]\"Only the sharpest speller survives the Homophone Gauntlet! Every word must be PERFECT.\"[/bold yellow]",
    "parts_of_speech": "A great Grammar Guardian — a stone statue covered in words — rumbles to life! [bold yellow]\"Name every part of speech in the right order, and the Guardian lets you pass!\"[/bold yellow]",
    "figurative_language": "The Imagination Engine roars! Gears of metaphor, pistons of alliteration, and clouds of onomatopoeia swirl together. [bold yellow]\"Can you spot TWO figurative techniques in a single sentence? Only a true word artist can!\"[/bold yellow]",
    "vocabulary_building": "The Vault Keeper — an enormous stone door carved with Greek and Latin letters — demands a password! [bold yellow]\"Use your knowledge of word roots to unlock the greatest word in the vault!\"[/bold yellow]",
    "storytelling": "The Story Forge blazes white-hot. Molten words pour into a mold shaped like an open book. [bold yellow]\"One sentence. Character. Setting. Problem. Write the perfect opening line, and the Forge accepts you as a Master Storyteller!\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "compound_crafter": (
        "Compound Crafter",
        "Joined words together like a master builder!",
    ),
    "synonym_seeker": (
        "Synonym Seeker",
        "Found twins and opposites across the whole language!",
    ),
    "affix_architect": (
        "Affix Architect",
        "Mastered prefixes and suffixes — the building blocks of words!",
    ),
    "homophone_hunter": (
        "Homophone Hunter",
        "Tamed every sound-alike trickster in the English language!",
    ),
    "grammar_guardian": (
        "Grammar Guardian",
        "Named every part of speech and put every word in its place!",
    ),
    "imagination_igniter": (
        "Imagination Igniter",
        "Wielded similes, metaphors, alliteration, and onomatopoeia like magic!",
    ),
    "vault_keeper": (
        "Vault Keeper",
        "Unlocked the Word Vault with context clues, dictionaries, and ancient roots!",
    ),
    "master_storyteller": (
        "Master Storyteller",
        "Forged a story with characters, setting, plot, and heart!",
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
