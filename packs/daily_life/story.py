"""
story.py — Narrative for the Daily Life skill pack.

龙龙 (Lóng Lóng) guides the learner through everyday Chinese vocabulary —
morning routines, school and work, hobbies, weather, shopping, colors,
and body parts.
"""

INTRO_STORY = """
[bold yellow]LEARN CHINESE[/bold yellow]
[bold yellow]Chapter: Daily Life — 日常生活[/bold yellow]

龙龙 swooped down from the clouds and landed in the middle of
a bustling Chinese city street. Morning light flooded the scene —
people brushing their teeth in doorways, students rushing to school,
shopkeepers opening their stores, steam rising from breakfast stalls.

[bold cyan]"This,"[/bold cyan] 龙龙 said, spreading its wings wide,
[bold cyan]"is everyday life in China — 日常生活 (rìcháng shēnghuó).
The words you'll learn here are the ones people use every single
day, from the moment they wake up to the moment they go to sleep."[/bold cyan]

The dragon pointed a claw at the busy scene.

[bold cyan]"Morning routines. School and work. Hobbies. Weather.
Shopping. Colors. Even the names of your own body parts.
These aren't textbook words — these are LIFE words."[/bold cyan]

龙龙 grinned.

[bold cyan]"Ready to live a day in Chinese?"[/bold cyan]

[bold white]Your journey through daily Chinese life begins now.[/bold white]
"""

