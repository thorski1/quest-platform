"""
story.py — Narrative for The Time Traveler's Primer (history skill pack).
"""

INTRO_STORY = """
[bold cyan]A New Page Appears in the Primer...[/bold cyan]

Puck floats over to a page that seems to shimmer with age.

[bold yellow]"Oh!"[/bold yellow] Puck breathes. [bold yellow]"This one is special."[/bold yellow]

The page is covered in tiny illustrations: pyramids, tall ships, airplanes,
people marching arm in arm, a boy with a telescope looking at the stars.

[bold yellow]"This is the history chapter,"[/bold yellow] Puck says softly.
[bold yellow]"It's about all the people who came before you. The things they built.
The journeys they took. The mistakes they made — and what they learned."[/bold yellow]

You touch the page, and suddenly the illustrations start moving.

[bold yellow]"History isn't just facts and dates,"[/bold yellow] Puck says.
[bold yellow]"It's people. Real people — who were brave, and scared, and curious,
and sometimes wrong, and sometimes remarkable.
Just like you."[/bold yellow]

[bold white]The page glows. Time begins to move.[/bold white]

[italic]"Those who cannot remember the past are condemned to repeat it." — George Santayana[/italic]
"""

ZONE_INTROS = {
    "ancient_civilizations": (
        "[bold cyan]THE ANCIENT WORLD[/bold cyan]\n\n"
        "Puck flutters around images of pyramids and marble temples.\n"
        "[bold yellow]'Before phones, before cars, before even books — people built incredible things. "
        "Cities! Writing! Democracy! Let's visit the very first great civilizations.'[/bold yellow]"
    ),
    "explorers_and_discoveries": (
        "[bold cyan]THE AGE OF EXPLORATION[/bold cyan]\n\n"
        "A tiny ship appears on the page, setting sail into unknown waters.\n"
        "[bold yellow]'Imagine getting on a boat and sailing toward the horizon, "
        "not knowing what you'd find. These explorers did exactly that. "
        "And what they found changed the world forever.'[/bold yellow]"
    ),
    "inventions_and_inventors": (
        "[bold cyan]THE INVENTION WORKSHOP[/bold cyan]\n\n"
        "Light bulbs and blueprints float across the page.\n"
        "[bold yellow]'Every invention started with someone saying: what if this was possible? "
        "The printing press. The telephone. The airplane. The internet. "
        "One idea — and nothing was ever the same.'[/bold yellow]"
    ),
    "world_wars": (
        "[bold cyan]THE GREAT CONFLICTS[/bold cyan]\n\n"
        "Puck's glow dims slightly. [bold yellow]'This chapter is about something hard. "
        "Two wars that changed everything — and cost millions of lives. "
        "We study them not to celebrate war, but to understand it. "
        "And to make sure we do better.'[/bold yellow]"
    ),
    "american_history": (
        "[bold cyan]THE AMERICAN STORY[/bold cyan]\n\n"
        "An eagle soars across the page. [bold yellow]'America is a country built on a promise: "
        "that all people are created equal. "
        "Sometimes that promise was broken. But people kept fighting to keep it. "
        "That fight is still happening today.'[/bold yellow]"
    ),
    "world_leaders_and_change": (
        "[bold cyan]THE COURAGE CHAPTER[/bold cyan]\n\n"
        "Puck glows warmly. [bold yellow]'These are the people who looked at something unfair "
        "and said: I will not accept this. They were not born powerful. "
        "They became powerful through courage. "
        "And because of them, the world is better.'[/bold yellow]"
    ),
    "ancient_wonders": (
        "[bold cyan]THE WONDERS CHAPTER[/bold cyan]\n\n"
        "Tiny golden images shimmer on the page — a pyramid, a lighthouse, a colossal statue.\n"
        "[bold yellow]'Long before cranes and computers and electricity, humans built things "
        "so incredible that people still talk about them thousands of years later. "
        "Let's visit the most extraordinary structures ever made.'[/bold yellow]"
    ),
    "indigenous_peoples": (
        "[bold cyan]THE FIRST PEOPLES[/bold cyan]\n\n"
        "The page fills with images from every continent — feathers, carved wood, stars, hands.\n"
        "[bold yellow]'Before explorers arrived, before empires formed, people lived everywhere on Earth — "
        "with languages, stories, science, and art. "
        "These are the first peoples of the world. Their stories are among the most important of all.'[/bold yellow]"
    ),
    "science_history": (
        "[bold cyan]THE SCIENTISTS[/bold cyan]\n\n"
        "Equations, telescopes, test tubes, and satellites float across the page.\n"
        "[bold yellow]'Some people changed history with armies. Others changed it with an idea. "
        "Scientists looked at the world — and figured out how it actually works. "
        "Let's meet the minds who changed everything.'[/bold yellow]"
    ),
    "rights_and_revolutions": (
        "[bold cyan]THE FREEDOM ROAD[/bold cyan]\n\n"
        "Torches, marches, peaceful protests, bold speeches — the page fills with "
        "images of ordinary people doing extraordinary things.\n"
        "[bold yellow]'History isn't just made by kings and generals. "
        "It's made by people who stood up and said: This is not fair. "
        "This must change. And then they did something about it.'[/bold yellow]"
    ),
    "women_in_history": (
        "[bold cyan]HIDDEN FIGURES[/bold cyan]\n\n"
        "Puck opened a page that was mostly blank — but as you looked, "
        "names began to appear, one by one. "
        "Women who had been overlooked. Women who had changed everything. Women whose stories waited to be found.\n"
        "[bold yellow]'History has two halves,' Puck said quietly. "
        "'For a long time, only one was being told. "
        "Let's find the other one.'[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "ancient_civilizations": (
        "[bold green]ZONE COMPLETE — THE ANCIENT WORLD![/bold green]\n\n"
        "You've visited Egypt, Greece, Rome, and Mesopotamia. "
        "[bold yellow]Puck claps. 'Those civilizations built the foundation for almost everything!'[/bold yellow]"
    ),
    "explorers_and_discoveries": (
        "[bold green]ZONE COMPLETE — AGE OF EXPLORATION![/bold green]\n\n"
        "The brave explorers are honored. "
        "[bold yellow]'They didn't know what they'd find,' Puck says. 'But they went anyway. That takes courage.'[/bold yellow]"
    ),
    "inventions_and_inventors": (
        "[bold green]ZONE COMPLETE — THE INVENTION WORKSHOP![/bold green]\n\n"
        "Every invention remembered. "
        "[bold yellow]'You know what's amazing?' Puck says. 'Every one of those inventors was told it was impossible first.'[/bold yellow]"
    ),
    "world_wars": (
        "[bold green]ZONE COMPLETE — THE GREAT CONFLICTS[/bold green]\n\n"
        "A heavy chapter, completed with care. "
        "[bold yellow]Puck is quiet for a moment. 'Thank you for taking this seriously. That's what history deserves.'[/bold yellow]"
    ),
    "american_history": (
        "[bold green]ZONE COMPLETE — THE AMERICAN STORY![/bold green]\n\n"
        "The Declaration, the Constitution, the Civil War, civil rights, and suffrage. "
        "[bold yellow]'America is still becoming what it promised to be,' Puck says. 'And that work belongs to you too.'[/bold yellow]"
    ),
    "world_leaders_and_change": (
        "[bold green]ZONE COMPLETE — THE COURAGE CHAPTER![/bold green]\n\n"
        "The great leaders remembered and celebrated. "
        "[bold yellow]Puck glows gold. 'One day, someone will be learning about the change YOU made. I believe that.'[/bold yellow]"
    ),
    "ancient_wonders": (
        "[bold green]ZONE COMPLETE — THE WONDERS CHAPTER![/bold green]\n\n"
        "Pyramids, lighthouses, colossal statues, the Great Wall — the ancient world explored! "
        "[bold yellow]'These wonders remind us that humans have always been capable of extraordinary things. "
        "And so are you.'[/bold yellow]"
    ),
    "indigenous_peoples": (
        "[bold green]ZONE COMPLETE — THE FIRST PEOPLES![/bold green]\n\n"
        "Aboriginal Australians, the Maya, the Iroquois, the Maori, and more — honored and remembered! "
        "[bold yellow]Puck is quiet for a moment. 'These stories were almost lost. "
        "You carrying them forward means they survive.'[/bold yellow]"
    ),
    "science_history": (
        "[bold green]ZONE COMPLETE — THE SCIENTISTS![/bold green]\n\n"
        "Newton, Darwin, Curie, Einstein, Franklin, and Johnson — the minds who changed the world! "
        "[bold yellow]'Science isn't done,' Puck says. 'It never is. "
        "Maybe the next name on this list... is yours.'[/bold yellow]"
    ),
    "rights_and_revolutions": (
        "[bold green]ZONE COMPLETE — THE FREEDOM ROAD![/bold green]\n\n"
        "The French Revolution, Gandhi's Salt March, Rosa Parks, Mandela, the suffragettes — "
        "ordinary people who changed the world! "
        "[bold yellow]'Every one of them was told they couldn't win,' Puck says softly. "
        "'Every one of them proved the doubters wrong. "
        "And every one of them started by simply deciding to try.'[/bold yellow]"
    ),
    "women_in_history": (
        "[bold green]ZONE COMPLETE — HIDDEN NO MORE![/bold green]\n\n"
        "Cleopatra, Curie, Tubman, Lovelace, Malala — and the thousands more whose stories "
        "are still being discovered! "
        "[bold yellow]Puck smiled, and the blank pages of the Primer glowed. "
        "'Half the story is back where it belongs. "
        "History is richer, truer, and more inspiring with all of it.'[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "ancient_civilizations": (
        "[bold red]BOSS CHALLENGE — ANCIENT CIVILIZATIONS QUIZ[/bold red]\n\n"
        "[bold yellow]'Puck shuffles the civilizations! Can you match each to its greatest achievement? No hints this time — you know this!'[/bold yellow]"
    ),
    "explorers_and_discoveries": (
        "[bold red]BOSS CHALLENGE — THE GREATEST JOURNEY[/bold red]\n\n"
        "[bold yellow]'Who did what? The explorers are all mixed up. Show Puck you can tell them apart!'[/bold yellow]"
    ),
    "inventions_and_inventors": (
        "[bold red]BOSS CHALLENGE — INVENTION TIMELINE[/bold red]\n\n"
        "[bold yellow]'Can you figure out which invention came FIRST in history? Think carefully!'[/bold yellow]"
    ),
    "world_wars": (
        "[bold red]BOSS CHALLENGE — PEACE AND JUSTICE[/bold red]\n\n"
        "[bold yellow]'This is the most important question in the whole chapter. Think about WHY we study these wars.'[/bold yellow]"
    ),
    "american_history": (
        "[bold red]BOSS CHALLENGE — THE AMERICAN PROMISE[/bold red]\n\n"
        "[bold yellow]'The Constitution has been amended many times to expand freedom. Which amendment was most important for ending slavery?'[/bold yellow]"
    ),
    "world_leaders_and_change": (
        "[bold red]BOSS CHALLENGE — THE COMMON THREAD[/bold red]\n\n"
        "[bold yellow]'Puck asks the deepest question: what connects Gandhi, Mandela, Malala, Roosevelt, and King?'[/bold yellow]"
    ),
    "ancient_wonders": (
        "[bold red]BOSS CHALLENGE — WONDER MATCH[/bold red]\n\n"
        "[bold yellow]'The wonders are all mixed up! Can you match each structure to where it stood "
        "and what made it remarkable? The ancient world is testing you!'[/bold yellow]"
    ),
    "indigenous_peoples": (
        "[bold red]BOSS CHALLENGE — FIRST PEOPLES[/bold red]\n\n"
        "[bold yellow]'Can you match each people to their homeland and their great achievement? "
        "These stories matter — show me you remember them!'[/bold yellow]"
    ),
    "science_history": (
        "[bold red]BOSS CHALLENGE — SCIENCE HALL OF FAME[/bold red]\n\n"
        "[bold yellow]'Newton to Johnson, Darwin to Curie — I describe a discovery, you name the scientist. "
        "These minds changed everything. Let them live in yours!'[/bold yellow]"
    ),
    "rights_and_revolutions": (
        "[bold red]BOSS CHALLENGE — THE COURAGE TEST[/bold red]\n\n"
        "[bold yellow]'Rosa Parks, Gandhi, Mandela, the suffragettes — ordinary people who changed the world. "
        "I will describe a struggle for justice. You tell me who fought it and what they believed. "
        "These are the stories that should never be forgotten.'[/bold yellow]"
    ),
    "women_in_history": (
        "[bold red]BOSS CHALLENGE — HALF THE STORY[/bold red]\n\n"
        "[bold yellow]'Cleopatra to Malala. Ada Lovelace to Harriet Tubman. "
        "These women changed the world — and the world didn't always notice. "
        "Show me you noticed. Show me you remember. Show me their work was not in vain.'[/bold yellow]"
    ),
}
