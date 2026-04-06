"""
story.py — Narrative for the Emotions & Mindfulness skill pack.

Puck opens the Heart Room deep inside the Primer — a place where
feelings become visible, nameable, and ultimately a superpower.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Heart Room[/bold yellow]

Puck appeared on the Primer's newest page looking unusually still.
No somersaults, no cheeky grin — just a gentle, thoughtful expression
and two hands pressed softly against the centre of the page, right
where a heartbeat might be.

[bold cyan]"There's a room inside this book,"[/bold cyan] Puck said quietly,
[bold cyan]"that most people walk right past. It doesn't have maps
or numbers or spelling lists. It has something more important."[/bold cyan]

The girl leaned closer. [bold white]"What's inside?"[/bold white]

Puck pressed both palms against the page. A door appeared —
not drawn in ink, but glowing from within, warm as candlelight.

[bold cyan]"Feelings,"[/bold cyan] Puck whispered. [bold cyan]"Every feeling you've
ever felt — happiness, sadness, anger, fear, surprise —
they all live in here. And once you learn their names,
once you understand what they're trying to tell you…"[/bold cyan]

Puck's wings spread wide and shimmered gold.

[bold cyan]"…they become your superpower."[/bold cyan]

The door swung open. Inside was a room of soft light,
with mirrors on every wall that didn't show your face —
they showed your heart.

[bold cyan]"Ready to step inside?"[/bold cyan]

[bold white]Your journey into the Heart Room begins now.[/bold white]
"""

