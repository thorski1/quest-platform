"""
story.py — Narrative for the Greetings skill pack.

Pierre guides you through French greetings, politeness, introductions, and cafe culture.
"""

INTRO_STORY = """
[bold red]LEARN FRENCH[/bold red]
[bold yellow]Chapter: Bonjour![/bold yellow]

Pierre stood behind the counter of his cozy Parisian cafe,
wiping a cup with a white cloth. The aroma of fresh coffee
and warm croissants filled the air as morning light
streamed through the lace curtains.

[bold cyan]"Ah, bienvenue!"[/bold cyan] Pierre said with a broad smile.
[bold cyan]"In France, everything begins with a greeting.
You walk into a shop -- bonjour. You meet someone new --
bonjour. You want help -- bonjour first, then ask.
It's the golden rule of French culture."[/bold cyan]

A regular customer walked in and Pierre called out,
[bold yellow]"Bonjour Madame Dupont! Comment allez-vous?"[/bold yellow]

[bold cyan]"See? That's how we connect. Let me teach you
the art of French greetings and politeness."[/bold cyan]

[bold white]Learn to greet, introduce, and connect in French.[/bold white]
"""

ZONE_INTROS = {
    "hello_goodbye": """
Pierre gestured toward the cafe entrance where people came and went.

[bold cyan]"Every interaction in France starts with hello and ends
with goodbye,"[/bold cyan] Pierre said. [bold cyan]"We change our greeting based on
the time of day, and we have casual and formal versions.
Get these right, and every French person will warm to you
immediately!"[/bold cyan]

[bold white]Let's master French hellos and goodbyes![/bold white]
""",
    "please_thank_you": """
Pierre placed a coffee and croissant on the counter.

[bold cyan]"In France, politeness is not optional -- it's essential,"[/bold cyan]
Pierre said firmly. [bold cyan]"Please, thank you, excuse me, sorry --
these words are the keys that open every door. Without them,
even the friendliest Parisian will turn cold."[/bold cyan]

[bold white]Let's learn the magic words of French politeness![/bold white]
""",
    "self_introduction": """
Pierre introduced you to a regular customer at the next table.

[bold cyan]"Time to learn how to introduce yourself!"[/bold cyan] Pierre said.
[bold cyan]"Your name, where you're from, what you do --
in France, a proper introduction shows respect and
creates an instant connection. Let me show you how."[/bold cyan]

[bold white]Let's learn to introduce ourselves in French![/bold white]
""",
    "tu_vs_vous": """
Pierre leaned in conspiratorially.

[bold cyan]"This is the most important cultural lesson,"[/bold cyan] Pierre whispered.
[bold cyan]"French has two words for 'you.' 'Tu' is for friends
and family. 'Vous' is for everyone else until they say otherwise.
Use the wrong one, and you'll make a very awkward impression!"[/bold cyan]

[bold white]Let's master tu vs vous![/bold white]
""",
    "at_the_cafe": """
Pierre spread his arms wide, presenting his cafe.

[bold cyan]"The cafe is the heart of French social life!"[/bold cyan] Pierre declared.
[bold cyan]"Ordering, chatting, asking for the bill -- there's an art
to it all. Get it right and you'll feel like a true Parisian.
Let me show you the ropes."[/bold cyan]

[bold white]Let's learn to navigate a French cafe![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "hello_goodbye": """
[bold green]Pierre gave you a warm handshake![/bold green]

[bold cyan]"Bonjour, bonsoir, au revoir, salut -- you've got them all!
You can now greet anyone at any time of day, formally or
casually. In France, this is half the battle won!"[/bold cyan]
""",
    "please_thank_you": """
[bold green]Pierre placed a hand over his heart![/bold green]

[bold cyan]"S'il vous plait, merci, pardon, desole -- you've mastered
the words that make French people smile. Politeness is the
key to every French heart. You're already ahead of
most visitors!"[/bold cyan]
""",
    "self_introduction": """
[bold green]Pierre clinked his coffee cup against yours![/bold green]

[bold cyan]"You can introduce yourself like a true francophone!
Je m'appelle, je viens de, enchante -- these phrases
will serve you from Paris to Montreal to Dakar.
First impressions, mastered!"[/bold cyan]
""",
    "tu_vs_vous": """
[bold green]Pierre nodded with deep respect![/bold green]

[bold cyan]"You understand tu and vous! This cultural awareness
is what separates a tourist from a true student of French.
You know when to be familiar and when to show respect.
Chapeau!"[/bold cyan]
""",
    "at_the_cafe": """
[bold green]Pierre poured you a celebratory espresso![/bold green]

[bold cyan]"You can walk into any cafe in France and order with
confidence! From bonjour to l'addition, you know
the whole dance. You're an honorary Parisian now!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "hello_goodbye": """
Pierre looked at the clock and then back at you.

[bold cyan]"Quick -- what greeting matches the situation?
I'll test you on every hello and goodbye we've learned.
Time of day and formality both matter!"[/bold cyan]
""",
    "please_thank_you": """
Pierre set up different social scenarios at the cafe.

[bold cyan]"Someone helps you. You bump into someone. You need
to ask for something. What polite phrase fits each moment?
Show me your French manners!"[/bold cyan]
""",
    "self_introduction": """
Pierre gestured to an imaginary group of new people.

[bold cyan]"Imagine you've just arrived at a dinner party in Paris.
Introduce yourself properly -- name, origin, pleasantries.
Can you handle a full French introduction?"[/bold cyan]
""",
    "tu_vs_vous": """
Pierre described different people and situations.

[bold cyan]"Your friend's grandmother. A waiter. Your classmate.
A job interview. Tu or vous? Every situation demands
the right level of formality!"[/bold cyan]
""",
    "at_the_cafe": """
Pierre handed you an imaginary menu.

[bold cyan]"You just sat down at a Parisian cafe. Walk me through
the entire visit -- from entering to leaving.
Show me you can do it like a local!"[/bold cyan]
""",
}
