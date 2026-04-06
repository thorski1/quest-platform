"""
story.py — Narrative for the Famous People & Biographies skill pack.

The Primer opens its Hall of Heroes — meet the people who changed the world!
Puck guides the reader through galleries of scientists, inventors, leaders,
artists, explorers, athletes, and modern heroes.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Hall of Heroes[/bold yellow]

Puck appeared at the top of the page, standing before an enormous pair
of golden doors. Letters carved into the stone above them read:
[bold yellow]THE HALL OF HEROES[/bold yellow]

[bold cyan]"Behind these doors,"[/bold cyan] Puck said softly,
[bold cyan]"are the people who changed the world.
Scientists who unlocked the secrets of the universe.
Inventors who built things nobody thought possible.
Leaders who stood up when everyone else sat down.
Artists who made the world more beautiful.
Explorers who went where no one had gone before.
Athletes who showed what the human body can do.
And heroes alive right now, still changing things."[/bold cyan]

The girl reached for the doors. [bold white]"Can I meet them?"[/bold white]

[bold cyan]"Every single one."[/bold cyan] Puck smiled.
[bold cyan]"And by the time we're done, you'll know their names,
their stories, and the one great thing each of them
gave to the world."[/bold cyan]

The golden doors swung open. Inside, portraits lined the walls
as far as the eye could see — each one glowing, each one waiting
to tell its story.

[bold cyan]"Ready to meet some heroes?"[/bold cyan]

[bold white]Your journey through the Hall of Heroes begins now.[/bold white]
"""

