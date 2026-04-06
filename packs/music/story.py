"""
story.py — Narrative for the Music skill pack.

Puck opens the Music Room within the Primer and guides the reader through
notes, rhythms, instruments, voices, world music, great composers,
the emotions of music, and the joy of making music yourself.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Music Room[/bold yellow]

Puck tilted a tiny head, listening. Somewhere deep within the Primer,
a sound was growing — not words, not pictures, but something older
and stranger than both.

[bold cyan]"Do you hear that?"[/bold cyan] Puck whispered, wings trembling.

The girl leaned closer to the page. A single clear note rose
from the paper itself, as if the book were learning to sing.

[bold cyan]"Music,"[/bold cyan] Puck said softly. [bold cyan]"The Primer has a room
I've never shown you — a room where the pages don't just show
and tell. They [italic]sing.[/italic]"[/bold cyan]

A door appeared in the margin of the page — small, arched,
glowing faintly gold, with a treble clef etched into its surface.

[bold white]"What's inside?"[/bold white] the girl asked.

[bold cyan]"Everything,"[/bold cyan] Puck said, pushing the door open.
[bold cyan]"Notes and rhythms. Instruments from every corner of the world.
Composers who wrote music so beautiful it made kings cry.
And the secret of why a song can make you feel happy,
or brave, or like you could fly."[/bold cyan]

The door swung wide. Inside, the Music Room glowed with soft light,
and every surface hummed with gentle sound — waiting.

[bold cyan]"Ready to listen?"[/bold cyan] Puck grinned.

[bold white]The Primer's pages begin to sing. Your musical journey starts now.[/bold white]
"""

