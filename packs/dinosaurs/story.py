"""
story.py — Narrative for the Dinosaurs & Prehistoric Life skill pack.

Puck opens a glowing Time Machine inside the Primer and guides the reader
back millions of years to meet dinosaurs, ancient sea creatures, and the
amazing animals that came after them.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Time Machine[/bold yellow]

Puck appeared on the edge of a brand-new page, holding something
extraordinary — a glowing brass dial covered in spinning numbers.
Every time the numbers changed, the world around them shifted:
jungles grew taller, oceans rose and fell, and enormous shadows
moved across the land.

[bold cyan]"A Time Machine!"[/bold cyan] Puck announced, wings trembling with excitement.
[bold cyan]"Not the kind with levers and steam — the kind that lives
inside a book. Turn the dial backwards, and the whole world
changes. Millions of years. Hundreds of millions of years.
All the way back to when the most amazing creatures
that ever lived walked the Earth."[/bold cyan]

The girl leaned closer. [bold white]"Dinosaurs?"[/bold white]

[bold cyan]"Dinosaurs."[/bold cyan] Puck grinned. [bold cyan]"And flying reptiles.
And sea monsters. And woolly mammoths. And the story of how
a single rock from space changed everything."[/bold cyan]

The dial spun backwards. The page shimmered. Ferns unfurled.
The ground trembled.

[bold cyan]"Ready to travel back in time?"[/bold cyan]

[bold white]Your prehistoric adventure begins now.[/bold white]
"""

