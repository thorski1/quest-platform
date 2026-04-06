"""
story.py — Narrative for the Family & Home skill pack.

龙龙 (Lóng Lóng) guides the learner through the rich world of Chinese
family vocabulary — from immediate family to extended clan, rooms of the
house, pets, and the web of relationships that hold Chinese society together.
"""

INTRO_STORY = """
[bold yellow]LEARN CHINESE[/bold yellow]
[bold yellow]Chapter: Family & Home — 家人与家[/bold yellow]

龙龙 appeared in a swirl of golden smoke, landing softly beside
a beautiful ink painting of a Chinese family gathered around a table.
The painting seemed alive — people laughing, children playing,
grandparents smiling.

[bold cyan]"Family,"[/bold cyan] 龙龙 said warmly, [bold cyan]"is the heart of Chinese culture.
And Chinese has the most detailed family vocabulary of any language
in the world. Where English just says 'grandmother,' Chinese has
FOUR different words — one for each grandparent!"[/bold cyan]

The dragon traced a family tree in golden smoke.

[bold cyan]"We'll learn your closest family first — mom, dad, brothers,
sisters. Then we'll meet the wider clan — grandparents, uncles,
aunts. We'll describe people, celebrate birthdays, explore the
rooms of a Chinese home, meet some pets, and learn how Chinese
people address everyone around them."[/bold cyan]

龙龙 smiled and curled its tail into the shape of the character 家.

[bold cyan]"家 — home. A pig under a roof. Prosperity and warmth.
Let's begin!"[/bold cyan]

[bold white]Your journey into the Chinese family begins now.[/bold white]
"""

