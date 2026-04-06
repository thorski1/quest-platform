"""
story.py — Narrative for the Culture skill pack.

龙龙 (Lóng Lóng) guides the learner through the rich tapestry of Chinese
culture — festivals, zodiac, calligraphy, tea, martial arts, modern tech,
and the wisdom of four-character idioms.
"""

INTRO_STORY = """
[bold yellow]LEARN CHINESE[/bold yellow]
[bold yellow]Chapter: Culture — 中国文化[/bold yellow]

龙龙 descended from the clouds not with a textbook, but with something
better — a scroll that seemed to contain all of China's 5,000-year history.
As it unrolled, images came to life: fireworks over the Great Wall, monks
practicing tai chi at dawn, ink flowing from a calligraphy brush, steam
rising from a tea ceremony.

[bold cyan]"Language is the key,"[/bold cyan] 龙龙 said, [bold cyan]"but culture is
the door. You can know every word in Chinese and still not understand
China — unless you know its festivals, its zodiac, its calligraphy,
its tea, its martial arts, its technology, and its wisdom."[/bold cyan]

The dragon spread its wings wide, and the scroll kept unrolling.

[bold cyan]"This is the heart of China. Not just words — but the stories,
traditions, and ideas that give those words their meaning.
Spring Festival fireworks, zodiac animals, the brush and ink,
the art of tea, the philosophy of kung fu, the digital revolution,
and the four-character wisdom that Chinese people have used
for thousands of years."[/bold cyan]

龙龙 rolled up the scroll and tucked it under one wing.

[bold cyan]"Ready to go deeper than vocabulary? Let's explore Chinese culture."[/bold cyan]

[bold white]Your cultural journey begins now.[/bold white]
"""

