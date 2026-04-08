"""
story.py — Narrative for the Grüße! skill pack.

Ritter Wolf guides you through German greetings, polite speech,
introductions, formality levels, and a real-world bakery encounter.
"""

INTRO_STORY = """
[bold red]LEARN GERMAN[/bold red]
[bold yellow]Chapter: Grüße! (Greetings!)[/bold yellow]

The morning sun broke through the mist as Ritter Wolf led you
across the drawbridge and into the bustling village outside the Sprachburg.
Market stalls lined the cobblestone street, and townsfolk called
out to one another in cheerful German.

[bold cyan]"Language lives in the spaces between people,"[/bold cyan]
Ritter Wolf said, adjusting his wolf-crested helmet.
[bold cyan]"Every conversation begins with a greeting and ends with
a farewell. Between them lies connection, politeness, identity."[/bold cyan]

A baker waved from a shop window: [bold yellow]"Guten Morgen!"[/bold yellow]
A blacksmith nodded: [bold yellow]"Hallo!"[/bold yellow]
A noblewoman curtsied: [bold yellow]"Grüß Gott!"[/bold yellow]

[bold cyan]"By the end of this chapter, you'll be able to greet anyone,
introduce yourself, know when to be formal and when to be friendly,
and even order a Brötchen at the bakery."[/bold cyan]

Ritter Wolf extended a gauntleted hand.

[bold cyan]"Bereit? Then let us speak!"[/bold cyan]

[bold white]Your journey into German greetings begins now.[/bold white]
"""

ZONE_INTROS = {
    "hello_goodbye": """
Ritter Wolf stopped at the village gate, where travelers came and went.

[bold cyan]"Every meeting begins with a greeting, and every parting
deserves a proper farewell,"[/bold cyan] Ritter Wolf said.
[bold cyan]"Hallo, Guten Tag, Auf Wiedersehen, Tschüss --
German has greetings for every occasion, from the castle
throne room to the village tavern."[/bold cyan]

[bold white]Let's learn to say hello and goodbye in German![/bold white]
""",
    "please_thankyou": """
Ritter Wolf held the tavern door open and gestured for you to enter.

[bold cyan]"Bitte and Danke -- please and thank you,"[/bold cyan]
Ritter Wolf said. [bold cyan]"These two words will carry you further
than any sword. In Germany, politeness is not optional --
it is the armor of civilization."[/bold cyan]

[bold white]Let's master the magic words of German politeness![/bold white]
""",
    "introductions": """
Ritter Wolf led you into a great hall where knights stood in a circle.

[bold cyan]"Now that you can greet, people will want to know who you are!"[/bold cyan]
Ritter Wolf said. [bold cyan]"Ich heiße... Ich komme aus...
Ich bin... These three phrases let you tell the world
your name, your origin, and your identity."[/bold cyan]

[bold white]Let's learn to introduce yourself in German![/bold white]
""",
    "du_sie": """
Ritter Wolf lowered his voice as you approached the royal court.

[bold cyan]"In German, the word 'you' is a choice,"[/bold cyan]
Ritter Wolf whispered. [bold cyan]"'Du' for friends and family.
'Sie' for strangers, elders, and anyone you wish to show respect.
Choose wrong, and you insult. Choose right, and doors open."[/bold cyan]

[bold white]Let's navigate the formal and informal worlds of German![/bold white]
""",
    "at_the_bakery": """
Ritter Wolf stopped in front of a warm, fragrant bakery.

[bold cyan]"Time to put it all together!"[/bold cyan] Ritter Wolf said.
[bold cyan]"Greetings, politeness, introductions, formality --
all in one real-world scenario. The German bakery is a sacred place.
Bread is serious business here."[/bold cyan]

[bold white]Let's survive your first real German conversation![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "hello_goodbye": """
[bold green]Ritter Wolf saluted![/bold green]

[bold cyan]"Hallo, Guten Tag, Auf Wiedersehen, Tschüss -- you can greet
anyone in the kingdom now, from dawn to dusk!"[/bold cyan]
""",
    "please_thankyou": """
[bold green]Ritter Wolf bowed with gratitude![/bold green]

[bold cyan]"Bitte, Danke, Entschuldigung -- the three pillars of German
politeness are yours. You are now fit for any court!"[/bold cyan]
""",
    "introductions": """
[bold green]Ritter Wolf clapped his gauntlets together![/bold green]

[bold cyan]"Splendid! You can introduce yourself, say where you're from,
and ask others about themselves. The first step to any friendship!"[/bold cyan]
""",
    "du_sie": """
[bold green]Ritter Wolf nodded with deep respect![/bold green]

[bold cyan]"You understand the sacred boundary between du and Sie.
This cultural knowledge is worth more than a thousand vocabulary words!"[/bold cyan]
""",
    "at_the_bakery": """
[bold green]Ritter Wolf held up a fresh Brötchen in triumph![/bold green]

[bold cyan]"You ordered at a German bakery! Greetings, politeness,
formality -- all working together in real life. You are ready
for the real Germany!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "hello_goodbye": """
Ritter Wolf stood at a crossroads, travelers passing in both directions.

[bold cyan]"Greet them correctly -- morning, afternoon, evening.
One wrong greeting and you reveal yourself as a Fremder!"[/bold cyan]
""",
    "please_thankyou": """
Ritter Wolf set up a mock banquet scene.

[bold cyan]"Bitte, Danke, Entschuldigung -- use them all in the right places.
A true knight's manners are tested at the feast table!"[/bold cyan]
""",
    "introductions": """
Ritter Wolf pushed you toward a group of strangers.

[bold cyan]"Introduce yourself completely -- name, origin, identity.
Show me you can meet anyone in the kingdom!"[/bold cyan]
""",
    "du_sie": """
Ritter Wolf presented three figures: a child, a colleague, and a king.

[bold cyan]"Du or Sie? Three people, three levels of formality.
One wrong choice could cost you your head!"[/bold cyan]
""",
    "at_the_bakery": """
Ritter Wolf opened the bakery door and pushed you inside.

[bold cyan]"Order a Brötchen, be polite, handle the conversation from
Guten Morgen to Auf Wiedersehen. This is the real test!"[/bold cyan]
""",
}
