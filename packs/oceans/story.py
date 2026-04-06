"""
story.py — Narrative for the Ocean Explorers skill pack.

The Primer becomes a submarine — Puck guides the reader down through every
layer of the ocean, from sunlit shallows to crushing abyss, meeting whales
and sharks, coral cities and deep-sea monsters, ocean currents and the
people working to protect it all.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Deep Dive[/bold yellow]

The Primer's pages rippled — not like paper, but like water.
Blue-green waves rolled across the open book, and the edges
of the page curved upward into a hull, a periscope,
a row of glowing portholes.

[bold cyan]"Hold on,"[/bold cyan] Puck said, pulling a pair of tiny goggles
over bright eyes. [bold cyan]"The Primer is becoming a submarine."[/bold cyan]

The girl watched the room dissolve into ocean.
Fish darted past the windows. Sunlight filtered down in columns of gold.

[bold white]"We're going underwater?"[/bold white]

[bold cyan]"All the way down."[/bold cyan] Puck tapped a depth gauge on the wall.
[bold cyan]"The ocean covers more than 70 percent of our planet,
and most of it has never been explored. There are mountains
down here taller than Everest. Creatures that make their own light.
Rivers of warm water that control the weather of entire continents."[/bold cyan]

Puck's wings folded into a tiny captain's coat.

[bold cyan]"Surface to abyss. Whales to microbes. Coral cities to volcanic vents.
The deepest, most mysterious world on Earth — and it's been here
all along, just beneath the waves."[/bold cyan]

The submarine hummed. The depth gauge began to tick.

[bold cyan]"Ready to dive?"[/bold cyan]

[bold white]Your ocean adventure begins now.[/bold white]
"""

