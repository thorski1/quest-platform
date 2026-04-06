"""
story.py — Narrative for The Code Garden (Coding Basics) skill pack.
"""

INTRO_STORY = """
[bold cyan]Welcome to The Code Garden![/bold cyan]

Puck flutters down onto a workbench covered in gears, buttons, and blinking lights.

[bold yellow]"Oh! Oh! You came just in time!"[/bold yellow] Puck squeaks.
[bold yellow]"The Garden is full of wonderful machines — but nobody taught them what to DO!"[/bold yellow]

You look around. A little robot stands frozen in the middle of a path.
A sorting machine has stopped halfway through a pile of colorful shapes.

[bold yellow]"Machines need INSTRUCTIONS. Without them, they just... sit there."[/bold yellow]

Puck spins happily. [bold yellow]"And that's what coding is! Giving machines clear, step-by-step instructions so they can do amazing things!"[/bold yellow]

[bold white]"So I'm going to be a programmer?"[/bold white]

[bold yellow]"YOU'RE going to be a CODE GARDENER! You'll learn how programs think, how they remember things, how they make choices... and how to grow ideas into instructions!"[/bold yellow]

The frozen robot blinks, waiting.
Let's wake it up.
"""

ZONE_INTROS = {
    "what_is_coding": (
        "[bold cyan]THE CODE WORKSHOP[/bold cyan]\n\n"
        "Puck points to the frozen robot. [bold yellow]'Before we can fix anything, "
        "we need to understand: what IS a program? What IS coding? "
        "Let's start from the very beginning!'[/bold yellow]"
    ),
    "sequences_loops": (
        "[bold cyan]THE LOOP BRIDGE[/bold cyan]\n\n"
        "[bold yellow]'Sometimes we need to do the same thing over and over again. "
        "Like brushing every tooth, or watering every plant in a row. "
        "That's called a LOOP! Loops save time — and make programs much shorter!'[/bold yellow]"
    ),
    "conditionals": (
        "[bold cyan]THE CHOICE CROSSROADS[/bold cyan]\n\n"
        "[bold yellow]'Puck lands at a fork in the path. "
        "'Programs have to make DECISIONS. If it's raining, take an umbrella. "
        "If not, leave it home. An IF statement lets a program choose what to do!'[/bold yellow]"
    ),
    "variables": (
        "[bold cyan]THE MEMORY MEADOW[/bold cyan]\n\n"
        "[bold yellow]'Computers need to remember things while they work. "
        "A variable is like a little box with a label on it — "
        "you put a value inside, give it a name, and you can use it later!'[/bold yellow]"
    ),
    "functions": (
        "[bold cyan]THE FUNCTION FACTORY[/bold cyan]\n\n"
        "[bold yellow]'What if you need to do the same set of steps in lots of different places? "
        "You could write them out every time... OR you could put them in a FUNCTION! "
        "Name it once, use it anywhere!'[/bold yellow]"
    ),
    "creative_computing": (
        "[bold cyan]THE INVENTION GARDEN[/bold cyan]\n\n"
        "[bold yellow]'You've learned how programs think. Now it's time to put it all together! "
        "Real coders combine sequences, loops, conditionals, variables, and functions "
        "to build things that have never existed before. Let's invent!'[/bold yellow]"
    ),
    "debugging": (
        "[bold cyan]THE BUG LAB[/bold cyan]\n\n"
        "Puck holds up a magnifying glass. [bold yellow]'Every programmer — even the best ones — "
        "writes bugs. It's not a sign you're bad at coding. It's just part of the job! "
        "The real skill is finding them, understanding them, and squashing them. "
        "Today: you become a Bug Hunter!'[/bold yellow]"
    ),
    "data_and_lists": (
        "[bold cyan]THE DATA VAULT[/bold cyan]\n\n"
        "[bold yellow]'Programs don't just DO things — they STORE things. "
        "Numbers, names, true/false switches, whole lists of items... "
        "every piece of information a program remembers has a type and a home. "
        "Let's explore how programs organize their world!'[/bold yellow]"
    ),
    "the_internet": (
        "[bold cyan]THE NETWORK WEB[/bold cyan]\n\n"
        "Puck spreads tiny wings wide. [bold yellow]'Imagine billions of computers, "
        "all whispering to each other across cables under oceans, through satellites, "
        "bouncing signals around the entire planet in less than a second. "
        "That is the internet — and it runs on code. Let's understand it!'[/bold yellow]"
    ),
    "artificial_intelligence": (
        "[bold yellow]◈  THE THINKING MACHINE  ◈[/bold yellow]\n\n"
        "[bold cyan]Puck holds up a tiny glowing brain.[/bold cyan]\n\n"
        "[bold yellow]'Have you ever wondered how your tablet knows which song you might like?"
        " Or how a computer can recognise your face? That's AI — Artificial Intelligence!"
        " Computers learning from MILLIONS of examples to spot patterns."
        " Let's find out how — and when to trust it!'[/bold yellow]"
    ),
    "algorithms_all_around": (
        "[bold yellow]◈  THE ALGORITHM ARCADE  ◈[/bold yellow]\n\n"
        "[bold cyan]Puck stands at a tiny arcade machine full of gears.[/bold cyan]\n\n"
        "[bold yellow]'Did you know that a recipe is an algorithm?"
        " Or directions to school? Or the way a GPS finds the fastest route?"
        " Algorithms are step-by-step instructions for solving problems —"
        " and they're EVERYWHERE. Let's find them!'[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "what_is_coding": (
        "[bold green]ZONE COMPLETE — THE CODE WORKSHOP![/bold green]\n\n"
        "You understand what a program is and how computers follow instructions. "
        "The frozen robot gives a happy beep. [bold yellow]'Great start! '[/bold yellow]"
    ),
    "sequences_loops": (
        "[bold green]ZONE COMPLETE — THE LOOP BRIDGE![/bold green]\n\n"
        "Loops make sense now! Instead of writing the same thing 100 times, "
        "one loop does it all. Puck does a little dance. [bold yellow]'So efficient!'[/bold yellow]"
    ),
    "conditionals": (
        "[bold green]ZONE COMPLETE — THE CHOICE CROSSROADS![/bold green]\n\n"
        "Programs can now think for themselves — choosing the right path "
        "based on what's true. [bold yellow]'Now THAT is a smart program!'[/bold yellow]"
    ),
    "variables": (
        "[bold green]ZONE COMPLETE — THE MEMORY MEADOW![/bold green]\n\n"
        "Variables stored and retrieved perfectly. The program's memory is sharp. "
        "[bold yellow]'Nothing forgotten!'[/bold yellow]"
    ),
    "functions": (
        "[bold green]ZONE COMPLETE — THE FUNCTION FACTORY![/bold green]\n\n"
        "Functions built and ready to use anywhere. No repeated code, no wasted effort. "
        "[bold yellow]'You're thinking like a real coder!'[/bold yellow]"
    ),
    "creative_computing": (
        "[bold green]ZONE COMPLETE — THE INVENTION GARDEN![/bold green]\n\n"
        "Every concept connected, every idea transformed into logic. "
        "The Code Garden is fully awake! "
        "[bold yellow]'You did it! You're a CODE GARDENER!'[/bold yellow]"
    ),
    "debugging": (
        "[bold green]ZONE COMPLETE — THE BUG LAB![/bold green]\n\n"
        "Syntax errors, logic errors, print debugging, systematic thinking — the bugs don't stand a chance! "
        "[bold yellow]'Every professional programmer debugs every single day. "
        "Now you know how!'[/bold yellow]"
    ),
    "data_and_lists": (
        "[bold green]ZONE COMPLETE — THE DATA VAULT![/bold green]\n\n"
        "Data, lists, booleans, sorting, zero-based indexing — the vault is open! "
        "[bold yellow]'You now understand how programs store and organize everything they know. "
        "That is half of what real programming is!'[/bold yellow]"
    ),
    "the_internet": (
        "[bold green]ZONE COMPLETE — THE NETWORK WEB![/bold green]\n\n"
        "Servers, HTML, HTTPS, algorithms, phishing — you're internet-literate! "
        "[bold yellow]'The internet is humanity's greatest invention. "
        "Now you understand how it works — and how to stay safe on it.'[/bold yellow]"
    ),
    "artificial_intelligence": (
        "[bold green]ZONE COMPLETE — THE THINKING MACHINE![/bold green]\n\n"
        "Training data, bias, AI in daily life, what AI can and can't do — you understand it! "
        "[bold yellow]Puck does a little robot dance.[/bold yellow] "
        "[bold yellow]'AI is an incredible tool — and now YOU know how to think about it critically. "
        "That makes you wiser than a lot of grown-ups!'[/bold yellow]"
    ),
    "algorithms_all_around": (
        "[bold green]ZONE COMPLETE — THE ALGORITHM ARCADE![/bold green]\n\n"
        "Step-by-step instructions, sorting, searching, GPS — algorithms decoded! "
        "[bold yellow]Puck stamps a tiny gold star on the atlas.[/bold yellow] "
        "[bold yellow]'You just finished the Code Garden! Every zone, every concept — "
        "you now think like a computer scientist. That is genuinely amazing!'[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "what_is_coding": (
        "[bold red]BOSS CHALLENGE — THE PROGRAM PUZZLE[/bold red]\n\n"
        "[bold yellow]'Time to show you really understand what a program is. "
        "No hints — just you and what you've learned!'[/bold yellow]"
    ),
    "sequences_loops": (
        "[bold red]BOSS CHALLENGE — THE INFINITE LOOP BEAST[/bold red]\n\n"
        "[bold yellow]'A loop gone wrong can run forever! "
        "Show me you know how loops START, how they RUN, and how they STOP.'[/bold yellow]"
    ),
    "conditionals": (
        "[bold red]BOSS CHALLENGE — THE BIG DECISION[/bold red]\n\n"
        "[bold yellow]'A complex IF... ELSE IF... ELSE chain. "
        "Think it through one step at a time. What happens in each case?'[/bold yellow]"
    ),
    "variables": (
        "[bold red]BOSS CHALLENGE — THE VARIABLE VAULT[/bold red]\n\n"
        "[bold yellow]'Multiple variables, changing values, and a tricky question at the end. "
        "Track every change carefully!'[/bold yellow]"
    ),
    "functions": (
        "[bold red]BOSS CHALLENGE — THE MASTER FUNCTION[/bold red]\n\n"
        "[bold yellow]'Design the perfect function. What does it take in? "
        "What does it give back? Show me you understand inputs and outputs!'[/bold yellow]"
    ),
    "creative_computing": (
        "[bold red]BOSS CHALLENGE — THE GARDEN GUARDIAN[/bold red]\n\n"
        "[bold yellow]'The final challenge combines EVERYTHING. "
        "A loop, a conditional, variables, and a function all working together. "
        "Think it through — you CAN do this!'[/bold yellow]"
    ),
    "debugging": (
        "[bold red]BOSS CHALLENGE — THE BIG BUG[/bold red]\n\n"
        "[bold yellow]'A program runs but gives the wrong answer. "
        "Is it a syntax error, a logic error, or something else? "
        "Put on your detective hat — and find the bug!'[/bold yellow]"
    ),
    "data_and_lists": (
        "[bold red]BOSS CHALLENGE — THE INVENTORY[/bold red]\n\n"
        "[bold yellow]'A game character needs to store items, track a score, "
        "and remember if the door is open. "
        "What data types do you need? What structure? Show me you know!'[/bold yellow]"
    ),
    "the_internet": (
        "[bold red]BOSS CHALLENGE — DIGITAL CITIZEN[/bold red]\n\n"
        "[bold yellow]'A suspicious email. A website without HTTPS. "
        "A request for your password. "
        "You know how the internet works — now show me you know how to stay SAFE on it!'[/bold yellow]"
    ),
    "artificial_intelligence": (
        "[bold red]BOSS CHALLENGE — THE AI DETECTIVE[/bold red]\n\n"
        "[bold yellow]'An AI is used to decide who passes an exam by watching their face."
        " Is that fair? Could it make mistakes? What should a human do?"
        " You understand AI now — show me you can think about when to trust it!'[/bold yellow]"
    ),
    "algorithms_all_around": (
        "[bold red]BOSS CHALLENGE — DESIGN YOUR ALGORITHM[/bold red]\n\n"
        "[bold yellow]'You need to find the BIGGEST number in a list of 1,000 numbers."
        " There are no shortcuts — you must check every single one."
        " What is your step-by-step plan? Think carefully — this is algorithmic thinking!'[/bold yellow]"
    ),
}
