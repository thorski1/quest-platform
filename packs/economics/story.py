"""
story.py — Narrative for the Economics skill pack (The Market Square).

Puck opens the gates to a bustling market square and guides the reader
through the world of economics — wants vs needs, supply and demand,
jobs and careers, saving and budgeting, and global trade.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Market Square[/bold yellow]

The Primer's pages rustled and opened to reveal something wonderful —
a tiny, bustling market square, alive with color and sound.
Stalls overflowed with fruits and fabrics, little signs showed prices,
and miniature people hurried back and forth, buying, selling, and trading.

Puck appeared in the middle of it all, wearing a tiny merchant's apron
and carrying a chalkboard that read: [bold yellow]OPEN FOR BUSINESS[/bold yellow].

[bold cyan]"Welcome to the Market Square!"[/bold cyan] Puck said, spreading his arms wide.
[bold cyan]"This is where the whole world of economics comes alive.
Every stall, every price, every decision someone makes about
what to buy and what to save — it all happens here."[/bold cyan]

The girl looked around the tiny square. [bold white]"Economics? That sounds like
a grown-up word."[/bold white]

[bold cyan]"It IS a grown-up word,"[/bold cyan] Puck grinned,
[bold cyan]"but the ideas are for everyone. Economics is just the study of
how people make choices about money, work, and resources.
And you make those choices every single day!"[/bold cyan]

He flipped his chalkboard over. On the other side it read:
[bold yellow]5 LESSONS. 1 MARKET SQUARE. INFINITE WISDOM.[/bold yellow]

[bold cyan]"We'll learn what you truly need versus what you just want.
We'll discover why things cost what they do.
We'll explore jobs, budgets, and how the whole world trades."[/bold cyan]

Puck winked.

[bold cyan]"Ready to enter the Market Square?"[/bold cyan]

[bold white]Your adventure into the world of economics begins now.[/bold white]
"""

