"""
story.py — Narrative for the Electricity skill pack.

Nell and Puck explore the invisible world of electricity — sparks, circuits,
magnets, and the power that lights up the modern world.
"""

INTRO_STORY = """
[bold yellow]THE SPARK LAB[/bold yellow]

[bold cyan]"Hold very still,"[/bold cyan] Puck whispered.

Nell held still.

Puck floated close and touched a tiny spark to her fingertip.
A warm tingle ran up her arm.

[bold white]"What was that?"[/bold white] Nell asked, eyes wide.

[bold cyan]"That,"[/bold cyan] Puck said, grinning, [bold cyan]"was electricity.
The same invisible force that makes lightning crack across the sky,
that lights up every lamp in every house,
that makes your heart beat
and your brain think."[/bold cyan]

The Primer hummed with a faint golden glow.

[bold cyan]"Electricity is everywhere — in the walls of your home,
in the clouds above you, even inside your own body.
It's made of tiny, tiny things called electrons
that move from atom to atom, faster than you can blink."[/bold cyan]

Puck held up a small copper wire. A faint light traveled along it
like a firefly in a tunnel.

[bold cyan]"Once you understand electricity,"[/bold cyan] Puck said softly,
[bold cyan]"you understand one of the most powerful forces in the universe.
And it all starts with a single spark."[/bold cyan]

Nell watched the light travel down the wire and smiled.

[bold white]Let's begin![/bold white]
"""

