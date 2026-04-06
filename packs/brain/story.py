"""
story.py — Narrative for the Brain Lab skill pack.

Puck takes the reader on a journey inside the most complex thing
in the known universe: the human brain. From neurons to emotions,
senses to sleep, every zone reveals a new wonder between your ears.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Brain Lab[/bold yellow]

The Primer's page shimmered, and Puck appeared — standing on what
looked like a glowing pink walnut, pulsing with tiny sparks of light.

[bold cyan]"Do you know what this is?"[/bold cyan] Puck asked, tapping it
with one foot. A cascade of sparkles rippled outward.

The girl peered closer. [bold white]"It looks like... a brain?"[/bold white]

[bold cyan]"Not just any brain,"[/bold cyan] Puck said, grinning.
[bold cyan]"YOUR brain. The most complex thing in the entire known
universe. More connections than there are stars in the Milky Way.
Faster than any computer ever built. And it fits right here."[/bold cyan]

Puck pointed at the girl's head.

[bold cyan]"It controls every thought you think, every feeling you feel,
every memory you treasure, and every move you make. It even keeps
your heart beating and your lungs breathing while you sleep."[/bold cyan]

The brain on the page unfolded like a flower, revealing five
glowing chambers inside — each one pulsing with a different colour.

[bold cyan]"Five rooms to explore,"[/bold cyan] Puck whispered.
[bold cyan]"Neurons and signals. Your five senses. Memory and learning.
Emotions and feelings. And the secrets to keeping this incredible
organ healthy for your whole life."[/bold cyan]

Puck spread both wings and dove into the first glowing chamber.

[bold cyan]"Ready to explore the most amazing thing you own?"[/bold cyan]

[bold white]Your adventure inside the brain begins now.[/bold white]
"""

