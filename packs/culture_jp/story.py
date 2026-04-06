"""
story.py — Narrative for the Japanese Culture skill pack.
"""

INTRO_STORY = """
[bold yellow]LEARN JAPANESE[/bold yellow]
[bold yellow]Chapter: 日本文化 — Japanese Culture[/bold yellow]

Sensei knelt beside a low table, a steaming cup of matcha before them.

[bold cyan]"Culture,"[/bold cyan] Sensei said softly, [bold cyan]"is not just facts.
It is the reason behind the bow. The meaning in the silence.
The beauty in the changing leaves."[/bold cyan]

A scroll unfurled, showing festivals, temples, and gardens.

[bold cyan]"Japan has preserved traditions for thousands of years —
and yet embraces the future at the same time.
Let me show you both."[/bold cyan]

[bold white]Your cultural journey begins now.[/bold white]
"""

ZONE_INTROS = {
    "festivals": """
Sensei opened a colorful calendar filled with celebrations.

[bold cyan]"Japan celebrates life all year round. Each festival — or matsuri —
has deep meaning, from honoring ancestors to welcoming spring."[/bold cyan]

[bold white]Let's explore Japan's most beloved festivals![/bold white]
""",
    "martial_arts": """
Sensei stood and bowed toward a wooden practice sword on the wall.

[bold cyan]"The martial arts of Japan are not just about fighting.
They are about discipline, respect, and mastering yourself."[/bold cyan]

[bold white]Let's explore the way of the warrior![/bold white]
""",
    "tea_ceremony": """
Sensei carefully placed a bamboo whisk beside the matcha bowl.

[bold cyan]"The tea ceremony — sadō — is meditation in motion.
Every movement has meaning. Every pause is intentional."[/bold cyan]

[bold white]Let's discover the art of tea![/bold white]
""",
    "anime_manga": """
Sensei smiled and held up a colorful manga volume.

[bold cyan]"Anime and manga are Japan's gift to storytelling.
From Studio Ghibli to shōnen adventures — they shape
how the world sees Japan today."[/bold cyan]

[bold white]Let's dive into the world of anime and manga![/bold white]
""",
    "seasons": """
A window opened to reveal cherry blossoms drifting in the wind.

[bold cyan]"Japan lives by its seasons more than almost any culture.
Each season has its own foods, festivals, colors, and feelings."[/bold cyan]

[bold white]Let's experience the beauty of Japan's four seasons![/bold white]
""",
    "etiquette": """
Sensei bowed deeply, then looked up with kind eyes.

[bold cyan]"In Japan, manners are a form of respect.
The way you bow, remove your shoes, use chopsticks —
these small things speak louder than words."[/bold cyan]

[bold white]Let's learn the art of Japanese etiquette![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "festivals": "[bold green]You know Japan's greatest celebrations![/bold green]\nFrom hanami to Obon, you understand how Japan honors tradition.",
    "martial_arts": "[bold green]You've walked the way of the warrior![/bold green]\nJudo, karate, kendo, aikido — the spirit of bushido lives in you.",
    "tea_ceremony": "[bold green]The tea ceremony is yours to appreciate![/bold green]\nWabi-sabi, ichigo ichie — you understand the beauty of simplicity.",
    "anime_manga": "[bold green]You're an anime and manga scholar![/bold green]\nFrom Miyazaki to One Piece, you know the art form that captivates billions.",
    "seasons": "[bold green]You've experienced all four seasons![/bold green]\nCherry blossoms, summer festivals, autumn leaves, winter snow — each one precious.",
    "etiquette": "[bold green]You are a master of Japanese etiquette![/bold green]\nYour bows are deep, your chopsticks are proper, and your shoes are at the door.",
}

BOSS_INTROS = {
    "festivals": "Sensei asks: [bold yellow]\"One festival involves writing wishes on paper strips and hanging them on bamboo. Which one is it?\"[/bold yellow]",
    "martial_arts": "Sensei asks: [bold yellow]\"Which martial art was created by Jigoro Kano and became an Olympic sport?\"[/bold yellow]",
    "tea_ceremony": "Sensei asks: [bold yellow]\"What is the Japanese aesthetic concept that finds beauty in imperfection?\"[/bold yellow]",
    "anime_manga": "Sensei asks: [bold yellow]\"Which Studio Ghibli film won the Academy Award for Best Animated Feature?\"[/bold yellow]",
    "seasons": "Sensei asks: [bold yellow]\"What is the Japanese practice of viewing autumn leaves called?\"[/bold yellow]",
    "etiquette": "Sensei asks: [bold yellow]\"In Japan, what should you NEVER do with chopsticks because it resembles a funeral ritual?\"[/bold yellow]",
}
