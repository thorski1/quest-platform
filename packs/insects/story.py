"""
story.py — Narrative for the Bug Safari skill pack.

Puck opens the Primer to a world smaller than a fingertip — where
six-legged engineers build cities, spinning architects weave silk
cathedrals, and tiny wings carry the weight of the whole world.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Bug Safari[/bold yellow]

The Primer's pages began to hum — a low, buzzing vibration, as if
something very small and very alive was moving inside.

The girl leaned closer. The paper shimmered, and then she saw them:
a line of ants carrying a crumb of gilded ink... a butterfly unfolding
wings made of pure colour... a beetle with a shell like polished copper.

[bold cyan]"Insects!"[/bold cyan] Puck burst through the page in a shower of
tiny golden sparks, wings beating so fast they blurred.
[bold cyan]"The smallest creatures with the biggest job in the
whole world. They pollinate the flowers. They feed the birds.
They recycle everything that falls. Without them —"[/bold cyan]
Puck paused for dramatic effect.
[bold cyan]"— the whole world stops."[/bold cyan]

A dragonfly the size of a comma darted across the margin.
A ladybug climbed the letter 'I.'

[bold white]"How many are there?"[/bold white] the girl asked.

[bold cyan]"More than every person, every bird, every fish,
every mammal put together. More than you could count
if you counted every second for a thousand years."[/bold cyan]

Puck landed on a flower drawn in the margin, and a bee
immediately buzzed over to investigate.

[bold cyan]"Six legs. Three body parts. An armour-plated skeleton
on the outside. That's the recipe. And with that recipe,
nature built a million different species — and probably
millions more we haven't found yet."[/bold cyan]

A tiny magnifying glass appeared on the next page, glowing gold.

[bold cyan]"Ready to look closer?"[/bold cyan]

[bold white]Your safari through the insect world begins now.[/bold white]
"""