ZONE_INTROS = {
    "wants_vs_needs": """
Puck stopped at the very first stall in the Market Square.
On one side hung a warm coat, a loaf of bread, and a jug of water.
On the other side sat a shiny toy robot, a bag of candy, and a comic book.

[bold cyan]"Before you spend a single coin,"[/bold cyan] Puck said seriously,
[bold cyan]"you need to know the most important rule in all of economics:
the difference between what you NEED and what you WANT."[/bold cyan]

He picked up the bread in one hand and the toy in the other.

[bold cyan]"One of these keeps you alive. The other makes you smile.
Both matter — but one matters MORE."[/bold cyan]

[bold white]Let's learn to tell needs from wants![/bold white]
""",
    "supply_and_demand": """
Puck led the way to a busy corner of the Market Square where
two lemonade stands faced each other — one with a long line,
the other with none.

[bold cyan]"See that?"[/bold cyan] Puck pointed. [bold cyan]"Same lemonade. Different prices.
One charges $1, the other charges $3. Guess which one has the line?"[/bold cyan]

He pulled out a tiny chalkboard and drew two arrows —
one pointing up labeled DEMAND, one pointing down labeled SUPPLY.

[bold cyan]"This right here — supply and demand — is the engine that
drives every price in every market in the entire world.
Once you understand it, you'll see it EVERYWHERE."[/bold cyan]

[bold white]Let's discover how prices really work![/bold white]
""",
    "jobs_and_careers": """
Puck walked past the market stalls to a wide boulevard where
tiny people hurried to work — a baker carrying bread,
a doctor with a stethoscope, a builder with a hammer,
and a teacher with a stack of books.

[bold cyan]"Every single thing in this Market Square,"[/bold cyan] Puck said,
[bold cyan]"was made or provided by someone doing a job.
The bread? A baker made it. The medicine? A scientist created it.
The stalls themselves? Builders put them up."[/bold cyan]

He straightened his apron and stood a little taller.

[bold cyan]"Jobs are how people earn money AND how they
help the world. Let's explore the wonderful world of work!"[/bold cyan]

[bold white]Let's discover different jobs and careers![/bold white]
""",
    "saving_and_budgeting": """
Puck pulled out three tiny jars from under a market stall.
Each one had a label: [bold yellow]SAVE[/bold yellow], [bold yellow]SPEND[/bold yellow], [bold yellow]SHARE[/bold yellow].

[bold cyan]"You've learned about needs and wants,"[/bold cyan] Puck said.
[bold cyan]"You understand supply and demand. You know how people
earn money through jobs. But now comes the BIG question..."[/bold cyan]

He held up a single shining coin.

[bold cyan]"Once you HAVE money... what do you DO with it?
Spend it all? Save it all? Give it away?
The answer is: a little bit of each. And the tool that
helps you decide is called a BUDGET."[/bold cyan]

[bold white]Let's learn to save, budget, and spend wisely![/bold white]
""",
    "trading_and_global": """
Puck climbed to the top of the tallest stall in the Market Square
and pointed to the horizon. In every direction, the girl could see
other market squares — connected by tiny roads, ships, and airplanes.

[bold cyan]"Our Market Square is wonderful,"[/bold cyan] Puck said,
[bold cyan]"but it's just ONE square in a world full of them.
Every country has its own markets, its own money,
its own special products."[/bold cyan]

He pulled out a tiny globe and spun it.

[bold cyan]"And here's the amazing part: they all trade with each other!
Bananas from Ecuador, electronics from Japan,
wool from New Zealand — all crisscrossing the globe."[/bold cyan]

[bold white]Let's explore how the whole world trades![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "wants_vs_needs": """
[bold green]The first stall glows — you understand wants and needs![/bold green]

The coat, bread, and water shimmer on one side.
The toy, candy, and comic glow softly on the other.
Both sides are valuable — but now you know which comes first.

[bold cyan]"You've learned the foundation,"[/bold cyan] Puck says proudly.
[bold cyan]"Needs before wants. Priorities before impulses.
This one skill will serve you your entire life."[/bold cyan]

The lemonade stands ahead are calling. Time to learn about prices...
""",
    "supply_and_demand": """
[bold green]The lemonade stands glow — you understand supply and demand![/bold green]

Price tags across the Market Square make perfect sense now —
high demand and low supply push prices up,
low demand and high supply bring them down.

[bold cyan]"You can read the market now,"[/bold cyan] Puck says, impressed.
[bold cyan]"Every price tells a story of supply and demand.
You'll never look at a price tag the same way again."[/bold cyan]

The workers' boulevard is just ahead. Time to explore jobs!
""",
    "jobs_and_careers": """
[bold green]The boulevard glows — you understand jobs and careers![/bold green]

Tiny workers wave as they pass — bakers, doctors, teachers,
builders, artists — each one contributing something valuable.

[bold cyan]"Every job matters,"[/bold cyan] Puck says warmly.
[bold cyan]"From the baker who makes your bread to the scientist
who cures diseases. And someday, YOU'LL find your place
in this amazing world of work."[/bold cyan]

Three tiny jars wait at the next stall. Time to learn about budgets!
""",
    "saving_and_budgeting": """
[bold green]The three jars glow — you're a master of saving and budgeting![/bold green]

SAVE, SPEND, and SHARE — each jar is perfectly balanced,
coins sorted wisely, not a penny wasted.

[bold cyan]"You've cracked the code,"[/bold cyan] Puck says with a grin.
[bold cyan]"Earn, budget, save, spend wisely, and share generously.
That's the formula for a life without money worries."[/bold cyan]

The globe at the top of the Market Square is spinning. One last adventure!
""",
    "trading_and_global": """
[bold green]The globe blazes with light — you understand the global economy![/bold green]

Tiny ships, planes, and trucks carry goods between glowing
market squares all around the world. Every country connected,
every trade making life better for both sides.

[bold cyan]"You've done it,"[/bold cyan] Puck whispers, his eyes shining.
[bold cyan]"You understand economics — needs and wants, supply and demand,
jobs and careers, saving and budgeting, and global trade.
You see the world differently now."[/bold cyan]

Puck takes off his merchant's apron and hangs it on a hook.
The Market Square's sign now glows with YOUR name.

[bold white]Smart Consumer. Wise Saver. Global Thinker.[/bold white]
[bold white]The Market Square is yours.[/bold white]
""",
}

BOSS_INTROS = {
    "wants_vs_needs": "Puck sets up a tiny shop with a limited budget and a mix of needs and wants. [bold yellow]\"You've got $20 and a tough choice. Needs or wants? Show me what you've learned!\"[/bold yellow]",
    "supply_and_demand": "Puck unveils a miniature marketplace with price tags that keep changing. [bold yellow]\"Supply is shifting. Demand is surging. Can you predict what happens to the price?\"[/bold yellow]",
    "jobs_and_careers": "Puck unrolls a tiny career map with winding paths leading to different futures. [bold yellow]\"Every career starts with a first step. Which step is the right one?\"[/bold yellow]",
    "saving_and_budgeting": "Puck pulls out a tiny calculator and a budget that doesn't add up. [bold yellow]\"Something's wrong with this budget. Can you find the mistake and fix it?\"[/bold yellow]",
    "trading_and_global": "Puck spins a globe and stops it with his finger on two countries. [bold yellow]\"Two countries, two specialties. How does trade make both of them better off?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "smart_shopper": (
        "Smart Shopper",
        "Mastered the difference between wants and needs!",
    ),
    "market_analyst": (
        "Market Analyst",
        "Understood supply, demand, and how prices work!",
    ),
    "career_explorer": (
        "Career Explorer",
        "Explored the world of jobs, skills, and careers!",
    ),
    "budget_builder": (
        "Budget Builder",
        "Learned to save, budget, and spend wisely!",
    ),
    "global_trader": (
        "Global Trader",
        "Discovered how countries trade and the global economy works!",
    ),
}
