"""
story.py — Narrative text for Baking Fundamentals
"""

INTRO_STORY = """
The kitchen is warm. Not from the sun this time — from the oven, preheating to 350 degrees,
radiating a steady, enveloping heat that makes the whole room feel like a blanket. Flour
dusts the counter. A stand mixer sits ready. The smell of vanilla extract lingers in the
air from something that came out of the oven an hour ago.

[bold yellow]Chef Sofia[/bold yellow] ties on a clean apron and sets a digital scale on the counter.

"Baking is different," she says, leveling a measuring cup with the back of a knife.
"Cooking forgives. Baking does not. Cooking is jazz — improvisation, intuition, a
pinch of this, a splash of that. Baking is [bold white]chemistry[/bold white]."

She taps the scale.

"Flour, fat, sugar, eggs, leavening, liquid. Six categories. Every baked good in existence
is some combination of those six things in different ratios. Bread is high flour, low sugar.
Cake is high sugar, low flour. Cookies live in between. The ratios determine the texture,
the structure, the crumb, the rise."

She opens a bag of flour and weighs out exactly 120 grams.

"In cooking, a tablespoon more or less of olive oil is a preference. In baking, a tablespoon
more or less of flour is the difference between a tender crumb and a doorstop."

She looks up.

"I can teach you to feel it eventually — the way the dough should look, the way the batter
should flow. But first, we learn the science. Because the science is what tells you
[bold white]why[/bold white] it works, and that's what lets you fix it when it doesn't."

[bold white]"Preheat is done. Let's bake."[/bold white]
"""

ZONE_INTROS = {
    "baking_science": """
[bold yellow]== THE SCIENCE LAB ==[/bold yellow]

Chef Sofia sets out a row of ingredients: flour, baking soda, baking powder, yeast,
eggs, butter, sugar. She arranges them like a periodic table.

"Before you bake anything, you need to understand what each ingredient actually
[bold white]does[/bold white]. Not what it tastes like — what it does structurally."

She holds up an egg.

"This is a binding agent, a leavening agent, a source of fat, a source of moisture,
and an emulsifier. One egg, five jobs. And whether you use the whole egg, just the yolk,
or just the white changes which of those jobs it performs."

She cracks it cleanly into a bowl.

"Flour provides structure through gluten. Sugar tenderizes by competing with gluten
for moisture. Fat coats flour particles and shortens gluten strands. Leaveners produce
gas. Temperature activates everything. This is the science of baking, and every
recipe is an equation."
""",
    "bread_basics": """
[bold yellow]== THE BREAD STATION ==[/bold yellow]

A mound of dough sits on the counter, smooth and supple. Chef Sofia pushes two fingers
into it and the dough slowly springs back.

"Bread is the oldest baked good. Flour, water, salt, yeast. Four ingredients. Humans
have been making bread for ten thousand years, and the basic process hasn't changed:
mix, knead, rise, shape, bake."

She folds the dough over itself, pressing with the heel of her hand.

"Kneading develops gluten — the protein network that traps the gas from yeast
fermentation. That's what gives bread its structure, its chew, its ability to rise
without collapsing. Under-knead and the bread is dense. Over-knead and it's tough."

She covers the dough with a towel.

"And then you wait. Bread teaches patience. The yeast works on its own schedule,
not yours. [bold white]Fermentation cannot be rushed.[/bold white]"
""",
    "cookies_bars": """
[bold yellow]== THE COOKIE STATION ==[/bold yellow]

Rows of cookies cool on wire racks — some crispy, some chewy, some cakey. All from
nearly the same recipe with small but critical variations.

Chef Sofia picks up two cookies that look almost identical.

"This one is crispy." She snaps it. "This one is chewy." She bends it. "The
difference? Two tablespoons more brown sugar and one fewer minute in the oven."

She sets them down.

"Cookie science is ratio science. More butter means spread. More flour means structure.
Brown sugar means moisture and chew. White sugar means crisp. Creaming the butter and
sugar traps air, which means lift. Melting the butter means [bold white]flat and chewy[/bold white]."

"Every cookie decision is a texture decision. Once you understand the variables,
you stop following cookie recipes and start designing them."
""",
    "cakes_frosting": """
[bold yellow]== THE CAKE STATION ==[/bold yellow]

Two cake layers cool on racks, golden and level. Beside them, a bowl of buttercream
so smooth it looks like satin. Piping bags, offset spatulas, a turntable.

Chef Sofia runs a finger along the top of a cake layer, checking for dome.

"Cake is the most forgiving of the precision baked goods — more forgiving than bread,
much more than pastry. But it still demands respect for ratios and technique."

She begins to level one layer with a serrated knife.

"The creaming method is the foundation: beat butter and sugar until light and fluffy.
That's not decoration — that's [bold white]mechanical leavening[/bold white]. The air you trap in that
step is what gives the cake its rise, along with the chemical leaveners."

"Frosting is its own discipline. Buttercream, cream cheese, ganache, meringue-based —
each has its own ratio, its own technique, its own temperature sensitivity. A great
cake with bad frosting is a tragedy."
""",
    "pastry_pies": """
[bold yellow]== THE PASTRY STATION ==[/bold yellow]

The counter is cold — deliberately. Chef Sofia has been chilling the marble surface
with bags of ice. Beside her: flour, butter cut into cubes and re-chilled, ice water,
a rolling pin.

"Pastry is where baking gets serious," she says, pressing a fingertip into one of the
butter cubes. "Feel that. Cold. That's the most important thing in pastry — temperature
control."

She begins cutting the butter into the flour with a pastry cutter.

"A flaky pie crust works because the butter stays in [bold white]discrete pieces[/bold white] inside the
dough. When the pastry hits the oven, those pieces of butter melt, creating steam,
which creates layers. If the butter melts before it hits the oven — because your hands
are too warm, or the kitchen is too hot, or you overworked the dough — you get a tough,
dense crust instead of a flaky one."

"Pastry is not hard. Pastry is [bold white]cold, fast, and confident[/bold white]."
""",
}

