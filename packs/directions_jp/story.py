"""
story.py — Narrative for the Directions & Places skill pack.

Umi (海) guides you through a Japanese coastal town, teaching you to
navigate streets, ask for directions, and describe locations.
"""

INTRO_STORY = """
[bold red]LEARN JAPANESE[/bold red]
[bold yellow]Chapter: Directions & Places[/bold yellow]

The morning fog lifted over the harbor, revealing a town of narrow
streets, tiled rooftops, and wooden signposts pointing in every direction.

You stepped off the ferry onto an unfamiliar dock, surrounded by
the sounds of seagulls and distant train bells.

A familiar figure emerged from the mist, a folded map tucked
under one arm.

[bold cyan]"Welcome,"[/bold cyan] Umi said, unfolding the map with a smile.

[bold cyan]"Today we learn the language of navigation.
Right, left, straight ahead. Stations, hospitals, schools.
How to ask where things are and how to get there --
the words that turn a stranger into a local."[/bold cyan]

She traced a route on the map with her finger.

[bold cyan]"In Japan, giving directions is an art.
There are no street names in most neighborhoods.
Instead, people guide you by landmarks, turns,
and the spaces between buildings."[/bold cyan]

Umi folded the map and began walking into the town.

[bold cyan]"Let's find our way -- the ocean is always our compass."[/bold cyan]

[bold white]Your journey into Japanese directions begins now.[/bold white]
"""

ZONE_INTROS = {
    "basic_directions": """
Umi stood at a four-way intersection where the harbor road
split into winding paths between traditional houses.

[bold cyan]"Before you can go anywhere, you need the basics,"[/bold cyan]
Umi said. [bold cyan]"右 for right, 左 for left, まっすぐ for
straight ahead, 曲がる for turning. These four words
are your compass. Master them and no street in Japan
can confuse you."[/bold cyan]

[bold white]Let's master basic directions![/bold white]
""",
    "places_in_town": """
Umi spread her map on a stone wall overlooking the town,
pointing out buildings dotted across the hillside.

[bold cyan]"Now that you can move, you need to know where to go,"[/bold cyan]
Umi explained. [bold cyan]"駅 for the station, 病院 for the hospital,
銀行 for the bank, 郵便局 for the post office, 学校 for the school.
Every town has these landmarks. Learn their names and
the whole map opens up to you."[/bold cyan]

[bold white]Let's learn the places in town![/bold white]
""",
    "asking_for_directions": """
Umi paused at the edge of a narrow street where an elderly
woman was sweeping the entrance to a tea shop.

[bold cyan]"Knowing words is one thing. Asking for help is another,"[/bold cyan]
Umi said quietly. [bold cyan]"すみません to get attention.
〜はどこですか to ask where something is.
Japanese people are incredibly kind to lost travelers --
but you need the right words to unlock that kindness."[/bold cyan]

[bold white]Let's learn to ask for directions![/bold white]
""",
    "transportation": """
Umi led you to the station platform where a sleek train
hummed on the tracks, ready for departure.

[bold cyan]"Japan moves on trains, buses, and taxis,"[/bold cyan]
Umi said, watching the departure board. [bold cyan]"電車 for trains,
バス for buses, タクシー for taxis, 歩いて for on foot.
Knowing how to talk about transport is knowing
how to connect the dots between everywhere you want to be."[/bold cyan]

[bold white]Let's learn about transportation![/bold white]
""",
    "describing_locations": """
Umi climbed to a lookout point where the entire town
was visible -- rooftops, the harbor, the station, the school.

[bold cyan]"The final skill: describing where things are,"[/bold cyan]
Umi said, sweeping her hand across the view.
[bold cyan]"隣 for next to, 前 for in front, 後ろ for behind,
近く for nearby, 遠い for far. With these words you don't
just follow directions -- you give them.
You become the guide."[/bold cyan]

[bold white]Let's learn to describe locations![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "basic_directions": """
[bold green]Umi drew arrows in the sand: right, left, straight, turn![/bold green]

[bold cyan]"You've got the compass in your head now.
右, 左, まっすぐ, 曲がる -- four simple words
that unlock every street and alley.
No road in Japan can send you the wrong way."[/bold cyan]
""",
    "places_in_town": """
[bold green]Umi checked off every landmark on her map![/bold green]

[bold cyan]"駅, 病院, 銀行, 郵便局, 学校 --
you know every important place in town by name.
Walk into any Japanese city and you'll recognize
the landmarks that locals navigate by."[/bold cyan]
""",
    "asking_for_directions": """
[bold green]Umi smiled as a local bowed and pointed the way![/bold green]

[bold cyan]"すみません、〜はどこですか --
with this simple pattern, you'll never truly be lost.
Japanese people love helping travelers who try.
Your politeness is your best map."[/bold cyan]
""",
    "transportation": """
[bold green]Umi punched two tickets and boarded the coastal train![/bold green]

[bold cyan]"電車, バス, タクシー, 歩いて --
you know every way to move through Japan.
From bullet trains to quiet walks,
the entire country is open to you now."[/bold cyan]
""",
    "describing_locations": """
[bold green]Umi placed the final pin on her map of the town![/bold green]

[bold cyan]"隣, 前, 後ろ, 近く, 遠い --
you can describe where anything is relative to anything else.
You're not just a traveler anymore.
You're a navigator. The ocean town has no more secrets."[/bold cyan]
""",
}

BOSS_INTROS = {
    "basic_directions": """
Umi drew a path in the sand with branching turns.

[bold cyan]"You know right, left, straight, and turn.
Now combine them into a real set of directions.
One sentence, two actions -- guide me to the destination."[/bold cyan]
""",
    "places_in_town": """
Umi held up a letter and pointed toward the town.

[bold cyan]"You know the places. Now match the need to the place.
Where do you go to send a letter?
Show me you know this town."[/bold cyan]
""",
    "asking_for_directions": """
Umi gestured toward a busy street full of strangers.

[bold cyan]"You're lost. You need to find the station.
Put it all together -- the greeting, the question,
the polite form. One perfect sentence."[/bold cyan]
""",
    "transportation": """
Umi stood at a crossroads: train tracks, bus stop, taxi stand.

[bold cyan]"You know every mode of transport.
Now put it together: destination, method, and time.
One complete travel question."[/bold cyan]
""",
    "describing_locations": """
Umi handed you a blank map and a pen.

[bold cyan]"Describe where the bank is using two landmarks.
Next to one, in front of another.
Paint the location with words."[/bold cyan]
""",
}
