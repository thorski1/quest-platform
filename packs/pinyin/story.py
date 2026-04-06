"""
story.py — Narrative for the Pinyin skill pack.

Long Long the dragon guides you through the sounds of Mandarin Chinese,
from the four tones to reading full pinyin syllables.
"""

INTRO_STORY = """
[bold red]LEARN CHINESE[/bold red]
[bold yellow]Chapter: The Sound of Chinese[/bold yellow]

A small golden dragon spiraled down from the clouds, landing on
an open scroll covered in strange markings. Some looked like English
letters, but with curious little marks above them.

[bold cyan]"Welcome!"[/bold cyan] the dragon said, smoke curling from its nostrils.
[bold cyan]"I am Long Long -- your guide to the sounds of Chinese.
Before you can read characters or speak sentences,
you need to master pinyin -- the sound system
that unlocks every word in Mandarin."[/bold cyan]

Long Long tapped the scroll. The markings began to glow:
[bold yellow]ma  ma  ma  ma[/bold yellow] -- but each one had a different
tone mark above it.

[bold cyan]"Same letters. Four completely different words.
That's the magic of Chinese -- the tones carry meaning.
Get the tone wrong, and 'mother' becomes 'horse'!"[/bold cyan]

Long Long grinned, showing rows of tiny teeth.

[bold cyan]"Don't worry. By the time we're done, you'll hear
every tone, say every sound, and read pinyin
like you've been doing it your whole life."[/bold cyan]

[bold white]Your journey into the sounds of Mandarin begins now.[/bold white]
"""

