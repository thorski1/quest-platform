"""
story.py — Narrative for the French Basics skill pack.

Marie guides you through the French alphabet, articles, pronouns, verbs, and adjectives.
"""

INTRO_STORY = """
[bold red]LEARN FRENCH[/bold red]
[bold yellow]Chapter: French Basics[/bold yellow]

Marie stood before a sunlit chalkboard in a cozy Parisian
classroom, the scent of fresh croissants drifting through
the open window. Outside, the Eiffel Tower sparkled in
the morning light.

[bold cyan]"Bienvenue!"[/bold cyan] Marie said with a warm smile.
[bold cyan]"Welcome to French. Before you can speak,
you must understand the building blocks -- the sounds,
the articles, the pronouns, and the verbs that make
every sentence possible."[/bold cyan]

She wrote on the board: [bold yellow]le, la, je, tu, etre, avoir[/bold yellow]

[bold cyan]"These little words are the foundation of everything.
Master them, and French will open up like a flower.
Shall we begin?"[/bold cyan]

[bold white]Learn the essential building blocks of French.[/bold white]
"""

ZONE_INTROS = {
    "alphabet_pronunciation": """
Marie picked up a piece of chalk and wrote the alphabet on the board.

[bold cyan]"French uses the same 26 letters as English, but they sound
very different!"[/bold cyan] Marie said. [bold cyan]"Silent letters, nasal vowels,
the famous French R -- these sounds give French its beautiful
melody. Let's train your ear and your tongue!"[/bold cyan]

[bold white]Let's master French pronunciation![/bold white]
""",
    "articles": """
Marie held up two small signs: one reading 'le' and the other 'la'.

[bold cyan]"In French, every noun has a gender,"[/bold cyan] Marie explained.
[bold cyan]"A table is feminine -- la table. A book is masculine --
le livre. There's no logic to it, you simply must learn
each word with its article. But I'll teach you some tricks!"[/bold cyan]

[bold white]Let's learn French articles![/bold white]
""",
    "subject_pronouns": """
Marie pointed to nine words written in a circle on the board.

[bold cyan]"Je, tu, il, elle, on, nous, vous, ils, elles,"[/bold cyan]
Marie read aloud. [bold cyan]"These are the subject pronouns -- they
tell you who is doing the action. French has more pronouns
than English, and each one changes how the verb looks."[/bold cyan]

[bold white]Let's master French subject pronouns![/bold white]
""",
    "etre_avoir": """
Marie wrote two verbs in large letters: ETRE and AVOIR.

[bold cyan]"These two verbs are the kings of French,"[/bold cyan] Marie declared.
[bold cyan]"'Etre' means 'to be' and 'avoir' means 'to have.'
Together they appear in almost every French sentence.
They're both irregular, but once you know them,
everything else becomes easier."[/bold cyan]

[bold white]Let's conquer etre and avoir![/bold white]
""",
    "common_adjectives": """
Marie opened a box full of colorful flashcards.

[bold cyan]"Now let's add color to your French!"[/bold cyan] Marie said excitedly.
[bold cyan]"Adjectives describe the world -- big, small, beautiful,
new, old. But in French, adjectives must agree with the noun
in gender and number, and their position matters too."[/bold cyan]

[bold white]Let's learn to describe the world in French![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "alphabet_pronunciation": """
[bold green]Marie applauded with delight![/bold green]

[bold cyan]"Magnifique! You understand French sounds -- silent letters,
nasal vowels, liaison, the French R. Your pronunciation
foundation is solid. Now every new word you learn,
you'll know exactly how to say it!"[/bold cyan]
""",
    "articles": """
[bold green]Marie drew a gold star on the board![/bold green]

[bold cyan]"Formidable! Le, la, les, un, une, des -- you've mastered
them all. You even know about elision and partitive articles.
This is the foundation that holds all of French grammar together!"[/bold cyan]
""",
    "subject_pronouns": """
[bold green]Marie raised both hands in celebration![/bold green]

[bold cyan]"Excellent! You know all nine subject pronouns, including
the tricky 'on' and the dual-purpose 'vous.' Every verb
you learn from now on will click into place because
you understand who's doing the action!"[/bold cyan]
""",
    "etre_avoir": """
[bold green]Marie wrote 'BRAVO' in huge letters on the board![/bold green]

[bold cyan]"You've conquered the two most important verbs in French!
Etre and avoir are the backbone of the language.
Age, feelings, descriptions, professions -- you can
express so much with just these two verbs!"[/bold cyan]
""",
    "common_adjectives": """
[bold green]Marie handed you a small French flag pin![/bold green]

[bold cyan]"Superbe! You can describe the world in French now.
Gender agreement, placement, irregular forms, colors --
you've learned them all. Your French is no longer
black and white -- it's full of color!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "alphabet_pronunciation": """
Marie pointed to a list of tricky French words.

[bold cyan]"Time for the final test! Can you identify which sounds
are silent, which consonants are pronounced, and how
the French accent system works? Let's see if your
ear for French is sharp!"[/bold cyan]
""",
    "articles": """
Marie laid out a series of nouns on the table.

[bold cyan]"Here's the challenge -- which article goes with which
noun? Le or la? Un or une? What about before a vowel?
Show me you've mastered the French article system!"[/bold cyan]
""",
    "subject_pronouns": """
Marie described several different people and groups.

[bold cyan]"I'll describe a situation and you tell me the right
pronoun. One person? A group? All women? Mixed?
Formal or informal? Every detail matters!"[/bold cyan]
""",
    "etre_avoir": """
Marie set up a rapid-fire conjugation challenge.

[bold cyan]"Etre or avoir? Which verb fits? And what's the right
form? This is the ultimate test of the two most
important verbs in French. Allez-y!"[/bold cyan]
""",
    "common_adjectives": """
Marie showed you pictures and asked you to describe them.

[bold cyan]"Beautiful or handsome? Before or after the noun?
Masculine or feminine form? Let's see if you can
put all the adjective rules together perfectly!"[/bold cyan]
""",
}
