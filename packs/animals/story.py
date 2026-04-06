"""
story.py — Narrative for the Animals skill pack.

Puck opens the Primer to pages that move — every animal in the world
waiting to be discovered. From tiny insects to giant whales, from
backyard pets to creatures of the deep, the animal kingdom unfolds.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Animal Kingdom[/bold yellow]

The Primer's pages rustled on their own — and then they [italic]moved.[/italic]

A tiny hummingbird zipped across the paper. A whale breached in
the margin. A line of ants marched along the spine of the book,
carrying crumbs of gilded ink.

[bold cyan]"Animals!"[/bold cyan] Puck appeared in a burst of light, wings buzzing
with excitement. [bold cyan]"Every creature that walks, swims, flies,
crawls, slithers, or hops — they're all in here. The whole
living, breathing, roaring, chirping animal kingdom."[/bold cyan]

The girl watched a chameleon change colour right there on the page.
[bold white]"They're all alive?"[/bold white]

[bold cyan]"In the Primer, everything is alive."[/bold cyan] Puck landed on
the chameleon's head. [bold cyan]"And every animal has a story.
How it's born. Where it lives. What it eats. What makes it
extraordinary. Some can see in the dark. Some can regrow
a lost arm. Some travel seventy thousand kilometres a year
and never get lost."[/bold cyan]

Puck looked up with shining eyes.

[bold cyan]"Mammals and birds and reptiles and fish. Jungles and oceans
and frozen tundra. Predators and prey. The tiny and the colossal.
[italic]All of it.[/italic] Ready for you."[/bold cyan]

A golden paw print appeared on the next page, glowing softly.

[bold cyan]"Follow the tracks?"[/bold cyan]

[bold white]Your journey through the animal kingdom begins now.[/bold white]
"""