ZONE_INTROS = {
    "chinese_festivals": """
龙龙 burst through a shower of red and gold fireworks.

[bold cyan]"春节! 中秋节! 端午节! 元宵节!"[/bold cyan] 龙龙 shouted.
[bold cyan]"Chinese festivals are spectacular — fireworks, dragon dances,
mooncakes, dragon boat races, lanterns! Each one has its own food,
its own traditions, and its own story stretching back centuries."[/bold cyan]

[bold yellow]春节 · 中秋节 · 端午节 · 元宵节[/bold yellow]

[bold white]Let's celebrate![/bold white]
""",
    "zodiac": """
龙龙 summoned twelve golden animal spirits that circled overhead.

[bold cyan]"The Chinese zodiac — 十二生肖 — twelve animals, twelve years,
one great cycle,"[/bold cyan] 龙龙 said. [bold cyan]"Every Chinese person
knows their zodiac animal. It shapes their identity, their
compatibility, even what underwear they wear in certain years!"[/bold cyan]

[bold yellow]鼠 · 牛 · 虎 · 兔 · 龙 · 蛇 · 马 · 羊 · 猴 · 鸡 · 狗 · 猪[/bold yellow]

[bold white]Let's meet the twelve animals![/bold white]
""",
    "calligraphy": """
龙龙 laid out brush, ink, paper, and inkstone with reverent care.

[bold cyan]"书法 — calligraphy — is not just writing,"[/bold cyan] 龙龙 said softly.
[bold cyan]"It is art. Philosophy. Meditation. Every stroke has a name,
every character has a structure, and the same word written by
two different people tells two completely different stories."[/bold cyan]

[bold yellow]笔 · 墨 · 纸 · 砚 — 文房四宝[/bold yellow]

[bold white]Let's pick up the brush![/bold white]
""",
    "tea_culture": """
龙龙 carefully poured water into a small clay teapot, steam rising gently.

[bold cyan]"China invented tea,"[/bold cyan] 龙龙 said. [bold cyan]"And from China,
it traveled to every corner of the world — by land as 'cha,'
by sea as 'te.' Six types of tea, a ceremony with finger-tapping
thanks, and a philosophy that says: slow down, pay attention,
and share a cup with someone."[/bold cyan]

[bold yellow]茶 · 绿茶 · 红茶 · 功夫茶[/bold yellow]

[bold white]Let's have some tea![/bold white]
""",
    "martial_arts": """
龙龙 landed in the courtyard of an ancient temple, mist swirling.

[bold cyan]"功夫 — kung fu — is more than fighting,"[/bold cyan] 龙龙 said.
[bold cyan]"It's a philosophy. 以柔克刚 — softness overcomes hardness.
From the Shaolin Temple to the flowing movements of tai chi,
Chinese martial arts are about discipline, patience, and
understanding yourself as much as your opponent."[/bold cyan]

[bold yellow]功夫 · 太极 · 少林 · 武侠[/bold yellow]

[bold white]Let's train![/bold white]
""",
    "modern_china": """
龙龙 held up a smartphone, its screen glowing with QR codes.

[bold cyan]"Modern China is a tech wonderland,"[/bold cyan] 龙龙 said.
[bold cyan]"WeChat does everything. Alipay made cash obsolete.
High-speed trains connect the whole country. TikTok was born here.
And on Double Eleven, China does more online shopping in one day
than most countries do in a month."[/bold cyan]

[bold yellow]微信 · 支付宝 · 高铁 · 抖音 · 二维码[/bold yellow]

[bold white]Let's explore digital China![/bold white]
""",
    "idioms_chengyu": """
龙龙 unrolled a scroll covered in four-character phrases.

[bold cyan]"成语 — chéngyǔ — are China's greatest linguistic treasure,"[/bold cyan]
龙龙 said. [bold cyan]"Four characters. One story. Thousands of years old.
A snake with feet, a lute played to a cow, a frog in a well.
Each one is a tiny story with a huge lesson."[/bold cyan]

[bold yellow]画蛇添足 · 对牛弹琴 · 井底之蛙 · 铁杵磨成针[/bold yellow]

[bold white]Let's unlock the wisdom of the ancients![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "chinese_festivals": """
[bold green]All four great festivals — celebrated![/bold green]

春节, 中秋节, 端午节, 元宵节 — each with their own food,
traditions, and stories.

[bold cyan]"恭喜发财!"[/bold cyan] 龙龙 says, handing you a red envelope.
[bold cyan]"You can now join any Chinese celebration and know
what's happening and why!"[/bold cyan]

The zodiac animals gather. It's time to meet them all...
""",
    "zodiac": """
[bold green]All twelve zodiac animals — mastered![/bold green]

Rat to Pig, personality traits, compatibility, and the 本命年 tradition.

[bold cyan]"You know the zodiac inside and out,"[/bold cyan] 龙龙 says.
[bold cyan]"Ask any Chinese person their zodiac animal —
it's a guaranteed conversation starter!"[/bold cyan]

Brush and ink await. Calligraphy is next...
""",
    "calligraphy": """
[bold green]The art of Chinese writing — explored![/bold green]

Brush, ink, paper, inkstone. Eight strokes. Five scripts. Radicals.

[bold cyan]"You understand the architecture of Chinese characters now,"[/bold cyan]
龙龙 says. [bold cyan]"Radicals, strokes, structure — these aren't just
calligraphy terms. They're the key to reading ANY Chinese character."[/bold cyan]

The water begins to boil. Tea is waiting...
""",
    "tea_culture": """
[bold green]Tea master — steeped in knowledge![/bold green]

Six tea types, the finger-tapping thanks, gongfu tea, and
China's gift of 'cha' and 'te' to the world.

[bold cyan]"Next time you drink tea,"[/bold cyan] 龙龙 says,
[bold cyan]"remember: you're drinking 5,000 years of Chinese culture.
And now you can discuss it — in Chinese!"[/bold cyan]

The temple courtyard beckons. Martial arts await...
""",
    "martial_arts": """
[bold green]The way of the warrior — understood![/bold green]

Kung fu, tai chi, Shaolin, and the philosophy of softness over hardness.

[bold cyan]"功夫 isn't just fighting — it's any skill mastered through effort,"[/bold cyan]
龙龙 says. [bold cyan]"Your Chinese learning is its own kind of 功夫.
Keep going!"[/bold cyan]

The digital world awaits. Modern China is next...
""",
    "modern_china": """
[bold green]Digital China — decoded![/bold green]

WeChat, Alipay, high-speed rail, TikTok, QR codes — all demystified.

[bold cyan]"China's tech landscape is reshaping the world,"[/bold cyan]
龙龙 says. [bold cyan]"Knowing these words and concepts isn't just
language learning — it's understanding the future."[/bold cyan]

One final challenge remains — the ancient wisdom of 成语...
""",
    "idioms_chengyu": """
[bold green]Four-character wisdom — unlocked![/bold green]

画蛇添足, 对牛弹琴, 井底之蛙, 铁杵磨成针 — each one a tiny
story with an eternal lesson.

[bold cyan]"You've reached the pinnacle,"[/bold cyan] 龙龙 says, eyes bright.
[bold cyan]"Using 成语 in context is what separates a language learner
from a true Chinese speaker. You did it."[/bold cyan]

[bold white]Culture keeper. Wisdom seeker. Four-character philosopher.
That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "chinese_festivals": "龙龙 holds up a red envelope. [bold yellow]\"恭喜发财! Can you tell me what this famous greeting really means?\"[/bold yellow]",
    "zodiac": "龙龙 and a rat stand side by side. [bold yellow]\"Which zodiac animal is the Dragon's best match? Choose wisely!\"[/bold yellow]",
    "calligraphy": "龙龙 writes the same character five times. [bold yellow]\"Five scripts, five styles. Can you name the wildest, most cursive one?\"[/bold yellow]",
    "tea_culture": "龙龙 lists seven items on a scroll. [bold yellow]\"柴米油盐酱醋茶 — tea is one of the seven necessities. What are the other six?\"[/bold yellow]",
    "martial_arts": "龙龙 draws a sword. [bold yellow]\"武侠 — the genre of martial heroes. Can you tell me what it means?\"[/bold yellow]",
    "modern_china": "龙龙 projects a QR code. [bold yellow]\"二维码 — scan me! In modern China, QR codes are used for EVERYTHING. Can you name what they cover?\"[/bold yellow]",
    "idioms_chengyu": "龙龙 describes a situation. [bold yellow]\"Your friend ruined a perfect cake by adding too much. Which 成语 fits?\"[/bold yellow]",
}
