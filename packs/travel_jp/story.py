"""
story.py — Narrative for the Travel skill pack.

Sensei (先生) guides you through travel vocabulary for
transportation, directions, hotels, sightseeing, and emergencies.
"""

INTRO_STORY = """
[bold red]LEARN JAPANESE[/bold red]
[bold yellow]Chapter: Traveling in Japan[/bold yellow]

Sensei stood on the platform of Tokyo Station,
surrounded by the hum of bullet trains and announcement chimes.

[bold cyan]"Japan's transportation system is a marvel,"[/bold cyan] Sensei said.
[bold cyan]"But to navigate it, you need the right words.
でんしゃ (train), えき (station), きっぷ (ticket).
And when you get lost -- and you will -- you need to
ask for help, find your hotel, and handle the unexpected."[/bold cyan]

Sensei checked the departure board with practiced ease.

[bold cyan]"Whether you're riding the しんかんせん (bullet train),
checking into a りょかん (traditional inn), or asking
for directions on a quiet countryside road --
the right Japanese words make all the difference."[/bold cyan]

[bold white]Your journey through travel Japanese begins now.[/bold white]
"""

ZONE_INTROS = {
    "transportation": """
Sensei tapped an IC card on the station gate.

[bold cyan]"Japan runs on trains,"[/bold cyan] Sensei said.
[bold cyan]"でんしゃ (train), バス (bus), タクシー (taxi),
しんかんせん (bullet train). The system is perfect --
but only if you know how to use it."[/bold cyan]

[bold white]Let's learn transportation vocabulary![/bold white]
""",
    "directions": """
Sensei stood at a crossroads with no GPS signal.

[bold cyan]"When technology fails, language saves you,"[/bold cyan] Sensei said.
[bold cyan]"みぎ (right), ひだり (left), まっすぐ (straight ahead).
Asking and understanding directions is a survival skill."[/bold cyan]

[bold white]Let's learn to ask for and give directions![/bold white]
""",
    "hotel": """
Sensei walked into a ryokan lobby.

[bold cyan]"Whether it's a ホテル (hotel) or a りょかん (traditional inn),"[/bold cyan]
Sensei said, [bold cyan]"checking in, requesting things, and checking out
all require specific vocabulary. Let's prepare you."[/bold cyan]

[bold white]Let's learn hotel and accommodation vocabulary![/bold white]
""",
    "asking_help": """
Sensei looked around with a deliberately confused expression.

[bold cyan]"すみません、たすけてください -- excuse me, please help,"[/bold cyan]
Sensei said. [bold cyan]"Asking for help in Japanese is an art.
Be polite, be clear, and people will go out of their way
to assist you. Japan is famously helpful to lost travelers."[/bold cyan]

[bold white]Let's learn how to ask for help![/bold white]
""",
    "sightseeing": """
Sensei unfolded a map covered in temple and shrine symbols.

[bold cyan]"Japan is full of wonders to see,"[/bold cyan] Sensei said.
[bold cyan]"おてら (temples), じんじゃ (shrines), おしろ (castles).
Knowing what you're looking at makes the experience richer."[/bold cyan]

[bold white]Let's learn sightseeing vocabulary![/bold white]
""",
    "emergencies": """
Sensei's expression turned serious.

[bold cyan]"I hope you never need these words,"[/bold cyan] Sensei said.
[bold cyan]"But たすけて (help!), けいさつ (police), きゅうきゅうしゃ
(ambulance) -- these words could save your life.
Japan's emergency number is 110 for police, 119 for fire and ambulance."[/bold cyan]

[bold white]Let's learn emergency vocabulary![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "transportation": """
[bold green]Sensei stamped your rail pass![/bold green]

[bold cyan]"You can navigate Japan's trains, buses, and taxis now.
The whole country is open to you."[/bold cyan]
""",
    "directions": """
[bold green]Sensei pointed ahead with confidence![/bold green]

[bold cyan]"You'll never be truly lost in Japan now.
You can ask anyone for directions and understand the answer."[/bold cyan]
""",
    "hotel": """
[bold green]Sensei handed you a room key![/bold green]

[bold cyan]"Check-in, requests, check-out -- you're ready.
Any hotel or ryokan in Japan will feel like home."[/bold cyan]
""",
    "asking_help": """
[bold green]Sensei gave a reassuring nod![/bold green]

[bold cyan]"You know how to ask for help politely.
Japanese people are incredibly kind to those who try."[/bold cyan]
""",
    "sightseeing": """
[bold green]Sensei took a commemorative photo![/bold green]

[bold cyan]"Temples, shrines, castles -- you know them all.
You'll appreciate Japan's wonders on a deeper level now."[/bold cyan]
""",
    "emergencies": """
[bold green]Sensei exhaled with relief![/bold green]

[bold cyan]"You're prepared for the worst. Let's hope you never
need these words, but you'll be glad you learned them."[/bold cyan]
""",
}

BOSS_INTROS = {
    "transportation": """
Sensei pointed to a complex railway map.

[bold cyan]"Get from Tokyo Station to Kyoto.
Tell me what you need and how to get there."[/bold cyan]
""",
    "directions": """
Sensei blindfolded you (metaphorically).

[bold cyan]"You're lost near a station. Ask me for directions
to the nearest convenience store."[/bold cyan]
""",
    "hotel": """
Sensei played the role of a front desk clerk.

[bold cyan]"Check into this ryokan. Handle every step
from reservation to room request."[/bold cyan]
""",
    "asking_help": """
Sensei created a scenario where you need help.

[bold cyan]"You've lost your wallet. Ask a stranger for help.
Be polite, be clear, get the help you need."[/bold cyan]
""",
    "sightseeing": """
Sensei showed photos of famous Japanese landmarks.

[bold cyan]"Name these places. Tell me what they are
and the vocabulary that goes with them."[/bold cyan]
""",
    "emergencies": """
Sensei simulated an emergency scenario.

[bold cyan]"Something has gone wrong. What do you say?
Who do you call? Show me you're prepared."[/bold cyan]
""",
}