ZONE_INTROS = {
    "naming_feelings": """
Puck flew to the first mirror on the wall. It swirled with colours —
red, blue, yellow, green, purple, grey — each one shifting and blending.

[bold cyan]"Before you can DO anything with a feeling,"[/bold cyan] Puck said,
[bold cyan]"you have to NAME it. That's the first rule of the Heart Room.
A feeling you can name is a feeling you can understand.
And a feeling you can understand? That's one you can handle."[/bold cyan]

Six coloured orbs floated in the mirror:
[bold yellow]Happy · Sad · Angry · Scared · Surprised · Disgusted[/bold yellow]

[bold white]Let's learn to name what you feel![/bold white]
""",
    "big_emotions": """
The second mirror on the wall was cracked — not broken, but shaking,
as if something enormous were pressing against it from the other side.

[bold cyan]"Sometimes,"[/bold cyan] Puck said carefully, [bold cyan]"feelings get REALLY big.
So big they feel like a storm inside you. Anger that makes you want
to throw things. Sadness so heavy you can't move. Fear so sharp
you can't breathe."[/bold cyan]

Puck placed a gentle hand on the cracked mirror.

[bold cyan]"Those feelings aren't bad. They're just BIG. And in this room,
we're going to learn what to do when the storm hits."[/bold cyan]

[bold white]Let's learn how to weather the storm![/bold white]
""",
    "empathy": """
The third mirror didn't show your reflection at all.
It showed someone else's face — a face that changed
every few seconds, showing different expressions.

[bold cyan]"Empathy,"[/bold cyan] Puck said softly, [bold cyan]"is the most magical
power in the Heart Room. It means being able to feel
what SOMEONE ELSE is feeling — to look at their face,
their body, their eyes — and understand."[/bold cyan]

The mirror flickered: a smiling face, a crying face,
a frightened face, a face full of hope.

[bold cyan]"When you truly understand how someone else feels,
you can help them. And that changes everything."[/bold cyan]

[bold white]Let's learn to read the language of hearts![/bold white]
""",
    "mindful_breathing": """
The centre of the Heart Room opened into a garden — not drawn,
but alive. Tiny flowers bloomed and closed in a slow, steady rhythm,
as if the whole garden were breathing.

[bold cyan]"This,"[/bold cyan] Puck whispered, sitting cross-legged on a tiny leaf,
[bold cyan]"is the Breathing Garden. The most powerful calm-down tool
in the entire world — and you carry it everywhere you go.
Your breath."[/bold cyan]

The flowers breathed in… and out… in… and out.

[bold cyan]"Deep breaths tell your brain: I am safe. I can think.
I am here. Let me teach you how."[/bold cyan]

[bold white]Let's discover the power of breathing![/bold white]
""",
    "gratitude": """
A new section of the Heart Room opened up, and in its centre
stood a tree — a great, golden tree with leaves that glowed
like little lanterns. Each leaf had a tiny word on it:
[bold yellow]sunshine · laughter · warm bed · kind word · birdsong[/bold yellow]

[bold cyan]"This is the Thankfulness Tree,"[/bold cyan] Puck said, gazing up.
[bold cyan]"Every leaf is something good in someone's life.
Most people walk past the good things without noticing.
But people who PRACTISE gratitude? They see treasure everywhere."[/bold cyan]

Puck plucked a glowing leaf: [bold yellow]a friend who listens[/bold yellow].

[bold cyan]"Let's grow your tree."[/bold cyan]

[bold white]Let's learn the art of being thankful![/bold white]
""",
    "friendship_skills": """
Two figures appeared on the page — standing on opposite sides
of a wide crack in the ground. They looked like they wanted
to reach each other but didn't know how.

[bold cyan]"Friendship,"[/bold cyan] Puck said, fluttering between them,
[bold cyan]"is one of the best things in life. But it takes SKILLS.
Sharing. Listening. Saying sorry when you mess up.
Including people who are left out. Setting boundaries.
None of it is automatic — all of it can be learned."[/bold cyan]

Puck began building a bridge across the crack, plank by plank.

[bold cyan]"Let's build bridges together."[/bold cyan]

[bold white]Let's learn the skills of true friendship![/bold white]
""",
    "self_confidence": """
The last mirror in the Heart Room was the biggest of all —
floor to ceiling, framed in gold. But it was dark.

[bold cyan]"This mirror,"[/bold cyan] Puck said gently, [bold cyan]"shows you something
very important. But it only lights up when you believe
in what you see."[/bold cyan]

Puck touched the glass. Slowly, a figure appeared —
glowing, strong, imperfect, and beautiful.

[bold cyan]"That's you,"[/bold cyan] Puck said. [bold cyan]"Not a perfect you.
Not a pretend you. The real you — the one who tries hard,
makes mistakes, gets back up, and keeps growing.
That is the most powerful person in this room."[/bold cyan]

[bold white]Let's discover the strength that's already inside you![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "naming_feelings": """
[bold green]The first mirror blazes with colour — every emotion named and known![/bold green]

Six orbs glow steadily: gold for happiness, blue for sadness,
red for anger, purple for fear, yellow for surprise, green for disgust.
Each one named. Each one understood.

[bold cyan]"You did it,"[/bold cyan] Puck says proudly.
[bold cyan]"You can name your feelings — and that means
you can understand them. The first step is always the hardest,
and you just took it."[/bold cyan]

The second mirror begins to tremble. The big emotions are next...
""",
    "big_emotions": """
[bold green]The cracked mirror mends itself — piece by piece, crack by crack![/bold green]

The storm behind the glass grows quiet. Not gone — just understood.

[bold cyan]"Big feelings don't disappear,"[/bold cyan] Puck says softly.
[bold cyan]"But now you know what to DO with them.
Breathe. Name them. Ask for help. Use your calm-down tools.
The storm will always pass."[/bold cyan]

The empathy mirror glimmers on the far wall. Someone else's feelings await...
""",
    "empathy": """
[bold green]The empathy mirror glows warm — showing face after face, all understood![/bold green]

Smiling faces, tearful faces, worried faces, hopeful faces —
you can read them all now.

[bold cyan]"Empathy,"[/bold cyan] Puck says with quiet pride,
[bold cyan]"is the superpower that changes the world.
Not by fighting. Not by force. But by understanding.
When you truly see how someone else feels,
you can help. And that is everything."[/bold cyan]

A gentle breeze blows. The Breathing Garden awaits...
""",
    "mindful_breathing": """
[bold green]The Breathing Garden blooms in full — every flower open, every leaf still![/bold green]

The whole garden breathes in perfect rhythm: in... and out... in... and out.

[bold cyan]"You carry this garden with you everywhere,"[/bold cyan] Puck says.
[bold cyan]"In a classroom. On a bus. In bed at night.
Wherever you are, your breath is there too —
the most powerful calm-down tool in the world."[/bold cyan]

A golden tree sprouts in the distance. The Thankfulness Tree is growing...
""",
    "gratitude": """
[bold green]The Thankfulness Tree blazes with golden leaves — hundreds of them![/bold green]

Every leaf glows with a tiny treasure: a warm meal, a friend's laugh,
a sunny afternoon, a bedtime story, the smell of rain.

[bold cyan]"Your tree is full,"[/bold cyan] Puck says, looking up in wonder.
[bold cyan]"And the beautiful thing? It never stops growing.
Every day you notice something good, a new leaf appears.
You'll never run out of things to be thankful for."[/bold cyan]

Two figures appear ahead. The Friendship Forge beckons...
""",
    "friendship_skills": """
[bold green]The bridge is complete — strong and golden, spanning the gap![/bold green]

Two figures walk toward each other across the bridge, meeting in the middle
with a handshake, a hug, and a laugh.

[bold cyan]"Friendship,"[/bold cyan] Puck says warmly, [bold cyan]"isn't about being perfect.
It's about showing up, being kind, saying sorry when you mess up,
and making room for others. You know how to build bridges now.
And bridges are the most beautiful things in the world."[/bold cyan]

The final mirror glows at the end of the room. Your reflection awaits...
""",
    "self_confidence": """
[bold green]The great mirror blazes with light — and the figure inside is YOU![/bold green]

Not a perfect figure. Not a pretend figure. The real you —
glowing with every lesson learned, every challenge faced,
every feeling named, every breath taken, every friend made.

[bold cyan]"Look at you,"[/bold cyan] Puck says, wings trembling with pride.
[bold cyan]"You walked into the Heart Room not knowing
what your feelings were for. Now you know.
They're your superpower. Every single one of them."[/bold cyan]

Puck places a tiny golden heart in your hands.

[bold white]Feeler. Empath. Listener. Healer. Sage. Heart Master.[/bold white]
[bold white]That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "naming_feelings": "Puck holds up a swirling jar of mixed colours. [bold yellow]\"Here's the trickiest truth about feelings — they don't always come one at a time. Can you feel more than one emotion at once? Think carefully!\"[/bold yellow]",
    "big_emotions": "The feelings thermometer on the wall glows red-hot at the top. [bold yellow]\"Big feelings need big tools. But which tool matches which size? That's the real skill!\"[/bold yellow]",
    "empathy": "Puck flips the whole page around. [bold yellow]\"Now — can you see the world through someone ELSE's eyes? Not guess. Not assume. Really see?\"[/bold yellow]",
    "mindful_breathing": "Puck closes both eyes and the whole garden goes perfectly still. [bold yellow]\"Mindfulness isn't just breathing — it's being fully HERE. Can you recognise what that really means?\"[/bold yellow]",
    "gratitude": "Rain falls softly across the Thankfulness Tree. [bold yellow]\"The hardest question: can you find something to be grateful for even when things are tough? This is where true gratitude lives.\"[/bold yellow]",
    "friendship_skills": "Puck draws a gentle golden line around themselves. [bold yellow]\"The final friendship skill isn't about giving — it's about knowing when to say no. What does it mean to set a boundary?\"[/bold yellow]",
    "self_confidence": "The great mirror dims and then flares. [bold yellow]\"One last question. What does it REALLY mean to believe in yourself? Not perfection. Not arrogance. Something deeper.\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "feeling_finder": (
        "Feeling Finder",
        "Named and identified all six core emotions!",
    ),
    "storm_weatherer": (
        "Storm Weatherer",
        "Learned what to do when feelings get really big!",
    ),
    "empathy_reader": (
        "Empathy Reader",
        "Learned to understand how others feel through faces and body language!",
    ),
    "breath_keeper": (
        "Breath Keeper",
        "Mastered breathing and mindfulness techniques!",
    ),
    "gratitude_grower": (
        "Gratitude Grower",
        "Learned to notice and appreciate the good things in life!",
    ),
    "bridge_builder": (
        "Bridge Builder",
        "Mastered sharing, conflict resolution, and true friendship!",
    ),
    "mirror_master": (
        "Mirror Master",
        "Discovered positive self-talk, growth mindset, and inner strength!",
    ),
}
