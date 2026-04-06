"""
story.py — Narrative for the Hiragana skill pack.

Sensei (先生) guides you through the 46 basic hiragana characters,
the foundation of all Japanese writing.
"""

INTRO_STORY = """
[bold red]LEARN JAPANESE[/bold red]
[bold yellow]Chapter: The Foundation of Japanese[/bold yellow]

You slid open a paper screen door and stepped into a quiet room
overlooking a Japanese garden. Cherry blossom petals drifted
across a still pond. At a low wooden desk sat an older figure
in a simple kimono, brush in hand, writing graceful curved
characters on rice paper.

[bold cyan]"Welcome,"[/bold cyan] the figure said without looking up.
[bold cyan]"I am your Sensei. Please, sit."[/bold cyan]

Sensei set down the brush and turned the paper toward you.
Five characters glowed softly: [bold yellow]あ い う え お[/bold yellow]

[bold cyan]"These are the five vowels of Japanese -- the very first
sounds you will learn. Japanese has 46 basic characters
called hiragana. Each one represents a single sound.
Unlike English, where letters can make many sounds,
each hiragana always sounds exactly the same."[/bold cyan]

Sensei smiled gently.

[bold cyan]"Master hiragana, and you hold the key to reading
any Japanese word. Shall we begin?"[/bold cyan]

[bold white]Your journey into the characters of Japanese begins now.[/bold white]
"""

