"""
story.py — Narrative for the Cooking & Nutrition skill pack.

Puck opens the Primer's Kitchen and guides the reader through the world
of food — food groups, vitamins, labels, safety, cooking basics,
world cuisines, and healthy choices.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Kitchen Adventure[/bold yellow]

Puck appeared at the edge of the Primer's newest page, wearing a tiny
white apron and a chef's hat that kept slipping over one eye.
Behind Puck, something extraordinary was happening — a whole kitchen
was unfolding from the page, pots and pans and jars of spices
rising like a pop-up book made of golden light.

[bold cyan]"A kitchen!"[/bold cyan] Puck announced, spreading wings wide.
[bold cyan]"Not just any kitchen — the Primer's Kitchen, where food
becomes an adventure. Where every meal has a story, every
ingredient has a secret, and every bite teaches you something
about how your body works."[/bold cyan]

The girl leaned forward. [bold white]"Can I actually learn to cook in here?"[/bold white]

[bold cyan]"Even better."[/bold cyan] Puck hopped onto a tiny cutting board.
[bold cyan]"You'll learn [italic]why[/italic] food matters. What it does
inside your body. How to read the secret codes on food packages.
How to be safe with knives and heat. And then — the best part —
you'll discover the most amazing foods from every corner
of the world."[/bold cyan]

A rainbow of fruits and vegetables floated across the page,
followed by steaming bowls of rice, golden loaves of bread,
and plates of food from a dozen different countries.

[bold cyan]"Seven kitchens to explore. Forty lessons to learn.
And by the end, you'll know more about food than most grown-ups."[/bold cyan]

Puck adjusted the little chef's hat and grinned.

[bold cyan]"Ready to cook up some knowledge?"[/bold cyan]

[bold white]The Primer's Kitchen opens — where food becomes an adventure![/bold white]
"""

