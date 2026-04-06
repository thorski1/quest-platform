"""
story.py — Narrative for the Money & Economics skill pack.

Puck opens a glowing treasure chest and guides the reader through the
world of money — what it is, how to earn and save it, spend it wisely,
understand banks, start a business, give generously, and explore the
currencies of the world.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Treasure Chest[/bold yellow]

Puck appeared on the Primer's newest page carrying something heavy —
a wooden chest, old and beautiful, clasped shut with a golden lock.
He set it down with a grunt and wiped his brow.

[bold cyan]"This,"[/bold cyan] Puck said, tapping the lid, [bold cyan]"is a treasure chest.
But the treasure inside isn't gold or jewels.
It's something far more powerful: [italic]knowledge about money.[/italic]"[/bold cyan]

The girl tilted her head. [bold white]"Knowledge about money is treasure?"[/bold white]

[bold cyan]"The most valuable kind!"[/bold cyan] Puck grinned and flipped the lock open.
The lid swung wide. Inside, golden light poured out — and within it,
tiny coins, bills, piggy banks, shop signs, and little flags
from every country in the world, all made of light.

[bold cyan]"Money is a language,"[/bold cyan] Puck said softly.
[bold cyan]"And once you learn to speak it — how to earn it,
save it, spend it wisely, share it, and understand it —
you'll never be confused by it again."[/bold cyan]

The girl reached in and picked up a glowing coin.
It felt warm in her hand.

[bold cyan]"Seven lessons. One treasure chest.
By the end, you'll understand money better than most grown-ups."[/bold cyan]

Puck winked.

[bold cyan]"Ready to open the chest?"[/bold cyan]

[bold white]Your adventure into the world of money begins now.[/bold white]
"""

