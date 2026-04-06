"""
story.py — Narrative for the Katakana skill pack.

Sensei (先生) guides you through katakana, the angular script used for
loanwords, foreign names, onomatopoeia, and emphasis in Japanese.
"""

INTRO_STORY = """
[bold red]LEARN JAPANESE[/bold red]
[bold yellow]Chapter: The Script of the World[/bold yellow]

Sensei placed a Japanese newspaper on the desk, pointing to
words written in sharp, angular characters -- different from
the flowing hiragana you already knew.

[bold cyan]"You can already read hiragana,"[/bold cyan] Sensei said.
[bold cyan]"Now it's time for katakana -- the second script.
Katakana is used for words borrowed from other languages,
foreign names, scientific terms, and emphasis.
In modern Japan, you see katakana everywhere."[/bold cyan]

Sensei pointed to words on the page:
[bold yellow]コーヒー  テレビ  コンピューター[/bold yellow]

[bold cyan]"Can you guess? These are 'coffee', 'television',
and 'computer' -- English words adapted into Japanese.
With katakana, you'll be able to read thousands of
familiar words in Japanese."[/bold cyan]

Sensei smiled.

[bold cyan]"The good news? Katakana has the same sounds as hiragana.
Same 46 characters, just different shapes. Shall we begin?"[/bold cyan]

[bold white]Your journey into the angular world of katakana begins now.[/bold white]
"""

