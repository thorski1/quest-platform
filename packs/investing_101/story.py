"""
story.py — Narrative for the Investing Fundamentals skill pack.

SAGE guides learners through the world of investing —
from stocks and bonds to ETFs, risk management, and portfolio construction.
Theme: "Make your money work for you."
"""

INTRO_STORY = """
[bold yellow]FINANCE QUEST[/bold yellow]
[bold yellow]Module: Investing Fundamentals[/bold yellow]

The study transformed. The oak shelves remained, but now they held
not ledgers but screens — live tickers scrolling green and red numbers,
charts tracing decades of market history, and a globe dotted with
glowing points representing every major stock exchange on Earth.

SAGE stepped forward, adjusting wire-rimmed glasses to observe
a century-long chart of the S&P 500.

[bold cyan]"Saving money is essential,"[/bold cyan] SAGE said,
[bold cyan]"but saving alone won't build wealth. Inflation eats savings
at about 3% per year. A dollar under your mattress today
buys less tomorrow. Every day."[/bold cyan]

Five glowing portals appeared, each leading to a different
corner of the investment world.

[bold cyan]"Investing is how you make money work for you —
how you turn time into your greatest asset instead of your enemy.
But most people either never start, or start without understanding
what they're doing. We're going to fix that."[/bold cyan]

SAGE gestured to the five portals.

[bold cyan]"Five domains. From your first stock to a diversified portfolio.
Each one builds on the last. Each one brings you closer to
financial independence."[/bold cyan]

SAGE's expression sharpened.

[bold cyan]"Make your money work for you. Ready to begin?"[/bold cyan]

[bold white]Your journey to investment literacy begins now.[/bold white]
"""

