"""
story.py — Narrative text for World Cuisines
"""

INTRO_STORY = """
The sun is setting over an open-air market. Somewhere between the spice stalls and the
fruit vendors, the aroma shifts — cumin gives way to soy sauce, then to fresh basil, then
to something grilling over charcoal that you can't quite place but desperately want to eat.

[bold yellow]Chef Sofia[/bold yellow] appears beside you, a canvas tote bag over one shoulder,
already full of ingredients from three different continents.

"Every cuisine tells a story," she says, lifting a bundle of lemongrass to her nose.
"Climate, geography, trade routes, colonization, migration — all of it written in the
food. You want to understand Italian cooking? Learn about the tomato arriving from the
Americas in the sixteenth century. You want to understand Mexican cooking? Start with
corn, thousands of years before the Spanish arrived."

She leads you through the market, stopping at each stall like she's greeting old friends.

"I'm not going to teach you recipes. Recipes are just snapshots. I'm going to teach you
[bold white]traditions[/bold white] — the ingredients, the techniques, the flavor profiles that define
each cuisine. Once you understand those, you can cook anything from that tradition,
recipe or no recipe."

She stops at a crossroads in the market where five paths diverge, each lined with different
stalls, different smells, different sounds.

"Five cuisines. Five traditions. Five ways the world learned to turn raw ingredients
into something that brings people to the table."

[bold white]"Pick a path. Let's eat."[/bold white]
"""

ZONE_INTROS = {
    "italian_cooking": """
[bold yellow]== THE ITALIAN KITCHEN ==[/bold yellow]

The path opens into a sun-drenched courtyard. Tomatoes ripen on the vine. A pot of water
is already boiling. Garlic sizzles in olive oil in a pan that has clearly seen decades of use.

Chef Sofia picks up a block of Parmigiano-Reggiano and weighs it in her hand.

"Italian cooking is the art of restraint. Three ingredients. Four, maximum. Each one
perfect. Each one doing exactly one job. The tomato is sweet and acidic. The olive oil
is rich and fruity. The garlic is sharp and warm. The pasta is the vehicle."

She drops a handful of spaghetti into the boiling water.

"The Italians didn't invent complexity. They perfected [bold white]simplicity[/bold white]. And
simplicity is the hardest thing to get right, because there's nowhere to hide."
""",
    "mexican_cooking": """
[bold yellow]== THE MEXICAN KITCHEN ==[/bold yellow]

Dried chiles hang from the ceiling in deep red cascades. A comal sits over a flame,
blackening tomatillos. In the corner, a molcajete — the volcanic stone mortar — holds
a salsa verde so green it practically glows.

Chef Sofia tears a dried ancho chile in half and inhales the scent.

"Mexican cooking is one of the oldest and most sophisticated food traditions on earth.
Corn, beans, squash — the Three Sisters — predate European contact by thousands of years.
The chile is not just heat. It's [bold white]flavor[/bold white] — fruity, smoky, earthy, sweet, bitter,
depending on the variety."

She gestures at the array of dried chiles: ancho, guajillo, pasilla, chipotle, arbol.

"Every region has its own mole, its own salsa, its own way with tortillas. This is not
Tex-Mex. This is a civilization's worth of culinary knowledge."
""",
    "japanese_cooking": """
[bold yellow]== THE JAPANESE KITCHEN ==[/bold yellow]

The space is immaculate. A wooden counter, freshly wiped. A single knife on a magnetic
strip. A pot of dashi — kelp and bonito — releasing a gentle, oceanic steam. Everything
in its place. Nothing extra.

Chef Sofia pours a small cup of the dashi and offers it to you.

"Taste that. That's [bold white]umami[/bold white] — the fifth taste. The Japanese didn't just discover
it; they built an entire cuisine around it. Kombu, bonito, miso, soy sauce, mirin — every
one of these is an umami delivery system."

She sets out a bowl of short-grain rice, steaming and perfect.

"Japanese cooking is about respect for the ingredient. You don't cover a piece of fish
with sauce. You honor it. The technique is invisible — you eat the result and think,
'That was simple.' It wasn't. It was [bold white]precise[/bold white]."
""",
    "indian_cooking": """
[bold yellow]== THE INDIAN KITCHEN ==[/bold yellow]

The air hits you before you see anything. Cumin seeds crackling in hot oil. Turmeric
staining a wooden spoon golden. Cardamom pods releasing their perfume as they split in
the heat. The fragrance is layered, complex, alive.

Chef Sofia drops mustard seeds into a small pan of hot ghee. They pop and dance.

"Indian cooking is the most sophisticated spice tradition in the world. Not because
they use the most spices — because they understand [bold white]when[/bold white] to add each one. Whole
spices at the start for the foundation. Ground spices in the middle for the body.
Fresh herbs at the end for brightness."

She gestures at a tray of small steel bowls, each holding a different spice.

"This is a masala dabba — the spice box. Every Indian kitchen has one. Every household
has their own proportions. This is not a single cuisine. This is a subcontinent of
regional traditions, each one deep enough to study for a lifetime."
""",
    "french_cooking": """
[bold yellow]== THE FRENCH KITCHEN ==[/bold yellow]

White tile. Heavy copper. A stockpot that has been simmering since morning, its contents
reduced to a glaze so concentrated it coats a spoon like velvet. The smell is rich,
complex, deeply savory.

Chef Sofia stirs the pot once, slowly.

"French cooking is where modern professional technique was born. Not because the French
invented cooking — because they [bold white]codified[/bold white] it. Auguste Escoffier organized the
kitchen into stations, standardized the sauces, created the brigade system. Every
professional kitchen in the world still runs on French bones."

She sets out five small pans, each with a different mother sauce at various stages.

"Five mother sauces. From those five, you can derive every classical French sauce.
Bechamel, veloute, espagnole, hollandaise, tomato. Master these and you understand
the architecture of Western cooking."
""",
}

