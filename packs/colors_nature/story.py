"""
story.py — Narrative for the Colors & Nature skill pack.

Umi (海) guides you through the colors and natural beauty of Japan,
from basic colors through seasons and scenic descriptions.
"""

INTRO_STORY = """
[bold red]LEARN JAPANESE[/bold red]
[bold yellow]Chapter: Colors & Nature[/bold yellow]

A gentle breeze carried the scent of salt and pine as you arrived
at a coastal trail winding between ocean and forest.

A figure stood at the trailhead, wearing a deep blue jacket
the exact shade of the sea behind her.

[bold cyan]"I'm Umi,"[/bold cyan] she said, gesturing to the panorama of colors
stretching from shoreline to mountain peak.

[bold cyan]"In Japanese, colors aren't just labels.
Some are adjectives that change form. Others are nouns
that need particles to describe things.
And nature -- 山, 海, 花, 空, 木 -- these words
are woven into everyday life and poetry."[/bold cyan]

Umi picked up a red maple leaf and held it against the blue sky.

[bold cyan]"We'll start with basic colors, learn how they work
as adjectives, explore nature vocabulary, travel through
the four seasons, and finally put it all together
to describe the world around you."[/bold cyan]

She smiled and began walking the trail.

[bold cyan]"Let's paint the world with words."[/bold cyan]

[bold white]Your journey into Japanese colors and nature begins now.[/bold white]
"""

ZONE_INTROS = {
    "basic_colors": """
Umi spread six colored stones on a flat rock by the shore.

[bold cyan]"These are the essential colors,"[/bold cyan] Umi said.
[bold cyan]"赤い (red), 青い (blue), 緑 (green), 黄色い (yellow),
白い (white), 黒い (black). Learn these and you can
describe almost anything you see."[/bold cyan]

[bold white]Let's learn the basic colors![/bold white]
""",
    "i_na_adjectives": """
Umi drew two columns in the sand: い and な.

[bold cyan]"Not all color words work the same way,"[/bold cyan] Umi explained.
[bold cyan]"赤い is an i-adjective -- it connects directly to nouns.
But 緑 is a noun-color and needs の. And some words like
きれい look like i-adjectives but are actually na-adjectives.
This matters for grammar."[/bold cyan]

[bold white]Let's master the grammar of color adjectives![/bold white]
""",
    "nature_words": """
Umi led you along a trail that passed through every landscape.

[bold cyan]"Japan's beauty comes from its nature,"[/bold cyan] Umi said.
[bold cyan]"山 (mountain), 海 (ocean), 花 (flower), 空 (sky),
木 (tree), 川 (river), 森 (forest) -- these kanji
appear everywhere, from place names to poetry.
Many of them are pictographic -- they look like what
they represent."[/bold cyan]

[bold white]Let's explore nature vocabulary![/bold white]
""",
    "seasons": """
Umi opened a folding screen painted with four panels.

[bold cyan]"Japan treasures its four seasons -- 四季 (shiki),"[/bold cyan]
Umi said reverently. [bold cyan]"春 (spring) brings cherry blossoms,
夏 (summer) brings festivals and fireworks,
秋 (autumn) brings red and gold leaves,
冬 (winter) brings snow and hot springs.
Seasons shape everything in Japanese culture."[/bold cyan]

[bold white]Let's journey through the four seasons![/bold white]
""",
    "describing_scenery": """
Umi handed you a blank sketchbook and a pen.

[bold cyan]"Now we put it all together,"[/bold cyan] Umi said.
[bold cyan]"Colors plus nature plus adjectives equals
the ability to describe any scene.
青い海はきれいです -- the blue ocean is beautiful.
高い山 -- a tall mountain. 静かな森 -- a quiet forest.
These patterns will let you paint with words."[/bold cyan]

[bold white]Let's learn to describe scenery in Japanese![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "basic_colors": """
[bold green]Umi arranged the colored stones into a rainbow![/bold green]

[bold cyan]"You know the essential colors now. Red, blue, green,
yellow, white, black -- the building blocks of description.
Remember: most are i-adjectives, but 緑 is different."[/bold cyan]
""",
    "i_na_adjectives": """
[bold green]Umi drew a checkmark in each column of the sand![/bold green]

[bold cyan]"You understand how color adjectives work in Japanese grammar.
I-adjectives connect directly, na-adjectives need な,
and noun-colors use の. This knowledge is the foundation
for building real Japanese sentences."[/bold cyan]
""",
    "nature_words": """
[bold green]Umi sketched the kanji for each nature word in the air![/bold green]

[bold cyan]"Mountain, ocean, flower, sky, tree, river, forest --
you've learned the vocabulary of the natural world.
These kanji are beautiful in their simplicity,
and you'll see them everywhere in Japan."[/bold cyan]
""",
    "seasons": """
[bold green]Umi closed the four-panel screen with a satisfied nod![/bold green]

[bold cyan]"You've traveled through all four seasons.
春, 夏, 秋, 冬 -- each one with its own colors,
traditions, and beauty. Understanding seasons
is understanding Japanese culture itself."[/bold cyan]
""",
    "describing_scenery": """
[bold green]Umi held up your completed sketchbook with pride![/bold green]

[bold cyan]"You can describe the world in Japanese now.
Colors, nature, adjectives, sentence patterns --
you've combined them all. The blue ocean, the tall mountain,
the quiet forest -- you can paint any scene with words."[/bold cyan]
""",
}

BOSS_INTROS = {
    "basic_colors": """
Umi held up a color chart with all six colors.

[bold cyan]"You've seen them all. Now tell me --
which one breaks the pattern? Show me you understand
not just the words, but how they work."[/bold cyan]
""",
    "i_na_adjectives": """
Umi wrote four sentences on a board by the shore.

[bold cyan]"Only one of these is grammatically correct.
I-adjectives, na-adjectives, noun-colors --
show me you can tell them apart."[/bold cyan]
""",
    "nature_words": """
Umi pointed to a compound word in the distance.

[bold cyan]"Japanese combines nature kanji into beautiful new words.
花火 -- what do you think 'flower fire' means?
Show me you can read between the characters."[/bold cyan]
""",
    "seasons": """
Umi held up four cards, each with a season's kanji.

[bold cyan]"Put them in order. Simple, but fundamental.
春, 夏, 秋, 冬 -- the cycle of the year."[/bold cyan]
""",
    "describing_scenery": """
Umi presented a complex scene: forest, mountain, and ocean.

[bold cyan]"Describe it all in one correct sentence.
Combine a na-adjective, a noun-color, and the right particles.
This is the final test of everything you've learned."[/bold cyan]
""",
}
