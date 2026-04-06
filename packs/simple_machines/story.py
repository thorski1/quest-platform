"""
story.py — Narrative for The Inventor's Workshop skill pack.

Puck leads the explorer through a workshop full of levers, wheels,
pulleys, ramps, and gears — the six simple machines that built
human civilization. For ages 5-12.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Inventor's Workshop[/bold yellow]

The Primer's pages turned to something different — not a garden
or a forest, but a [italic]workshop.[/italic]

Heavy wooden doors creaked open. Inside, gears turned slowly
on the walls. Ropes hung from pulleys on the ceiling. A ramp
of polished wood stretched across one corner, and levers
of every size lined a long workbench.

[bold cyan]"Before electricity,"[/bold cyan] Puck said, landing on a brass gear
twice his size, eyes bright with excitement.
[bold cyan]"Before engines or computers — people built
pyramids, cathedrals, castles, and bridges.
With their hands. And six simple tools."[/bold cyan]

The girl picked up a small lever and balanced it on a wooden block.
One end went down. The other went up.

[bold cyan]"Levers, wheels, pulleys, ramps, wedges, and screws.
That's all there is. Every machine ever built —
from a pair of scissors to a space shuttle —
is just some combination of those six things."[/bold cyan]

Puck grinned, wings buzzing.

[bold cyan]"Ready to learn the six secrets that built the world?"[/bold cyan]

A golden wrench appeared on the next page, glowing softly.

[bold white]Your journey through the workshop begins now.[/bold white]
"""