ZONE_COMPLETIONS = {
    "italian_cooking": """
[bold green]THE ITALIAN KITCHEN — COMPLETATO.[/bold green]

The pasta is al dente. The sauce clings to every strand without pooling at the bottom.
The Parmigiano is grated, not shredded. The basil is torn, not cut.

Chef Sofia twirls a forkful and tastes.

"[bold white]Perfetto.[/bold white] You understand now — Italian cooking isn't about what you add.
It's about what you don't add. Restraint is the hardest skill, and you have it."

[bold yellow]More cuisines await. The world's table is large.[/bold yellow]
""",
    "mexican_cooking": """
[bold green]THE MEXICAN KITCHEN — COMPLETO.[/bold green]

The salsa is balanced — heat, acid, smoke, sweetness. The tortillas are handmade,
still warm, with that slight char from the comal. The mole took hours and it was
worth every minute.

Chef Sofia dips a tortilla chip into your salsa and nods slowly.

"You understand the chiles now. Not just the heat — the [bold white]flavor[/bold white].
That's what separates someone who cooks Mexican food from someone who just
adds hot sauce."

[bold yellow]The journey continues. Another kitchen, another tradition.[/bold yellow]
""",
    "japanese_cooking": """
[bold green]THE JAPANESE KITCHEN — COMPLETE.[/bold green]

The dashi is clear and golden. The rice is glossy, each grain distinct. The knife
cuts are so precise they look machined.

Chef Sofia inspects your work with the quiet satisfaction of someone who knows
how hard simplicity actually is.

"You've learned that less is not lazy. Less is [bold white]disciplined[/bold white]. Every ingredient
justified. Every cut intentional. Every temperature exact. This is what Japanese
cooking teaches — and it makes everything else you cook better."

[bold yellow]More flavors await on the world's table.[/bold yellow]
""",
    "indian_cooking": """
[bold green]THE INDIAN KITCHEN — COMPLETE.[/bold green]

The curry is layered — you can taste the bloomed whole spices underneath, the
ground spice body in the middle, the fresh cilantro brightness on top. The rice
is fluffy, each grain separate. The naan is blistered and tender.

Chef Sofia breathes in the aroma and smiles.

"You've learned the most important lesson of Indian cooking: spices are not
interchangeable. Each one has a purpose, a moment, a temperature. You don't
just add them — you [bold white]conduct[/bold white] them."

[bold yellow]The journey nears its end. One tradition remains.[/bold yellow]
""",
    "french_cooking": """
[bold yellow]THE FRENCH KITCHEN — COMPLETE.[/bold yellow]

The mother sauces are smooth, each one a different texture, a different depth.
The stock is clear and concentrated. The technique is clean and classical.

Chef Sofia tastes each sauce, one by one. She sets down the spoon.

"[bold white]You understand the architecture now.[/bold white] Every Western sauce descends from
these five. Every braise, every gratin, every classical preparation — they all
come back to stock, roux, and reduction. The French didn't invent flavor. They
organized it."

[bold yellow]World Cuisines — complete. Five traditions. Five philosophies.
One table that stretches around the globe.[/bold yellow]
""",
}