ZONE_INTROS = {
    "what_is_money": """
Puck pulled out the very first treasure from the chest —
an ancient coin, dull and heavy, with strange markings on its face.

[bold cyan]"Before there were dollars or euros or yen,"[/bold cyan] Puck said,
[bold cyan]"before there were even coins — people just traded things.
A basket of fish for a bag of grain. A wool blanket for a clay pot.
It worked... sort of. But it had a big problem."[/bold cyan]

He held up the old coin.

[bold cyan]"Then someone had a brilliant idea."[/bold cyan]

[bold white]Let's discover the story of money — from the very beginning![/bold white]
""",
    "earning_and_saving": """
Puck reached into the chest and pulled out a tiny piggy bank,
pink and round, with a slot in the top.

[bold cyan]"Money doesn't just appear,"[/bold cyan] Puck said.
[bold cyan]"People earn it — by working, by helping, by making things
the world needs. And the really smart ones? They don't spend
every penny. They save some, too."[/bold cyan]

He dropped a small coin into the piggy bank. [italic]Clink![/italic]

[bold cyan]"Small amounts, added up over time, become something big.
That's the secret most people learn too late."[/bold cyan]

[bold white]Let's learn how to earn and save![/bold white]
""",
    "spending_wisely": """
Puck pulled out two tiny signs from the chest:
one said [bold yellow]NEED[/bold yellow] and the other said [bold yellow]WANT[/bold yellow].

[bold cyan]"This,"[/bold cyan] Puck said, holding up NEED,
[bold cyan]"is something you can't live without — food, water, shelter.
And this,"[/bold cyan] he held up WANT,
[bold cyan]"is something nice to have, but you'd survive without it."[/bold cyan]

He placed both signs on the page.

[bold cyan]"The secret to spending wisely? Know the difference.
Take care of needs first. Then — if there's money left —
enjoy some wants. And always, always compare prices."[/bold cyan]

[bold white]Let's learn to be a smart spender![/bold white]
""",
    "banks_and_interest": """
Puck pulled a tiny building from the chest — it had thick walls,
a heavy door, and a little sign that read [bold yellow]BANK[/bold yellow].

[bold cyan]"A bank,"[/bold cyan] Puck said, [bold cyan]"is like a fortress for your money.
You put your money in, and the bank keeps it safe.
But here's the amazing part..."[/bold cyan]

He leaned in and whispered.

[bold cyan]"The bank actually [italic]pays you[/italic] to keep your money there.
It's called interest. Your money grows — all by itself —
just by sitting in the bank."[/bold cyan]

His eyes sparkled.

[bold cyan]"Like planting a seed and watching it grow."[/bold cyan]

[bold white]Let's open the vault and learn about banks![/bold white]
""",
    "entrepreneurship": """
Puck reached into the chest and pulled out a miniature lemonade stand,
complete with a tiny pitcher, cups, and a hand-painted sign.

[bold cyan]"Every business in the world,"[/bold cyan] Puck said,
[bold cyan]"started with one person and one idea.
A problem that needed solving. A product people wanted.
A service that made life better."[/bold cyan]

He stood behind the tiny stand and straightened his bow tie.

[bold cyan]"You don't have to be a grown-up to be an entrepreneur.
You just need an idea, a little courage, and the willingness
to try."[/bold cyan]

[bold white]Let's build a business — starting with lemonade![/bold white]
""",
    "sharing_and_giving": """
Puck reached deep into the chest and pulled out something different —
not a coin or a bill, but a small, glowing heart.

[bold cyan]"Money isn't just about earning and spending,"[/bold cyan] Puck said quietly.
[bold cyan]"Some of the best things you can do with money
are things that help [italic]other[/italic] people."[/bold cyan]

He held the heart up and it cast a warm light across the page.

[bold cyan]"Charity. Volunteering. Fairness. Taxes that build schools
and roads for everyone. When we share, the whole community
gets stronger."[/bold cyan]

[bold white]Let's discover the power of giving![/bold white]
""",
    "global_money": """
Puck tipped the treasure chest upside down, and out tumbled
bills and coins from every corner of the world — colorful notes
with pandas and pyramids, coins stamped with maple leaves and eagles.

[bold cyan]"In America, it's dollars,"[/bold cyan] Puck said, sorting through the pile.
[bold cyan]"In Japan, yen. In India, rupees. In Europe, euros.
Every country has its own money, its own currency."[/bold cyan]

He held up two different bills side by side.

[bold cyan]"And here's the interesting part: they're not all worth
the same amount. One dollar might be worth a hundred yen!
That's called an exchange rate."[/bold cyan]

[bold white]Let's travel the world and learn about global money![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "what_is_money": """
[bold green]The first treasure glows — the story of money is yours![/bold green]

From bartering to coins to paper bills, the whole history shimmers
on the page like a golden timeline.

[bold cyan]"You understand where money came from,"[/bold cyan] Puck says proudly.
[bold cyan]"That's something most people never stop to think about.
Now you know: money is trust, turned into something you can hold."[/bold cyan]

The piggy bank in the chest shimmers. Time to learn about earning and saving...
""",
    "earning_and_saving": """
[bold green]The piggy bank glows — you understand earning and saving![/bold green]

Tiny coins stack higher and higher, showing weeks of patient saving.

[bold cyan]"You've learned the first great money skill,"[/bold cyan] Puck says.
[bold cyan]"Earn honestly. Save patiently. Small amounts become big ones.
And a savings goal turns waiting into something exciting."[/bold cyan]

The treasure chest opens wider. Smart spending is next...
""",
    "spending_wisely": """
[bold green]The NEED and WANT signs both glow — you're a smart spender![/bold green]

A perfectly balanced budget floats on the page,
every dollar accounted for.

[bold cyan]"Needs first. Wants second. Compare prices. Think before you buy,"[/bold cyan]
Puck says with a satisfied nod.
[bold cyan]"You've cracked the code of smart spending."[/bold cyan]

A tiny vault door opens in the chest. The bank awaits...
""",
    "banks_and_interest": """
[bold green]The vault door opens — you understand banks and interest![/bold green]

A tiny savings account balance ticks upward: $100... $105... $110.25...
growing all by itself.

[bold cyan]"Your money can grow while you sleep,"[/bold cyan] Puck says, amazed.
[bold cyan]"Interest is one of the most powerful forces in the world of money.
Now you understand how banks work — inside and out."[/bold cyan]

A tiny lemonade stand appears in the chest. Time to build a business!
""",
    "entrepreneurship": """
[bold green]The lemonade stand glows — you're an entrepreneur![/bold green]

A little cash register rings: costs subtracted, profit counted,
a successful business humming along.

[bold cyan]"You know what most people never learn,"[/bold cyan] Puck says proudly.
[bold cyan]"How a business actually works: costs, revenue, profit.
Ideas that solve problems. The courage to try."[/bold cyan]

A warm light glows from deep in the chest. The giving heart awaits...
""",
    "sharing_and_giving": """
[bold green]The giving heart glows — you understand the power of sharing![/bold green]

Tiny golden coins flow outward, building roads, filling food banks,
lighting up a community.

[bold cyan]"Money isn't just for you,"[/bold cyan] Puck says softly.
[bold cyan]"When we share — through charity, volunteering, and taxes —
we build a world that works for everyone.
You have a generous heart."[/bold cyan]

Coins from around the world tumble out. One last treasure to claim!
""",
    "global_money": """
[bold green]The treasure chest blazes with light from every currency on Earth![/bold green]

Dollars, euros, yen, rupees, pounds — all glowing side by side,
each one beautiful, each one different.

[bold cyan]"You've done it,"[/bold cyan] Puck whispers, his eyes wide.
[bold cyan]"You understand money — where it came from, how to earn it,
save it, spend it wisely, grow it in a bank, build a business,
share it generously, and see it in every country on Earth."[/bold cyan]

Puck closes the treasure chest gently. But now it has YOUR name on it.

[bold white]Penny Pincher. Smart Saver. Young Entrepreneur. Global Thinker.[/bold white]
[bold white]That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "what_is_money": "Puck draws a glowing timeline in the air — from cave paintings to coins to paper to phones. [bold yellow]\"The whole history of money in one question. Think carefully about what came first!\"[/bold yellow]",
    "earning_and_saving": "Puck holds up five tiny coins and three little jars: Save, Spend, Give. [bold yellow]\"Splitting your money wisely is the greatest skill of all. Let's see if you can do it!\"[/bold yellow]",
    "spending_wisely": "Puck pulls out a tiny chalkboard with a money puzzle. [bold yellow]\"A real budget — adding, subtracting, figuring out what's left. Ready to crunch the numbers?\"[/bold yellow]",
    "banks_and_interest": "Puck stands between a saver and a borrower, arrows flowing both ways. [bold yellow]\"Banks sit right in the middle. They pay one, charge the other, and keep the difference. But can you explain WHY?\"[/bold yellow]",
    "entrepreneurship": "Puck puts on a tiny business hat and grabs a calculator. [bold yellow]\"You know your costs. You know your price. You know how many you sold. Time for the big calculation!\"[/bold yellow]",
    "sharing_and_giving": "Puck holds a single small coin — but behind him, hundreds of people each hold one too. [bold yellow]\"One coin is small. But what happens when EVERYONE gives one? Let's find out.\"[/bold yellow]",
    "global_money": "Puck opens a tiny passport and stamps it three times — USA, UK, Japan. [bold yellow]\"Three countries, three currencies. Where do you go to swap one for another?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "money_historian": (
        "Money Historian",
        "Traced the story of money from bartering to paper bills!",
    ),
    "smart_saver": (
        "Smart Saver",
        "Learned how to earn money and save it patiently!",
    ),
    "budget_master": (
        "Budget Master",
        "Mastered needs vs. wants and the art of budgeting!",
    ),
    "vault_keeper": (
        "Vault Keeper",
        "Opened the vault and understood banks and interest!",
    ),
    "young_entrepreneur": (
        "Young Entrepreneur",
        "Built a lemonade stand and calculated real profit!",
    ),
    "generous_heart": (
        "Generous Heart",
        "Discovered the power of charity, taxes, and community!",
    ),
    "world_trader": (
        "World Trader",
        "Explored currencies and exchange rates around the globe!",
    ),
}