ZONE_INTROS = {
    "vowels_kata": """
Sensei wrote five angular characters in a row.

[bold cyan]"Just like hiragana, we start with the five vowels,"[/bold cyan] Sensei said.
[bold cyan]"ア (a), イ (i), ウ (u), エ (e), オ (o).
Same sounds as あいうえお, but sharper, more angular shapes.
Katakana was originally derived from parts of kanji characters."[/bold cyan]

[bold white]Let's learn the five katakana vowels![/bold white]
""",
    "ka_sa_rows": """
Sensei laid out two rows of angular characters.

[bold cyan]"We'll cover two rows at once,"[/bold cyan] Sensei said.
[bold cyan]"Ka-row: カ (ka), キ (ki), ク (ku), ケ (ke), コ (ko).
Sa-row: サ (sa), シ (shi), ス (su), セ (se), ソ (so).
Watch out for シ (shi) and ツ (tsu) -- they look very similar!"[/bold cyan]

[bold white]Let's learn the katakana ka-row and sa-row![/bold white]
""",
    "ta_na_rows": """
Sensei continued building the katakana chart.

[bold cyan]"Ta-row: タ (ta), チ (chi), ツ (tsu), テ (te), ト (to),"[/bold cyan] Sensei said.
[bold cyan]"Na-row: ナ (na), ニ (ni), ヌ (nu), ネ (ne), ノ (no).
Remember: チ is 'chi' and ツ is 'tsu' -- same irregulars as hiragana."[/bold cyan]

[bold white]Let's learn the katakana ta-row and na-row![/bold white]
""",
    "ha_ma_rows": """
Sensei added the next two rows to the growing chart.

[bold cyan]"Ha-row: ハ (ha), ヒ (hi), フ (fu), ヘ (he), ホ (ho),"[/bold cyan] Sensei said.
[bold cyan]"Ma-row: マ (ma), ミ (mi), ム (mu), メ (me), モ (mo).
フ is still 'fu', not 'hu' -- same as in hiragana."[/bold cyan]

[bold white]Let's learn the katakana ha-row and ma-row![/bold white]
""",
    "ya_ra_wa_n": """
Sensei wrote the remaining katakana characters.

[bold cyan]"Almost complete!"[/bold cyan] Sensei said.
[bold cyan]"Ya-row: ヤ (ya), ユ (yu), ヨ (yo).
Ra-row: ラ (ra), リ (ri), ル (ru), レ (re), ロ (ro).
Wa-row: ワ (wa), ヲ (wo). And finally ン (n)."[/bold cyan]

[bold white]Let's finish the katakana chart![/bold white]
""",
    "long_vowels_special": """
Sensei drew a long horizontal line: ー

[bold cyan]"Katakana has special features hiragana doesn't,"[/bold cyan] Sensei explained.
[bold cyan]"The long vowel mark ー extends a vowel sound.
コーヒー (koohii) = coffee. See the ー after コ and ヒ?
We also have special combinations for sounds that don't
exist in native Japanese, like ティ (ti), ファ (fa), ヴ (vu)."[/bold cyan]

[bold white]Let's master the special features of katakana![/bold white]
""",
    "reading_loanwords": """
Sensei spread a collection of product labels and signs across the desk.

[bold cyan]"Now for the fun part,"[/bold cyan] Sensei said with a grin.
[bold cyan]"Reading real loanwords! Japanese has borrowed thousands
of words from English and other languages. Once you decode
the katakana, you'll often recognize the original word."[/bold cyan]

[bold white]Let's read real loanwords in katakana![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "vowels_kata": """
[bold green]Sensei nodded with approval![/bold green]

[bold cyan]"アイウエオ -- the five katakana vowels are yours.
Same sounds as hiragana, new shapes. You're adapting quickly."[/bold cyan]
""",
    "ka_sa_rows": """
[bold green]Sensei tapped the desk in satisfaction![/bold green]

[bold cyan]"Ten more katakana mastered! You can tell カ from サ,
and you know that シ is still 'shi'. Excellent progress."[/bold cyan]
""",
    "ta_na_rows": """
[bold green]Sensei poured celebratory tea![/bold green]

[bold cyan]"The ta-row and na-row -- complete. ツ (tsu) and チ (chi)
are no longer mysteries. You're past the halfway point!"[/bold cyan]
""",
    "ha_ma_rows": """
[bold green]Sensei clapped with delight![/bold green]

[bold cyan]"Ha-row and ma-row conquered! フ is still 'fu',
and you can spot the difference between ハ and ハ行.
The chart is nearly complete."[/bold cyan]
""",
    "ya_ra_wa_n": """
[bold green]Sensei bowed respectfully![/bold green]

[bold cyan]"Every katakana character is now in your arsenal.
From ア to ン -- all 46 angular forms. You now know
both Japanese phonetic scripts!"[/bold cyan]
""",
    "long_vowels_special": """
[bold green]Sensei struck the desk with joy![/bold green]

[bold cyan]"Long vowels, special combinations -- you've mastered
the unique features that make katakana so versatile.
コーヒー, ティッシュ, ファイル -- nothing can stop you now."[/bold cyan]
""",
    "reading_loanwords": """
[bold green]Sensei stood and applauded![/bold green]

[bold cyan]"You can read real loanwords in katakana! Restaurant menus,
product labels, street signs -- thousands of words in Japan
are now accessible to you. This is a powerful skill."[/bold cyan]
""",
}

BOSS_INTROS = {
    "vowels_kata": """
Sensei held up flashcards with both hiragana and katakana.

[bold cyan]"Can you match each katakana vowel to its hiragana twin?
Same sounds, different shapes. Show me you know them."[/bold cyan]
""",
    "ka_sa_rows": """
Sensei mixed ka-row and sa-row characters together.

[bold cyan]"Ten characters, all shuffled. Can you identify
every one, including the tricky シ (shi)?"[/bold cyan]
""",
    "ta_na_rows": """
Sensei arranged confusing look-alike characters.

[bold cyan]"ツ and シ, ソ and ン -- these are the pairs
that confuse everyone. Can you tell them apart?"[/bold cyan]
""",
    "ha_ma_rows": """
Sensei wrote characters at speed.

[bold cyan]"Quick identification challenge! ハ-row and マ-row
characters coming at you fast."[/bold cyan]
""",
    "ya_ra_wa_n": """
Sensei displayed the full katakana chart.

[bold cyan]"The complete chart challenge. I'll test you on
characters from every row. All 46 -- are you ready?"[/bold cyan]
""",
    "long_vowels_special": """
Sensei held up words with special features.

[bold cyan]"Long vowels, double consonants, and foreign sounds.
This is what makes katakana truly powerful."[/bold cyan]
""",
    "reading_loanwords": """
Sensei placed a restaurant menu written entirely in katakana.

[bold cyan]"The ultimate loanword challenge. Read the menu,
understand the items. This is real-world katakana!"[/bold cyan]
""",
}
