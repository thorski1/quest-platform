"""
story.py -- Narrative for the Hangul skill pack.

An alien linguist has intercepted Korean transmissions and recruits
you to help decode Hangul, the most scientifically designed writing
system on the planet.
"""

INTRO_STORY = """
[bold red]LEARN KOREAN[/bold red]
[bold yellow]Chapter: The Hangul Gateway[/bold yellow]

The alien linguist's ship hummed softly in orbit above Earth.
Screens flickered with intercepted signals -- all in a strange,
geometric script made of circles, lines, and angles.

[bold cyan]"This writing system,"[/bold cyan] the linguist said, adjusting a translator,
[bold cyan]"is unlike anything else on this planet. It was designed --
not evolved, not borrowed -- designed from scratch by a king
who wanted his people to read and write."[/bold cyan]

The linguist zoomed in on a block of characters: 한글.

[bold cyan]"They call it Hangul. Each symbol maps to a sound.
The shapes of the consonants mirror the shape of the mouth.
The vowels are built from three elements: heaven, earth, and human.
It is... beautifully logical."[/bold cyan]

The linguist turned to you.

[bold cyan]"Help me decode it. We start with the building blocks."[/bold cyan]

[bold white]Your journey into the Korean alphabet begins now.[/bold white]
"""

ZONE_INTROS = {
    "basic_vowels": """
The linguist pulled up a display of simple strokes -- vertical lines,
horizontal lines, and small branches.

[bold cyan]"Korean vowels are built from three cosmic elements,"[/bold cyan] the linguist said.
[bold cyan]"A dot for heaven (ㆍ), a horizontal line for earth (ㅡ),
and a vertical line for human (ㅣ). From these three shapes,
all vowels are constructed. Elegant, isn't it?"[/bold cyan]

[bold white]Let's decode the basic vowels![/bold white]
""",
    "basic_consonants": """
The linguist displayed consonant symbols alongside diagrams of a human mouth.

[bold cyan]"Here's what's remarkable,"[/bold cyan] the linguist said, eyes wide.
[bold cyan]"The consonant shapes were designed to match the position
of the tongue, lips, and throat when making each sound.
ㄱ looks like the tongue pulling back for a 'g' sound.
ㄴ looks like the tongue touching the roof of the mouth for 'n'."[/bold cyan]

[bold white]Let's decode the basic consonants![/bold white]
""",
    "syllable_blocks": """
The linguist arranged individual letters into neat square blocks.

[bold cyan]"Korean doesn't write letters in a line like English,"[/bold cyan]
the linguist explained. [bold cyan]"Instead, letters are grouped into
syllable blocks. Each block is one syllable: a consonant + a vowel,
sometimes with a final consonant underneath. The block 한 is
ㅎ + ㅏ + ㄴ packed together."[/bold cyan]

[bold white]Let's learn how syllable blocks are built![/bold white]
""",
    "double_consonants": """
The linguist's display showed pairs of identical consonants side by side.

[bold cyan]"Some consonants come in doubled form,"[/bold cyan] the linguist noted.
[bold cyan]"ㄱ becomes ㄲ, ㄷ becomes ㄸ, and so on. These are tensed --
you say them with more force, like you're holding your breath
for a split second before releasing the sound."[/bold cyan]

[bold white]Let's tackle the double consonants![/bold white]
""",
    "reading_practice": """
The linguist loaded a set of common Korean words onto the screen.

[bold cyan]"You know the letters. You know the blocks. Now let's read,"[/bold cyan]
the linguist said with a grin. [bold cyan]"Real Korean words.
Sound them out, piece by piece. You already have all the tools."[/bold cyan]

[bold white]Let's put it all together and read Korean![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "basic_vowels": """
[bold green]The linguist's screen flashed with approval![/bold green]

[bold cyan]"Excellent -- you've decoded all ten basic vowels.
Heaven, earth, and human -- the building blocks of Korean sound."[/bold cyan]
""",
    "basic_consonants": """
[bold green]The linguist clapped their hands together![/bold green]

[bold cyan]"The consonants are mapped. You can now see how the shapes
mirror the sounds. This writing system is a work of genius."[/bold cyan]
""",
    "syllable_blocks": """
[bold green]The linguist's translator hummed with satisfaction![/bold green]

[bold cyan]"You understand how Korean assembles its blocks.
Consonant, vowel, sometimes a final consonant -- stacked neatly
into one syllable. The architecture is clear to you now."[/bold cyan]
""",
    "double_consonants": """
[bold green]The linguist nodded with deep respect![/bold green]

[bold cyan]"The tensed consonants are tricky even for advanced learners.
You've decoded them all. Impressive signal processing."[/bold cyan]
""",
    "reading_practice": """
[bold green]The linguist stood and bowed -- an Earth gesture they'd learned![/bold green]

[bold cyan]"You can read Hangul. From individual strokes to full words,
you've cracked the code. King Sejong would be proud."[/bold cyan]
""",
}

BOSS_INTROS = {
    "basic_vowels": """
The linguist dimmed the lights and projected vowel symbols.

[bold cyan]"Final test -- identify these vowels from memory.
No hints from the translator this time."[/bold cyan]
""",
    "basic_consonants": """
The linguist scrambled consonants across the screen.

[bold cyan]"Match each consonant to its sound.
Show me you've internalized the pattern."[/bold cyan]
""",
    "syllable_blocks": """
The linguist displayed a partially assembled block.

[bold cyan]"Build this syllable from its components.
Prove you understand the architecture."[/bold cyan]
""",
    "double_consonants": """
The linguist played pairs of similar sounds.

[bold cyan]"Regular or doubled? The difference is subtle
but critical. Listen carefully."[/bold cyan]
""",
    "reading_practice": """
The linguist loaded a final sequence of Korean words.

[bold cyan]"Read these words without romanization.
Pure Hangul. You're ready."[/bold cyan]
""",
}
