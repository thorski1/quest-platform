"""
story.py — Narrative for The Hall of Legends (mythology skill pack).
"""

INTRO_STORY = """
[bold cyan]A New Page Appears in the Primer...[/bold cyan]

Puck flutters toward a page that shimmers with golden light and ancient symbols.

[bold yellow]"Oh!"[/bold yellow] Puck gasps, eyes wide. [bold yellow]"This is one of the oldest pages in the whole Primer."[/bold yellow]

The page is covered in tiny illustrations: a thunderbolt, a golden hammer,
a winged horse, a jackal-headed figure, a dragon coiling through clouds,
and a phoenix rising from flames.

[bold yellow]"This is the mythology chapter,"[/bold yellow] Puck whispers.
[bold yellow]"It's about the stories people told before there were books.
Before there was science. Before anyone knew why the sun rose or where
the thunder came from."[/bold yellow]

You touch the page, and the illustrations begin to move and glow.

[bold yellow]"Every culture on Earth made up stories to explain the world,"[/bold yellow] Puck says.
[bold yellow]"Gods and monsters. Heroes and tricksters. Magical creatures and epic quests.
And the amazing thing is — the stories are still with us.
Because the best stories never really end."[/bold yellow]

[bold white]The page glows. The legends awaken.[/bold white]

[italic]"Myths are public dreams, dreams are private myths." — Joseph Campbell[/italic]
"""

ZONE_INTROS = {
    "greek_mythology": (
        "[bold cyan]GREEK MYTHOLOGY[/bold cyan]\n\n"
        "Puck floats beside a marble column covered in ancient Greek writing.\n"
        "[bold yellow]'The Greeks told some of the greatest stories ever. "
        "Gods on a mountaintop. Heroes fighting monsters. A wooden horse that won a war. "
        "These stories are thousands of years old — and people still love them today.'[/bold yellow]"
    ),
    "norse_mythology": (
        "[bold cyan]NORSE MYTHOLOGY[/bold cyan]\n\n"
        "Frost crystals form on the page. A distant hammer rings against an anvil.\n"
        "[bold yellow]'The Vikings lived in a cold, harsh world — and their stories were just as bold. "
        "Gods who fought giants. A world tree holding nine realms. A prophecy about the end of everything. "
        "These myths are wild, fierce, and unforgettable.'[/bold yellow]"
    ),
    "egyptian_mythology": (
        "[bold cyan]EGYPTIAN MYTHOLOGY[/bold cyan]\n\n"
        "Golden sand swirls across the page, revealing hieroglyphics and a gleaming sun.\n"
        "[bold yellow]'The Egyptians built pyramids that have lasted thousands of years — "
        "and their myths are just as lasting. A sun god sailing across the sky. "
        "A jackal guiding the dead. A feather that decides your fate. "
        "Welcome to the land of the pharaohs.'[/bold yellow]"
    ),
    "asian_legends": (
        "[bold cyan]ASIAN LEGENDS[/bold cyan]\n\n"
        "A silk scroll unrolls to reveal a dragon dancing through clouds and cherry blossoms.\n"
        "[bold yellow]'In the East, dragons bring good luck, spirits live in every tree and river, "
        "and an elephant-headed god helps you overcome obstacles. "
        "Asian mythology is beautiful, wise, and full of wonder. "
        "Let's explore it together.'[/bold yellow]"
    ),
    "mythical_creatures": (
        "[bold cyan]MYTHICAL CREATURES[/bold cyan]\n\n"
        "The page fills with wings, scales, horns, and hooves — creatures from every legend ever told.\n"
        "[bold yellow]'Unicorns! Phoenixes! Griffins! Mermaids! Dragons! "
        "Every culture imagined incredible creatures. Some were scary, some were beautiful, "
        "and some might even have been inspired by real animals. "
        "Let's meet the most legendary beings ever imagined.'[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "greek_mythology": (
        "[bold green]ZONE COMPLETE — GREEK MYTHOLOGY![/bold green]\n\n"
        "You've met Zeus, Athena, Hercules, Odysseus, and Pegasus! "
        "[bold yellow]Puck smiles. 'The Greeks invented the word \"hero.\" And now you know why.'[/bold yellow]"
    ),
    "norse_mythology": (
        "[bold green]ZONE COMPLETE — NORSE MYTHOLOGY![/bold green]\n\n"
        "Thor, Odin, Loki, Yggdrasil, and Ragnarok — the Viking sagas are yours! "
        "[bold yellow]'Even the end of the world leads to a new beginning,' Puck says. 'That's what the Vikings believed.'[/bold yellow]"
    ),
    "egyptian_mythology": (
        "[bold green]ZONE COMPLETE — EGYPTIAN MYTHOLOGY![/bold green]\n\n"
        "Ra, Anubis, Isis, the pharaohs, and the afterlife — the mysteries of Egypt are revealed! "
        "[bold yellow]Puck glows like the sun. 'The Egyptians believed your story doesn't end when you die. I think they were right.'[/bold yellow]"
    ),
    "asian_legends": (
        "[bold green]ZONE COMPLETE — ASIAN LEGENDS![/bold green]\n\n"
        "Chinese dragons, Japanese kami, the Monkey King, and Lord Ganesh — the wisdom of the East! "
        "[bold yellow]'East and West tell different stories,' Puck says, 'but they all ask the same big questions. "
        "That's what makes mythology universal.'[/bold yellow]"
    ),
    "mythical_creatures": (
        "[bold green]ZONE COMPLETE — MYTHICAL CREATURES![/bold green]\n\n"
        "Unicorns, phoenixes, griffins, mermaids, dragons, and more — the bestiary is complete! "
        "[bold yellow]Puck laughs. 'You know what I love? These creatures never existed — "
        "but they changed the world anyway. That's the power of imagination.'[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "greek_mythology": (
        "[bold red]BOSS CHALLENGE — GREEK MYTHOLOGY QUIZ[/bold red]\n\n"
        "[bold yellow]'The Olympians are watching! Zeus, Athena, Poseidon — they want to know "
        "if you've been paying attention. Show them what you've learned!'[/bold yellow]"
    ),
    "norse_mythology": (
        "[bold red]BOSS CHALLENGE — NORSE MYTHOLOGY QUIZ[/bold red]\n\n"
        "[bold yellow]'Odin's ravens have been watching you learn. Now the All-Father wants to test your wisdom. "
        "Pick up your courage — the nine worlds are counting on you!'[/bold yellow]"
    ),
    "egyptian_mythology": (
        "[bold red]BOSS CHALLENGE — EGYPTIAN MYTHOLOGY QUIZ[/bold red]\n\n"
        "[bold yellow]'Anubis stands before you with the scales of judgment. "
        "Your knowledge will be weighed against the Feather of Truth. "
        "Answer wisely — the afterlife awaits!'[/bold yellow]"
    ),
    "asian_legends": (
        "[bold red]BOSS CHALLENGE — ASIAN LEGENDS QUIZ[/bold red]\n\n"
        "[bold yellow]'The Dragon King rises from the sea! The kami whisper in the wind! "
        "Ganesh raises his hand to clear your path — but first, you must prove what you know. "
        "The wisdom of the East is calling!'[/bold yellow]"
    ),
    "mythical_creatures": (
        "[bold red]BOSS CHALLENGE — MYTHICAL CREATURES QUIZ[/bold red]\n\n"
        "[bold yellow]'The bestiary is open and every creature is watching! "
        "Phoenix, griffin, unicorn, dragon, mermaid — can you tell them all apart? "
        "Show me you know every legend in the book!'[/bold yellow]"
    ),
}