ZONE_COMPLETIONS = {
    "baking_science": """
[bold green]THE SCIENCE LAB — CLEARED.[/bold green]

Chef Sofia looks at your notes and nods.

"You understand the why now. Gluten, leavening, emulsification, the Maillard reaction —
these aren't vocabulary words. They're the physics and chemistry of everything you'll
bake from here on."

"When a recipe fails, you won't just shrug. You'll know [bold white]why[/bold white] it failed.
That's the difference between a baker and someone who follows instructions."

[bold yellow]The Bread Station is ready. Flour, water, salt, yeast. Time to build.[/bold yellow]
""",
    "bread_basics": """
[bold green]THE BREAD STATION — RISEN.[/bold green]

The loaf comes out of the oven with a hollow thump when you tap the bottom. The crust
is golden and crackly. The crumb, when you slice it, is open and airy with an even
distribution of holes.

Chef Sofia holds the slice up to the light.

"That's a well-fermented bread. The yeast did its work. The gluten held. The oven
spring was strong. You [bold white]understand[/bold white] bread now — not just how to make it,
but why it works."

[bold yellow]Cookies and bars are next. Same ingredients, different ratios, different results.[/bold yellow]
""",
    "cookies_bars": """
[bold green]THE COOKIE STATION — COMPLETE.[/bold green]

Twelve cookies on the rack. Each one exactly the texture you intended — the chewy ones
are chewy, the crispy ones snap, the cakey ones are tender and tall.

Chef Sofia picks up one of each.

"You're not following recipes anymore. You're [bold white]engineering[/bold white] cookies. You know
what each variable does. Brown sugar for moisture. Bread flour for chew. Extra egg
yolk for richness. Chill time for thickness."

[bold yellow]The Cake Station rises ahead. Layers, frosting, and the art of assembly.[/bold yellow]
""",
    "cakes_frosting": """
[bold green]THE CAKE STATION — FROSTED.[/bold green]

Two layers, level and even. Crumb coat chilled and set. Final coat of buttercream
smooth enough to see your reflection in. The piping is clean and confident.

Chef Sofia steps back and admires the cake.

"That's professional-level work. The crumb is tender, the frosting is silky, the
layers are even. You understand creaming, chemical leavening, and the critical
importance of [bold white]room-temperature ingredients[/bold white]."

[bold yellow]One station remains. The Pastry Station. Cold hands, cold butter, cold nerve.[/bold yellow]
""",
    "pastry_pies": """
[bold yellow]THE PASTRY STATION — COMPLETE.[/bold yellow]

The pie crust is a thing of beauty. Layer upon layer of flaky, golden pastry that
shatters at the touch of a fork. The filling is perfectly set — not runny, not stiff.

Chef Sofia cuts a clean wedge and holds it up.

"[bold white]Look at those layers.[/bold white] Every one of them is a piece of cold butter that
survived mixing, survived rolling, and turned to steam in a hot oven. That's not
luck. That's technique."

She sets the slice on a plate.

"You have the fundamentals of baking now. Science, bread, cookies, cakes, pastry.
Every bakery in the world is built on what you learned at these stations. The rest
is practice, repetition, and the occasional spectacular failure that teaches you
more than success ever could."

[bold yellow]Baking Fundamentals — complete. The oven is yours.[/bold yellow]
""",
}

