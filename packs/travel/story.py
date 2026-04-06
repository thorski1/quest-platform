"""
story.py — Narrative for the Travel skill pack.

龙龙 (Lóng Lóng) guides the learner through essential travel Chinese —
transportation, directions, hotels, airports, sightseeing, and emergency
phrases for navigating China with confidence.
"""

INTRO_STORY = """
[bold yellow]LEARN CHINESE[/bold yellow]
[bold yellow]Chapter: Travel — 旅行[/bold yellow]

龙龙 descended from the clouds carrying a well-worn leather satchel
and a map covered in Chinese characters. The dragon landed on the
steps of Beijing Capital Airport, its eyes bright with excitement.

[bold cyan]"Travel!"[/bold cyan] 龙龙 declared. [bold cyan]"The greatest teacher
in the world. And China — with its bullet trains, ancient walls,
forbidden palaces, and bustling cities — is one of the greatest
places to explore."[/bold cyan]

The dragon unrolled its map, revealing routes crisscrossing the country.

[bold cyan]"But to really travel in China, you need more than a passport.
You need the words. How to take a train, ask for directions,
check into a hotel, find your way around an airport, visit the
Great Wall, and — hopefully you won't need this, but just in case —
ask for help in an emergency."[/bold cyan]

龙龙 slung its satchel over one wing.

[bold cyan]"Ready to explore? 出发吧! (Chūfā ba!) — Let's go!"[/bold cyan]

[bold white]Your journey across China begins now.[/bold white]
"""

