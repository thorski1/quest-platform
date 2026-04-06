"""
story.py — Narrative for the Greetings skill pack.

Long Long guides you through your first conversations in Chinese,
from hello to polite expressions.
"""

INTRO_STORY = """
[bold red]LEARN CHINESE[/bold red]
[bold yellow]Chapter: First Words[/bold yellow]

Long Long the dragon landed in the middle of a bustling Chinese street.
Red lanterns hung overhead, and the smell of steamed buns drifted
through the air. People were talking, laughing, greeting each other.

[bold cyan]"This,"[/bold cyan] Long Long said, gesturing with a golden claw,
[bold cyan]"is where language comes alive. Not in a textbook --
in the street, in the market, between people.
And it all starts with one word..."[/bold cyan]

Long Long turned to a passing stranger and said:
[bold yellow]"Ni hao!"[/bold yellow] (你好!)

The stranger smiled and replied: [bold yellow]"Ni hao!"[/bold yellow]

[bold cyan]"See? Two syllables and you've made a connection.
That's the power of greetings -- they open every door.
By the end of this chapter, you'll be able to
introduce yourself, be polite, ask questions,
and hold a basic conversation."[/bold cyan]

Long Long spread both wings wide.

[bold cyan]"Ready to say your first words in Chinese?"[/bold cyan]

[bold white]Your journey into Chinese conversation begins now.[/bold white]
"""

ZONE_INTROS = {
    "hello_goodbye": """
Long Long stood at the entrance of a teahouse.

[bold cyan]"Every conversation starts and ends with a greeting,"[/bold cyan]
Long Long said. [bold cyan]"In Chinese, 'hello' is simple and beautiful:
ni hao -- literally 'you good'. And when you leave,
you say zai jian -- 'again see', meaning 'see you again'."[/bold cyan]

[bold white]Let's learn the words that open and close every conversation![/bold white]
""",
    "introductions": """
Long Long offered a claw to shake.

[bold cyan]"Now that you can say hello, people will want to know
who you are!"[/bold cyan] Long Long said. [bold cyan]"In Chinese, you introduce
yourself by saying 'wo jiao...' (I'm called...) or
'wo shi...' (I am...). Simple and direct."[/bold cyan]

[bold white]Let's learn to introduce yourself in Mandarin![/bold white]
""",
    "how_are_you": """
Long Long tilted the dragon head with concern.

[bold cyan]"After hello, the next natural question is:
how are you?"[/bold cyan] Long Long said. [bold cyan]"In Chinese it's
'ni hao ma?' And the answers range from
'very good' to 'not great' -- just like in life."[/bold cyan]

[bold white]Let's learn to ask and answer about wellbeing![/bold white]
""",
    "please_thanks": """
Long Long bowed deeply.

[bold cyan]"Politeness opens more doors than any key,"[/bold cyan]
Long Long said. [bold cyan]"Please, thank you, sorry, and no problem --
these four expressions will carry you through
almost any social situation in China."[/bold cyan]

[bold white]Let's master the magic words of Chinese politeness![/bold white]
""",
    "yes_no": """
Long Long held up two claws -- one for yes, one for no.

[bold cyan]"Here's something fascinating about Chinese,"[/bold cyan]
Long Long said. [bold cyan]"There's no single word for 'yes' or 'no'!
Instead, you repeat the verb to say yes, or add 'bu'
before it to say no. It's a completely different system."[/bold cyan]

[bold white]Let's learn the Chinese way of saying yes and no![/bold white]
""",
    "common_phrases": """
Long Long pulled out a pocket phrasebook.

[bold cyan]"Some phrases are so useful you'll need them every day,"[/bold cyan]
Long Long said. [bold cyan]"How much? Where is it? What is this?
Master these and you can navigate markets, streets,
and conversations with confidence."[/bold cyan]

[bold white]Let's learn the phrases that solve everyday problems![/bold white]
""",
    "polite_expressions": """
Long Long straightened up with perfect posture.

[bold cyan]"Chinese has layers of politeness,"[/bold cyan] Long Long explained.
[bold cyan]"There's casual speech for friends, and formal speech
for elders and strangers. The word 'nin' instead of 'ni'
can show deep respect with just one syllable change."[/bold cyan]

[bold white]Let's explore the art of Chinese politeness![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "hello_goodbye": """
[bold green]Long Long beamed with pride![/bold green]

[bold cyan]"You can greet anyone in Chinese now! Ni hao, xie xie,
zai jian -- these simple words connect you to 1.4 billion people."[/bold cyan]
""",
    "introductions": """
[bold green]Long Long clapped those golden claws![/bold green]

[bold cyan]"Wonderful! You can introduce yourself, ask someone's name,
say where you're from. The first real conversation is within reach!"[/bold cyan]
""",
    "how_are_you": """
[bold green]Long Long nodded warmly![/bold green]

[bold cyan]"You can ask how someone is doing and respond naturally.
This is real social connection -- not just vocabulary!"[/bold cyan]
""",
    "please_thanks": """
[bold green]Long Long bowed in appreciation![/bold green]

[bold cyan]"Please, thank you, sorry, no problem -- the four pillars
of politeness. You now have the tools to be gracious in any situation."[/bold cyan]
""",
    "yes_no": """
[bold green]Long Long raised both claws in triumph![/bold green]

[bold cyan]"You've mastered the Chinese yes/no system! No single word
for yes or no -- instead, you echo the verb. It's elegant once you get it!"[/bold cyan]
""",
    "common_phrases": """
[bold green]Long Long did a little victory dance![/bold green]

[bold cyan]"How much? Where? What? You can ask the questions that matter most.
With these phrases, you could actually survive a trip to China!"[/bold cyan]
""",
    "polite_expressions": """
[bold green]Long Long bowed with deep respect![/bold green]

[bold cyan]"You understand the nuances of Chinese politeness -- formal vs casual,
nin vs ni, the respect shown to elders. This cultural knowledge
is just as important as the words themselves."[/bold cyan]
""",
}

BOSS_INTROS = {
    "hello_goodbye": """
Long Long's eyes sparkled.

[bold cyan]"Final greeting challenge! Can you handle hello, goodbye,
thanks, and politeness all mixed together?"[/bold cyan]
""",
    "introductions": """
Long Long gestured to an imaginary crowd.

[bold cyan]"Introduce yourself perfectly -- name, nationality, identity.
Show me you can meet anyone in Chinese!"[/bold cyan]
""",
    "how_are_you": """
Long Long looked concerned, then happy, then so-so.

[bold cyan]"How are you? The answers aren't always simple.
Show me you can handle the full range!"[/bold cyan]
""",
    "please_thanks": """
Long Long set up a mock social scenario.

[bold cyan]"Please, thanks, sorry, you're welcome -- all in one challenge.
True politeness means knowing which to use when!"[/bold cyan]
""",
    "yes_no": """
Long Long fired rapid questions.

[bold cyan]"Yes or no? But remember -- there's no single word for either!
Show me you've truly understood the Chinese way."[/bold cyan]
""",
    "common_phrases": """
Long Long transformed into a market vendor.

[bold cyan]"You're in a Chinese market. Prices, directions, questions --
use everything you've learned!"[/bold cyan]
""",
    "polite_expressions": """
Long Long became a wise elder.

[bold cyan]"The ultimate politeness test. Formal, informal, respectful --
show me you understand the layers of Chinese courtesy."[/bold cyan]
""",
}
