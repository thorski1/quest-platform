"""
story.py — Narrative for the Daily Life skill pack.

Sensei (先生) guides you through everyday Japanese vocabulary
covering routines, work, hobbies, weather, shopping, and health.
"""

INTRO_STORY = """
[bold red]LEARN JAPANESE[/bold red]
[bold yellow]Chapter: Everyday Japanese[/bold yellow]

Sensei opened the curtains of a small Tokyo apartment,
letting morning light flood the room.

[bold cyan]"Language lives in the everyday,"[/bold cyan] Sensei said.
[bold cyan]"The words you use when you wake up, go to work,
talk about the weather, shop for groceries --
these are the words that make you fluent."[/bold cyan]

Sensei gestured out the window at the bustling streets below.

[bold cyan]"Textbooks teach you grammar. But daily life
teaches you how to actually live in Japanese.
Let's walk through a typical day together."[/bold cyan]

[bold white]Your journey into everyday Japanese begins now.[/bold white]
"""

ZONE_INTROS = {
    "morning_routine": """
Sensei's alarm clock buzzed at 6:30 AM.

[bold cyan]"Every Japanese morning follows a rhythm,"[/bold cyan] Sensei said.
[bold cyan]"おきる (get up), かおをあらう (wash your face),
はをみがく (brush your teeth), あさごはんをたべる (eat breakfast).
The vocabulary of routine is the vocabulary of life."[/bold cyan]

[bold white]Let's learn the morning routine![/bold white]
""",
    "school_work": """
Sensei put on a suit jacket and picked up a briefcase.

[bold cyan]"がっこう (school) and しごと (work) consume most
of the day in Japan,"[/bold cyan] Sensei said.
[bold cyan]"Whether you're a がくせい (student) or a かいしゃいん
(company employee), these words are essential."[/bold cyan]

[bold white]Let's learn school and work vocabulary![/bold white]
""",
    "hobbies": """
Sensei set out a collection of hobby items -- a book, a camera, running shoes.

[bold cyan]"しゅみはなんですか -- what are your hobbies?"[/bold cyan] Sensei said.
[bold cyan]"This is one of the most common questions in Japanese
conversation. Let's make sure you can answer it."[/bold cyan]

[bold white]Let's learn to talk about hobbies![/bold white]
""",
    "weather": """
Sensei looked out the window at a changing sky.

[bold cyan]"てんき (weather) is Japan's favorite small talk,"[/bold cyan] Sensei said.
[bold cyan]"いいてんきですね (nice weather, isn't it?) is how
thousands of conversations begin every day."[/bold cyan]

[bold white]Let's learn weather vocabulary![/bold white]
""",
    "shopping": """
Sensei walked into a convenience store -- a コンビニ.

[bold cyan]"かいもの (shopping) happens everywhere in Japan,"[/bold cyan] Sensei said.
[bold cyan]"From コンビニ to デパート (department stores),
knowing prices, quantities, and polite phrases is essential."[/bold cyan]

[bold white]Let's learn shopping vocabulary![/bold white]
""",
    "body_health": """
Sensei pointed to a simple anatomy chart on the wall.

[bold cyan]"Knowing body parts and health words could save your life,"[/bold cyan]
Sensei said seriously. [bold cyan]"あたま (head), おなか (stomach),
びょういん (hospital). If you're sick in Japan, you need these words."[/bold cyan]

[bold white]Let's learn body and health vocabulary![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "morning_routine": """
[bold green]Sensei smiled at the sunrise![/bold green]

[bold cyan]"You now know the rhythm of a Japanese morning.
These everyday words will serve you every single day."[/bold cyan]
""",
    "school_work": """
[bold green]Sensei put away the briefcase with satisfaction![/bold green]

[bold cyan]"School and work vocabulary mastered.
You can navigate the professional side of Japanese life."[/bold cyan]
""",
    "hobbies": """
[bold green]Sensei applauded your interests![/bold green]

[bold cyan]"Now you can share your hobbies in Japanese.
This is how friendships begin."[/bold cyan]
""",
    "weather": """
[bold green]Sensei looked pleased at the clear sky![/bold green]

[bold cyan]"Weather mastered! You can make small talk
like a true Japanese local."[/bold cyan]
""",
    "shopping": """
[bold green]Sensei handed you a shopping bag![/bold green]

[bold cyan]"You can shop confidently in Japan now.
From prices to politeness, you're ready."[/bold cyan]
""",
    "body_health": """
[bold green]Sensei gave a relieved nod![/bold green]

[bold cyan]"Body and health vocabulary complete.
If anything goes wrong, you can communicate what you need."[/bold cyan]
""",
}

BOSS_INTROS = {
    "morning_routine": """
Sensei set up a morning scenario.

[bold cyan]"Walk me through a complete Japanese morning.
Show me you know every step."[/bold cyan]
""",
    "school_work": """
Sensei played the role of a colleague.

[bold cyan]"Introduce yourself at a new workplace.
Use the right vocabulary and politeness."[/bold cyan]
""",
    "hobbies": """
Sensei asked the classic question.

[bold cyan]"しゅみはなんですか? Answer me fully.
Tell me what you enjoy."[/bold cyan]
""",
    "weather": """
Sensei pointed to various weather symbols.

[bold cyan]"Describe today's weather. Use the right words
for what you see outside."[/bold cyan]
""",
    "shopping": """
Sensei set up a mock store counter.

[bold cyan]"Buy what you need. Ask the price, pay,
and be polite. All in Japanese."[/bold cyan]
""",
    "body_health": """
Sensei played the role of a doctor.

[bold cyan]"Tell me what hurts. Describe your symptoms.
Your Japanese could save your life."[/bold cyan]
""",
}