ZONE_INTROS = {
    "food_groups": """
Puck set five glowing plates on the kitchen table, each one a different color.

[bold cyan]"Everything you eat,"[/bold cyan] Puck said, [bold cyan]"belongs to
one of five great families. We call them the food groups.
Each one does something different for your body — and you need
ALL of them to be healthy and strong."[/bold cyan]

Five labels appeared above the plates:
[bold yellow]Fruits · Vegetables · Grains · Protein · Dairy[/bold yellow]

[bold cyan]"Fruits give you vitamins. Vegetables build your shield.
Grains fuel your engine. Protein builds your muscles.
Dairy strengthens your bones."[/bold cyan]

[bold white]Let's discover what each food group does for you![/bold white]
""",
    "vitamins_and_nutrients": """
Puck opened a tiny treasure chest, and light spilled out —
orange, green, white, red, and sparkling blue.

[bold cyan]"Inside every food,"[/bold cyan] Puck said, [bold cyan]"are tiny
invisible helpers called vitamins and nutrients. You can't see them,
but your body absolutely needs them. Each one has a special job."[/bold cyan]

The glowing helpers floated into the air, each wearing a tiny letter:
[bold yellow]Vitamin C · Calcium · Iron · Fiber · Water · Vitamin A[/bold yellow]

[bold cyan]"Some fight germs. Some build bones. Some carry oxygen
through your blood. And the most important one of all?
It comes straight from the tap."[/bold cyan]

[bold white]Let's meet the tiny heroes inside your food![/bold white]
""",
    "reading_labels": """
Puck pulled a cereal box from behind the kitchen counter
and flipped it around to show a panel covered in tiny numbers.

[bold cyan]"This,"[/bold cyan] Puck said, tapping the panel, [bold cyan]"is a
Nutrition Facts label. Every packaged food has one. And once
you learn to read it, you'll have a superpower — you'll know
exactly what's inside before you even take a bite."[/bold cyan]

Numbers and percentages glowed on the page:
[bold yellow]Calories · Fat · Sugar · Protein · Vitamins · Serving Size[/bold yellow]

[bold cyan]"Companies sometimes try to trick you with small serving sizes
and hidden sugars. But not us — we're going to be Label Detectives."[/bold cyan]

[bold white]Let's learn to read the secret codes on food packages![/bold white]
""",
    "kitchen_safety": """
Puck landed on the kitchen counter with a serious expression —
more serious than the girl had ever seen from the little sprite.

[bold cyan]"The kitchen,"[/bold cyan] Puck said quietly, [bold cyan]"is wonderful.
But it's also full of things that can hurt you if you're not careful.
Sharp knives. Hot stoves. Slippery floors. Invisible germs."[/bold cyan]

A tiny shield appeared in Puck's hands.

[bold cyan]"The rules I'm about to teach you aren't boring rules.
They're [italic]armor.[/italic] Real chefs follow every single one of them,
every single day. And once you know them, the kitchen becomes
the safest room in the house."[/bold cyan]

[bold white]Let's learn the rules that keep every chef safe![/bold white]
""",
    "cooking_basics": """
Puck lined up a row of tools on the counter — measuring cups,
wooden spoons, whisks, and a rolling pin.

[bold cyan]"Now that you know your food groups and your safety rules,"[/bold cyan]
Puck said, [bold cyan]"it's time to learn how to actually MAKE things.
Measuring. Mixing. The difference between baking and frying.
How to read a recipe. And some simple dishes you can help
make at home — starting today!"[/bold cyan]

A recipe book opened on the counter, its pages glowing softly.

[bold cyan]"Cooking is part science, part art, and part magic.
Let's learn the basics!"[/bold cyan]

[bold white]Welcome to Cooking 101![/bold white]
""",
    "foods_around_world": """
The Primer's Kitchen suddenly transformed — the walls dissolved
into a spinning globe, and the smells of a hundred different
kitchens filled the air.

[bold cyan]"Every country on Earth,"[/bold cyan] Puck said, inhaling deeply,
[bold cyan]"has its own food, its own flavors, its own way of cooking.
Sushi in Japan. Tacos in Mexico. Pasta in Italy.
Curry in India. Dim sum in China."[/bold cyan]

Tiny flags appeared above steaming dishes from around the world.

[bold cyan]"Food is how people share their culture. When you taste
a dish from another country, you're tasting their history,
their land, their story."[/bold cyan]

[bold white]Let's taste our way around the world![/bold white]
""",
    "healthy_choices": """
Puck sat at the edge of a table set for a perfect meal.

[bold cyan]"You've learned the food groups. The vitamins. The labels.
The safety rules. The cooking basics. Foods from every continent.
Now comes the most important lesson of all —
how to put it all together, every day."[/bold cyan]

A glowing plate appeared, divided into colorful sections.

[bold cyan]"Healthy eating isn't about being perfect. It's about
making good choices [italic]most[/italic] of the time. Balanced meals.
Smart snacks. Enough water. A good breakfast.
And yes — a treat now and then, because life should be delicious."[/bold cyan]

[bold white]Let's learn to choose wisely![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "food_groups": """
[bold green]All five food group plates glow with light![/bold green]

Fruits shimmer with vitamins. Vegetables gleam with strength.
Grains glow with golden energy. Protein flexes with power.
Dairy sparkles white for strong bones.

[bold cyan]"You know the five food groups,"[/bold cyan] Puck says proudly.
[bold cyan]"Every time you eat, you can look at your plate and think —
am I getting what my body needs?"[/bold cyan]

Tiny treasures begin to sparkle inside the food. The vitamins are next...
""",
    "vitamins_and_nutrients": """
[bold green]The treasure chest glows with every color of the rainbow![/bold green]

Vitamin C in orange. Calcium in white. Iron in deep red.
Fiber in brown. Water in crystal blue. Vitamin A in golden amber.

[bold cyan]"You know the tiny heroes now,"[/bold cyan] Puck says.
[bold cyan]"They're invisible, but they're working inside you
every single minute — building, repairing, protecting."[/bold cyan]

A cereal box appears on the counter. Time to learn to read the labels...
""",
    "reading_labels": """
[bold green]The magnifying glass glows — you're a certified Label Detective![/bold green]

Serving sizes, ingredient lists, percent daily values, hidden sugars —
you can spot them all now.

[bold cyan]"Most people never learn to read labels,"[/bold cyan] Puck says.
[bold cyan]"But you can. And that means no one can trick you
about what's really in your food."[/bold cyan]

Puck puts on a serious face. The kitchen safety zone is ahead...
""",
    "kitchen_safety": """
[bold green]The safety shield gleams bright — the kitchen is yours![/bold green]

Clean hands. Careful cuts. Respect for heat. Allergy awareness.
Fire safety. Every rule learned, every danger understood.

[bold cyan]"You know the rules now,"[/bold cyan] Puck says with a nod.
[bold cyan]"A real chef doesn't just make great food — a real chef
keeps everyone safe. That's you."[/bold cyan]

Measuring cups and spoons line up on the counter. Cooking 101 begins...
""",
    "cooking_basics": """
[bold green]The recipe book glows — you've mastered the basics![/bold green]

Measuring, mixing, folding, baking, frying — the tools
and techniques of the kitchen are in your hands.

[bold cyan]"You can follow a recipe,"[/bold cyan] Puck says with pride.
[bold cyan]"You know your teaspoons from your tablespoons,
your baking from your frying, and you always read
the whole recipe before you start."[/bold cyan]

The kitchen walls dissolve into a spinning globe. World foods await...
""",
    "foods_around_world": """
[bold green]The globe spins and every country's flag is lit![/bold green]

Sushi from Japan. Tacos from Mexico. Pasta from Italy.
Curry from India. Dim sum from China. Rice feeding half the planet.

[bold cyan]"Food connects every person on Earth,"[/bold cyan] Puck says softly.
[bold cyan]"When you taste a dish from another country,
you're sharing in their story. That's beautiful."[/bold cyan]

A perfect plate takes shape. The final lesson awaits — choosing wisely...
""",
    "healthy_choices": """
[bold green]The perfect plate glows — balanced, colorful, and beautiful![/bold green]

Balanced meals. Smart snacks. Less sugar. More water.
A good breakfast. And treats in moderation — because balance
means enjoying life, too.

[bold cyan]"You've done it."[/bold cyan] Puck's wings spread wide.
[bold cyan]"Food groups, vitamins, labels, safety, cooking, world foods,
and now — the wisdom to put it all together every day.
You know more about food than most grown-ups."[/bold cyan]

Puck removes the little chef's hat and places it on the page.

[bold white]Taster. Helper. Sous Chef. Chef. Master Chef. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "food_groups": "Puck sets a single empty plate on the table. [bold yellow]\"One plate. Five food groups. Can you build the perfect balanced meal?\"[/bold yellow]",
    "vitamins_and_nutrients": "Puck holds up an orange carrot and a golden mango. [bold yellow]\"These foods share a color and a vitamin. Both help your eyes see in dim light. Which vitamin is it?\"[/bold yellow]",
    "reading_labels": "Puck points to a percentage on a nutrition label. [bold yellow]\"This number tells you how much of your daily needs one serving covers. Do you know what it really means?\"[/bold yellow]",
    "kitchen_safety": "Puck stands in front of the stove with a very serious face. [bold yellow]\"A grease fire in a pan — the most dangerous moment in any kitchen. Do you know what to do? Remember: water is the WRONG answer!\"[/bold yellow]",
    "cooking_basics": "Puck holds up a handful of strawberries and a bowl. [bold yellow]\"Your first recipe! Something safe, delicious, and entirely your own. Which dish can a kid make right now?\"[/bold yellow]",
    "foods_around_world": "Puck holds up a single grain of rice. [bold yellow]\"This tiny grain feeds more than half the people on Earth. It's been farmed for 9,000 years. Do you know what it is?\"[/bold yellow]",
    "healthy_choices": "Puck winks and holds up a cookie in one hand and an apple in the other. [bold yellow]\"Here's the real secret of healthy eating — it's not about saying 'no' to everything. It's about one magic word. Do you know what it is?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "food_group_master": (
        "Food Group Master",
        "Learned what all five food groups do for your body!",
    ),
    "nutrient_hunter": (
        "Nutrient Hunter",
        "Discovered the vitamins and minerals hidden inside your food!",
    ),
    "label_detective": (
        "Label Detective",
        "Learned to read nutrition labels like a pro!",
    ),
    "safety_star": (
        "Safety Star",
        "Mastered every kitchen safety rule!",
    ),
    "junior_chef": (
        "Junior Chef",
        "Learned measuring, mixing, and the basics of cooking!",
    ),
    "world_taster": (
        "World Taster",
        "Tasted your way around the globe — from sushi to tacos!",
    ),
    "wise_eater": (
        "Wise Eater",
        "Learned to make balanced, healthy choices every day!",
    ),
}