ZONE_INTROS = {
    "vowels": """
Sensei placed five characters in a neat row on the desk.

[bold cyan]"Every sound in Japanese is built on five vowels,"[/bold cyan] Sensei explained.
[bold cyan]"あ (a) — like 'ah' at the dentist.
い (i) — like 'ee' in 'see'.
う (u) — like 'oo' in 'food'.
え (e) — like 'e' in 'pet'.
お (o) — like 'o' in 'go'."[/bold cyan]

[bold white]Let's master the five vowels of Japanese![/bold white]
""",
    "ka_row": """
Sensei added a new column of characters beside the vowels.

[bold cyan]"Now we add the 'k' sound to each vowel,"[/bold cyan] Sensei said.
[bold cyan]"か (ka), き (ki), く (ku), け (ke), こ (ko).
This is the ka-row. See the pattern? One consonant
combined with each of the five vowels."[/bold cyan]

[bold white]Let's learn the ka-row![/bold white]
""",
    "sa_row": """
Sensei dipped the brush in fresh ink.

[bold cyan]"The sa-row follows the same pattern,"[/bold cyan] Sensei continued.
[bold cyan]"さ (sa), し (shi), す (su), せ (se), そ (so).
Notice し is 'shi', not 'si' -- this is one of the
special readings you must remember."[/bold cyan]

[bold white]Let's learn the sa-row![/bold white]
""",
    "ta_row": """
Sensei wrote five new characters with careful strokes.

[bold cyan]"The ta-row has two special readings,"[/bold cyan] Sensei noted.
[bold cyan]"た (ta), ち (chi), つ (tsu), て (te), と (to).
Both ち and つ are irregular -- 'chi' not 'ti',
and 'tsu' not 'tu'. These are important!"[/bold cyan]

[bold white]Let's learn the ta-row![/bold white]
""",
    "na_row": """
Sensei smiled as the characters took shape.

[bold cyan]"The na-row is perfectly regular,"[/bold cyan] Sensei said with satisfaction.
[bold cyan]"な (na), に (ni), ぬ (nu), ね (ne), の (no).
No surprises here. And の is one of the most common
characters in Japanese -- it means 'of' or 'possessive'."[/bold cyan]

[bold white]Let's learn the na-row![/bold white]
""",
    "ha_ma_row": """
Sensei laid out two rows of characters side by side.

[bold cyan]"We'll cover two rows together now,"[/bold cyan] Sensei said.
[bold cyan]"The ha-row: は (ha), ひ (hi), ふ (fu), へ (he), ほ (ho).
Note: ふ is 'fu', not 'hu'. And は as a particle is read 'wa'.
The ma-row: ま (ma), み (mi), む (mu), め (me), も (mo)."[/bold cyan]

[bold white]Let's learn the ha-row and ma-row together![/bold white]
""",
    "ya_ra_wa_n": """
Sensei wrote the final characters with a flourish.

[bold cyan]"Almost there! The remaining characters,"[/bold cyan] Sensei said.
[bold cyan]"Ya-row: や (ya), ゆ (yu), よ (yo) — only three.
Ra-row: ら (ra), り (ri), る (ru), れ (re), ろ (ro).
Wa-row: わ (wa), を (wo) — only two.
And finally ん (n) — the only consonant that stands alone."[/bold cyan]

[bold white]Let's complete the hiragana chart![/bold white]
""",
    "reading_practice": """
Sensei placed a card with a full word written in hiragana.

[bold cyan]"Now comes the real test,"[/bold cyan] Sensei said proudly.
[bold cyan]"You know every character. Let's put them together
and read real Japanese words. Sound out each character
one at a time, then blend them together."[/bold cyan]

[bold white]Let's read real words in hiragana![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "vowels": """
[bold green]Sensei nodded with warm approval![/bold green]

[bold cyan]"The five vowels are yours. あいうえお -- these are the foundation
of every sound in Japanese. Well done."[/bold cyan]
""",
    "ka_row": """
[bold green]Sensei placed a small stamp of approval on your paper![/bold green]

[bold cyan]"かきくけこ -- the ka-row is complete. You now know ten hiragana.
The pattern is becoming clear, yes?"[/bold cyan]
""",
    "sa_row": """
[bold green]Sensei's eyes crinkled with a smile![/bold green]

[bold cyan]"さしすせそ -- excellent! Even the tricky し (shi) didn't stop you.
You're building momentum."[/bold cyan]
""",
    "ta_row": """
[bold green]Sensei set down the brush with satisfaction![/bold green]

[bold cyan]"たちつてと -- both irregular readings mastered. ち (chi) and つ (tsu)
trip up many learners, but not you."[/bold cyan]
""",
    "na_row": """
[bold green]Sensei poured you a cup of tea in celebration![/bold green]

[bold cyan]"なにぬねの -- the na-row is yours. You now know half of all hiragana.
The halfway point deserves a moment of rest."[/bold cyan]
""",
    "ha_ma_row": """
[bold green]Sensei clapped once, softly but proudly![/bold green]

[bold cyan]"Two rows in one lesson! は-row and ま-row are complete.
Remember: ふ is 'fu', and は as a particle says 'wa'."[/bold cyan]
""",
    "ya_ra_wa_n": """
[bold green]Sensei bowed respectfully![/bold green]

[bold cyan]"Every hiragana character -- all 46 -- is now in your mind.
From あ to ん, the complete chart is yours. This is a great achievement."[/bold cyan]
""",
    "reading_practice": """
[bold green]Sensei stood and bowed deeply![/bold green]

[bold cyan]"You can read real Japanese words in hiragana. The characters
are no longer mysteries -- they are tools you can use.
You have completed the foundation of Japanese writing."[/bold cyan]
""",
}

BOSS_INTROS = {
    "vowels": """
Sensei held up a fan painted with the five vowels.

[bold cyan]"One final challenge. Can you identify each vowel
by sight and sound without hesitation? Show me."[/bold cyan]
""",
    "ka_row": """
Sensei shuffled five cards and laid them face down.

[bold cyan]"The ka-row challenge. I'll test every character.
Speed and accuracy -- that is the mark of mastery."[/bold cyan]
""",
    "sa_row": """
Sensei wrote characters in rapid succession.

[bold cyan]"The sa-row test, including the tricky し.
Can you read them all without a pause?"[/bold cyan]
""",
    "ta_row": """
Sensei arranged the ta-row in random order.

[bold cyan]"ち and つ -- the irregular readings. This challenge
will test whether you truly know them."[/bold cyan]
""",
    "na_row": """
Sensei held up a scroll with mixed na-row characters.

[bold cyan]"The na-row seems simple, but can you spot each one
among similar-looking characters?"[/bold cyan]
""",
    "ha_ma_row": """
Sensei mixed the ha-row and ma-row characters together.

[bold cyan]"Ten characters, two rows, all mixed together.
Sort them out and read them all correctly."[/bold cyan]
""",
    "ya_ra_wa_n": """
Sensei spread every remaining character across the desk.

[bold cyan]"The final group -- ya, ra, wa, and ん.
Master these and the full chart is yours."[/bold cyan]
""",
    "reading_practice": """
Sensei placed a full sentence in hiragana before you.

[bold cyan]"The ultimate reading challenge. Real words, real sentences.
Read them as naturally as you can. I believe in you."[/bold cyan]
""",
}