ZONE_INTROS = {
    "ocean_zones": """
The submarine hovered at the surface, sunlight streaming through the water.

[bold cyan]"The ocean isn't just one big pool,"[/bold cyan] Puck said, pressing
a button that lit up a cross-section of the sea on the wall.
[bold cyan]"It has layers — like a building with many floors.
Each floor has different light, different pressure,
different creatures. And the deeper you go,
the stranger it gets."[/bold cyan]

Four layers glowed on the diagram:
[bold yellow]Sunlight · Twilight · Midnight · Abyss[/bold yellow]

[bold white]Let's explore every layer of the ocean![/bold white]
""",
    "marine_mammals": """
A great whooshing sound echoed through the submarine, and a spray
of mist erupted from the surface above.

[bold cyan]"Mammals,"[/bold cyan] Puck said warmly. [bold cyan]"Warm-blooded, air-breathing,
milk-feeding mammals — living right here in the cold ocean.
Whales the length of two buses. Dolphins that call each other
by name. Otters that use tools. Seals that dive deeper
than skyscrapers are tall."[/bold cyan]

A pod of dolphins raced past the porthole.

[bold white]Let's meet the warm hearts of the cold sea![/bold white]
""",
    "coral_reefs": """
The submarine rose into shallow, crystal-clear water, and colour
exploded in every direction — purple fans, orange branches,
green plates, pink fingers.

[bold cyan]"Coral reefs,"[/bold cyan] Puck breathed. [bold cyan]"The cities of the sea.
More species live on a coral reef than almost anywhere else
in the ocean. And every bit of it — every branch, every fan —
is built by tiny animals no bigger than your fingernail."[/bold cyan]

A clownfish peeked out of an anemone and stared at the submarine.

[bold white]Let's explore the rainforests of the sea![/bold white]
""",
    "deep_sea": """
The submarine's lights cut through absolute darkness.
The depth gauge read 2,000 metres. Then 3,000.

[bold cyan]"Welcome to the deep,"[/bold cyan] Puck whispered.
[bold cyan]"No sunlight has ever reached this place.
The pressure would crush a car. The water is barely
above freezing. And yet — life is everywhere.
Strange life. Glowing life. Life that looks like it belongs
on another planet."[/bold cyan]

A faint blue spark drifted past the window.

[bold white]Let's meet the strangest creatures on Earth![/bold white]
""",
    "ocean_currents": """
Puck pulled up a glowing map of the world's oceans. Red and blue
arrows swirled across it in great loops.

[bold cyan]"The ocean moves,"[/bold cyan] Puck said. [bold cyan]"Not just waves and tides —
the whole ocean flows in enormous currents, like invisible rivers
thousands of kilometres long. Warm water flows from the tropics
toward the poles. Cold water sinks and flows back.
It takes a thousand years for water to go all the way around."[/bold cyan]

The submarine caught a current and surged forward.

[bold white]Let's ride the rivers of the sea![/bold white]
""",
    "sharks_and_rays": """
A shadow passed over the submarine — something sleek,
powerful, and very old.

[bold cyan]"Sharks,"[/bold cyan] Puck said with a respectful nod.
[bold cyan]"They've been here for over 400 million years —
before the dinosaurs, before the trees, before almost
everything. And rays — their graceful cousins — glide
through the water like living wings."[/bold cyan]

A hammerhead shark swept past, its wide head scanning
the water like a metal detector.

[bold white]Let's meet the ocean's most ancient hunters![/bold white]
""",
    "ocean_conservation": """
The submarine surfaced near a beach. Plastic bottles and bags
floated on the water. A seabird struggled with a piece of netting.

Puck was quiet for a moment.

[bold cyan]"The ocean has given us everything,"[/bold cyan] Puck said softly.
[bold cyan]"It gives us the air we breathe, the rain that waters our food,
the fish that feed billions of people. It controls our climate.
It is the heart of our planet."[/bold cyan]

Puck looked up.

[bold cyan]"But it needs our help now. Plastic, overfishing,
warming water, rising acid — the ocean is in trouble.
And the good news? Every single one of us can be part
of the solution."[/bold cyan]

[bold white]Let's learn how to protect the ocean — starting today.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "ocean_zones": """
[bold green]All four ocean layers glow on the submarine's depth chart![/bold green]

Sunlight, twilight, midnight, abyss — each one explored,
each one understood.

[bold cyan]"You know the architecture of the sea,"[/bold cyan] Puck says proudly.
[bold cyan]"From the sunny surface where life teems
to the crushing dark of the abyss —
you've mapped it all."[/bold cyan]

A whale song echoes from somewhere above. The mammals are calling...
""",
    "marine_mammals": """
[bold green]The warm-blooded ocean dwellers are all accounted for![/bold green]

Whales, dolphins, seals, sea lions, and otters —
each one known, each one marvelled at.

[bold cyan]"Warm hearts in cold water,"[/bold cyan] Puck says.
[bold cyan]"They breathe air like us, feed their babies milk like us,
and yet they chose the ocean as their home.
Remarkable creatures."[/bold cyan]

The water ahead turns crystal clear. Something colourful glitters below...
""",
    "coral_reefs": """
[bold green]The coral city blazes with colour and life![/bold green]

Polyps, algae, fish, turtles — the whole reef ecosystem
understood, from its tiny builders to its greatest threats.

[bold cyan]"Coral reefs are the most beautiful places in the ocean,"[/bold cyan]
Puck says, [bold cyan]"and the most fragile. Now you understand
why they matter — and why we must protect them."[/bold cyan]

The submarine dives deeper. The light fades. Something glows in the dark...
""",
    "deep_sea": """
[bold green]The abyss has surrendered its secrets![/bold green]

Anglerfish, giant squid, hydrothermal vents, bioluminescence,
and the deepest trench on Earth — all explored.

[bold cyan]"You've been to the bottom of the world,"[/bold cyan] Puck says quietly.
[bold cyan]"Deeper than Everest is tall. Into darkness no sunlight
has ever touched. And you found life even there.
The ocean never stops surprising us."[/bold cyan]

The submarine catches a current and begins to move. The invisible rivers are next...
""",
    "ocean_currents": """
[bold green]The great ocean highways glow on the map![/bold green]

Gulf Stream, conveyor belt, upwelling zones —
the invisible forces that shape our world, now visible to you.

[bold cyan]"Currents are the ocean's circulatory system,"[/bold cyan] Puck says.
[bold cyan]"They carry heat, nutrients, and life around the globe.
Without them, the world's climate would be unrecognisable."[/bold cyan]

A shadow passes overhead. Something ancient this way comes...
""",
    "sharks_and_rays": """
[bold green]The ancient hunters of the deep are known![/bold green]

Cartilage skeletons, electroreception, conveyor-belt teeth,
gentle whale sharks and soaring manta rays — all understood.

[bold cyan]"Four hundred million years,"[/bold cyan] Puck says with awe.
[bold cyan]"Sharks survived every mass extinction this planet has seen.
They are the ocean's greatest success story."[/bold cyan]

The submarine surfaces near a beach. There is one more lesson ahead...
""",
    "ocean_conservation": """
[bold green]The ocean's story is complete — and its future is in your hands![/bold green]

Plastic pollution, overfishing, acidification, marine protected areas,
and the power of individual action — all understood.

[bold cyan]"You've dived to the bottom of the sea,"[/bold cyan] Puck says,
eyes bright. [bold cyan]"You've met whales and sharks, explored coral cities,
ridden the great currents, and seen the strangest creatures on Earth.
And now you know the most important thing of all:
the ocean needs people who understand it. People who care."[/bold cyan]

Puck smiles.

[bold cyan]"People like you."[/bold cyan]

[bold white]Ocean Explorer. Deep Diver. Guardian of the Sea. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "ocean_zones": "Puck points to the depth chart on the submarine wall. [bold yellow]\"You've learned about each layer. Now — can you put them in order, from the surface all the way down to the crushing deep?\"[/bold yellow]",
    "marine_mammals": "Puck pulls out a diagram of a whale's body. [bold yellow]\"All these mammals live in freezing water, but they're warm-blooded. There's one secret they all share — a built-in winter coat. What is it?\"[/bold yellow]",
    "coral_reefs": "The submarine hovers over a ghostly white reef. Puck's voice is serious. [bold yellow]\"This coral has lost its colour. Something has gone very wrong. Do you know what causes coral bleaching?\"[/bold yellow]",
    "deep_sea": "The depth gauge ticks past 10,000 metres. Puck stares at the number. [bold yellow]\"We're approaching the deepest point in any ocean on Earth. If you dropped Mount Everest in here, it would disappear completely. How deep are we?\"[/bold yellow]",
    "ocean_currents": "Puck traces a single loop around the entire globe. [bold yellow]\"One drop of water, traveling on the great ocean conveyor belt, takes an almost unbelievable amount of time to complete the journey. How long?\"[/bold yellow]",
    "sharks_and_rays": "Puck holds up a single shark tooth, then points to the rows of replacements behind it. [bold yellow]\"Sharks never run out of teeth. But just how many teeth can one shark go through in a lifetime? The answer might astonish you.\"[/bold yellow]",
    "ocean_conservation": "Puck looks through the submarine window at the vast blue ocean. [bold yellow]\"Scientists have set a goal — a percentage of the ocean that must be protected by 2030. It has a catchy name. Do you know the number?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "zone_mapper": (
        "Zone Mapper",
        "Explored every layer of the ocean from sunlight to abyss!",
    ),
    "mammal_watcher": (
        "Mammal Watcher",
        "Met every warm-blooded creature in the cold ocean!",
    ),
    "reef_guardian": (
        "Reef Guardian",
        "Understood coral reefs — their beauty and their fragility!",
    ),
    "abyss_diver": (
        "Abyss Diver",
        "Explored the strangest creatures in the deepest darkness!",
    ),
    "current_rider": (
        "Current Rider",
        "Rode the invisible rivers that shape our planet's climate!",
    ),
    "shark_scholar": (
        "Shark Scholar",
        "Met the ocean's most ancient and misunderstood predators!",
    ),
    "ocean_guardian": (
        "Ocean Guardian",
        "Learned how to protect the ocean — and promised to try!",
    ),
}