ZONE_INTROS = {
    "immediate_family": """
龙龙 drew six figures in golden smoke — two tall ones and four smaller ones.

[bold cyan]"Every Chinese child learns these words first,"[/bold cyan] 龙龙 said.
[bold cyan]"妈妈, 爸爸, 哥哥, 姐姐, 弟弟, 妹妹 — mother, father, older
brother, older sister, younger brother, younger sister. Notice
something? Chinese tells you EXACTLY who's older and who's younger.
English doesn't do that!"[/bold cyan]

The six figures glowed:
[bold yellow]爸爸 · 妈妈 · 哥哥 · 姐姐 · 弟弟 · 妹妹[/bold yellow]

[bold white]Let's learn your closest family![/bold white]
""",
    "extended_family": """
龙龙 unfurled a massive family tree that filled the entire scroll.

[bold cyan]"Now here's where Chinese gets truly amazing,"[/bold cyan] 龙龙 said,
eyes bright. [bold cyan]"English has ONE word for 'grandmother.' Chinese has
TWO — 奶奶 for your father's mother, 外婆 for your mother's mother.
And uncles? Don't get me started — there are at least FOUR
different uncle words depending on which side and whether they're
older or younger than your parent!"[/bold cyan]

[bold yellow]爷爷 · 奶奶 · 外公 · 外婆 · 叔叔 · 阿姨[/bold yellow]

[bold white]Let's meet the extended family![/bold white]
""",
    "describing_people": """
龙龙 pulled out an ink brush and started sketching faces in the air.

[bold cyan]"How do we describe people?"[/bold cyan] 龙龙 mused.
[bold cyan]"Tall or short? Thin or round? Beautiful or handsome?
These words come in pairs — opposites that help each other
stick in your memory."[/bold cyan]

[bold yellow]高/矮 · 胖/瘦 · 漂亮 · 帅[/bold yellow]

[bold white]Let's paint people with words![/bold white]
""",
    "ages_birthdays": """
龙龙 held up a birthday cake with candles shaped like zodiac animals.

[bold cyan]"How old are you? 你几岁?"[/bold cyan] 龙龙 asked with a grin.
[bold cyan]"In Chinese culture, your age connects to the great zodiac
cycle — twelve animals, twelve years, each one with its own
personality and fortune."[/bold cyan]

[bold yellow]几岁? · 生日快乐 · 十二生肖[/bold yellow]

[bold white]Let's celebrate ages and birthdays![/bold white]
""",
    "my_house": """
龙龙 pushed open the door to a traditional Chinese courtyard house.

[bold cyan]"家 — home,"[/bold cyan] 龙龙 said, stepping inside.
[bold cyan]"Every room has a name, and every name tells you what
happens there. The 'lying-down room,' the 'cooking room,'
the 'guest hall,' the 'hygiene room.' Chinese is wonderfully
literal!"[/bold cyan]

[bold yellow]卧室 · 厨房 · 客厅 · 卫生间[/bold yellow]

[bold white]Let's explore the rooms of a Chinese home![/bold white]
""",
    "pets_animals": """
龙龙 landed in a garden where cats, dogs, birds, and fish lived together.

[bold cyan]"Animals!"[/bold cyan] 龙龙 said happily, watching a cat chase a butterfly.
[bold cyan]"Every pet has its own character, its own sound, its own
cultural meaning. Did you know that fish are lucky in Chinese?
And that there's a rabbit living on the moon?"[/bold cyan]

[bold yellow]猫 · 狗 · 鱼 · 鸟 · 兔子[/bold yellow]

[bold white]Let's meet our furry and feathered friends![/bold white]
""",
    "relationships": """
龙龙 stood in a bustling Chinese neighborhood — people greeting each other,
children running to school, shopkeepers waving.

[bold cyan]"Beyond family, we have friends, classmates, teachers, neighbors,"[/bold cyan]
龙龙 said. [bold cyan]"And in Chinese culture, how you ADDRESS people matters
enormously. You don't call your friend's mother by her first name —
you call her 阿姨 (auntie). Respect is built into the language."[/bold cyan]

[bold yellow]朋友 · 同学 · 老师 · 邻居[/bold yellow]

[bold white]Let's learn the words that connect us to the world![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "immediate_family": """
[bold green]You know your closest family in Chinese![/bold green]

爸爸, 妈妈, 哥哥, 姐姐, 弟弟, 妹妹 — all six glow warmly.

[bold cyan]"You've learned something special,"[/bold cyan] 龙龙 says.
[bold cyan]"Chinese doesn't just say 'brother' — it tells you if they're
older or younger. The language carries respect for age
built right into the words."[/bold cyan]

The extended family tree unfurls. There are more relatives to meet...
""",
    "extended_family": """
[bold green]The family tree is complete — both sides![/bold green]

Paternal grandparents, maternal grandparents, uncles, aunties —
every branch of the family tree glows with life.

[bold cyan]"You now know more family vocabulary than most Chinese textbooks
teach in an entire semester,"[/bold cyan] 龙龙 says proudly.
[bold cyan]"Chinese family terms are the most specific in the world.
You should be proud!"[/bold cyan]

An ink brush appears. It's time to describe the people you know...
""",
    "describing_people": """
[bold green]You can paint people with Chinese words![/bold green]

Tall, short, thin, round, beautiful, handsome — the pairs
of opposites glow side by side.

[bold cyan]"Opposites help you remember,"[/bold cyan] 龙龙 says.
[bold cyan]"高 and 矮, 胖 and 瘦. Learn them as pairs
and they'll stick forever."[/bold cyan]

Birthday candles appear. It's time to talk about ages...
""",
    "ages_birthdays": """
[bold green]Ages, birthdays, and the zodiac — all yours![/bold green]

Twelve zodiac animals circle overhead in golden light.

[bold cyan]"You know how to ask someone's age, wish them happy birthday,
and talk about the zodiac,"[/bold cyan] 龙龙 says.
[bold cyan]"Every Chinese person knows their zodiac animal.
Now you can ask them about it — in Chinese!"[/bold cyan]

A door opens to a Chinese house. Let's explore the rooms inside...
""",
    "my_house": """
[bold green]Every room of the house glows with warmth![/bold green]

卧室, 厨房, 客厅, 卫生间 — you know them all.

[bold cyan]"家,"[/bold cyan] 龙龙 says softly. [bold cyan]"A pig under a roof.
It's the most beautiful character in Chinese, because it means
the place where everyone you love gathers together."[/bold cyan]

Paws and feathers appear. The animals are waiting...
""",
    "pets_animals": """
[bold green]You've met all the animals![/bold green]

Cats meow, dogs bark, fish swim, birds sing, rabbits hop —
each with their Chinese name glowing beside them.

[bold cyan]"And you learned measure words too!"[/bold cyan] 龙龙 says.
[bold cyan]"一只猫, 一条鱼 — every noun needs the right counter.
That's a skill that impresses native speakers!"[/bold cyan]

The neighborhood bustles. It's time to meet the people around us...
""",
    "relationships": """
[bold green]Friends, classmates, teachers, neighbors — all connected![/bold green]

A web of relationships glows warmly, with each word at a node.

[bold cyan]"You've learned more than vocabulary,"[/bold cyan] 龙龙 says.
[bold cyan]"You've learned about Chinese culture itself — how respect
is woven into every greeting, every title, every word you use
to address the people around you."[/bold cyan]

[bold white]Family master. Relationship builder. Culture learner.
That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "immediate_family": "龙龙 draws all six family members in the air. [bold yellow]\"Quick — which word means 'younger sister'? Don't mix up the older and younger ones!\"[/bold yellow]",
    "extended_family": "龙龙 points to a confusing family tree. [bold yellow]\"This is the trickiest part of Chinese! Can you tell your 阿姨 from your 叔叔?\"[/bold yellow]",
    "describing_people": "龙龙 strikes a pose. [bold yellow]\"Am I 帅 or 漂亮? Choose your words carefully — they mean different things!\"[/bold yellow]",
    "ages_birthdays": "龙龙 holds up a birthday card. [bold yellow]\"Can you say your age in Chinese? Remember — no verb needed!\"[/bold yellow]",
    "my_house": "龙龙 stands at the front door. [bold yellow]\"家 — one of the most beautiful characters in Chinese. Do you know what it's made of?\"[/bold yellow]",
    "pets_animals": "龙龙 holds up three fingers. [bold yellow]\"一只猫, 一条鱼, 一头牛 — different animals need different measure words! Which one goes with most pets?\"[/bold yellow]",
    "relationships": "龙龙 stands with a group of adults. [bold yellow]\"How do you politely greet your friend's mother in Chinese? Remember — names are rude!\"[/bold yellow]",
}