ZONE_INTROS = {
    "animal_groups": """
Puck opened the Primer to its first chapter of creatures. Six great
circles glowed on the page, each one filled with moving animals.

[bold cyan]"Every animal on Earth belongs to a group,"[/bold cyan] Puck said.
[bold cyan]"Mammals — that's us. Birds with their feathers. Reptiles
basking in the sun. Amphibians living double lives. Fish breathing
underwater. And insects — six legs, everywhere, more of them
than anything else alive."[/bold cyan]

Six golden labels appeared:
[bold yellow]Mammals · Birds · Reptiles · Amphibians · Fish · Insects[/bold yellow]

[bold cyan]"Each group has something special that makes it different
from all the others. Let's find out what!"[/bold cyan]

[bold white]Let's discover the great animal families![/bold white]
""",
    "habitats": """
The page turned, and the world opened up — not as a map this time,
but as a living painting. Green jungles steamed. Golden deserts shimmered.
Dark oceans churned. White ice glittered.

[bold cyan]"A habitat,"[/bold cyan] Puck said, wings brushing a tiny illustrated fern,
[bold cyan]"is an animal's home. Not just a place — the [italic]right[/italic] place.
The place where it finds everything it needs to survive: food,
water, shelter, and the right temperature."[/bold cyan]

Five habitats glowed across the page:
[bold yellow]Rainforest · Ocean · Desert · Arctic · Grassland[/bold yellow]

[bold cyan]"Put a polar bear in the desert and it won't last a day.
Put a camel in the Arctic and it would shiver to pieces.
Every animal is perfectly matched to its home."[/bold cyan]

[bold white]Let's explore where animals live![/bold white]
""",
    "food_chains": """
Puck traced a golden line from a blade of grass to a grasshopper,
from the grasshopper to a frog, from the frog to a snake,
from the snake to a hawk circling high above.

[bold cyan]"Everything is connected,"[/bold cyan] Puck said quietly.
[bold cyan]"The grass feeds the grasshopper. The grasshopper feeds the frog.
The frog feeds the snake. The snake feeds the hawk. Energy flows
from the sun through plants through animals — a chain of life."[/bold cyan]

Three golden words appeared:
[bold yellow]Herbivore · Carnivore · Omnivore[/bold yellow]

[bold cyan]"Plant eaters. Meat eaters. Everything eaters.
And predators — the hunters — and prey — the hunted.
Nature keeps it all in balance."[/bold cyan]

[bold white]Let's follow the chain of life![/bold white]
""",
    "baby_animals": """
The page turned to something soft and warm. Tiny creatures everywhere —
a kitten curled in a ball, a chick pecking through its shell,
a tadpole growing legs, a joey peeking from a pouch.

[bold cyan]"Every animal was a baby once,"[/bold cyan] Puck said with a gentle smile.
[bold cyan]"Some hatch from eggs. Some are born live. Some start life looking
completely different from their parents — a caterpillar doesn't look
anything like a butterfly, but that's what it becomes!"[/bold cyan]

Puck landed on a nest of speckled eggs.

[bold cyan]"Baby animals have special names, too. A puppy. A cub.
A joey. A fry. A kit. Each one with a whole life ahead of it."[/bold cyan]

[bold white]Let's meet the babies of the animal kingdom![/bold white]
""",
    "animal_superpowers": """
The page crackled with energy. Lightning bolts, sound waves,
colour-shifting skin, and golden speed lines — the Primer was
showing off.

[bold cyan]"If animals were superheroes,"[/bold cyan] Puck said, eyes wide,
[bold cyan]"they wouldn't need capes. Bats see with sound. Chameleons
disappear. Electric eels shoot lightning. Starfish regrow arms.
Arctic terns fly from pole to pole — [italic]seventy thousand
kilometres[/italic] — every single year."[/bold cyan]

Puck spun in the air with excitement.

[bold cyan]"Nature gave animals superpowers that no comic book
could make up. Every one of them is real."[/bold cyan]

[bold white]Let's discover nature's most incredible abilities![/bold white]
""",
    "endangered_species": """
The page turned, and the colours dimmed. The animals on this page
moved more slowly. Some seemed to flicker, like candle flames
in the wind.

[bold cyan]"This,"[/bold cyan] Puck said softly, [bold cyan]"is the hardest chapter.
Some animals are disappearing. Their forests are being cut down.
Their oceans are being polluted. Their numbers are falling."[/bold cyan]

A red glow pulsed at the edge of the page — a warning.

[bold cyan]"But here's the thing that matters most: it's not too late.
People are fighting to save them. And kids — kids just like you —
can help. Every single day."[/bold cyan]

Puck's wings brightened with determination.

[bold white]Let's learn about the animals that need us most.[/bold white]
""",
    "pets_and_care": """
The page turned to something familiar — not a jungle or an ocean,
but a cozy room. A dog wagged its tail. A cat stretched on a
windowsill. A goldfish swam in gentle circles. A hamster ran
on its wheel.

[bold cyan]"Pets!"[/bold cyan] Puck said warmly. [bold cyan]"The animals that share
our homes. Dogs and cats and fish and rabbits — animals
that trust us to take care of them."[/bold cyan]

Puck sat on the illustrated dog's head.

[bold cyan]"Having a pet is wonderful — but it's also a promise.
A promise to feed them, keep them safe, take them to the vet,
and love them for their whole life. Let's learn what that
really means."[/bold cyan]

[bold white]Let's learn about our animal friends![/bold white]
""",
    "ocean_creatures": """
The final chapter opened, and the page flooded with blue.

Deep, dark, endless blue. The surface shimmered far above.
Below, the water plunged into shadow, and then into absolute
darkness — the deep ocean, where sunlight never reaches.

[bold cyan]"The ocean,"[/bold cyan] Puck whispered, floating in a bubble
of Primer-light, [bold cyan]"is the last great mystery.
Blue whales bigger than dinosaurs. Octopuses with three hearts
and nine brains. Coral cities built by creatures smaller than
your fingernail. And in the deepest dark... animals that make
their own light."[/bold cyan]

Tiny glowing dots appeared in the darkness below.

[bold cyan]"Ready to dive?"[/bold cyan]

[bold white]Let's explore the wonders of the deep![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "animal_groups": """
[bold green]All six animal families glow on the page![/bold green]

Mammals with their fur and milk. Birds with their feathers.
Reptiles with their scales. Amphibians with their double lives.
Fish with their gills. Insects with their six legs.

[bold cyan]"You know the families now,"[/bold cyan] Puck says proudly.
[bold cyan]"Every animal you ever see — you'll know which group
it belongs to. That's real knowledge."[/bold cyan]

The page turns to a world of wild places. The habitats are waiting...
""",
    "habitats": """
[bold green]Five habitats shine across the page — each one alive with creatures![/bold green]

Green rainforests. Golden deserts. Blue oceans. White arctic ice.
Golden grasslands stretching to the horizon.

[bold cyan]"Every animal has a home,"[/bold cyan] Puck says softly.
[bold cyan]"And now you know why they live where they do.
The right place, the right food, the right temperature.
It all fits together perfectly."[/bold cyan]

Golden links appear on the next page. The food chains are calling...
""",
    "food_chains": """
[bold green]The chain of life glows from bottom to top![/bold green]

Producers. Herbivores. Carnivores. Omnivores. Apex predators.
All connected in a web of energy that starts with the sun.

[bold cyan]"Everything is connected,"[/bold cyan] Puck says.
[bold cyan]"Pull one link out of the chain and the whole thing
wobbles. That's why every animal matters — even the ones
people don't think about."[/bold cyan]

Something soft and small moves on the next page. The babies are waiting...
""",
    "baby_animals": """
[bold green]The nursery page glows with warmth![/bold green]

Joeys in pouches. Chicks breaking through shells. Caterpillars
becoming butterflies. Tiny turtles racing to the sea.

[bold cyan]"Every great animal,"[/bold cyan] Puck says gently,
[bold cyan]"started as something small and fragile.
A lion was once a cub. A whale was once a calf.
A butterfly was once a caterpillar. The beginning
is never the end of the story."[/bold cyan]

Lightning crackles on the next page. The superpowers are waiting...
""",
    "animal_superpowers": """
[bold green]The page blazes with incredible abilities![/bold green]

Echolocation. Camouflage. Migration. Regeneration. Electricity.
Speed beyond belief.

[bold cyan]"Nature is the greatest inventor,"[/bold cyan] Puck says in awe.
[bold cyan]"No laboratory in the world has matched what evolution
built over millions of years. These aren't superpowers —
they're real life. And real life is more amazing than fiction."[/bold cyan]

The page dims. A softer, more solemn chapter waits ahead...
""",
    "endangered_species": """
[bold green]A warm glow of hope spreads across the page![/bold green]

Pandas recovering. Eagles soaring again. Kids planting trees.
Conservation working, slowly but surely.

[bold cyan]"It's not all sad,"[/bold cyan] Puck says, and there's hope
in those bright eyes. [bold cyan]"People ARE helping. Numbers ARE
climbing back. Forests ARE being replanted. And now you know
why it matters — and what you can do."[/bold cyan]

The page turns to something warm and familiar. Our pets are waiting...
""",
    "pets_and_care": """
[bold green]The cozy page glows with love![/bold green]

Dogs and cats and fish and horses — all cared for,
all understood, all loved the way they deserve.

[bold cyan]"A pet isn't a toy,"[/bold cyan] Puck says warmly.
[bold cyan]"It's a friend. A responsibility. A life
that depends on you. And if you take that seriously —
there's nothing better in the world."[/bold cyan]

The page fills with deep blue. The ocean is calling, one last time...
""",
    "ocean_creatures": """
[bold green]The ocean glows from surface to abyss — every depth alive with wonder![/bold green]

Blue whales and dolphins at the surface. Coral cities in the shallows.
Octopuses and sharks in the middle waters. And in the deepest dark —
creatures that make their own light, glowing like underwater stars.

[bold cyan]"You've done it."[/bold cyan] Puck's wings spread wide, glowing
brighter than ever. [bold cyan]"Every animal family. Every habitat.
Food chains and baby animals and superpowers and endangered species
and pets and the deep ocean. The whole animal kingdom — explored,
understood, and loved."[/bold cyan]

Puck lands on the girl's shoulder.

[bold cyan]"The animals were always there. Now you [italic]see[/italic] them."[/bold cyan]

[bold white]Animal Guardian. Nature's Champion. Keeper of the Wild. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "animal_groups": "Puck holds up a tiny beetle, turning it slowly in the Primer's light. [bold yellow]\"This little creature belongs to the largest group of animals on Earth. Every single one of them has exactly the same number of legs. How many?\"[/bold yellow]",
    "habitats": "Puck places four animal illustrations on the page — a toucan, a jaguar, a tree frog, and one that doesn't belong. [bold yellow]\"Three of these animals live in the tropical rainforest. One would freeze the others out — literally! Which one doesn't belong?\"[/bold yellow]",
    "food_chains": "A great shadow passes across the page — something powerful, ancient, and feared. [bold yellow]\"At the very top of the ocean food chain sits a hunter that nothing else dares to chase. Can you name this apex predator?\"[/bold yellow]",
    "baby_animals": "The page fills with moonlight and soft sand. Tiny shapes begin to move. [bold yellow]\"These babies hatch on a beach and must make the most dangerous journey of their lives — alone, under the stars. Who are they?\"[/bold yellow]",
    "animal_superpowers": "A golden blur streaks across the page — so fast it leaves a trail of fire behind it. [bold yellow]\"This animal goes from zero to a hundred kilometres per hour in three seconds flat. Faster than a sports car! What is it?\"[/bold yellow]",
    "endangered_species": "A tiny, shy shape appears in the dark blue water of the Gulf of California. [bold yellow]\"Fewer than ten of these small, gentle creatures remain on Earth. It's the most endangered marine mammal in the world. Can you name it?\"[/bold yellow]",
    "pets_and_care": "A powerful, striped animal stares out from the page with fierce golden eyes. [bold yellow]\"Three of these animals have lived happily alongside humans for thousands of years. But this one? This one belongs in the wild. Which one is it?\"[/bold yellow]",
    "ocean_creatures": "The page goes completely dark. Then, one by one, tiny lights appear in the abyss — living lights, made by creatures in the deepest ocean. [bold yellow]\"What is this magical ability called — when living things make their own light in the darkness?\"[/bold yellow]",
}
