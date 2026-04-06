"""
story.py — Narrative for the Transport skill pack.

Long Long guides you through the world of Chinese transportation,
from basic vehicle words to navigating stations and real travel conversations.
"""

INTRO_STORY = """
[bold red]LEARN CHINESE[/bold red]
[bold yellow]Chapter: Getting Around[/bold yellow]

Long Long the dragon swooped low over a bustling city, where buses
threaded through crowded streets, subway trains rumbled underground,
and high-speed rail lines stretched to the horizon like silver ribbons.

[bold cyan]"In China, you can cross the entire country without ever
driving a car,"[/bold cyan] Long Long said, landing atop a grand
train station with a tiled roof and red pillars.
[bold cyan]"Gong gong qi che, di tie, huo che, fei ji -- buses,
subways, trains, and planes. The transport network is a marvel,
but you need the right words to use it."[/bold cyan]

A family rushed past with suitcases, checking their tickets
and scanning departure boards covered in Chinese characters.

[bold cyan]"You'll need to buy tickets, ask for directions,
find the right platform, and tell the taxi driver where to go.
Every journey starts with a single word -- and today,
we'll learn them all."[/bold cyan]

Long Long spread his wings against the city skyline.

[bold cyan]"Ready to master the language of travel?"[/bold cyan]

[bold white]Your journey into Chinese transportation begins now.[/bold white]
"""

ZONE_INTROS = {
    "transportation_words": """
Long Long perched on a highway overpass, watching vehicles of
every kind stream past -- buses, taxis, bicycles, and sleek
electric cars.

[bold cyan]"Every vehicle has a name, and in Chinese, those names
tell you exactly what the vehicle does,"[/bold cyan] Long Long said,
counting the cars below. [bold cyan]"A bus is a 'public vehicle,'
a train is a 'fire vehicle,' an airplane is a 'flying machine.'
Learn the characters and the logic reveals itself."[/bold cyan]

[bold white]Let's learn essential transportation vocabulary![/bold white]
""",
    "buying_tickets": """
Long Long led you to a busy ticket hall where travelers queued
at windows and tapped on self-service machines. Numbers flashed
on overhead screens and announcements echoed off marble walls.

[bold cyan]"Before you board anything, you need a ticket,"[/bold cyan]
Long Long said, studying the price board. [bold cyan]"Piao.
That one word opens every journey. One-way or round trip?
How much? Which class? These are the words that get you
from here to there."[/bold cyan]

[bold white]Let's learn to buy tickets in Chinese![/bold white]
""",
    "asking_directions": """
Long Long landed at a crossroads where four streets met in a
tangle of signs, arrows, and painted lane markings. Pedestrians
hurried in every direction.

[bold cyan]"Even with a map, you'll sometimes need to ask a stranger
for help,"[/bold cyan] Long Long said, turning his head left and right.
[bold cyan]"Zuo, you, zhi zou -- left, right, straight ahead.
Zen me qu? Zai na li? These questions will save you every time
you're lost."[/bold cyan]

[bold white]Let's master asking and understanding directions![/bold white]
""",
    "at_the_station": """
Long Long walked through the cavernous hall of a train station,
past security checks, ticket gates, and glowing departure boards.
Escalators carried passengers up to platforms while subway signs
pointed underground.

[bold cyan]"Stations are worlds of their own,"[/bold cyan] Long Long said,
reading the signs overhead. [bold cyan]"Entrance, exit, transfer,
platform, next stop -- if you know these words, you can navigate
any station in China, from Beijing's massive railway hub to
a tiny village bus stop."[/bold cyan]

[bold white]Let's learn to navigate stations like a local![/bold white]
""",
    "travel_conversations": """
Long Long climbed into the back of a taxi and addressed the driver
with a respectful nod.

[bold cyan]"Now we put it all together -- real conversations with
real people,"[/bold cyan] Long Long said, leaning forward.
[bold cyan]"Telling the driver where to go, asking how far,
checking if you've arrived, being polite to strangers.
This is where vocabulary becomes communication."[/bold cyan]

[bold white]Let's practice real travel conversations![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "transportation_words": """
[bold green]Long Long roared with delight, rattling the windows of a passing bus![/bold green]

[bold cyan]"Gong gong qi che, di tie, chu zu che, huo che, fei ji --
you know every way to travel! The roads, rails, and skies
are yours to navigate."[/bold cyan]
""",
    "buying_tickets": """
[bold green]Long Long stamped the ground, making ticket machines rattle![/bold green]

[bold cyan]"Piao, dan cheng, wang fan, duo shao qian -- you can walk up
to any ticket counter in China and get exactly what you need.
No journey is beyond your reach now!"[/bold cyan]
""",
    "asking_directions": """
[bold green]Long Long twirled at the crossroads, his tail spinning like a compass needle![/bold green]

[bold cyan]"Zuo zhuan, you zhuan, zhi zou, zai na li -- you can find
your way anywhere! The streets of China hold no mystery
for you now."[/bold cyan]
""",
    "at_the_station": """
[bold green]Long Long slid down the escalator railing with a triumphant roar![/bold green]

[bold cyan]"Zhan, chu kou, ru kou, huan cheng, zhan tai -- you own
the station! From entrance to exit, from platform to transfer,
you can navigate it all."[/bold cyan]
""",
    "travel_conversations": """
[bold green]Long Long breathed a triumphant plume of golden fire across the city skyline![/bold green]

[bold cyan]"You've done it! Vehicles, tickets, directions, stations,
and real conversations -- all woven together. You can hail a taxi,
buy a train ticket, find your platform, and chat with the driver.
China is yours to explore!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "transportation_words": """
Long Long lined up model vehicles on a table: bus, subway, taxi, train, plane.

[bold cyan]"You've learned the names. Now prove you can use them
in a sentence -- tell me how you get to work, to the airport,
to anywhere!"[/bold cyan]
""",
    "buying_tickets": """
Long Long pushed you toward the ticket counter with a grin.

[bold cyan]"Time to buy a real ticket! One-way or round trip,
train or plane -- show me you can handle the transaction
all in Chinese!"[/bold cyan]
""",
    "asking_directions": """
Long Long blindfolded himself with his own wing.

[bold cyan]"I can't see a thing! Guide me with your directions.
Left, right, straight -- decode the instructions and
prove you won't get lost!"[/bold cyan]
""",
    "at_the_station": """
Long Long dropped you in the middle of a busy station with no map.

[bold cyan]"Entrances, exits, platforms, transfers -- the announcements
are all in Chinese. Listen carefully and show me you can
find your way!"[/bold cyan]
""",
    "travel_conversations": """
Long Long handed you a suitcase and pointed to a waiting taxi.

[bold cyan]"The ultimate test -- a real journey. Tell the driver
where to go, ask how long, check the fare, and arrive
at your destination. Speak Chinese like a traveler!"[/bold cyan]
""",
}
