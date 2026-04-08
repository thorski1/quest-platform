"""
story.py — Narrative text for Kitchen Fundamentals
"""

INTRO_STORY = """
There is a kitchen. Not a restaurant kitchen with its steel counters and ticket rails — not yet.
This one is quieter. Copper pots hang from a rack above a butcher-block island. Late afternoon
sun pours through tall windows, casting long amber shadows across the tile floor. The air smells
like garlic and fresh herbs and something baking slowly in the oven.

[bold yellow]Chef Sofia[/bold yellow] stands at the counter, wiping her hands on a linen towel. She's cooked
professionally for twenty years — Michelin kitchens in Lyon, street stalls in Bangkok, a tiny
pasta shop in Bologna where the grandmother wouldn't let her touch the dough for the first
six months. She left all of it to teach.

"Every great dish," she says, not looking up from the cutting board, "starts with the same
thing. Not ingredients. Not recipes. [bold white]Fundamentals.[/bold white]"

She slides a knife across a shallot — one clean motion, paper-thin slices fanning out like
a deck of cards. No wasted movement. No hesitation.

"A sharp knife. Clean technique. Understanding heat. Knowing your ingredients by smell and
touch, not just by what the recipe tells you. These are the things that separate someone
who follows instructions from someone who [bold yellow]cooks[/bold yellow]."

She gestures toward the stations set up around the kitchen. Each one is a lesson. Each one
builds on the last.

[bold white]"Shall we begin?"[/bold white]
"""

ZONE_INTROS = {
    "kitchen_safety": """
[bold yellow]== THE SAFETY STATION ==[/bold yellow]

Chef Sofia sets down her knife and turns to face you directly.

"Before we cook anything — before you even turn on a burner — we talk about safety.
I've seen talented cooks lose weeks to burns they could have prevented. I've seen
kitchens shut down because someone didn't understand cross-contamination."

She taps the first-aid kit mounted on the wall.

"A professional kitchen is full of things that can hurt you: open flames, boiling liquids,
sharp edges, hot surfaces. The difference between a home cook who's afraid of the kitchen
and a confident one isn't bravery — it's [bold white]knowledge[/bold white]."

"Learn the rules. Respect the hazards. Then you can move fast without fear."
""",
    "knife_skills": """
[bold yellow]== THE CUTTING STATION ==[/bold yellow]

Chef Sofia places a heavy chef's knife on the cutting board. Beside it: an onion, a carrot,
a bundle of herbs. The blade catches the late-afternoon light.

"This is the most important tool you will ever hold in a kitchen. Not a blender. Not a
food processor. Not any gadget with a plug. [bold white]The knife.[/bold white]"

She picks it up, demonstrating her grip — thumb and forefinger pinching the blade
just above the heel, the other three fingers wrapped around the handle.

"A dull knife is more dangerous than a sharp one. A sharp knife goes where you tell it.
A dull one slips. Learn to hold it properly. Learn the basic cuts. Learn to keep the
blade sharp. Everything else in cooking gets easier once the knife feels like an
extension of your hand."
""",
    "measuring_temps": """
[bold yellow]== THE PRECISION STATION ==[/bold yellow]

Chef Sofia opens a drawer and lays out measuring cups, a digital scale, and an
instant-read thermometer.

"Cooking is generous. Baking is precise. But even in cooking, there are moments
where precision matters — and temperature is the most important one."

She holds up the thermometer.

"Every protein has a temperature where it goes from raw to safe. Every fat has a
smoke point. Every sugar has a stage. The difference between a medium-rare steak
and a dry, gray disappointment is [bold white]fifteen degrees[/bold white]."

"Measuring by volume is fine for most things. Measuring by weight is better for
everything. And checking temperature is non-negotiable for safety and quality."
""",
    "cooking_methods": """
[bold yellow]== THE FLAME STATION ==[/bold yellow]

Chef Sofia turns on the stove. A blue ring of flame appears, steady and controlled.
Beside it, the oven glows at 400 degrees. A pot of water begins its slow climb toward
a boil.

"Heat is the transformation. Raw ingredients become food through the application of
heat — but [bold white]how[/bold white] you apply it changes everything."

She gestures at the different stations: a saute pan, a deep pot, a sheet pan, a grill grate.

"Sauteing is fast and hot. Braising is slow and gentle. Roasting is dry heat in an
enclosed space. Boiling is wet heat at a fixed temperature. Each method does something
different to the food — and knowing which one to use is what makes a cook, not a recipe."

"Today you learn to control fire."
""",
    "seasoning_spices": """
[bold yellow]== THE FLAVOR STATION ==[/bold yellow]

The counter is lined with small bowls: kosher salt, black pepper, cumin, paprika,
dried oregano, fresh thyme, garlic, ginger, chili flakes. The air is fragrant.

Chef Sofia picks up a pinch of salt and drops it into a pot of simmering broth.
She tastes. Adds another pinch. Tastes again.

"Seasoning is the difference between food that nourishes and food that [bold white]sings[/bold white].
And it's the skill most home cooks never develop, because they season once at the
end instead of building flavor at every stage."

She holds up a dried bay leaf and inhales.

"Salt enhances. Acid brightens. Fat carries. Heat blooms. Spices are not decoration —
they are architecture. Learn when to add them, how much, and why, and you will
never cook a bland meal again."
""",
}

