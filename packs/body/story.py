"""
story.py — Narrative for the Body Explorer skill pack.

Puck shrinks the reader down to explore the most amazing machine
ever built: the human body. From bones to brain, heart to immune
system, every zone is a new adventure inside yourself.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Body Explorer[/bold yellow]

The Primer's page shimmered, and Puck appeared — smaller than usual,
standing on what looked like a tiny launchpad made of light.

[bold cyan]"Today,"[/bold cyan] Puck said, eyes wide with excitement,
[bold cyan]"we're going somewhere no atlas can take you.
Somewhere you've been your whole life but never really explored.
We're going [italic]inside.[/italic]"[/bold cyan]

The girl tilted her head. [bold white]"Inside what?"[/bold white]

[bold cyan]"Inside [italic]you.[/italic]"[/bold cyan] Puck grinned and spread both wings.
[bold cyan]"Your body is the most amazing machine ever built.
It has 206 bones, 600 muscles, a brain with 86 billion tiny
messengers, a heart that beats 100,000 times a day, and a defence
army that fights off invaders you can't even see."[/bold cyan]

The page glowed, and the girl saw the outline of a human body
appear — bones shining white, blood flowing red and blue,
lungs breathing in and out, the brain sparkling with light.

[bold cyan]"And the best part?"[/bold cyan] Puck whispered.
[bold cyan]"It all belongs to you. Every cell, every heartbeat,
every breath. Yours."[/bold cyan]

Puck tapped the launchpad. A warm glow surrounded them both.

[bold cyan]"Ready to shrink down and explore?"[/bold cyan]

[bold white]Your adventure inside the human body begins now.[/bold white]
"""