BOSS_INTROS = {
    "baking_science": "Chef Sofia holds up a failed cake. 'Tell me what went wrong. Dense, gummy, sunken in the middle. Walk me through the science of the failure.'",
    "bread_basics": "Chef Sofia sets a timer. 'Yeast, fermentation, gluten, hydration, oven spring. Five concepts. Prove you understand every stage of bread from mix to loaf.'",
    "cookies_bars": "Chef Sofia shows you three cookies with different textures. 'Explain what made each one different. Same base recipe — what changed? This is cookie engineering.'",
    "cakes_frosting": "Chef Sofia presents a lopsided cake with broken frosting. 'Diagnose it. Every problem has a cause. Identify the failures and tell me how to fix each one.'",
    "pastry_pies": "Chef Sofia slides a tough, dense pie crust across the counter. 'This is what failure looks like in pastry. Tell me every mistake that led to this, and how cold butter would have saved it.'",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Batch", "Pulled your first tray from the oven. The baker's journey begins."),
    "science_certified": ("Lab Coat Earned", "Cleared the Science Lab. You understand the chemistry behind every bake."),
    "bread_baker": ("Bread Winner", "Mastered the Bread Station. Flour, water, salt, yeast — you understand the oldest recipe."),
    "cookie_master": ("Cookie Engineer", "Completed the Cookie Station. You design cookies, not just follow recipes."),
    "cake_artist": ("Layer Master", "Frosted the Cake Station. Crumb coats, buttercream, and perfect layers."),
    "pastry_chef": ("Cold Hands, Flaky Crust", "Completed the Pastry Station. Temperature control and confident technique."),
    "streak_3": ("Consistent Batch", "3 correct in a row. Your results are reproducible."),
    "streak_5": ("Baker's Rhythm", "5 correct in a row. The kitchen timer is your metronome."),
    "streak_10": ("Perfect Proof", "10 correct in a row. Flawless execution from scale to oven."),
    "no_hints": ("No Recipe Card", "Cleared a zone without any hints. Baked from pure knowledge."),
    "speed_demon": ("Speed Proof", "Answered in under 5 seconds. Faster than a convection cycle."),
    "level_10": ("Home Baker", "Level 10. Your kitchen smells like a bakery now."),
    "level_20": ("Artisan Baker", "Level 20. You could open a shop and nobody would question it."),
    "level_30": ("Pastry Chef", "Maximum level. Complete mastery of baking fundamentals."),
    "completionist": ("Full Bakery", "Every challenge completed. Every station mastered. From science to pastry, the oven is yours."),
    "boss_slayer": ("Bake-Off Winner", "Beat your first boss challenge. Chef Sofia tips her toque."),
}
