"""
story.py — Narrative for the Earth Science skill pack.

Nell and Puck explore the Earth — its rocks, volcanoes, water, soil, and resources.
"""

INTRO_STORY = """
[bold yellow]THE EARTH EXPLORER[/bold yellow]

[bold cyan]"Put your hand on the ground,"[/bold cyan] Puck said.

Nell knelt and pressed her palm flat against the earth.

[bold cyan]"Feel that? That's not just dirt.
That's the skin of a planet.
Beneath it, there are rocks older than anything alive.
Rivers of melted stone. Crystals growing in the dark.
Mountains being pushed up and worn down,
over and over, for billions of years."[/bold cyan]

Nell looked at the ground beneath her hand.
It didn't feel like much. Just soil. Cool and quiet.

[bold cyan]"The Earth looks still,"[/bold cyan] Puck whispered,
[bold cyan]"but it never stops moving.
Plates shift. Volcanoes build new land.
Water carves canyons. Wind shapes mountains.
And every rock has a story — if you know how to read it."[/bold cyan]

The Primer glowed with a warm amber light.

[bold cyan]"You walk on this planet every day.
Let's find out what it's made of."[/bold cyan]

[bold white]The ground is waiting. Let's explore![/bold white]
"""

ZONE_INTROS = {
    "rocks_and_minerals": """
Puck picked up a small stone and held it to the light.
It sparkled — just a little.

[bold cyan]"Every rock you've ever stepped on has a story,"[/bold cyan]
Puck said. [bold cyan]"Some were born in fire, spat out of volcanoes.
Some were built layer by layer at the bottom of ancient seas.
And some were squeezed and heated deep underground
until they became something entirely new."[/bold cyan]

[bold cyan]"Three kinds of rock. Three origin stories.
And hiding inside them — crystals, minerals, even gems."[/bold cyan]

[bold white]What stories are hidden inside the rocks around you?[/bold white]
""",
    "volcanoes_and_earthquakes": """
The ground trembled — just slightly.

[bold cyan]"Did you feel that?"[/bold cyan] Puck asked, eyes wide.
[bold cyan]"The Earth's surface is cracked into giant pieces,
and they're all slowly moving.
When they bump, slide, or pull apart —
the ground shakes. Mountains rise.
Volcanoes explode."[/bold cyan]

A distant rumble. A glow on the horizon.

[bold cyan]"The Earth isn't solid and still.
It's alive with motion — and it always has been."[/bold cyan]

[bold white]Why does the Earth shake and rumble?[/bold white]
""",
    "water_cycle": """
A single raindrop landed on Nell's hand.

[bold cyan]"That drop,"[/bold cyan] Puck said, [bold cyan]"has been on a journey
longer than you can imagine.
It might have been part of an ocean,
then a cloud, then a river, then a glacier,
then a puddle that evaporated yesterday —
and now it's here, on your hand."[/bold cyan]

[bold cyan]"Water never stops moving.
Up into the sky. Down as rain.
Into the ground. Back to the sea.
Round and round, forever."[/bold cyan]

[bold white]Where does water go, and where does it come from?[/bold white]
""",
    "soil_and_erosion": """
Puck dug a small hole and peered inside.

[bold cyan]"People walk over it every day and never think about it,"[/bold cyan]
Puck said. [bold cyan]"But soil is one of the most important things
on the entire planet. Without it, nothing grows.
No food. No forests. No life."[/bold cyan]

[bold cyan]"And it takes hundreds of years to make just one inch of it.
Hundreds of years — and a careless flood
can wash it away in minutes."[/bold cyan]

Puck brushed the dirt from tiny hands.

[bold cyan]"Soil, erosion, fossils, worms —
there's a whole world beneath your feet."[/bold cyan]

[bold white]What secrets lie in the ground below?[/bold white]
""",
    "natural_resources": """
Puck held up a leaf in one hand and a small dark stone in the other.

[bold cyan]"Both of these are gifts from the Earth,"[/bold cyan] Puck said.
[bold cyan]"The leaf comes from a tree that will grow back.
This stone — coal — took millions of years to form.
When it's gone, it's gone."[/bold cyan]

[bold cyan]"Some gifts renew themselves.
Some don't. And the ones that don't
are running out faster than most people realize."[/bold cyan]

Puck set both down gently.

[bold cyan]"Knowing the difference —
that's the first step to taking care of this planet."[/bold cyan]

[bold white]What does the Earth give us, and how do we protect it?[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "rocks_and_minerals": """
[bold green]The Rock Collection glitters with understanding![/bold green]

Igneous, sedimentary, metamorphic — three stories,
one endless cycle. And inside every rock, minerals
with their own crystal secrets.

[bold cyan]"You'll never look at a plain old rock the same way again,"[/bold cyan]
Puck says. [bold cyan]"Every one of them has been on a journey
of millions of years — and the journey isn't over."[/bold cyan]

[bold white]The rocks remember. And now, so do you.[/bold white]
""",
    "volcanoes_and_earthquakes": """
[bold green]The Shaking Earth settles — for now![/bold green]

Tectonic plates, fault lines, the Ring of Fire,
layers of the Earth all the way down to the iron core.

[bold cyan]"The ground beneath you is always moving,"[/bold cyan]
Puck says. [bold cyan]"Slowly, patiently, powerfully.
Building mountains. Opening oceans.
The Earth is never finished."[/bold cyan]

[bold white]You understand the forces that shape our world.[/bold white]
""",
    "water_cycle": """
[bold green]The Water Wanderers complete their journey![/bold green]

Evaporation, condensation, precipitation, groundwater —
the endless loop that gives life to everything.

[bold cyan]"Every glass of water you drink,"[/bold cyan] Puck says quietly,
[bold cyan]"has been on a billion-year adventure.
Ocean to cloud to rain to river to you.
And after you, it keeps going."[/bold cyan]

[bold white]Water connects everything. And now you know how.[/bold white]
""",
    "soil_and_erosion": """
[bold green]The Ground Beneath Us reveals its secrets![/bold green]

Topsoil, subsoil, bedrock. Weathering and erosion.
Composting and fossils. Earthworms tunneling in the dark.

[bold cyan]"Most people never think about what's under their feet,"[/bold cyan]
Puck says. [bold cyan]"But you will.
Every handful of soil is alive with stories —
and now you know how to read them."[/bold cyan]

[bold white]The earth beneath you is more alive than it looks.[/bold white]
""",
    "natural_resources": """
[bold green]The Treasures of the Earth are understood![/bold green]

Renewable and nonrenewable. Solar, wind, water.
Coal, oil, gas — and why they'll run out.
Reduce, reuse, recycle — and why it matters.

[bold cyan]"You know something important now,"[/bold cyan] Puck says.
[bold cyan]"This planet gives us everything we need.
But it can't give forever — not unless we help it.
And now you know how."[/bold cyan]

[bold white]One Earth. Your Earth. Take care of it.[/bold white]
""",
}

BOSS_INTROS = {
    "rocks_and_minerals": "A stone splits open to reveal glittering crystals inside. [bold yellow]\"The rock cycle never stops. Can you explain what keeps it going? Think about all three forces!\"[/bold yellow]",
    "volcanoes_and_earthquakes": "The ground trembles and a red glow appears on the horizon. [bold yellow]\"Why do volcanoes erupt? Think about what's happening deep underground — the pressure building, the magma rising...\"[/bold yellow]",
    "water_cycle": "A glass of water sits on a table, catching the light. [bold yellow]\"That water has been around for billions of years. Where has it been? Think about the biggest journey of all.\"[/bold yellow]",
    "soil_and_erosion": "A handful of rich, dark soil sits in a beam of sunlight, alive with tiny creatures. [bold yellow]\"Why does soil matter? Think about everything that depends on it — every plant, every creature, every meal.\"[/bold yellow]",
    "natural_resources": "A globe spins slowly, glowing blue and green. [bold yellow]\"We only get one planet. Why does it matter how we use its gifts? Think about what runs out and what doesn't.\"[/bold yellow]",
}
