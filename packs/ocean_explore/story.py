"""
story.py — Narrative for the Ocean Explore skill pack.

The Primer becomes an advanced deep-sea research vessel. Puck guides the reader
through ocean zones, coral reefs, deep-sea creatures, ocean conservation,
and underwater technology — a comprehensive ocean adventure.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Deep Dive[/bold yellow]

The Primer's pages shimmered and went dark — then lit up
from within, a deep, pulsing blue. The edges of the book
curved upward into a hull of steel and glass, portholes
glowing with bioluminescent light.

[bold cyan]"Hold tight,"[/bold cyan] Puck said, fastening a tiny captain's hat
over bright eyes. [bold cyan]"The Primer is becoming a research vessel —
the kind that can go anywhere in the ocean. Surface to trench.
Reef to abyss."[/bold cyan]

Water swallowed the room. A school of silver fish exploded
past the windows and vanished into blue.

[bold white]"Where are we going?"[/bold white]

[bold cyan]"Everywhere."[/bold cyan] Puck tapped a glowing map on the wall.
[bold cyan]"The ocean covers more than 70 percent of our planet,
but we've explored less than a quarter of the seafloor.
There are mountains down here taller than anything on land.
Creatures that glow in colours we don't even have names for.
Reefs so vast they can be seen from space. Technology so clever
it lets us breathe underwater and send robots to the deepest
trenches."[/bold cyan]

Puck's wings folded into a tiny wetsuit.

[bold cyan]"Five expeditions. Ocean layers, coral cities, deep-sea monsters,
the fight to save it all, and the machines that take us there.
The most mysterious world on Earth is right beneath the waves —
and it has been waiting for someone like you."[/bold cyan]

The depth gauge began to tick. The adventure had begun.

[bold white]Your ocean exploration starts now.[/bold white]
"""

