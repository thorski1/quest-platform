"""
story.py — Narrative for the Numbers skill pack.

Long Long guides you through the Chinese number system, from 1-10
through measure words, money, time, and dates.
"""

INTRO_STORY = """
[bold red]LEARN CHINESE[/bold red]
[bold yellow]Chapter: The Number Dragon[/bold yellow]

Long Long landed beside an ancient abacus, its wooden beads
polished smooth by centuries of counting. The dragon's claws
clicked the beads back and forth with practiced ease.

[bold cyan]"Numbers,"[/bold cyan] Long Long said, [bold cyan]"are the skeleton of daily life.
How much does this cost? What time is it? When's your birthday?
You can't answer any of these without numbers."[/bold cyan]

Long Long held up one claw, then two, then flashed all five
in a gesture that looked nothing like what you'd expect.

[bold cyan]"And here's something fascinating: Chinese people can
count to ten on ONE hand. The hand gestures for 6 through 10
are completely different from the West."[/bold cyan]

Long Long slid beads on the abacus.

[bold cyan]"Chinese numbers are beautifully logical. Once you know
1 through 10, you can build any number. Eleven is literally
'ten-one'. Twenty is 'two-ten'. A hundred is 'one hundred'.
No 'eleven' or 'twelve' nonsense like English!"[/bold cyan]

The dragon grinned.

[bold cyan]"Ready to count like a dragon?"[/bold cyan]

[bold white]Your journey into Chinese numbers begins now.[/bold white]
"""

