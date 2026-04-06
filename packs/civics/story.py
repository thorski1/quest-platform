"""
story.py — Narrative for the Social Studies & Civics skill pack.

Puck opens the Citizen's Handbook and guides the reader through
community helpers, rules and laws, government, maps, holidays,
rights and responsibilities, and world cultures.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Citizen's Handbook[/bold yellow]

Puck appeared at the edge of a brand-new page, carrying a book
bound in deep blue leather with gold letters on the spine:
[bold white]THE CITIZEN'S HANDBOOK[/bold white].

[bold cyan]"This,"[/bold cyan] Puck said, holding it up with both hands,
[bold cyan]"is the most important book in the whole Primer.
Not because it teaches you magic or monsters or maps —
but because it teaches you how people live [italic]together.[/italic]"[/bold cyan]

The girl tilted her head. [bold white]"Together?"[/bold white]

[bold cyan]"Together,"[/bold cyan] Puck repeated. [bold cyan]"How communities work.
Why we have rules. How leaders are chosen. What it means
to be a citizen — not just of a country, but of the whole world."[/bold cyan]

The book opened on its own, and the first page showed
a neighborhood: houses, a school, a fire station, a park,
and tiny people helping each other everywhere you looked.

[bold cyan]"Helpers, laws, governments, holidays, rights, cultures —
all the things that hold the world together.
And once you understand them, you'll understand
why the world works the way it does."[/bold cyan]

Puck grinned and flew to the top of the page.

[bold cyan]"Ready to become a citizen of the world?"[/bold cyan]

[bold white]Your journey through the Citizen's Handbook begins now.[/bold white]
"""