ZONE_INTROS = {
    "ocean_zones": """
The submarine hovered at the surface, sunlight streaming through crystal water.

[bold cyan]"The ocean is not just one big pool,"[/bold cyan] Puck said, pressing
a button that projected a cross-section of the sea onto the wall.
[bold cyan]"It has layers — like floors in an enormous building.
Each layer has different light, different pressure,
different temperatures, and completely different creatures.
The deeper you go, the stranger and more wonderful it becomes."[/bold cyan]

Five layers glowed on the diagram:
[bold yellow]Sunlight · Twilight · Midnight · Abyss · Hadal[/bold yellow]

[bold white]Let's dive through every layer of the ocean![/bold white]
""",
    "coral_reefs": """
The research vessel rose into warm, shallow water, and colour
erupted in every direction — branching purple fans, bright orange
plates, delicate pink fingers reaching toward the light.

[bold cyan]"Coral reefs,"[/bold cyan] Puck breathed, pressing against the glass.
[bold cyan]"The cities of the sea. They cover less than one percent
of the ocean floor, but a quarter of all marine species
call them home. And every branch, every fan, every tower
is built by tiny animals no bigger than the tip of your pencil."[/bold cyan]

A clownfish peered out from an anemone and stared at the vessel.

[bold white]Let's explore the rainforests of the sea![/bold white]
""",
    "deep_sea_creatures": """
The vessel's floodlights carved tunnels through absolute darkness.
The depth gauge read 2,000 metres. Then 3,000. Then 4,000.

[bold cyan]"Welcome to the deep,"[/bold cyan] Puck whispered, voice hushed.
[bold cyan]"No sunlight has ever touched this water. The pressure would
crush a car flat. The temperature hovers near freezing.
And yet — life is everywhere down here. Strange, beautiful,
terrifying life. Creatures that make their own light.
Animals with no eyes, no stomachs, no bones.
Life that looks like it drifted in from another galaxy."[/bold cyan]

A faint blue spark pulsed past the window. Then another. Then hundreds.

[bold white]Let's meet the strangest creatures on Earth![/bold white]
""",
    "ocean_conservation": """
The vessel surfaced near a coastline. The water should have been
crystal blue, but it was clouded with sediment and scattered with
floating plastic — bottles, bags, tangled fishing line.

Puck was quiet for a long time.

[bold cyan]"The ocean has given us everything,"[/bold cyan] Puck said softly.
[bold cyan]"It gives us the oxygen we breathe, the rain that waters
our food, the fish that feed billions of people.
It absorbs heat and CO2 that would otherwise cook the planet.
It is, quite literally, the life support system of Earth."[/bold cyan]

Puck looked up, eyes bright and serious.

[bold cyan]"But it needs our help. Plastic pollution, overfishing,
warming waters, rising acidity — the ocean is under pressure.
And the hopeful news? Every single one of us —
no matter how young — can be part of the solution."[/bold cyan]

[bold white]Let's learn how to protect the ocean — starting today.[/bold white]
""",
    "underwater_technology": """
Puck pressed a button, and the walls of the vessel became
transparent screens showing the history of ocean exploration —
from wooden diving bells to nuclear submarines to robot explorers
gliding through underwater canyons.

[bold cyan]"Humans are land animals,"[/bold cyan] Puck said, tapping a timeline
on the wall. [bold cyan]"We can't breathe underwater. We can't survive
the pressure. We can't see in the dark. And yet — we have found
ways to go everywhere. From the first breath of compressed air
to robots that explore the deepest trenches on their own,
our curiosity has always been stronger than our limitations."[/bold cyan]

A model ROV whirred past the window, cameras blinking.

[bold cyan]"Submarines, scuba gear, sonar, ROVs, satellites —
these are the tools that turn the impossible into the explored."[/bold cyan]

[bold white]Let's discover the machines of the deep![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "ocean_zones": """
[bold green]All five ocean layers glow on the vessel's depth chart![/bold green]

Sunlight, twilight, midnight, abyss, and hadal —
each one explored, each one understood.

[bold cyan]"You know the architecture of the sea,"[/bold cyan] Puck says proudly.
[bold cyan]"From the bright surface where life teems
to the volcanic vents of the abyss
to the crushing trenches where almost nothing
has ever been — you've mapped it all."[/bold cyan]

Colour shimmers ahead. The reefs are calling...
""",
    "coral_reefs": """
[bold green]The coral cities glow with colour and life![/bold green]

Polyps, algae, symbiosis, bleaching, barrier reefs —
the whole reef ecosystem understood, from its tiny builders
to its greatest threats.

[bold cyan]"Coral reefs are the most beautiful and fragile places
in the ocean,"[/bold cyan] Puck says. [bold cyan]"Now you understand
why they matter — and what we stand to lose."[/bold cyan]

The vessel dives deeper. The light fades. Something glows in the dark...
""",
    "deep_sea_creatures": """
[bold green]The creatures of the abyss have revealed their secrets![/bold green]

Anglerfish, giant squid, tube worms, vampire squid,
dumbo octopus, and the miracle of bioluminescence —
all met, all marvelled at.

[bold cyan]"You've been to the bottom of the world,"[/bold cyan] Puck says quietly.
[bold cyan]"Into darkness no sunlight has ever touched.
And you found life — strange, beautiful, resilient life —
even there. The ocean never stops surprising us."[/bold cyan]

The vessel surfaces. The real world returns — and it needs our help...
""",
    "ocean_conservation": """
[bold green]The ocean's story is told — and its future is in your hands![/bold green]

Plastic pollution, microplastics, overfishing, acidification,
ghost nets, marine protected areas, and the power of
individual action — all understood.

[bold cyan]"You now know more about the ocean's challenges than most
adults,"[/bold cyan] Puck says, eyes shining. [bold cyan]"And you know
the most important thing: it is not too late.
Every piece of plastic you refuse, every voice you raise,
every choice you make — it matters."[/bold cyan]

One more expedition remains. The machines of the deep await...
""",
    "underwater_technology": """
[bold green]The full history of ocean exploration technology is mapped![/bold green]

From wooden submarines to nuclear vessels, from the first
scuba breath to autonomous robots mapping the abyss —
the ingenuity of human curiosity, fully explored.

[bold cyan]"You've seen it all,"[/bold cyan] Puck says, standing before the
glowing map of the world's oceans. [bold cyan]"The layers, the reefs,
the creatures, the threats, and the tools we've built
to understand it all. You are an Ocean Explorer now —
someone who knows the ocean is not just water,
but the beating heart of our planet."[/bold cyan]

Puck salutes.

[bold cyan]"The ocean is lucky to have a friend like you."[/bold cyan]

[bold white]Ocean Explorer. Deep Diver. Reef Guardian. Tech Pioneer. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "ocean_zones": "Puck unfurls a glowing cross-section of the entire ocean. [bold yellow]\"Five layers, surface to trench. Can you name them all in the right order?\"[/bold yellow]",
    "coral_reefs": "Puck projects a map of the world's reefs — some green for healthy, others flashing red. [bold yellow]\"You've learned about reef builders and reef destroyers. Time for the final test: which threats are real?\"[/bold yellow]",
    "deep_sea_creatures": "Puck dims the lights and projects every deep-sea creature on the wall. [bold yellow]\"One creature holds a record that no other animal on Earth can match. Which one — and what record?\"[/bold yellow]",
    "ocean_conservation": "Puck stands before a giant globe, the ocean glowing blue. [bold yellow]\"Everything you've learned about the ocean's threats comes down to one truth. What is it?\"[/bold yellow]",
    "underwater_technology": "Puck gestures at a wall of screens showing ROV feeds, sonar maps, and satellite data. [bold yellow]\"From wooden barrels to robot explorers — which tools let us study the deep without risking human lives?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "zone_explorer": (
        "Zone Explorer",
        "Mapped every layer of the ocean from sunlight to hadal trench!",
    ),
    "reef_scholar": (
        "Reef Scholar",
        "Understood coral reefs — their beauty, their builders, and their battles!",
    ),
    "abyss_navigator": (
        "Abyss Navigator",
        "Met the strangest and most wonderful creatures of the deep!",
    ),
    "ocean_protector": (
        "Ocean Protector",
        "Learned how to protect the ocean — and promised to try!",
    ),
    "tech_pioneer": (
        "Tech Pioneer",
        "Mastered the machines that take us into the deep unknown!",
    ),
}
