"""
story.py — Narrative for the Geography skill pack.

Puck opens a glowing atlas and guides the reader across the entire world —
continents and oceans, capitals and maps, mountains and rivers, and the
greatest wonders the Earth has ever made.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Atlas of Wonders[/bold yellow]

Puck appeared at the edge of the Primer's newest page, holding something
enormous — a book almost as big as the Primer itself, its cover made of
living light. Every time it shifted, a different country came into focus.

[bold cyan]"An atlas!"[/bold cyan] Puck announced, spreading wings wide.
[bold cyan]"A book of maps. And not just any maps — the whole world,
every continent, every ocean, every great city and river and mountain.
All of it waiting for you."[/bold cyan]

The girl leaned forward. [bold white]"The whole world is in there?"[/bold white]

[bold cyan]"Every part of it."[/bold cyan] Puck ran a tiny hand across the glowing cover.
[bold cyan]"And once you know where things are — and [italic]why[/italic] they're there —
the world stops being a jumble of names and becomes a place
you can actually [italic]understand.[/italic]"[/bold cyan]

The atlas opened on its own. A map of the Earth appeared,
all blues and greens and golds, with tiny glowing dots
where the great cities stood.

[bold cyan]"Seven continents. Five oceans. Hundreds of countries.
One planet. [italic]Our[/italic] planet."[/bold cyan]

Puck looked up with a grin.

[bold cyan]"Ready to explore it?"[/bold cyan]

[bold white]Your adventure around the world begins now.[/bold white]
"""