ZONE_INTROS = {
    "tones": """
Long Long breathed a soft flame that formed four glowing lines in the air.

[bold cyan]"Chinese has four main tones,"[/bold cyan] Long Long explained.
[bold cyan]"First tone is high and flat -- like singing one steady note.
Second tone rises -- like asking 'huh?' in English.
Third tone dips down then comes back up.
Fourth tone drops sharply -- like giving a command."[/bold cyan]

Four tone marks appeared: [bold yellow]- / v \\[/bold yellow]

[bold white]Let's learn to hear and identify the four tones![/bold white]
""",
    "initials": """
Long Long arranged puffs of smoke into neat rows of letters.

[bold cyan]"Initials are the consonant sounds at the beginning of a syllable,"[/bold cyan]
Long Long said. [bold cyan]"Some sound like English: b, p, m, f.
Others are completely new: zh, ch, sh, and the tricky q, x, and r."[/bold cyan]

[bold white]Let's master every initial consonant in Mandarin![/bold white]
""",
    "finals": """
Long Long opened a fan-shaped chart of vowel sounds.

[bold cyan]"Finals are the vowel sounds that end each syllable,"[/bold cyan]
Long Long explained. [bold cyan]"Simple ones like a, o, e, i, u, and the
special u with two dots. Then compound finals like ai, ei, ao, ou.
And nasal finals that end in -n or -ng."[/bold cyan]

[bold white]Time to explore the vowel sounds of Chinese![/bold white]
""",
    "pinyin_reading": """
Long Long unrolled a scroll covered with complete pinyin syllables.

[bold cyan]"Now you know initials and finals separately,"[/bold cyan] Long Long said.
[bold cyan]"Time to put them together! Reading pinyin means combining
an initial + a final + a tone into one smooth syllable.
And knowing where one syllable ends and the next begins."[/bold cyan]

[bold white]Let's read complete pinyin syllables![/bold white]
""",
    "common_sounds": """
Long Long produced a glowing list of the most frequent Chinese syllables.

[bold cyan]"Not all pinyin syllables are created equal,"[/bold cyan] Long Long said.
[bold cyan]"Some appear in hundreds of common words. If you master
these high-frequency sounds first, you'll understand
more Chinese faster."[/bold cyan]

[bold white]Let's practice the most useful sounds in Mandarin![/bold white]
""",
    "tones_in_context": """
Long Long held up two cards, each showing the third tone mark.

[bold cyan]"Here's a secret about tones,"[/bold cyan] Long Long whispered.
[bold cyan]"They change depending on their neighbors! When two
third tones meet, the first one becomes a second tone.
And the words bu and yi change tone based on what follows."[/bold cyan]

[bold white]Let's master the rules of tone change![/bold white]
""",
    "pinyin_typing": """
Long Long pulled out a tiny glowing keyboard.

[bold cyan]"In the real world, you'll need to type Chinese,"[/bold cyan]
Long Long said. [bold cyan]"The good news? You type pinyin
on a regular keyboard, and the computer shows you
characters to choose from. It's easier than you think!"[/bold cyan]

[bold white]Let's learn to type Chinese on your devices![/bold white]
""",
    "pinyin_vs_english": """
Long Long placed two scrolls side by side -- one English, one pinyin.

[bold cyan]"Pinyin uses the same letters as English,"[/bold cyan] Long Long warned,
[bold cyan]"but many sounds are completely different! The letter 'c'
doesn't sound like English c. The letter 'q' is nothing like
English q. And then there's the mysterious u with two dots..."[/bold cyan]

[bold white]Let's spot the tricky differences between English and Chinese sounds![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "tones": """
[bold green]Long Long did a joyful loop in the air![/bold green]

[bold cyan]"You can hear all four tones! This is the foundation of everything
in Chinese. Every single word has a tone, and you now know them all."[/bold cyan]
""",
    "initials": """
[bold green]Long Long breathed a celebratory burst of golden flame![/bold green]

[bold cyan]"Every initial consonant -- mastered! From the easy ones like b and m
to the tricky zh, ch, sh, and r. Your mouth is learning new shapes!"[/bold cyan]
""",
    "finals": """
[bold green]Long Long spread both wings wide in triumph![/bold green]

[bold cyan]"Simple finals, compound finals, nasal finals -- you know them all!
These vowel sounds are the melody that carries every Chinese word."[/bold cyan]
""",
    "pinyin_reading": """
[bold green]Long Long clapped tiny claws together![/bold green]

[bold cyan]"You can read complete pinyin syllables now! Initial + final + tone,
all flowing together. You're reading the sound map of Chinese!"[/bold cyan]
""",
    "common_sounds": """
[bold green]Long Long purred with satisfaction![/bold green]

[bold cyan]"You've practiced the most common sounds in Mandarin.
These syllables appear in thousands of everyday words.
Your ears are already tuning to the rhythm of Chinese!"[/bold cyan]
""",
    "tones_in_context": """
[bold green]Long Long did a spinning dance in midair![/bold green]

[bold cyan]"Tone sandhi mastered! You understand that tones are alive --
they shift and change based on their neighbors. This is something
even many textbooks don't teach well, but you've got it!"[/bold cyan]
""",
    "pinyin_typing": """
[bold green]Long Long tapped the keyboard with a flourish![/bold green]

[bold cyan]"You know how to type Chinese on any device! Pinyin input
is used by hundreds of millions of people every day.
Now you can join them."[/bold cyan]
""",
    "pinyin_vs_english": """
[bold green]Long Long breathed a rainbow of flame![/bold green]

[bold cyan]"You've spotted every tricky difference between English and Chinese sounds!
No more false friends, no more confusion. You hear Chinese as Chinese now,
not filtered through English. That is a huge milestone!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "tones": """
Long Long's eyes glowed bright gold.

[bold cyan]"One final challenge on tones. This one tests everything --
all four tones, the neutral tone, and tone pairs.
Show me you truly hear the music of Chinese!"[/bold cyan]
""",
    "initials": """
Long Long arranged smoke letters into a swirling circle.

[bold cyan]"The ultimate initials challenge! I'll test you on the trickiest
consonants -- the ones that trip up every English speaker.
Can you tell zh from z? q from ch? Let's find out!"[/bold cyan]
""",
    "finals": """
Long Long fanned out every vowel sound in a glowing arc.

[bold cyan]"Time for the finals boss challenge! I'm mixing simple, compound,
and nasal finals together. Listen carefully -- some of these
sounds are very close to each other!"[/bold cyan]
""",
    "pinyin_reading": """
Long Long unrolled the longest scroll yet.

[bold cyan]"Can you read any pinyin syllable I throw at you?
Multi-syllable words, tricky combinations, unusual pairings --
this is the real test of your pinyin reading skills!"[/bold cyan]
""",
    "common_sounds": """
Long Long held up a golden character.

[bold cyan]"Let's see how well you know the most common sounds.
I'll test speed and accuracy -- these should be second nature by now!"[/bold cyan]
""",
    "tones_in_context": """
Long Long placed a complex sentence on the scroll.

[bold cyan]"Tone sandhi in action! Multiple tone changes in sequence,
bu and yi rules mixed together -- this is how real Chinese sounds.
Can you track every shift?"[/bold cyan]
""",
    "pinyin_typing": """
Long Long summoned a virtual keyboard.

[bold cyan]"Final typing challenge! I'll test your knowledge of input methods,
special characters, and the tricks that make typing Chinese fast.
Ready to prove you can write digitally?"[/bold cyan]
""",
    "pinyin_vs_english": """
Long Long placed English and Chinese sounds in a maze.

[bold cyan]"The ultimate comparison challenge! Every tricky sound,
every false friend, every letter that means something different
in pinyin. Only a true Sound Detective can ace this!"[/bold cyan]
""",
}
