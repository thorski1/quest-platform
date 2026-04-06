"""
story.py — Narrative for the Cultures of the World skill pack.

The Primer opens The World Festival — discover how people live, eat, dress,
speak, and build homes across the globe!
Puck guides the reader through five vibrant zones.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The World Festival[/bold yellow]

Puck appeared at the top of the page, standing before a pair of
enormous gates woven from flowers, fabric, and flags from every nation.
Above them, letters spelled out in every alphabet:
[bold yellow]THE WORLD FESTIVAL[/bold yellow]

[bold cyan]"Behind these gates,"[/bold cyan] Puck said, eyes wide with wonder,
[bold cyan]"is the whole world.
Not a map — the real thing. The celebrations people dance to.
The foods their grandmothers taught them to cook.
The clothes they wear with pride.
The languages they whisper, sing, and shout in.
And the homes they build — from snow, from mud,
from felt, and even on water."[/bold cyan]

The girl pressed her hand against the gate. [bold white]"Can I see it all?"[/bold white]

[bold cyan]"Every last bit."[/bold cyan] Puck grinned.
[bold cyan]"And by the time we're done, you'll know
how people live in every corner of the Earth —
and just how much we all share."[/bold cyan]

The gates swung open. Music, laughter, and the smell of a thousand
kitchens drifted out — and the whole world waited inside.

[bold cyan]"Ready to celebrate?"[/bold cyan]

[bold white]Your journey through The World Festival begins now.[/bold white]
"""

