"""
story.py — Narrative for the Music Advanced skill pack (The Concert Hall).

Puck leads the reader deeper into music — reading notation, exploring genres,
meeting great composers, hearing the world's instruments, and making music.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Concert Hall[/bold yellow]

Puck hovered at the far end of the Music Room, where a door
the girl had never noticed before stood slightly ajar.
Golden light spilled through the crack, and with it came
the sound of many instruments playing together — not a lesson,
but a [italic]performance[/italic].

[bold cyan]"You learned the basics,"[/bold cyan] Puck said, wings flickering
with excitement. [bold cyan]"Notes, rhythms, instruments, voices.
But music goes so much deeper. Behind that door is
the Concert Hall — where the real magic lives."[/bold cyan]

The girl pushed the door open. The room beyond was vast,
with soaring ceilings, velvet seats, and a grand stage
where instruments of every kind gleamed under golden lights.

[bold cyan]"In here,"[/bold cyan] Puck continued, [bold cyan]"you'll learn to read
the language musicians write in. You'll hear genres
from rock to jazz to electronic. You'll meet the greatest
composers who ever lived. You'll travel the world
through its music. And at the end — you'll be ready
to make music of your own."[/bold cyan]

The conductor's podium glowed softly, waiting.

[bold cyan]"Ready for the Concert Hall?"[/bold cyan] Puck grinned.

[bold white]The Primer opens a new chapter. Your deeper musical journey begins now.[/bold white]
"""