ZONE_INTROS = {
    "stocks_basics": """
SAGE walked to the first portal, where a giant ticker board
displayed company names and prices in constant motion.

[bold cyan]"Stocks,"[/bold cyan] SAGE said, watching the numbers flicker,
[bold cyan]"are where most people start — and where most people
make their first mistakes. A stock is ownership. A tiny piece
of a real company. When you buy a share, you're buying
a fraction of everything that company earns."[/bold cyan]

A single share certificate materialized, ornate and official.

[bold cyan]"We're going to learn what stocks actually are,
how they make you money, and why understanding the basics
prevents the panic that destroys most new investors."[/bold cyan]

[bold white]Let's understand what you're actually buying.[/bold white]
""",
    "bonds_fixed_income": """
SAGE opened a vault door, revealing shelves of government bonds
and corporate certificates, each with precise terms and dates.

[bold cyan]"Bonds,"[/bold cyan] SAGE said, picking up a Treasury note,
[bold cyan]"are the other side of investing. Where stocks are ownership,
bonds are loans. You lend money to a government or company,
and they pay you back with interest."[/bold cyan]

Interest payments ticked upward on a nearby display.

[bold cyan]"They're less exciting than stocks. But they're the ballast
that keeps a portfolio steady when markets get rough.
Every serious investor needs to understand them."[/bold cyan]

[bold white]Let's learn the language of fixed income.[/bold white]
""",
    "index_funds_etfs": """
SAGE conjured a massive basket, filled with miniature versions
of hundreds of different company logos.

[bold cyan]"Index funds and ETFs,"[/bold cyan] SAGE said, lifting the basket,
[bold cyan]"are arguably the most important invention in the history
of personal investing. Instead of picking individual stocks,
you buy a basket that holds hundreds — even thousands — at once."[/bold cyan]

The basket glowed, its contents diversifying before your eyes.

[bold cyan]"Warren Buffett, Jack Bogle, Nobel Prize winners —
they all agree on this: for most people, index funds
are the single best way to invest. Let's understand why."[/bold cyan]

[bold white]Let's discover the power of the index.[/bold white]
""",
    "risk_and_return": """
SAGE projected a roller coaster — its track shaped exactly like
a stock market chart, with stomach-dropping dips and exhilarating climbs.

[bold cyan]"Risk and return,"[/bold cyan] SAGE said, watching a cart climb
the first hill, [bold cyan]"are two sides of the same coin.
You cannot earn higher returns without accepting higher risk.
Period. Anyone who tells you otherwise is either lying or confused."[/bold cyan]

The cart plunged — then soared higher than before.

[bold cyan]"The goal isn't to eliminate risk. It's to understand it,
measure it, and make sure you're being compensated for taking it.
That's what separates investors from gamblers."[/bold cyan]

[bold white]Let's learn to manage risk like a professional.[/bold white]
""",
    "portfolio_diversification": """
SAGE revealed the final portal — a command center with screens
showing asset classes from around the world: stocks, bonds,
real estate, commodities, international markets.

[bold cyan]"Diversification,"[/bold cyan] SAGE said, orchestrating the screens
into a harmonious display, [bold cyan]"is the only free lunch in investing.
By spreading your money across different types of assets,
you can reduce risk without sacrificing expected return."[/bold cyan]

The screens merged into a single, balanced portfolio visualization.

[bold cyan]"This is where everything comes together. Stocks, bonds, index funds,
risk management — all woven into a portfolio that matches
your goals, your timeline, and your tolerance for volatility."[/bold cyan]

[bold white]Let's build your portfolio.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "stocks_basics": """
[bold green]The ticker board glows with understanding![/bold green]

Shares, dividends, market caps, P/E ratios — the numbers
that once seemed like gibberish now tell clear stories
about real companies.

[bold cyan]"You now speak the language of equities,"[/bold cyan]
SAGE says. [bold cyan]"You know what you're buying
when you buy a stock. That knowledge alone
prevents most beginner mistakes."[/bold cyan]

The bond vault awaits beyond...
""",
    "bonds_fixed_income": """
[bold green]The vault of fixed income knowledge is unlocked![/bold green]

Yields, durations, ratings — bonds are no longer a mystery.
You understand the steady, reliable side of investing.

[bold cyan]"Bonds aren't glamorous,"[/bold cyan] SAGE says,
[bold cyan]"but they're essential. A portfolio without bonds
is like a ship without ballast — fast, but unstable.
Now let's learn the most efficient way to own both."[/bold cyan]

The index fund portal glows ahead...
""",
    "index_funds_etfs": """
[bold green]The basket of index funds overflows with efficiency![/bold green]

Low fees, broad diversification, market returns — the case
for index investing is clear and compelling.

[bold cyan]"You've just learned what takes most investors decades
to figure out,"[/bold cyan] SAGE says.
[bold cyan]"The smartest strategy is often the simplest.
Now let's make sure you understand the risks involved."[/bold cyan]

The risk management roller coaster awaits...
""",
    "risk_and_return": """
[bold green]The risk-return roller coaster has been mastered![/bold green]

Volatility, standard deviation, time horizon — you now understand
that risk isn't something to fear, but something to manage.

[bold cyan]"You can't eliminate risk,"[/bold cyan] SAGE says,
[bold cyan]"but you can ensure you're compensated for it.
That understanding is what separates investors from gamblers.
Now let's put it all together."[/bold cyan]

The portfolio command center awaits for the final challenge...
""",
    "portfolio_diversification": """
[bold green]The portfolio command center hums with balanced precision![/bold green]

Asset classes, allocations, rebalancing — every piece fits together
into a cohesive investment strategy tailored to your life.

[bold cyan]"You've done something extraordinary,"[/bold cyan] SAGE says,
stepping back to admire the portfolio you've constructed.

[bold cyan]"Stocks. Bonds. Index funds. Risk management. Diversification.
Five pillars. One investment philosophy.
You didn't just learn about investing —
you built a framework for [italic]building wealth[/italic]."[/bold cyan]

SAGE smiles with quiet confidence.

[bold cyan]"Make your money work for you.
That's not a dream anymore. It's a plan."[/bold cyan]

[bold white]Market Sage. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "stocks_basics": "SAGE projects a stock that just dropped 30% in a week. [bold yellow]\"Everyone is panicking. The headlines are terrifying. But the company's fundamentals haven't changed. What do you do — and more importantly, why? This is where real investors are made.\"[/bold yellow]",
    "bonds_fixed_income": "SAGE presents a scenario: interest rates just rose 1%. [bold yellow]\"Your bond portfolio dropped in value. Half your friends are saying bonds are dead. Walk me through what actually happened, what it means for your strategy, and whether you should change anything.\"[/bold yellow]",
    "index_funds_etfs": "SAGE shows two fund options: a hot actively managed fund that returned 25% last year with a 1.2% fee, and an index fund that returned 18% with a 0.03% fee. [bold yellow]\"Your colleague swears the active fund is better. Make the case — with math — for which is the better long-term choice.\"[/bold yellow]",
    "risk_and_return": "SAGE presents a portfolio stress test: a 40% market crash just happened, similar to 2008. [bold yellow]\"You're 35, retirement is 30 years away, and your portfolio just lost $120,000 on paper. Talk me through your decision process. Panic or plan?\"[/bold yellow]",
    "portfolio_diversification": "SAGE lays out a complete financial profile: age 30, $80,000 income, $50,000 to invest, moderate risk tolerance, 30-year horizon. [bold yellow]\"Design this person a portfolio. Asset allocation, specific fund types, rebalancing strategy, and the reasoning behind every choice. This is portfolio architecture.\"[/bold yellow]",
}
