"""
story.py — Narrative for the Astronomy (Star Observatory) skill pack.

Puck opens a grand observatory dome and guides the reader through
the night sky — stars, the Moon, galaxies, spacecraft, and the
brave humans who journey into the void.

Theme: "The observatory sees everything — every star has a story,
and every story leads to another!"
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Star Observatory[/bold yellow]

Puck pushed open a heavy door at the top of a spiral staircase,
and the Primer's page became a round stone room with a domed
ceiling. In the centre stood a magnificent brass telescope, bigger
than any the girl had ever seen.

[bold cyan]"Welcome to the Observatory,"[/bold cyan] Puck said, pulling a lever.
The dome rumbled and split open, revealing a sky so full of stars
it took her breath away.

[bold cyan]"We've looked at planets before. But tonight we go further —
much, much further. Stars that burn a thousand times brighter
than our Sun. The Moon and its secrets. Galaxies spinning
millions of light-years away. Spacecraft sailing into the
unknown."[/bold cyan]

Puck climbed onto the telescope's viewing platform and beckoned.

[bold cyan]"And the bravest part of all — the humans who strap into
rockets and leave everything they know behind, just to see
what's out there."[/bold cyan]

The girl stepped up to the eyepiece. The first constellation
swam into focus — Orion, belt and all, standing guard over
the winter sky.

[bold white]Your journey through the cosmos begins now.[/bold white]
"""

