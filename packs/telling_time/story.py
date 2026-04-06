"""
story.py — Narrative for the Time & Calendar skill pack.

Puck opens the Primer's Clock Tower and guides the reader through
telling time, days, months, seasons, elapsed time, calendars,
and time zones around the world.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Clock Tower[/bold yellow]

A new page turned in the Primer, and a sound filled the air that
the girl had never heard before — a deep, steady ticking, like
the heartbeat of something very old and very wise.

[bold cyan]"Do you hear that?"[/bold cyan] Puck appeared on a ledge high above,
silhouetted against an enormous clock face that glowed with
golden light. Gears turned behind the glass. Pendulums swung
in slow, perfect arcs.

[bold cyan]"This is the Clock Tower,"[/bold cyan] Puck said, spreading wings wide.
[bold cyan]"Every tick and tock tells a story. Hours, minutes, days,
months, seasons — all of time lives here, turning like
the gears of this great machine."[/bold cyan]

The girl looked up at the vast clock face, its hands moving
with quiet purpose. [bold white]"Can you teach me to read it?"[/bold white]

Puck grinned and swooped down to land on the minute hand.

[bold cyan]"I can teach you all of it. How to read a clock.
Why morning is different from night. The names of every
day and every month. How to figure out how long things take.
How to read a calendar. And even why it's bedtime here
when children on the other side of the world are waking up."[/bold cyan]

The great clock chimed once — a warm, golden sound.

[bold cyan]"Ready? The Clock Tower is open."[/bold cyan]

[bold white]Your journey through time begins now.[/bold white]
"""

