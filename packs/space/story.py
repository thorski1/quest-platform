"""
story.py — Narrative for the Space skill pack.

Puck opens the Primer's newest chapter: a glowing star map that
shows the whole Universe — or at least the part we've explored.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Book of Stars[/bold yellow]

The page the Primer opened to was different from all the others.

It was dark. Completely, beautifully dark — and then, one by one,
tiny lights began to appear across it. Stars. Hundreds of them.
Then thousands.

Puck floated down through the stars, wings trailing silver light.

[bold cyan]"Oh,"[/bold cyan] Puck breathed, looking around. [bold cyan]"Oh, this is my favourite chapter."[/bold cyan]

The girl looked up. The entire ceiling had become a night sky.

[bold white]"What is this place?"[/bold white]

[bold cyan]"The Universe,"[/bold cyan] Puck said simply. [bold cyan]"Or at least — the little corner
of it we call home. One star. Eight planets. One moon of our very
own. And billions of other stars, each one a sun, some with their
own planets going around them."[/bold cyan]

A glowing map appeared — the Solar System, each planet in its orbit,
the Sun blazing at the centre.

[bold cyan]"The Ancient Greeks watched these same stars. So did
the sailors who crossed the oceans, the farmers who planted
their fields by the seasons, the explorers who used the night sky
as their map."[/bold cyan]

Puck settled on the girl's shoulder, looking up with her.

[bold cyan]"And now you. Ready to learn the sky?"[/bold cyan]

[bold white]Your journey through the stars begins now.[/bold white]
"""

