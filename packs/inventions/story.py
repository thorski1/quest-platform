"""
story.py — Narrative for the Inventions & Technology skill pack.

Puck opens the Workshop of Wonders and guides the reader through
the greatest inventions in human history — from simple machines to
the technologies of tomorrow.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Workshop of Wonders[/bold yellow]

Puck appeared on a new page of the Primer, standing in front of
an enormous door made of brass gears, copper pipes, and tiny
blinking lights. A sign above it read:

[bold yellow]WORKSHOP OF WONDERS[/bold yellow]

[bold cyan]"Behind this door,"[/bold cyan] Puck said, eyes shining,
[bold cyan]"is every invention that ever changed the world.
The wheel. The light bulb. The computer. The rocket.
Every single one started the same way — with a curious person
who looked at a problem and said: [italic]I can fix that.[/italic]"[/bold cyan]

The girl reached for the door handle. It was warm to the touch.

[bold white]"Will I learn how things work?"[/bold white]

[bold cyan]"Everything."[/bold cyan] Puck grinned and pushed the door open.
Inside, golden gears turned, sparks drifted like fireflies,
and shelves stretched to the ceiling — covered in levers, bulbs,
magnets, tiny engines, and things she didn't have names for yet.

[bold cyan]"Simple machines. Great inventions. Computers. Rockets.
And the inventions that haven't been invented yet —
the ones that are waiting for someone exactly like you."[/bold cyan]

Puck hopped onto a workbench and spread both wings wide.

[bold cyan]"Ready to build something wonderful?"[/bold cyan]

[bold white]Your adventure through the Workshop of Wonders begins now.[/bold white]
"""

