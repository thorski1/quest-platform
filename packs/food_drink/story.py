"""
story.py — Narrative for the Food & Drink skill pack.

Long Long guides you through the delicious world of Chinese cuisine,
from fruits and drinks to ordering food and understanding food culture.
"""

INTRO_STORY = """
[bold red]LEARN CHINESE[/bold red]
[bold yellow]Chapter: The Dragon's Kitchen[/bold yellow]

The smell hit you first -- ginger, garlic, chili oil, and steaming rice.
Long Long had landed in the middle of a night market, surrounded by
dozens of food stalls, each one sizzling and steaming and fragrant.

[bold cyan]"Food,"[/bold cyan] Long Long said reverently, [bold cyan]"is the heart of Chinese culture.
China has one of the oldest and most diverse cuisines on Earth.
Sichuan is fiery. Cantonese is delicate. Northern food is hearty.
And everywhere, food is how people show love."[/bold cyan]

A vendor called out, holding up skewers of something delicious.
Long Long translated: [bold yellow]"Chuan'r! Yang rou chuan'r!"[/bold yellow]
(Skewers! Lamb skewers!)

[bold cyan]"There's an old Chinese saying: min yi shi wei tian
(民以食为天) -- 'food is the people's heaven'.
To understand China, you must understand its food.
And to eat well, you need the right words."[/bold cyan]

Long Long's stomach growled audibly.

[bold cyan]"Shall we eat our way through the vocabulary?"[/bold cyan]

[bold white]Your culinary journey through Chinese begins now.[/bold white]
"""

ZONE_INTROS = {
    "fruits_vegetables": """
Long Long stood before a colorful produce stand.

[bold cyan]"Let's start fresh -- literally!"[/bold cyan] Long Long said.
[bold cyan]"Fruits and vegetables are some of the easiest food words
to learn, and you'll see them everywhere: supermarkets,
street vendors, and on every restaurant menu."[/bold cyan]

[bold white]Let's learn the names of Chinese fruits and vegetables![/bold white]
""",
    "drinks": """
Long Long poured tea from a tiny clay teapot.

[bold cyan]"China is the birthplace of tea,"[/bold cyan] Long Long said.
[bold cyan]"But there's so much more to drink: water, coffee, juice,
milk, and yes -- beer. Let's learn how to order them all."[/bold cyan]

[bold white]Let's master drink vocabulary in Chinese![/bold white]
""",
    "common_dishes": """
Long Long sat down at a table covered in steaming dishes.

[bold cyan]"These are the dishes that define Chinese cuisine,"[/bold cyan]
Long Long said. [bold cyan]"Rice, noodles, dumplings, stir-fry --
the staples that billions of people eat every day.
You'll see these on every menu in China."[/bold cyan]

[bold white]Let's learn the most famous Chinese dishes![/bold white]
""",
    "ordering_food": """
Long Long picked up a menu with anticipation.

[bold cyan]"Knowing food words is great,"[/bold cyan] Long Long said,
[bold cyan]"but you also need to know HOW to order.
'I want...', 'bring one of...', 'the check please' --
these phrases turn vocabulary into actual meals."[/bold cyan]

[bold white]Let's learn to order food like a local![/bold white]
""",
    "tastes": """
Long Long set out five small bowls, each a different color.

[bold cyan]"Chinese cuisine is built on five fundamental flavors,"[/bold cyan]
Long Long said. [bold cyan]"Sweet, sour, bitter, spicy, and salty.
A great dish balances these. A great eater can name them all."[/bold cyan]

[bold white]Let's explore the five flavors of Chinese food![/bold white]
""",
    "cooking_words": """
Long Long tied on a tiny apron.

[bold cyan]"To truly understand Chinese food,"[/bold cyan] Long Long said,
[bold cyan]"you need to know how it's cooked. Stir-frying, boiling,
steaming, roasting, slicing -- each method creates a
completely different dish from the same ingredients."[/bold cyan]

[bold white]Let's learn the essential cooking methods![/bold white]
""",
    "food_culture": """
Long Long set a pair of chopsticks on the table with care.

[bold cyan]"Food in China is never just food,"[/bold cyan] Long Long said.
[bold cyan]"It's family, tradition, celebration, and respect.
How you eat, what you eat, who you eat with --
all of it carries deep cultural meaning."[/bold cyan]

[bold white]Let's discover the culture behind Chinese cuisine![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "fruits_vegetables": """
[bold green]Long Long juggled three fruits in the air![/bold green]

[bold cyan]"You know your fruits and vegetables in Chinese!
Now you can shop at any Chinese market with confidence!"[/bold cyan]
""",
    "drinks": """
[bold green]Long Long raised a cup of tea in celebration![/bold green]

[bold cyan]"From water to tea to beer -- you can order any drink!
Let's toast to that: gan bei! (干杯! Cheers!)"[/bold cyan]
""",
    "common_dishes": """
[bold green]Long Long patted a very full dragon belly![/bold green]

[bold cyan]"Rice, noodles, dumplings, buns -- the essentials are yours!
You could read a Chinese menu and actually know what you're ordering!"[/bold cyan]
""",
    "ordering_food": """
[bold green]Long Long called the waiter with confidence![/bold green]

[bold cyan]"You can walk into any Chinese restaurant and order a meal!
From sitting down to paying the bill, you've got it covered!"[/bold cyan]
""",
    "tastes": """
[bold green]Long Long savored each flavor one more time![/bold green]

[bold cyan]"Sweet, sour, bitter, spicy, salty -- the five pillars of Chinese flavor.
You can now describe any dish like a true food critic!"[/bold cyan]
""",
    "cooking_words": """
[bold green]Long Long took off the apron triumphantly![/bold green]

[bold cyan]"Stir-fry, boil, steam, roast, slice -- you know the kitchen verbs!
You could follow a Chinese recipe or understand what the chef is doing!"[/bold cyan]
""",
    "food_culture": """
[bold green]Long Long placed the chopsticks down with respect![/bold green]

[bold cyan]"You understand the soul of Chinese food culture -- chopsticks, tea,
dim sum, hotpot, and the traditions behind them all.
Food connects you to China in the deepest way."[/bold cyan]
""",
}

BOSS_INTROS = {
    "fruits_vegetables": """
Long Long lined up produce for a final quiz.

[bold cyan]"Name them all! From watermelon to potato,
show me you know your Chinese produce!"[/bold cyan]
""",
    "drinks": """
Long Long arranged an entire drink menu.

[bold cyan]"What are you having? Name every drink and order it properly!"[/bold cyan]
""",
    "common_dishes": """
Long Long presented a massive Chinese menu.

[bold cyan]"Identify the dish! This is the real restaurant test!"[/bold cyan]
""",
    "ordering_food": """
Long Long played the role of waiter.

[bold cyan]"Order a full meal -- from start to finish, in Chinese!"[/bold cyan]
""",
    "tastes": """
Long Long blindfolded the dragon eyes.

[bold cyan]"Describe the flavor! Which taste dominates each dish?"[/bold cyan]
""",
    "cooking_words": """
Long Long lit the stove.

[bold cyan]"How is it cooked? Match the method to the dish!"[/bold cyan]
""",
    "food_culture": """
Long Long set a formal Chinese dinner table.

[bold cyan]"The ultimate food culture challenge! Traditions, customs,
and the deep meaning behind Chinese dining."[/bold cyan]
""",
}
