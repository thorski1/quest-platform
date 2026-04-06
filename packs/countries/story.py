"""
story.py — Narrative for the Countries skill pack (The Passport Office).

Puck stamps open a magical passport and guides the reader on a journey
through every nation — flags, capitals, continents, landmarks, and languages.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Passport Office[/bold yellow]

Puck appeared from behind a tall wooden desk, wearing a tiny customs
officer's cap and holding up a small blue book — no bigger than a
playing card, but glowing softly at the edges.

[bold cyan]"A passport!"[/bold cyan] Puck announced, stamping it with a flourish.
[bold cyan]"Every great traveler needs one. And this is no ordinary passport —
every time you learn something about a new country, a stamp appears
inside. Flags, capitals, landmarks, languages — each one earns you
a new stamp."[/bold cyan]

The girl reached for the little book. It felt warm in her hand.
[bold white]"How many stamps can I collect?"[/bold white]

[bold cyan]"As many as the world has countries!"[/bold cyan] Puck grinned,
adjusting the tiny cap. [bold cyan]"And that's nearly two hundred.
But we'll start with the most interesting ones — the flags that
tell stories, the capitals that surprise you, the landmarks
that take your breath away."[/bold cyan]

The passport opened on its own, and the first page was blank,
waiting for its very first stamp.

[bold cyan]"Ready to see the world?"[/bold cyan]

[bold white]Your journey through the nations of the world begins now.[/bold white]
"""

