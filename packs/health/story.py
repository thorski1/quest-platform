"""
story.py — Narrative for The Healthy Hero skill pack.

Puck guides the reader through an adventure of health and wellness,
from germ-busting to feelings, teaching kids that taking care of
yourself is the greatest superpower of all.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Healthy Hero[/bold yellow]

The Primer's pages rustled, and Puck appeared — wearing a tiny
cape made of bandages and carrying a shield shaped like a heart.

[bold cyan]"Today,"[/bold cyan] Puck said, standing tall (well, as tall
as a small fairy can stand), [bold cyan]"we're going on the most
important quest of all. We're going to learn how to be a
[italic]Healthy Hero.[/italic]"[/bold cyan]

The girl looked curious. [bold white]"What's a Healthy Hero?"[/bold white]

[bold cyan]"Someone who knows how to take care of the most
amazing thing they'll ever own — their own body and mind."[/bold cyan]
Puck tapped the page, and a glowing map appeared with five
shining landmarks.

[bold cyan]"We'll battle germs with soap, fuel up with the right
foods, power up with exercise and sleep, meet the healers who
keep you strong, and — most importantly — learn to take care
of the feelings inside you."[/bold cyan]

Five paths branched out across the map, each one glowing
with a different colour — blue for clean, green for food,
gold for energy, white for healing, and pink for feelings.

[bold cyan]"Every hero needs training,"[/bold cyan] Puck said,
fastening the tiny cape. [bold cyan]"And by the end of this
adventure, you'll know more about staying healthy than
most grown-ups. Ready?"[/bold cyan]

[bold white]Your quest to become a Healthy Hero begins now.[/bold white]
"""