ZONE_INTROS = {
    "community_helpers": """
Puck turned to the first chapter of the Handbook. A bright neighborhood
appeared on the page — full of people in uniforms, each one busy helping.

[bold cyan]"Every neighborhood has heroes,"[/bold cyan] Puck said.
[bold cyan]"Not the kind with capes — the kind with badges, stethoscopes,
lesson plans, and mail bags. They keep us safe, healthy,
educated, and connected."[/bold cyan]

Five figures stood in a line, each one glowing:
[bold yellow]Firefighter · Police Officer · Doctor · Teacher · Mail Carrier[/bold yellow]

[bold white]Let's meet the people who help our community![/bold white]
""",
    "rules_and_laws": """
Puck flipped to a new chapter. The page showed two paths:
one orderly and bright, the other tangled and dark.

[bold cyan]"Rules,"[/bold cyan] Puck said, tracing the bright path,
[bold cyan]"are like trails through a forest. Without them,
everyone gets lost. With them, everyone finds their way."[/bold cyan]

[bold cyan]"Some rules are small — like 'raise your hand in class.'
Some are big — like 'don't drive through a red light.'
But every single one exists for a reason:
to keep things [italic]safe[/italic] and [italic]fair.[/italic]"[/bold cyan]

[bold white]Let's discover why rules and laws matter![/bold white]
""",
    "government_basics": """
Puck opened the Handbook to a page showing a great building
with columns and a dome, surrounded by people casting votes.

[bold cyan]"Somebody has to make the big decisions,"[/bold cyan] Puck explained.
[bold cyan]"Who builds the roads? Who runs the schools?
Who keeps the country safe? That's what a government does.
And in a democracy, the people get to choose who leads."[/bold cyan]

Three words glowed on the page:
[bold yellow]President · Mayor · Vote[/bold yellow]

[bold white]Let's learn how our country is run![/bold white]
""",
    "maps_and_globes": """
Puck pulled a small globe from behind the Handbook's pages
and set it spinning in the air.

[bold cyan]"Before you can understand the world's people,"[/bold cyan] Puck said,
[bold cyan]"you need to know where they live. Seven continents.
Hundreds of countries. Thousands of cities.
And maps are the language that shows you all of it."[/bold cyan]

The globe slowed, and lines of latitude and longitude
appeared like a glowing net around the Earth.

[bold white]Let's read the world![/bold white]
""",
    "holidays_traditions": """
Puck opened a chapter bursting with color — fireworks, candles,
feasts, parades, and music from every direction.

[bold cyan]"People love to celebrate,"[/bold cyan] Puck said with delight.
[bold cyan]"Independence Day, Thanksgiving, Diwali, Chinese New Year —
every holiday tells a story about what people care about.
And traditions? Those are the special things families
do the same way, year after year, generation after generation."[/bold cyan]

[bold white]Let's explore the days we celebrate![/bold white]
""",
    "rights_responsibilities": """
Puck held up two golden coins. One said [bold yellow]RIGHTS[/bold yellow].
The other said [bold yellow]RESPONSIBILITIES[/bold yellow].

[bold cyan]"These two always go together,"[/bold cyan] Puck said.
[bold cyan]"A right is something you're free to do — like speak your mind
or go to school. A responsibility is something you [italic]should[/italic] do —
like be kind, follow the rules, and help your community."[/bold cyan]

[bold cyan]"You can't have one without the other.
That's what being a good citizen is all about."[/bold cyan]

[bold white]Let's learn what it means to be a true citizen![/bold white]
""",
    "world_cultures": """
The final chapter of the Handbook opened to a spectacular scene:
the whole world, filled with music, food, languages, and faces
from every continent.

[bold cyan]"There are almost eight billion people on this planet,"[/bold cyan]
Puck said softly. [bold cyan]"They speak thousands of languages.
They eat different foods, wear different clothes,
celebrate different holidays, and tell different stories."[/bold cyan]

[bold cyan]"But everywhere you go, people love their families,
sing songs, share meals, and dream of a better world.
We are more alike than we are different."[/bold cyan]

[bold white]Let's explore the beautiful cultures of the world![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "community_helpers": """
[bold green]Every helper in the neighborhood stands tall and proud![/bold green]

Firefighters, police officers, doctors, teachers, mail carriers —
each one glowing on the page, each one keeping the community strong.

[bold cyan]"You know your neighborhood heroes now,"[/bold cyan] Puck says warmly.
[bold cyan]"And the best part? One day, you might become
one of these helpers yourself."[/bold cyan]

The Handbook turns to a new chapter. Rules and laws await...
""",
    "rules_and_laws": """
[bold green]The golden scale of fairness balances perfectly![/bold green]

Rules, laws, fairness, consequences, the Golden Rule —
all understood, all glowing on the page.

[bold cyan]"Rules aren't there to stop you,"[/bold cyan] Puck says.
[bold cyan]"They're there to help everyone. And the Golden Rule
is the one rule that works everywhere in the world."[/bold cyan]

The Handbook opens to a page of grand buildings. Government is next...
""",
    "government_basics": """
[bold green]Three great pillars hold up the roof of democracy![/bold green]

President, mayor, voting, democracy, the White House,
the three branches — all of it learned, all of it yours.

[bold cyan]"You understand how your country works,"[/bold cyan] Puck says proudly.
[bold cyan]"And that means you understand something powerful:
the people have the power. Including you."[/bold cyan]

A globe begins to spin on the next page. Maps and places await...
""",
    "maps_and_globes": """
[bold green]The globe spins with every continent aglow![/bold green]

Seven continents, fifty states, capital cities, map symbols —
the world laid out before you, readable and clear.

[bold cyan]"You can read the world now,"[/bold cyan] Puck says with a smile.
[bold cyan]"Every map, every globe, every atlas —
they all speak a language you understand."[/bold cyan]

The Handbook opens to a colorful page of celebrations. Holidays are next...
""",
    "holidays_traditions": """
[bold green]The page explodes with celebration![/bold green]

Fireworks, feasts, parades, candles, and music from every culture
light up the Handbook.

[bold cyan]"Holidays connect us,"[/bold cyan] Puck says. [bold cyan]"To our history,
to our families, and to each other. Every celebration
is a story about what people love most."[/bold cyan]

Two golden coins appear on the next page. Rights and responsibilities await...
""",
    "rights_responsibilities": """
[bold green]The golden coins click together — Rights and Responsibilities, united![/bold green]

Citizenship, helping others, freedom, responsibility —
all learned, all understood, all part of who you are.

[bold cyan]"You know what it means to be a good citizen now,"[/bold cyan]
Puck says quietly. [bold cyan]"Not just someone who follows rules,
but someone who makes the world better for everyone."[/bold cyan]

The final chapter of the Handbook glows with warmth. World cultures await...
""",
    "world_cultures": """
[bold green]The whole world glows with connection and understanding![/bold green]

Languages, foods, festivals, traditions — every culture explored,
every difference respected, every similarity celebrated.

[bold cyan]"You've done it,"[/bold cyan] Puck says, wings spread wide.
[bold cyan]"Community helpers, rules, government, maps, holidays,
rights, and cultures — the whole Citizen's Handbook,
every page of it. You understand how the world
works [italic]together.[/italic]"[/bold cyan]

Puck closes the Handbook gently.

[bold white]Citizen. Helper. Leader. Ambassador. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "community_helpers": "Puck looks up at a very tall tree. [bold yellow]\"A cat is stuck at the very top! Which community helper has the tall ladders and the training to rescue it? Think carefully!\"[/bold yellow]",
    "rules_and_laws": "Puck holds up a glowing golden rule — the oldest, most universal rule in all of human history. [bold yellow]\"This rule is found in almost every culture on Earth. It's about treating others the way you want to be treated. Why is it so important?\"[/bold yellow]",
    "government_basics": "Puck draws three tall pillars on the page, each one holding up part of a great roof. [bold yellow]\"The U.S. government was built with three branches — so no one person could have ALL the power. Do you know what they're called?\"[/bold yellow]",
    "maps_and_globes": "Puck holds a round globe in one hand and a flat map in the other. [bold yellow]\"These both show the Earth — but one is more accurate than the other. Why? Think about the shape of our planet!\"[/bold yellow]",
    "holidays_traditions": "Puck stands in a swirl of lanterns, fireworks, candles, and flowers from a dozen different countries. [bold yellow]\"Every culture celebrates — but they all celebrate differently. What does that teach us about the world?\"[/bold yellow]",
    "rights_responsibilities": "Puck holds up two golden coins that fit together like puzzle pieces. [bold yellow]\"Rights and responsibilities always go together. But WHY? Think about what happens if everyone has rights but nobody takes responsibility.\"[/bold yellow]",
    "world_cultures": "Puck stands on a tiny globe, arms spread wide, with children from every continent waving. [bold yellow]\"You've traveled the world through its cultures. Now tell me: why does learning about other cultures matter so much?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "community_champion": (
        "Community Champion",
        "Learned about all the helpers who keep our neighborhoods safe and strong!",
    ),
    "rule_keeper": (
        "Rule Keeper",
        "Understood why rules and laws keep the world fair and safe!",
    ),
    "democracy_scholar": (
        "Democracy Scholar",
        "Learned how government works and why every vote counts!",
    ),
    "map_navigator": (
        "Map Navigator",
        "Read maps, found continents, and located capital cities!",
    ),
    "tradition_keeper": (
        "Tradition Keeper",
        "Explored holidays and traditions from around the world!",
    ),
    "citizen_hero": (
        "Citizen Hero",
        "Understood what rights and responsibilities mean for everyone!",
    ),
    "culture_explorer": (
        "Culture Explorer",
        "Explored languages, foods, and celebrations from every corner of the globe!",
    ),
}