ZONE_INTROS = {
    "transportation": """
龙龙 hovered above a highway, railway, subway entrance, and taxi stand.

[bold cyan]"China has some of the best transportation in the world,"[/bold cyan]
龙龙 said. [bold cyan]"The fastest trains. The biggest subway systems.
And in Chinese, you 'sit' on all of them — 坐飞机, 坐火车, 坐地铁.
One verb, many rides!"[/bold cyan]

[bold yellow]坐飞机 · 坐火车 · 坐地铁 · 打车 · 走路[/bold yellow]

[bold white]Let's learn how to get around![/bold white]
""",
    "directions": """
龙龙 pulled out a compass and held it up.

[bold cyan]"Left, right, front, back, and the four compass directions,"[/bold cyan]
龙龙 said. [bold cyan]"But here's something interesting — Chinese starts
from East (东), not North! 东南西北 — East, South, West, North.
The sun rises in the East, and so does Chinese geography."[/bold cyan]

[bold yellow]左 · 右 · 前 · 后 · 东南西北[/bold yellow]

[bold white]Let's find our way![/bold white]
""",
    "at_the_hotel": """
龙龙 pushed through the revolving door of a grand Chinese hotel.

[bold cyan]"After a long day of travel, you need a place to stay,"[/bold cyan]
龙龙 said. [bold cyan]"And in a Chinese hotel, you need to know
how to ask for your room, your key, the WiFi password,
and — eventually — how to check out."[/bold cyan]

[bold yellow]酒店 · 房间 · 钥匙 · 退房 · WiFi密码[/bold yellow]

[bold white]Let's check in![/bold white]
""",
    "asking_directions": """
龙龙 stood at a busy intersection in a Chinese city, looking both ways.

[bold cyan]"请问...怎么走?"[/bold cyan] 龙龙 practiced.
[bold cyan]"This is the magic phrase. Start with 请问 (excuse me),
add your destination, then 怎么走 (how do I get there).
People will point the way — and now you'll understand
when they say 左转, 右转, 一直走!"[/bold cyan]

[bold yellow]请问 · 怎么走 · 在哪里 · 远/近[/bold yellow]

[bold white]Let's ask for directions![/bold white]
""",
    "at_the_airport": """
龙龙 wheeled a suitcase through the airport departures hall.

[bold cyan]"Airports are stressful enough in your own language,"[/bold cyan]
龙龙 said. [bold cyan]"In a foreign country, they can be terrifying.
But not if you know the words: 护照, 登机牌, 行李, 海关.
These four words will get you through any Chinese airport."[/bold cyan]

[bold yellow]护照 · 登机牌 · 行李 · 海关[/bold yellow]

[bold white]Let's navigate the airport![/bold white]
""",
    "sightseeing": """
龙龙 soared over the Great Wall, the Forbidden City glittering in the distance.

[bold cyan]"China has 5,000 years of history,"[/bold cyan] 龙龙 said with pride.
[bold cyan]"The Great Wall. The Forbidden City. The Terracotta Warriors.
West Lake. And so much more. Let's learn the words you need
to visit these incredible places — and take the perfect photo!"[/bold cyan]

[bold yellow]长城 · 故宫 · 博物馆 · 拍照 · 门票[/bold yellow]

[bold white]Let's see the sights![/bold white]
""",
    "emergencies": """
龙龙 turned serious for a moment, its golden eyes steady.

[bold cyan]"I hope you never need these words,"[/bold cyan] 龙龙 said quietly.
[bold cyan]"But if you do, they could save your life. How to cry for help.
How to say you're lost. How to find a hospital, call the police,
or reach your embassy. Different numbers than back home —
110, 120, 119. Learn them now, just in case."[/bold cyan]

[bold yellow]救命! · 我迷路了 · 医院 · 报警[/bold yellow]

[bold white]Let's learn the words you need when things go wrong.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "transportation": """
[bold green]You can get around China — in Chinese![/bold green]

Planes, trains, subways, taxis, and your own two feet — all covered.

[bold cyan]"You learned the 坐 pattern,"[/bold cyan] 龙龙 says.
[bold cyan]"And the most useful travel question: 怎么去?
With these words, you can get anywhere in China."[/bold cyan]

Time to learn which way to go...
""",
    "directions": """
[bold green]Left, right, front, back, and all four compass points — mastered![/bold green]

东南西北 glow like a compass rose in the sky.

[bold cyan]"You know Chinese starts from East,"[/bold cyan] 龙龙 says.
[bold cyan]"And you can combine directions: 东北, 西南.
You'll never be lost — at least not for long!"[/bold cyan]

A hotel awaits. Let's check in...
""",
    "at_the_hotel": """
[bold green]Hotel vocabulary — complete![/bold green]

Check-in, room, key, WiFi, checkout — you're a pro.

[bold cyan]"The WiFi password question alone was worth the whole zone,"[/bold cyan]
龙龙 says with a grin. [bold cyan]"WiFi密码是什么?
— the most important question in modern travel!"[/bold cyan]

The city streets beckon. Time to ask for directions...
""",
    "asking_directions": """
[bold green]You can ask for and follow directions in Chinese![/bold green]

请问, 怎么走, 在哪里, 一直走, 左转, 右转 — all yours.

[bold cyan]"You just decoded a full set of Chinese directions,"[/bold cyan]
龙龙 says proudly. [bold cyan]"一直走, 到路口左转, 就在右边.
You understood every word. That's real progress!"[/bold cyan]

The airport awaits. Passport ready?
""",
    "at_the_airport": """
[bold green]Airport navigation — unlocked![/bold green]

Passport, boarding pass, luggage, customs — no more confusion.

[bold cyan]"You know the airport inside and out now,"[/bold cyan] 龙龙 says.
[bold cyan]"And you know China's emergency numbers too:
110, 120, 119. Different from back home — important to remember!"[/bold cyan]

The sights of China await...
""",
    "sightseeing": """
[bold green]China's greatest landmarks — explored![/bold green]

The Great Wall, the Forbidden City, museums, photos, tickets — all yours.

[bold cyan]"不到长城非好汉,"[/bold cyan] 龙龙 quotes.
[bold cyan]"And now you know what that means!
You can navigate China's most famous sites in Chinese."[/bold cyan]

One final zone remains — the one we hope you never need...
""",
    "emergencies": """
[bold green]Emergency phrases — learned and ready![/bold green]

救命, 我迷路了, 医院在哪里, 报警, 大使馆 — all memorized.

[bold cyan]"You're prepared for anything now,"[/bold cyan] 龙龙 says.
[bold cyan]"You can travel, navigate, sightsee, and handle
emergencies — all in Chinese. That's not just language learning.
That's real-world readiness."[/bold cyan]

[bold white]World traveler. Direction master. Emergency-ready explorer.
That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "transportation": "龙龙 stands at a crossroads with five paths. [bold yellow]\"怎么去? — the most useful travel question. Can you ask it?\"[/bold yellow]",
    "directions": "龙龙 draws a compass. [bold yellow]\"东北 — which two directions combine to make it? Chinese compass logic!\"[/bold yellow]",
    "at_the_hotel": "龙龙 can't get online. [bold yellow]\"WiFi密码是什么? — can you ask the most important modern travel question?\"[/bold yellow]",
    "asking_directions": "龙龙 reads out directions in Chinese. [bold yellow]\"一直走,到路口左转,就在右边 — can you follow these directions?\"[/bold yellow]",
    "at_the_airport": "A flight status board flashes red. [bold yellow]\"航班延误了! What just happened to your flight?\"[/bold yellow]",
    "sightseeing": "龙龙 points to four landmarks. [bold yellow]\"Three are real UNESCO sites. One is made up. Can you spot the fake?\"[/bold yellow]",
    "emergencies": "龙龙 holds up emergency numbers. [bold yellow]\"110, 120, 119 — do you know which number to call for what? This could save a life!\"[/bold yellow]",
}
