"""
story.py — Narrative for the Hobbies & Free Time skill pack.

龙龙 (Lóng Lóng) guides the learner through Chinese hobby vocabulary —
sports, music & art, reading & media, outdoor activities,
and talking about hobbies.
"""

INTRO_STORY = """
[bold yellow]LEARN CHINESE[/bold yellow]
[bold yellow]Chapter: Hobbies & Free Time — 爱好与休闲[/bold yellow]

龙龙 glided over the castle battlements and landed beside a great
notice board covered in colorful posters — each one depicting a
different hobby. Knights jousted, bards strummed lutes, scholars
read beneath ancient oaks, and travelers pointed toward distant peaks.

[bold cyan]"Welcome to the Hall of Pastimes,"[/bold cyan] 龙龙 said,
tapping a claw on the board. [bold cyan]"In Chinese, hobbies are called
爱好 — literally 'love-good.' And talking about what you love to do
is one of the most important skills in any language."[/bold cyan]

The dragon swept a wing across the posters.

[bold cyan]"We'll explore five realms of free time: the sports arena,
the bard's tower of music and art, the scribe's library of books
and media, the wilds beyond the wall, and finally — the council
chamber where you'll learn to talk about all of it."[/bold cyan]

龙龙 grinned, a wisp of smoke curling from its nostrils.

[bold cyan]"So — 你的爱好是什么? Let's find out!"[/bold cyan]

[bold white]Your journey through Chinese hobbies begins now.[/bold white]
"""

