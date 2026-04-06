"""
story.py — Narrative for the Numbers skill pack.

Sensei (先生) guides you through the Japanese number system,
from basic counting to counters, time, and money.
"""

INTRO_STORY = """
[bold red]LEARN JAPANESE[/bold red]
[bold yellow]Chapter: The World of Japanese Numbers[/bold yellow]

Sensei placed an old wooden abacus on the desk, its beads
clicking softly as they slid along the rods.

[bold cyan]"Numbers in Japanese are wonderfully logical,"[/bold cyan]
Sensei said, sliding beads back and forth.
[bold cyan]"Once you learn one through ten, you can build
any number. Eleven is simply 'ten-one'. Twenty is 'two-ten'.
The system makes perfect mathematical sense."[/bold cyan]

Sensei paused, then smiled.

[bold cyan]"But Japanese numbers have a special twist --
counters. You don't just say 'three' -- you say
'three flat things' or 'three long things' or
'three people'. The counter changes based on
what you're counting."[/bold cyan]

Sensei held up three pencils and three sheets of paper.

[bold cyan]"Three pencils: さんぼん. Three papers: さんまい.
Different counters for different shapes.
Ready to master the art of Japanese counting?"[/bold cyan]

[bold white]Your journey into Japanese numbers begins now.[/bold white]
"""

ZONE_INTROS = {
    "one_to_ten": """
Sensei held up fingers one at a time.

[bold cyan]"The foundation: one through ten,"[/bold cyan] Sensei began.
[bold cyan]"いち (1), に (2), さん (3), し/よん (4), ご (5),
ろく (6), しち/なな (7), はち (8), きゅう/く (9), じゅう (10).
Notice: 4, 7, and 9 each have TWO readings!"[/bold cyan]

[bold white]Let's count from one to ten![/bold white]
""",
    "eleven_to_99": """
Sensei wrote じゅういち on the board.

[bold cyan]"Building bigger numbers is simple,"[/bold cyan] Sensei said.
[bold cyan]"11 = じゅう + いち = じゅういち (ten-one).
20 = に + じゅう = にじゅう (two-ten).
99 = きゅうじゅうきゅう (nine-ten-nine)."[/bold cyan]

[bold white]Let's build numbers from 11 to 99![/bold white]
""",
    "hundreds_plus": """
Sensei clicked the abacus to show larger numbers.

[bold cyan]"For hundreds, we use ひゃく,"[/bold cyan] Sensei explained.
[bold cyan]"But be careful -- 300, 600, and 800 have sound changes!
さんびゃく, ろっぴゃく, はっぴゃく.
Thousands use せん. Ten-thousands use まん."[/bold cyan]

[bold white]Let's master big numbers![/bold white]
""",
    "counters": """
Sensei laid out objects of different shapes on the desk.

[bold cyan]"This is uniquely Japanese,"[/bold cyan] Sensei said.
[bold cyan]"When counting objects, you must use the right counter:
つ (general), 人 (にん, people), 本 (ほん, long things),
枚 (まい, flat things). Choose wrong and it sounds strange!"[/bold cyan]

[bold white]Let's learn the essential Japanese counters![/bold white]
""",
    "time": """
Sensei pointed to a clock on the wall.

[bold cyan]"Telling time uses じ (ji) for hours and ふん (fun) for minutes,"[/bold cyan]
Sensei said. [bold cyan]"いちじ = 1 o'clock, にじ = 2 o'clock.
But watch out -- 4 o'clock is よじ, not しじ,
and some minutes have sound changes!"[/bold cyan]

[bold white]Let's learn to tell time in Japanese![/bold white]
""",
    "money": """
Sensei placed coins and bills on the desk.

[bold cyan]"Japan uses 円 (えん, en/yen),"[/bold cyan] Sensei explained.
[bold cyan]"No decimals, no cents. Prices are whole numbers.
ひゃくえん = 100 yen. せんえん = 1000 yen.
And asking 'how much?' is いくらですか."[/bold cyan]

[bold white]Let's learn about Japanese money![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "one_to_ten": """
[bold green]Sensei clapped the abacus beads together![/bold green]

[bold cyan]"いち through じゅう -- the foundation is set!
With these ten numbers, you can build every number in Japanese."[/bold cyan]
""",
    "eleven_to_99": """
[bold green]Sensei beamed with pride![/bold green]

[bold cyan]"You can construct any number up to 99. The logic is
beautifully simple -- Japanese numbers build like blocks."[/bold cyan]
""",
    "hundreds_plus": """
[bold green]Sensei struck the desk with satisfaction![/bold green]

[bold cyan]"Hundreds, thousands, ten-thousands -- even the sound changes
can't stop you. You can now handle any practical number in Japan."[/bold cyan]
""",
    "counters": """
[bold green]Sensei lined up all the objects neatly![/bold green]

[bold cyan]"You've mastered the essential counters. つ for general counting,
人 for people, 本 for long things, 枚 for flat things.
This is a skill many Japanese learners struggle with!"[/bold cyan]
""",
    "time": """
[bold green]Sensei adjusted the clock with a smile![/bold green]

[bold cyan]"You can read the time in Japanese. なんじですか will never
stump you again. Trains, meetings, daily life -- time is everywhere."[/bold cyan]
""",
    "money": """
[bold green]Sensei handed you an imaginary wallet![/bold green]

[bold cyan]"You can handle money in Japanese! Shopping, dining,
travel -- いくらですか and you're ready for anything."[/bold cyan]
""",
}

BOSS_INTROS = {
    "one_to_ten": """
Sensei held up the abacus.

[bold cyan]"Quick count! All ten numbers, including
the tricky double readings for 4, 7, and 9."[/bold cyan]
""",
    "eleven_to_99": """
Sensei wrote random two-digit numbers.

[bold cyan]"Build these numbers from their parts.
Speed and accuracy!"[/bold cyan]
""",
    "hundreds_plus": """
Sensei showed large numbers on cards.

[bold cyan]"Big numbers with sound changes.
さんびゃく, ろっぴゃく -- can you handle them all?"[/bold cyan]
""",
    "counters": """
Sensei placed mixed objects in front of you.

[bold cyan]"Choose the right counter for each object.
Pencils, papers, people, and general items."[/bold cyan]
""",
    "time": """
Sensei pointed to different clock positions.

[bold cyan]"What time is it? Quick -- the train is leaving!"[/bold cyan]
""",
    "money": """
Sensei set up a mock shopping scenario.

[bold cyan]"How much does it cost? Can you count your change?
The ultimate money challenge!"[/bold cyan]
""",
}
