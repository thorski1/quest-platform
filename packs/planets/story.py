"""
story.py — Narrative for the Planets (Solar System Deep Dive) skill pack.

Puck pulls out a telescope and guides the reader deep into every planet —
craters, storms, hidden oceans, diamond rain, and the missions that
carry humanity's curiosity to the farthest reaches of the solar system.

Theme: "The Primer's telescope sees further — every planet has secrets
waiting to be discovered!"
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Telescope[/bold yellow]

Puck appeared carrying something long and gleaming — a brass telescope,
polished so brightly it reflected every star in the Primer's sky.

[bold cyan]"We've seen the solar system before,"[/bold cyan] Puck said, extending
the telescope with a satisfying click. [bold cyan]"We know the names.
We know the order. But names are just the beginning."[/bold cyan]

Puck aimed the telescope at the night sky, and the Primer's page
transformed into a window of deep, velvet black, scattered with
pinpricks of light.

[bold cyan]"Every planet has secrets. Mercury's ancient craters,
Venus's deadly clouds, Mars's frozen rivers, Jupiter's ocean moons,
diamond rain inside Neptune..."[/bold cyan]

Puck lowered the telescope and looked up with bright eyes.

[bold cyan]"The Primer's telescope sees further — every planet has
secrets waiting to be discovered! And now, we go [italic]deep.[/italic]"[/bold cyan]

The girl took the telescope and raised it to her eye.
The first planet swam into focus — small, silver-grey, pocked with
craters older than anything on Earth.

[bold white]Your deep dive into the solar system begins now.[/bold white]
"""

