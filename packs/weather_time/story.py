"""
story.py — Narrative for the Weather & Time skill pack.

Long Long guides you through the world of weather and time in Chinese,
from basic weather words to making plans with friends.
"""

INTRO_STORY = """
[bold red]LEARN CHINESE[/bold red]
[bold yellow]Chapter: Weather & Time[/bold yellow]

Long Long the dragon circled above an ancient castle, where a great
stone sundial stood in the courtyard and weather vanes spun on every
tower. Storm clouds gathered in the west while golden sunlight still
bathed the eastern battlements.

[bold cyan]"Every morning, the first thing people ask is about the weather
and the time,"[/bold cyan] Long Long said, landing beside the sundial.
[bold cyan]"Tian qi zen me yang? Ji dian le? These are the questions
that start every conversation, plan every journey, shape every day."[/bold cyan]

A castle guard hurried past, glancing at the darkening sky and then
at the water clock on the wall.

[bold cyan]"In Chinese, weather words paint a picture -- rain falls,
snow falls, the sky clears. Time is counted in points and small hours.
Days follow a numbered cycle, and months track the moon."[/bold cyan]

Long Long traced a circle around the sundial with one golden claw.

[bold cyan]"We'll start with weather -- hot, cold, rain, snow, sunshine.
Then seasons, the rhythm of the year. Next, telling time like a native.
After that, days and months. And finally, we'll put it all together
to make plans -- because language exists to connect with others."[/bold cyan]

Long Long spread his wings wide against the changing sky.

[bold cyan]"Ready to read the heavens and master time itself?"[/bold cyan]

[bold white]Your journey into weather and time in Chinese begins now.[/bold white]
"""

ZONE_INTROS = {
    "weather_words": """
Long Long stood on the castle's highest tower, where flags
snapped in the wind and clouds raced across the sky.

[bold cyan]"The weather changes everything -- what you wear, where you go,
how you feel,"[/bold cyan] Long Long said, watching a rainstorm approach
from the mountains. [bold cyan]"In Chinese, weather words are vivid.
Rain doesn't just happen -- it 'falls down.' The sky doesn't just
clear up -- it 'becomes sunny.' Let's learn the words that
describe the world above our heads."[/bold cyan]

[bold white]Let's learn essential weather vocabulary![/bold white]
""",
    "seasons": """
Long Long led you through a magical courtyard where four gardens
existed side by side -- one blooming with spring flowers, one
blazing with summer heat, one carpeted in golden autumn leaves,
and one blanketed in winter snow.

[bold cyan]"Four seasons, four characters, four moods,"[/bold cyan]
Long Long said, breathing warmth into the winter garden.
[bold cyan]"Chun, xia, qiu, dong -- spring, summer, autumn, winter.
Each season has its own weather, its own festivals, its own
poetry. Learn the seasons and you'll understand the rhythm
of Chinese life."[/bold cyan]

[bold white]Let's master the four seasons![/bold white]
""",
    "telling_time": """
Long Long brought you to the castle's clock tower, where a massive
bronze bell marked the hours and a water clock dripped steadily
in the corner.

[bold cyan]"Ji dian le?"[/bold cyan] Long Long asked, pointing at the sundial.
[bold cyan]"That question -- 'what time is it?' -- is one you'll hear
and say a hundred times a day. Chinese time-telling is wonderfully
logical: number plus 'dian' for the hour, number plus 'fen'
for the minutes. No 'quarter to' confusion, no AM/PM --
just clean, clear numbers."[/bold cyan]

[bold white]Let's learn to tell time in Chinese![/bold white]
""",
    "days_months": """
Long Long unrolled an enormous scroll calendar across the castle's
great hall table. Each month was marked with beautiful paintings --
plum blossoms for winter, lotus flowers for summer.

[bold cyan]"Chinese calendars are elegant in their logic,"[/bold cyan]
Long Long said, running a claw along the months.
[bold cyan]"Monday is 'week-one,' January is 'month-one.'
No need to memorize twelve different month names or seven
different day names -- just learn the pattern and count.
It's one of the most learner-friendly parts of Chinese."[/bold cyan]

[bold white]Let's master days, months, and years![/bold white]
""",
    "making_plans": """
Long Long gathered a group of castle inhabitants around a table
covered with maps, weather charts, and a calendar.

[bold cyan]"Now we bring it all together,"[/bold cyan] Long Long said,
tapping the weather chart with a claw. [bold cyan]"Tomorrow,
the day after tomorrow, this weekend -- these are the words
that turn language into action. Add weather and you can make
real plans: 'If it's sunny this weekend, let's go hiking.'
That's not just vocabulary -- that's communication."[/bold cyan]

[bold white]Let's combine weather and time to make plans![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "weather_words": """
[bold green]Long Long roared with joy, sending warm gusts across the courtyard![/bold green]

[bold cyan]"Tian qi, re, leng, xia yu, xia xue, qing tian -- you command
the language of the skies! You can describe any weather now,
and that's a conversation starter anywhere in China."[/bold cyan]
""",
    "seasons": """
[bold green]Long Long soared through all four gardens in one graceful arc![/bold green]

[bold cyan]"Chun, xia, qiu, dong -- the four seasons are yours!
You understand the cycle of the year and the weather
that comes with each turn. The poets would be proud!"[/bold cyan]
""",
    "telling_time": """
[bold green]Long Long struck the great bronze bell with his tail![/bold green]

[bold cyan]"Ji dian, xiao shi, fen zhong -- you can tell time
like a native speaker! The logical beauty of Chinese time
is at your command. Never late to a dragon meeting again!"[/bold cyan]
""",
    "days_months": """
[bold green]Long Long stamped the royal seal on the calendar![/bold green]

[bold cyan]"Xing qi, yue, nian -- days, months, and years all bow
to you now. The numbered system of Chinese dates is yours.
You can schedule, plan, and navigate any calendar!"[/bold cyan]
""",
    "making_plans": """
[bold green]Long Long breathed a triumphant plume of golden fire![/bold green]

[bold cyan]"You've done it! Weather, seasons, time, dates, and now plans --
all woven together into real communication. You can check the weather,
pick a day, set a time, and make plans with anyone.
That's not just language -- that's connection."[/bold cyan]
""",
}

BOSS_INTROS = {
    "weather_words": """
Long Long conjured storm clouds and sunshine side by side.

[bold cyan]"You've learned the weather words. Now prove you can
use them in a real sentence -- describe the day,
feel the temperature, see the sky!"[/bold cyan]
""",
    "seasons": """
Long Long spun the four-season courtyard like a carousel.

[bold cyan]"Spring, summer, autumn, winter -- put them in order,
know their weather, feel their moods. Show me you understand
the rhythm of the year!"[/bold cyan]
""",
    "telling_time": """
Long Long covered the sundial and the water clock with his wings.

[bold cyan]"No peeking at the clocks! Tell me the time from memory.
Hours, minutes, half past -- prove you're the master of
Chinese time-telling!"[/bold cyan]
""",
    "days_months": """
Long Long scattered calendar pages across the great hall.

[bold cyan]"Days, months, years -- all jumbled up! Sort them out,
name them correctly, and show me you can navigate
the Chinese calendar without hesitation!"[/bold cyan]
""",
    "making_plans": """
Long Long presented a scenario: friends, weather, and a weekend.

[bold cyan]"The ultimate test -- combine everything you've learned.
Weather, time, dates, and plans. Make a real plan in Chinese
and prove you can communicate like a native speaker!"[/bold cyan]
""",
}