ZONE_INTROS = {
    "simple_machines": """
Puck led the way to the first workbench, where six gleaming tools
were laid out in a neat row: a lever, a wheel, a pulley, a ramp,
a screw, and a wedge.

[bold cyan]"These,"[/bold cyan] Puck said proudly, [bold cyan]"are the six simple machines.
They were invented thousands of years ago — and every machine
ever built, from a bicycle to a space shuttle, is made from
combinations of these six things."[/bold cyan]

Six golden labels glowed beneath each tool:
[bold yellow]Lever · Wheel & Axle · Pulley · Inclined Plane · Screw · Wedge[/bold yellow]

[bold cyan]"Simple doesn't mean boring. Simple means [italic]powerful.[/italic]"[/bold cyan]

[bold white]Let's discover how these six machines make the impossible possible![/bold white]
""",
    "great_inventions": """
Puck flew to a long hallway lined with glass cases, each one
glowing with its own light. Inside each case was a model of
an invention that changed the world.

[bold cyan]"The printing press,"[/bold cyan] Puck whispered, pointing.
[bold cyan]"The light bulb. The telephone. The airplane. The internet.
Each one was impossible — until someone made it possible."[/bold cyan]

Five golden plaques shone:
[bold yellow]Gutenberg · Edison · Bell · The Wrights · Berners-Lee[/bold yellow]

[bold cyan]"Behind every great invention is a person who refused to give up."[/bold cyan]

[bold white]Let's meet the inventors who changed everything![/bold white]
""",
    "how_things_work": """
Puck opened a door marked [bold yellow]HOW THINGS WORK[/bold yellow] and
inside was a room full of wires, magnets, batteries, gears,
and tiny light bulbs — all waiting to be connected.

[bold cyan]"This,"[/bold cyan] Puck said, [bold cyan]"is where we learn the science
behind the inventions. Electricity. Magnets. Circuits. Gears.
The invisible forces that make everything in the modern world
hum and glow and spin."[/bold cyan]

Sparks danced between two copper wires.

[bold cyan]"Don't worry — we'll start with the basics!"[/bold cyan]

[bold white]Let's discover the science inside every machine![/bold white]
""",
    "computers_basics": """
Puck tapped a glowing screen and it flickered to life, filling
with cascading green ones and zeros.

[bold cyan]"Computers,"[/bold cyan] Puck said, [bold cyan]"are the most powerful thinking
machines humans have ever built. But here's the secret —
they don't actually [italic]think.[/italic] They follow instructions.
Really, really, [italic]really[/italic] fast."[/bold cyan]

A tiny cursor blinked on the screen, waiting.

[bold cyan]"Input and output. Hardware and software. And underneath
it all — a language made of just two numbers: zero and one.
That's all a computer needs to do everything it does."[/bold cyan]

[bold white]Let's learn how the thinking machines really work![/bold white]
""",
    "transportation_history": """
Puck stood beside a long timeline painted on the workshop wall.
At one end was a horse. At the other end was a rocket.

[bold cyan]"For most of human history,"[/bold cyan] Puck said, [bold cyan]"the fastest thing
on land was a horse. Then, in just two hundred years — WHOOSH —
trains, cars, airplanes, rockets. Humans went from trotting
along muddy roads to walking on the Moon."[/bold cyan]

Five glowing models stood along the timeline:
[bold yellow]Horse · Steam Train · Automobile · Airplane · Rocket[/bold yellow]

[bold cyan]"Each one changed the world. Let's find out how."[/bold cyan]

[bold white]Let's race through the history of transportation![/bold white]
""",
    "communication_history": """
Puck cupped both hands around a tiny flame, then puffed —
a ring of smoke drifted upward.

[bold cyan]"That,"[/bold cyan] Puck said, [bold cyan]"is how messages used to be sent.
Smoke signals. Then letters carried by riders on horseback.
Then the telegraph — dots and dashes on a wire.
Then the telephone — a real voice, miles away.
Then the internet — everything, everywhere, instantly."[/bold cyan]

Six glowing icons appeared on the wall:
[bold yellow]Smoke · Letter · Telegraph · Telephone · Internet · Video Call[/bold yellow]

[bold cyan]"The story of communication is the story of people
who refused to be far apart."[/bold cyan]

[bold white]Let's follow the message from smoke to screen![/bold white]
""",
    "future_inventions": """
Puck pushed open the final door in the workshop — and beyond it
was not a room but an open sky, full of stars and glowing blueprints
floating in the air.

[bold cyan]"This,"[/bold cyan] Puck whispered, [bold cyan]"is the room that isn't finished yet.
The inventions of [italic]tomorrow.[/italic] Robots that help doctors.
Rockets that carry people to Mars. Energy from the sun and wind.
Machines that learn. Printers that build real objects from nothing."[/bold cyan]

Five shimmering outlines floated overhead:
[bold yellow]Robots · Space Travel · Renewable Energy · Artificial Intelligence · 3D Printing[/bold yellow]

[bold cyan]"And the most exciting part? The people who will build
these inventions are kids right now. Kids like [italic]you.[/italic]"[/bold cyan]

[bold white]Let's explore the inventions of tomorrow![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "simple_machines": """
[bold green]All six simple machines glow on the workbench![/bold green]

Lever, wheel, pulley, ramp, screw, wedge — each one understood,
each one a building block for everything that came after.

[bold cyan]"You know the six foundations,"[/bold cyan] Puck says proudly.
[bold cyan]"Every crane, every bicycle, every clock in the world
is made from combinations of these six machines.
Now you see them everywhere."[/bold cyan]

The Hall of Great Inventions beckons ahead...
""",
    "great_inventions": """
[bold green]Five glass cases blaze with golden light![/bold green]

The printing press, the light bulb, the telephone, the airplane,
the World Wide Web — each one a turning point in human history.

[bold cyan]"These inventors didn't give up,"[/bold cyan] Puck says.
[bold cyan]"Edison tried thousands of times before his light bulb worked.
The Wright Brothers were told humans would never fly.
Persistence. That's the real invention."[/bold cyan]

The HOW THINGS WORK room hums with electricity ahead...
""",
    "how_things_work": """
[bold green]Sparks fly and circuits glow across the workshop![/bold green]

Electricity, magnets, gears, batteries, circuits, conductors —
the invisible forces behind every modern machine, now understood.

[bold cyan]"You see the world differently now,"[/bold cyan] Puck says.
[bold cyan]"Every time you flip a light switch, you'll know
about electrons flowing through a circuit.
Every time you see a gear, you'll know which way it turns."[/bold cyan]

A glowing screen flickers to life. The computers are waiting...
""",
    "computers_basics": """
[bold green]The screen fills with cascading ones and zeros — and you can read them![/bold green]

Input, output, hardware, software, binary — the language of
the thinking machines is no longer a mystery.

[bold cyan]"Computers aren't magic,"[/bold cyan] Puck says with a grin.
[bold cyan]"They're incredibly fast instruction-followers.
And now you know how they work — from the outside
all the way down to the ones and zeros."[/bold cyan]

A timeline stretches across the wall. The history of transportation awaits...
""",
    "transportation_history": """
[bold green]Five models glow along the timeline — horse to rocket![/bold green]

In just two hundred years, humans went from horse-drawn carriages
to walking on the Moon. Each invention built on the last.

[bold cyan]"Speed changed everything,"[/bold cyan] Puck says.
[bold cyan]"Trains connected cities. Cars gave people freedom.
Planes shrank the world. Rockets opened the universe.
And it's still going — faster and farther, every year."[/bold cyan]

Smoke drifts in from the next room. The history of communication calls...
""",
    "communication_history": """
[bold green]Six icons blaze in a line — from smoke to screen![/bold green]

Smoke signals, letters, telegraph, telephone, internet, video calls —
the whole story of how humans learned to talk across any distance.

[bold cyan]"From a puff of smoke to a video call with someone
on the other side of the planet,"[/bold cyan] Puck says softly.
[bold cyan]"All because people kept asking: how can I reach
someone who's far away?"[/bold cyan]

The final door glows. Tomorrow's Workshop awaits...
""",
    "future_inventions": """
[bold green]The starry room blazes with light — every blueprint complete![/bold green]

Robots, space travel, renewable energy, AI, 3D printing —
the inventions of tomorrow, explored and understood.

[bold cyan]"You've done it,"[/bold cyan] Puck says, wings spread wide.
[bold cyan]"From the lever to artificial intelligence.
From the wheel to the rocket. From smoke signals to video calls.
The whole story of human invention — all of it yours."[/bold cyan]

Puck looks at you one more time.

[bold cyan]"And remember: every inventor started as a kid
with a question. Never stop asking."[/bold cyan]

[bold white]Tinkerer. Builder. Inventor. Visionary. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "simple_machines": "Puck picks up the last tool on the bench — a sharp, triangular blade. [bold yellow]\"This one is two simple machines in one! It's sharp, it splits things apart, and you use one every time you eat. What simple machine is it?\"[/bold yellow]",
    "great_inventions": "Puck stands before the brightest case in the hall — a web of glowing light connecting every corner of the room. [bold yellow]\"This invention was given away for free, so the whole world could use it. One person's generosity changed everything. Who was it?\"[/bold yellow]",
    "how_things_work": "Puck holds up two pieces of wire — one copper, one rubber. [bold yellow]\"One lets electricity through. One blocks it. The difference between these two materials keeps the whole world safe. Which is which — and what do we call them?\"[/bold yellow]",
    "computers_basics": "Puck lines up five tiny light switches — each one either ON or OFF. [bold yellow]\"If ON means 1 and OFF means 0, can you figure out what number these switches show? This is how computers count!\"[/bold yellow]",
    "transportation_history": "Puck places five tiny models in a row and mixes them up. [bold yellow]\"Horse, car, train, plane, rocket. Can you put them in the right order — from oldest to newest? The whole history of speed in one line!\"[/bold yellow]",
    "communication_history": "Puck holds a tiny screen showing a face waving hello. [bold yellow]\"From smoke in the sky to a face on a screen — thousands of years of invention led to this moment. What three things does a video call need to work?\"[/bold yellow]",
    "future_inventions": "Puck looks at you — not at a model or a screen, but directly at you. [bold yellow]\"Every invention ever made started the same way. Not with money. Not with a lab. With something much simpler — something every kid already has. What is it?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "machine_master": (
        "Machine Master",
        "Understood all six simple machines — the building blocks of every invention!",
    ),
    "invention_scholar": (
        "Invention Scholar",
        "Met the inventors who changed the world — from Gutenberg to Berners-Lee!",
    ),
    "circuit_builder": (
        "Circuit Builder",
        "Mastered electricity, magnets, gears, batteries, and circuits!",
    ),
    "digital_thinker": (
        "Digital Thinker",
        "Learned how computers work — from input/output to binary!",
    ),
    "speed_historian": (
        "Speed Historian",
        "Traced the history of transportation from horse to rocket!",
    ),
    "message_keeper": (
        "Message Keeper",
        "Followed the story of communication from smoke signals to video calls!",
    ),
    "future_visionary": (
        "Future Visionary",
        "Explored the inventions of tomorrow — robots, AI, and beyond!",
    ),
}