ZONE_INTROS = {
    "what_are_dinosaurs": """
Puck turned the Time Machine dial all the way back — 230 million years.

The Primer's pages transformed. The air felt hot and thick.
Strange ferns and towering conifers filled the landscape.
Something enormous moved behind the trees.

[bold cyan]"Welcome to the Mesozoic Era,"[/bold cyan] Puck whispered.
[bold cyan]"The Age of Reptiles. This is when dinosaurs first appeared —
and they ruled the Earth for over 160 million years.
That's a thousand times longer than humans have existed."[/bold cyan]

[bold cyan]"But first — we need to understand what a dinosaur
actually [italic]is.[/italic] Not every big reptile was a dinosaur.
Not every ancient creature counts. There are rules."[/bold cyan]

[bold white]Let's find out what makes a dinosaur a dinosaur![/bold white]
""",
    "famous_dinosaurs": """
Puck adjusted the dial, and the Primer opened to a gallery of giants.

Enormous shapes filled the pages — some with long necks reaching
into the treetops, some with horns and armoured plates, some
with jaws full of teeth as long as bananas.

[bold cyan]"These,"[/bold cyan] Puck said reverently, [bold cyan]"are the most famous
dinosaurs that ever lived. You've probably heard their names —
but do you really know them?"[/bold cyan]

[bold yellow]T-Rex · Triceratops · Stegosaurus · Brachiosaurus · Velociraptor[/bold yellow]

[bold cyan]"Each one was extraordinary. Each one has a story.
Let's meet them properly."[/bold cyan]

[bold white]Time to meet the giants![/bold white]
""",
    "herbivores_vs_carnivores": """
Puck held up two very different teeth on the Primer's page —
one flat and wide, the other sharp and serrated like a steak knife.

[bold cyan]"In the world of dinosaurs,"[/bold cyan] Puck said,
[bold cyan]"there were two great teams: the plant eaters
and the meat eaters. And you can tell which team a dinosaur
played for just by looking at its teeth."[/bold cyan]

The page split in two — peaceful herbivores on one side,
fierce carnivores on the other.

[bold cyan]"But don't think the plant eaters were pushovers.
Some of them had horns, clubs, armour, and spikes.
Being a herbivore didn't mean being helpless!"[/bold cyan]

[bold white]Let's discover who ate what — and how they defended themselves![/bold white]
""",
    "fossils": """
Puck knelt beside something half-buried in the Primer's page —
a long, curved shape poking out of layered stone.

[bold cyan]"This,"[/bold cyan] Puck said softly, brushing away tiny grains of sand,
[bold cyan]"is how we know any of this. Without fossils,
we would never even know dinosaurs existed."[/bold cyan]

The shape became clearer — a bone, turned to stone,
preserved for millions of years inside the rock.

[bold cyan]"Fossils are clues. And the people who find them
and put the puzzle together — paleontologists —
are some of the greatest detectives in the world."[/bold cyan]

[bold white]Let's learn how bones become stone and stone becomes knowledge![/bold white]
""",
    "flying_and_swimming": """
Puck pointed up at the sky, then down into a deep blue ocean
on the Primer's page.

[bold cyan]"Dinosaurs ruled the land,"[/bold cyan] Puck said.
[bold cyan]"But the sky and the sea had their OWN rulers —
amazing reptiles that were just as extraordinary as any dinosaur,
even though they technically weren't dinosaurs at all."[/bold cyan]

A shadow with vast wings glided overhead.
Something with a very long neck rose from the waves below.

[bold cyan]"Pterosaurs in the air. Plesiosaurs and ichthyosaurs
and mosasaurs in the water. A whole world of creatures
most people forget about."[/bold cyan]

[bold white]Let's meet the rulers of the prehistoric sky and sea![/bold white]
""",
    "extinction": """
The Time Machine dial jumped forward — to exactly 66 million years ago.

The Primer's page went very still. Puck spoke quietly.

[bold cyan]"Something is about to happen,"[/bold cyan] Puck said.
[bold cyan]"Something that will change the world forever.
A rock from space — an asteroid — is falling toward Earth
right now. It's about 10 kilometres wide.
And when it hits…"[/bold cyan]

The page flashed white.

[bold cyan]"…everything changes. Most of the dinosaurs,
the pterosaurs, the great sea reptiles —
gone. In a geological instant."[/bold cyan]

[bold cyan]"But not everything died. And what survived
will surprise you."[/bold cyan]

[bold white]Let's discover what happened on the day the dinosaurs disappeared.[/bold white]
""",
    "after_dinosaurs": """
The dust settled. The Primer's pages slowly brightened again.

Where dinosaurs once thundered, the world was quiet —
but not empty. Small, furry creatures crept out from burrows.
Birds sang in the recovering trees. And slowly, over millions
of years, new giants began to appear.

[bold cyan]"The dinosaurs were gone,"[/bold cyan] Puck said gently.
[bold cyan]"But life didn't stop. Mammals — tiny, timid mammals
that had hidden in the shadows for 160 million years —
finally had their chance. And oh, what they did with it."[/bold cyan]

[bold cyan]"Woolly mammoths. Saber-tooth cats. Giant sloths.
And eventually… humans."[/bold cyan]

[bold white]Let's see what happened after the dinosaurs — all the way to us.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "what_are_dinosaurs": """
[bold green]The Mesozoic Era glows on the Time Machine![/bold green]

Three great periods shine: Triassic, Jurassic, Cretaceous —
230 million years of dinosaur history, all understood.

[bold cyan]"You know when they lived, how long they ruled,
and what made a dinosaur a dinosaur,"[/bold cyan] Puck says proudly.
[bold cyan]"Now let's meet the most famous ones face to face."[/bold cyan]

The pages rustle. Enormous shapes are waiting...
""",
    "famous_dinosaurs": """
[bold green]Five legendary dinosaurs stand together on the page![/bold green]

T-Rex with its mighty jaws. Triceratops with three proud horns.
Stegosaurus with diamond plates. Brachiosaurus reaching for the sky.
Velociraptor, small and clever and feathered.

[bold cyan]"You know them now,"[/bold cyan] Puck says.
[bold cyan]"Not just their names — their stories.
That's what a real dinosaur expert does."[/bold cyan]

Teeth of different shapes appear on the next page. Time to learn about diets...
""",
    "herbivores_vs_carnivores": """
[bold green]The great food chain of the Mesozoic is complete![/bold green]

Plant eaters and meat eaters, teeth and claws,
armour and horns — the whole picture.

[bold cyan]"You understand who ate what, and how the plant eaters
fought back,"[/bold cyan] Puck says with a nod.
[bold cyan]"Every ecosystem needs both sides.
Even 200 million years ago, nature kept its balance."[/bold cyan]

Something is half-buried in the rock on the next page...
""",
    "fossils": """
[bold green]The fossil record glows with ancient secrets![/bold green]

Bones turned to stone. Footprints preserved in rock.
Scientists with brushes and hammers, piecing together the past.

[bold cyan]"Without fossils, we'd know nothing,"[/bold cyan] Puck says.
[bold cyan]"Every single thing we've learned about dinosaurs
came from someone finding a fossil and asking:
'What was this? When did it live? What can it tell us?'"[/bold cyan]

Shadows pass overhead. Something is flying above the ancient sea...
""",
    "flying_and_swimming": """
[bold green]The sky and the sea come alive with prehistoric wonder![/bold green]

Pterosaurs soar overhead. Plesiosaurs glide through deep waters.
Ichthyosaurs dart like ancient dolphins. Mosasaurus prowls the depths.

[bold cyan]"Now you know the truth,"[/bold cyan] Puck says.
[bold cyan]"The dinosaurs ruled the land — but the air and the ocean
had their own magnificent rulers. And none of them
were actually dinosaurs!"[/bold cyan]

The sky darkens. Something is falling from above...
""",
    "extinction": """
[bold green]The great extinction is understood![/bold green]

The asteroid. The dust. The darkness. The cold.
And then — the survivors, creeping back into the light.

[bold cyan]"Sixty-six million years ago, one rock from space
changed everything,"[/bold cyan] Puck says quietly.
[bold cyan]"But life found a way. Small mammals survived.
Birds survived. And from that survival came
the whole world we know today."[/bold cyan]

[bold cyan]"Including the most amazing part: birds ARE dinosaurs.
The dinosaurs never fully left."[/bold cyan]

The pages warm up. New creatures are emerging...
""",
    "after_dinosaurs": """
[bold green]The whole story of life glows from beginning to end![/bold green]

From the first dinosaurs 230 million years ago, through the great
extinction, through the Ice Age, through mammoths and saber-tooth cats,
all the way to the first humans walking out of Africa.

[bold cyan]"You've traveled the entire journey,"[/bold cyan] Puck says,
wings spread wide. [bold cyan]"Hundreds of millions of years
of the most incredible story ever told —
the story of life on Earth."[/bold cyan]

Puck gently closes the Time Machine.

[bold white]Time Traveler. Fossil Hunter. Dino Expert. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "what_are_dinosaurs": "Puck crosses tiny arms and looks very serious. [bold yellow]\"Here's the question that trips up almost everyone — even grown-ups. Think carefully about what you've learned!\"[/bold yellow]",
    "famous_dinosaurs": "The ground shakes. A shadow falls across the page. [bold yellow]\"The King of the Dinosaurs is here. Can you identify it from its description alone?\"[/bold yellow]",
    "herbivores_vs_carnivores": "Puck looks at the vast herds of dinosaurs on the page. [bold yellow]\"Here's a question about the balance of nature — one that's just as true today as it was 200 million years ago.\"[/bold yellow]",
    "fossils": "Puck holds up a piece of layered rock and turns it over carefully. [bold yellow]\"This is the big one — the question that connects everything about fossils together. Why THIS kind of rock?\"[/bold yellow]",
    "flying_and_swimming": "Puck looks at the sky, then at the sea, then back at you. [bold yellow]\"One big truth connects all these amazing creatures. Can you see it?\"[/bold yellow]",
    "extinction": "Puck points to a bird singing on a branch and grins. [bold yellow]\"If birds are dinosaurs... then what does that mean about extinction? Think about it!\"[/bold yellow]",
    "after_dinosaurs": "Puck closes the Time Machine dial for the last time. [bold yellow]\"One final question about the greatest force in all of nature — the force that connects every living thing on Earth.\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "mesozoic_scholar": (
        "Mesozoic Scholar",
        "Learned when dinosaurs lived and what made them special!",
    ),
    "dino_spotter": (
        "Dino Spotter",
        "Met the most famous dinosaurs and learned their secrets!",
    ),
    "food_chain_master": (
        "Food Chain Master",
        "Understood the difference between herbivores and carnivores!",
    ),
    "fossil_finder": (
        "Fossil Finder",
        "Discovered how fossils form and how paleontologists study them!",
    ),
    "sky_sea_explorer": (
        "Sky & Sea Explorer",
        "Met the amazing pterosaurs, plesiosaurs, and other prehistoric reptiles!",
    ),
    "extinction_expert": (
        "Extinction Expert",
        "Learned the truth about the asteroid and which animals survived!",
    ),
    "time_traveler": (
        "Time Traveler",
        "Journeyed from the Ice Age to early humans — the whole story of life!",
    ),
}
