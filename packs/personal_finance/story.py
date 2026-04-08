"""
story.py — Narrative for the Personal Finance 101 skill pack.

SAGE guides learners through mastering everyday money management —
from budgeting and saving to debt, credit, and insurance.
Theme: "Take control of your money before it controls you."
"""

INTRO_STORY = """
[bold yellow]FINANCE QUEST[/bold yellow]
[bold yellow]Module: Personal Finance 101[/bold yellow]

The screen flickered to life. Where there had been darkness, a warm
study materialized — leather-bound ledgers lining oak shelves, a mahogany
desk covered with neatly organized financial statements, and a window
overlooking a city skyline at sunset.

A figure stepped out from behind the desk — composed, confident,
with the quiet authority of someone who has guided thousands
through their financial awakening.

[bold cyan]"I'm SAGE,"[/bold cyan] the figure said, adjusting wire-rimmed glasses.
[bold cyan]"And this — "[/bold cyan] a gesture swept across the study,
[bold cyan]" — is where you learn to take control of your money."[/bold cyan]

Five glowing folders appeared on the desk, each labeled
with a different financial domain.

[bold cyan]"Most people never learn this. Not in school. Not from their parents.
They figure it out the hard way — overdraft fees, surprise bills,
debt that snowballs. But you're here. That already puts you ahead."[/bold cyan]

SAGE tapped the first folder, and it pulsed with golden light.

[bold cyan]"Five domains. From your first budget to protecting everything you build.
Each one practical. Each one something you can act on [italic]today[/italic]."[/bold cyan]

SAGE's expression sharpened into focus.

[bold cyan]"Take control of your money before it controls you.
Ready to begin?"[/bold cyan]

[bold white]Your journey to financial literacy begins now.[/bold white]
"""