ZONE_INTROS = {
    "sports_exercise": """
龙龙 led you through an iron gate into a roaring arena. Knights
sparred, archers loosed arrows, and squires raced around the track.

[bold cyan]"Every kingdom needs strong warriors,"[/bold cyan] 龙龙 said,
flexing a wing. [bold cyan]"打篮球, 踢足球, 跑步, 游泳, 骑自行车 —
basketball, soccer, running, swimming, cycling. Five sports, five
ways to stay strong."[/bold cyan]

Banners bearing each sport's characters fluttered in the wind:
[bold yellow]打篮球 · 踢足球 · 跑步 · 游泳 · 骑自行车[/bold yellow]

[bold white]Let's train![/bold white]
""",
    "music_art": """
龙龙 pushed open a heavy oak door and led you up a spiral staircase
into the Bard's Tower. Melodies drifted from every window, and
canvases lined the walls.

[bold cyan]"Not all power comes from the sword,"[/bold cyan] 龙龙 said
softly. [bold cyan]"听音乐, 弹钢琴, 唱歌, 画画, 跳舞 — listening to
music, playing piano, singing, drawing, dancing. The creative arts
feed the soul."[/bold cyan]

Instruments and paintbrushes glowed with golden light:
[bold yellow]听音乐 · 弹钢琴 · 唱歌 · 画画 · 跳舞[/bold yellow]

[bold white]Let's create![/bold white]
""",
    "reading_media": """
龙龙 ushered you into a vast library. Enchanted books floated
between shelves, crystal screens flickered with moving images,
and a great chess board sat in the corner.

[bold cyan]"Knowledge is the greatest treasure,"[/bold cyan] 龙龙 said,
settling among the shelves. [bold cyan]"看书, 看电影, 玩游戏, 上网,
拍照 — reading, watching movies, playing games, going online,
taking photos. The modern scribe has many tools."[/bold cyan]

Glowing titles appeared on the spines of floating books:
[bold yellow]看书 · 看电影 · 玩游戏 · 上网 · 拍照[/bold yellow]

[bold white]Let's explore![/bold white]
""",
    "outdoor_activities": """
龙龙 took flight and carried you beyond the castle walls. Below,
rolling hills, sparkling rivers, and misty mountain peaks stretched
to the horizon.

[bold cyan]"The greatest adventures await outside,"[/bold cyan] 龙龙 called
over the wind. [bold cyan]"爬山, 钓鱼, 散步, 旅游, 野餐 — hiking,
fishing, walking, traveling, picnicking. Nature is the grandest
classroom of all."[/bold cyan]

Trail markers appeared along the path, each bearing characters:
[bold yellow]爬山 · 钓鱼 · 散步 · 旅游 · 野餐[/bold yellow]

[bold white]Let's venture forth![/bold white]
""",
    "talking_about_hobbies": """
龙龙 led you into a grand council chamber. A round table stood at
the center, surrounded by chairs — each engraved with a hobby's
Chinese characters.

[bold cyan]"You know the words. Now learn to wield them,"[/bold cyan]
龙龙 said, taking a seat. [bold cyan]"你的爱好是什么? 我喜欢...
我不太喜欢... 因为... — asking about hobbies, expressing likes and
dislikes, giving reasons. This is where vocabulary becomes
conversation."[/bold cyan]

Speech bubbles floated around the chamber:
[bold yellow]爱好 · 喜欢 · 不太喜欢 · 最喜欢 · 因为[/bold yellow]

[bold white]Let's talk![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "sports_exercise": """
[bold green]All five sports — conquered in the arena![/bold green]

打篮球, 踢足球, 跑步, 游泳, 骑自行车 — your athletic vocabulary is set.

[bold cyan]"You mastered the 打 vs. 踢 pattern,"[/bold cyan] 龙龙 says.
[bold cyan]"打 for hand sports, 踢 for foot sports. That one rule
unlocks every sport in Chinese!"[/bold cyan]

The arena gates swing open. The Bard's Tower awaits...
""",
    "music_art": """
[bold green]The Bard's Tower — all arts mastered![/bold green]

听音乐, 弹钢琴, 唱歌, 画画, 跳舞 — five creative pursuits, all yours.

[bold cyan]"You discovered the 琴 pattern,"[/bold cyan] 龙龙 says.
[bold cyan]"钢琴, 小提琴, 大提琴 — one character that marks every
stringed instrument. Patterns are power!"[/bold cyan]

A hidden door opens in the tower wall. The library beckons...
""",
    "reading_media": """
[bold green]The Scribe's Library — fully catalogued![/bold green]

看书, 看电影, 玩游戏, 上网, 拍照 — the modern world at your fingertips.

[bold cyan]"You found the 看 pattern,"[/bold cyan] 龙龙 says.
[bold cyan]"看书, 看电影, 看电视, 看病 — one verb for reading,
watching, and seeing. Chinese efficiency at its finest!"[/bold cyan]

The library doors open onto daylight. The wilds await...
""",
    "outdoor_activities": """
[bold green]The wilds beyond the wall — fully explored![/bold green]

爬山, 钓鱼, 散步, 旅游, 野餐 — you know every outdoor adventure.

[bold cyan]"You learned the 步 pattern,"[/bold cyan] 龙龙 says.
[bold cyan]"跑步, 散步, 进步, 脚步 — one character for every kind
of step. And the 吧 suggestion pattern to invite friends along!"[/bold cyan]

The path leads back to the castle. One final challenge remains...
""",
    "talking_about_hobbies": """
[bold green]The Council of Interests — you can speak your passions![/bold green]

爱好, 喜欢, 不太喜欢, 最喜欢, 因为 — full conversational mastery.

[bold cyan]"You can now say 我的爱好是听音乐，因为很放松,"[/bold cyan]
龙龙 says. [bold cyan]"That's not just vocabulary — that's a real
conversation. You're expressing yourself in Chinese!"[/bold cyan]

[bold white]Hobby master. Sports champion. Art connoisseur. Adventurer.
Conversationalist. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "sports_exercise": "龙龙 raises a champion's banner. [bold yellow]\"打篮球, 踢足球, 跑步, 游泳, 骑自行车 — can you match them all?\"[/bold yellow]",
    "music_art": "龙龙 conducts an invisible orchestra. [bold yellow]\"听音乐, 弹钢琴, 唱歌, 画画, 跳舞 — name every art!\"[/bold yellow]",
    "reading_media": "龙龙 stamps a golden seal. [bold yellow]\"看书, 看电影, 玩游戏, 上网, 拍照 — prove your knowledge of the modern world!\"[/bold yellow]",
    "outdoor_activities": "龙龙 roars from a hilltop. [bold yellow]\"爬山, 钓鱼, 散步, 旅游, 野餐 — the wilds test you one last time!\"[/bold yellow]",
    "talking_about_hobbies": "龙龙 leans forward at the council table. [bold yellow]\"我的爱好是听音乐，因为很放松 — can you build a perfect hobby sentence?\"[/bold yellow]",
}