ZONE_INTROS = {
    "what_is_electricity": """
Puck rubbed a small balloon against Nell's sleeve.
The balloon crackled and stuck to the wall.

[bold cyan]"See that?"[/bold cyan] Puck said. [bold cyan]"That's not magic.
That's electrons — tiny particles smaller than anything you've ever seen —
jumping from your sleeve to the balloon."[/bold cyan]

[bold cyan]"Everything is made of atoms, and atoms have electrons
spinning around them. When those electrons move,
you get electricity. It's that simple."[/bold cyan]

Puck paused.

[bold cyan]"Well, almost that simple. Let's find out."[/bold cyan]

[bold white]What is electricity, really?[/bold white]
""",
    "circuits_and_batteries": """
Puck set a small battery on the table next to a light bulb
and a coil of copper wire.

[bold cyan]"Here's the challenge,"[/bold cyan] Puck said.
[bold cyan]"Make the bulb light up. You have everything you need."[/bold cyan]

Nell stared at the pieces.

[bold cyan]"Electricity is like water in a pipe,"[/bold cyan] Puck explained.
[bold cyan]"It needs a complete path — a loop — to flow.
If there's a gap anywhere, it stops.
A battery pushes the electrons. The wire carries them.
The bulb uses them. And around they go."[/bold cyan]

[bold white]Can you build a circuit?[/bold white]
""",
    "conductors_and_insulators": """
Puck laid out a collection of objects on the workbench:
a copper coin, a rubber band, a steel spoon, a wooden stick,
a glass marble, and a strip of aluminum foil.

[bold cyan]"Some of these will let electricity pass right through,"[/bold cyan]
Puck said. [bold cyan]"And some will block it completely.
The ones that let it through? Conductors.
The ones that block it? Insulators."[/bold cyan]

Puck picked up the rubber band.

[bold cyan]"This one is why you don't get shocked
every time you touch a power cord.
The plastic on the outside? Insulator.
The copper on the inside? Conductor.
They work together."[/bold cyan]

[bold white]Which materials let electricity through?[/bold white]
""",
    "magnets_and_electromagnets": """
Puck held two small magnets and pushed them toward each other.
They snapped together with a click.

Then Puck flipped one around and tried again.
This time they pushed apart, as if an invisible hand
were holding them away from each other.

[bold cyan]"Magnets,"[/bold cyan] Puck said, eyes sparkling.
[bold cyan]"They can pull. They can push.
And here's the really wild part —
[italic]electricity and magnetism are the same force.[/italic]"[/bold cyan]

[bold cyan]"Run electricity through a wire
and you get a magnet.
Spin a magnet near a wire
and you get electricity.
They're two sides of the same coin."[/bold cyan]

[bold white]How are magnets and electricity connected?[/bold white]
""",
    "electricity_in_daily_life": """
Puck flicked an invisible switch and the whole room lit up.

[bold cyan]"Every light in your house. Every screen you look at.
Every fridge keeping your food cold.
Every hospital keeping people alive.
All of it — electricity."[/bold cyan]

Puck looked out the window at the power lines
stretching toward the horizon.

[bold cyan]"But where does it come from?
How does it travel all the way to your house?
And how do we make sure it's safe —
for you AND for the planet?"[/bold cyan]

[bold cyan]"This is the most important zone.
Because electricity isn't just science.
It's the thing that powers your whole world."[/bold cyan]

[bold white]How does electricity power your daily life?[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "what_is_electricity": """
[bold green]The Spark Chamber crackles with understanding![/bold green]

Nell held up her hand. She knew now that inside every atom,
tiny electrons were spinning. She knew that when they jumped
from one thing to another, that was static electricity.
And when they flowed through a wire, that was current.

[bold cyan]"You've learned the first secret,"[/bold cyan] Puck said.
[bold cyan]"Electricity isn't magic. It's electrons moving.
And now you know what makes them move."[/bold cyan]

[bold white]Next stop: circuits and batteries![/bold white]
""",
    "circuits_and_batteries": """
[bold green]The Circuit Workshop hums with power![/bold green]

The light bulb on the table glowed bright and steady.
Nell had connected everything perfectly —
battery to wire to bulb and back again. A complete loop.

[bold cyan]"Open, closed. Series, parallel,"[/bold cyan] Puck said proudly.
[bold cyan]"You understand how electricity travels now.
You know why a switch works, why a burned-out bulb
can kill a whole string of lights,
and why your house doesn't go dark
when one lamp turns off."[/bold cyan]

[bold white]Now let's find out what electricity can flow through![/bold white]
""",
    "conductors_and_insulators": """
[bold green]The Material Lab glows with knowledge![/bold green]

Nell picked up a power cord and looked at it differently now.
Copper inside — conductor. Plastic outside — insulator.
Working together to keep electricity safe and useful.

[bold cyan]"You can look at any material now,"[/bold cyan] Puck said,
[bold cyan]"and know whether electricity will flow through it or not.
Metal? Conductor. Rubber? Insulator.
That knowledge keeps you safe."[/bold cyan]

[bold white]Time to discover the secret link between magnets and electricity![/bold white]
""",
    "magnets_and_electromagnets": """
[bold green]The Magnet Workshop buzzes with invisible force![/bold green]

Nell held the electromagnet she'd imagined building —
wire wrapped around an iron nail, connected to a battery.
Magnetic when on. Not magnetic when off.

[bold cyan]"Motors, generators, compasses, MRI machines,"[/bold cyan]
Puck listed, counting on tiny fingers.
[bold cyan]"All of them work because of what you just learned:
electricity makes magnets, and magnets make electricity.
That one idea powers the entire modern world."[/bold cyan]

[bold white]One more zone — electricity in your daily life![/bold white]
""",
    "electricity_in_daily_life": """
[bold green]The Power Grid lights up from coast to coast![/bold green]

Nell looked out the window at the power lines and understood.
Power plants spinning generators. Wires carrying current
across hundreds of miles. Transformers stepping it down.
Solar panels catching sunlight. Wind turbines spinning.

[bold cyan]"You know where electricity comes from now,"[/bold cyan] Puck said quietly.
[bold cyan]"You know how it gets to your home.
You know how to stay safe around it.
And you know why renewable energy matters
for the future of this planet."[/bold cyan]

A long, satisfied pause.

[bold cyan]"The Spark Lab is yours.
You understand one of the most powerful forces in the universe.
And that understanding? Nobody can ever take it away."[/bold cyan]

[bold white]The Spark Lab is complete. The power is yours.[/bold white]
""",
}

BOSS_INTROS = {
    "what_is_electricity": "A tiny storm cloud forms above the workbench, crackling with miniature lightning. [bold yellow]\"This is the final spark challenge. Think about a famous experiment with a kite and a key — you know this!\"[/bold yellow]",
    "circuits_and_batteries": "A battery, a bulb, and a single wire sit on the table. [bold yellow]\"Simple materials, big question. What's the absolute minimum you need to make light? Think about what electricity needs to flow!\"[/bold yellow]",
    "conductors_and_insulators": "A small bird lands on a wire high above the lab. [bold yellow]\"Here's a puzzle that stumps most adults. Why doesn't the bird get shocked? Think about what electricity needs to flow through something!\"[/bold yellow]",
    "magnets_and_electromagnets": "A compass needle spins slowly and points north. [bold yellow]\"That needle is a magnet. But what enormous magnet is it pointing toward? Think BIG — really, really big!\"[/bold yellow]",
    "electricity_in_daily_life": "The lights flicker. The screens go dark for a moment. [bold yellow]\"Imagine if all the power stopped. Why do we need to find better, cleaner ways to make electricity? This is the most important question of all.\"[/bold yellow]",
}
