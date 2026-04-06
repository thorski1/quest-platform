"""
story.py — Narrative for the Shopping & Money skill pack.

Umi (海) guides you through the bustling markets and shops of a Japanese
coastal town, teaching you to count, pay, request, and bargain.
"""

INTRO_STORY = """
[bold red]LEARN JAPANESE[/bold red]
[bold yellow]Chapter: Shopping & Money[/bold yellow]

The morning sun glittered across the harbor as you stepped onto
a wooden boardwalk lined with market stalls and shops.

The scent of fresh seafood and steamed buns drifted through the air,
mingling with the calls of vendors and the clink of coins.

A familiar figure stood at the entrance to the market district,
a canvas bag slung over one shoulder.

[bold cyan]"Welcome back,"[/bold cyan] Umi said, gesturing to the lively scene.

[bold cyan]"Today we learn the language of shopping.
Numbers, counters, money, polite requests --
everything you need to navigate a Japanese market
with confidence and courtesy."[/bold cyan]

She held up a 500-yen coin, spinning it between her fingers.

[bold cyan]"In Japan, shopping isn't just a transaction.
It's a ritual of politeness. The right counter for
the right object. The right phrase at the right moment.
Even bargaining has its own gentle art."[/bold cyan]

Umi pocketed the coin and began walking into the crowd.

[bold cyan]"Let's dive in -- the tide of commerce waits for no one."[/bold cyan]

[bold white]Your journey into Japanese shopping begins now.[/bold white]
"""

ZONE_INTROS = {
    "numbers_counters": """
Umi spread a collection of objects on a market stall:
apples, pencils, tickets, and small round stones.

[bold cyan]"Before you can buy anything, you need to count it,"[/bold cyan]
Umi said. [bold cyan]"Japanese has special counters for
different shapes of objects. 一つ, 二つ for general things.
〜個 for small objects. 〜本 for long things.
〜枚 for flat things. Get these right and you'll
sound like a natural."[/bold cyan]

[bold white]Let's master numbers and counters![/bold white]
""",
    "money": """
Umi opened a small leather purse and laid out coins and bills
on the counter of a seaside shop.

[bold cyan]"円 -- yen -- is the heartbeat of Japanese commerce,"[/bold cyan]
Umi explained. [bold cyan]"百円, 千円, 一万円 -- you need to
know these denominations by heart. And you need to understand
おつり (change), 税込み (tax included), and how to
talk about money naturally."[/bold cyan]

[bold white]Let's learn the language of money![/bold white]
""",
    "at_the_store": """
Umi led you through the sliding glass doors of a department store
with a view of the ocean from every floor.

[bold cyan]"Now we put words into action,"[/bold cyan] Umi said.
[bold cyan]"いくらですか to ask prices. ください to request items.
売り場 to find the right section. These phrases are
your survival kit for any Japanese store, from a
convenience store to a luxury department store."[/bold cyan]

[bold white]Let's learn essential store phrases![/bold white]
""",
    "polite_requests": """
Umi paused at an elegant gift shop near the harbor,
where clerks bowed to entering customers.

[bold cyan]"Japanese shopping runs on politeness,"[/bold cyan] Umi said quietly.
[bold cyan]"すみません to get attention. お願いします for formal requests.
Knowing how to ask for bags, wrapping, and payment options --
these small courtesies make all the difference.
A polite customer is always treated well."[/bold cyan]

[bold white]Let's master polite shopping requests![/bold white]
""",
    "bargaining_receipts": """
Umi stopped at a street market where red banners
reading セール and 割引 flapped in the ocean wind.

[bold cyan]"Now for the art of the deal,"[/bold cyan] Umi grinned.
[bold cyan]"高い, 安い -- expensive and cheap. 割引 -- discounts.
レシート -- receipts. And the subtle Japanese way
of suggesting a better price without being rude.
Master these and you'll shop like a local."[/bold cyan]

[bold white]Let's learn about bargaining and receipts![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "numbers_counters": """
[bold green]Umi arranged all the counted objects into neat groups![/bold green]

[bold cyan]"You've mastered the counters. 〜個 for round things,
〜本 for long things, 〜枚 for flat things, and 〜つ
for everything else. You can count anything in a store now.
That's the foundation of shopping in Japanese."[/bold cyan]
""",
    "money": """
[bold green]Umi stacked the coins into a perfect tower![/bold green]

[bold cyan]"You know your yen now -- coins, bills, change, and tax.
百円, 千円, 一万円 -- these numbers will flow naturally.
You can handle any price and calculate any change.
The currency of Japan is no longer a mystery."[/bold cyan]
""",
    "at_the_store": """
[bold green]Umi held up a shopping bag full of successful purchases![/bold green]

[bold cyan]"いくらですか, ください, はありますか --
you have the essential phrases to navigate any store.
From convenience stores to department stores,
you can find what you need and ask for what you want."[/bold cyan]
""",
    "polite_requests": """
[bold green]Umi bowed gracefully as the shop clerk smiled warmly![/bold green]

[bold cyan]"すみません, お願いします, けっこうです --
you know the language of courtesy in Japanese shopping.
Politeness isn't just nice -- it's the key that opens doors.
You'll be welcomed back to any shop you visit."[/bold cyan]
""",
    "bargaining_receipts": """
[bold green]Umi held up a receipt and a bag full of great deals![/bold green]

[bold cyan]"高い, 安い, 割引, セール, レシート --
you can read prices, spot deals, and navigate sales.
From lucky bags to discount signs, the world of
Japanese shopping has no more secrets for you."[/bold cyan]
""",
}

BOSS_INTROS = {
    "numbers_counters": """
Umi laid out a mixed tray of items: tickets, pens, and fruit.

[bold cyan]"You've learned the counters. Now prove it --
match each object to the right counter.
Shape determines everything in Japanese counting."[/bold cyan]
""",
    "money": """
Umi handed you a 1,000-yen bill and pointed at a price tag.

[bold cyan]"Simple arithmetic, but in Japanese.
How much change will you get back?
Show me you can handle money."[/bold cyan]
""",
    "at_the_store": """
Umi stood beside a display case in a beautiful shop.

[bold cyan]"You know the phrases. Now put them together.
You see something you want -- how do you ask for it?
One complete, natural sentence."[/bold cyan]
""",
    "polite_requests": """
Umi gestured toward an elegant jewelry display.

[bold cyan]"The full sequence: get attention, identify the item,
make a polite request. Three steps, one smooth sentence.
Show me you can be a courteous Japanese shopper."[/bold cyan]
""",
    "bargaining_receipts": """
Umi pointed to a discount sign with Japanese characters.

[bold cyan]"Read the sign. Calculate the price.
This is the final test -- can you decode
a Japanese discount and find the real price?"[/bold cyan]
""",
}
