"""
story.py — Narrative for the Environment & Ecology skill pack.

Puck opens the Primer's greenest pages and guides the reader through
ecosystems, the water cycle, climate, recycling, endangered habitats,
renewable energy, and how one kid can change the world.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Green Pages[/bold yellow]

The Primer opened to a page the girl had never seen before.
It was green — not printed green, but [italic]living[/italic] green.
Tiny leaves unfurled across the margins. A miniature waterfall
tumbled down the spine of the book. And somewhere, very faintly,
she could hear birdsong.

[bold cyan]"Ah,"[/bold cyan] said Puck, landing on a dandelion that had sprouted
from the page. [bold cyan]"The Green Pages. These are the pages
about the Earth itself — not where things are, but how they
[italic]work.[/italic] How forests breathe. How water travels.
How everything alive is connected to everything else."[/bold cyan]

The girl watched a tiny caterpillar inch across a leaf.
[bold white]"Connected how?"[/bold white]

[bold cyan]"That,"[/bold cyan] Puck said, eyes sparkling, [bold cyan]"is exactly
what we're going to find out. And along the way, you'll learn
something even more important — what [italic]you[/italic] can do
to help keep it all alive."[/bold cyan]

The Primer's greenest pages rustled in an invisible breeze.

[bold cyan]"Ready to protect our planet?"[/bold cyan]

[bold white]Your adventure through the living world begins now.[/bold white]
"""