ZONE_INTROS = {
    "telling_time": """
Puck landed on the rim of the great clock face and pointed to
the two hands — one short, one long — sweeping around the dial.

[bold cyan]"Two hands,"[/bold cyan] Puck said. [bold cyan]"That's the secret.
The short one tells you the hour. The long one tells you
the minutes. Once you understand these two, you can read
any clock in the world."[/bold cyan]

The numbers 1 through 12 glowed around the clock face:
[bold yellow]O'clock · Half Past · Quarter Past · Quarter To[/bold yellow]

[bold white]Let's learn to read the clock![/bold white]
""",
    "am_and_pm": """
The clock tower windows shifted — one side bright with morning
sunlight, the other dark with twinkling stars.

[bold cyan]"The clock goes around twice every day,"[/bold cyan] Puck explained.
[bold cyan]"Once for the morning — that's AM — and once for
the afternoon and night — that's PM. Two little letters
that tell you which half of the day you're in."[/bold cyan]

Two golden letters hung in the air:
[bold yellow]AM — Before Noon  ·  PM — After Noon[/bold yellow]

[bold white]Let's learn the difference between AM and PM![/bold white]
""",
    "days_of_week": """
Puck flew to a new wall of the tower where seven banners
hung in a row, each a different colour, each with a name
stitched in silver thread.

[bold cyan]"Seven days,"[/bold cyan] Puck said, touching each banner in turn.
[bold cyan]"Monday, Tuesday, Wednesday, Thursday, Friday,
Saturday, Sunday. Seven days make one week — and the weeks
just keep rolling, one after another, forever."[/bold cyan]

The seven banners fluttered:
[bold yellow]Mon · Tue · Wed · Thu · Fri · Sat · Sun[/bold yellow]

[bold white]Let's learn the seven days![/bold white]
""",
    "months_and_seasons": """
Puck opened a tall door in the tower to reveal a circular room
with twelve stained-glass windows, each showing a different scene —
snow, blossoms, sunshine, falling leaves, and back to snow again.

[bold cyan]"Twelve months,"[/bold cyan] Puck said softly. [bold cyan]"Each one has its own
personality. January is cold and quiet. July is warm and long.
September smells like new pencils and fresh starts."[/bold cyan]

The twelve windows glowed in order:
[bold yellow]Jan · Feb · Mar · Apr · May · Jun · Jul · Aug · Sep · Oct · Nov · Dec[/bold yellow]

[bold white]Let's explore the twelve months and four seasons![/bold white]
""",
    "elapsed_time": """
Puck pulled out two pocket watches and held them side by side.

[bold cyan]"Sometimes,"[/bold cyan] Puck said, [bold cyan]"you need to know how much time
has passed between two moments. How long was the movie?
How long until dinner? How many minutes until the bus comes?"[/bold cyan]

Puck clicked both watches. One started at 2:00, the other at 3:30.

[bold cyan]"This is time math — and it's easier than you think.
You just count the hours and minutes between two times."[/bold cyan]

[bold white]Let's learn to calculate elapsed time![/bold white]
""",
    "calendars": """
Puck unfurled an enormous calendar across the tower floor —
rows and columns stretching out like a great grid, each square
holding a number.

[bold cyan]"A calendar,"[/bold cyan] Puck said, [bold cyan]"is a map of time.
Instead of showing places, it shows days. Each row is a week.
Each column is a day of the week. And if you can read it,
you can find any date, count the days until anything,
and plan adventures weeks ahead."[/bold cyan]

[bold white]Let's learn to read the calendar![/bold white]
""",
    "time_around_world": """
The highest room in the Clock Tower had no walls — only windows
in every direction, and through each one, a different sky.
Through one, a sunrise. Through another, a bright afternoon.
Through a third, a deep, starry night.

[bold cyan]"Right now,"[/bold cyan] Puck whispered, [bold cyan]"at this very moment —
children in one country are eating breakfast, children in another
are playing at recess, and children somewhere else are fast asleep."[/bold cyan]

Twenty-four clocks circled the room, each showing a different hour:
[bold yellow]New York · London · Tokyo · Sydney · Cairo · Mumbai[/bold yellow]

[bold cyan]"Same moment. Different times. That's the magic of time zones."[/bold cyan]

[bold white]Let's discover how time works around the world![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "telling_time": """
[bold green]The great clock face glows with understanding![/bold green]

Hour hand, minute hand, o'clock, half past, quarter past,
quarter to — every position on the dial is yours.

[bold cyan]"You can read a clock,"[/bold cyan] Puck says proudly.
[bold cyan]"Any clock, anywhere — on a wall, on a wrist,
on a tower. The two hands have no more secrets from you."[/bold cyan]

The tower windows brighten and darken. AM and PM await...
""",
    "am_and_pm": """
[bold green]The tower shines — half in daylight, half in starlight![/bold green]

AM and PM, noon and midnight, the 24-hour rhythm of the day —
all of it clear as the clock's chime.

[bold cyan]"You know the whole day now,"[/bold cyan] Puck says.
[bold cyan]"Morning, afternoon, evening, night — and the exact moment
when one becomes the other."[/bold cyan]

Seven coloured banners flutter on the wall. The days of the week are calling...
""",
    "days_of_week": """
[bold green]Seven banners wave in perfect order![/bold green]

Monday through Sunday, weekdays and weekends,
the endless cycle of the seven-day week.

[bold cyan]"You know the rhythm of the week,"[/bold cyan] Puck says.
[bold cyan]"Every culture on Earth follows these seven days.
Now you can count forward, count backward,
and always know what day is coming next."[/bold cyan]

Twelve stained-glass windows begin to glow. The months and seasons are next...
""",
    "months_and_seasons": """
[bold green]Twelve windows blaze with colour — every month alive![/bold green]

January's snow, April's rain, July's sunshine, October's gold —
all twelve months in order, each one with its season.

[bold cyan]"You know the year now,"[/bold cyan] Puck says warmly.
[bold cyan]"Twelve months. Four seasons. The great wheel that turns
from January back to January, year after year."[/bold cyan]

Two pocket watches begin to tick. Elapsed time awaits...
""",
    "elapsed_time": """
[bold green]The pocket watches click in perfect sync![/bold green]

Hours, half hours, minutes — you can calculate how long
anything takes, from a cartoon to a car ride.

[bold cyan]"Time math,"[/bold cyan] Puck says with admiration.
[bold cyan]"You can figure out how long things take. That's a skill
that will help you every single day of your life."[/bold cyan]

A great calendar unfurls across the tower floor. Let's learn to read it...
""",
    "calendars": """
[bold green]The calendar glows — every date findable, every week countable![/bold green]

Rows and columns, weeks and days, counting forward and backward
through the grid of time.

[bold cyan]"You can read a calendar like a pro,"[/bold cyan] Puck says.
[bold cyan]"Find any date, count any number of days,
and plan ahead like a true time keeper."[/bold cyan]

The tower's highest room awaits. Time zones and the whole wide world...
""",
    "time_around_world": """
[bold green]Twenty-four clocks glow around the tower — every time zone alight![/bold green]

New York and London and Tokyo and Sydney, all ticking
at the same moment but showing different hours.

[bold cyan]"You've done it."[/bold cyan] Puck's wings spread wide.
[bold cyan]"Clocks, hours, days, months, seasons, calendars, time zones —
the whole great clockwork of time. You understand it all."[/bold cyan]

The Clock Tower chimes twelve golden notes.

[bold white]Time Keeper. Clock Reader. Calendar Master. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "telling_time": "The great tower clock's hands spin and stop in a tricky position. Puck points upward. [bold yellow]\"Read both hands carefully — the hour hand and the minute hand. What time does the tower show?\"[/bold yellow]",
    "am_and_pm": "The tower lights flicker between day and night. Puck stands at the edge of midnight. [bold yellow]\"This is the trickiest moment of the whole day — when PM ends and AM begins. Think carefully!\"[/bold yellow]",
    "days_of_week": "The seven banners spin in a circle. Puck calls out from the whirlwind. [bold yellow]\"Days move in circles — count forward and tell me where you land!\"[/bold yellow]",
    "months_and_seasons": "The stained-glass windows split — half showing snow, half showing sunshine. Puck stands in the middle. [bold yellow]\"Same month, two hemispheres, two different seasons. Which is which?\"[/bold yellow]",
    "elapsed_time": "Puck holds up two pocket watches showing different times and a museum ticket. [bold yellow]\"From arrival to departure — how long were you there? Count carefully!\"[/bold yellow]",
    "calendars": "The calendar lights up with glowing dates. Puck flies from one to another. [bold yellow]\"Use the seven-day pattern — can you figure out the day of the week?\"[/bold yellow]",
    "time_around_world": "Clocks from every city light up at once. Puck spins the globe. [bold yellow]\"New York, London — five hours apart. Same moment, different clocks. What does London's say?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "clock_reader": (
        "Clock Reader",
        "Read the hour hand, minute hand, and every position on the clock face!",
    ),
    "day_night_knower": (
        "Day & Night Knower",
        "Mastered AM and PM, noon and midnight!",
    ),
    "week_walker": (
        "Week Walker",
        "Learned all seven days and their perfect order!",
    ),
    "season_keeper": (
        "Season Keeper",
        "Named every month and matched them to their seasons!",
    ),
    "time_mathematician": (
        "Time Mathematician",
        "Calculated elapsed time like a true clockmaker!",
    ),
    "calendar_master": (
        "Calendar Master",
        "Read calendars, found dates, and counted days with ease!",
    ),
    "world_clock_keeper": (
        "World Clock Keeper",
        "Understood time zones and why the world ticks at different hours!",
    ),
}