ZONE_INTROS = {
    "morning_routine": """
龙龙 appeared at the crack of dawn, hovering beside an alarm clock.

[bold cyan]"Every day starts the same way,"[/bold cyan] 龙龙 said with a yawn.
[bold cyan]"起床, 刷牙, 洗脸, 吃早饭, 出门 — get up, brush teeth,
wash face, eat breakfast, head out. These five words are the
rhythm of every Chinese morning."[/bold cyan]

The alarm rang:
[bold yellow]起床 · 刷牙 · 洗脸 · 吃早饭 · 出门[/bold yellow]

[bold white]Let's start the day![/bold white]
""",
    "school_work": """
龙龙 flew over a school and an office building side by side.

[bold cyan]"学校 and 上班,"[/bold cyan] 龙龙 said.
[bold cyan]"Whether you're a student doing 作业 or a worker facing 考试,
these words shape how Chinese people spend most of their waking hours.
And wait till you hear about '996'..."[/bold cyan]

[bold yellow]学校 · 上班 · 下班 · 作业 · 考试[/bold yellow]

[bold white]Let's learn about school and work life![/bold white]
""",
    "hobbies": """
龙龙 landed in a park where people were reading, exercising, painting,
and playing games — all at once.

[bold cyan]"After work comes play!"[/bold cyan] 龙龙 said happily.
[bold cyan]"看书, 听音乐, 运动, 画画, 玩游戏 — reading, music,
sports, drawing, gaming. What are YOUR hobbies? After this zone,
you'll be able to say them in Chinese!"[/bold cyan]

[bold yellow]看书 · 听音乐 · 运动 · 画画 · 游戏[/bold yellow]

[bold white]Let's talk about fun![/bold white]
""",
    "weather": """
龙龙 looked up at a sky that was half sunny, half stormy.

[bold cyan]"天气怎么样?"[/bold cyan] 龙龙 asked.
[bold cyan]"Weather talk is universal — every culture does it.
But Chinese weather words are built from beautiful radicals:
雨 (rain) sits inside snow, thunder, frost, and fog.
One radical unlocks a whole family of words!"[/bold cyan]

[bold yellow]天气 · 热 · 冷 · 下雨 · 下雪 · 晴天[/bold yellow]

[bold white]Let's check the forecast![/bold white]
""",
    "shopping": """
龙龙 stood at the entrance of a busy Chinese market, its eyes wide.

[bold cyan]"Shopping in China is an art!"[/bold cyan] 龙龙 declared.
[bold cyan]"You need to know 贵 and 便宜, you need to understand
Chinese discounts (they work differently!), and you need one
essential phrase: 多少钱?"[/bold cyan]

[bold yellow]买东西 · 商店 · 超市 · 贵/便宜 · 打折[/bold yellow]

[bold white]Let's go shopping![/bold white]
""",
    "colors": """
龙龙 conjured a rainbow of Chinese characters in the air.

[bold cyan]"Colors in Chinese aren't just pretty words,"[/bold cyan] 龙龙 said.
[bold cyan]"They carry deep cultural meaning. Red is lucky.
Yellow is imperial. White is for mourning. Green hats are...
well, you'll find out!"[/bold cyan]

[bold yellow]红 · 蓝 · 绿 · 黄 · 白 · 黑 · 粉红[/bold yellow]

[bold white]Let's paint the world with Chinese colors![/bold white]
""",
    "body_parts": """
龙龙 pointed to its own head, hands, feet, eyes, mouth, and ears.

[bold cyan]"Your body, in Chinese!"[/bold cyan] 龙龙 said.
[bold cyan]"And here's the secret: body part radicals appear EVERYWHERE
in Chinese. The mouth radical 口 is in 'eat,' 'drink,' and 'sing.'
The eye radical 目 is in 'look' and 'sleep.' Learn the body,
and hundreds of other characters start making sense!"[/bold cyan]

[bold yellow]头 · 手 · 脚 · 眼睛 · 嘴巴 · 耳朵[/bold yellow]

[bold white]Let's learn the body![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "morning_routine": """
[bold green]Your morning routine is complete — in Chinese![/bold green]

起床 → 刷牙 → 洗脸 → 吃早饭 → 出门. A perfect morning.

[bold cyan]"You can now narrate your entire morning in Chinese,"[/bold cyan]
龙龙 says. [bold cyan]"Try it tomorrow when you wake up — say
each step out loud. That's how words become habits!"[/bold cyan]

The school bell rings. Time for the next zone...
""",
    "school_work": """
[bold green]School and work vocabulary — mastered![/bold green]

学校, 上班, 下班, 作业, 考试 — the daily grind, in Chinese.

[bold cyan]"You learned the 上/下 pattern too,"[/bold cyan] 龙龙 says.
[bold cyan]"上班/下班, 上课/下课, 上车/下车 — one pattern,
endless uses. That's the beauty of Chinese!"[/bold cyan]

Free time awaits. Let's talk about hobbies...
""",
    "hobbies": """
[bold green]Hobbies unlocked — in Chinese![/bold green]

Reading, music, sports, drawing, gaming — you can talk about them all.

[bold cyan]"Now you can answer the question: 你的爱好是什么?"[/bold cyan]
龙龙 says. [bold cyan]"Hobbies are the best conversation starter
in any language!"[/bold cyan]

Clouds gather overhead. Let's check the weather...
""",
    "weather": """
[bold green]You're a weather reporter — in Chinese![/bold green]

Hot, cold, rain, snow, sunny — the forecast is yours.

[bold cyan]"You discovered the 雨 radical family,"[/bold cyan] 龙龙 says.
[bold cyan]"One radical, many weather words. Chinese characters
are like building blocks — once you know the pieces,
you can decode new words on sight!"[/bold cyan]

The shops are open. Time to go shopping...
""",
    "shopping": """
[bold green]Shopping master — bargaining ready![/bold green]

买, 卖, 贵, 便宜, 打折, 多少钱 — all yours.

[bold cyan]"You know the Chinese discount system now,"[/bold cyan] 龙龙 says.
[bold cyan]"八折 = pay 80%. 五折 = half price. Armed with this
knowledge, you'll never overpay!"[/bold cyan]

A rainbow appears. Let's explore colors...
""",
    "colors": """
[bold green]The rainbow is complete — every color named![/bold green]

Red, blue, green, yellow, white, black, pink — each with its story.

[bold cyan]"Colors in Chinese carry centuries of meaning,"[/bold cyan]
龙龙 says. [bold cyan]"Red for luck, yellow for royalty,
white for mourning. Now you see China through its colors!"[/bold cyan]

One last zone remains — your own body, in Chinese...
""",
    "body_parts": """
[bold green]Head to toe — you know every body part in Chinese![/bold green]

头, 手, 脚, 眼睛, 嘴巴, 耳朵 — and their radicals unlock
hundreds more characters.

[bold cyan]"This is the real power,"[/bold cyan] 龙龙 says.
[bold cyan]"Body radicals appear in countless characters.
目 is in 'look,' 口 is in 'eat,' 耳 is in 'smart.'
You've learned words AND the system behind them."[/bold cyan]

[bold white]Daily life master. Routine expert. Color connoisseur.
That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "morning_routine": "龙龙 scrambles the morning routine. [bold yellow]\"Can you put it back in the right order? 起床 first, 出门 last — but what goes in between?\"[/bold yellow]",
    "school_work": "龙龙 holds up a newspaper article about '996.' [bold yellow]\"This number shook all of China. Do you know what it means?\"[/bold yellow]",
    "hobbies": "龙龙 pulls out a microphone. [bold yellow]\"你的爱好是什么? Can you ask this question in Chinese?\"[/bold yellow]",
    "weather": "龙龙 stands in bright sunshine. [bold yellow]\"晴天 or 阴天? Make sure you know your weather words!\"[/bold yellow]",
    "shopping": "龙龙 points to a '多少钱' sign. [bold yellow]\"The most important shopping phrase! And can you decode Chinese discounts?\"[/bold yellow]",
    "colors": "龙龙 blows seven colored smoke rings. [bold yellow]\"Colors carry meaning! Do you know which color means 'mourning' in China?\"[/bold yellow]",
    "body_parts": "龙龙 points to its ears. [bold yellow]\"耳 appears inside 聪明 — 'smart.' Why? Because listening is the root of wisdom!\"[/bold yellow]",
}
