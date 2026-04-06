"""
story.py — Narrative for the Maps & Navigation skill pack.

Puck opens the Primer's Map Room and guides the reader through the
art and science of maps — from reading a legend to navigating by
satellite, from ancient clay tablets to augmented reality.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Map Room[/bold yellow]

The Primer's pages rustled and turned on their own, settling on a door
the girl had never seen before — a heavy oak door with a brass compass
rose set into its surface, its four points gleaming.

[bold cyan]"Ah,"[/bold cyan] said Puck, landing on the door's iron handle.
[bold cyan]"The Map Room. I was wondering when you'd find this."[/bold cyan]

The girl pushed the door open. Inside was a round chamber with
walls made entirely of maps — old maps drawn on yellowed parchment,
bright digital maps that pulsed with light, maps of cities and oceans
and even maps of the Moon. In the center of the room stood a great
globe, slowly spinning, with tiny golden lines of latitude and
longitude crisscrossing its surface.

[bold white]"Every line leads somewhere?"[/bold white] the girl asked.

[bold cyan]"Every line leads to adventure,"[/bold cyan] Puck said, flying to the top
of the globe and sitting cross-legged on the North Pole.
[bold cyan]"A map is a promise: follow me, and I'll show you the way.
Learn to read maps, and you'll never truly be lost —
not in a forest, not in a city, not even on another planet."[/bold cyan]

The compass rose on the door began to glow. North, South, East, West —
each point lit up in turn.

[bold cyan]"Ready to learn the language of maps?"[/bold cyan]

[bold white]The Map Room is open. Your navigation begins now.[/bold white]
"""

