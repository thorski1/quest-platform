"""
story.py -- Narrative for the Korean Greetings skill pack.

An alien diplomat studies Korean social protocols to understand
how Earthlings build trust and respect through language.
"""

INTRO_STORY = """
[bold red]LEARN KOREAN[/bold red]
[bold yellow]Chapter: Korean Greetings[/bold yellow]

The alien diplomat reviewed transmissions from the Korean peninsula,
fascinated by how a single phrase could convey respect, warmth,
and social standing all at once.

[bold cyan]"Remarkable,"[/bold cyan] the diplomat murmured, replaying a clip.
[bold cyan]"Their greeting system encodes social hierarchy directly
into the language. A single word changes form depending on
who you're speaking to -- age, status, familiarity."[/bold cyan]

The diplomat turned to you with keen interest.

[bold cyan]"In Korean, greetings are not just pleasantries.
They are social contracts. 안녕하세요 is not merely 'hello' --
it literally asks 'Are you at peace?' The response matters.
The formality level matters. Everything matters."[/bold cyan]

The diplomat adjusted their translator.

[bold cyan]"Help me decode these social protocols.
We start with the basics: hello and goodbye."[/bold cyan]

[bold white]Your journey into Korean social language begins now.[/bold white]
"""

ZONE_INTROS = {
    "hello_goodbye": """
The diplomat played back recordings of Koreans greeting each other
at different times of day.

[bold cyan]"Unlike some Earth languages, Korean doesn't change greetings
by time of day,"[/bold cyan] the diplomat noted. [bold cyan]"안녕하세요 works morning,
noon, and night. But the LEVEL of formality changes everything.
And goodbye? They have different words depending on who's leaving."[/bold cyan]

[bold white]Let's learn hello and goodbye![/bold white]
""",
    "thank_sorry": """
The diplomat observed Koreans bowing to each other in various situations.

[bold cyan]"Gratitude and apology are deeply intertwined here,"[/bold cyan]
the diplomat observed. [bold cyan]"감사합니다 and 죄송합니다 --
thank you and I'm sorry -- are said with equal frequency.
The depth of the bow matches the depth of the feeling."[/bold cyan]

[bold white]Let's master thanking and apologizing![/bold white]
""",
    "self_intro": """
The diplomat watched a Korean business meeting where everyone
exchanged cards and introduced themselves.

[bold cyan]"Self-introduction follows a precise pattern,"[/bold cyan] the diplomat said.
[bold cyan]"Name, origin, occupation -- delivered with a bow.
처음 뵙겠습니다 (nice to meet you) and 잘 부탁드립니다
(please take care of me) bookend the introduction."[/bold cyan]

[bold white]Let's learn to introduce yourself![/bold white]
""",
    "polite_casual": """
The diplomat compared two conversations: one between colleagues
and one between close friends.

[bold cyan]"This is where Korean gets fascinating,"[/bold cyan] the diplomat said.
[bold cyan]"The same sentence changes completely based on formality.
해요 (polite) vs 해 (casual). 먹어요 vs 먹어.
Using the wrong level can cause real social damage."[/bold cyan]

[bold white]Let's navigate politeness levels![/bold white]
""",
    "common_phrases": """
The diplomat compiled a list of phrases that appeared most
frequently in everyday Korean conversations.

[bold cyan]"These are the high-frequency phrases,"[/bold cyan] the diplomat said.
[bold cyan]"잠깐만요 (just a moment), 괜찮아요 (it's okay),
네 (yes), 아니요 (no). Master these and you can handle
basic interactions anywhere in Korea."[/bold cyan]

[bold white]Let's learn essential everyday phrases![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "hello_goodbye": """
[bold green]The diplomat's translator hummed with approval![/bold green]

[bold cyan]"You now know how to greet and part with anyone in Korean.
안녕 -- may you always be at peace."[/bold cyan]
""",
    "thank_sorry": """
[bold green]The diplomat bowed -- an Earth gesture they'd practiced![/bold green]

[bold cyan]"Gratitude and humility -- 감사합니다 and 죄송합니다.
These words build trust in Korean society."[/bold cyan]
""",
    "self_intro": """
[bold green]The diplomat handed you a virtual Korean business card![/bold green]

[bold cyan]"You can introduce yourself properly in Korean now.
First impressions are everything in this culture."[/bold cyan]
""",
    "polite_casual": """
[bold green]The diplomat nodded with understanding![/bold green]

[bold cyan]"You can navigate the formality spectrum.
This is perhaps the most critical social skill in Korean."[/bold cyan]
""",
    "common_phrases": """
[bold green]The diplomat's database updated with new entries![/bold green]

[bold cyan]"Essential phrases acquired. You now have the tools
to handle everyday Korean interactions with confidence."[/bold cyan]
""",
}

BOSS_INTROS = {
    "hello_goodbye": """
The diplomat set up a simulation of meeting someone new.

[bold cyan]"Greet them properly. Say goodbye correctly.
Show me you understand Korean social entry and exit."[/bold cyan]
""",
    "thank_sorry": """
The diplomat presented awkward social scenarios.

[bold cyan]"When to thank? When to apologize?
Choose the right expression for each situation."[/bold cyan]
""",
    "self_intro": """
The diplomat role-played a new acquaintance.

[bold cyan]"Introduce yourself completely. Name, background,
and the proper closing phrase. Get it all right."[/bold cyan]
""",
    "polite_casual": """
The diplomat presented pairs of speakers with different relationships.

[bold cyan]"Polite or casual? The context tells you which.
One wrong choice and the social fabric tears."[/bold cyan]
""",
    "common_phrases": """
The diplomat simulated rapid everyday situations.

[bold cyan]"React quickly with the right phrase.
In real life, you won't have time to think."[/bold cyan]
""",
}
