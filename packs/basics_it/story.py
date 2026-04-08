"""
story.py — Narrative for the Italian Basics skill pack.

A sunset journey through the Italian countryside, building
the foundations of Italian language one stone at a time.
"""

INTRO_STORY = """
[bold red]LEARN ITALIAN[/bold red]
[bold yellow]Chapter: Italian Basics[/bold yellow]

The evening sun painted the Tuscan hills in shades of amber and rose.
You stood at the edge of a vineyard, the air thick with the scent
of ripe grapes and wild rosemary. A winding stone path led
toward a small village where warm light spilled from open windows.

An old woman appeared at the gate, drying her hands on an apron.

[bold cyan]"Benvenuto!"[/bold cyan] she called out, smiling.
[bold cyan]"Welcome! You've come to learn our beautiful language, sì?
Good. Every great journey starts with the first step --
and in Italian, that step is the alphabet."[/bold cyan]

She gestured toward the village.

[bold cyan]"We will walk through sounds, words, and little rules
that make Italian the most musical language in the world.
By the time the sun sets, you'll have the foundation
to build anything."[/bold cyan]

[bold white]Your Italian journey begins at golden hour.[/bold white]
"""

ZONE_INTROS = {
    "alphabet_pronunciation": """
The old woman led you to a stone wall covered in faded letters.

[bold cyan]"Italian has 21 letters -- not 26 like English,"[/bold cyan]
she said. [bold cyan]"And every letter is pronounced. No silent tricks,
no surprises. What you see is what you say.
That's the beauty of Italian."[/bold cyan]

[bold white]Let's learn the sounds that make Italian sing![/bold white]
""",
    "articles": """
You passed a market stall filled with bread, cheese, and fruit.

[bold cyan]"In Italian, every noun has a gender -- masculine or feminine,"[/bold cyan]
the woman explained. [bold cyan]"And before each noun, we place
a little word: il, la, lo, i, le, gli...
These are our articles. They tell you the gender and number."[/bold cyan]

[bold white]Let's master the small words that frame every Italian noun![/bold white]
""",
    "subject_pronouns": """
The village square was full of people -- children, elders, couples.

[bold cyan]"Io, tu, lui, lei..."[/bold cyan] the woman pointed to different people.
[bold cyan]"In Italian, we have pronouns for every person.
But here's a secret -- Italians often drop the pronoun entirely!
The verb tells you who's speaking."[/bold cyan]

[bold white]Let's learn who's who in Italian![/bold white]
""",
    "essere_avere": """
You sat down at a wooden table under a pergola draped in wisteria.

[bold cyan]"Two verbs rule Italian: essere -- to be,
and avere -- to have,"[/bold cyan] she said, pouring a glass of water.
[bold cyan]"Master these two and you can say almost anything.
'I am happy.' 'I have a question.' Everything starts here."[/bold cyan]

[bold white]Let's conjugate the two most important verbs in Italian![/bold white]
""",
    "common_adjectives": """
The sunset deepened to crimson as you walked through an olive grove.

[bold cyan]"Italian adjectives are alive,"[/bold cyan] the woman said,
touching a leaf. [bold cyan]"They change to match the noun --
grande, grandi, bello, bella...
An adjective agrees with its noun like a dance partner."[/bold cyan]

[bold white]Let's paint with Italian adjectives![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "alphabet_pronunciation": """
[bold green]The woman clapped her hands with delight![/bold green]

[bold cyan]"Perfetto! You can hear the music in Italian now.
Every vowel open, every consonant clear. No mumbling in this language!"[/bold cyan]
""",
    "articles": """
[bold green]The woman raised her glass![/bold green]

[bold cyan]"Bravissimo! Il, la, lo, i, le, gli -- you've tamed them all.
Now every noun in Italian has its proper escort."[/bold cyan]
""",
    "subject_pronouns": """
[bold green]The woman smiled warmly![/bold green]

[bold cyan]"Io, tu, lui, lei, noi, voi, loro -- you know them all!
And remember, Italian often hides the pronoun in the verb itself."[/bold cyan]
""",
    "essere_avere": """
[bold green]The woman stood and applauded![/bold green]

[bold cyan]"Essere and avere -- the twin pillars of Italian!
You can now say who you are and what you have. That is powerful."[/bold cyan]
""",
    "common_adjectives": """
[bold green]The woman gazed at the sunset with satisfaction![/bold green]

[bold cyan]"Bello, grande, buono, piccolo... you can describe the world
in Italian now. And you know the secret: adjectives dance with their nouns."[/bold cyan]
""",
}

BOSS_INTROS = {
    "alphabet_pronunciation": """
The woman leaned against the stone wall, arms crossed.

[bold cyan]"Final test on sounds and letters. Italian pronunciation
has rules -- let's see if you've truly learned them."[/bold cyan]
""",
    "articles": """
The woman held up a basket of mixed items.

[bold cyan]"Il pane, la frutta, lo zucchero, i fiori, le mele...
Match the right article to each noun. No mistakes!"[/bold cyan]
""",
    "subject_pronouns": """
The woman pointed to the crowd in the piazza.

[bold cyan]"Who is io? Who is loro? Can you keep all the pronouns
straight when the pressure is on?"[/bold cyan]
""",
    "essere_avere": """
The woman set two cups on the table -- one marked ESSERE, one AVERE.

[bold cyan]"Which verb, which form, which person? Conjugation
is the heartbeat of Italian. Show me yours is strong."[/bold cyan]
""",
    "common_adjectives": """
The woman gestured at the painted sky.

[bold cyan]"Describe it all -- the big, the small, the beautiful, the old.
And make every adjective agree. This is your final canvas."[/bold cyan]
""",
}