ZONE_INTROS = {
    "budgeting_basics": """
SAGE opened the first folder, revealing a blank spreadsheet
and a stack of receipts.

[bold cyan]"Budgeting,"[/bold cyan] SAGE said, [bold cyan]"is the foundation
of everything. You can't manage what you don't measure.
And most people have no idea where their money actually goes."[/bold cyan]

A pie chart materialized, slicing income into colorful wedges.

[bold cyan]"We're going to fix that. Not with complicated software
or rigid rules — but with a system that works for your life,
your income, and your goals."[/bold cyan]

[bold white]Let's build your first budget.[/bold white]
""",
    "emergency_funds": """
SAGE pulled out a folder marked with a bright red cross.

[bold cyan]"Life throws curveballs,"[/bold cyan] SAGE said, flipping through
scenarios — a car breaking down, a medical bill, a sudden job loss.
[bold cyan]"The question isn't whether something unexpected will happen.
It's whether you'll be ready when it does."[/bold cyan]

A safety net shimmered into existence beneath the desk.

[bold cyan]"An emergency fund isn't exciting. It's not glamorous.
But it's the single most important financial asset you can build.
It's the difference between a setback and a catastrophe."[/bold cyan]

[bold white]Let's build your safety net.[/bold white]
""",
    "debt_management": """
SAGE opened a heavy folder — inside, a tangled web of numbers,
interest rates, and due dates.

[bold cyan]"Debt,"[/bold cyan] SAGE said, carefully untangling a thread,
[bold cyan]"is a tool. Like fire — incredibly useful when controlled,
destructive when it's not. Most people only experience the second kind."[/bold cyan]

The web slowly organized itself into neat, manageable streams.

[bold cyan]"We're going to learn which debts to attack first,
how to stop the bleeding, and how to build a plan
that gets you to zero — and keeps you there."[/bold cyan]

[bold white]Let's conquer your debt.[/bold white]
""",
    "credit_scores": """
SAGE projected a three-digit number into the air — glowing,
shifting, almost alive.

[bold cyan]"Your credit score,"[/bold cyan] SAGE said, watching it pulse,
[bold cyan]"is a number that follows you everywhere.
It decides your interest rates, your apartment applications,
sometimes even your job prospects. And most people have no idea
how it actually works."[/bold cyan]

The number expanded into a detailed breakdown of factors.

[bold cyan]"We're going to demystify it. Every factor. Every trick.
Every way to build it up — and every mistake that tears it down."[/bold cyan]

[bold white]Let's decode your credit score.[/bold white]
""",
    "insurance": """
SAGE revealed the final folder — thick, official-looking,
filled with policy documents and fine print.

[bold cyan]"Insurance,"[/bold cyan] SAGE said, fanning out the pages,
[bold cyan]"is the part of personal finance everyone skips —
until they desperately need it. Health, auto, renters, life —
each one a shield against a different kind of financial disaster."[/bold cyan]

Shields materialized around the desk, each labeled with a different
type of coverage.

[bold cyan]"You don't need to become an insurance expert.
But you do need to know enough to protect yourself
without overpaying for coverage you don't need."[/bold cyan]

[bold white]Let's build your protection plan.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "budgeting_basics": """
[bold green]The spreadsheet glows with a balanced budget![/bold green]

Income, expenses, savings — all accounted for. The pie chart
is perfectly sliced, and every dollar has a job.

[bold cyan]"You've taken the most important step,"[/bold cyan]
SAGE says. [bold cyan]"You know where your money goes.
That alone puts you ahead of most people.
Now let's make sure you're prepared for the unexpected."[/bold cyan]

The emergency fund folder beckons...
""",
    "emergency_funds": """
[bold green]The safety net gleams, strong and ready![/bold green]

Three to six months of expenses, tucked away in a high-yield account.
The red cross folder is now marked with a green checkmark.

[bold cyan]"Peace of mind,"[/bold cyan] SAGE says.
[bold cyan]"That's what an emergency fund really buys you.
Not just money — but the freedom to handle whatever comes
without panic or debt."[/bold cyan]

The debt management folder awaits...
""",
    "debt_management": """
[bold green]The tangled web of debt is organized and shrinking![/bold green]

High-interest debts are targeted. Payment plans are set.
The path to zero is clear and achievable.

[bold cyan]"Debt doesn't have to define your financial life,"[/bold cyan]
SAGE says. [bold cyan]"With the right strategy,
it's just a problem with a solution and a timeline.
Now let's make sure your credit score reflects your progress."[/bold cyan]

The credit score display glows ahead...
""",
    "credit_scores": """
[bold green]The credit score pulses with healthy, rising numbers![/bold green]

Payment history: strong. Utilization: low. Credit age: growing.
The three-digit number shines brighter than before.

[bold cyan]"A good credit score isn't about gaming the system,"[/bold cyan]
SAGE says. [bold cyan]"It's about demonstrating reliability.
And now you know exactly how to do that."[/bold cyan]

The insurance folder awaits for your final challenge...
""",
    "insurance": """
[bold green]The shields of protection glow around you — complete![/bold green]

Health, auto, renters, life — each policy understood,
each coverage level optimized for your situation.

[bold cyan]"You've done something remarkable,"[/bold cyan] SAGE says,
stepping back to admire the complete picture.

[bold cyan]"Budgeting. Emergency funds. Debt management. Credit. Insurance.
Five pillars. One financial foundation.
You didn't just learn about money —
you built a system to [italic]manage[/italic] it."[/bold cyan]

SAGE's expression warms with genuine pride.

[bold cyan]"Take control of your money before it controls you.
That's not advice anymore. It's how you live."[/bold cyan]

[bold white]Financial Master. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "budgeting_basics": "SAGE slides a complex scenario across the desk: a household with irregular income, variable expenses, and competing financial goals. [bold yellow]\"Build me a budget that handles all of this — not a perfect-world budget, but one that works when life is messy. That's real budgeting.\"[/bold yellow]",
    "emergency_funds": "SAGE presents three emergency scenarios hitting simultaneously — a job loss, a medical bill, and a car repair. [bold yellow]\"Your emergency fund needs to handle the worst case, not the average case. Show me you understand how to prepare for when everything goes wrong at once.\"[/bold yellow]",
    "debt_management": "SAGE lays out a complex debt portfolio — student loans, credit cards, a car loan, and a medical bill, each with different rates and terms. [bold yellow]\"Which do you pay first? How much? And what do you do when an unexpected expense threatens your payoff plan? Show me you can think strategically about debt.\"[/bold yellow]",
    "credit_scores": "SAGE projects a credit report with several issues — a missed payment, high utilization, and a short credit history. [bold yellow]\"This person needs to improve their score by 100 points in the next year. Build me a realistic action plan. Not tricks — sustainable habits.\"[/bold yellow]",
    "insurance": "SAGE presents a life scenario: a young professional with a new apartment, a car, student loans, and aging parents. [bold yellow]\"Design an insurance portfolio for this person. What do they need? What can they skip? And how do they balance coverage against cost? This is real-world risk management.\"[/bold yellow]",
}
