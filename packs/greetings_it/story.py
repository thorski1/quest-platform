"""
story.py — Narrative for the Ciao! (Greetings) skill pack.

A sunset stroll through an Italian piazza, learning to greet,
introduce yourself, be polite, and order gelato.
"""

INTRO_STORY = """
[bold red]LEARN ITALIAN[/bold red]
[bold yellow]Chapter: Ciao![/bold yellow]

The piazza glowed in the amber light of early evening.
Café tables spilled out onto warm cobblestones. An accordion player
filled the air with a lazy waltz. Children chased pigeons
while their grandparents watched from wrought-iron benches.

A barista in a white apron stepped out from behind his espresso machine,
wiping his hands.

[bold cyan]"Ciao!"[/bold cyan] he called out, grinning.
[bold cyan]"Welcome to the piazza. You want to learn Italian?
Then you've come to the right place. Because Italian
doesn't start in a classroom -- it starts in conversation.
And conversation starts with one word..."[/bold cyan]

He spread his arms wide.

[bold yellow]"Ciao!"[/bold yellow]

[bold cyan]"The most beautiful greeting in any language.
By the end of this chapter, you'll greet people, thank them,
introduce yourself, know when to be formal,
and order the perfect gelato."[/bold cyan]

[bold white]Your Italian conversations begin at sunset.[/bold white]
"""

ZONE_INTROS = {
    "hello_goodbye": """
The barista gestured you to a table near the fountain.

[bold cyan]"Every language has a rhythm,"[/bold cyan] he said,
[bold cyan]"and Italian's rhythm starts with hello.
Ciao, buongiorno, buonasera, arrivederci...
each greeting paints a different mood."[/bold cyan]

[bold white]Let's learn the words that open and close every Italian encounter![/bold white]
""",
    "please_thank_you": """
The barista placed a tiny espresso cup before you.

[bold cyan]"In Italy, manners are not optional,"[/bold cyan] he said seriously.
[bold cyan]"Per favore, grazie, prego, scusa...
These little words are the oil that keeps
Italian society running smoothly."[/bold cyan]

[bold white]Let's master the magic words of Italian courtesy![/bold white]
""",
    "introductions": """
A group of locals gathered at a nearby table, curious about the newcomer.

[bold cyan]"They want to know who you are!"[/bold cyan] the barista laughed.
[bold cyan]"In Italian, you say 'Mi chiamo...' (I call myself...)
or 'Sono...' (I am...). Simple, direct, and warm."[/bold cyan]

[bold white]Let's learn to introduce yourself in Italian![/bold white]
""",
    "tu_vs_lei": """
An elderly signora in pearls approached, and the barista straightened up.

[bold cyan]"Watch this,"[/bold cyan] he whispered. [bold cyan]"With my friend Marco,
I say TU. With Signora Rossi, I say LEI.
Italian has two ways to say 'you' --
and using the wrong one can be very awkward."[/bold cyan]

[bold white]Let's navigate the delicate art of Italian formality![/bold white]
""",
    "at_the_gelateria": """
The barista led you to a gelateria across the piazza.
Rows of colorful gelato glistened behind curved glass.

[bold cyan]"This,"[/bold cyan] he said reverently, [bold cyan]"is the real test.
Can you order gelato in Italian? Choose your flavor,
ask the price, say please and thank you?
This is where language becomes life."[/bold cyan]

[bold white]Let's order gelato -- in perfect Italian![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "hello_goodbye": """
[bold green]The barista raised his espresso cup in a toast![/bold green]

[bold cyan]"Ciao, buongiorno, arrivederci -- you've got the music of Italian greetings.
Now you can walk into any piazza and feel at home."[/bold cyan]
""",
    "please_thank_you": """
[bold green]The barista bowed with theatrical grace![/bold green]

[bold cyan]"Per favore, grazie, prego, scusa -- the four pillars of Italian politeness.
You are now officially well-mannered in Italian!"[/bold cyan]
""",
    "introductions": """
[bold green]The barista clapped you on the shoulder![/bold green]

[bold cyan]"Mi chiamo, sono, di dove sei -- you can meet anyone now!
In Italy, introductions are the beginning of friendship."[/bold cyan]
""",
    "tu_vs_lei": """
[bold green]The barista gave a respectful nod![/bold green]

[bold cyan]"Tu with friends, Lei with strangers and elders. You understand
the invisible rules of Italian society. That's real fluency."[/bold cyan]
""",
    "at_the_gelateria": """
[bold green]The barista and the gelateria owner both applauded![/bold green]

[bold cyan]"You ordered gelato in perfect Italian! Flavor, size, price --
everything. This is what language learning is for."[/bold cyan]
""",
}

BOSS_INTROS = {
    "hello_goodbye": """
The barista leaned across the counter.

[bold cyan]"Hello, goodbye, good morning, good evening -- all mixed together.
Can you keep them straight under pressure?"[/bold cyan]
""",
    "please_thank_you": """
The barista set up a rapid-fire scenario.

[bold cyan]"Please, thanks, sorry, you're welcome -- in one conversation.
Show me your Italian manners are automatic!"[/bold cyan]
""",
    "introductions": """
The barista gestured to a table of strangers.

[bold cyan]"Introduce yourself to everyone. Name, origin, profession.
Make it natural, make it Italian!"[/bold cyan]
""",
    "tu_vs_lei": """
The barista presented two scenarios side by side.

[bold cyan]"Your best friend and the mayor walk in at the same time.
Navigate both conversations without a single formality mistake!"[/bold cyan]
""",
    "at_the_gelateria": """
The gelateria was packed. The server was impatient.

[bold cyan]"Order for yourself and three friends. Flavors, sizes, prices.
All in Italian. No English allowed!"[/bold cyan]
""",
}