ZONE_INTROS = {
    "germs_and_handwashing": """
Puck landed on a giant bar of soap, sliding down it like a slide.

[bold cyan]"Germs!"[/bold cyan] Puck announced, hopping to a stop.
[bold cyan]"They're everywhere — on door handles, on phones,
on playground equipment. Tiny things too small to see, and some
of them would love to make you sick."[/bold cyan]

A magnifying glass appeared on the page, showing cartoon germs
with silly faces bumping into each other.

[bold cyan]"But here's the secret — you have the most powerful
germ-fighting weapon in the world, and it's sitting right next
to every sink."[/bold cyan] Puck pointed to a bar of soap
that glowed like a golden sword.

[bold cyan]"Soap. Water. Twenty seconds. That's all it takes
to send those germs packing."[/bold cyan]

[bold white]Let's learn how to bust those germs![/bold white]
""",
    "healthy_eating": """
Puck stood in front of a magnificent rainbow made entirely of food —
red strawberries, orange carrots, yellow bananas, green broccoli,
blueberries, and purple grapes arching across the page.

[bold cyan]"Your body,"[/bold cyan] Puck said, arms spread wide,
[bold cyan]"is like the most incredible machine ever built.
But every machine needs the right fuel. Put in the wrong stuff
and it sputters. Put in the right stuff and it [italic]soars.[/italic]"[/bold cyan]

Five colourful plates appeared below the rainbow, each representing
a food group.

[bold cyan]"Fruits, vegetables, grains, protein, dairy — these are
your five best friends. And water? Water is the hero that ties
it all together."[/bold cyan]

[bold white]Let's discover the fuel that powers you![/bold white]
""",
    "exercise_and_sleep": """
Puck bounced onto the page doing a somersault, landing next to
a glowing clock and a cosy-looking bed.

[bold cyan]"Two things,"[/bold cyan] Puck said, slightly breathless
from the somersault. [bold cyan]"Two things that are absolute
[italic]superpowers[/italic] for your body and brain.
Moving... and sleeping."[/bold cyan]

On one side of the page, kids were shown running, jumping,
and dancing, golden sparks flying from their feet.
On the other side, a child slept peacefully while tiny workers
inside their brain organised memories like books on a shelf.

[bold cyan]"Exercise makes everything stronger — your heart,
your muscles, your bones, even your mood. And sleep?
Sleep is when your body does its best repair work.
Put them together and you're unstoppable."[/bold cyan]

[bold white]Let's power up with movement and rest![/bold white]
""",
    "going_to_the_doctor": """
Puck appeared wearing a tiny white coat with a stethoscope
around its neck, standing at the entrance of a bright, friendly hall.

[bold cyan]"A lot of kids feel nervous about visiting the doctor,"[/bold cyan]
Puck said gently. [bold cyan]"And that's completely okay.
But here's a secret — doctors, nurses, and dentists are some
of the greatest heroes in the real world. Their whole job
is to keep you healthy and safe."[/bold cyan]

Inside the hall, friendly figures stood at different stations —
one with a stethoscope, one with a thermometer, one holding
a toothbrush, and one with a tiny shield labelled 'Vaccine.'

[bold cyan]"Check-ups, vaccines, clean teeth, and knowing when
to ask for help — these are the tools that keep your body
running at its best. And the more you know about them,
the less scary they feel."[/bold cyan]

[bold white]Let's meet your health team![/bold white]
""",
    "mental_health": """
Puck walked slowly into a beautiful garden where flowers of
every colour were blooming — but some were bright and open,
while others were closed or wilting.

[bold cyan]"This,"[/bold cyan] Puck said softly, [bold cyan]"is the
Feelings Garden. Every flower is a feeling — happiness,
sadness, anger, fear, excitement, worry. They're all here,
and they all [italic]belong[/italic] here."[/bold cyan]

The girl looked at a drooping blue flower. [bold white]"Even
the sad ones?"[/bold white]

[bold cyan]"[italic]Especially[/italic] the sad ones,"[/bold cyan]
Puck said warmly. [bold cyan]"Because a garden with only one
kind of flower isn't really a garden at all. Your feelings
make you [italic]you.[/italic] The trick isn't to have only
happy feelings — it's to understand all of them, take care
of them, and know when to ask for help."[/bold cyan]

[bold white]Let's explore the most important garden of all.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "germs_and_handwashing": """
[bold green]The soap glows golden. The germs retreat in defeat![/bold green]

Bubbles float across the page, each one popping a cartoon germ.
Clean hands shine like shields.

[bold cyan]"You did it,"[/bold cyan] Puck says, drying tiny hands on a towel.
[bold cyan]"Soap, water, twenty seconds — that's your first line of
defence against any germ out there. You've earned the title
of Germ Buster."[/bold cyan]

A rainbow of food glows ahead. Time to fuel up...
""",
    "healthy_eating": """
[bold green]The food rainbow shines brighter than ever![/bold green]

Five plates glow on the page — fruits, vegetables, grains,
protein, and dairy — perfectly balanced. A glass of crystal-clear
water sparkles beside them.

[bold cyan]"You know the secret now,"[/bold cyan] Puck says, patting
a satisfied tummy. [bold cyan]"Eat the rainbow, drink your water,
and your body will have all the fuel it needs to do
anything you dream of."[/bold cyan]

A glowing clock and a pair of running shoes appear ahead. Energy awaits...
""",
    "exercise_and_sleep": """
[bold green]The Energy Engine hums with golden power![/bold green]

A kid on the page glows with energy — running, jumping, and then
sleeping peacefully as stars swirl around them. The clock reads a
perfect balance of activity and rest.

[bold cyan]"Move for an hour, sleep for ten,"[/bold cyan] Puck says,
stretching happily. [bold cyan]"That's the formula. Your heart is
stronger, your brain is sharper, and those endorphins are flowing.
You're an energy champion!"[/bold cyan]

A bright, friendly hall opens ahead. The healers are waiting...
""",
    "going_to_the_doctor": """
[bold green]The Healer's Hall shines with warm, welcoming light![/bold green]

Friendly doctors, dentists, and nurses stand on the page, each
one smiling. A vaccine shield gleams on the wall. A sparkling
set of teeth grins beside it.

[bold cyan]"Doctors aren't scary,"[/bold cyan] Puck says, hanging up
the tiny white coat. [bold cyan]"They're your teammates. Check-ups,
vaccines, clean teeth — these are the tools that keep your
amazing body in top shape. And you can always tell them
how you feel."[/bold cyan]

A beautiful garden blooms ahead. The most important zone of all...
""",
    "mental_health": """
[bold green]The Feelings Garden is in full bloom — every flower bright and cared for![/bold green]

Flowers of every colour sway gently: golden joy, blue calm,
red courage, purple creativity, and soft pink kindness.
Not a single flower is hidden or ignored.

[bold cyan]"You've done it,"[/bold cyan] Puck says, wings spreading
wide in the garden's warm light. [bold cyan]"You've learned the
most important lesson of all — your feelings matter, you're
never alone, and asking for help is the bravest thing
anyone can do."[/bold cyan]

Puck places a hand over the heart on the page. It glows warmly.

[bold white]Germ Buster. Fuel Master. Energy Champion. Healer's Friend.
Feelings Guardian. You are a Healthy Hero — and the world is
better because you're in it.[/bold white]
""",
}

BOSS_INTROS = {
    "germs_and_handwashing": "A big cartoon germ with a silly face blocks the path. Puck pulls out a bar of soap like a sword. [bold yellow]\"This germ thinks it can get past your defences. Can you spot the one thing that WON'T protect you?\"[/bold yellow]",
    "healthy_eating": "A feast is laid out on the page — but not all of it is healthy! Puck puts on a chef's hat. [bold yellow]\"Time for the ultimate test: can you spot the BEST balanced meal?\"[/bold yellow]",
    "exercise_and_sleep": "A golden clock spins on the page, showing a full day. Puck stretches and yawns. [bold yellow]\"Sleep, food, exercise — you know them all now. But which daily routine puts it ALL together?\"[/bold yellow]",
    "going_to_the_doctor": "Two kids sit in a waiting room on the page. One looks nervous. Puck sits beside them gently. [bold yellow]\"A friend is scared of the doctor. What would a true Healthy Hero say?\"[/bold yellow]",
    "mental_health": "A friend sits alone in the garden, looking sad. Puck looks at you with gentle, serious eyes. [bold yellow]\"This is the most important challenge of all. What does a real friend do when someone is hurting?\"[/bold yellow]",
}