ZONE_INTROS = {
    "bones_and_muscles": """
Puck landed on a glowing white bone — the femur, longest in the body.

[bold cyan]"This,"[/bold cyan] Puck said, knocking on it, [bold cyan]"is your skeleton.
Two hundred and six bones, all connected, all holding you up.
Without them, you'd be a puddle on the floor."[/bold cyan]

Muscles wrapped around the bones like red ropes, pulling and flexing.

[bold cyan]"And these are the muscles — over 600 of them.
They pull on your bones to make you move.
Every step, every smile, every blink — that's muscle power."[/bold cyan]

[bold white]Let's explore the framework that holds you together![/bold white]
""",
    "heart_and_blood": """
Puck pressed an ear against a glowing red wall. Thump-thump. Thump-thump.

[bold cyan]"Hear that?"[/bold cyan] Puck whispered. [bold cyan]"That's the heart.
A muscle the size of your fist, pumping blood through
100,000 kilometres of blood vessels — every minute of every day,
even while you sleep."[/bold cyan]

Rivers of red and blue light branched out from the heart in all directions.

[bold cyan]"Red blood goes out, carrying oxygen. Blue blood comes back,
ready for a refill. It never stops. [italic]Ever.[/italic]"[/bold cyan]

[bold white]Let's follow the blood and discover the beating engine![/bold white]
""",
    "lungs_and_breathing": """
Puck floated between two enormous pink structures that expanded
and contracted like slow, gentle balloons.

[bold cyan]"Your lungs,"[/bold cyan] Puck said, breathing deeply.
[bold cyan]"You take about 20,000 breaths every single day.
Each one brings in oxygen — the fuel your cells need —
and pushes out carbon dioxide, the waste they don't."[/bold cyan]

A dome-shaped muscle below the lungs flattened and rose,
flattened and rose.

[bold cyan]"And that's the diaphragm — the engine of every breath."[/bold cyan]

[bold white]Take a deep breath. Let's explore![/bold white]
""",
    "brain_and_nerves": """
Puck stood in a vast, glowing chamber — sparks of light racing
in every direction like a city of a billion fireflies.

[bold cyan]"Welcome to the brain,"[/bold cyan] Puck said in an awed whisper.
[bold cyan]"Eighty-six billion neurons. Each one connected to thousands
of others. Every thought you've ever had, every memory,
every feeling — it all happens [italic]here.[/italic]"[/bold cyan]

A spark raced from the brain down a long glowing cord.

[bold cyan]"And those sparks travel through your nerves at up to
270 miles per hour. Faster than a race car.
Your body has its own lightning."[/bold cyan]

[bold white]Let's explore mission control![/bold white]
""",
    "digestion": """
Puck stood at the entrance to a long, winding tunnel.
At the very start: a set of teeth.

[bold cyan]"The moment food enters your mouth,"[/bold cyan] Puck said,
[bold cyan]"an incredible journey begins. Your teeth chop it up.
Your stomach dissolves it. Your intestines — all nine metres
of them — pull out every nutrient your body needs."[/bold cyan]

The tunnel glowed with activity: acids churning, tiny villi
waving, nutrients floating into the bloodstream.

[bold cyan]"From start to finish, it takes one to three days.
Your body is a food factory that never closes."[/bold cyan]

[bold white]Let's follow the food![/bold white]
""",
    "exercise_and_fitness": """
Puck bounced onto the page, doing a cartwheel and landing
with a flourish.

[bold cyan]"Your body,"[/bold cyan] Puck said, slightly out of breath,
[bold cyan]"was built to [italic]move.[/italic] Run, jump, climb, swim, dance.
When you exercise, your heart gets stronger, your muscles grow,
your bones harden, and your brain releases happy chemicals
called endorphins."[/bold cyan]

Three glowing icons appeared: a running shoe, a stretching figure,
and a flexing arm.

[bold cyan]"Cardio for your heart. Strength for your muscles.
Flexibility for your joints. And sleep to tie it all together.
Your body rewards you for taking care of it."[/bold cyan]

[bold white]Let's get moving![/bold white]
""",
    "germs_and_immunity": """
Puck pulled on a tiny suit of armour and raised a microscope like a sword.

[bold cyan]"Right now,"[/bold cyan] Puck said seriously, [bold cyan]"there are tiny things
all around you that you can't see. Bacteria. Viruses. Fungi.
Most of them are harmless — some are even helpful! But a few
would love to make you sick."[/bold cyan]

Inside the body on the page, an army of white blood cells
stood at attention.

[bold cyan]"Luckily, you have an immune system — a defence force
so smart it [italic]remembers[/italic] every enemy it's ever fought.
Vaccines train it. Handwashing blocks invaders at the gate.
And your skin? That's the first wall they have to get past."[/bold cyan]

[bold white]Let's meet the invisible battle![/bold white]
""",
    "growing_up": """
Puck sat on a timeline that stretched across the whole page —
from a tiny baby at one end to a tall young adult at the other.

[bold cyan]"You're growing,"[/bold cyan] Puck said warmly.
[bold cyan]"Every single day, your body is changing.
Bones fusing. Teeth swapping. Muscles strengthening.
And one day, hormones will trigger even bigger changes —
that's called puberty, and it happens to everyone."[/bold cyan]

Children of different sizes and shapes dotted the timeline,
each one glowing with their own light.

[bold cyan]"Everyone grows at their own pace. There's no 'right' speed,
no 'right' shape. The only thing that matters is that you
take care of the amazing body you've got."[/bold cyan]

[bold white]Let's discover the amazing you![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "bones_and_muscles": """
[bold green]The skeleton stands tall and strong, every bone aglow![/bold green]

Muscles flex and pull, joints bend and twist,
the spine stands straight like a tower of light.

[bold cyan]"You know your skeleton now,"[/bold cyan] Puck says proudly.
[bold cyan]"206 bones, over 600 muscles, and joints that let you
move in every direction. You're a walking, running,
jumping masterpiece."[/bold cyan]

A heartbeat pulses ahead. The beating engine is next...
""",
    "heart_and_blood": """
[bold green]The heart glows red and strong, pumping rivers of light![/bold green]

Arteries branch outward in red. Veins return in blue.
Red blood cells carry their tiny sparkles of oxygen everywhere.

[bold cyan]"Your heart never takes a day off,"[/bold cyan] Puck says.
[bold cyan]"It's been beating since before you were born,
and it won't stop for your whole life. Take care of it —
it takes care of everything else."[/bold cyan]

Two pink lungs expand gently ahead. Time to breathe...
""",
    "lungs_and_breathing": """
[bold green]The lungs glow pink, breathing in rhythm![/bold green]

The diaphragm pulses below. Oxygen flows in, carbon dioxide flows out.
Twenty thousand breaths a day, every one keeping you alive.

[bold cyan]"You'll never think about breathing the same way again,"[/bold cyan]
Puck says. [bold cyan]"Every breath is a tiny miracle —
an exchange of gases that keeps every cell in your body alive."[/bold cyan]

Sparks of light flicker ahead. The brain is waiting...
""",
    "brain_and_nerves": """
[bold green]The brain blazes with light — 86 billion neurons firing![/bold green]

Messages race down nerves like lightning. Senses report in.
Reflexes snap. Memories shimmer in the background.

[bold cyan]"This,"[/bold cyan] Puck whispers, [bold cyan]"is the most complex thing
in the known universe. And it's sitting right between your ears.
Everything you think, feel, dream, and remember — it all starts here."[/bold cyan]

A winding tunnel opens ahead. The food factory awaits...
""",
    "digestion": """
[bold green]The digestive system glows from mouth to finish![/bold green]

Teeth gleam. The stomach churns. The small intestine waves
its millions of tiny villi, catching every nutrient.

[bold cyan]"From the first bite to the last step,"[/bold cyan] Puck says,
[bold cyan]"your digestive system turns food into fuel.
Nine metres of incredible machinery, working around the clock."[/bold cyan]

A pair of running shoes glows ahead. Time to get moving...
""",
    "exercise_and_fitness": """
[bold green]The body on the page radiates energy and strength![/bold green]

Muscles pulse. The heart beats strong. Bones gleam white.
A clock shows a full 60 minutes of joyful movement.

[bold cyan]"Move, stretch, sleep, repeat,"[/bold cyan] Puck says, beaming.
[bold cyan]"Your body rewards you for every minute of exercise.
Stronger heart, stronger bones, happier brain. It's the best deal going."[/bold cyan]

Tiny invaders gather at the gates. The immune system stands ready...
""",
    "germs_and_immunity": """
[bold green]The immune army stands victorious![/bold green]

White blood cells patrol with confidence. The skin glows like a shield.
Vaccines stand like training manuals on a shelf, ready when needed.

[bold cyan]"Your body fights battles you never even notice,"[/bold cyan]
Puck says with respect. [bold cyan]"Billions of defenders, working day
and night. All you have to do is wash your hands, eat well,
sleep enough, and let your immune system do the rest."[/bold cyan]

A timeline stretches ahead. One last zone — the most personal of all...
""",
    "growing_up": """
[bold green]The timeline glows from beginning to end — and beyond![/bold green]

Children of every size and shape shine with their own light.
Bones fuse. Teeth grow. Bodies change and strengthen.

[bold cyan]"You've done it,"[/bold cyan] Puck says, wings spreading wide.
[bold cyan]"Bones, heart, lungs, brain, digestion, exercise, immunity,
and growth — you've explored the most amazing machine
in the universe. And it's [italic]yours.[/italic]"[/bold cyan]

Puck places a hand over the heart on the page. It pulses warmly.

[bold white]Body Explorer. Health Champion. The Amazing You. That's who you are.[/bold white]
""",
}

BOSS_INTROS = {
    "bones_and_muscles": "Puck flexes a tiny arm and points to the skeleton on the page. [bold yellow]\"Muscles can only PULL — they can't push! That's why they always work in pairs. Can you figure out how?\"[/bold yellow]",
    "heart_and_blood": "Puck holds a fist up next to the glowing heart. [bold yellow]\"Your heart is about this big — the size of your own fist. But how powerful is this little muscle really?\"[/bold yellow]",
    "lungs_and_breathing": "Puck hiccups dramatically on the page. Hic! Hic! [bold yellow]\"Everyone gets hiccups — but do you know which muscle causes them?\"[/bold yellow]",
    "brain_and_nerves": "The brain on the page splits into two glowing halves. [bold yellow]\"Your brain has two sides that need to talk to each other. But what connects them?\"[/bold yellow]",
    "digestion": "Puck traces the long, winding path from mouth to end. [bold yellow]\"Food travels through NINE metres of tubing inside you. How long does the whole journey take?\"[/bold yellow]",
    "exercise_and_fitness": "A clock appears on the page, slowly filling up. [bold yellow]\"Every kid needs a certain amount of exercise each day. Do you know the magic number?\"[/bold yellow]",
    "germs_and_immunity": "The skin on the page glows like a golden shield. [bold yellow]\"Before your white blood cells even join the fight, something else stops most germs. What is it?\"[/bold yellow]",
    "growing_up": "Children of all different heights and shapes appear on the page. [bold yellow]\"Everyone's body is different. But WHY do people grow to different heights and shapes?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "skeleton_scholar": (
        "Skeleton Scholar",
        "Named every bone, joint, and muscle challenge in the body!",
    ),
    "heart_hero": (
        "Heart Hero",
        "Followed the blood from heart to body and back again!",
    ),
    "breath_master": (
        "Breath Master",
        "Understood lungs, oxygen, and the mighty diaphragm!",
    ),
    "brain_explorer": (
        "Brain Explorer",
        "Mapped the brain, the senses, and the lightning-fast nerves!",
    ),
    "digestion_guide": (
        "Digestion Guide",
        "Followed food on its incredible nine-metre journey!",
    ),
    "fitness_champion": (
        "Fitness Champion",
        "Mastered cardio, strength, flexibility, and the power of sleep!",
    ),
    "immunity_warrior": (
        "Immunity Warrior",
        "Defeated germs and discovered the body's amazing defences!",
    ),
    "growth_guru": (
        "Growth Guru",
        "Explored how bodies grow, change, and become uniquely amazing!",
    ),
}