ZONE_INTROS = {
    "flags_of_the_world": """
Puck flew to a wall of fluttering flags — hundreds of them,
each one different, each one telling a story.

[bold cyan]"Every country in the world has a flag,"[/bold cyan] Puck said,
landing on a bright red one. [bold cyan]"And every flag has a reason —
a colour chosen for bravery, a shape for unity, a star for hope.
Some flags are famous. Some will surprise you."[/bold cyan]

Flags of every colour swirled in the air:
[bold yellow]Red circles, maple leaves, crescent moons, southern crosses...[/bold yellow]

[bold white]Can you recognize the flags of the world?[/bold white]
""",
    "capital_cities": """
Puck pulled out a magnifying glass and held it over the glowing map.
Tiny dots of light marked every capital city on Earth.

[bold cyan]"A capital city,"[/bold cyan] Puck explained, [bold cyan]"is the heartbeat
of a country. It's where the leaders meet, where the biggest decisions
are made. Some capitals are famous — but some will surprise you.
The biggest city isn't always the capital!"[/bold cyan]

Glowing names floated above the dots:
[bold yellow]Paris · Tokyo · Cairo · Canberra · Brasilia...[/bold yellow]

[bold white]Can you match each country to its capital?[/bold white]
""",
    "continents_deep_dive": """
Puck spread a giant atlas across the desk — so big it hung off
the edges — and pointed to each continent in turn.

[bold cyan]"You know the seven continents,"[/bold cyan] Puck said.
[bold cyan]"But do you know what makes each one special?
Africa's longest river, Asia's billions of people,
Antarctica's impossible cold, Australia's one-of-a-kind animals?
Every continent has secrets waiting to be discovered."[/bold cyan]

Seven continents glowed in seven colours.

[bold white]Let's dive deep into each continent![/bold white]
""",
    "famous_landmarks": """
Puck gasped and pointed to golden spots glowing on the map —
each one marking something extraordinary.

[bold cyan]"Landmarks!"[/bold cyan] Puck whispered. [bold cyan]"The most amazing
things that humans have ever built — and the most incredible
places that nature has ever made. Towers and pyramids,
temples and statues, cities carved from stone."[/bold cyan]

Golden light traced paths between the landmarks:
[bold yellow]Paris · Egypt · India · Peru · Rome · Jordan...[/bold yellow]

[bold cyan]"Some of these are thousands of years old.
Some were almost lost. All of them will take your breath away."[/bold cyan]

[bold white]Let's visit the world's most famous landmarks![/bold white]
""",
    "countries_and_languages": """
Puck cupped a wing to one ear and listened. From the passport's
pages came a hundred different voices, each speaking a different
language — greetings from every corner of the world.

[bold cyan]"Bonjour! Jambo! Ni hao! Hola! Namaste!"[/bold cyan] Puck called out.
[bold cyan]"There are over 7,000 languages on Earth. SEVEN THOUSAND.
Some are spoken by a billion people. Some are spoken by just
a few hundred. Each one is a whole way of seeing the world."[/bold cyan]

The passport pages filled with scripts from every continent —
Latin letters, Chinese characters, Arabic calligraphy, Devanagari...

[bold white]Let's discover the languages of the world![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "flags_of_the_world": """
[bold green]A wall of flags unfurls in celebration![/bold green]

Every flag you learned glows with its true colors —
the red circle of Japan, the maple leaf of Canada,
the six colors of South Africa, the impossible triangles of Nepal.

[bold cyan]"You can read flags now,"[/bold cyan] Puck says proudly.
[bold cyan]"Every flag is a story — courage, history, hope —
and you know how to read them."[/bold cyan]

The passport stamps itself: [bold yellow]FLAG EXPERT[/bold yellow]

Capital city dots begin to glow on the map. The next adventure awaits...
""",
    "capital_cities": """
[bold green]Capital cities blaze like stars across the map![/bold green]

Paris, Tokyo, Cairo, Canberra, Brasilia, Nairobi, Seoul —
each one shining, each one named, each one yours.

[bold cyan]"You know where the hearts of countries beat,"[/bold cyan] Puck says.
[bold cyan]"Some capitals surprise people — Australia's isn't Sydney,
Brazil's isn't Rio. But you know the truth."[/bold cyan]

The passport stamps itself: [bold yellow]CAPITAL EXPERT[/bold yellow]

The continents glow warmly. It's time to dive deeper...
""",
    "continents_deep_dive": """
[bold green]All seven continents glow with new knowledge![/bold green]

The Nile winding through Africa. Asia's billions of people.
Europe's patchwork of nations. The Amazon breathing for the world.
The Great Lakes of North America. Antarctica's impossible cold.
Australia's one-of-a-kind animals. And Pangaea — the ancient
supercontinent that started it all.

[bold cyan]"You don't just know the continents,"[/bold cyan] Puck says warmly.
[bold cyan]"You understand them. That's the difference between
memorizing and truly learning."[/bold cyan]

The passport stamps itself: [bold yellow]CONTINENT SCHOLAR[/bold yellow]

Golden landmarks begin to glow on the map...
""",
    "famous_landmarks": """
[bold green]The landmarks blaze with golden light![/bold green]

The Eiffel Tower reaching for the sky. The Great Wall winding
across China. The Pyramids standing eternal in the desert.
The Taj Mahal glowing white. Lady Liberty holding her torch.
Machu Picchu above the clouds. The Colosseum echoing with
ancient cheers. And Petra — a whole city carved from pink stone.

[bold cyan]"These are humanity's greatest achievements,"[/bold cyan] Puck says quietly.
[bold cyan]"People built these. People just like you — with ideas,
determination, and a dream of making something that would last."[/bold cyan]

The passport stamps itself: [bold yellow]LANDMARK EXPLORER[/bold yellow]

Voices from a hundred countries drift from the final pages...
""",
    "countries_and_languages": """
[bold green]A chorus of voices rises from every page of the passport![/bold green]

Mandarin and Portuguese, French and Swahili, sign language
and hieroglyphics — and 840 languages in one incredible country.

[bold cyan]"You've done it,"[/bold cyan] Puck says, wings spread wide.
[bold cyan]"Flags, capitals, continents, landmarks, languages —
you've traveled the entire world without leaving this page.
And every stamp in your passport proves it."[/bold cyan]

Puck removes the tiny customs cap and bows.

[bold cyan]"The world isn't strange anymore. It's yours."[/bold cyan]

[bold white]World Traveler. Flag Reader. Language Explorer. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "flags_of_the_world": "Puck holds up a flag that looks completely wrong — it isn't even a rectangle! [bold yellow]\"Almost every flag in the world is a rectangle. But one country broke all the rules. Can you guess which one?\"[/bold yellow]",
    "capital_cities": "Puck points to a mysterious country on the map. [bold yellow]\"This country moved its capital to a secret new city — and most people have never even heard of it. Can you name it?\"[/bold yellow]",
    "continents_deep_dive": "Puck pushes the seven continents together on the atlas like puzzle pieces. [bold yellow]\"Millions of years ago, all the continents were ONE. What was that ancient supercontinent called?\"[/bold yellow]",
    "famous_landmarks": "Puck flies through a narrow canyon on the map and gasps at what lies beyond. [bold yellow]\"An entire city — carved from pink stone, hidden in a desert canyon for centuries. Do you know its name?\"[/bold yellow]",
    "countries_and_languages": "Puck holds up a globe covered in tiny dots of light — each one a different language. [bold yellow]\"One small country has over 840 languages — more than any other place on Earth. Which country holds this incredible record?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "flag_expert": (
        "Flag Expert",
        "Recognized flags from countries all around the world!",
    ),
    "capital_expert": (
        "Capital Expert",
        "Matched countries to their capital cities — even the tricky ones!",
    ),
    "continent_scholar": (
        "Continent Scholar",
        "Discovered deep facts about all seven continents!",
    ),
    "landmark_explorer": (
        "Landmark Explorer",
        "Visited the world's greatest buildings and monuments!",
    ),
    "language_explorer": (
        "Language Explorer",
        "Discovered the amazing languages spoken around the world!",
    ),
}
