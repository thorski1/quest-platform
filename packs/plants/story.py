"""
story.py — Narrative for the Plants skill pack.

Puck opens the Primer to pages of living green — roots digging down,
leaves turning toward the sun, flowers blooming in fast-forward.
The secret life of plants unfolds, from seed to forest.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Secret Garden[/bold yellow]

The Primer's pages turned on their own — and something [italic]grew.[/italic]

A tiny green shoot pushed up from the paper, unfolding two perfect
leaves. Then another. And another. Vines curled along the margins.
Flowers bloomed in the corners. A whole garden was growing
right there on the page.

[bold cyan]"Plants!"[/bold cyan] Puck appeared perched on a sunflower that hadn't
been there a moment ago. [bold cyan]"The quietest, most amazing living
things on Earth. They don't run. They don't roar. They don't
have eyes or ears or brains — and yet they conquered the
entire planet."[/bold cyan]

A tiny tree grew from the spine of the book, its roots wrapping
around the binding, its branches reaching toward the light.

[bold white]"How?"[/bold white] the girl asked, touching a petal with one careful finger.

[bold cyan]"By doing something no animal can do,"[/bold cyan] Puck said, wings
glowing green. [bold cyan]"They eat sunlight. They drink rain. They
breathe the air and turn it into food. They make the oxygen
we breathe. Every forest, every garden, every blade of grass —
it all starts with one tiny seed."[/bold cyan]

Puck held up a seed no bigger than a full stop.

[bold cyan]"Shall we plant it and see what grows?"[/bold cyan]

[bold white]Your journey through the secret garden begins now.[/bold white]
"""

