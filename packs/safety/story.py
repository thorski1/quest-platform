"""
story.py — Narrative for the Safety & First Aid skill pack.

Puck opens the Primer's Shield of Safety and guides the reader through
home safety, road smarts, water rules, stranger awareness, internet
safety, basic first aid, and emergency preparedness.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Shield of Safety[/bold yellow]

The Primer's pages rustled on their own, and when they settled,
something new had appeared: a glowing shield, no bigger than Puck's
outstretched wings, hovering in the center of the page. It shimmered
silver and gold, and tiny symbols danced across its surface — a flame,
a road, a wave, a key, a bandaid, and three bright numbers: 9-1-1.

[bold cyan]"A shield!"[/bold cyan] Puck announced, landing on its rim.
[bold cyan]"Not the kind knights carry into battle — though it IS
just as important. This is the Shield of Safety."[/bold cyan]

The girl traced its edge with a finger. [bold white]"What does it protect?"[/bold white]

[bold cyan]"You,"[/bold cyan] Puck said simply. [bold cyan]"It protects you.
Because knowing what to do — in a fire, on the road, in the water,
with strangers, online, when someone is hurt — that knowledge
is the strongest shield anyone can carry."[/bold cyan]

The shield pulsed with warm light.

[bold cyan]"You can't always stop bad things from happening,"[/bold cyan]
Puck said gently. [bold cyan]"But you CAN learn what to do when they do.
And that — "[/bold cyan] Puck tapped the shield, [bold cyan]"can save a life.
Maybe even your own."[/bold cyan]

[bold white]The Primer opens its Shield of Safety — because knowing
what to do can save a life![/bold white]
"""