ZONE_INTROS = {
    "what_makes_an_insect": """
Puck pulled a magnifying glass from behind a comma and held it up.
The page exploded with detail — a single ant grew until every joint,
every hair, every segment was visible.

[bold cyan]"Rule number one,"[/bold cyan] Puck said, tapping the ant's legs.
[bold cyan]"Six legs. Always six. Not four, not eight — six.
Three on each side, neat as anything."[/bold cyan]

Puck drew three dotted lines across the ant's body.

[bold cyan]"Rule number two: three body parts. Head up front —
that's where the eyes and antennae live. Thorax in the middle —
that's where the legs attach. Abdomen at the back —
that's the engine room."[/bold cyan]

Puck knocked on the beetle's shell.

[bold cyan]"And rule number three: an exoskeleton. No bones inside —
instead, a hard shell on the outside. Like wearing your
skeleton as a suit of armour."[/bold cyan]

Three golden words appeared on the page:
[bold yellow]Six Legs · Three Parts · Exoskeleton[/bold yellow]

[bold cyan]"Learn the rules, and you'll never confuse an insect
with anything else. Ready?"[/bold cyan]

[bold white]Let's discover what makes an insect an insect![/bold white]
""",
    "butterflies_and_moths": """
The page turned, and the whole world filled with wings.

Hundreds of butterflies rose from the paper like confetti — monarchs
in orange, swallowtails in yellow, morphos in impossible blue.
Between them, softer shapes drifted: moths with feathered antennae
and wings dusted in silver.

[bold cyan]"Butterflies and moths,"[/bold cyan] Puck whispered, floating
among them. [bold cyan]"The artists of the insect world. But here's
the real magic — every single one of them started life as
something completely different."[/bold cyan]

Four golden stages appeared in a circle:
[bold yellow]Egg → Caterpillar → Chrysalis → Butterfly[/bold yellow]

[bold cyan]"A caterpillar goes into a chrysalis as a crawling,
munching tube... and comes out with wings. It completely
rebuilds its body from the inside out. If that's not magic,
I don't know what is."[/bold cyan]

[bold white]Let's follow the transformation![/bold white]
""",
    "ants_and_bees": """
The page split in two. On the left, a network of tunnels burrowed
deep underground — an ant colony, bustling with millions of workers.
On the right, a golden honeycomb glowed with warmth and sweetness —
a beehive, humming with purpose.

[bold cyan]"Ants and bees,"[/bold cyan] Puck said reverently.
[bold cyan]"The civilisation builders. They don't just live together —
they build cities. They have queens and workers and soldiers.
They communicate, cooperate, and solve problems that
no single insect could handle alone."[/bold cyan]

Golden labels appeared:
[bold yellow]Queens · Workers · Soldiers · Colonies[/bold yellow]

[bold cyan]"An ant colony can have millions of members.
A beehive makes honey that never spoils. And without bees
carrying pollen from flower to flower, most of the food
in your kitchen would vanish."[/bold cyan]

Puck looked at both civilisations with admiration.

[bold cyan]"Tiny insects. Giant achievements."[/bold cyan]

[bold white]Let's explore the world of colonies![/bold white]
""",
    "creepy_crawlies": """
The page darkened. The edges curled like shadows. Something skittered
in the margin — eight legs, fast and silent.

[bold cyan]"Now,"[/bold cyan] Puck said, landing on a web that stretched
across the gutter of the book, [bold cyan]"we meet the creatures
that people call 'creepy.' Spiders — which are NOT insects,
by the way. Beetles with horns. Dragonflies older than
dinosaurs. Mantises that strike faster than you can blink."[/bold cyan]

A jewel-bright beetle trundled past. A dragonfly hovered overhead.
A praying mantis held perfectly still, watching.

[bold cyan]"Some of them look a bit scary. But once you understand them —
once you know what they do and how they work — 'creepy'
turns into 'incredible.' I promise."[/bold cyan]

Golden words appeared:
[bold yellow]Spiders · Beetles · Dragonflies · Mantises · Fireflies[/bold yellow]

[bold white]Let's meet the creepy crawlies — and discover they're not so creepy after all![/bold white]
""",
    "insects_and_environment": """
The final chapter opened, and the page became the whole world.

Green forests. Golden fields of wheat. Orchards heavy with fruit.
Rivers running clean. Soil dark and rich. And everywhere — tiny,
busy, six-legged shapes, holding it all together.

[bold cyan]"This,"[/bold cyan] Puck said, and there was something serious
in those bright eyes, [bold cyan]"is the most important chapter.
Because insects aren't just interesting — they're essential.
They pollinate the flowers that become the food you eat.
They break down dead things and return the nutrients to the soil.
They feed the birds and the frogs and the fish."[/bold cyan]

Puck's wings dimmed for a moment.

[bold cyan]"And right now, insect numbers are falling. Habitats
are disappearing. Pesticides are poisoning them. But it's
not too late — and you can help."[/bold cyan]

Golden threads appeared, connecting insects to every living thing
on the page.

[bold cyan]"Small creatures. Big responsibility. Let's understand
why they matter."[/bold cyan]

[bold white]Let's discover how insects power the planet![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "what_makes_an_insect": """
[bold green]Three golden rules glow on the page — mastered![/bold green]

Six legs. Three body parts. Exoskeleton. The insect blueprint,
clear as day.

[bold cyan]"You've got it,"[/bold cyan] Puck says proudly.
[bold cyan]"From now on, you'll never look at a bug and wonder
'is that an insect?' You'll KNOW. Six legs? Three parts?
Hard shell on the outside? Insect. Every time."[/bold cyan]

The page turns to a world of colour and wings. The butterflies are waiting...
""",
    "butterflies_and_moths": """
[bold green]A butterfly unfolds its wings across the whole page — brilliant and complete![/bold green]

Egg to caterpillar to chrysalis to butterfly. The whole
miraculous transformation, understood from start to finish.

[bold cyan]"Metamorphosis,"[/bold cyan] Puck whispers with a smile.
[bold cyan]"The most beautiful word in science. A creature that
completely rebuilds itself — and emerges with wings.
Now you know how it works."[/bold cyan]

The page fills with bustling tunnels and golden honeycombs.
The colonies are calling...
""",
    "ants_and_bees": """
[bold green]An ant colony and a beehive glow side by side — two great civilisations![/bold green]

Queens and workers and dancers and builders. Millions of tiny
individuals working as one. Honey that never spoils. Pollen
carried from flower to flower.

[bold cyan]"They're tiny,"[/bold cyan] Puck says with admiration,
[bold cyan]"but they built something we can barely comprehend.
Cities underground. Factories of honey. Communication through
dance. No single insect could do it alone — but together,
they change the world."[/bold cyan]

Shadows move on the next page. The creepy crawlies are stirring...
""",
    "creepy_crawlies": """
[bold green]A gallery of incredible creatures fills the page — spiders, beetles, dragonflies, and more![/bold green]

Eight-legged web spinners. Horned beetles. Ancient dragonflies.
Patient mantises. Glowing fireflies in the dark.

[bold cyan]"Still think they're creepy?"[/bold cyan] Puck grins.
[bold cyan]"A spider's silk is stronger than steel. A dragonfly
catches 95% of everything it chases. A firefly makes its
own light. These aren't creepy — they're extraordinary."[/bold cyan]

The page opens wide. The whole world appears, held together
by tiny wings and legs. The final chapter awaits...
""",
    "insects_and_environment": """
[bold green]The web of life glows across the page — every thread connected, every insect essential![/bold green]

Pollination. Decomposition. Food chains. Soil health.
The invisible machinery of the living world, powered by
the smallest engineers on Earth.

[bold cyan]"You did it."[/bold cyan] Puck's wings spread wide, glowing
brighter than they've ever glowed. [bold cyan]"You understand now.
Insects aren't just bugs — they're the foundation of life
on this planet. They pollinate our food. They recycle our waste.
They feed the animals we love. And they need our help."[/bold cyan]

Puck lands on the girl's shoulder.

[bold cyan]"The next time you see a bee on a flower, or an ant
carrying a crumb, or a beetle trundling across the path —
you'll know what they're doing. And you'll know
why it matters."[/bold cyan]

[bold white]Bug Safari Champion. Insect Guardian. Keeper of the Small and Mighty. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "what_makes_an_insect": "Puck holds up a magnifying glass and places a mystery creature on the page — six legs, three body parts, hard shell. [bold yellow]\"It has all the right features. Does this creature pass the official Insect Test?\"[/bold yellow]",
    "butterflies_and_moths": "The page glows gold. Inside a shimmering chrysalis, something is stirring — wings folding, colours forming. [bold yellow]\"The greatest transformation in nature. A caterpillar becomes a butterfly through a process called... what?\"[/bold yellow]",
    "ants_and_bees": "The page zooms out to show an entire ant colony and a beehive side by side — millions of individuals, one shared purpose. [bold yellow]\"Scientists call a colony that acts like one giant living creature a 'superorganism.' Why does that name fit?\"[/bold yellow]",
    "creepy_crawlies": "A shadow appears on the page — eight legs unfurling, silk trailing behind it. [bold yellow]\"This creature has eight legs, two body parts, no antennae, and spins silk. It's NOT an insect. What is it?\"[/bold yellow]",
    "insects_and_environment": "The page shows the whole living world — plants, animals, soil, water, air — with golden threads connecting everything to insects at the centre. [bold yellow]\"If insects vanished from Earth tomorrow, what would happen to the rest of life?\"[/bold yellow]",
}