ZONE_COMPLETIONS = {
    "kitchen_safety": """
[bold green]THE SAFETY STATION — CLEARED.[/bold green]

Chef Sofia nods approvingly.

"Good. You understand the rules now — not because someone told you to memorize them,
but because you understand [bold white]why[/bold white] they exist. Cross-contamination isn't
abstract when you've seen someone get sick. Burns aren't theoretical when you know
how fast hot oil moves."

"The kitchen is no longer a dangerous place for you. It's a workspace you respect."

[bold yellow]The Cutting Station awaits. Time to pick up the knife.[/bold yellow]
""",
    "knife_skills": """
[bold green]THE CUTTING STATION — MASTERED.[/bold green]

The onion sits in a perfect small dice. The carrot is a uniform julienne. The herbs
are chiffonaded into delicate ribbons.

Chef Sofia inspects your work, running a fingertip along the cuts.

"Consistent size means consistent cooking. Every piece the same thickness means every
piece finishes at the same time. That's not perfectionism — that's [bold white]technique[/bold white]."

[bold yellow]The Precision Station is next. Time to measure with confidence.[/bold yellow]
""",
    "measuring_temps": """
[bold green]THE PRECISION STATION — CALIBRATED.[/bold green]

Chef Sofia watches you read the thermometer without hesitation.

"You know what 165 means for chicken. You know what 325 means for a slow braise.
You know the difference between a tablespoon and a fluid ounce. These aren't
trivia — they're the foundation of every recipe you'll ever follow or improvise."

[bold yellow]The Flame Station burns ahead. Time to learn what heat really does.[/bold yellow]
""",
    "cooking_methods": """
[bold green]THE FLAME STATION — CONQUERED.[/bold green]

The saute pan sizzles. The braise simmers. The roast emerges golden and fragrant.

"You don't just cook now," Chef Sofia says. "You choose [bold white]how[/bold white] to cook.
That's the difference. A recipe says 'saute the onions.' You understand what
sauteing actually does to the onion — the Maillard reaction, the caramelization,
the release of sugars. You're not following steps. You're making decisions."

[bold yellow]One station remains. The Flavor Station. This is where it all comes together.[/bold yellow]
""",
    "seasoning_spices": """
[bold yellow]THE FLAVOR STATION — COMPLETE.[/bold yellow]

Chef Sofia tastes the broth you've seasoned. She closes her eyes. She nods.

"[bold white]That's it.[/bold white] That's the balance. Salt, acid, heat, fat — and the spices
layered at the right moments. You didn't just follow a recipe. You tasted.
You adjusted. You trusted your palate."

She sets down the spoon and looks at you.

"You have the fundamentals now. Every cuisine in the world is built on what
you learned in this kitchen. The knife. The heat. The seasoning. The rest
is just geography and tradition."

[bold yellow]Kitchen Fundamentals — complete. The world's kitchens are open to you.[/bold yellow]
""",
}

BOSS_INTROS = {
    "kitchen_safety": "Chef Sofia sets a timer. 'Quick-fire round. Kitchen hazards — name them, handle them, prevent them. No second chances in a real kitchen.'",
    "knife_skills": "Chef Sofia slides a whole butternut squash onto the board. 'Break this down. Every cut clean. Every piece uniform. Show me you understand the blade.'",
    "measuring_temps": "Chef Sofia holds up three different proteins. 'Give me the safe internal temperature for each. No thermometer guessing — you need to know these cold.'",
    "cooking_methods": "Chef Sofia gestures at four pans, four proteins, four methods. 'Match them. Cook them. Explain why each method works for each ingredient.'",
    "seasoning_spices": "Chef Sofia pushes a bowl of unseasoned soup toward you. 'Fix it. Layer the seasoning. Tell me what you're adding and why. This is your final exam.'",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Chop", "Made your first cut in the kitchen. Every chef starts somewhere."),
    "safety_certified": ("Safety First", "Cleared the Safety Station. You know how to protect yourself and others in the kitchen."),
    "blade_master": ("Blade Master", "Mastered the Cutting Station. Your knife skills are clean, confident, and consistent."),
    "precision_cook": ("Precision Cook", "Calibrated at the Precision Station. You measure and temp with confidence."),
    "method_master": ("Method Master", "Conquered the Flame Station. You understand heat and how it transforms food."),
    "flavor_architect": ("Flavor Architect", "Completed the Flavor Station. You season with intention and taste with awareness."),
    "streak_3": ("Mise en Place", "3 correct in a row. Your prep is organized and your rhythm is steady."),
    "streak_5": ("Flow State", "5 correct in a row. You're moving through the kitchen like a professional."),
    "streak_10": ("Chef's Table", "10 correct in a row. The kitchen bends to your will. Flawless execution."),
    "no_hints": ("No Recipe Needed", "Cleared a zone without any hints. Pure knowledge, no safety net."),
    "speed_demon": ("Flash Saute", "Answered in under 5 seconds. Fast hands, faster mind."),
    "level_10": ("Line Cook", "Level 10. You've moved past the basics and into real technique."),
    "level_20": ("Sous Chef", "Level 20. The kitchen feels like home now."),
    "level_30": ("Executive Chef", "Maximum level. Complete mastery of kitchen fundamentals."),
    "completionist": ("Full Course", "Every challenge completed. Every station mastered. The kitchen holds no secrets."),
    "boss_slayer": ("Quick-Fire Winner", "Beat your first boss challenge. Chef Sofia is impressed."),
}