ZONE_INTROS = {
    "scientists": """
Puck flew into the first gallery. The walls were covered in equations,
star charts, and drawings of atoms.

[bold cyan]"Scientists,"[/bold cyan] Puck said, eyes shining,
[bold cyan]"are the people who ask 'why?' and then spend their whole
lives finding the answer. Why does an apple fall down?
Why do stars shine? What are we made of?
These five asked the biggest questions — and found the answers."[/bold cyan]

Five portraits glowed on the wall:
[bold yellow]Einstein · Curie · Newton · Goodall · deGrasse Tyson[/bold yellow]

[bold white]Let's meet the scientists![/bold white]
""",
    "inventors": """
Puck pushed open a heavy door into a workshop full of sparks and gears.

[bold cyan]"Inventors,"[/bold cyan] Puck said, dodging a tiny spark,
[bold cyan]"don't just understand the world — they build new parts of it.
The light bulb. The telephone. The aeroplane. The computer.
Every one of these started as an idea in someone's head."[/bold cyan]

Five workbenches glowed, each with a different invention:
[bold yellow]Edison · Tesla · Bell · The Wright Brothers · Lovelace[/bold yellow]

[bold white]Let's meet the inventors![/bold white]
""",
    "leaders": """
Puck entered a grand hall with tall windows and flags from every nation.

[bold cyan]"Leaders,"[/bold cyan] Puck said quietly,
[bold cyan]"are the people who stood up and said 'this isn't right'
when everyone else was too afraid. They marched. They spoke.
They went to prison. Some were children when they started.
And they changed the world — not with inventions,
but with words and courage."[/bold cyan]

Five flags rippled in an unseen breeze:
[bold yellow]King · Mandela · Malala · Lincoln · Gandhi[/bold yellow]

[bold white]Let's meet the leaders![/bold white]
""",
    "artists": """
Puck floated into a gallery alive with colour, music, and poetry.

[bold cyan]"Artists,"[/bold cyan] Puck whispered,
[bold cyan]"show us what it means to be human.
A painting that makes you feel something you can't name.
A symphony that makes you cry. A poem that says exactly
what you always felt but couldn't put into words.
These five changed what art could be."[/bold cyan]

Five easels, a piano, and a quill pen glowed softly:
[bold yellow]da Vinci · Kahlo · Beethoven · Shakespeare · Angelou[/bold yellow]

[bold white]Let's meet the artists![/bold white]
""",
    "explorers": """
Puck stood at the prow of a tiny glowing ship, wind in its wings.

[bold cyan]"Explorers,"[/bold cyan] Puck called over the wind,
[bold cyan]"are the ones who looked at the edge of the map
and said 'what's out there?' They sailed unknown oceans.
They flew across continents. They walked on the Moon.
They dove to the bottom of the sea."[/bold cyan]

Five paths glowed across a map of the world — and beyond:
[bold yellow]Columbus · Earhart · Armstrong · Cousteau · Jemison[/bold yellow]

[bold white]Let's meet the explorers![/bold white]
""",
    "athletes": """
Puck landed on a golden medal, beaming.

[bold cyan]"Athletes,"[/bold cyan] Puck said,
[bold cyan]"show us what the human body can do when someone trains
and trains and never gives up. They run faster, jump higher,
fight harder — and sometimes, they change the world
just by stepping onto the field."[/bold cyan]

Five Olympic torches blazed:
[bold yellow]Ali · Williams · Owens · Biles · Pelé[/bold yellow]

[bold white]Let's meet the athletes![/bold white]
""",
    "modern_heroes": """
Puck opened the final gallery — and instead of old portraits,
the walls were covered with screens, solar panels, and living trees.

[bold cyan]"These heroes,"[/bold cyan] Puck said,
[bold cyan]"are alive right now. Some are young — one of them
started when she was only fifteen! They're fighting climate change,
building rockets, inventing the internet, making beautiful films,
and planting millions of trees."[/bold cyan]

Five glowing screens lit up:
[bold yellow]Thunberg · Musk · Berners-Lee · Miyazaki · Maathai[/bold yellow]

[bold white]Let's meet today's heroes![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "scientists": """
[bold green]All five scientist portraits glow with golden light![/bold green]

Einstein, Curie, Newton, Goodall, deGrasse Tyson —
each one shining, each story known.

[bold cyan]"You've met the people who asked 'why?'"[/bold cyan] Puck says proudly.
[bold cyan]"And now you know what they discovered.
The universe makes a little more sense, doesn't it?"[/bold cyan]

Sparks and gears glimmer ahead. The inventors are waiting...
""",
    "inventors": """
[bold green]Five workbenches blaze with light — every invention understood![/bold green]

Light bulbs, alternating current, telephones, aeroplanes, and the
very first computer program — all of them born from a single idea.

[bold cyan]"Ideas change the world,"[/bold cyan] Puck says.
[bold cyan]"And now you know the people who proved it."[/bold cyan]

A grand hall with tall windows beckons. The leaders are waiting...
""",
    "leaders": """
[bold green]Five flags wave proudly — every leader's story known![/bold green]

King's dream. Mandela's long walk. Malala's voice. Lincoln's
proclamation. Gandhi's peaceful march.

[bold cyan]"Courage,"[/bold cyan] Puck says softly,
[bold cyan]"isn't the absence of fear. It's doing what's right
even when you're terrified. These five proved that."[/bold cyan]

Colour and music spill from the next gallery. The artists are waiting...
""",
    "artists": """
[bold green]The gallery blazes with colour, music, and poetry![/bold green]

The Mona Lisa smiles. Frida's flowers bloom. Beethoven's
Fifth thunders. Shakespeare's words dance. Maya's caged bird sings.

[bold cyan]"Art,"[/bold cyan] Puck says, [bold cyan]"is how we tell each other
what it feels like to be alive. And these five
did it better than almost anyone."[/bold cyan]

A ship's prow appears through the mist. The explorers are waiting...
""",
    "explorers": """
[bold green]Five paths glow across the map — every journey complete![/bold green]

Across oceans, through the sky, to the Moon, under the sea,
and into orbit — every frontier explored.

[bold cyan]"They went first,"[/bold cyan] Puck says,
[bold cyan]"so the rest of us could follow.
That's what explorers do."[/bold cyan]

A golden medal gleams ahead. The athletes are waiting...
""",
    "athletes": """
[bold green]Five Olympic torches blaze — every champion celebrated![/bold green]

Ali floats like a butterfly. Serena serves an ace. Jesse
outruns hatred. Simone defies gravity. Pelé scores the beautiful goal.

[bold cyan]"Sports,"[/bold cyan] Puck says, [bold cyan]"aren't just about winning.
They're about showing what's possible when you never give up."[/bold cyan]

Screens and solar panels glow ahead. The modern heroes are waiting...
""",
    "modern_heroes": """
[bold green]Every screen glows — all the modern heroes are known![/bold green]

Climate strikes, rocket launches, the World Wide Web,
animated masterpieces, and thirty million trees.

[bold cyan]"These heroes are still going,"[/bold cyan] Puck says.
[bold cyan]"Their stories aren't finished yet.
And yours? Yours is just beginning."[/bold cyan]

Puck looks at you warmly.

[bold white]Fan. Student. Scholar. Historian. Biographer. Legend.[/bold white]
[bold white]That's who you've become.[/bold white]
""",
}

BOSS_INTROS = {
    "scientists": "Puck points to a portrait of a woman holding a glowing vial. [bold yellow]\"She won not one but TWO Nobel Prizes — in two different sciences! Almost nobody has ever done that. Do you know who she is?\"[/bold yellow]",
    "inventors": "Puck holds up a tiny glowing card covered in strange symbols. [bold yellow]\"Long before computers existed, one brilliant woman wrote the very first computer program. Who was she?\"[/bold yellow]",
    "leaders": "Puck stands before a portrait of a young girl holding a book like a shield. [bold yellow]\"She was shot for going to school — and she stood right back up and kept fighting for every child's right to learn. Who is she?\"[/bold yellow]",
    "artists": "Puck points to a painting so famous that millions of people travel to see it every year. [bold yellow]\"He painted the Mona Lisa, designed flying machines, and studied the human body — all five hundred years ago. Who was this genius?\"[/bold yellow]",
    "explorers": "Puck floats beside a glowing footprint on grey dust. [bold yellow]\"One small step for man, one giant leap for mankind. Who left this footprint on the Moon?\"[/bold yellow]",
    "athletes": "Puck stands beside a tiny figure mid-flip in the air. [bold yellow]\"She's considered the greatest gymnast of all time, with moves so difficult they're named after her. Who is she?\"[/bold yellow]",
    "modern_heroes": "Puck points to a photograph of a girl with braids standing alone outside a parliament building. [bold yellow]\"She was only fifteen when she started a movement that spread to every country on Earth. Who is she?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "science_star": (
        "Science Star",
        "Met the scientists who unlocked the secrets of the universe!",
    ),
    "invention_spark": (
        "Invention Spark",
        "Discovered the inventors who built the modern world!",
    ),
    "voice_of_change": (
        "Voice of Change",
        "Learned about leaders who fought for justice and freedom!",
    ),
    "creative_soul": (
        "Creative Soul",
        "Explored the artists who filled the world with beauty!",
    ),
    "trailblazer": (
        "Trailblazer",
        "Followed the explorers who ventured into the unknown!",
    ),
    "champion_spirit": (
        "Champion Spirit",
        "Celebrated the athletes who showed what the human body can do!",
    ),
    "future_maker": (
        "Future Maker",
        "Met the modern heroes shaping tomorrow's world!",
    ),
}