ZONE_INTROS = {
    "stars_constellations": """
Puck aimed the great telescope at a dazzling cluster of stars.

[bold cyan]"Stars,"[/bold cyan] Puck said softly. [bold cyan]"Every one of them is a sun —
some smaller than ours, some so enormous they could swallow
a million Earths. They're born inside clouds of gas, they burn
for millions or billions of years, and when they die..."[/bold cyan]

Puck's eyes went wide.

[bold cyan]"Some of them explode so brightly they outshine entire galaxies.
And the patterns they make — the constellations — have guided
sailors, inspired myths, and filled people with wonder since
the very first humans looked up."[/bold cyan]

[bold white]Let's explore the stars and the patterns they paint across the sky![/bold white]
""",
    "the_moon": """
Puck swung the telescope down toward the brightest object in
the night sky — the Moon.

[bold cyan]"Our closest companion,"[/bold cyan] Puck said. [bold cyan]"It controls our tides,
gives us eclipses, and changes shape every single night —
or so it seems."[/bold cyan]

The telescope revealed craters and plains in sharp detail,
the grey surface glowing silver in the earthshine.

[bold cyan]"People have been fascinated by the Moon for as long as
there have been people. And in 1969, we actually went there
and walked on it. But there's still so much to discover."[/bold cyan]

[bold white]Let's uncover the Moon's secrets![/bold white]
""",
    "galaxies_universe": """
Puck pulled the telescope back — way back — until the stars
blurred into a soft, glowing river of light.

[bold cyan]"That,"[/bold cyan] Puck whispered, [bold cyan]"is our galaxy. The Milky Way.
A hundred billion stars, spinning together in a great spiral.
And it's just one galaxy among trillions."[/bold cyan]

The Primer's page expanded outward, showing galaxy after galaxy —
spirals, blobs, and strange irregular shapes, stretching into
every direction.

[bold cyan]"The universe is so big that light itself takes billions of
years to cross it. Every time we look at a distant galaxy,
we're looking back in time."[/bold cyan]

[bold white]Let's journey beyond our galaxy and into the universe![/bold white]
""",
    "space_exploration": """
Puck set down the telescope and picked up a model rocket,
its tiny engines painted silver.

[bold cyan]"Everything we know about the stars, the Moon, the galaxies —
we learned because humans built incredible machines and sent
them out to look."[/bold cyan]

The Primer's page filled with spacecraft: the Hubble floating
above Earth, James Webb unfolding its golden mirror, rovers
trundling across Mars, Voyager sailing into the darkness.

[bold cyan]"Space stations, telescopes, rovers, probes — each one a
message from humanity saying: we want to understand."[/bold cyan]

[bold white]Let's explore the spacecraft that explore for us![/bold white]
""",
    "astronauts_space_life": """
Puck pulled on an imaginary helmet and gave a thumbs-up.

[bold cyan]"The machines are extraordinary,"[/bold cyan] Puck said. [bold cyan]"But the bravest
thing of all is sending people. Real humans — eating, sleeping,
exercising, working — in the emptiness of space."[/bold cyan]

The Primer showed the interior of the space station: sleeping
bags strapped to walls, floating water droplets, astronauts
jogging on treadmills in zero gravity.

[bold cyan]"Becoming an astronaut is one of the hardest things a person
can do. And living in space changes everything — how you eat,
how you sleep, even how your bones work."[/bold cyan]

[bold white]Let's find out what it's really like to live among the stars![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "stars_constellations": """
[bold green]The stars blaze in the observatory dome — every type and pattern revealed![/bold green]

Red giants, blue supergiants, nebulae, supernovae, the Big Dipper,
Orion, and the steadfast North Star — all explored and understood.

[bold cyan]"Now you know what stars really are,"[/bold cyan] Puck says, beaming.
[bold cyan]"Not just twinkling lights — they're nuclear furnaces, cosmic
factories that forge the very atoms inside your body."[/bold cyan]

The telescope tilts downward. A familiar silver face rises over the horizon...
""",
    "the_moon": """
[bold green]The Moon glows in the eyepiece — phases, eclipses, tides, and craters all understood![/bold green]

From new moon to full moon, from solar eclipses to blood moons,
from the pull of tides to the far side no one sees — every
secret of our closest neighbour laid bare.

[bold cyan]"The Moon has been with us since the beginning,"[/bold cyan] Puck says.
[bold cyan]"And now you understand it like an astronomer."[/bold cyan]

The telescope pulls back. The stars blur into a river of light — a galaxy awaits...
""",
    "galaxies_universe": """
[bold green]Galaxies spin across the observatory dome — spirals, ellipticals, and the vast cosmos![/bold green]

The Milky Way, Andromeda on its collision course, light-years
stretching beyond imagination, and the Big Bang that started
it all.

[bold cyan]"The universe is 13.8 billion years old,"[/bold cyan] Puck says quietly,
[bold cyan]"and it's still expanding. Every time you look at the night sky,
you're looking back in time. You're a time traveller."[/bold cyan]

A model rocket gleams on the observatory desk. It's time to explore how we explore...
""",
    "space_exploration": """
[bold green]Every great mission glows on the observatory wall — from Apollo to James Webb![/bold green]

The ISS circling Earth, Hubble's stunning images, James Webb
peering into the infrared, Perseverance collecting Martian rocks,
Voyager sailing into interstellar space, and Artemis pointing
back to the Moon.

[bold cyan]"Every one of these missions,"[/bold cyan] Puck says, [bold cyan]"started with
someone asking a question and then building something
extraordinary to find the answer."[/bold cyan]

A spacesuit hangs on a rack nearby. One final frontier awaits...
""",
    "astronauts_space_life": """
[bold green]The astronaut's world is revealed — training, eating, sleeping, and walking in the void![/bold green]

From the gruelling application process to sleeping bags on walls,
from recycled water to seven hours of underwater training for
every hour of spacewalk — the life of an astronaut, understood.

[bold cyan]"You've seen everything,"[/bold cyan] Puck says, wings spread wide.
[bold cyan]"The stars, the Moon, the galaxies, the spacecraft, and the
people brave enough to ride them into the unknown."[/bold cyan]

Puck closes the observatory dome gently.

[bold cyan]"The universe is yours now. Every star, every galaxy,
every mission, every dream of exploration. All of it."[/bold cyan]

[bold white]Stargazer. Astronomer. Explorer. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "stars_constellations": "Puck points straight up at a star that never moves. [bold yellow]\"One star in the sky holds perfectly still while all the others spin around it. Sailors have used it for centuries. What is its name?\"[/bold yellow]",
    "the_moon": "Puck stretches a measuring tape toward the sky. [bold yellow]\"The Moon is our closest neighbour in space — but it's still incredibly far. How far away is it?\"[/bold yellow]",
    "galaxies_universe": "The observatory fills with light from every direction. [bold yellow]\"Everything — every star, every atom — began in one incredible moment 13.8 billion years ago. What is this event called?\"[/bold yellow]",
    "space_exploration": "Puck gazes at a red dot on the horizon. [bold yellow]\"All the great space agencies are working toward one goal — sending humans to another planet. Which planet is next?\"[/bold yellow]",
    "astronauts_space_life": "Puck cannonballs into an imaginary pool. [bold yellow]\"Astronauts train for spacewalks in a very surprising place. How does being underwater help them prepare?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "constellation_mapper": (
        "Constellation Mapper",
        "Charted the stars — from red giants to supernovae to the North Star!",
    ),
    "lunar_scholar": (
        "Lunar Scholar",
        "Mastered the Moon — phases, eclipses, tides, and craters!",
    ),
    "galaxy_voyager": (
        "Galaxy Voyager",
        "Journeyed through the Milky Way, Andromeda, and the Big Bang!",
    ),
    "mission_specialist": (
        "Mission Specialist",
        "Explored every great mission from Hubble to James Webb to Artemis!",
    ),
    "space_cadet": (
        "Space Cadet",
        "Learned what it takes to live and work in the void of space!",
    ),
}