ZONE_INTROS = {
    "parts_of_a_plant": """
The Primer opened to a page that showed a single, perfect plant —
roots spreading underground, a strong stem reaching upward, wide
green leaves, a bright flower, and a plump fruit hanging from a branch.

[bold cyan]"Every plant has the same basic parts,"[/bold cyan] Puck said, tracing
a finger from root to flower tip. [bold cyan]"Roots that drink.
A stem that carries. Leaves that make food. Flowers that attract.
And fruits that protect the seeds for the next generation."[/bold cyan]

Golden labels appeared beside each part:
[bold yellow]Roots · Stem · Leaves · Flower · Fruit[/bold yellow]

[bold cyan]"Each part has a job. Take one away, and the whole plant
struggles. Together? They're a perfect team."[/bold cyan]

[bold white]Let's explore each part of a plant![/bold white]
""",
    "how_plants_grow": """
The page turned, and time sped up. A seed split open in the soil.
A root pushed down. A shoot pushed up. Leaves unfurled. A stem
thickened. A flower opened. A fruit swelled. Seeds scattered.
The whole life of a plant played out in seconds.

[bold cyan]"Growing,"[/bold cyan] Puck said quietly, watching the cycle repeat.
[bold cyan]"It starts with a seed no bigger than a crumb. Give it
water, warmth, and a little patience — and it becomes
something extraordinary."[/bold cyan]

Five glowing words appeared:
[bold yellow]Seeds · Germination · Sunlight · Water · Soil[/bold yellow]

[bold cyan]"These are the secrets of growth. Master them,
and you can grow anything."[/bold cyan]

[bold white]Let's discover how plants grow![/bold white]
""",
    "photosynthesis": """
The page began to glow — actually [italic]glow[/italic] — with warm golden light.
A leaf appeared, magnified a thousand times, and inside it tiny green
particles were spinning, catching light, building something.

[bold cyan]"Photosynthesis,"[/bold cyan] Puck said the word slowly, letting each
syllable shine. [bold cyan]"The most important chemical reaction on Earth.
Plants take sunlight, water, and carbon dioxide — a gas in the air —
and turn them into food and oxygen. [italic]They make food from light.[/italic]
No animal can do that. No machine can do it as well."[/bold cyan]

A simple equation appeared in golden letters:
[bold yellow]Sunlight + Water + Carbon Dioxide → Sugar + Oxygen[/bold yellow]

[bold cyan]"Every breath you take? Thank a plant."[/bold cyan]

[bold white]Let's understand the magic of photosynthesis![/bold white]
""",
    "trees_and_forests": """
The Primer's pages opened wide, and a forest grew from the binding.
Towering oaks and whispering pines, golden maples dropping leaves
and dark firs standing tall in the snow — all of them alive,
all of them ancient, all of them telling stories in their rings.

[bold cyan]"Trees,"[/bold cyan] Puck said with awe, flying between the branches.
[bold cyan]"The oldest, tallest, most magnificent plants on Earth.
Some have been alive for thousands of years. Some are taller
than buildings. And together, they make forests — the green
lungs of our planet."[/bold cyan]

Four golden topics glowed in the canopy:
[bold yellow]Deciduous · Evergreen · Rainforest · Tree Rings[/bold yellow]

[bold cyan]"Let's walk among the giants."[/bold cyan]

[bold white]Let's explore the world of trees and forests![/bold white]
""",
    "plants_we_eat": """
The final chapter opened to an illustrated feast — a long table
covered with food, every dish glowing with colour. Bright red
tomatoes. Golden wheat. Green basil. Orange carrots. Purple grapes.
White rice in steaming bowls.

[bold cyan]"Everything on this table,"[/bold cyan] Puck said, landing beside
a crusty loaf of bread, [bold cyan]"came from a plant. The bread
from wheat. The pasta from flour. The salad from leaves.
The fruit from flowers. Even the spices — cinnamon from bark,
pepper from berries, vanilla from orchids."[/bold cyan]

Five glowing labels appeared:
[bold yellow]Fruits · Vegetables · Grains · Herbs · Spices[/bold yellow]

[bold cyan]"Plants don't just give us air. They give us
breakfast, lunch, and dinner."[/bold cyan]

[bold white]Let's discover the plants on our plates![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "parts_of_a_plant": """
[bold green]Every part of the plant glows with understanding![/bold green]

Roots drinking deep. Stems carrying life upward. Leaves catching
sunlight. Flowers calling to pollinators. Fruits protecting
the precious seeds inside.

[bold cyan]"You see the whole plant now,"[/bold cyan] Puck says proudly.
[bold cyan]"Not just green stuff growing in the dirt — a living machine
where every part has a purpose. Roots, stem, leaves, flower, fruit.
A perfect team."[/bold cyan]

The page turns to a time-lapse of growth. Something is sprouting...
""",
    "how_plants_grow": """
[bold green]The cycle of growth spins on the page — seed to plant to seed again![/bold green]

Seeds splitting open. Roots reaching down. Shoots stretching
toward the light. Leaves unfurling like tiny green flags.

[bold cyan]"You know the recipe now,"[/bold cyan] Puck says, holding up
a tiny watering can. [bold cyan]"Water, sunlight, good soil, and time.
That's all it takes to turn a seed into something wonderful.
You could grow a garden. You could grow a forest."[/bold cyan]

The page begins to glow with golden light. Photosynthesis awaits...
""",
    "photosynthesis": """
[bold green]The equation of life shines on the page in golden letters![/bold green]

Sunlight plus water plus carbon dioxide equals sugar and oxygen.
The most important recipe on Earth, happening in every leaf,
every second of every day.

[bold cyan]"You understand it now,"[/bold cyan] Puck says, and there's real
wonder in those bright eyes. [bold cyan]"Plants eat light. They breathe
for us. Every breath you take, every meal you eat — it all
traces back to a green leaf catching sunshine."[/bold cyan]

Tall shadows appear on the next page. The trees are calling...
""",
    "trees_and_forests": """
[bold green]The forest grows tall and proud across the page![/bold green]

Deciduous trees in autumn gold. Evergreen pines in winter white.
Rainforest layers stretching from dark floor to bright canopy.
Tree rings counting centuries of quiet, patient life.

[bold cyan]"Trees are the cathedrals of nature,"[/bold cyan] Puck says softly,
sitting on a branch. [bold cyan]"They house millions. They clean the air.
They hold the soil. They outlive everything. And they started —
every single one of them — as a tiny seed no bigger than your thumb."[/bold cyan]

The page turns to a colourful feast. The garden has one more gift...
""",
    "plants_we_eat": """
[bold green]The table is full — every dish a gift from the plant kingdom![/bold green]

Fruits and vegetables and grains and herbs and spices — an entire
world of flavour and nourishment, all grown from the earth.

[bold cyan]"You've done it."[/bold cyan] Puck's wings spread wide, glowing green
and gold. [bold cyan]"Parts of a plant. How they grow. Photosynthesis.
Trees and forests. And now, the plants that feed the world.
The whole secret garden — understood, explored, and loved."[/bold cyan]

Puck lands on the girl's shoulder, holding a tiny seed.

[bold cyan]"Everything starts with a seed. And now you know
exactly what that seed can become."[/bold cyan]

[bold white]Garden Keeper. Seed Sower. Friend of Every Growing Thing. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "parts_of_a_plant": "Puck traces a shimmering blue line from the bottom of the page to the top, following water's journey through a plant. [bold yellow]\"Water travels from one end of the plant to the other. Do you know the path it takes?\"[/bold yellow]",
    "how_plants_grow": "Puck holds up a tiny golden seed and a watering can, a painted sun glowing behind them. [bold yellow]\"You want to grow the strongest, healthiest plant. What does this little seed need from you?\"[/bold yellow]",
    "photosynthesis": "The page glows with a golden equation — sunlight, water, and carbon dioxide on one side, sugar on the other, and one blank space. [bold yellow]\"Plants take in sunlight, water, and carbon dioxide. They make sugar and one more thing. The thing you're breathing right now. What is it?\"[/bold yellow]",
    "trees_and_forests": "Puck stands before a magnificent illustrated forest, every kind of tree you could imagine growing side by side. [bold yellow]\"Trees produce oxygen, provide homes, and help control the climate. But someone says cutting them down doesn't matter. You know better — which statement is true?\"[/bold yellow]",
    "plants_we_eat": "The illustrated table groans with food — every dish made from plants. Roots and stems and leaves and flowers and fruits and seeds. [bold yellow]\"We eat so many different parts of plants! Can you see the whole picture now?\"[/bold yellow]",
}