ZONE_INTROS = {
    "continents": """
Puck spread the atlas open to a page showing the whole round Earth.

[bold cyan]"The land is divided into seven great pieces,"[/bold cyan] Puck said.
[bold cyan]"We call them continents. Each one has its own animals,
its own weather, its own people and languages and stories."[/bold cyan]

Seven colored shapes glowed on the map:
[bold yellow]Africa · Antarctica · Asia · Australia · Europe · North America · South America[/bold yellow]

[bold white]Let's learn where they all are![/bold white]
""",
    "oceans_and_seas": """
Puck dipped a wing into the blue spaces between the continents.

[bold cyan]"Most of the Earth,"[/bold cyan] Puck said, [bold cyan]"is water. Five great oceans
cover more than two-thirds of our whole planet. Ships sail them.
Fish live in them. Rain begins in them. And every shoreline
in the world has one of them lapping at its feet."[/bold cyan]

Five ocean names shimmered across the deep blue:
[bold yellow]Pacific · Atlantic · Indian · Arctic · Southern[/bold yellow]

[bold white]Let's dive in and learn the Great Waters![/bold white]
""",
    "countries_capitals": """
Puck flew to a tiny glowing dot on the map.

[bold cyan]"Every country has a capital city,"[/bold cyan] Puck explained.
[bold cyan]"It's where the leaders meet, where the great buildings stand,
where the heart of the country beats. If you know the capital,
you know something true about every country in the world."[/bold cyan]

Little flags fluttered above the glowing dots.

[bold white]Can you match the country to its capital city?[/bold white]
""",
    "maps_and_directions": """
Puck pointed to a small compass rose in the corner of the atlas.

[bold cyan]"A map,"[/bold cyan] Puck said, [bold cyan]"is only useful if you can read it.
And to read it, you need to understand its language —
directions, distance, the lines that wrap around the globe."[/bold cyan]

The compass needle spun slowly and settled: North.

[bold cyan]"North, South, East, West. The equator. The prime meridian.
The key that tells you what every symbol means.
Once you know these, every map in the world opens up to you."[/bold cyan]

[bold white]Let's learn to read the map![/bold white]
""",
    "landforms": """
Puck traced a finger along a line of tiny mountains on the map.

[bold cyan]"The land isn't flat,"[/bold cyan] Puck said. [bold cyan]"It rises into mountains
and sinks into valleys. Rivers carve through it. Deserts bake.
Islands float. Peninsulas reach out into the sea.
Each landform has a name — and once you know the name,
you can picture it anywhere in the world."[/bold cyan]

The atlas showed mountains, rivers, deserts, and more.

[bold white]Let's discover mountains, rivers, and all the shapes of the Earth![/bold white]
""",
    "world_wonders": """
Puck held up the very last page of the atlas, and it glowed gold.

[bold cyan]"This,"[/bold cyan] Puck whispered, [bold cyan]"is the most special page.
The wonders. Places so extraordinary that the whole world
agrees: these must be remembered, protected, celebrated.
Some were built by people thousands of years ago.
Some were made by the Earth itself over millions of years."[/bold cyan]

A golden light traced across the map — Egypt, China, France,
Peru, the border between two great countries...

[bold white]Let's visit the wonders of the world![/bold white]
""",
    "weather_and_climate": """
Puck floated to a new section of the atlas — pages that shifted colour
as you watched, from deep green to pale gold to icy white.

[bold cyan]"Climate,"[/bold cyan] Puck said, [bold cyan]"is the long-term weather pattern
of a place. Not just today's forecast — but what every year
feels like: how hot, how cold, how wet, how dry."[/bold cyan]

Four great bands of colour spread across the globe:
[bold yellow]Tropical · Desert · Temperate · Polar[/bold yellow]

[bold cyan]"And then there are the great rains — the monsoon —
and the mystery of why we have four seasons at all.
It all comes down to one thing: the tilt of the Earth."[/bold cyan]

[bold white]Let's explore the weathers of the world![/bold white]
""",
    "flags_and_symbols": """
Puck flew to a new page of the atlas where tiny flags fluttered
on every country — hundreds of them, each one different.

[bold cyan]"Flags,"[/bold cyan] Puck said, landing on one, [bold cyan]"are a country's
hello to the world. Each one has a story: a colour chosen
for a reason, a symbol with a meaning, a shape no other
country shares."[/bold cyan]

Flags swirled past — red leaves, rising suns, southern crosses,
eagles, triangles...

[bold cyan]"National animals are the same — chosen because they say
something true about the land. A jaguar, an eagle, a kangaroo.
Each one belongs to one place on Earth."[/bold cyan]

[bold white]Let's read the language of flags![/bold white]
""",
    "peoples_and_cultures": """
The final page of the atlas was different from all the others.

It didn't show mountains or oceans or borders.
It showed [bold yellow]faces[/bold yellow] — thousands of faces from every corner of the world.

[bold cyan]"Eight billion people,"[/bold cyan] Puck said quietly,
[bold cyan]"speak 7,000 languages. They eat different foods,
celebrate different festivals, tell different stories.
And yet — everywhere you go — people love their children,
tell jokes, sing songs, and watch the same sun set."[/bold cyan]

[bold white]The atlas glows its warmest yet. Let's meet the people of Earth.[/bold white]
""",
    "rivers_and_lakes": """
Puck traced a glowing blue line across the atlas with one wing.

[bold cyan]"Rivers,"[/bold cyan] Puck said, [bold cyan]"are the veins of the world.
They carry fresh water from the mountains to the sea,
feeding every plant and animal and city along the way."[/bold cyan]

The Nile glowed in Africa. The Amazon shimmered in South America.
Lake Baikal sparkled deep in Russia.

[bold cyan]"Every great civilisation in history was born beside a river.
Let's discover the world's greatest rivers and lakes!"[/bold cyan]

[bold white]Where will the water take us?[/bold white]
""",
    "animals_and_habitats": """
Puck opened the very last section of the atlas — and it was alive.

Tiny animals moved across every page: a polar bear in the white north,
a toucan in the green south, a camel crossing gold sand, a whale
diving through dark blue deep.

[bold cyan]"A habitat,"[/bold cyan] Puck said warmly, [bold cyan]"is home.
Every animal on Earth has a habitat — the place where it finds
everything it needs: food, water, shelter, and the right temperature.
And each one has its own amazing adaptations."[/bold cyan]

[bold white]Let's explore where animals live all over the world![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "continents": """
[bold green]All seven continents glow on the map![/bold green]

Each one shines in its own color — Africa in amber, Asia in jade,
Antarctica in white, the Americas in gold, Europe in rose, Australia in coral.

[bold cyan]"You know the seven lands,"[/bold cyan] Puck says proudly.
[bold cyan]"Wherever you go in the world, you'll always know
which great continent you're standing on."[/bold cyan]

The oceans shimmer invitingly. The Great Waters are next...
""",
    "oceans_and_seas": """
[bold green]Five oceans ripple with light![/bold green]

The Pacific, the Atlantic, the Indian, the Arctic, the Southern —
all five glow a deep, beautiful blue.

[bold cyan]"You know the Great Waters now,"[/bold cyan] Puck says.
[bold cyan]"Every sailor who ever set out across the sea knew these names.
Now you do too."[/bold cyan]

Little capital city dots light up across the map. The countries are waiting...
""",
    "countries_capitals": """
[bold green]The capital cities glow like stars![/bold green]

Paris and Tokyo and Washington D.C. and Brasília —
each one lit and named, each one yours.

[bold cyan]"Capitals,"[/bold cyan] Puck says, [bold cyan]"are where history happens.
You'll see these names in newspapers and stories for the rest of your life —
and now you know exactly where they are."[/bold cyan]

A compass rose begins to spin in the corner of the map. It's time to learn how to read it...
""",
    "maps_and_directions": """
[bold green]The compass glows, the grid lines shine![/bold green]

North, South, East, West. Latitude and longitude.
The equator. The prime meridian. The legend.
All of it yours.

[bold cyan]"You can read a map,"[/bold cyan] Puck says with delight.
[bold cyan]"Any map. Any atlas. Any globe.
The language of maps is yours now."[/bold cyan]

The atlas opens to a page of mountains and rivers. The landforms are waiting...
""",
    "landforms": """
[bold green]The landforms rise and shine across the atlas![/bold green]

Mountains, rivers, deserts, islands, peninsulas —
each one glowing with its name and its shape.

[bold cyan]"The Earth has so many faces,"[/bold cyan] Puck says softly.
[bold cyan]"And you know them all. The Nile cutting through the desert,
the Sahara stretching to the horizon, an island surrounded by sea.
You see the world more clearly now."[/bold cyan]

The final golden page shimmers ahead. The wonders are waiting...
""",
    "world_wonders": """
[bold green]The golden page blazes with wonder![/bold green]

Every wonder glows: the Great Wall, the Eiffel Tower, the Pyramid,
Niagara Falls, Machu Picchu — all of them real, all of them waiting
for you to one day see them with your own eyes.

[bold cyan]"You've traveled the whole world,"[/bold cyan] Puck says quietly.
[bold cyan]"Seven continents. Five oceans. Capitals, maps, landforms, wonders.
The atlas is yours now — every page of it."[/bold cyan]

Puck closes the glowing atlas gently.

[bold white]Explorer. Adventurer. World-knower.[/bold white]
[bold white]That's you.[/bold white]
""",
    "weather_and_climate": """
[bold green]The climate map glows in four beautiful bands![/bold green]

Tropical green at the Equator. Desert gold across the dry belts.
Temperate blue-green across the middle latitudes. Polar white
at both ends of the world.

[bold cyan]"You understand why the world's weather is the way it is,"[/bold cyan] Puck says.
[bold cyan]"The tilt of the Earth. The rains that farmers pray for.
The four seasons that turn like a wheel, year after year.
This is geography [italic]and[/italic] science at the same time."[/bold cyan]

The atlas turns to its brightest, most colourful pages: the flags...
""",
    "flags_and_symbols": """
[bold green]The Hall of Flags rings with colour![/bold green]

Red maple leaves, rising suns, Southern Crosses, bald eagles,
double pennants — every flag understood, every symbol known.

[bold cyan]"Flags and symbols,"[/bold cyan] Puck says softly, [bold cyan]"are how countries
say who they are without using words.
Now when you see a flag, you'll know its story."[/bold cyan]
""",
    "peoples_and_cultures": """
[bold green]Eight billion faces, all known![/bold green]

Languages, populations, festivals, traditions — the people
of Earth explored from Carnival in Brazil to origami in Japan,
from Mandarin speakers to the 840 languages of Papua New Guinea.

[bold cyan]"You've learned so much,"[/bold cyan] Puck says.
[bold cyan]"But the atlas still has two more pages — the waters that flow
through the land, and the wild creatures that call it home."[/bold cyan]

A ribbon of blue light flows across the map. The rivers are calling...
""",
    "rivers_and_lakes": """
[bold green]The rivers glow — great blue ribbons across the world![/bold green]

The Nile winding north to the sea. The Amazon rushing east
through green shadow. Lake Baikal shining deep in Russia's heart.

[bold cyan]"Rivers,"[/bold cyan] Puck says softly, [bold cyan]"are the veins of the world.
Every great civilisation was born beside one.
Now you know the greatest of them all."[/bold cyan]

The atlas rustles to its final page — the animals are waiting...
""",
    "animals_and_habitats": """
[bold green]The whole world glows — and every corner is full of life![/bold green]

Arctic bears and desert camels, rainforest toucans and ocean whales,
migrating terns crossing the sky from pole to pole.

[bold cyan]"You've done it."[/bold cyan] Puck's wings spread wide.
[bold cyan]"Continents, oceans, capitals, maps, landforms, wonders,
weather, flags, peoples, rivers, animals —
the whole world, page by page. It's all yours."[/bold cyan]

[bold white]World Explorer. Map Master. Habitat Guide. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "continents": "Puck points to the smallest, strangest continent on the map. [bold yellow]\"This one is the trickiest! It's a continent all by itself — and almost nobody lives there. Think carefully!\"[/bold yellow]",
    "oceans_and_seas": "The atlas turns to a page showing Antarctica surrounded by swirling blue water. [bold yellow]\"One special ocean wraps all the way around the bottom of the world. Do you know its name?\"[/bold yellow]",
    "countries_capitals": "A large country with a dragon on its flag glows on the map. [bold yellow]\"The most populous country on Earth! Do you know where its leaders meet?\"[/bold yellow]",
    "maps_and_directions": "Puck draws a long line straight down the center of the atlas. [bold yellow]\"This is the most important line on any map. It's where East meets West. What's it called?\"[/bold yellow]",
    "landforms": "A tiny triangle of land appears where a great river meets the sea. [bold yellow]\"Rivers drop their soil as they reach the ocean and build a special shape. What do we call it?\"[/bold yellow]",
    "world_wonders": "The atlas blazes gold. [bold yellow]\"One country has more UNESCO World Heritage Sites than any other. It's ancient, beautiful, and full of art. Which country is it?\"[/bold yellow]",
    "weather_and_climate": "The climate map shows four great coloured bands across the globe. [bold yellow]\"One zone has four proper seasons — warm summers, cold winters, everything in between. It covers most of Europe and North America. Which climate zone is it?\"[/bold yellow]",
    "flags_and_symbols": "A soaring bird of prey glides across the atlas page. [bold yellow]\"One great nation chose this bird as its national symbol — a bird found only in North America, meaning freedom and strength. Which country, and which bird?\"[/bold yellow]",
    "peoples_and_cultures": "Puck holds up a tiny globe with thousands of tiny dots of light — each one a different language. [bold yellow]\"One small country near Australia has over 840 different languages. Can you name it? The most linguistically rich place on Earth!\"[/bold yellow]",
    "rivers_and_lakes": "Puck points to the deepest spot on the map of Russia — a shimmering dark blue. [bold yellow]\"This lake is the deepest in the world — deeper than five Empire State Buildings! It holds 20% of all the fresh water on Earth. Which lake is it?\"[/bold yellow]",
    "animals_and_habitats": "A tiny bird appears on the atlas page, drawing a line from the very top of the world all the way to the very bottom. [bold yellow]\"This small seabird makes the longest journey of any animal on Earth — 70,000 kilometres every year! What is it called?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "continent_explorer": (
        "Continent Explorer",
        "Named and placed all seven continents on the world map!",
    ),
    "ocean_keeper": (
        "Ocean Keeper",
        "Learned the five great oceans and their places on the globe!",
    ),
    "capital_scholar": (
        "Capital Scholar",
        "Matched every country to its capital city!",
    ),
    "map_reader": (
        "Map Reader",
        "Learned to read directions, latitude, longitude, and map legends!",
    ),
    "landform_guide": (
        "Landform Guide",
        "Named the mountains, rivers, deserts, and shapes of the Earth!",
    ),
    "world_wonder": (
        "World Wonder",
        "Visited all the great wonders of the world — without leaving the Primer!",
    ),
}