ZONE_INTROS = {
    "mercury_venus": """
Puck aimed the telescope at the two planets closest to the Sun.

[bold cyan]"Mercury and Venus,"[/bold cyan] Puck said. [bold cyan]"The scorched worlds.
Mercury is battered with craters and swings from boiling hot to
freezing cold in a single day. And Venus..."[/bold cyan]

Puck shuddered.

[bold cyan]"Venus looks beautiful from far away — bright and golden.
But up close, it's the most hostile place in the inner solar system.
Crushing pressure, acid clouds, and temperatures that melt lead.
Oh — and it spins the wrong way."[/bold cyan]

[bold white]Let's explore the Sun's closest neighbors![/bold white]
""",
    "earth_moon_deep": """
Puck turned the telescope back toward home — toward Earth.

[bold cyan]"We think we know our own planet,"[/bold cyan] Puck said softly.
[bold cyan]"But have you ever thought about what's beneath your feet?
Thousands of kilometres of rock and liquid metal, a spinning core
of iron hotter than the Sun's surface, giant plates of stone
grinding against each other..."[/bold cyan]

The Primer's page showed Earth sliced open like a fruit,
glowing layers nested inside each other.

[bold cyan]"And then there's the Moon — born in fire, carved by impacts,
the reason we have tides and eclipses."[/bold cyan]

[bold white]Let's look deeper at the world we call home![/bold white]
""",
    "mars_deep": """
Puck swung the telescope to the red dot in the sky.

[bold cyan]"Mars,"[/bold cyan] Puck breathed. [bold cyan]"The Red Planet. It has the
tallest volcano in the solar system, a canyon that could swallow
the United States, and evidence that water once flowed on
its surface. Rivers. Maybe even an ocean."[/bold cyan]

The Primer's page turned rust-red. A six-wheeled rover trundled
across the landscape, cameras scanning.

[bold cyan]"And right now — right this very moment — robots built by humans
are driving across Mars, tasting its soil, listening to its wind,
and flying a tiny helicopter through its thin, thin air."[/bold cyan]

[bold white]Let's drive across the Red Planet![/bold white]
""",
    "jupiter_saturn_deep": """
The telescope needed a wider lens for this one. Puck clicked
a new piece into place and aimed at the gas giants.

[bold cyan]"Jupiter and Saturn,"[/bold cyan] Puck announced. [bold cyan]"The kings of
the solar system. Jupiter is so massive it could swallow all the
other planets and still have room. Its Great Red Spot is a storm
bigger than Earth that has raged for centuries."[/bold cyan]

Swirling bands of orange and cream filled the telescope.

[bold cyan]"And its moons! Europa has a hidden ocean that might — just might —
harbor life. Io has volcanoes erupting into space. And Saturn..."[/bold cyan]

Puck grinned.

[bold cyan]"Saturn has the most magnificent rings in the solar system,
and a moon called Titan where it rains methane."[/bold cyan]

[bold white]Let's explore the gas giants and their incredible moons![/bold white]
""",
    "ice_giants": """
Puck squinted through the telescope at two pale, distant dots.

[bold cyan]"Uranus and Neptune,"[/bold cyan] Puck said. [bold cyan]"The ice giants.
So far from the Sun that light takes hours to reach them.
Most people forget about them — but they shouldn't."[/bold cyan]

The telescope revealed a pale blue-green world tilted on its side
and a deep blue world streaked with the fastest winds in the
solar system.

[bold cyan]"Uranus rolls around the Sun like a ball. Neptune's winds
are faster than the speed of sound. And deep inside both of them..."[/bold cyan]

Puck's eyes went wide.

[bold cyan]"It rains [italic]diamonds.[/italic]"[/bold cyan]

[bold white]Let's venture to the farthest planets![/bold white]
""",
    "dwarf_planets": """
Puck pointed the telescope past Neptune, into the darkness.

[bold cyan]"Out here,"[/bold cyan] Puck whispered, [bold cyan]"beyond the last planet,
there are thousands of small icy worlds drifting in the cold.
The Kuiper Belt. And among them — the dwarf planets."[/bold cyan]

A tiny world with a heart-shaped mark swam into view.

[bold cyan]"Pluto. Ceres. Eris — the troublemaker. Makemake. Haumea,
shaped like an egg because it spins so fast. They're small,
but every one of them has a story."[/bold cyan]

[bold white]Let's meet the small worlds at the edge of the solar system![/bold white]
""",
    "space_missions": """
Puck set down the telescope and picked up something else —
a tiny golden disc, smaller than a coin.

[bold cyan]"Everything we've learned about the planets,"[/bold cyan] Puck said,
[bold cyan]"we learned because humans built machines and sent them out
into the void. Voyager, sailing past Jupiter and Saturn and beyond.
Hubble, orbiting above our atmosphere. James Webb, seeing the
universe in infrared from a million miles away."[/bold cyan]

The Primer's page showed a timeline: rockets launching,
spacecraft flying past planets, telescopes unfolding in space.

[bold cyan]"And now — Artemis, going back to the Moon. And one day,
maybe your day — humans walking on Mars."[/bold cyan]

[bold white]Let's celebrate humanity's greatest voyages![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "mercury_venus": """
[bold green]The scorched worlds glow in the telescope — understood at last![/bold green]

Mercury's craters and Venus's acid clouds, every secret laid bare.

[bold cyan]"Now you know,"[/bold cyan] Puck says, [bold cyan]"why Mercury swings from
boiling to freezing, and why Venus — beautiful Venus — is the most
dangerous planet in the inner solar system."[/bold cyan]

The telescope turns toward a familiar blue marble. Home is next...
""",
    "earth_moon_deep": """
[bold green]The Earth glows — layers, plates, and magnetic shield all revealed![/bold green]

From the crust to the inner core, from tectonic plates to the Moon's
fiery birth — you've gone deeper than most people ever do.

[bold cyan]"You understand your own world now,"[/bold cyan] Puck says proudly.
[bold cyan]"The ground beneath your feet, the shield above your head,
the Moon that lights your night. All of it connected."[/bold cyan]

A red dot beckons in the distance. Mars is waiting...
""",
    "mars_deep": """
[bold green]The Red Planet stands revealed — volcano, canyon, rovers, and all![/bold green]

Olympus Mons. Valles Marineris. Ancient rivers. Curiosity and
Perseverance, driving across an alien world right now.

[bold cyan]"Mars was once a blue world,"[/bold cyan] Puck says quietly.
[bold cyan]"Rivers flowed, lakes filled its craters. And today,
our robots are there, searching for echoes of that lost water —
and maybe, just maybe, signs of ancient life."[/bold cyan]

The telescope widens. The gas giants are calling...
""",
    "jupiter_saturn_deep": """
[bold green]The gas giants blaze with colour — storms, moons, and rings![/bold green]

Jupiter's Great Red Spot, Europa's hidden ocean, Io's volcanoes,
Saturn's glittering rings, Titan's methane rain — all explored.

[bold cyan]"The giants,"[/bold cyan] Puck says with awe, [bold cyan]"are worlds within worlds.
Jupiter alone has more than 90 moons — each one a story.
And Saturn's rings... the most beautiful thing in the solar system."[/bold cyan]

Two pale dots shimmer in the far distance. The ice giants beckon...
""",
    "ice_giants": """
[bold green]The ice giants gleam — tilted, windy, and raining diamonds![/bold green]

Uranus on its side, Neptune's supersonic winds, Triton's geysers,
diamond rain in the crushing depths — the strangest worlds of all.

[bold cyan]"Most people never think about Uranus and Neptune,"[/bold cyan] Puck says.
[bold cyan]"But now you know their secrets — and they're some of the
most extraordinary secrets in the entire solar system."[/bold cyan]

The telescope turns to the darkness beyond. The small worlds are waiting...
""",
    "dwarf_planets": """
[bold green]The small worlds shine — Pluto's heart, Haumea's spin, the vast Kuiper Belt![/bold green]

Pluto, Ceres, Eris, Makemake, Haumea — each one small, each one
full of surprises.

[bold cyan]"They're not planets,"[/bold cyan] Puck says, [bold cyan]"but they're no less
wonderful. Pluto's heart, Haumea's egg shape, Eris the troublemaker —
the edge of the solar system is full of marvels."[/bold cyan]

A golden disc glimmers. It's time to celebrate the missions...
""",
    "space_missions": """
[bold green]Every mission glows — from Voyager's golden record to tomorrow's Mars landing![/bold green]

Voyager sailing into interstellar space. Hubble orbiting above the clouds.
James Webb seeing the invisible. Artemis going back to the Moon.

[bold cyan]"Every single thing we've learned,"[/bold cyan] Puck says, wings spread wide,
[bold cyan]"came because someone asked a question and then built something
extraordinary to find the answer."[/bold cyan]

Puck lowers the telescope and hands it to you.

[bold cyan]"The solar system is yours now. Every planet, every moon,
every mission. You understand it all."[/bold cyan]

[bold white]Stargazer. Astronaut. Astrophysicist. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "mercury_venus": "The telescope focuses on Venus's volcanic landscape. [bold yellow]\"Venus has more volcanoes than any other planet. Scientists have mapped over a thousand! How many major ones have they counted?\"[/bold yellow]",
    "earth_moon_deep": "Puck tilts the Primer's globe and walks it around a glowing lamp. [bold yellow]\"The tilt of the Earth — 23.5 degrees — is the key to something we experience every single year. What does it cause?\"[/bold yellow]",
    "mars_deep": "A tiny helicopter rises above the Martian dust. [bold yellow]\"Flying on Mars is nearly impossible because the air is so thin. Ingenuity solved this — but WHY is it so hard?\"[/bold yellow]",
    "jupiter_saturn_deep": "The Primer shows tiny Earths streaming into Jupiter like marbles. [bold yellow]\"Jupiter is enormous beyond imagining. How many Earths could fit inside the King of Planets?\"[/bold yellow]",
    "ice_giants": "Puck draws wobbly magnetic lines around Uranus and Neptune. [bold yellow]\"These planets break all the rules — even their magnetic fields are strange. What makes them so unusual?\"[/bold yellow]",
    "dwarf_planets": "The telescope pulls back to show a glittering band of ice beyond Neptune. [bold yellow]\"The Kuiper Belt is a vast frontier. What is it most similar to in our inner solar system?\"[/bold yellow]",
    "space_missions": "The Primer shows a red dot growing larger through a spacecraft window. [bold yellow]\"One day, humans will walk on Mars. But first they have to get there. How long would the journey take?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "scorched_worlds_explorer": (
        "Scorched Worlds Explorer",
        "Survived Mercury's extremes and Venus's greenhouse inferno!",
    ),
    "earth_moon_expert": (
        "Earth & Moon Expert",
        "Explored Earth's layers, magnetic shield, and the Moon's fiery origin!",
    ),
    "mars_rover_driver": (
        "Mars Rover Driver",
        "Climbed Olympus Mons, crossed Valles Marineris, and drove the rovers!",
    ),
    "gas_giant_navigator": (
        "Gas Giant Navigator",
        "Explored Jupiter's storms, Europa's ocean, Saturn's rings, and Titan!",
    ),
    "ice_giant_pioneer": (
        "Ice Giant Pioneer",
        "Discovered diamond rain, sideways planets, and supersonic winds!",
    ),
    "dwarf_planet_hunter": (
        "Dwarf Planet Hunter",
        "Met Pluto's heart, Haumea's spin, and the icy Kuiper Belt!",
    ),
    "mission_commander": (
        "Mission Commander",
        "Celebrated every great mission from Voyager to Artemis!",
    ),
}