ZONE_INTROS = {
    "our_solar_system": """
Puck pointed to the glowing map of the Solar System.

[bold cyan]"Here we are,"[/bold cyan] Puck said, [bold cyan]"one pale blue dot orbiting one
average yellow star, in one ordinary galaxy.
But our Solar System is anything but ordinary — once you know it."[/bold cyan]

Eight planets glowed on the map, from tiny Mercury to distant Neptune.

[bold cyan]"Eight worlds. Each one completely different.
Some are rock and dust. Some are storms of gas.
One has rings of ice. One has life."[/bold cyan]

Puck grinned. [bold cyan]"Ours."[/bold cyan]

[bold white]Let's meet all eight planets![/bold white]
""",
    "the_sun_and_stars": """
The map zoomed out. Suddenly, the Solar System was just one tiny
dot among millions.

[bold cyan]"Everything you've ever known,"[/bold cyan] Puck said softly,
[bold cyan]"is in that tiny dot.
All those other dots? Each one is a sun. Some bigger than ours.
Some smaller. All of them burning, just like our star burns."[/bold cyan]

The Primer's ceiling blazed with starlight.

[bold cyan]"And those ancient patterns — the ones people have told stories
about for thousands of years? Those are constellations.
Star-pictures. Dot-to-dot pictures written across the entire sky."[/bold cyan]

[bold white]Let's learn about stars — including the one that warms our faces![/bold white]
""",
    "the_moon": """
A large silver circle rose above the star-map.

[bold cyan]"Our moon,"[/bold cyan] Puck said, voice quiet. [bold cyan]"The only place
beyond Earth that human beings have ever walked.
Think about that — a world you can see with your own eyes
every night, and twelve people have stood on it."[/bold cyan]

The Moon's face was full of craters, mountains, and dark plains.

[bold cyan]"It changes shape — or seems to.
It pulls our oceans up into tides.
It has no air, no wind, no weather.
And yet it's the most familiar object in the night sky."[/bold cyan]

[bold white]Let's explore our nearest neighbour in space![/bold white]
""",
    "planets_up_close": """
Puck flew from planet to planet on the glowing map.

[bold cyan]"Every planet has a personality,"[/bold cyan] Puck said.
[bold cyan]"Mars is red and rusty. Venus is unbearably hot.
Saturn has rings of ice that would stretch almost to Earth.
Jupiter has a storm three times bigger than our whole planet
that's been raging for 400 years."[/bold cyan]

Each planet glowed as Puck named it.

[bold cyan]"Once you know these worlds — really know them —
you'll never look at the night sky the same way again."[/bold cyan]

[bold white]Let's explore what makes each planet extraordinary![/bold white]
""",
    "space_exploration": """
Puck held up a tiny silver rocket, no bigger than a finger.

[bold cyan]"Sixty years ago,"[/bold cyan] Puck said, [bold cyan]"no human being had ever
left the ground and entered space. Not once, in all of history."[/bold cyan]

The first satellite appeared on the map. Then the first astronaut.
Then the Moon landing. Then the Space Station.

[bold cyan]"Now there are people living in space right now —
floating in a metal room, orbiting Earth every 90 minutes.
Robots are driving across the surface of Mars.
We have pictures from the edges of the Solar System."[/bold cyan]

The little rocket glowed.

[bold cyan]"The greatest adventure humans have ever gone on
is still just beginning."[/bold cyan]

[bold white]Let's explore the story of space exploration![/bold white]
""",
    "day_night_seasons": """
The Primer showed Earth from space — a blue and green marble,
slowly spinning in the darkness.

[bold cyan]"There,"[/bold cyan] Puck said, pointing to the lit half.
[bold cyan]"Day. And there — night. And as the Earth turns,
they swap. Every 24 hours, without fail, the whole world
turns through light and dark."[/bold cyan]

Then the map tilted, showing Earth's angled axis.

[bold cyan]"And that little tilt — just 23.5 degrees —
is the reason we have summer and winter.
The reason some days are long and some are short.
The reason the North Pole is lit all day in June
and dark all day in December."[/bold cyan]

[bold white]Let's discover why the sky changes and why seasons happen![/bold white]
""",
    "comets_and_asteroids": """
The map of the Solar System filled with new objects — tiny dots
and streaks and strange shapes, between and beyond the planets.

[bold cyan]"The planets,"[/bold cyan] Puck said, [bold cyan]"are not the whole story."[/bold cyan]

A comet appeared, trailing a glowing white tail.

[bold cyan]"There are billions of smaller things out there —
rocky asteroids, icy comets, dwarf planets, shooting stars.
The Solar System is full of wanderers."[/bold cyan]

A meteor streaked across the Primer's sky.

[bold cyan]"And some of them visit us.
Every shooting star you've ever wished upon
was a piece of space rock burning up in our sky."[/bold cyan]

[bold white]Let's meet the wanderers of the Solar System![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "our_solar_system": """
[bold green]All eight planets glow on the map![/bold green]

Mercury. Venus. Earth. Mars. Jupiter. Saturn. Uranus. Neptune.

[bold cyan]"You know every world in our Solar System,"[/bold cyan] Puck says.
[bold cyan]"You know which ones are small and rocky,
which ones are giants of gas. You know the order
from the Sun to the very edge of the system."[/bold cyan]

The star map zooms out. The rest of the galaxy waits...
""",
    "the_sun_and_stars": """
[bold green]A thousand stars glow across the Primer's sky![/bold green]

Constellations take shape — Orion, the Great Bear, the Southern Cross.

[bold cyan]"Stars,"[/bold cyan] Puck says quietly, [bold cyan]"are not decoration.
They are other suns, some with their own planets,
all of them burning millions of kilometres away.
And now you understand what you're looking at
every time you look up at a clear night sky."[/bold cyan]

The Moon rises over the star-map. Time to explore it...
""",
    "the_moon": """
[bold green]The Moon shines full and bright on the map![/bold green]

Craters and seas. Phases and tides. And twelve pairs of human footprints.

[bold cyan]"The Moon,"[/bold cyan] Puck says, [bold cyan]"is the most visited world
beyond our own. And now you know it well —
its phases, its tides, its craters, and the story
of the brave people who walked across it."[/bold cyan]

The planets of the Solar System beckon. Up close, this time...
""",
    "planets_up_close": """
[bold green]Every planet shines with its own colour and character![/bold green]

Red Mars. Ringed Saturn. Stormy Jupiter. Blue Neptune.

[bold cyan]"You know these worlds,"[/bold cyan] Puck says.
[bold cyan]"Not just their names — their personalities.
Their storms and rings and rust and heat.
You could find them in the sky and know exactly
what kind of world you're looking at."[/bold cyan]

The history of exploration begins now...
""",
    "space_exploration": """
[bold green]The Solar System is mapped with human missions![/bold green]

From Sputnik to the ISS. From Yuri Gagarin to Mars rovers.

[bold cyan]"People built rockets and trusted them with their lives,"[/bold cyan] Puck says.
[bold cyan]"They flew to the Moon with computers less powerful
than your phone. They built a floating station
and have lived there continuously since the year 2000."[/bold cyan]

Puck pauses. [bold cyan]"And they're still going."[/bold cyan]

The reason the sky changes glows with invitation...
""",
    "day_night_seasons": """
[bold green]Earth spins and the seasons turn on the map![/bold green]

Summer and winter. Day and night. The Midnight Sun.

[bold cyan]"You understand now,"[/bold cyan] Puck says,
[bold cyan]"why the Sun rises in the east every morning.
Why December is cold and June is warm.
Why the day is long in summer and short in winter.
It's not magic — it's geometry. The angle of light. A tilt of 23.5 degrees."[/bold cyan]

The wanderers of the outer Solar System drift into view...
""",
    "comets_and_asteroids": """
[bold green]The whole Solar System blazes with wandering light![/bold green]

Comets with glowing tails. Rocky asteroids. Shooting stars.
Pluto, the dwarf planet. Halley's Comet, returning every 76 years.

[bold cyan]"You've done it,"[/bold cyan] Puck says, wings spread wide.
[bold cyan]"Eight planets. The Sun and stars. The Moon.
Space exploration. Day, night, and seasons.
And now the wanderers — the comets and asteroids
that remind us the Solar System is still wild and alive."[/bold cyan]

[bold white]Stargazer. Space Explorer. World-Knower. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "our_solar_system": "The map zooms in on the farthest planet. [bold yellow]\"Cold. Dark. Blue. So far away that sunlight reaching it is 900 times dimmer than here. It takes 165 years to orbit the Sun. Which planet is it?\"[/bold yellow]",
    "the_sun_and_stars": "A star glows brilliant blue-white in the Primer's sky. [bold yellow]\"This is Sirius — the brightest star in our night sky. But is it bigger and hotter than our Sun, or smaller and cooler?\"[/bold yellow]",
    "the_moon": "The Moon on the map is dark — no sunlit side visible. [bold yellow]\"What phase is this — when the Moon is between Earth and the Sun, and we can't see the lit side at all?\"[/bold yellow]",
    "planets_up_close": "A giant red spot swirls on the map of Jupiter. [bold yellow]\"Jupiter's Great Red Spot is a storm that's been going for at least 400 years. It's bigger than our entire planet. What kind of planet is Jupiter — rocky or gas?\"[/bold yellow]",
    "space_exploration": "A tiny glowing dot appears at the very edge of the map. [bold yellow]\"Voyager 1 was launched in 1977 and is now the furthest human-made object from Earth — over 23 billion kilometres away. What kind of spacecraft is it?\"[/bold yellow]",
    "day_night_seasons": "The map shows the Northern Hemisphere tilted directly toward the Sun. [bold yellow]\"At the summer solstice, some places near the Arctic Circle have sunlight all day and night. What do we call this amazing phenomenon?\"[/bold yellow]",
    "comets_and_asteroids": "A comet blazes across the star map, tail streaming behind it. [bold yellow]\"Halley's Comet last passed Earth in 1986. When will it return? And in which direction does its tail point — behind it, or away from the Sun?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "solar_system_scholar": (
        "Solar System Scholar",
        "Named and described all eight planets of the Solar System!",
    ),
    "stargazer": (
        "Stargazer",
        "Learned about stars, constellations, and what they really are!",
    ),
    "moon_watcher": (
        "Moon Watcher",
        "Explored the Moon's phases, tides, and human landings!",
    ),
    "planet_expert": (
        "Planet Expert",
        "Discovered what makes every planet unique and extraordinary!",
    ),
    "mission_controller": (
        "Mission Controller",
        "Followed the history of space exploration from Gagarin to Mars rovers!",
    ),
    "sky_reader": (
        "Sky Reader",
        "Understood why day, night, and seasons happen!",
    ),
    "comet_chaser": (
        "Comet Chaser",
        "Tracked comets, asteroids, meteors, and the wanderers of the Solar System!",
    ),
}
