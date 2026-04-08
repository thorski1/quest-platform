"""
story.py — Narrative for the German Basics skill pack.

Ritter Wolf guides you through the foundations of German,
from the alphabet to sentence structure.
"""

INTRO_STORY = """
[bold red]LEARN GERMAN[/bold red]
[bold yellow]Chapter: Die Grundlagen (The Basics)[/bold yellow]

The drawbridge lowered with a groan, revealing a vast stone courtyard.
Torches flickered along the walls of the Sprachburg -- the Language Castle.
A knight in silver armor stepped forward, a wolf crest on his shield.

[bold cyan]"Willkommen!"[/bold cyan] the knight announced, voice echoing off the
ancient walls. [bold cyan]"I am Ritter Wolf, guardian of the Sprachburg.
Every great journey through the German language begins here,
in the Hall of Foundations."[/bold cyan]

He gestured to five great doors lining the courtyard, each carved
with runes and symbols.

[bold cyan]"Behind these doors lie the building blocks of German:
sounds, articles, pronouns, verbs, and the secret logic
of German word order. Master them all, and the castle's
inner chambers shall open to you."[/bold cyan]

Ritter Wolf drew his sword and saluted.

[bold cyan]"Bereit? Ready? Then let us begin!"[/bold cyan]

[bold white]Your journey into the German language starts now.[/bold white]
"""

ZONE_INTROS = {
    "alphabet_pronunciation": """
Ritter Wolf led you into a torch-lit chamber lined with carved letters.

[bold cyan]"Every language has its own music,"[/bold cyan] Ritter Wolf said,
running a gauntleted hand across the stone alphabet on the wall.
[bold cyan]"German has sounds you already know -- and a few that will
surprise you. The umlauts -- ä, ö, ü -- and the sharp ß.
Master these sounds and you will speak like a true Ritter!"[/bold cyan]

[bold white]Let's learn the sounds of the German alphabet![/bold white]
""",
    "articles": """
Ritter Wolf opened a heavy oak door into the Chamber of Nouns.

[bold cyan]"In German, every noun has a gender,"[/bold cyan] Ritter Wolf explained,
pointing to three banners: one blue (der), one red (die), one gold (das).
[bold cyan]"Der for masculine, die for feminine, das for neuter.
There is no perfect rule -- you must learn each noun with its article.
This is the trial that separates the peasants from the knights!"[/bold cyan]

[bold white]Let's conquer der, die, and das![/bold white]
""",
    "personal_pronouns": """
Ritter Wolf led you to a round table with chairs arranged in a circle.

[bold cyan]"Before you can speak of others, you must know how to
address them,"[/bold cyan] Ritter Wolf said, tapping each chair in turn.
[bold cyan]"Ich, du, er, sie, es... German pronouns are your
companions on every sentence you build."[/bold cyan]

[bold white]Let's learn the German personal pronouns![/bold white]
""",
    "sein_haben": """
Ritter Wolf threw open the gates to the Verb Forge, where
hammers rang against anvils.

[bold cyan]"Two verbs rule the German language above all others,"[/bold cyan]
Ritter Wolf declared. [bold cyan]"Sein -- to be. Haben -- to have.
Every sentence you will ever speak depends on these two.
They are irregular, unpredictable, and absolutely essential."[/bold cyan]

[bold white]Let's master sein and haben![/bold white]
""",
    "word_order": """
Ritter Wolf led you into a hall where sentences were carved
into the stone floor, words rearranging themselves like puzzle pieces.

[bold cyan]"German word order follows rules that may seem strange
at first,"[/bold cyan] Ritter Wolf said. [bold cyan]"The verb always claims the
second position in a statement. Always. This is the iron law
of German syntax -- and it changes everything."[/bold cyan]

[bold white]Let's unlock the secrets of German word order![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "alphabet_pronunciation": """
[bold green]Ritter Wolf nodded approvingly![/bold green]

[bold cyan]"Ausgezeichnet! You can hear the music of German now --
the umlauts, the sharp ß, the guttural ch. Your ear is trained!"[/bold cyan]
""",
    "articles": """
[bold green]Ritter Wolf raised a banner in your honor![/bold green]

[bold cyan]"Der, die, das -- the three-headed dragon of German grammar,
and you have tamed it! Every noun you meet from now on,
learn its article like a knight learns his oath."[/bold cyan]
""",
    "personal_pronouns": """
[bold green]Ritter Wolf clasped your shoulder![/bold green]

[bold cyan]"Ich, du, er, sie, es, wir, ihr, sie, Sie -- you know them all!
Now you can address anyone in the kingdom, from peasant to king."[/bold cyan]
""",
    "sein_haben": """
[bold green]Ritter Wolf struck the anvil in celebration![/bold green]

[bold cyan]"Sein and haben -- the twin pillars of German! You have forged
these verbs into your memory. Every sentence you build
from now on rests upon this foundation."[/bold cyan]
""",
    "word_order": """
[bold green]Ritter Wolf unsheathed his sword in salute![/bold green]

[bold cyan]"The iron law of German word order is yours to command!
Verb second, time-manner-place, and the verb-final rule in
subclauses -- you understand the architecture of German!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "alphabet_pronunciation": """
Ritter Wolf tapped the wall, and the carved letters began to glow.

[bold cyan]"Final trial of sounds! Umlauts, consonants, the ß --
can you identify them all under pressure?"[/bold cyan]
""",
    "articles": """
Ritter Wolf placed three shields on the table: der, die, das.

[bold cyan]"The ultimate article challenge! Which gender belongs to which noun?
No guessing -- a true knight knows!"[/bold cyan]
""",
    "personal_pronouns": """
Ritter Wolf pointed to an empty throne.

[bold cyan]"Who sits where? Match every pronoun to its role.
One mistake and the round table falls!"[/bold cyan]
""",
    "sein_haben": """
Ritter Wolf crossed two swords in the air.

[bold cyan]"Sein or haben? Conjugate under fire!
Show me every form, every person, no hesitation!"[/bold cyan]
""",
    "word_order": """
Ritter Wolf scattered stone tiles across the floor.

[bold cyan]"Rearrange the chaos! Put every word in its proper place.
The iron law demands perfection!"[/bold cyan]
""",
}
