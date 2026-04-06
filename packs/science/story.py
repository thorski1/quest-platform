"""
story.py — Narrative for the Science skill pack.

Nell and Puck explore the natural world — living things, sky and weather,
the human body, and how things work.
"""

INTRO_STORY = """
[bold yellow]THE WORLD OF WONDERING[/bold yellow]

[bold cyan]"Close your eyes,"[/bold cyan] Puck said.

Nell closed them.

[bold cyan]"Now open them slowly. What do you see?"[/bold cyan]

Nell looked around. Sunlight. A tree. A bird on a branch.
A cloud drifting. Her own hands.

[bold white]"Everything,"[/bold white] she said.

[bold cyan]"Exactly,"[/bold cyan] Puck said, settling on her shoulder.
[bold cyan]"Everything around you is a puzzle. The sun, the rain,
why trees grow up instead of sideways, how your heart beats
without you thinking about it — all of it follows rules.
And once you know the rules, the world stops being confusing
and starts being [italic]wonderful.[/italic]"[/bold cyan]

The Primer glowed with a soft green light.

[bold cyan]"Scientists are just people who ask the question [italic]why[/italic]
about everything they see. You've been doing it your whole life —
you just didn't have the word for it."[/bold cyan]

Nell looked at the tree. At the bird. At the cloud.

She was going to figure out how all of it worked.

[bold white]Let's explore![/bold white]
"""