ZONE_INTROS = {
    "how_your_brain_works": """
Puck landed softly on a glowing neuron — a spidery cell with long arms
reaching out in every direction, sparking with tiny flashes of light.

[bold cyan]"Welcome to Mission Control,"[/bold cyan] Puck said, eyes wide.
[bold cyan]"Everything starts here. Eighty-six billion of these tiny cells —
called neurons — are firing right now inside your head.
Each one connected to thousands of others."[/bold cyan]

A spark leapt from one neuron to the next, then the next, then the next —
a chain of lightning racing across the page.

[bold cyan]"That signal just told your lungs to breathe.
This one remembered your best friend's name.
And that one? It's the reason you're reading these words right now."[/bold cyan]

Puck pointed to the brain's two halves, glowing pink and gold.

[bold cyan]"Left side, right side, connected in the middle.
Let's find out how this incredible machine works!"[/bold cyan]

[bold white]Let's explore Mission Control![/bold white]
""",
    "the_five_senses": """
Puck stood at a crossroads where five glowing paths met — one gold,
one blue, one green, one red, and one purple.

[bold cyan]"Your brain is locked inside a dark, silent skull,"[/bold cyan]
Puck said. [bold cyan]"It can't see, hear, or feel anything on its own.
So how does it know what's happening in the world?"[/bold cyan]

The girl thought for a moment. [bold white]"The senses?"[/bold white]

[bold cyan]"Exactly!"[/bold cyan] Puck beamed. [bold cyan]"Five amazing systems that
collect information from the outside world and send it to your brain.
Sight, hearing, touch, taste, and smell — the Sense Squad!"[/bold cyan]

Each path pulsed with light — eyes, ears, skin, tongue, nose —
all sending streams of signals toward the brain at the centre.

[bold cyan]"Without them, your brain would be the smartest thing
in the universe... with absolutely nothing to think about."[/bold cyan]

[bold white]Let's meet the Sense Squad![/bold white]
""",
    "memory_and_learning": """
Puck pushed open a grand door into an enormous library that stretched
in every direction — shelves of glowing books reaching to the ceiling.

[bold cyan]"Welcome to the Memory Palace,"[/bold cyan] Puck whispered.
[bold cyan]"Every memory you have — your first day of school, your
favourite song, the face of someone you love — it's stored here,
coded in the connections between your neurons."[/bold cyan]

Some books glowed brightly. Others were faded and dusty.

[bold cyan]"The bright ones? Those are memories you use a lot —
strong connections your brain keeps polished. The dusty ones?
Memories your brain hasn't needed in a while."[/bold cyan]

A tiny seahorse-shaped creature swam through the air between shelves.

[bold cyan]"And that little guy? The hippocampus. Your brain's librarian.
It decides what gets filed permanently and what gets recycled."[/bold cyan]

[bold white]Let's unlock the secrets of memory![/bold white]
""",
    "emotions_and_the_brain": """
Puck stepped into a room where the walls kept changing colour —
warm yellow, angry red, peaceful blue, anxious purple — shifting
with every heartbeat.

[bold cyan]"This,"[/bold cyan] Puck said softly, [bold cyan]"is where feelings live.
Joy. Fear. Anger. Sadness. Surprise. Love. Every emotion you've
ever felt was born right here, in the brain."[/bold cyan]

A tiny almond-shaped structure pulsed red in the centre.

[bold cyan]"That's the amygdala — your brain's alarm bell.
When it senses danger, it can hijack your whole body in an instant.
Heart pounding, muscles tense, ready to fight or run."[/bold cyan]

Golden sparkles drifted through the room like warm sunlight.

[bold cyan]"But your brain also makes happiness chemicals — dopamine,
serotonin, endorphins, oxytocin. The ingredients of every smile,
every hug, every moment of pride."[/bold cyan]

[bold white]Let's explore the Feelings Factory![/bold white]
""",
    "taking_care_of_your_brain": """
Puck walked into a bright, clean room filled with exercise mats,
colourful fruits, a cozy bed, and a water fountain.

[bold cyan]"You've learned how your brain works,"[/bold cyan] Puck said.
[bold cyan]"You've explored your senses, your memories, your emotions.
Now for the most important question of all:
how do you take care of this incredible organ?"[/bold cyan]

Four glowing icons appeared on the page: a pillow, a running shoe,
an apple, and a clock.

[bold cyan]"Sleep — your brain's repair and filing time.
Exercise — the best brain-growing medicine there is.
Food and water — fuel for 86 billion hungry neurons.
And screen time — the modern challenge every brain faces."[/bold cyan]

Puck stood at the centre of it all, wings folded, serious for once.

[bold cyan]"Your brain will be with you your whole life.
The choices you make now — every glass of water, every good night's
sleep, every time you run and play — shape the brain you'll have
forever."[/bold cyan]

[bold white]Let's learn how to be your brain's best friend![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "how_your_brain_works": """
[bold green]Mission Control blazes with light — 86 billion neurons firing in harmony![/bold green]

Signals race through pathways like lightning. The two hemispheres
glow in unison, connected by their bridge of 200 million fibres.

[bold cyan]"You've mapped Mission Control,"[/bold cyan] Puck says proudly.
[bold cyan]"Neurons, signals, hemispheres, and wrinkles — you understand
the basics of the most complex thing in the known universe.
And it's sitting right between your ears."[/bold cyan]

Five glowing paths appear ahead. Your senses are calling...
""",
    "the_five_senses": """
[bold green]All five senses blaze to life — sight, hearing, touch, taste, and smell![/bold green]

Streams of coloured light pour from eyes, ears, skin, tongue, and nose,
all converging on the brain at the centre.

[bold cyan]"The Sense Squad is complete,"[/bold cyan] Puck says.
[bold cyan]"Five incredible systems, all working together to build
your picture of the world. Your brain sees, hears, feels, tastes,
and smells — through them."[/bold cyan]

A grand door appears ahead. The Memory Palace awaits...
""",
    "memory_and_learning": """
[bold green]The Memory Palace glows — shelves organised, pathways strong![/bold green]

The hippocampus swims proudly between bright, well-filed memories.
New neural pathways shine like freshly paved roads.

[bold cyan]"Short-term, long-term, practice, sleep, and neuroplasticity,"[/bold cyan]
Puck says, beaming. [bold cyan]"You understand how memories are made,
stored, and strengthened. And you know the most amazing part —
your brain never stops growing and changing."[/bold cyan]

The walls shift colour ahead. The Feelings Factory is next...
""",
    "emotions_and_the_brain": """
[bold green]The Feelings Factory hums with balanced, understood emotions![/bold green]

Joy glows gold. Fear flashes red — but controlled. Sadness shimmers
blue and gentle. Anger burns bright but measured.

[bold cyan]"Every emotion has a purpose,"[/bold cyan] Puck says warmly.
[bold cyan]"Fear keeps you safe. Joy rewards you. Sadness helps you heal.
Anger tells you something matters. Understanding your feelings
is one of the most powerful things your brain can do."[/bold cyan]

A bright, clean room opens ahead. Time to learn the brain's best secrets...
""",
    "taking_care_of_your_brain": """
[bold green]The Brain Gym radiates health and energy![/bold green]

A well-rested brain files memories perfectly. Exercise sparks
new connections. Colourful foods fuel every neuron.
A balanced clock ticks with healthy habits.

[bold cyan]"You've done it,"[/bold cyan] Puck says, wings spreading wide.
[bold cyan]"Neurons and signals. Senses and memory. Emotions and care.
You've explored the most amazing organ in the known universe —
and now you know how to keep it healthy for life."[/bold cyan]

Puck places a hand on the brain. It pulses warmly with light.

[bold white]Brain Explorer. Neuron Navigator. Mind Master.
You know the most incredible thing in the universe — and it's you.[/bold white]
""",
}

BOSS_INTROS = {
    "how_your_brain_works": "Puck unfolds the brain's surface like a crumpled piece of paper. It just keeps going! [bold yellow]\"Your brain is wrinkled for a very clever reason. Can you figure out why?\"[/bold yellow]",
    "the_five_senses": "Puck draws two lines on the page — they look different lengths, but are they? [bold yellow]\"Sometimes your senses fool your brain. What do we call these visual tricks?\"[/bold yellow]",
    "memory_and_learning": "New pathways light up across the brain, branching like a growing tree. [bold yellow]\"Your brain can change and grow new connections your whole life. Scientists have a special name for this — do you know it?\"[/bold yellow]",
    "emotions_and_the_brain": "Puck lines up every emotion — joy, anger, fear, sadness — and they all glow equally. [bold yellow]\"Some people call anger and fear 'bad' emotions. But are they really?\"[/bold yellow]",
    "taking_care_of_your_brain": "Puck stands at a finish line with a glowing brain trophy. [bold yellow]\"If you could only do ONE thing for brain health your whole life, what would scientists recommend?\"[/bold yellow]",
}