ZONE_INTROS = {
    "musical_notes": """
Puck flew to a great golden staff — five lines stretching across the page
like a road made of light.

[bold cyan]"Before you can play music, you have to read it,"[/bold cyan] Puck said.
[bold cyan]"And reading music starts right here — with notes.
Each note has a name, a place on the staff, and a length.
Learn these, and you can read any piece of music in the world."[/bold cyan]

Seven glowing letters appeared above the staff:
[bold yellow]A  B  C  D  E  F  G[/bold yellow]

[bold white]Let's learn the language of notes![/bold white]
""",
    "rhythm_and_beat": """
Puck began tapping a tiny foot on the page — tap, tap, tap, tap —
steady as a heartbeat.

[bold cyan]"Every piece of music has a pulse,"[/bold cyan] Puck said.
[bold cyan]"A steady beat underneath everything, like a heart
pumping life through the song. And on top of that beat,
rhythm dances — long sounds, short sounds, silences."[/bold cyan]

The tapping grew into a pattern: TAP-tap-tap-TAP-tap-tap.

[bold cyan]"Time signatures tell you how to count. Tempo tells you
how fast. And once you feel the beat, you'll never lose it."[/bold cyan]

[bold white]Let's discover the pulse of music![/bold white]
""",
    "instruments_orchestra": """
Puck pushed open a heavy velvet curtain on the page,
and behind it — an orchestra, frozen mid-note, waiting to play.

[bold cyan]"An orchestra has four great families,"[/bold cyan] Puck said,
flying over the players. [bold cyan]"Strings over here — violins
and cellos singing with their bows. Woodwinds in the middle —
flutes and clarinets breathing life into melody. Brass at the back —
trumpets and trombones blazing with power. And percussion
all around — drums and xylophones keeping the beat."[/bold cyan]

[bold yellow]Strings ~ Woodwinds ~ Brass ~ Percussion[/bold yellow]

[bold white]Let's meet the instrument families![/bold white]
""",
    "singing_and_voice": """
Puck pointed to the girl's throat with a tiny glowing finger.

[bold cyan]"You already own the most amazing instrument
in the world,"[/bold cyan] Puck said. [bold cyan]"Your voice.
Two tiny folds inside your throat vibrate when air passes
over them — and just like that, you can make music.
No strings, no keys, no buttons. Just you."[/bold cyan]

A soft hum rose from the page, and the girl realized
it was her own voice, reflected back.

[bold cyan]"High notes, low notes, harmony, melody —
your voice can do it all."[/bold cyan]

[bold white]Let's explore the human instrument![/bold white]
""",
    "music_around_world": """
The Music Room's walls melted away, and suddenly
the page showed the whole world — but instead of borders
and cities, it was filled with instruments.

[bold cyan]"Every culture on Earth makes music,"[/bold cyan] Puck said,
flying across the map. [bold cyan]"Talking drums in West Africa.
The shimmering sitar in India. The elegant koto in Japan.
Dancing fiddles in Ireland. Sunny steel pans in Trinidad.
Different sounds, different stories — but all of it music."[/bold cyan]

[bold yellow]Africa ~ India ~ Japan ~ Ireland ~ Caribbean[/bold yellow]

[bold white]Let's hear the songs of every land![/bold white]
""",
    "famous_composers": """
Four portraits appeared on the wall of the Music Room,
each one glowing with golden light.

[bold cyan]"These four people,"[/bold cyan] Puck said reverently,
[bold cyan]"changed music forever. A boy who wrote symphonies
before he was ten. A man who kept composing even after
he went deaf. A father of twenty who was also the father
of all Western music. And a genius who made
sugar plum fairies dance."[/bold cyan]

[bold yellow]Mozart ~ Beethoven ~ Bach ~ Tchaikovsky[/bold yellow]

[bold white]Let's meet the great composers![/bold white]
""",
    "music_and_feelings": """
Puck sat quietly on the edge of a note, wings folded.

[bold cyan]"Have you ever noticed,"[/bold cyan] Puck said softly,
[bold cyan]"how a song can make you feel things — even without words?
Happy. Sad. Brave. Scared. Peaceful.
Music speaks straight to your heart, skipping
right past your thinking brain."[/bold cyan]

Two chords glowed on the page — one bright gold, one deep blue.

[bold cyan]"Major keys sound happy. Minor keys sound sad.
Loud is powerful. Soft is gentle. And the way music
grows from quiet to thundering — that's dynamics.
These are the tools composers use to paint with feelings."[/bold cyan]

[bold white]Let's discover how music speaks to our hearts![/bold white]
""",
    "making_music": """
Puck landed on the final door in the Music Room.
It was smaller than the others, and it had the girl's name on it.

[bold cyan]"This room,"[/bold cyan] Puck said, [bold cyan]"is yours.
Not about listening to music. Not about learning facts.
This is about [italic]making[/italic] music — your own music,
with your own hands, your own voice, your own heart."[/bold cyan]

Inside, simple instruments waited on velvet cushions:
a recorder, a ukulele, a small keyboard, a pair of drumsticks.

[bold cyan]"You don't need to be a genius. You don't need
expensive equipment. You just need to start."[/bold cyan]

[bold white]Your musical journey begins here![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "musical_notes": """
[bold green]The staff glows with every note in place![/bold green]

A through G, treble clef, whole notes and quarter notes —
all of them shining on the five golden lines.

[bold cyan]"You can read music now,"[/bold cyan] Puck says proudly.
[bold cyan]"Those little dots on lines aren't mysteries anymore.
They're letters. They're sounds. They're the beginning
of every song ever written."[/bold cyan]

A steady beat begins to pulse beneath the staff. The rhythm awaits...
""",
    "rhythm_and_beat": """
[bold green]The beat pulses strong and sure![/bold green]

Whole notes, half notes, quarter notes, rests — all in their places,
the rhythm of the page alive and breathing.

[bold cyan]"You feel it now, don't you?"[/bold cyan] Puck says, tapping along.
[bold cyan]"The beat underneath everything. The rhythm dancing on top.
Once you feel it, you can never un-feel it.
Every song you hear from now on — you'll feel its pulse."[/bold cyan]

The velvet curtain ahead rustles. The orchestra is warming up...
""",
    "instruments_orchestra": """
[bold green]All four families play together in harmony![/bold green]

Strings singing, woodwinds breathing, brass blazing,
percussion keeping time — the full orchestra plays as one.

[bold cyan]"Eighty musicians,"[/bold cyan] Puck says, eyes wide,
[bold cyan]"and a single conductor making them play as one voice.
You know the families now. You know how they work together.
Next time you hear an orchestra, you'll recognize every sound."[/bold cyan]

A single voice rises above the orchestra. The human instrument calls...
""",
    "singing_and_voice": """
[bold green]The human voice rings clear and true![/bold green]

From soprano to bass, from solo to choir — every voice
on the page sings together, high and low and everything between.

[bold cyan]"Your voice is the first instrument you ever played,"[/bold cyan]
Puck says warmly. [bold cyan]"You used it before you could walk.
And no one in the world has one exactly like yours."[/bold cyan]

The Music Room's walls dissolve, and the sounds of distant lands drift in...
""",
    "music_around_world": """
[bold green]Instruments from every land sing together![/bold green]

African drums, Indian sitar, Japanese koto, Irish fiddle,
Caribbean steel pans — all playing at once, all different,
all beautiful, all unmistakably music.

[bold cyan]"Every corner of the world,"[/bold cyan] Puck says,
[bold cyan]"makes music in its own way. And somehow,
even though the instruments and scales are different,
the feeling is the same. Music connects everyone."[/bold cyan]

Four golden portraits glow on the wall ahead. The great composers await...
""",
    "famous_composers": """
[bold green]The portraits glow with golden light![/bold green]

Mozart the prodigy. Beethoven the unstoppable. Bach the father.
Tchaikovsky the storyteller. All of them shining in the Music Room.

[bold cyan]"These four people,"[/bold cyan] Puck says softly,
[bold cyan]"gave the world music that will last forever.
A five-year-old who wrote symphonies. A deaf man
who made the world sing. You know their stories now —
and their music will never sound the same to you."[/bold cyan]

Two chords shimmer ahead — one gold, one blue. The feelings room beckons...
""",
    "music_and_feelings": """
[bold green]Major and minor, loud and soft — the language of feelings![/bold green]

The page pulses between gold and blue, bright and dark,
whisper and roar — all the ways music speaks to the heart.

[bold cyan]"Now you know the secret,"[/bold cyan] Puck says quietly.
[bold cyan]"Major keys for joy. Minor keys for mystery.
Crescendo for power. Pianissimo for tenderness.
Every emotion you've ever felt — music can say it
without a single word."[/bold cyan]

A small door glows ahead with the girl's name on it. The final room awaits...
""",
    "making_music": """
[bold green]The Music Room fills with light — every note, every rhythm,
every instrument, every voice, every feeling, all alive![/bold green]

Puck lands on the girl's shoulder and folds tiny wings.

[bold cyan]"You've done it,"[/bold cyan] Puck says, voice full of warmth.
[bold cyan]"You know notes and rhythms. You know instruments
and voices. You've heard the music of the world
and met the great composers. You understand how music
speaks to the heart. And now — the most important part —
you know that [italic]you[/italic] can make music too."[/bold cyan]

Puck grins.

[bold cyan]"The Music Room is always here. Come back whenever
you want to play. Whenever you want to sing.
Whenever you want to listen."[/bold cyan]

[bold white]Listener. Melody Maker. Musician. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "musical_notes": "Puck points to the four glowing spaces between the staff lines. [bold yellow]\"These four spaces hide a secret — the notes in them spell a word! But which word? Think carefully about F, A, C, and E...\"[/bold yellow]",
    "rhythm_and_beat": "The page goes completely still. Not a sound. Not a note. [bold yellow]\"Silence in music has its own special name — and its own symbols on the staff. What do we call planned silence in music?\"[/bold yellow]",
    "instruments_orchestra": "Puck picks up a tiny baton and stands at the front of the miniature orchestra. [bold yellow]\"Eighty musicians. One person leads them all — without playing a single note. What do we call this person?\"[/bold yellow]",
    "singing_and_voice": "Dozens of tiny singers appear on the page, all singing different notes that blend into something magnificent. [bold yellow]\"When many voices join together like this — sopranos, altos, tenors, and basses — what is this group called?\"[/bold yellow]",
    "music_around_world": "Instruments from every continent swirl around Puck in a glowing spiral. [bold yellow]\"Music exists in every culture ever discovered on Earth. Why do scientists think music might be truly universal?\"[/bold yellow]",
    "famous_composers": "The most famous melody in classical music begins to play — slow, majestic, about the joy of all people being united. [bold yellow]\"Beethoven's 'Ode to Joy' was chosen as the anthem of a great union of nations. Which one?\"[/bold yellow]",
    "music_and_feelings": "Puck touches the page and a warm glow spreads outward, like the feeling of hearing your favorite song. [bold yellow]\"Scientists found that music you love makes your brain release a special 'feel-good' chemical. What is it called?\"[/bold yellow]",
    "making_music": "Puck's wings glow warm gold as the Music Room fills with every sound you've learned. [bold yellow]\"This is the most important question of all: Who can learn to make music? Is it only for the talented few — or is it truly for everyone?\"[/bold yellow]",
}
