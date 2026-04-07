"""
story.py — Narrative for The Python Playground skill pack.
Puck-narrated, aimed at kids ages 8-12 learning real Python.
"""

INTRO_STORY = """
[bold cyan]Welcome to The Python Playground![/bold cyan]

Puck zooms through a glowing archway and lands on a keyboard the size of a park bench.

[bold yellow]"Whoa! Look at this place!"[/bold yellow] Puck squeaks, bouncing on the spacebar.
[bold yellow]"This is the Python Playground — where you learn to write REAL code that REALLY runs!"[/bold yellow]

All around you, colourful lines of code float in the air like fireflies.
A friendly snake — the Python mascot — coils around a signpost that reads:
[bold green]"print('Hello, world!')"[/bold green]

[bold yellow]"In The Code Garden, we learned HOW programs think. But here? Here we WRITE them!"[/bold yellow]

Puck pulls out a tiny glowing laptop. [bold yellow]"Python is one of the most popular programming languages in the world. It's used to build games, websites, robots, and even AI! And the best part? It reads almost like English."[/bold yellow]

[bold white]"Will it be hard?"[/bold white]

[bold yellow]"Nah! We'll start with one tiny line of code and build up from there. By the end, you'll be making your OWN games. Ready?"[/bold yellow]

The Python snake winks and slithers toward the first zone.
Let's follow it!
"""

ZONE_INTROS = {
    "hello_world": (
        "[bold cyan]HELLO WORLD STATION[/bold cyan]\n\n"
        "Puck hops onto a giant PRINT button. "
        "[bold yellow]'Every programmer's journey starts with these two words: Hello, world! "
        "Let's learn how to make Python talk — using print, strings, and input!'[/bold yellow]"
    ),
    "variables_math": (
        "[bold cyan]THE NUMBER FORGE[/bold cyan]\n\n"
        "Puck picks up a little box labelled [bold green]'score'[/bold green] and drops a shiny 10 inside. "
        "[bold yellow]'Variables are named boxes that hold values. "
        "And once you have numbers, you can do MATHS with them! "
        "Addition, subtraction, multiplication — Python handles it all!'[/bold yellow]"
    ),
    "lists_loops": (
        "[bold cyan]THE LOOP LAGOON[/bold cyan]\n\n"
        "Puck stands at the edge of a sparkling pool filled with floating items. "
        "[bold yellow]'Lists let you store LOTS of things in one place. "
        "And loops let you do something to EACH one! "
        "Together, they're one of the most powerful combos in all of programming!'[/bold yellow]"
    ),
    "if_else_adventures": (
        "[bold cyan]THE DECISION DUNGEON[/bold cyan]\n\n"
        "Puck lands at a fork where three paths glow different colours. "
        "[bold yellow]'Programs need to make CHOICES. Is the score high enough? "
        "Did the player say yes? Is it raining? "
        "If/else lets your code pick the right path — just like YOU do every day!'[/bold yellow]"
    ),
    "fun_projects": (
        "[bold cyan]THE INVENTION LAB[/bold cyan]\n\n"
        "Puck throws open the doors to a workshop full of half-built gadgets. "
        "[bold yellow]'This is it — the big one! We're going to build REAL things. "
        "Mad Libs, number guessing games, calculators, dice rollers... "
        "everything you've learned comes together RIGHT HERE!'[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "hello_world": (
        "[bold green]ZONE COMPLETE — HELLO WORLD STATION![/bold green]\n\n"
        "You can print, use strings, take input, and build greetings! "
        "The Python snake nods approvingly. "
        "[bold yellow]'Your first words in Python! This is just the beginning!'[/bold yellow]"
    ),
    "variables_math": (
        "[bold green]ZONE COMPLETE — THE NUMBER FORGE![/bold green]\n\n"
        "Variables created, maths mastered, calculators built! "
        "[bold yellow]'You can store anything, calculate anything. "
        "A programmer who understands variables understands HALF of programming!'[/bold yellow]"
    ),
    "lists_loops": (
        "[bold green]ZONE COMPLETE — THE LOOP LAGOON![/bold green]\n\n"
        "Lists collected, for loops spinning, while loops counting! "
        "[bold yellow]'You just learned one of the most powerful patterns in computing. "
        "Loops run the world — from search engines to video games!'[/bold yellow]"
    ),
    "if_else_adventures": (
        "[bold green]ZONE COMPLETE — THE DECISION DUNGEON![/bold green]\n\n"
        "Conditions checked, branches chosen, logic mastered! "
        "[bold yellow]'Your programs can now THINK and DECIDE. "
        "That makes them truly intelligent!'[/bold yellow]"
    ),
    "fun_projects": (
        "[bold green]ZONE COMPLETE — THE INVENTION LAB![/bold green]\n\n"
        "Mad Libs built, games designed, calculators wired, dice rolling! "
        "Puck does a triple backflip. "
        "[bold yellow]'You did it! You're a real Python programmer now! "
        "You can print, calculate, loop, decide, and BUILD. "
        "The whole world of coding is open to you!'[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "hello_world": (
        "[bold red]BOSS CHALLENGE — THE GREETING MACHINE[/bold red]\n\n"
        "[bold yellow]'Time to put print, input, and strings together. "
        "Can you trace through a whole program and predict the output? "
        "Let's find out!'[/bold yellow]"
    ),
    "variables_math": (
        "[bold red]BOSS CHALLENGE — THE PRICE CALCULATOR[/bold red]\n\n"
        "[bold yellow]'Multiple variables, multiplication, subtraction — "
        "all chained together. Track every value carefully "
        "and tell me: what does the program print?'[/bold yellow]"
    ),
    "lists_loops": (
        "[bold red]BOSS CHALLENGE — THE LONGEST WORD[/bold red]\n\n"
        "[bold yellow]'A loop, a list, a comparison inside — "
        "this one tests EVERYTHING you learned in this zone. "
        "Walk through it step by step. You can do this!'[/bold yellow]"
    ),
    "if_else_adventures": (
        "[bold red]BOSS CHALLENGE — THE ADVENTURE GATE[/bold red]\n\n"
        "[bold yellow]'Multiple conditions, an AND operator, elif chains — "
        "one wrong step and you'll pick the wrong path. "
        "Read carefully and think it through!'[/bold yellow]"
    ),
    "fun_projects": (
        "[bold red]BOSS CHALLENGE — BUILD THE GAME![/bold red]\n\n"
        "[bold yellow]'A real mini game — random numbers, input, if/else, and str(). "
        "Every concept from every zone, all in one program. "
        "This is the final test. You've got this!'[/bold yellow]"
    ),
}