BOSS_INTROS = {
    "italian_cooking": "Chef Sofia sets a timer. 'Pasta, sauce, finish. You have the knowledge — now prove you understand the tradition. Precision and simplicity. Go.'",
    "mexican_cooking": "Chef Sofia lines up five dried chiles. 'Name them. Describe their flavor profiles. Tell me which salsa each one belongs in. This is the heart of Mexican cooking.'",
    "japanese_cooking": "Chef Sofia places a single piece of fish on the counter. 'Dashi, rice, knife work, umami. Everything comes together now. Show me you understand Japanese precision.'",
    "indian_cooking": "Chef Sofia opens the masala dabba. 'Build a spice blend from scratch. Tell me the order, the timing, the temperature. This is the final test of spice mastery.'",
    "french_cooking": "Chef Sofia points to five empty pans. 'Five mother sauces. Name them, describe them, and tell me what each one becomes. The foundation of classical cooking — prove you own it.'",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Taste", "Took your first bite of world cuisine knowledge. The journey begins."),
    "italian_master": ("Fatto in Casa", "Mastered the Italian Kitchen. Simplicity perfected."),
    "mexican_master": ("Sabor Completo", "Mastered the Mexican Kitchen. You understand the chile."),
    "japanese_master": ("Itadakimasu", "Mastered the Japanese Kitchen. Precision and respect."),
    "indian_master": ("Masala Master", "Mastered the Indian Kitchen. The spice box is yours."),
    "french_master": ("Classique", "Mastered the French Kitchen. The mother sauces bow to you."),
    "streak_3": ("Seasoned Palate", "3 correct in a row. Your palate is developing nicely."),
    "streak_5": ("World Traveler", "5 correct in a row. You move between cuisines with confidence."),
    "streak_10": ("Grand Tour", "10 correct in a row. Culinary mastery across borders."),
    "no_hints": ("No Map Needed", "Cleared a zone without any hints. Pure culinary knowledge."),
    "speed_demon": ("Street Food Speed", "Answered in under 5 seconds. Fast as a Bangkok wok station."),
    "level_10": ("Seasoned Traveler", "Level 10. You've tasted enough to know what you're talking about."),
    "level_20": ("Culinary Ambassador", "Level 20. You can navigate any kitchen in the world."),
    "level_30": ("World Chef", "Maximum level. Five cuisines mastered. The world is your kitchen."),
    "completionist": ("Around the World", "Every challenge completed. Every cuisine explored. A true culinary citizen."),
    "boss_slayer": ("Quick-Fire Champion", "Beat your first boss challenge. Chef Sofia raises a glass."),
}