ZONE_INTROS = {
    "reading_music": """
Puck flew to an enormous sheet of music pinned to the Concert Hall wall —
staves stretching in every direction, covered in notes and symbols.

[bold cyan]"In the Music Room, you learned what notes are,"[/bold cyan] Puck said.
[bold cyan]"Now it's time to learn to [italic]read[/italic] them — really read them.
Treble clef for the high notes. Bass clef for the low ones.
Time signatures that tell you how to count.
Sharps and flats hiding between the main notes."[/bold cyan]

A grand staff glowed on the wall — treble and bass clefs
joined together, Middle C shining like a star between them.

[bold cyan]"Master this, and you can read any piece of music
ever written — from Mozart to movie soundtracks."[/bold cyan]

[bold white]Let's learn to read the language of music![/bold white]
""",
    "musical_genres": """
Puck pushed open a door labeled [bold yellow]GENRES[/bold yellow],
and behind it was a hallway with six rooms, each pulsing
with a completely different sound.

[bold cyan]"Music isn't just one thing,"[/bold cyan] Puck said, dodging
a blast of electric guitar from the first room.
[bold cyan]"It's hundreds of different styles — genres —
each with its own instruments, its own rules,
its own feeling. Rock is power. Jazz is freedom.
Classical is elegance. Hip-hop is poetry.
Country is storytelling. Electronic is invention."[/bold cyan]

Six doors glowed with different colors, each one vibrating
with its own unique sound.

[bold cyan]"Let's visit them all."[/bold cyan]

[bold white]Let's explore the many worlds of music![/bold white]
""",
    "famous_composers": """
The Concert Hall's walls transformed into a grand gallery.
Four enormous portraits hung in golden frames, each one
glowing with inner light — and faintly, you could hear
the music each composer was most famous for.

[bold cyan]"You met them briefly before,"[/bold cyan] Puck said reverently.
[bold cyan]"But now we go deeper. Mozart the child genius
who wrote over 600 works. Beethoven who composed
masterpieces after going completely deaf.
Bach who invented musical forms still used today.
Tchaikovsky who made ballet music that changed the world."[/bold cyan]

[bold yellow]Mozart ~ Beethoven ~ Bach ~ Tchaikovsky[/bold yellow]

[bold cyan]"Their stories are as extraordinary as their music."[/bold cyan]

[bold white]Let's discover the lives behind the music![/bold white]
""",
    "world_music": """
The Concert Hall's stage began to rotate, and with each turn
a different landscape appeared — sun-baked African plains,
misty Indian palaces, serene Japanese gardens, rolling Celtic hills.

[bold cyan]"Every corner of the world makes music,"[/bold cyan] Puck said,
flying across the spinning stage. [bold cyan]"And each tradition
has instruments, scales, and rhythms that are completely unique.
African polyrhythms that layer beat upon beat.
Indian ragas that paint with sound. Japanese koto music
as delicate as cherry blossoms. Celtic reels so fast
your feet can't help but dance."[/bold cyan]

[bold yellow]Africa ~ India ~ Japan ~ Celtic Lands[/bold yellow]

[bold white]Let's hear how the whole world sings![/bold white]
""",
    "making_music": """
Puck landed on the Concert Hall stage and looked back
at the girl with a serious, shining expression.

[bold cyan]"You've learned to read music. You've heard every genre.
You've met the greatest composers. You've traveled the world
through its instruments and rhythms."[/bold cyan]

Puck paused.

[bold cyan]"Now comes the most important part of all.
[italic]Making[/italic] music. Your own music.
Band instruments. Orchestra sections. Your voice.
And the art of writing a song."[/bold cyan]

Instruments appeared on velvet stands — guitars, drums,
a keyboard, a microphone — all glowing softly.

[bold cyan]"You don't need to be perfect. You just need to start."[/bold cyan]

[bold white]Your turn to make the Concert Hall sing![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "reading_music": """
[bold green]The grand staff blazes with light — every note, every clef,
every time signature glowing in perfect order![/bold green]

Treble clef and bass clef, sharps and flats, ledger lines
and time signatures — all of it makes sense now.

[bold cyan]"You can read music,"[/bold cyan] Puck says, impressed.
[bold cyan]"Not just the basics — really read it. Hand you
a piece of sheet music and you'd know exactly
what every symbol means. That's a superpower."[/bold cyan]

The genre hallway glows ahead, six doors pulsing with different sounds...
""",
    "musical_genres": """
[bold green]Six doors fly open and six genres play together
in a glorious, impossible mashup![/bold green]

Rock power chords, jazz improvisation, classical strings,
hip-hop beats, country storytelling, electronic synths —
all weaving together.

[bold cyan]"You know the genres now,"[/bold cyan] Puck says.
[bold cyan]"Rock, jazz, classical, hip-hop, country, electronic —
each one a different world, each one beautiful.
And the best part? They keep mixing and making
new genres all the time. Music never stops evolving."[/bold cyan]

Four golden portraits glow in the gallery ahead...
""",
    "famous_composers": """
[bold green]All four portraits blaze with golden light,
and their music plays simultaneously — a symphony
of genius across three centuries![/bold green]

Mozart's elegance, Beethoven's power, Bach's intricacy,
Tchaikovsky's emotion — all alive in the Concert Hall.

[bold cyan]"You truly know them now,"[/bold cyan] Puck says softly.
[bold cyan]"Not just their names — their stories. A child prodigy.
A deaf genius. A father of twenty. A ballet master.
Their music will sound different to you from now on,
because you know the humans behind it."[/bold cyan]

The stage begins to rotate toward distant lands...
""",
    "world_music": """
[bold green]Djembe drums, sitar, koto, and Celtic fiddle
join together in a celebration that spans the globe![/bold green]

African polyrhythms, Indian ragas, Japanese pentatonic scales,
Celtic reels — all different, all beautiful, all music.

[bold cyan]"The whole world sings,"[/bold cyan] Puck says, eyes shining.
[bold cyan]"Different instruments, different scales, different traditions —
but the same human need to make music. It connects us all.
Every culture. Every continent. Every person."[/bold cyan]

The stage lights focus on waiting instruments. It's time to make music...
""",
    "making_music": """
[bold green]The Concert Hall erupts in sound and light!
Every instrument plays, every voice sings,
every rhythm pulses — and at the center of it all
stands you![/bold green]

Puck lands on your shoulder one last time.

[bold cyan]"You've done something remarkable,"[/bold cyan] Puck says,
voice warm with pride. [bold cyan]"You can read music.
You know every genre. You've met the greatest composers.
You've heard the music of the whole world.
And now you know the most important secret of all —
that [italic]you[/italic] can make music. Your own music.
With your own voice, your own hands, your own heart."[/bold cyan]

Puck's wings glow gold.

[bold cyan]"The Concert Hall is always here.
Come back whenever you want to play."[/bold cyan]

[bold white]Reader. Listener. Musician. Creator. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "reading_music": "The grand staff glows with treble and bass clefs joined together, Middle C shining between them. [bold yellow]\"The grand staff is the whole musical world in one system. Can you tell me what it's called when these two staves join together?\"[/bold yellow]",
    "musical_genres": "A river of music flows across the page, branching into streams of rock, jazz, and R&B. [bold yellow]\"All these genres flowed from the same source. Blues gave birth to which two great genres of the 1950s?\"[/bold yellow]",
    "famous_composers": "A timeline stretches across the Concert Hall — Baroque, Classical, Romantic, Modern. [bold yellow]\"Bach, Mozart, Beethoven, Tchaikovsky — each belonged to a different era. Which era came first?\"[/bold yellow]",
    "world_music": "Instruments from four continents swirl together in a spiral of sound. [bold yellow]\"African drums, Indian sitar, Japanese koto, Celtic fiddle — all different. But what do ALL musical traditions share?\"[/bold yellow]",
    "making_music": "The Concert Hall fills with light. Every instrument glows. Puck asks the final question. [bold yellow]\"What is the very first thing you need to write a song? Not equipment. Not training. What?\"[/bold yellow]",
}