ZONE_INTROS = {
    "levers_and_fulcrums": """
Puck placed a long stick across a triangular block of wood.

[bold cyan]"Push down on that end,"[/bold cyan] Puck said.

The girl pushed. The other end lifted a heavy stone into the air
as easily as lifting a feather.

[bold cyan]"A stick and a balance point. That's all a lever is.
But with it — you can move the world. Archimedes said that,
and he meant it literally."[/bold cyan]

Six golden labels appeared on the workbench:
[bold yellow]Seesaws · Scissors · Catapults · Crowbars · Bottle Openers · Your Arm[/bold yellow]

[bold cyan]"All levers. Every single one. Let's find out why!"[/bold cyan]

[bold white]How do levers make hard work easy?[/bold white]
""",
    "wheels_and_axles": """
A wooden wheel sat on the workbench, a thin rod through its center.
Puck gave it a spin, and it whirred beautifully.

[bold cyan]"Before this,"[/bold cyan] Puck said, watching it turn,
[bold cyan]"people dragged everything. Imagine dragging
a cart full of stones across the ground. Your arms aching.
Your feet slipping. Terrible."[/bold cyan]

The girl winced.

[bold cyan]"Then someone — some brilliant, tired, fed-up someone —
noticed that round things roll. And [italic]everything[/italic]
changed forever."[/bold cyan]

Five golden labels appeared:
[bold yellow]Cars · Bicycles · Doorknobs · Steering Wheels · Ferris Wheels[/bold yellow]

[bold white]Why did the wheel change the world?[/bold white]
""",
    "pulleys_and_gears": """
A rope hung from the ceiling, looped over a small wheel at the top.

[bold cyan]"Pull down,"[/bold cyan] Puck said quietly.

The girl pulled the rope down, and a heavy bucket
rose smoothly off the floor — as if by magic.

[bold cyan]"You just changed the direction of force!
Instead of pushing UP — which is hard and awkward —
you pulled DOWN — which is easy, because gravity
helps you. That's the magic of a pulley."[/bold cyan]

Puck pointed to a row of gears on the wall, each one
turning the next.

[bold cyan]"And gears — gears are wheels that talk to each other.
One turns, and the next one listens."[/bold cyan]

[bold white]What can pulleys and gears lift?[/bold white]
""",
    "inclined_planes_and_wedges": """
A long wooden ramp stretched from the floor to a high table.
A heavy barrel sat at the bottom.

[bold cyan]"Could you lift that barrel straight up to the table?"[/bold cyan]
Puck asked.

The girl shook her head. It was way too heavy.

[bold cyan]"But could you push it up this ramp?"[/bold cyan]

She thought about it. Slowly... maybe. Yes!

[bold cyan]"A ramp spreads the work over distance.
Instead of one big lift, you do many small pushes.
And a wedge? A wedge is a ramp that [italic]moves[/italic] —
it pushes into things and forces them apart."[/bold cyan]

Puck held up a tiny axe and a doorstop.

[bold cyan]"Both wedges. Both brilliant."[/bold cyan]

[bold white]Where are all the ramps and wedges hiding?[/bold white]
""",
    "compound_machines": """
[bold cyan]"Now,"[/bold cyan] Puck said, stepping back to reveal
the entire workshop at once.

Levers connected to wheels connected to pulleys
connected to gears. Everything moved together
in one grand, clicking, turning, lifting dance.

[bold cyan]"You know the six building blocks now.
Levers. Wheels. Pulleys. Ramps. Wedges. Screws.
But here's the real secret —"[/bold cyan]

Puck's eyes sparkled.

[bold cyan]"Nobody uses just [italic]one[/italic]. Every machine
you've ever seen — bicycles, scissors, cars,
cranes, clocks, can openers — is just simple
machines working [italic]together[/italic]. Once you see it,
you can't unsee it."[/bold cyan]

[bold white]What happens when simple machines team up?[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "levers_and_fulcrums": """
[bold green]The lever workbench glows with golden light![/bold green]

The girl balanced the lever perfectly. The heavy stone floated
in the air like it weighed nothing.

[bold cyan]"You understand levers now,"[/bold cyan] Puck said proudly.
[bold cyan]"A stick, a fulcrum, and the power to move
anything. Seesaws, scissors, catapults —
all just levers in disguise."[/bold cyan]

The next workbench begins to glow. Wheels are waiting...
""",
    "wheels_and_axles": """
[bold green]The wheels spin and the workshop hums![/bold green]

Every wheel in the room started turning — big ones slowly,
small ones quickly, all connected by invisible energy.

[bold cyan]"Wheels changed everything,"[/bold cyan] Puck said.
[bold cyan]"Without them, there would be no cars, no bicycles,
no clocks, no gears. The wheel is humanity's
greatest invention."[/bold cyan]

A rope dangles from the ceiling. The pulleys are calling...
""",
    "pulleys_and_gears": """
[bold green]The lifting tower raises its flag![/bold green]

The girl pulled the rope and a banner unfurled at the top
of the workshop: a golden gear on a blue field.

[bold cyan]"Pulleys and gears,"[/bold cyan] Puck said warmly.
[bold cyan]"They lift what we can't carry.
They turn what we can't reach.
From flagpoles to elevators to cranes —
pulleys and gears do the heavy lifting."[/bold cyan]

A long wooden ramp gleams in the next room...
""",
    "inclined_planes_and_wedges": """
[bold green]The ramp room gleams with understanding![/bold green]

The girl pushed a heavy barrel up the ramp with one hand.
Easy.

[bold cyan]"Ramps built the pyramids,"[/bold cyan] Puck said softly.
[bold cyan]"Wedges split logs, cut food, and open doors.
Screws are just ramps wrapped in spirals.
The inclined plane is everywhere."[/bold cyan]

The whole workshop begins to move at once. The final challenge awaits...
""",
    "compound_machines": """
[bold green]The Grand Workshop blazes with light![/bold green]

Every machine in the room moved at once — levers lifting,
wheels spinning, pulleys pulling, gears turning,
ramps sliding, wedges splitting.

All of it connected. All of it working together.

[bold cyan]"You did it,"[/bold cyan] Puck said quietly, and there was
real pride in those bright eyes.
[bold cyan]"You understand the six simple machines
that built human civilization. Lever. Wheel and axle.
Pulley. Inclined plane. Wedge. Screw.
Every machine ever made is just a combination
of these six ideas."[/bold cyan]

Puck smiled.

[bold cyan]"Next time you see a bicycle, a crane,
a pair of scissors — you'll know exactly
what's happening inside. And that knowledge?
That's yours forever."[/bold cyan]

[bold white]Master Builder. Workshop Champion. Inventor. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "levers_and_fulcrums": "A giant catapult stands at the end of the workshop, loaded and ready. Puck's eyes are wide with excitement. [bold yellow]\"This is the ultimate lever challenge. Think about everything you've learned about levers and fulcrums!\"[/bold yellow]",
    "wheels_and_axles": "A massive Ferris wheel model turns slowly on the workbench, lights twinkling. [bold yellow]\"The biggest wheel and axle challenge! Think about what holds everything together and lets it spin.\"[/bold yellow]",
    "pulleys_and_gears": "A model crane towers over the workshop floor, cables taut. [bold yellow]\"How does this crane lift things that weigh more than a car? You know the answer — you've been learning it all along!\"[/bold yellow]",
    "inclined_planes_and_wedges": "A small rubber wedge sits under a heavy iron door. Puck points at it in amazement. [bold yellow]\"Such a tiny thing holding such a heavy door. How does it do it? This is your final ramp and wedge challenge!\"[/bold yellow]",
    "compound_machines": "A deep well with a bucket and crank stands in the center of the workshop. Water glints far below. [bold yellow]\"Your final challenge: design the perfect machine to lift water from the deep. Everything you've learned comes together here!\"[/bold yellow]",
}