ZONE_INTROS = {
    "reading_maps": """
Puck flew to the nearest wall and tapped a simple map — a drawing
of a town with little symbols for houses, trees, and a winding river.

[bold cyan]"Before you can use any map,"[/bold cyan] Puck said,
[bold cyan]"you need to learn how to read one. What do the symbols mean?
What's that little box in the corner? Why is everything so tiny?
A map has its own language — and once you speak it,
every map in the world makes sense."[/bold cyan]

The town map glowed softly, its symbols waiting to be understood.

[bold white]Let's learn to read our first map![/bold white]
""",
    "compass_directions": """
Puck flew to a large brass compass mounted on the wall.
Its needle swung gently and settled, pointing North.

[bold cyan]"North, South, East, West,"[/bold cyan] Puck said, touching each point.
[bold cyan]"These four directions are the foundation of all navigation.
Every map uses them. Every compass shows them. Every explorer
who ever lived learned them first."[/bold cyan]

The compass needle glowed gold.

[bold cyan]"The sun rises in the East and sets in the West.
The stars wheel around the North. Once you know the directions,
the whole world has a shape."[/bold cyan]

[bold white]Let's master the compass![/bold white]
""",
    "types_of_maps": """
Puck gestured at the walls of the Map Room, where dozens of
different maps hung side by side — some showing roads, some showing
weather, one that looked like a pirate's treasure map.

[bold cyan]"There isn't just one kind of map,"[/bold cyan] Puck explained.
[bold cyan]"There are road maps and weather maps, treasure maps and
topographic maps, satellite images taken from space.
Each one shows the world in a different way —
because each one has a different job to do."[/bold cyan]

The maps rustled as if eager to be explored.

[bold white]Let's discover all the different kinds of maps![/bold white]
""",
    "coordinates": """
Puck flew to the great spinning globe in the center of the room
and traced the golden lines with one finger.

[bold cyan]"See these lines?"[/bold cyan] Puck said. [bold cyan]"Latitude and longitude.
They wrap around the whole Earth like an invisible net.
And with just two numbers — one for the sideways line,
one for the up-and-down line — you can find any place
on the entire planet."[/bold cyan]

The globe's lines pulsed with light.

[bold cyan]"It's like giving every spot on Earth its own secret address."[/bold cyan]

[bold white]Let's learn the lines on the globe![/bold white]
""",
    "map_skills": """
Puck unrolled a large map across the floor of the Map Room
and placed a tiny compass, a ruler, and a magnifying glass beside it.

[bold cyan]"Reading a map is one thing,"[/bold cyan] Puck said.
[bold cyan]"Using one is something else entirely. Following directions.
Planning a route. Measuring how far it really is.
These are the skills that turn a reader into a navigator."[/bold cyan]

A dotted line appeared on the map, tracing a path
from a little house to a mountain peak.

[bold cyan]"Shall we follow the path?"[/bold cyan]

[bold white]Let's learn the navigator's toolkit![/bold white]
""",
    "famous_maps": """
Puck flew to the oldest corner of the Map Room, where ancient
maps hung behind glass — cracked clay tablets, hand-drawn parchments
with sea monsters at the edges, and glowing maps of the Moon and Mars.

[bold cyan]"People have been making maps for thousands of years,"[/bold cyan]
Puck said reverently. [bold cyan]"The Babylonians carved them in clay.
Explorers drew them on ships. Astronauts mapped the Moon.
And now, robots are mapping Mars."[/bold cyan]

An ancient clay tablet glowed next to a shimmering map of Mars.

[bold cyan]"Every map tells a story about the people who made it."[/bold cyan]

[bold white]Let's travel through the history of maps![/bold white]
""",
    "digital_maps": """
Puck flew to the newest wall of the Map Room — a wall that
wasn't made of stone at all, but of light. Digital maps scrolled
and zoomed across its surface, satellites blinked overhead,
and a tiny blue dot pulsed, showing exactly where they were.

[bold cyan]"The future of maps,"[/bold cyan] Puck said, eyes wide.
[bold cyan]"GPS satellites that know where you are anywhere on Earth.
Digital maps that update in real time. Navigation apps that talk to you.
And one day — maps that float in the air around you."[/bold cyan]

The blue dot pulsed warmly.

[bold cyan]"The Map Room's final chapter. Are you ready?"[/bold cyan]

[bold white]Let's explore the maps of tomorrow![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "reading_maps": """
[bold green]The first map glows — every symbol understood![/bold green]

The town map on the wall shines warmly. Its legend, its symbols,
its scale bar, its title — all of them clear as day.

[bold cyan]"You can read a map!"[/bold cyan] Puck says proudly.
[bold cyan]"That's the first skill every navigator needs.
Now you'll never look at a map and feel lost."[/bold cyan]

The brass compass on the wall begins to spin. The directions are calling...
""",
    "compass_directions": """
[bold green]The compass glows — all four directions mastered![/bold green]

North, South, East, West — and every direction in between.
The brass compass shines with a golden light.

[bold cyan]"You know the directions,"[/bold cyan] Puck says with a grin.
[bold cyan]"The sun rises in the East, sets in the West, and
the compass needle always finds North. You're oriented!"[/bold cyan]

Different maps begin to glow on the walls. Each one is a different kind...
""",
    "types_of_maps": """
[bold green]Every kind of map glows on the wall![/bold green]

Road maps, weather maps, treasure maps, topographic maps,
satellite images — each one understood, each one useful.

[bold cyan]"You know that there's a map for everything,"[/bold cyan] Puck says.
[bold cyan]"Need to plan a drive? Road map. Check the forecast? Weather map.
See the shape of mountains? Topographic map. There's always a map
for the job."[/bold cyan]

Golden lines begin to shimmer on the great globe. Coordinates are next...
""",
    "coordinates": """
[bold green]The globe's lines blaze with golden light![/bold green]

Latitude and longitude, the Equator and the Prime Meridian,
hemispheres and grid references — all of them yours.

[bold cyan]"Every place on Earth has an address now,"[/bold cyan] Puck says.
[bold cyan]"Two numbers — latitude and longitude — and you can find
any spot on the entire planet. Even the middle of the ocean."[/bold cyan]

A ruler, compass, and magnifying glass appear. It's time to use these skills...
""",
    "map_skills": """
[bold green]The navigator's tools glow with mastery![/bold green]

Routes planned, distances measured, landmarks spotted,
maps oriented to match the real world.

[bold cyan]"You're not just reading maps now,"[/bold cyan] Puck says warmly.
[bold cyan]"You're using them. Following directions, planning journeys,
measuring distances. You're a true navigator."[/bold cyan]

Ancient maps begin to glow in the oldest corner of the room. History awaits...
""",
    "famous_maps": """
[bold green]Maps from every age glow across the wall![/bold green]

Ancient clay tablets, exploration charts, Moon maps, Mars maps,
and sonar images of the ocean floor — the whole history of cartography.

[bold cyan]"Four thousand years of map-making,"[/bold cyan] Puck says quietly.
[bold cyan]"From scratches in clay to photographs from space.
And every single one was made by someone who wanted to understand
the world a little better."[/bold cyan]

The digital wall begins to pulse with light. The future of maps is next...
""",
    "digital_maps": """
[bold green]The digital wall blazes with light![/bold green]

GPS satellites, digital maps, navigation apps, augmented reality —
the future of maps, understood and explored.

[bold cyan]"You've done it,"[/bold cyan] Puck says, spreading wings wide.
[bold cyan]"From the very first map to the maps of tomorrow.
From compass roses to GPS satellites. From reading symbols
to navigating the whole world."[/bold cyan]

Puck flies to the top of the spinning globe and looks down.

[bold cyan]"The Map Room is yours now — every wall, every map,
every line and symbol. Wherever you go in life,
you'll always know the way."[/bold cyan]

[bold white]Navigator. Cartographer. Map Master. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "reading_maps": "Puck taps the top of the map where words are written in fine script. [bold yellow]\"Every map has a name — a title that tells you what it shows. What does a map's title tell you?\"[/bold yellow]",
    "compass_directions": "Puck stands facing the wall and slowly turns around. [bold yellow]\"If North is straight ahead of you, what direction is directly behind you? Think about opposites!\"[/bold yellow]",
    "types_of_maps": "Puck zooms the map view out further and further until the whole planet is visible — a photograph from space. [bold yellow]\"This isn't a drawing — it's a real picture taken from high above. What kind of map is this?\"[/bold yellow]",
    "coordinates": "Puck taps the globe and two glowing numbers appear beside every spot. [bold yellow]\"Latitude and longitude give every place on Earth a unique address. But why are they so useful? Think about who might need to find an exact spot — pilots, sailors, rescue teams...\"[/bold yellow]",
    "map_skills": "Puck holds up a paper map and a compass in the field. [bold yellow]\"You've got a real map and the real world around you. What's the very first thing a navigator does to make the map useful?\"[/bold yellow]",
    "famous_maps": "Puck dives below the surface of a painted ocean on the wall. Sound waves pulse downward. [bold yellow]\"We've mapped the land, the Moon, and Mars — but what about the bottom of the sea? What technology maps the ocean floor?\"[/bold yellow]",
    "digital_maps": "Puck puts on a pair of tiny glowing glasses and arrows appear floating in the air. [bold yellow]\"In the future, maps won't just be on screens — they'll float in the world around you. What is this technology called?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "map_reader": (
        "Map Reader",
        "Learned to read symbols, legends, scale bars, and titles on any map!",
    ),
    "compass_master": (
        "Compass Master",
        "Mastered all four cardinal directions and the compass rose!",
    ),
    "map_collector": (
        "Map Collector",
        "Explored every kind of map — from road maps to satellite images!",
    ),
    "coordinate_finder": (
        "Coordinate Finder",
        "Learned latitude, longitude, and grid references to find any place on Earth!",
    ),
    "navigator": (
        "Navigator",
        "Mastered route planning, distance measuring, and real-world map use!",
    ),
    "map_historian": (
        "Map Historian",
        "Explored maps from ancient Babylon to Mars and the ocean floor!",
    ),
    "digital_explorer": (
        "Digital Explorer",
        "Discovered GPS, satellites, navigation apps, and the future of maps!",
    ),
}