ZONE_INTROS = {
    "home_safety": """
Puck flew to the first symbol on the shield — a small orange flame.

[bold cyan]"Home,"[/bold cyan] Puck said. [bold cyan]"The place where you feel safest.
But even at home, there are things that can hurt you if you don't
know the rules. Fire. Electricity. Sharp things. Cleaning bottles
that look like juice but aren't."[/bold cyan]

The flame flickered gently on the page.

[bold cyan]"The good news? Every one of these dangers has a simple rule
that keeps you safe. Learn the rules, and your home stays
the safe place it's supposed to be."[/bold cyan]

[bold white]Let's make your home the safest place in the world![/bold white]
""",
    "road_safety": """
Puck hopped to the second symbol — a little road stretching into the distance.

[bold cyan]"Streets and roads,"[/bold cyan] Puck said. [bold cyan]"Cars, bikes, buses,
crosswalks. Every day you share the world with vehicles that are
bigger, faster, and heavier than you."[/bold cyan]

Tiny cars zipped across the page.

[bold cyan]"But here's the thing — drivers follow rules, and so can you.
When you know the rules of the road, you and the cars can share
the world safely."[/bold cyan]

[bold white]Let's learn the street smarts that keep you safe![/bold white]
""",
    "water_safety": """
Puck glided to the third symbol — a shimmering blue wave.

[bold cyan]"Water,"[/bold cyan] Puck said softly. [bold cyan]"Beautiful, fun,
and powerful. Swimming pools, lakes, rivers, the ocean — they're
wonderful places. But water demands respect."[/bold cyan]

A gentle wave rolled across the bottom of the page.

[bold cyan]"The rules of water safety are simple, and every single one
of them exists because water doesn't give second chances.
Learn them well."[/bold cyan]

[bold white]Let's learn to respect the water![/bold white]
""",
    "stranger_safety": """
Puck settled on the fourth symbol — a circle with small figures inside.

[bold cyan]"People,"[/bold cyan] Puck said carefully. [bold cyan]"Most people
in the world are kind and good. But not everyone is.
And since you can't always tell the difference by looking,
you need to know who to trust — and what to do when
something doesn't feel right."[/bold cyan]

The circle glowed warm and steady.

[bold cyan]"This isn't about being scared of everyone. It's about
being smart. And smart is the best kind of brave."[/bold cyan]

[bold white]Let's learn who to trust and how to stay safe![/bold white]
""",
    "internet_safety": """
Puck flew to the fifth symbol — a glowing key.

[bold cyan]"The internet,"[/bold cyan] Puck said. [bold cyan]"A whole world
inside a screen. You can learn anything, talk to friends,
play games, watch videos. But just like the real world,
the digital world has rules that keep you safe."[/bold cyan]

A tiny screen flickered on the page.

[bold cyan]"Behind every screen name is a real person — and you can't
always tell if they're who they say they are. Your personal
information is precious. Guard it like treasure."[/bold cyan]

[bold white]Let's learn to be safe in the digital world![/bold white]
""",
    "basic_first_aid": """
Puck landed beside the sixth symbol — a small white bandaid with a red cross.

[bold cyan]"First aid,"[/bold cyan] Puck said proudly. [bold cyan]"The healer's art.
When someone gets a cut, a bump, a burn, or a sting —
you don't have to stand there feeling helpless.
You can actually DO something."[/bold cyan]

A tiny first aid kit opened on the page, its contents glowing.

[bold cyan]"You won't be doing surgery,"[/bold cyan] Puck added with a grin.
[bold cyan]"But you WILL learn the basics — and sometimes the basics
are all it takes."[/bold cyan]

[bold white]Let's open the healer's handbook![/bold white]
""",
    "emergency_numbers": """
Puck flew to the final symbol on the shield — three bright numbers: 9-1-1.

[bold cyan]"This,"[/bold cyan] Puck said solemnly, [bold cyan]"is the most important
lesson in the whole shield. Three numbers that bring help
running — police, firefighters, paramedics.
Nine. One. One."[/bold cyan]

The numbers glowed steady and strong.

[bold cyan]"But calling 911 isn't just about dialing. It's about knowing
WHEN to call, WHAT to say, and how to stay calm when your
heart is racing. That's what makes you a real hero."[/bold cyan]

[bold white]Let's learn the lesson that could save someone's life![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "home_safety": """
[bold green]The flame on the shield burns steady and safe![/bold green]

Fire escape plans, poison awareness, electrical safety, sharp objects —
every danger in the home now has a rule to match it.

[bold cyan]"Your home is safer now,"[/bold cyan] Puck says warmly,
[bold cyan]"because YOU are smarter. That's how safety works —
knowledge is the best protection of all."[/bold cyan]

The road stretches ahead on the shield. Street smarts are next...
""",
    "road_safety": """
[bold green]The road on the shield glows with safe, steady light![/bold green]

Looking both ways, crosswalks, helmets, seatbelts, bus safety,
being visible at night — the rules of the road are yours.

[bold cyan]"Cars are big and fast,"[/bold cyan] Puck says,
[bold cyan]"but you're smart. And smart beats fast every time."[/bold cyan]

A blue wave ripples on the shield. The water is calling...
""",
    "water_safety": """
[bold green]The wave on the shield sparkles calm and clear![/bold green]

The buddy system, pool rules, life jackets, rip currents,
checking depth before diving — you respect the water now.

[bold cyan]"Water is wonderful,"[/bold cyan] Puck says, [bold cyan]"and now you know
how to enjoy it safely. That's the whole point —
safety doesn't mean missing out. It means coming home."[/bold cyan]

The circle of trust glows warmly on the shield...
""",
    "stranger_safety": """
[bold green]The safety circle on the shield burns bright![/bold green]

Trusted adults, saying no, safe places, calling 911,
recognising tricks — your instincts are sharper than ever.

[bold cyan]"Most people are good,"[/bold cyan] Puck says softly.
[bold cyan]"But you don't have to figure that out alone.
Your trusted adults are there to help. Always tell them."[/bold cyan]

A glowing key appears on the shield. The digital world awaits...
""",
    "internet_safety": """
[bold green]The digital key on the shield shines with confidence![/bold green]

Private information, strong passwords, cyberbullying, online strangers,
knowing when to tell a parent — the digital world is yours to explore safely.

[bold cyan]"The internet is amazing,"[/bold cyan] Puck says.
[bold cyan]"And now you know how to enjoy it without giving
away the things that matter most: your safety and your privacy."[/bold cyan]

A tiny first aid kit appears on the shield. The healer's training begins...
""",
    "basic_first_aid": """
[bold green]The bandaid on the shield glows with healing light![/bold green]

Cuts, bumps, nosebleeds, bee stings, burns — you know what to do
for each one, and you know when to get an adult.

[bold cyan]"You're a healer now,"[/bold cyan] Puck says proudly.
[bold cyan]"Not a doctor, not yet — but someone who can help
when it matters. That's a beautiful thing to be."[/bold cyan]

Three numbers glow on the shield: 9-1-1. The final lesson awaits...
""",
    "emergency_numbers": """
[bold green]The three numbers blaze: 9-1-1![/bold green]

What 911 is, when to call, what to say, staying calm,
knowing your address, the phone that always works —
the final and most important lesson is complete.

[bold cyan]"You've done it,"[/bold cyan] Puck whispers. [bold cyan]"Every symbol
on the shield is lit. Home, road, water, people, internet,
first aid, emergencies — you know them all."[/bold cyan]

Puck places a hand on the glowing shield.

[bold cyan]"This shield isn't made of metal or magic.
It's made of knowledge. And it will protect you
for the rest of your life."[/bold cyan]

[bold white]Safety Hero. Shield Bearer. Life Saver. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "home_safety": "Puck unrolls a glowing map of a house with arrows pointing to every door and window. [bold yellow]\"The best time to plan for a fire is BEFORE it happens. Do you know the most important thing every family should practice?\"[/bold yellow]",
    "road_safety": "The sun dips low on the page and the sky goes dark. Puck's wings catch the last light. [bold yellow]\"When the sun goes down, drivers can barely see you. What's the one thing that makes the biggest difference?\"[/bold yellow]",
    "water_safety": "Puck peers over the edge of a rocky cliff into water far below. [bold yellow]\"It looks deep from up here — but looks can be deceiving. What's the rule every diver must follow?\"[/bold yellow]",
    "stranger_safety": "Puck's expression turns serious. A stranger on the page is waving and calling out. [bold yellow]\"This person says they know your mom and something bad happened. Your heart is racing. What do you do?\"[/bold yellow]",
    "internet_safety": "A message flashes on a screen: 'Something scary appeared.' Puck stands beside it calmly. [bold yellow]\"You see something online that makes your stomach turn. What's the very first thing you should do?\"[/bold yellow]",
    "basic_first_aid": "Steam rises from a hot pan on the page. Puck winces. [bold yellow]\"A burn! It hurts! Some people say butter, some say toothpaste — but what does REAL first aid say?\"[/bold yellow]",
    "emergency_numbers": "Puck holds up a locked phone. The screen shows only one button: Emergency. [bold yellow]\"The phone is locked and there's no time for passwords. Can you still call for help?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "home_guardian": (
        "Home Guardian",
        "Mastered fire safety, poison awareness, electrical safety, and sharp object rules!",
    ),
    "street_scholar": (
        "Street Scholar",
        "Learned every rule of the road — crosswalks, helmets, seatbelts, and more!",
    ),
    "water_wise": (
        "Water Wise",
        "Learned to respect the water and swim safely every time!",
    ),
    "trust_keeper": (
        "Trust Keeper",
        "Learned who to trust, how to say no, and when to tell an adult!",
    ),
    "digital_defender": (
        "Digital Defender",
        "Mastered the rules of online safety and privacy!",
    ),
    "young_healer": (
        "Young Healer",
        "Learned first aid for cuts, bumps, burns, stings, and nosebleeds!",
    ),
    "emergency_ready": (
        "Emergency Ready",
        "Knows when and how to call 911, and what to say when seconds count!",
    ),
}