ZONE_INTROS = {
    "numbers_1_10": """
Long Long held up the golden claws one at a time.

[bold cyan]"Let's start with the foundation: one through ten,"[/bold cyan]
Long Long said. [bold cyan]"These ten numbers are the building blocks
for EVERY number in Chinese. Learn them well, and you can
count to ten thousand."[/bold cyan]

[bold yellow]yi  er  san  si  wu  liu  qi  ba  jiu  shi[/bold yellow]
[bold yellow]一  二  三  四  五  六  七  八  九  十[/bold yellow]

[bold white]Let's master the first ten numbers![/bold white]
""",
    "numbers_11_99": """
Long Long clicked abacus beads into the tens column.

[bold cyan]"Here's where Chinese gets beautiful,"[/bold cyan] Long Long said.
[bold cyan]"Eleven is 'ten-one' (shi yi). Twenty is 'two-ten' (er shi).
Ninety-nine is 'nine-ten-nine' (jiu shi jiu).
No irregular numbers like English 'eleven' or 'twelve'!"[/bold cyan]

[bold white]Let's build every number from 11 to 99![/bold white]
""",
    "numbers_100_plus": """
Long Long expanded the abacus to show more columns.

[bold cyan]"Big numbers in Chinese use a different system,"[/bold cyan]
Long Long explained. [bold cyan]"Chinese has a word for ten-thousand: wan (万).
English doesn't -- you say 'ten thousand'. This means
Chinese and English group large numbers differently."[/bold cyan]

[bold white]Let's tackle hundreds, thousands, and beyond![/bold white]
""",
    "counting_words": """
Long Long placed different objects on the table: a book, a cup, a dog.

[bold cyan]"In Chinese, you can't just say 'one book' or 'three dogs',"[/bold cyan]
Long Long said. [bold cyan]"You need a measure word between the number
and the noun. Different objects use different measure words.
It's like English 'a PIECE of cake' or 'a GLASS of water'
-- but for everything."[/bold cyan]

[bold white]Let's learn the essential measure words![/bold white]
""",
    "money": """
Long Long pulled out a handful of Chinese currency.

[bold cyan]"Money talks -- and in Chinese, it talks in yuan,"[/bold cyan]
Long Long said. [bold cyan]"The formal word is yuan (元), but
everyone says kuai (块) in daily life. Like the difference
between 'dollar' and 'buck' in English."[/bold cyan]

[bold white]Let's learn to talk about money and prices![/bold white]
""",
    "time": """
Long Long pointed to a clock with Chinese numerals.

[bold cyan]"What time is it? ji dian le?"[/bold cyan] Long Long asked.
[bold cyan]"Chinese tells time using dian (点, o'clock) for hours
and fen (分) for minutes. Three o'clock is san dian.
Half past is ban. Simple and logical."[/bold cyan]

[bold white]Let's learn to tell time in Chinese![/bold white]
""",
    "dates": """
Long Long opened a Chinese calendar.

[bold cyan]"Dates in Chinese go from BIGGEST to SMALLEST,"[/bold cyan]
Long Long explained. [bold cyan]"Year first, then month, then day.
And months are just numbers: January is 'one-month',
February is 'two-month'. No new words to memorize!"[/bold cyan]

[bold white]Let's master the Chinese calendar![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "numbers_1_10": """
[bold green]Long Long counted ten golden sparks from dragon claws![/bold green]

[bold cyan]"Yi, er, san, si, wu, liu, qi, ba, jiu, shi!
You know the ten building blocks. Everything else builds from here!"[/bold cyan]
""",
    "numbers_11_99": """
[bold green]Long Long clicked ninety-nine beads on the abacus![/bold green]

[bold cyan]"From eleven to ninety-nine -- every double-digit number mastered!
The beauty of Chinese numbers is their perfect logic."[/bold cyan]
""",
    "numbers_100_plus": """
[bold green]Long Long breathed fire that spelled out 10,000![/bold green]

[bold cyan]"Hundreds, thousands, and the mighty wan (ten-thousand)!
You can now handle numbers in the millions and beyond!"[/bold cyan]
""",
    "counting_words": """
[bold green]Long Long lined up objects, each with its perfect measure word![/bold green]

[bold cyan]"Measure words mastered! This is one of the hardest parts
of Chinese for English speakers, and you've nailed it!"[/bold cyan]
""",
    "money": """
[bold green]Long Long flipped a golden coin with the dragon tail![/bold green]

[bold cyan]"You can talk about money, ask prices, and understand costs.
You could haggle in a Chinese market now!"[/bold cyan]
""",
    "time": """
[bold green]Long Long pointed to the clock triumphantly![/bold green]

[bold cyan]"You can tell time in Chinese! Hours, minutes, morning and afternoon.
You'll never be late -- in any language!"[/bold cyan]
""",
    "dates": """
[bold green]Long Long circled a date on the calendar with a golden claw![/bold green]

[bold cyan]"Years, months, days, and days of the week -- all mastered!
The Chinese calendar system makes so much logical sense."[/bold cyan]
""",
}

BOSS_INTROS = {
    "numbers_1_10": """
Long Long held up a claw.

[bold cyan]"Quick count challenge! All ten numbers plus the hand gestures.
Show me you've got the foundation solid!"[/bold cyan]
""",
    "numbers_11_99": """
Long Long spun the abacus.

[bold cyan]"Build me any number from 11 to 99. No hesitation!"[/bold cyan]
""",
    "numbers_100_plus": """
Long Long wrote a massive number in the air.

[bold cyan]"Big number showdown! Can you handle the wan system?"[/bold cyan]
""",
    "counting_words": """
Long Long scattered objects across the table.

[bold cyan]"Match the object to its measure word. Every one is different!"[/bold cyan]
""",
    "money": """
Long Long set up a market stall.

[bold cyan]"Buy and sell! Can you handle prices, change, and bargaining?"[/bold cyan]
""",
    "time": """
Long Long pointed to a complicated schedule.

[bold cyan]"What time is it? When does it start? Morning or evening?
Show me you can handle any time question!"[/bold cyan]
""",
    "dates": """
Long Long held up a calendar full of marked dates.

[bold cyan]"Year, month, day, day of the week -- give me the full date
in Chinese. Every part of it!"[/bold cyan]
""",
}
