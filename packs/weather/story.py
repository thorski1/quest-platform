"""
story.py — Narrative for the Weather & Seasons skill pack.

Puck opens the Primer's Weather Station and guides the reader through
clouds, storms, seasons, and the tools that help us understand the sky.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Weather Station[/bold yellow]

Puck appeared on the Primer's newest page carrying something peculiar —
a tiny brass barometer in one hand and a spinning anemometer in the other.
Behind Puck, the sky on the page was alive: clouds drifted, rain fell
in silver streaks, and far off on the horizon, lightning flickered.

[bold cyan]"A Weather Station!"[/bold cyan] Puck announced, landing on the edge
of the page. [bold cyan]"The sky is the biggest, wildest, most
amazing show on Earth — and most people never look up."[/bold cyan]

The girl looked at the swirling sky on the page.
[bold white]"You can predict the weather?"[/bold white]

[bold cyan]"Anyone can,"[/bold cyan] Puck said, tucking the barometer under
one wing. [bold cyan]"Once you know what the clouds are saying,
why the wind blows, how the rain is born, and what makes
winter turn to spring — the sky stops being a mystery
and becomes a story you can [italic]read.[/italic]"[/bold cyan]

A thermometer rose on the left side of the page. A rain gauge
on the right. A weather vane spun gently at the top.

[bold cyan]"Every cloud tells a story. Every season has a reason.
Every storm follows rules. And once you know those rules —"[/bold cyan]

Puck grinned.

[bold cyan]"You'll never be surprised by the sky again."[/bold cyan]

[bold white]Your adventure through the Weather Station begins now.[/bold white]
"""