ZONE_INTROS = {
    "the_human_body": """
Puck unfurled a glowing map that looked exactly like a person —
every organ lit up in a different color.

[bold cyan]"Your body,"[/bold cyan] Puck whispered, [bold cyan]"is the most amazing machine
that has ever existed. It breathes, pumps, thinks,
moves, heals — all at once, all the time,
[italic]without you even having to ask it to.[/italic]"[/bold cyan]

The glowing figure pulsed softly — a heartbeat.

[bold white]Explore the map. Your body has stories to tell.[/bold white]
""",
    "living_things": """
[bold cyan]"First question,"[/bold cyan] Puck said. [bold cyan]"What's alive?"[/bold cyan]

Nell looked around. The tree was alive. The bird was alive.
The rock on the ground... probably not?

[bold cyan]"Living things do certain things that rocks can't do,"[/bold cyan]
Puck said. [bold cyan]"They grow. They eat. They breathe.
They can have babies. Once you know the rules,
you can tell what's living and what's not — and that's
the beginning of understanding life itself."[/bold cyan]

[bold white]What makes something alive?[/bold white]
""",
    "sky_and_weather": """
Puck zoomed up high and pointed at the sky.

[bold cyan]"Everything up there is happening for a reason.
The sun isn't just bright — it's keeping you warm,
making plants grow, pulling water into clouds.
The rain isn't just wet — it's the same water cycling
round and round, forever."[/bold cyan]

[bold white]What's happening in the sky above us?[/bold white]
""",
    "body_basics": """
[bold cyan]"You've been living in that body your whole life,"[/bold cyan]
Puck said, [bold cyan]"but do you know what's happening inside it?"[/bold cyan]

Nell looked at her hand. Her heart was beating right now.
Her lungs were breathing. Her eyes were seeing.
All without her doing anything at all.

[bold cyan]"Your body is the most amazing machine ever built.
Let's learn how it works."[/bold cyan]

[bold white]How does your amazing body work?[/bold white]
""",
    "how_things_work": """
[bold cyan]"Cause and effect,"[/bold cyan] Puck said.
[bold cyan]"That's the secret of science. Every effect has a cause.
Every cause has an effect. Once you find the pattern,
you can [italic]predict[/italic] what happens next — and that's
[italic]power.[/italic]"[/bold cyan]

A wheel turned. A lever lifted. A shadow moved.

[bold white]What happens when you push, pull, or spin?[/bold white]
""",
    "simple_machines": """
[bold cyan]"Long before electricity,"[/bold cyan] Puck said, eyes wide,
[bold cyan]"before engines or computers — people built
the pyramids, the great cathedrals, whole cities.
With their hands. And six tools."[/bold cyan]

Six. That's all.

[bold cyan]"The lever. The wheel and axle. The inclined plane.
The pulley. The wedge. The screw.
These are the six ancient tools that built every civilization
that ever existed. And once you understand them,
you'll see them [italic]everywhere.[/italic]"[/bold cyan]

[bold white]What's the secret of each simple machine?[/bold white]
""",
    "earth_and_space": """
Puck pointed straight up.

[bold cyan]"We live on a giant ball,"[/bold cyan] Puck said, [bold cyan]"spinning through
space, flying around a star, while a moon circles around us,
and billions of other suns burn silently in every direction."[/bold cyan]

Nell looked up at the blue sky.

[bold cyan]"On a clear night you can see some of those other suns.
They look like tiny dots. They're not tiny.
They're enormous — just very, very far away."[/bold cyan]

[bold white]What do you know about our place in the sky?[/bold white]
""",
    "matter_and_energy": """
[bold cyan]"Everything around you,"[/bold cyan] Puck said, gesturing at the walls,
the floor, the air, [bold cyan]"is made of matter.
And all matter exists in one of three states:
solid, liquid, or gas."[/bold cyan]

[bold cyan]"Your pencil. The water in your glass.
The air filling your lungs right now.
All matter — just in different forms.
And here's the amazing part:"[/bold cyan] Puck paused for effect.

[bold cyan]"They can change from one to another."[/bold cyan]

[bold white]Let's find out what's solid, what's liquid, and what's gas![/bold white]
""",
    "weather_watch": """
Puck took Nell's hand and led her up a tall, winding staircase.

At the top, the whole sky stretched out in every direction.
Clouds drifted. The wind stirred. A distant rumble.

[bold cyan]"The sky is a story that's always changing,"[/bold cyan] Puck said softly.
[bold cyan]"Every cloud, every gust, every snowflake follows rules —
and once you know the rules, you can read
what the sky is telling you."[/bold cyan]

Nell watched a dark cloud rolling in from the west.

[bold white]What is the sky saying today?[/bold white]
""",
    "animal_world": """
The Primer's pages began to rustle, as if something
were moving inside them. Leaves appeared.
Then sounds — chirping, rustling, a distant splash.

Puck grinned. [bold cyan]"Every creature has something amazing about it.
The way a dolphin breathes. The way a frog
lives in two worlds. The way a caterpillar
becomes something completely different."[/bold cyan]

[bold cyan]"The animal kingdom is one of the most wonderful things
there is — and you're part of it."[/bold cyan]

[bold white]What do you know about the creatures we share this world with?[/bold white]
""",
    "ecosystems_and_food_chains": """
[bold cyan]THE WEB OF LIFE[/bold cyan]

Puck spread out across a patch of grass at the edge of the forest,
watching a butterfly land on a flower, a bird watching the butterfly,
a fox watching from the shadows.

[bold cyan]"See it?"[/bold cyan] Puck said quietly.
[bold cyan]"Everything is watching everything else.
Everything is eating, being eaten, growing, decomposing.
The grass becomes a rabbit, the rabbit becomes a fox,
the fox becomes the soil, the soil becomes the grass."[/bold cyan]

The butterfly flew away. The bird watched it go.

[bold cyan]"A chain. A web. A circle.
None of it works without all of it.
And when one piece breaks —"[/bold cyan]

Puck snapped a small twig.

[bold cyan]"— everything feels it."[/bold cyan]

[bold white]The web of life is waiting for you to understand it.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "the_human_body": """
[bold green]The Body Map glows from head to toe![/bold green]

Every organ lights up: the heart pumping, the lungs breathing,
the brain sparkling, the muscles ready.

[bold cyan]"You know yourself a little better now,"[/bold cyan] Puck says quietly.
[bold cyan]"206 bones. A heart that beats 100,000 times a day.
Lungs that breathe in what you need and breathe out
what you don't. A brain running everything — even now,
even in your sleep."[/bold cyan]

[bold white]That machine is you. And it is extraordinary.[/bold white]
""",
    "living_things": """
[bold green]The garden glows![/bold green]

Every living thing around you seems a little more remarkable now.
You know what makes them alive — growing, eating, breathing, changing.

[bold cyan]"Wherever you go,"[/bold cyan] Puck says, [bold cyan]"you'll see living things
differently now. Every plant is working. Every insect has a job.
Life is everywhere."[/bold cyan]

The sky is next. Look up!
""",
    "sky_and_weather": """
[bold green]The sky opens up![/bold green]

Clouds, rain, seasons, the sun — you understand the patterns now.

[bold cyan]"The weather isn't random,"[/bold cyan] Puck says. [bold cyan]"There are reasons.
And once you know why it rains, why it gets cold in winter,
why the sun rises in the east — you'll never look at a
cloudy day the same way."[/bold cyan]

Now let's look closer — at your own amazing body!
""",
    "body_basics": """
[bold green]Your body hums with understanding![/bold green]

[bold cyan]"Five senses. A heart that never stops. Lungs breathing
without being told. Bones making you strong."[/bold cyan]

Puck nods with deep satisfaction.

[bold cyan]"Taking care of your body means understanding it.
And now you do."[/bold cyan]

One more zone — how do things around us work?
""",
    "how_things_work": """
[bold green]The world of cause and effect is yours![/bold green]

[bold cyan]"You know why things happen now,"[/bold cyan] Puck says.
[bold cyan]"You know that ramps make heavy things easier to lift,
that shadows are made by blocking light,
that magnets pull on some things and not others."[/bold cyan]

A long pause.

[bold cyan]"The whole world works on rules like these.
And now you know the rules."[/bold cyan]
""",
    "simple_machines": """
[bold green]The workshop rings with the sound of discovery![/bold green]

[bold cyan]"Six tools,"[/bold cyan] Puck says with great satisfaction.
[bold cyan]"Lever, wheel and axle, inclined plane,
pulley, wedge, and screw.
You now understand every simple machine
that built human civilization."[/bold cyan]

[bold cyan]"Next time you see a ramp, a jar lid, a bicycle —
you'll know exactly what's happening.
And that knowledge is yours forever."[/bold cyan]
""",
    "earth_and_space": """
[bold green]The sky observatory lights up![/bold green]

[bold cyan]"Earth goes around the Sun. The Moon goes around Earth.
Day and night from spinning. A year from orbiting.
The Moon's phases from where we stand."[/bold cyan]

Puck looks at the stars beginning to appear.

[bold cyan]"And every single one of those stars is a sun.
Burning. Enormous. Some of them might have their
own Earths going around them."[/bold cyan]

A pause full of wonder.

[bold cyan]"Isn't that the most AMAZING thing?"[/bold cyan]
""",
    "matter_and_energy": """
[bold green]The matter lab glows with understanding![/bold green]

[bold cyan]"Solid, liquid, gas,"[/bold cyan] Puck says.
[bold cyan]"And they transform. Melt. Freeze. Evaporate.
The water in your glass might have been a glacier once.
Or a cloud. Or part of the ocean."[/bold cyan]

[bold cyan]"Matter doesn't disappear — it just changes.
And now you understand how."[/bold cyan]

[bold white]That's the science of the world all around you![/bold white]
""",
    "weather_watch": """
[bold green]The watchtower glows in the afternoon light![/bold green]

Nell looks out at the sky — the same sky as before,
but somehow richer now.

[bold cyan]"You can read it,"[/bold cyan] Puck says. [bold cyan]"Dark clouds bring rain.
Wind is moving air. Winter brings snow.
A rainbow needs both sun and rain."[/bold cyan]

[bold cyan]"The sky has always been telling its story.
Now you know how to listen."[/bold cyan]
""",
    "animal_world": """
[bold green]The pages of the Animal Kingdom settle with a gentle hush.[/bold green]

[bold cyan]"Herbivores. Mammals. Amphibians.
Metamorphosis. Cold-blooded. Warm-blooded."[/bold cyan]

Puck looks at Nell with sparkling eyes.

[bold cyan]"You share this world with millions of other creatures,
each one remarkable in its own way.
And now you understand a little more about how they work —
and how you work too."[/bold cyan]

[bold white]The animal kingdom is yours to explore![/bold white]
""",
    "ecosystems_and_food_chains": """
[bold green]The Web of Life is fully mapped![/bold green]

Producers, herbivores, carnivores, decomposers —
every link in the chain understood.

[bold cyan]"You know something now that most adults don't really think about,"[/bold cyan]
Puck said.
[bold cyan]"That everything is connected. That removing one thread
can unravel the whole web.
That a wolf can change a river."[/bold cyan]

Puck smiled.

[bold cyan]"That's not just science.
That's wisdom."[/bold cyan]

[bold white]The World of Wondering is yours. The web of life holds you too.[/bold white]
""",
}

BOSS_INTROS = {
    "the_human_body": "The glowing figure on the map does a small jumping jack. [bold yellow]\"Final question — it's about taking care of that incredible body of yours. Think about what really helps!\"[/bold yellow]",
    "living_things": "Puck points to the tallest tree in the garden. [bold yellow]\"The hardest living things question is waiting at the top. Are you ready?\"[/bold yellow]",
    "sky_and_weather": "A big storm cloud gathers overhead. [bold yellow]\"This is the toughest sky question. Think carefully — you know this!\"[/bold yellow]",
    "body_basics": "A giant diagram of the body appears. [bold yellow]\"Final body question — it's a tricky one. But you've learned so much!\"[/bold yellow]",
    "how_things_work": "A tall machine with gears and levers stands before you. [bold yellow]\"The hardest 'how things work' question. All your science knowledge comes together here!\"[/bold yellow]",
    "simple_machines": "A mysterious screw glints in the lamplight. [bold yellow]\"Every civilization used this one. It looks simple but it's hiding a brilliant secret. Think it through!\"[/bold yellow]",
    "earth_and_space": "The night sky fills with thousands of stars. [bold yellow]\"What are all those tiny lights, really? This is the question that will change how you see the night sky forever.\"[/bold yellow]",
    "matter_and_energy": "A puddle is slowly disappearing on a warm day. [bold yellow]\"The water is going somewhere. Where? This is the final mystery of the Matter Lab!\"[/bold yellow]",
    "weather_watch": "A strange sky appears — clouds, temperature, possibilities. [bold yellow]\"This is the toughest weather question. Think about what happens to water when it gets very, very cold!\"[/bold yellow]",
    "animal_world": "Two animals stand side by side — one warm-blooded, one cold-blooded. [bold yellow]\"What's really the difference between them? This is the big animal question. You can do it!\"[/bold yellow]",
    "ecosystems_and_food_chains": "A food web stretches across the whole lab — arrows connecting wolves to deer to grass to soil and back again. [bold yellow]\"This is the biggest question of all: what happens when one piece of the web breaks? Think through the whole chain!\"[/bold yellow]",
}
