"""
story.py — Narrative for the School & Education skill pack.

龙龙 (Lóng Lóng) guides the learner through Chinese school vocabulary —
subjects, classroom objects, school actions, talking about school,
and school life.
"""

INTRO_STORY = """
[bold yellow]LEARN CHINESE[/bold yellow]
[bold yellow]Chapter: School & Education — 学校与教育[/bold yellow]

龙龙 swooped through a stone archway and landed in the courtyard
of a towering medieval academy. Banners bearing Chinese characters
hung from the turrets, and the sound of a great bell echoed across
the grounds.

[bold cyan]"Welcome to the Academy,"[/bold cyan] 龙龙 said, folding its
wings. [bold cyan]"In China, school is the center of life. Students
spend years mastering their subjects, and the words they use every
day — 学习, 考试, 老师, 同学 — are some of the most important
in the entire language."[/bold cyan]

The dragon gestured toward the castle's many towers.

[bold cyan]"We'll explore five parts of school life: the subjects
you study, the objects in your classroom, the actions of your
school day, how to talk about your opinions, and the people
and places that make school feel like home."[/bold cyan]

龙龙 grinned, smoke curling from its nostrils.

[bold cyan]"Ready to enroll?"[/bold cyan]

[bold white]Your journey through Chinese school life begins now.[/bold white]
"""

ZONE_INTROS = {
    "school_subjects": """
龙龙 led you into a grand lecture hall lined with subject banners.

[bold cyan]"Every scholar must know the names of their studies,"[/bold cyan]
龙龙 said, pointing a claw at each banner in turn.
[bold cyan]"数学, 英语, 科学, 历史, 体育 — math, English, science,
history, PE. Five subjects, five keys to the scholar's path."[/bold cyan]

The banners shimmered with golden characters:
[bold yellow]数学 · 英语 · 科学 · 历史 · 体育[/bold yellow]

[bold white]Let's name your subjects![/bold white]
""",
    "classroom_objects": """
龙龙 pushed open the door to an enchanted classroom. Quills floated
in mid-air and books arranged themselves on shelves.

[bold cyan]"Every student needs their tools,"[/bold cyan] 龙龙 said.
[bold cyan]"书, 笔, 本子, 电脑, 黑板 — book, pen, notebook,
computer, blackboard. These are your weapons of knowledge!"[/bold cyan]

Objects drifted toward you, each glowing with its Chinese name:
[bold yellow]书 · 笔 · 本子 · 电脑 · 黑板[/bold yellow]

[bold white]Let's learn your tools![/bold white]
""",
    "school_actions": """
龙龙 perched atop the academy's clock tower as bells tolled the hour.

[bold cyan]"A school day is built from actions,"[/bold cyan] 龙龙 said.
[bold cyan]"学习, 考试, 做作业, 上课, 下课 — study, test,
do homework, start class, end class. Master these verbs and you'll
understand the rhythm of every school day."[/bold cyan]

The clock hands spun through the daily schedule:
[bold yellow]学习 · 考试 · 做作业 · 上课 · 下课[/bold yellow]

[bold white]Let's learn the daily grind![/bold white]
""",
    "talking_about_school": """
龙龙 sat across from you at a round table in the scholars' common room.

[bold cyan]"Knowing words is good. Having opinions is better!"[/bold cyan]
龙龙 said. [bold cyan]"你学什么? 我最喜欢科学。数学很难。英语很容易。
Now it's time to TALK about school — your favorites, your struggles,
your reasons."[/bold cyan]

Conversation bubbles floated around the room:
[bold yellow]你学什么 · 我最喜欢 · 难 · 容易[/bold yellow]

[bold white]Let's share some opinions![/bold white]
""",
    "school_life": """
龙龙 gave you a tour of the entire academy — towers, halls,
courtyards, and all.

[bold cyan]"School isn't just classes,"[/bold cyan] 龙龙 said warmly.
[bold cyan]"It's the people and places. 同学 who study beside you.
老师 who guide you. The 图书馆 where you lose yourself in books.
The 食堂 where everyone gathers to eat. This is school LIFE."[/bold cyan]

Figures and buildings glowed on a magical map:
[bold yellow]同学 · 老师 · 图书馆 · 食堂[/bold yellow]

[bold white]Let's explore the academy![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "school_subjects": """
[bold green]All five subjects — named and conquered![/bold green]

数学, 英语, 科学, 历史, 体育 — your academic vocabulary is set.

[bold cyan]"You also discovered the 学 pattern,"[/bold cyan] 龙龙 says.
[bold cyan]"数学, 科学, 化学, 文学 — one character that unlocks
every field of study. That's the power of Chinese patterns!"[/bold cyan]

The classroom door creaks open. Time for the next zone...
""",
    "classroom_objects": """
[bold green]The enchanted classroom — fully catalogued![/bold green]

书, 笔, 本子, 电脑, 黑板 — every tool at your fingertips.

[bold cyan]"You found the 电 pattern too,"[/bold cyan] 龙龙 says.
[bold cyan]"电脑, 电话, 电视, 电影 — 'electric' plus something poetic.
Chinese builds modern words from ancient roots!"[/bold cyan]

The bell tolls. Class is about to begin...
""",
    "school_actions": """
[bold green]Every school action — learned and drilled![/bold green]

学习, 考试, 做作业, 上课, 下课 — you know the full routine.

[bold cyan]"The 上/下 pattern is yours now,"[/bold cyan] 龙龙 says.
[bold cyan]"上课/下课, 上班/下班, 上车/下车 — begin and end,
on and off. One of the most useful pairs in Chinese!"[/bold cyan]

Time to share your opinions about school...
""",
    "talking_about_school": """
[bold green]Opinions unlocked — you can TALK about school![/bold green]

Favorites, difficulty, reasons — all in Chinese.

[bold cyan]"You can now say things like 我最喜欢科学课，因为很有意思,"[/bold cyan]
龙龙 says. [bold cyan]"That's not just vocabulary — that's a real
conversation. You're thinking in Chinese!"[/bold cyan]

One final zone remains — the people and places of school life...
""",
    "school_life": """
[bold green]The academy tour is complete — you know school life![/bold green]

同学, 老师, 图书馆, 食堂 — the heart and soul of school.

[bold cyan]"You discovered the 馆 pattern,"[/bold cyan] 龙龙 says.
[bold cyan]"图书馆, 博物馆, 体育馆, 餐馆 — one character that
marks any public building. Patterns are your superpower!"[/bold cyan]

[bold white]School master. Subject expert. Conversation scholar.
That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "school_subjects": "龙龙 holds up five subject banners. [bold yellow]\"数学, 英语, 科学, 历史, 体育 — can you match them all?\"[/bold yellow]",
    "classroom_objects": "龙龙 plays teacher and gives a command. [bold yellow]\"请打开书，拿出笔和本子! Can you understand the teacher?\"[/bold yellow]",
    "school_actions": "龙龙 rings the great bell. [bold yellow]\"From 上课 to 考试 — do you know the order of a school day?\"[/bold yellow]",
    "talking_about_school": "龙龙 challenges you to translate. [bold yellow]\"我最喜欢科学课，因为很有意思，不太难。Prove you can think in Chinese!\"[/bold yellow]",
    "school_life": "龙龙 points to the academy map. [bold yellow]\"老师在图书馆 — which sentence means 'The teacher is in the library'?\"[/bold yellow]",
}
