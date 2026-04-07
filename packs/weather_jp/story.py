"""
story.py — Narrative for the Weather & Seasons skill pack.

Umi (海) guides you along a coastline where the sky is always changing,
teaching you to read, describe, and plan around Japanese weather.
"""

INTRO_STORY = """
[bold red]LEARN JAPANESE[/bold red]
[bold yellow]Chapter: Weather & Seasons[/bold yellow]

The harbor stretched before you under a sky that couldn't decide
what it wanted to be — half blue, half bruised with clouds,
a curtain of rain dragging across the far headland.

Fishing boats rocked gently. A wind vane on the breakwater
spun from west to east. Somewhere a radio crackled:
[bold cyan]「明日は晴れでしょう。」[/bold cyan]

Umi stood at the water's edge, face tilted toward the sky,
reading it the way others read books.

[bold cyan]"Weather shapes everything in Japan,"[/bold cyan] Umi said quietly.

[bold cyan]"The words for rain, wind, snow, and sun.
The four seasons — each with its own vocabulary,
its own festivals, its own food.
Even plans change with the forecast.
A single word — 台風 — can cancel an entire week."[/bold cyan]

She turned to you, ocean spray catching the light behind her.

[bold cyan]"Today we learn the language of the sky.
How to name what you see, predict what's coming,
and make plans that bend with the weather."[/bold cyan]

Umi gestured toward the shifting horizon.

[bold cyan]"Let's begin — the sky won't wait."[/bold cyan]

[bold white]Your journey into Japanese weather and seasons begins now.[/bold white]
"""

ZONE_INTROS = {
    "weather_words": """
Umi pointed to the sky, where clouds drifted over the harbor
and sunlight broke through in shifting columns.

[bold cyan]"Every conversation in Japan starts with the weather,"[/bold cyan]
Umi said, watching the light play on the waves.
[bold cyan]"天気, 暑い, 寒い, 雨, 雪, 晴れ, 曇り, 風 —
hot, cold, rain, snow, sun, clouds, wind.
These are the first words you need
to talk about the world outside your window."[/bold cyan]

[bold white]Let's learn the weather words![/bold white]
""",
    "seasons": """
Umi stopped at a shrine gate where four banners hung,
each painted with a different tree — cherry, sunflower, maple, pine.

[bold cyan]"Japan lives and breathes its four seasons,"[/bold cyan]
Umi said, touching each banner in turn.
[bold cyan]"春, 夏, 秋, 冬 — spring, summer, autumn, winter.
Each season has its own festivals, food, and customs.
お花見 in spring, 花火 in summer, 紅葉 in autumn.
The seasons aren't just weather — they're culture."[/bold cyan]

[bold white]Let's explore the four seasons![/bold white]
""",
    "temperature_climate": """
Umi led you to a small weather station perched on the cliff,
its instruments spinning and clicking in the wind.

[bold cyan]"Numbers tell part of the story,"[/bold cyan]
Umi said, tapping a thermometer.
[bold cyan]"温度, 度, 湿度, 気温 — temperature, degrees,
humidity, air temperature.
蒸し暑い — that heavy, sticky summer heat.
涼しい — the cool relief of an autumn breeze.
Japan's climate swings from one extreme to another."[/bold cyan]

[bold white]Let's learn about temperature and climate![/bold white]
""",
    "weather_forecasts": """
Umi tuned the radio to the morning forecast.
A calm voice read numbers and conditions across the map.

[bold cyan]"Every Japanese morning starts with 天気予報,"[/bold cyan]
Umi said, listening closely.
[bold cyan]"降水確率 — chance of rain.
最高気温, 最低気温 — high and low temperatures.
晴れ時々曇り — sunny, sometimes cloudy.
梅雨, 台風 — rainy season, typhoons.
Understanding the forecast is a survival skill."[/bold cyan]

[bold white]Let's decode weather forecasts![/bold white]
""",
    "plans_with_weather": """
Umi spread a hand-drawn calendar on the table,
weather icons sketched next to each day's plans.

[bold cyan]"In Japan, plans always have a weather clause,"[/bold cyan]
Umi said, tapping the calendar.
[bold cyan]"雨だったら — if it rains.
晴れたら — if it clears up.
中止, 延期, 雨天決行 — cancelled, postponed, rain or shine.
台風 alone can rewrite an entire schedule.
Let's learn to make plans that work with the sky."[/bold cyan]

[bold white]Let's learn to plan around the weather![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "weather_words": """
[bold green]Umi closed her weather journal with a satisfied nod![/bold green]

[bold cyan]"天気, 暑い, 寒い, 雨, 雪, 晴れ, 曇り, 風 —
you can name everything the sky throws at you now.
Sun, rain, snow, wind, clouds — these eight words
are your foundation for every weather conversation."[/bold cyan]
""",
    "seasons": """
[bold green]Umi hung a completed four-seasons banner on the shrine gate![/bold green]

[bold cyan]"春, 夏, 秋, 冬 — you know them all.
Cherry blossoms, summer festivals, autumn leaves, winter snow.
Japan's four seasons aren't just on the calendar —
they're in the food, the fashion, and every greeting."[/bold cyan]
""",
    "temperature_climate": """
[bold green]Umi recorded your results on the weather station clipboard![/bold green]

[bold cyan]"温度, 湿度, 気温, 蒸し暑い, 涼しい, 暖かい, 乾燥 —
you can describe any climate condition now.
From Tokyo's muggy summers to Hokkaido's dry winters,
you have the vocabulary to feel the weather in Japanese."[/bold cyan]
""",
    "weather_forecasts": """
[bold green]Umi turned off the radio — you don't need it anymore![/bold green]

[bold cyan]"天気予報, 降水確率, 最高気温, 最低気温,
時々, 注意報, 梅雨 — you can decode
any Japanese weather forecast now.
Tomorrow's weather? You'll understand it
before the announcer finishes speaking."[/bold cyan]
""",
    "plans_with_weather": """
[bold green]Umi tore up the backup plan — you won't need it![/bold green]

[bold cyan]"雨だったら, 晴れたら, 寒かったら,
中止, 延期, 雨天決行 — you can make plans,
change plans, and talk about plans
all in natural Japanese.
Rain or shine, you're ready for anything."[/bold cyan]
""",
}

BOSS_INTROS = {
    "weather_words": """
Umi stood at the cliff edge, wind whipping around her.

[bold cyan]"Sun, rain, snow, wind, clouds, hot, cold —
name them all. The sky is testing you,
and so am I."[/bold cyan]
""",
    "seasons": """
Umi pointed to where four paths met at the shrine,
each one representing a different season.

[bold cyan]"Spring, summer, autumn, winter —
their festivals, their traditions, their words.
Show me you know them all."[/bold cyan]
""",
    "temperature_climate": """
Umi stood before a wall of climate charts and maps.

[bold cyan]"Degrees, humidity, muggy heat, cool breezes.
Japan's climate is extreme in every direction.
Prove you can describe it all."[/bold cyan]
""",
    "weather_forecasts": """
Umi handed you headphones playing a rapid-fire forecast.

[bold cyan]"Chance of rain, highs and lows,
advisories and rainy season.
Decode the forecast like a native listener."[/bold cyan]
""",
    "plans_with_weather": """
Umi stood at the harbor in the pouring rain, smiling.

[bold cyan]"If it rains, if it's sunny, if a typhoon hits —
cancelled, postponed, rain or shine.
Make your plans. The weather won't wait."[/bold cyan]
""",
}
