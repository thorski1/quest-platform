"""
story.py — Narrative for the Family & Home skill pack.

Umi (海) guides you through a seaside village, exploring the warmth of
Japanese family life, the rooms of a traditional home, and daily routines.
"""

INTRO_STORY = """
[bold red]LEARN JAPANESE[/bold red]
[bold yellow]Chapter: Family & Home[/bold yellow]

A narrow lane wound uphill from the harbor, lined with wooden houses
whose sliding doors stood open to the morning breeze.

Laundry fluttered on balconies, the scent of miso soup drifted
from open kitchens, and somewhere a child called out
[bold cyan]「お母さん！」[/bold cyan]

Umi waited at a crossroads where a stone lantern marked the
entrance to a quiet residential neighborhood.

[bold cyan]"Family is the heart of Japanese culture,"[/bold cyan] Umi said softly.

[bold cyan]"The words for mother, father, brother, sister --
they change depending on who you're speaking to.
The rooms of a home have their own vocabulary.
Even daily routines follow a rhythm
you can hear in the language itself."[/bold cyan]

She gestured toward the houses around you.

[bold cyan]"Today we learn the language of home.
The people who live there, the spaces they share,
and the small rituals that hold a family together."[/bold cyan]

Umi started up the lane, morning light catching her hair.

[bold cyan]"Let's step inside -- every family has a story to tell."[/bold cyan]

[bold white]Your journey into Japanese family life begins now.[/bold white]
"""

ZONE_INTROS = {
    "family_members": """
Umi opened a photo album on a low wooden table.
Each page showed a different family portrait.

[bold cyan]"Let's start with the people,"[/bold cyan]
Umi said, tracing the faces in the photos.
[bold cyan]"お父さん, お母さん, 兄, 姉, 弟, 妹,
おじいさん, おばあさん -- father, mother,
brothers, sisters, grandparents.
These are the first words every Japanese child learns."[/bold cyan]

[bold white]Let's learn the family members![/bold white]
""",
    "polite_casual_family": """
Umi sat across from you at a kitchen table,
two columns written on a sheet of paper: ウチ and ソト.

[bold cyan]"In Japanese, you speak differently about your family
depending on your audience,"[/bold cyan] Umi explained.
[bold cyan]"父 when talking to a colleague.
お父さん when talking to your dad.
This humble/polite distinction is one of the most
important concepts in Japanese society."[/bold cyan]

[bold white]Let's master polite and casual family terms![/bold white]
""",
    "rooms_in_house": """
Umi slid open the front door of a traditional Japanese house
and stepped down into the genkan.

[bold cyan]"A Japanese home is a world of its own,"[/bold cyan]
Umi said, removing her shoes.
[bold cyan]"部屋, 台所, お風呂, トイレ, 寝室 --
each room has a purpose, a name, and often
its own set of customs. The genkan alone
has rules that every visitor must follow."[/bold cyan]

[bold white]Let's explore the rooms of a Japanese house![/bold white]
""",
    "daily_routines": """
An alarm clock rang softly in a bedroom
where morning light filtered through paper screens.

[bold cyan]"Every day follows a rhythm,"[/bold cyan] Umi said,
stretching beside the window.
[bold cyan]"起きる, 顔を洗う, 歯を磨く, 食べる,
出かける, 帰る, 寝る -- wake up, wash,
brush, eat, leave, return, sleep.
These verbs are the heartbeat of daily life."[/bold cyan]

[bold white]Let's learn the daily routine![/bold white]
""",
    "describing_family": """
Umi handed you a blank card and a pen.

[bold cyan]"Now you put it all together,"[/bold cyan] Umi said.
[bold cyan]"何人家族ですか -- how many in your family?
一緒に住んでいます -- we live together.
You know the members. You know humble and polite.
Now let's learn to describe your family
the way a Japanese speaker would."[/bold cyan]

[bold white]Let's learn to describe your family![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "family_members": """
[bold green]Umi closed the photo album with a satisfied smile![/bold green]

[bold cyan]"お父さん, お母さん, 兄, 姉, 弟, 妹,
おじいさん, おばあさん -- you know them all now.
These eight words are the foundation of
family vocabulary in Japanese.
Every conversation about home starts here."[/bold cyan]
""",
    "polite_casual_family": """
[bold green]Umi drew a line connecting the ウチ and ソト columns![/bold green]

[bold cyan]"父 and お父さん. 母 and お母さん.
You understand the difference now --
when to humble your own family
and when to elevate someone else's.
This is real Japanese fluency."[/bold cyan]
""",
    "rooms_in_house": """
[bold green]Umi slid open the last door in the house![/bold green]

[bold cyan]"部屋, 台所, お風呂, トイレ, 寝室,
居間, 玄関, 庭 -- you can name every
corner of a Japanese home now.
From the genkan to the garden,
this house has no secrets left."[/bold cyan]
""",
    "daily_routines": """
[bold green]Umi checked off every item on a daily schedule![/bold green]

[bold cyan]"起きる, 寝る, 食べる, 歯を磨く,
顔を洗う, 着替える, 出かける, 帰る --
you know the rhythm of a Japanese day.
Morning to night, these verbs will carry you
through every conversation about daily life."[/bold cyan]
""",
    "describing_family": """
[bold green]Umi held up your completed family card with pride![/bold green]

[bold cyan]"何人家族ですか -- you can answer.
一緒に住んでいます -- you can explain.
Father, mother, siblings, jobs --
you can describe your entire family in Japanese.
That's not just vocabulary. That's connection."[/bold cyan]
""",
}

BOSS_INTROS = {
    "family_members": """
Umi spread out eight cards, each with a family member's kanji.

[bold cyan]"You've met everyone in the family.
Now prove you remember them all --
from grandparents to youngest sibling."[/bold cyan]
""",
    "polite_casual_family": """
Umi set up a role-play scenario: you're at the office,
talking about your family.

[bold cyan]"Humble or polite? The situation decides.
Show me you know which form to use
and when. One wrong word changes everything."[/bold cyan]
""",
    "rooms_in_house": """
Umi stood at the center of the house and pointed in every direction.

[bold cyan]"Name every room from memory.
Genkan to garden, kitchen to bedroom.
A house is only a home when you know
every corner by name."[/bold cyan]
""",
    "daily_routines": """
Umi held up a blank daily schedule.

[bold cyan]"Fill in the day from morning to night.
Wake up, wash, eat, leave, return, sleep.
One complete day, all in Japanese."[/bold cyan]
""",
    "describing_family": """
Umi handed you a microphone and smiled.

[bold cyan]"Introduce your family to the class.
How many members? Who are they?
Where do you live? What do they do?
Everything you've learned -- in one answer."[/bold cyan]
""",
}
