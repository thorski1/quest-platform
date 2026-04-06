"""
story.py — Narrative for The Robot Factory (Robotics) skill pack.
"""

INTRO_STORY = """
[bold cyan]Welcome to The Robot Factory![/bold cyan]

Puck zips through a doorway into an enormous workshop filled with gears, wires, and half-built machines.

[bold yellow]"Whoa! Look at this place!"[/bold yellow] Puck squeaks, landing on a workbench next to a small robot arm.

The arm twitches once — then freezes.

[bold yellow]"These robots were being built by the greatest inventor in the land, but she left before finishing them. The instructions are incomplete. The sensors are disconnected. The motors just... sit there."[/bold yellow]

You pick up a tiny wheel and spin it between your fingers.

[bold white]"So we need to finish building them?"[/bold white]

[bold yellow]"Even better — we need to UNDERSTAND them! How they sense, how they think, how they move. Once you understand robots, you can build ANYTHING!"[/bold yellow]

Puck hops onto the little robot arm. It buzzes to life for just a second, then goes still again.

[bold yellow]"Five workshops. Five big ideas. By the end, you'll know more about robots than most grown-ups. Ready?"[/bold yellow]

The factory hums with possibility.
Let's power it up.
"""

ZONE_INTROS = {
    "what_is_a_robot": (
        "[bold cyan]WORKSHOP 1 — WHAT IS A ROBOT?[/bold cyan]\n\n"
        "Puck picks up a magnifying glass and peers at the frozen robot arm. "
        "[bold yellow]'Before we can build anything, we need to answer the BIG question: "
        "what actually makes something a robot? Is a toaster a robot? "
        "Is a remote-control car? Let's find out!'[/bold yellow]"
    ),
    "robot_parts": (
        "[bold cyan]WORKSHOP 2 — ROBOT PARTS[/bold cyan]\n\n"
        "Puck opens a huge drawer full of motors, gears, wheels, and wires. "
        "[bold yellow]'A robot is only as good as its parts! Motors for moving, sensors for seeing, "
        "batteries for energy. Today we take robots apart — piece by piece — "
        "and learn what every part does!'[/bold yellow]"
    ),
    "programming_robots": (
        "[bold cyan]WORKSHOP 3 — PROGRAMMING ROBOTS[/bold cyan]\n\n"
        "Puck taps a small screen that flickers to life with green text. "
        "[bold yellow]'A robot without a program is just a pile of parts. "
        "The program is the BRAIN — it tells the robot what to sense, what to decide, "
        "and what to do. Today you learn to think like a robot programmer!'[/bold yellow]"
    ),
    "robots_in_the_real_world": (
        "[bold cyan]WORKSHOP 4 — ROBOTS IN THE REAL WORLD[/bold cyan]\n\n"
        "Puck unrolls a giant map covered in tiny robot stickers. "
        "[bold yellow]'Robots aren't just in movies! They're in factories, hospitals, "
        "the deep ocean, and even on MARS. Let's travel the world and discover "
        "all the amazing places robots are already working!'[/bold yellow]"
    ),
    "future_of_robots": (
        "[bold cyan]WORKSHOP 5 — FUTURE OF ROBOTS[/bold cyan]\n\n"
        "Puck puts on tiny futuristic goggles. "
        "[bold yellow]'Self-driving cars! Swarm robots! Drones delivering packages! "
        "The future is WILD. But with great power comes great responsibility — "
        "we also need to think about what's fair, what's safe, and what's right. "
        "Ready for the final workshop?'[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "what_is_a_robot": (
        "[bold green]WORKSHOP COMPLETE — WHAT IS A ROBOT?[/bold green]\n\n"
        "You understand sensors, actuators, and the Sense-Think-Act loop. "
        "The frozen arm gives a tiny wave. [bold yellow]'Now you know what makes a robot a ROBOT!'[/bold yellow]"
    ),
    "robot_parts": (
        "[bold green]WORKSHOP COMPLETE — ROBOT PARTS![/bold green]\n\n"
        "Motors, wheels, grippers, cameras, batteries — you know them all! "
        "Puck tightens a tiny bolt proudly. [bold yellow]'You could build a robot from scratch now!'[/bold yellow]"
    ),
    "programming_robots": (
        "[bold green]WORKSHOP COMPLETE — PROGRAMMING ROBOTS![/bold green]\n\n"
        "Step-by-step instructions, loops, conditionals, sensor logic — you think like a programmer! "
        "[bold yellow]'The robots are listening to YOU now. That's real power!'[/bold yellow]"
    ),
    "robots_in_the_real_world": (
        "[bold green]WORKSHOP COMPLETE — ROBOTS IN THE REAL WORLD![/bold green]\n\n"
        "Factories, hospitals, space, oceans, farms — robots are everywhere! "
        "[bold yellow]Puck sticks a gold star on the map.[/bold yellow] "
        "[bold yellow]'You've seen how robots are changing the world. Pretty amazing, right?'[/bold yellow]"
    ),
    "future_of_robots": (
        "[bold green]WORKSHOP COMPLETE — FUTURE OF ROBOTS![/bold green]\n\n"
        "Self-driving cars, drones, swarms, ethics, privacy — you've thought about it all! "
        "[bold yellow]Puck does a tiny robot dance.[/bold yellow] "
        "[bold yellow]'You finished the ENTIRE Robot Factory! You now understand robots better "
        "than most adults. That is seriously impressive!'[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "what_is_a_robot": (
        "[bold red]BOSS CHALLENGE — THE ROBOT TEST[/bold red]\n\n"
        "[bold yellow]'Time to prove you know what a robot really is. "
        "Sensors, actuators, AI, pre-programmed — show me you understand it all!'[/bold yellow]"
    ),
    "robot_parts": (
        "[bold red]BOSS CHALLENGE — THE ASSEMBLY LINE[/bold red]\n\n"
        "[bold yellow]'A robot needs to be built for a special mission. "
        "You pick the parts — motors, sensors, grippers. Choose wisely!'[/bold yellow]"
    ),
    "programming_robots": (
        "[bold red]BOSS CHALLENGE — THE GLITCHY ROBOT[/bold red]\n\n"
        "[bold yellow]'A robot is misbehaving! Its program has bugs and its logic is tangled. "
        "Read the code, find the errors, and think like a programmer!'[/bold yellow]"
    ),
    "robots_in_the_real_world": (
        "[bold red]BOSS CHALLENGE — MISSION CONTROL[/bold red]\n\n"
        "[bold yellow]'A Mars rover has lost contact with Earth. A surgical robot needs a new sensor. "
        "A rescue drone is heading into a storm. Make the right calls!'[/bold yellow]"
    ),
    "future_of_robots": (
        "[bold red]BOSS CHALLENGE — DESIGN THE FUTURE[/bold red]\n\n"
        "[bold yellow]'The hardest questions don't have easy answers. "
        "Self-driving cars, robot jobs, privacy, fairness — "
        "show me you can think about technology AND humanity!'[/bold yellow]"
    ),
}