ZONE_INTROS = {
    "types_of_weather": """
Puck pointed up at the Primer's sky, which shifted from blue to grey
to gold to white as the page turned.

[bold cyan]"Let's start with the basics,"[/bold cyan] Puck said.
[bold cyan]"Sunny, rainy, snowy, windy, cloudy, foggy, stormy —
every type of weather you've ever felt on your face.
But do you know [italic]why[/italic] each one happens?"[/bold cyan]

Seven little weather icons danced across the top of the page:
[bold yellow]Sun · Raindrop · Snowflake · Wind · Cloud · Fog · Lightning[/bold yellow]

[bold white]Let's discover what makes the weather![/bold white]
""",
    "water_cycle_deep": """
Puck drew a glowing circle in the air with one wingtip.

[bold cyan]"Water,"[/bold cyan] Puck said, [bold cyan]"is on a never-ending
journey. From the ocean to the sky to the clouds to the rain
to the rivers and back to the ocean again.
Round and round and round — forever."[/bold cyan]

A single raindrop on the page began to glow, then rose
into the air, became a cloud, fell again, and flowed into a river.

[bold cyan]"It's called the water cycle. And the water you drink today
might be the same water a dinosaur splashed through
millions of years ago!"[/bold cyan]

[bold white]Let's follow the water on its great journey![/bold white]
""",
    "clouds": """
Puck floated upward until tiny wings brushed the top of the page,
where four very different clouds drifted past.

[bold cyan]"Clouds,"[/bold cyan] Puck whispered, [bold cyan]"are not just
pretty shapes. Each type has a name, a meaning, and a message.
Learn to read them and you can predict the weather
just by looking up."[/bold cyan]

Four cloud types appeared, each labelled in golden letters:
[bold yellow]Cumulus · Stratus · Cirrus · Cumulonimbus[/bold yellow]

[bold cyan]"Fluffy ones, flat ones, wispy ones, and the giants
that bring thunder. Let's meet them all."[/bold cyan]

[bold white]Welcome to the Cloud Gallery![/bold white]
""",
    "severe_weather": """
The Primer's sky darkened. The wind picked up.
Puck's expression turned serious — but not frightened.

[bold cyan]"Severe weather,"[/bold cyan] Puck said steadily.
[bold cyan]"Thunderstorms. Tornadoes. Hurricanes. Blizzards.
These are powerful forces — the most dramatic things
the atmosphere can do."[/bold cyan]

Lightning crackled across the dark page. A funnel cloud
twisted in the distance. A massive white spiral churned
over the ocean.

[bold cyan]"But here's the important part: if you understand them,
you don't have to be afraid of them. You just need to know
what to do. Knowledge is safety."[/bold cyan]

[bold white]Let's face the storms — and learn to stay safe![/bold white]
""",
    "seasons_deep": """
Puck held up a small model of the Earth — tilted slightly
to one side, spinning gently as it orbited a tiny Sun.

[bold cyan]"Why do we have summer and winter?"[/bold cyan] Puck asked.
[bold cyan]"Most people think it's because the Earth moves closer
to the Sun and farther away. But that's not right at all."[/bold cyan]

The little Earth tilted, and one half glowed warm while
the other half turned cool and blue.

[bold cyan]"It's the tilt. Just 23.5 degrees — a gentle lean.
That tiny angle gives us spring flowers, summer heat,
autumn colours, and winter snow."[/bold cyan]

[bold white]Let's discover why the seasons turn![/bold white]
""",
    "weather_tools": """
Puck pushed open a small wooden door on the page, revealing
a shed full of gleaming instruments — glass tubes, spinning cups,
brass dials, and a tall pole with an arrow on top.

[bold cyan]"The Instrument Shed!"[/bold cyan] Puck said proudly.
[bold cyan]"Every one of these tools measures something different
about the weather. Temperature, pressure, wind speed,
rainfall, wind direction — and way up in space,
satellites watching it all from above."[/bold cyan]

Six instruments hung on the wall, each glowing softly:
[bold yellow]Thermometer · Barometer · Anemometer · Rain Gauge · Weather Vane · Satellite[/bold yellow]

[bold white]Let's learn to use the tools of the trade![/bold white]
""",
    "weather_forecasting": """
Puck stood before a huge wall of weather maps, radar screens,
satellite images, and scrolling data.

[bold cyan]"This,"[/bold cyan] Puck said, spreading both wings wide,
[bold cyan]"is where everything comes together. All the clouds,
all the tools, all the science — meteorologists use it all
to answer the most important question in weather:"[/bold cyan]

Puck paused dramatically.

[bold cyan]"[italic]What's going to happen next?[/italic]"[/bold cyan]

Weather maps glowed with blue cold fronts and red warm fronts.
Radar screens showed green and yellow blobs of rain.
A forecast scrolled across the bottom of the page.

[bold white]Let's learn to predict the weather![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "types_of_weather": """
[bold green]All seven weather types glow across the sky![/bold green]

Sun, rain, snow, wind, cloud, fog, and storm —
each one understood, each one explained.

[bold cyan]"You know what causes every type of weather now,"[/bold cyan] Puck says.
[bold cyan]"Next time it rains, you'll know exactly why.
Next time the wind blows, you'll know where it's coming from."[/bold cyan]

A glowing drop of water begins to rise from the page. The water cycle awaits...
""",
    "water_cycle_deep": """
[bold green]The water cycle spins in a perfect, glowing circle![/bold green]

Evaporation, condensation, precipitation, collection —
round and round, never stopping, never running out.

[bold cyan]"The same water, over and over,"[/bold cyan] Puck says softly.
[bold cyan]"Every raindrop has been on this journey billions of times.
Now you know the whole trip by heart."[/bold cyan]

Four different clouds appear overhead. Time to learn their names...
""",
    "clouds": """
[bold green]The Cloud Gallery is complete![/bold green]

Cumulus, stratus, cirrus, cumulonimbus —
four great cloud families, each with its own shape,
its own height, its own weather story.

[bold cyan]"You can read the sky now,"[/bold cyan] Puck says with pride.
[bold cyan]"Look up tomorrow and name what you see.
The clouds have been talking all along —
now you understand their language."[/bold cyan]

The sky darkens ahead. The storms are waiting...
""",
    "severe_weather": """
[bold green]The storms part, and calm returns![/bold green]

Thunderstorms, tornadoes, hurricanes, blizzards —
each one understood, each one respected.

[bold cyan]"You faced the fiercest weather on Earth,"[/bold cyan] Puck says.
[bold cyan]"And more importantly, you know how to stay safe.
Knowledge doesn't just help you understand storms —
it protects you."[/bold cyan]

The Earth tilts gently on the next page. The seasons are calling...
""",
    "seasons_deep": """
[bold green]The Earth tilts, and the seasons turn like a great wheel![/bold green]

Solstice, equinox, hemisphere, axis —
the grand clockwork of the year, finally clear.

[bold cyan]"23.5 degrees,"[/bold cyan] Puck says. [bold cyan]"That's all it takes
to give us spring blossoms and autumn leaves,
long summer days and dark winter nights.
One small tilt — and everything changes."[/bold cyan]

A small wooden door appears on the page. The Instrument Shed is next...
""",
    "weather_tools": """
[bold green]Every instrument gleams — the Instrument Shed is mastered![/bold green]

Thermometer, barometer, anemometer, rain gauge,
weather vane, satellite — six tools, six measurements,
one complete picture of the sky.

[bold cyan]"You know how to measure the weather,"[/bold cyan] Puck says.
[bold cyan]"Temperature, pressure, wind, rain, direction —
and the satellites watching it all from space.
Now it's time to put it all together."[/bold cyan]

A wall of weather maps and forecasts lights up ahead...
""",
    "weather_forecasting": """
[bold green]The forecast is clear — and so is your understanding![/bold green]

Weather maps, radar, fronts, forecasts,
and the great difference between weather and climate —
all of it yours.

[bold cyan]"You've done it."[/bold cyan] Puck's wings spread wide.
[bold cyan]"Clouds, water cycles, storms, seasons, instruments,
and forecasting — the whole sky, explained.
Every time you look up from now on,
you'll see more than most people ever will."[/bold cyan]

Puck closes the Weather Station doors gently.

[bold white]Cloud Watcher. Storm Chaser. Weather Wizard. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "types_of_weather": "The Primer's page flashes white. Puck holds up a hand. [bold yellow]\"Lightning and thunder happen at the same instant — but we always see one before the other. Which one, and why?\"[/bold yellow]",
    "water_cycle_deep": "Puck draws a circle in the air — the great water cycle. [bold yellow]\"Four steps, one endless loop. Can you put them in the right order?\"[/bold yellow]",
    "clouds": "Puck soars to the highest point in the Primer's sky. [bold yellow]\"One type of cloud is made entirely of ice crystals — no liquid water at all. Which one?\"[/bold yellow]",
    "severe_weather": "Puck gestures to the four great storms on the page. [bold yellow]\"Only one of these forms over warm ocean water and can grow hundreds of kilometres wide. Which one?\"[/bold yellow]",
    "seasons_deep": "The Primer's page goes dark — no sunrise at all. [bold yellow]\"On one special day, the Sun never rises above the Arctic Circle. When, and why?\"[/bold yellow]",
    "weather_tools": "Puck points to the sky — far, far above, a satellite orbits silently. [bold yellow]\"This tool changed weather forecasting forever. What does it do that no ground instrument can?\"[/bold yellow]",
    "weather_forecasting": "Puck stands before a wall of data: pressure falling, warm air from the south, cold front from the west. [bold yellow]\"Put it all together — what's coming?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "weather_watcher": (
        "Weather Watcher",
        "Learned what causes every type of weather — sun, rain, snow, wind, and more!",
    ),
    "cycle_master": (
        "Cycle Master",
        "Followed water on its never-ending journey through the water cycle!",
    ),
    "cloud_reader": (
        "Cloud Reader",
        "Named every type of cloud and learned to read the sky!",
    ),
    "storm_survivor": (
        "Storm Survivor",
        "Faced thunderstorms, tornadoes, hurricanes, and blizzards — and learned to stay safe!",
    ),
    "season_scholar": (
        "Season Scholar",
        "Discovered why Earth has seasons — tilt, solstice, equinox, and all!",
    ),
    "instrument_keeper": (
        "Instrument Keeper",
        "Mastered every weather tool from thermometer to satellite!",
    ),
    "forecaster": (
        "Forecaster",
        "Learned to predict the weather like a real meteorologist!",
    ),
}
