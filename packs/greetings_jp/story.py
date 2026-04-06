"""
story.py — Narrative for the Greetings skill pack.

Sensei (先生) guides you through essential Japanese greetings,
self-introduction, and the foundations of polite speech.
"""

INTRO_STORY = """
[bold red]LEARN JAPANESE[/bold red]
[bold yellow]Chapter: The Art of Japanese Greetings[/bold yellow]

Sensei stood at the entrance of a traditional Japanese home,
sliding the front door open with a gentle motion.

[bold cyan]"In Japan,"[/bold cyan] Sensei began, [bold cyan]"greetings are more than words.
They carry respect, warmth, and social awareness.
The right greeting at the right time shows you understand
not just the language, but the culture."[/bold cyan]

Sensei bowed slightly -- not too deep, not too shallow.

[bold cyan]"We have different greetings for morning, afternoon,
and evening. We introduce ourselves with a set pattern.
We apologize and thank with genuine feeling.
And we adjust our language based on who we're speaking to."[/bold cyan]

Sensei smiled.

[bold cyan]"Let's begin with the most important word
you'll ever learn in Japanese: こんにちは."[/bold cyan]

[bold white]Your journey into Japanese social language begins now.[/bold white]
"""

ZONE_INTROS = {
    "hello_goodbye": """
Sensei stood at the doorway, greeting an imaginary visitor.

[bold cyan]"Every day in Japan begins and ends with greetings,"[/bold cyan] Sensei said.
[bold cyan]"おはようございます in the morning, こんにちは during the day,
こんばんは in the evening, and さようなら when parting.
Each one sets the tone for the interaction."[/bold cyan]

[bold white]Let's learn the essential greetings![/bold white]
""",
    "self_intro": """
Sensei handed you a blank name card.

[bold cyan]"Self-introduction -- じこしょうかい -- is a ritual in Japan,"[/bold cyan] Sensei said.
[bold cyan]"You'll introduce yourself with: はじめまして (nice to meet you),
your name with ...です (I am ...), and よろしくおねがいします
(please treat me well). This pattern never changes."[/bold cyan]

[bold white]Let's learn to introduce yourself![/bold white]
""",
    "thanks_sorry": """
Sensei demonstrated two different bows -- one grateful, one apologetic.

[bold cyan]"ありがとう and すみません are two of the most useful words,"[/bold cyan]
Sensei explained. [bold cyan]"Japanese people express gratitude and
apology frequently. Even bumping into someone on the train
deserves a quick すみません."[/bold cyan]

[bold white]Let's master thanking and apologizing![/bold white]
""",
    "counting_people": """
Sensei gestured to a group of people passing by.

[bold cyan]"Counting people in Japanese uses a special counter: 人 (にん/り),"[/bold cyan]
Sensei said. [bold cyan]"But watch out -- one person and two people
have irregular readings: ひとり and ふたり."[/bold cyan]

[bold white]Let's learn to count and refer to people![/bold white]
""",
    "classroom": """
Sensei set up a mock classroom with a desk and chair.

[bold cyan]"In school or any learning environment, certain phrases
come up constantly,"[/bold cyan] Sensei explained.
[bold cyan]"わかりますか (do you understand?), わかりません (I don't understand),
もういちど おねがいします (one more time, please)."[/bold cyan]

[bold white]Let's learn essential classroom phrases![/bold white]
""",
    "keigo_basics": """
Sensei's posture became more formal.

[bold cyan]"Keigo -- polite speech -- is the heart of Japanese,"[/bold cyan]
Sensei said seriously. [bold cyan]"At minimum, you should know
the です/ます form. It turns casual speech into polite speech
and is what you should always use with strangers."[/bold cyan]

[bold white]Let's take your first steps into polite Japanese![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "hello_goodbye": """
[bold green]Sensei bowed warmly![/bold green]

[bold cyan]"You now know how to greet anyone in Japan at any time of day.
These simple words open every door."[/bold cyan]
""",
    "self_intro": """
[bold green]Sensei handed you your own name card![/bold green]

[bold cyan]"You can introduce yourself properly in Japanese now.
はじめまして -- from this moment, you can make new connections."[/bold cyan]
""",
    "thanks_sorry": """
[bold green]Sensei nodded with deep respect![/bold green]

[bold cyan]"Gratitude and humility -- ありがとう and すみません.
These two words will carry you far in Japan."[/bold cyan]
""",
    "counting_people": """
[bold green]Sensei smiled with satisfaction![/bold green]

[bold cyan]"You can count people correctly now -- even the tricky
ひとり and ふたり. This is practical, everyday Japanese."[/bold cyan]
""",
    "classroom": """
[bold green]Sensei gave you a gold star sticker![/bold green]

[bold cyan]"Essential classroom phrases mastered! You can now
navigate any Japanese lesson or conversation about learning."[/bold cyan]
""",
    "keigo_basics": """
[bold green]Sensei bowed deeply and formally![/bold green]

[bold cyan]"You've taken your first steps into keigo. Using です and ます
shows respect and cultural awareness. You're speaking properly now."[/bold cyan]
""",
}

BOSS_INTROS = {
    "hello_goodbye": """
Sensei set up three scenarios: morning, afternoon, and evening.

[bold cyan]"Match the right greeting to the right time.
Show me you know when to use each one."[/bold cyan]
""",
    "self_intro": """
Sensei played the role of a new acquaintance.

[bold cyan]"Introduce yourself to me, using the full pattern.
Get every part right."[/bold cyan]
""",
    "thanks_sorry": """
Sensei presented various social situations.

[bold cyan]"When to thank? When to apologize?
The right word at the right moment -- that's the test."[/bold cyan]
""",
    "counting_people": """
Sensei pointed to groups of different sizes.

[bold cyan]"Count these people correctly.
Remember the irregular forms!"[/bold cyan]
""",
    "classroom": """
Sensei spoke rapidly in Japanese.

[bold cyan]"You didn't understand. What do you say?
Use the classroom phrases you've learned."[/bold cyan]
""",
    "keigo_basics": """
Sensei presented casual sentences.

[bold cyan]"Convert these to polite form.
Show me you can speak with proper respect."[/bold cyan]
""",
}