ZONE_INTROS = {
    "celebrations": """
Puck flew through the gates into a dazzling square filled with lights,
fireworks, and the sound of drums from every direction.

[bold cyan]"Celebrations!"[/bold cyan] Puck laughed, spinning in the air.
[bold cyan]"Every culture on Earth has special days — days when
people come together to eat, dance, sing, and remember
what matters most. Some celebrate with lights.
Some with parades. Some with feasts. All with joy."[/bold cyan]

Five glowing festivals shimmered ahead:
[bold yellow]Diwali · Chinese New Year · Carnival · Hanukkah · Eid[/bold yellow]

[bold white]Let's discover how the world celebrates![/bold white]
""",
    "traditional_foods": """
Puck pushed open the doors to an enormous kitchen — pots bubbling,
bread baking, and spices swirling in the air.

[bold cyan]"Food,"[/bold cyan] Puck said, taking a deep breath,
[bold cyan]"is how families say 'I love you' without words.
Every culture has special dishes — recipes passed down
from grandparents to parents to children.
Some are thousands of years old!"[/bold cyan]

Five steaming dishes waited on a long table:
[bold yellow]Sushi · Pasta · Tacos · Injera · Dim Sum[/bold yellow]

[bold white]Let's taste the foods of the world![/bold white]
""",
    "traditional_clothing": """
Puck opened a wardrobe that seemed to stretch on forever —
silk, cotton, wool, and fabric of every colour imaginable.

[bold cyan]"Clothing,"[/bold cyan] Puck said softly, running a hand along a bolt of silk,
[bold cyan]"isn't just about keeping warm. It tells a story.
Where you come from. What you believe.
Who your family is. And what makes you proud."[/bold cyan]

Four beautiful garments floated gently on display:
[bold yellow]Kimono · Sari · Kilt · Dashiki[/bold yellow]

[bold white]Let's see what the world wears![/bold white]
""",
    "languages": """
Puck floated up to a tall tower made entirely of books,
scrolls, and glowing letters in every alphabet.

[bold cyan]"Languages!"[/bold cyan] Puck whispered in amazement.
[bold cyan]"There are about seven THOUSAND of them.
Some are spoken by a billion people. Some by only a handful.
Some are written left to right. Some right to left.
Some use characters instead of letters.
And some don't use writing at all — they're spoken with hands."[/bold cyan]

Words in a hundred languages floated through the air:
[bold yellow]Mandarin · Sign Language · Alphabets · French · Swahili[/bold yellow]

[bold white]Let's explore the languages of the world![/bold white]
""",
    "homes": """
Puck landed on a hilltop overlooking an extraordinary neighbourhood —
igloos next to houseboats, yurts beside adobe houses,
treehouses above and caves below.

[bold cyan]"Home,"[/bold cyan] Puck said warmly,
[bold cyan]"is wherever your family is. But look at HOW people build!
In the Arctic, they use snow. In the desert, mud and straw.
On the grasslands, felt and wood that packs up in two hours.
On the water, a boat that never docks.
People are geniuses at building exactly what they need."[/bold cyan]

Five homes glowed softly in the distance:
[bold yellow]Igloo · Yurt · Houseboat · Adobe House · and more![/bold yellow]

[bold white]Let's visit the homes of the world![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "celebrations": """
[bold green]The Festival Square blazes with light — every celebration explored![/bold green]

Diwali's lamps, Chinese New Year's dragons, Carnival's dancers,
Hanukkah's candles, Eid's feasts — all glowing, all understood.

[bold cyan]"Every culture celebrates,"[/bold cyan] Puck says happily.
[bold cyan]"Different lights, different music, different food —
but the same joy. Isn't that beautiful?"[/bold cyan]

The smell of something delicious drifts from ahead. The Global Kitchen awaits...
""",
    "traditional_foods": """
[bold green]The Global Kitchen is complete — every dish tasted and understood![/bold green]

Sushi rolled, pasta twirled, tacos filled, injera shared,
and dim sum steamed — a feast from every continent.

[bold cyan]"Food connects people,"[/bold cyan] Puck says, patting a full tummy.
[bold cyan]"A grandmother's recipe can travel across oceans
and still taste like home."[/bold cyan]

Beautiful fabrics shimmer ahead. The Wardrobe of the World awaits...
""",
    "traditional_clothing": """
[bold green]The Wardrobe of the World shines — every garment known![/bold green]

Kimonos, saris, kilts, and dashikis —
each one a story sewn in fabric and colour.

[bold cyan]"Clothes aren't just clothes,"[/bold cyan] Puck says proudly.
[bold cyan]"They're how people show the world who they are
and where they come from."[/bold cyan]

Words in a thousand languages whisper ahead. The Tower of Tongues awaits...
""",
    "languages": """
[bold green]The Tower of Tongues glows — every language celebrated![/bold green]

Seven thousand languages. Hundreds of alphabets.
Hands that speak. Words that carry worlds.

[bold cyan]"Every language,"[/bold cyan] Puck says softly,
[bold cyan]"is a treasure. When one is lost,
a whole way of seeing the world disappears.
So learn a new word today — in any language!"[/bold cyan]

Homes of every shape rise on the horizon. The Neighbourhood of the World awaits...
""",
    "homes": """
[bold green]Every home visited — the Neighbourhood of the World is complete![/bold green]

Igloos of snow, yurts on the move, houseboats on still water,
and adobe walls baked by the sun — each one a masterpiece.

[bold cyan]"People build with what they have,"[/bold cyan] Puck says,
[bold cyan]"and what they build is always beautiful.
Snow, mud, felt, water — it doesn't matter.
Home is wherever your family is."[/bold cyan]

Puck looks at you warmly.

[bold white]Explorer. Traveller. Student. Ambassador. Citizen of the World.[/bold white]
[bold white]That's who you've become.[/bold white]
""",
}

BOSS_INTROS = {
    "celebrations": "Puck holds up a glowing globe covered in tiny sparkling lights. [bold yellow]\"You've seen celebrations from around the world — now tell me about one! Name a celebration AND where it's from!\"[/bold yellow]",
    "traditional_foods": "Puck stands in a kitchen wearing a tiny chef's hat, surrounded by ingredients from every continent. [bold yellow]\"One of these amazing foods is used as a plate AND a utensil — and it's made from a grain that only grows in one country. Which food is it?\"[/bold yellow]",
    "traditional_clothing": "Puck struts down a tiny runway surrounded by the most beautiful garments in the world. [bold yellow]\"One of these garments is made from a SINGLE piece of fabric up to 9 metres long — no stitching at all! Which one is it?\"[/bold yellow]",
    "languages": "Puck stands atop a tower of books, each in a different language. [bold yellow]\"Here's the big question: about how many languages are spoken in the world today? Think carefully!\"[/bold yellow]",
    "homes": "Puck stands on a hilltop overlooking homes from every zone. [bold yellow]\"One of these homes can be taken apart in two hours and carried on horseback. Nomads have used it for thousands of years. Which home is it?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "festival_explorer": (
        "Festival Explorer",
        "Discovered how people celebrate around the world!",
    ),
    "global_chef": (
        "Global Chef",
        "Tasted the traditional foods of every continent!",
    ),
    "fashion_scholar": (
        "Fashion Scholar",
        "Learned about the beautiful clothing of different cultures!",
    ),
    "word_traveller": (
        "Word Traveller",
        "Explored the incredible variety of the world's languages!",
    ),
    "world_architect": (
        "World Architect",
        "Visited the amazing homes people build around the world!",
    ),
}