ZONE_INTROS = {
    "ecosystems": """
Puck flew to a page showing a forest, a pond, a desert, and a coral reef —
all alive, all humming with tiny creatures.

[bold cyan]"An ecosystem,"[/bold cyan] Puck said, [bold cyan]"is a community.
Not a town of people — a community of [italic]everything[/italic] living
in one place: plants, animals, fungi, even tiny bacteria.
They all depend on each other."[/bold cyan]

Tiny arrows appeared between the creatures — a web of connections.

[bold cyan]"Some make their own food from sunlight. Some eat plants.
Some eat the plant-eaters. And when anything dies, the decomposers
break it down so the soil can feed new life. It's a circle —
and every part matters."[/bold cyan]

[bold white]Let's explore the web of life![/bold white]
""",
    "water_cycle": """
Puck pointed upward. A tiny cloud formed above the open page,
and a single raindrop fell — splashing into a miniature ocean.

[bold cyan]"Water,"[/bold cyan] Puck said, [bold cyan]"never disappears.
The water you drink today might have been rain a thousand years ago.
It rises, it falls, it flows, it freezes — and it does this
over and over again, forever. We call it the water cycle."[/bold cyan]

Arrows traced the path: ocean to cloud to rain to river to ocean again.

[bold cyan]"Every living thing on Earth depends on this cycle.
Let's follow the water!"[/bold cyan]

[bold white]Where does the water go? Let's find out![/bold white]
""",
    "climate_and_weather": """
Puck held up two tiny cards. One showed a thunderstorm.
The other showed a long, slow calendar of sunshine.

[bold cyan]"Weather,"[/bold cyan] Puck said, holding up the storm,
[bold cyan]"is what's happening outside [italic]right now.[/italic]
Climate —"[/bold cyan] Puck held up the calendar —
[bold cyan]"is the pattern of weather over [italic]many, many years.[/italic]
They sound the same, but they're very different."[/bold cyan]

The page shifted through seasons — snow, blossoms, sunshine, falling leaves.

[bold cyan]"And the biggest question of all: why is the Earth
getting warmer? The answer is simpler than you think —
and more important than almost anything."[/bold cyan]

[bold white]Let's understand weather, climate, and the seasons![/bold white]
""",
    "recycling": """
Puck landed on a page covered in things: a plastic bottle, a banana peel,
a stack of newspapers, a torn t-shirt, a broken toy.

[bold cyan]"Everything we use,"[/bold cyan] Puck said, [bold cyan]"has to go somewhere
when we're done with it. And 'somewhere' used to mean a big hole
in the ground — a landfill. But the Earth is running out of holes."[/bold cyan]

Three glowing words appeared: [bold yellow]REDUCE  ·  REUSE  ·  RECYCLE[/bold yellow]

[bold cyan]"These three words can change everything.
Use less. Use again. And when you really can't use it anymore —
make sure it becomes something new."[/bold cyan]

[bold white]Let's learn how to give our waste a second life![/bold white]
""",
    "endangered_earth": """
The page turned dark. A forest shrank. Water turned murky.
A coral reef faded from bright colour to pale white.

[bold cyan]"This page is harder than the others,"[/bold cyan] Puck said quietly.
[bold cyan]"Because it shows what happens when we don't take care
of the Earth. Forests cut down. Oceans filled with plastic.
Animals losing the only home they've ever known."[/bold cyan]

But then — a small green shoot pushed through the dark soil.

[bold cyan]"But here's the thing: it's not too late.
Not even close. People all over the world are working
to fix these problems — and now you'll understand
exactly what they're fighting for."[/bold cyan]

[bold white]Let's learn what's at stake — and why it matters.[/bold white]
""",
    "renewable_energy": """
Puck flew to a page split down the middle. On one side:
a dark, smoky factory with a tall chimney. On the other:
a bright hillside covered in solar panels and windmills.

[bold cyan]"For a long time,"[/bold cyan] Puck said, [bold cyan]"we got our energy
by burning things — coal, oil, gas. They worked,
but they filled the sky with invisible gases that trap heat
and warm the Earth."[/bold cyan]

The sunny side of the page grew brighter.

[bold cyan]"But the sun shines every day. The wind blows.
Rivers flow. And clever people figured out how to catch
that energy — clean energy, energy that doesn't hurt the air."[/bold cyan]

[bold white]Let's discover the power of the sun, wind, and water![/bold white]
""",
    "what_you_can_do": """
Puck flew to the very last green page — and it was blank.

[bold cyan]"This page,"[/bold cyan] Puck said with a grin,
[bold cyan]"is for [italic]you.[/italic] Because everything we've learned
so far — ecosystems, water, climate, recycling, endangered places,
clean energy — it all comes down to one question:"[/bold cyan]

A single line of golden text appeared on the blank page:

[bold yellow]What will YOU do?[/bold yellow]

[bold cyan]"You're a kid. But kids can plant trees. Kids can save water.
Kids can teach their families. Kids can change the world.
And it starts with knowing what to do."[/bold cyan]

[bold white]Let's fill this page with everything you can do to help![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "ecosystems": """
[bold green]The web of life glows across the page![/bold green]

Producers, consumers, decomposers — all connected,
all depending on each other in a beautiful, balanced web.

[bold cyan]"You see it now,"[/bold cyan] Puck says warmly.
[bold cyan]"Nothing in nature lives alone. Every creature,
every plant, every tiny mushroom is part of something bigger.
And when the web is healthy, everything thrives."[/bold cyan]

A tiny raindrop forms above the page. The water cycle is next...
""",
    "water_cycle": """
[bold green]The water cycle spins in a perfect, endless loop![/bold green]

Evaporation lifts the water up. Condensation forms the clouds.
Precipitation brings it down. And the rivers carry it home again.

[bold cyan]"Every drop matters,"[/bold cyan] Puck says.
[bold cyan]"The rain that falls on your roof traveled thousands of miles
to get there — and it will travel thousands more after.
Water is the Earth's greatest traveler."[/bold cyan]

The clouds part to reveal sunshine and snowflakes. Climate and weather are next...
""",
    "climate_and_weather": """
[bold green]The seasons turn like a great, gentle wheel![/bold green]

Spring, summer, autumn, winter — and behind them all,
the slow, long story of climate stretching back thousands of years.

[bold cyan]"Weather changes every day,"[/bold cyan] Puck says.
[bold cyan]"Climate changes over lifetimes. And right now,
the Earth's climate is changing faster than it should.
But you understand why — and that's the first step
to doing something about it."[/bold cyan]

Three glowing words appear: Reduce, Reuse, Recycle. The recycling zone awaits...
""",
    "recycling": """
[bold green]The three Rs shine like gold: REDUCE - REUSE - RECYCLE![/bold green]

Bottles become new bottles. Food scraps become rich soil.
Old clothes find new homes. Nothing has to be wasted.

[bold cyan]"Every time you recycle,"[/bold cyan] Puck says proudly,
[bold cyan]"you're telling the Earth: I care about you.
And every time you reduce or reuse, you're doing
something even better — making sure there's less waste
in the first place."[/bold cyan]

The page darkens slightly. It's time to face the harder truths...
""",
    "endangered_earth": """
[bold green]A green shoot pushes through the dark — hope is growing![/bold green]

Forests being replanted. Oceans being cleaned. Coral reefs
being protected. Endangered animals given safe places to live.

[bold cyan]"The problems are real,"[/bold cyan] Puck says seriously.
[bold cyan]"But so are the solutions. People are planting billions of trees.
Countries are banning single-use plastics. Marine parks are growing.
The fight isn't over — but it's a fight we can win."[/bold cyan]

Solar panels gleam on the next page. Clean energy is calling...
""",
    "renewable_energy": """
[bold green]The sun, wind, and water glow with clean, endless power![/bold green]

Solar panels catch the light. Wind turbines spin on green hills.
Water rushes through dams, powering cities without a puff of smoke.

[bold cyan]"The future of energy,"[/bold cyan] Puck says brightly,
[bold cyan]"is already here. Every year, more and more of our power
comes from the sun, the wind, and the water.
And the best part? They'll never run out."[/bold cyan]

The final green page waits — blank, ready to be filled by you...
""",
    "what_you_can_do": """
[bold green]The blank page is blank no more — it's covered in YOUR actions![/bold green]

Plant a tree. Turn off the tap. Walk instead of drive.
Carry a reusable bottle. Pick up litter. Tell a friend.
Compost your apple core. Learn, and keep learning.

[bold cyan]"You did it,"[/bold cyan] Puck says, wings shining green.
[bold cyan]"You learned how the Earth works — and how to take care of it.
Ecosystems, water, climate, recycling, endangered places,
clean energy, and your own power to make a difference.
The Green Pages are yours now."[/bold cyan]

[bold white]Seedling. Sprout. Guardian. Ranger. Champion. Earth Hero.[/bold white]
[bold white]That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "ecosystems": "Puck points to a creature at the very bottom of the food web. [bold yellow]\"Everything depends on these tiny, quiet workers. Without them, dead things would pile up and nothing new could grow. What are they called?\"[/bold yellow]",
    "water_cycle": "A cloud hangs heavy over the Primer's page. [bold yellow]\"Water rises as invisible gas, then cools high in the sky and turns back into tiny droplets that form clouds. What is this process called?\"[/bold yellow]",
    "climate_and_weather": "Puck holds up a tiny model of the Earth, tilted to one side. [bold yellow]\"This tilt — just 23.5 degrees — is the reason we have summer and winter. But what actually causes the greenhouse effect to work?\"[/bold yellow]",
    "recycling": "Puck stands on a pile of banana peels and leaves. [bold yellow]\"There's a way to turn food scraps and garden waste into rich, dark soil that helps plants grow. What is this process called?\"[/bold yellow]",
    "endangered_earth": "The page shows a beautiful underwater world — but half of it has turned ghostly white. [bold yellow]\"When the ocean gets too warm, these living structures lose their colour and begin to die. What is happening to them?\"[/bold yellow]",
    "renewable_energy": "Puck stands between a solar panel and a lump of coal. [bold yellow]\"Burning coal and oil releases a gas that traps heat in the atmosphere like a blanket. What is this gas called?\"[/bold yellow]",
    "what_you_can_do": "The blank page glows with golden light. [bold yellow]\"One single tree can absorb a huge amount of carbon dioxide in its lifetime. But trees do something else that's just as important — what do they release into the air?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "ecosystem_expert": (
        "Ecosystem Expert",
        "Explored food webs, producers, consumers, and the balance of nature!",
    ),
    "water_wizard": (
        "Water Wizard",
        "Traced every drop through the water cycle — from ocean to cloud to rain and back!",
    ),
    "climate_scholar": (
        "Climate Scholar",
        "Learned the difference between climate and weather and understood the greenhouse effect!",
    ),
    "recycling_champion": (
        "Recycling Champion",
        "Mastered reduce, reuse, recycle — and composting too!",
    ),
    "habitat_defender": (
        "Habitat Defender",
        "Stood up for endangered forests, oceans, coral reefs, and habitats!",
    ),
    "energy_pioneer": (
        "Energy Pioneer",
        "Discovered how the sun, wind, and water can power our world!",
    ),
    "eco_hero": (
        "Eco Hero",
        "Learned how one kid can make a real difference for planet Earth!",
    ),
}
