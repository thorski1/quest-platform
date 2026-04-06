"""
story.py — Narrative for the Food & Drink skill pack.

Sensei (先生) guides you through Japanese food vocabulary,
ordering, tastes, chopstick manners, and dining culture.
"""

INTRO_STORY = """
[bold red]LEARN JAPANESE[/bold red]
[bold yellow]Chapter: The Japanese Kitchen[/bold yellow]

Sensei led you through a bustling Tokyo side street,
past steaming ramen shops and glowing izakaya lanterns.

[bold cyan]"Food is the soul of Japan,"[/bold cyan] Sensei said, breathing in the aroma.
[bold cyan]"Every dish tells a story. Every meal has its rituals.
You say いただきます before eating, ごちそうさま after.
You hold your chopsticks with care, and you never waste."[/bold cyan]

Sensei stopped at a small restaurant and slid the door open.

[bold cyan]"To truly experience Japan, you need to know
what to eat, how to order, and how to show respect
at the table. Let's begin."[/bold cyan]

[bold white]Your journey into Japanese food culture starts now.[/bold white]
"""

ZONE_INTROS = {
    "common_foods": """
Sensei pointed to a colorful display of plastic food models outside a restaurant.

[bold cyan]"Japanese cuisine is built on a few staples,"[/bold cyan] Sensei said.
[bold cyan]"ごはん (rice), ラーメン (ramen), すし (sushi), てんぷら (tempura).
These are the words you'll see on every menu."[/bold cyan]

[bold white]Let's learn the essential Japanese foods![/bold white]
""",
    "drinks": """
Sensei stopped at a vending machine glowing with options.

[bold cyan]"Japan has vending machines on every corner,"[/bold cyan] Sensei said.
[bold cyan]"おちゃ (tea), みず (water), ビール (beer), コーヒー (coffee).
Knowing your drinks is survival knowledge here."[/bold cyan]

[bold white]Let's learn Japanese drink vocabulary![/bold white]
""",
    "ordering": """
Sensei sat down at a restaurant table and handed you a menu.

[bold cyan]"Ordering in Japanese is polite and formulaic,"[/bold cyan] Sensei said.
[bold cyan]"...をください (...o kudasai) = please give me...
...をおねがいします (...o onegaishimasu) = I'd like...
These two patterns will get you through any restaurant."[/bold cyan]

[bold white]Let's learn how to order food and drinks![/bold white]
""",
    "tastes": """
Sensei set out small dishes with different flavors.

[bold cyan]"Describing taste is part of appreciating food,"[/bold cyan] Sensei said.
[bold cyan]"おいしい (delicious), からい (spicy), あまい (sweet),
しょっぱい (salty), にがい (bitter). Your tongue needs vocabulary too."[/bold cyan]

[bold white]Let's learn to describe flavors in Japanese![/bold white]
""",
    "chopstick_etiquette": """
Sensei placed a pair of chopsticks in front of you.

[bold cyan]"Chopsticks -- おはし -- have strict rules in Japan,"[/bold cyan] Sensei said.
[bold cyan]"Never stick them upright in rice. Never pass food
chopstick-to-chopstick. These actions are associated with
funeral rituals and are deeply taboo."[/bold cyan]

[bold white]Let's learn proper chopstick etiquette![/bold white]
""",
    "food_culture": """
Sensei folded their hands before an imaginary meal.

[bold cyan]"Before and after every meal, Japanese people speak,"[/bold cyan] Sensei said.
[bold cyan]"いただきます before eating -- 'I humbly receive.'
ごちそうさまでした after eating -- 'It was a feast.'
These are not optional. They are the heartbeat of Japanese dining."[/bold cyan]

[bold white]Let's learn the rituals of Japanese food culture![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "common_foods": """
[bold green]Sensei clapped approvingly![/bold green]

[bold cyan]"You now know the essential Japanese foods.
Walk into any restaurant in Japan and you'll recognize the menu."[/bold cyan]
""",
    "drinks": """
[bold green]Sensei raised an imaginary cup![/bold green]

[bold cyan]"You can order any drink in Japan now.
From tea houses to izakayas, you'll never go thirsty."[/bold cyan]
""",
    "ordering": """
[bold green]Sensei gave you a thumbs-up![/bold green]

[bold cyan]"You can order confidently in any Japanese restaurant.
ください and おねがいします are your keys to any menu."[/bold cyan]
""",
    "tastes": """
[bold green]Sensei savored an imaginary bite![/bold green]

[bold cyan]"You can now describe flavors in Japanese.
おいしい is the word every cook wants to hear."[/bold cyan]
""",
    "chopstick_etiquette": """
[bold green]Sensei nodded with quiet pride![/bold green]

[bold cyan]"You understand chopstick manners now.
This knowledge shows deep respect for Japanese culture."[/bold cyan]
""",
    "food_culture": """
[bold green]Sensei bowed with hands together![/bold green]

[bold cyan]"いただきます and ごちそうさま -- you understand the spirit
of gratitude that surrounds every Japanese meal. Beautiful."[/bold cyan]
""",
}

BOSS_INTROS = {
    "common_foods": """
Sensei pointed to a restaurant menu with no pictures.

[bold cyan]"Read the menu. Tell me what each dish is.
Show me you know your Japanese food basics."[/bold cyan]
""",
    "drinks": """
Sensei stood before a vending machine with labels covered.

[bold cyan]"Which button gives you tea? Which one is beer?
Prove you know your Japanese drinks."[/bold cyan]
""",
    "ordering": """
Sensei played the role of a waiter, notepad ready.

[bold cyan]"Order a complete meal -- food and drink.
Use proper Japanese ordering phrases."[/bold cyan]
""",
    "tastes": """
Sensei presented several unlabeled dishes.

[bold cyan]"Taste and describe. Use the right Japanese word
for each flavor."[/bold cyan]
""",
    "chopstick_etiquette": """
Sensei set up a formal dinner table.

[bold cyan]"Show me you know what NOT to do with chopsticks.
One wrong move can offend an entire table."[/bold cyan]
""",
    "food_culture": """
Sensei prepared a full traditional meal.

[bold cyan]"From the first word to the last, show me
you understand the ritual of a Japanese meal."[/bold cyan]
""",
}
