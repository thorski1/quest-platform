"""
story.py — Narrative for the Colors & Shapes skill pack.

Long Long guides you through the colorful world of Chinese,
from basic colors to cultural symbolism.
"""

INTRO_STORY = """
[bold red]LEARN CHINESE[/bold red]
[bold yellow]Chapter: Colors & Shapes[/bold yellow]

Long Long the dragon soared over a vast medieval marketplace,
where silk banners in every hue rippled in the wind. Red lanterns
swayed from timber beams, golden characters gleamed on shop signs,
and bolts of green, purple, and blue silk spilled from merchant stalls.

[bold cyan]"Look at this world,"[/bold cyan] Long Long said, banking low over the
square. [bold cyan]"Every color has a name, and in Chinese, every color
tells a story. Red isn't just red -- it's luck, joy, celebration.
White isn't just white -- it carries the weight of farewell."[/bold cyan]

The dragon landed beside a painter's workshop where an old master
was mixing pigments -- vermillion, indigo, ochre, ink-black.

[bold cyan]"Colors are one of the first things children learn in any language,
but in Chinese they unlock something deeper: culture, history,
and a way of seeing the world that's thousands of years old."[/bold cyan]

Long Long picked up a brush and painted a single red circle.

[bold cyan]"We'll start with the basics -- six colors that form the foundation.
Then we'll expand your palette, learn shapes, build descriptions,
and discover what colors really mean in Chinese culture."[/bold cyan]

Long Long spread both wings wide, each scale reflecting a different color.

[bold cyan]"Ready to paint your first words?"[/bold cyan]

[bold white]Your journey into the colorful world of Chinese begins now.[/bold white]
"""

ZONE_INTROS = {
    "basic_colors": """
Long Long stood before six large silk banners hanging from a castle wall,
each a different color: red, blue, green, yellow, white, and black.

[bold cyan]"These are the six colors every Chinese learner must know first,"[/bold cyan]
Long Long said, pointing a golden claw at each banner in turn.
[bold cyan]"Hong, lan, lv, huang, bai, hei -- six words that let you
describe almost anything you see. And each one carries
a thousand years of meaning."[/bold cyan]

[bold white]Let's learn the six foundational colors of Chinese![/bold white]
""",
    "more_colors": """
Long Long led you into a royal dye workshop where artisans
were mixing pigments in stone bowls -- deep purple, soft pink,
warm orange, cool gray, earthy brown.

[bold cyan]"Six colors is a good start, but the world has more shades
than that,"[/bold cyan] Long Long said. [bold cyan]"Purple for royalty, orange for autumn,
pink for blossoms, gray for stone, brown for earth.
And once you learn 'shen' and 'qian', you can make
any shade darker or lighter."[/bold cyan]

[bold white]Let's expand your color vocabulary![/bold white]
""",
    "shapes": """
Long Long brought you to a stonemason's workshop in the castle courtyard.
Circles, squares, and triangles were carved into marble slabs.

[bold cyan]"Chinese shape words are beautifully logical,"[/bold cyan] Long Long said,
tracing a triangle in the dust. [bold cyan]"San jiao xing -- three corner shape.
See? Once you know the pattern, you can figure out
any shape just by counting corners or sides."[/bold cyan]

[bold white]Let's learn the shapes that build our world![/bold white]
""",
    "describing_with_colors": """
Long Long opened a thick scroll filled with paintings of
red flowers, blue skies, white rabbits, and green mountains.

[bold cyan]"Knowing colors and knowing nouns is one thing,"[/bold cyan] Long Long said.
[bold cyan]"But putting them together -- that's where language comes alive.
Hong hua, lan tian, bai yun... in Chinese, colors become
adjectives with a simple, elegant pattern."[/bold cyan]

[bold white]Let's learn to describe the world in color![/bold white]
""",
    "colors_in_culture": """
Long Long led you into a grand hall decorated for a festival.
Red banners with gold characters hung from every rafter.
White chrysanthemums sat in a quiet corner shrine.
A painting of the emperor in bright yellow robes dominated one wall.

[bold cyan]"Now for the real lesson,"[/bold cyan] Long Long said solemnly.
[bold cyan]"In China, colors aren't just colors -- they're symbols.
Red means luck. White means mourning. Yellow means imperial power.
And whatever you do... never give someone a green hat."[/bold cyan]

[bold white]Let's discover what colors truly mean in Chinese culture![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "basic_colors": """
[bold green]Long Long roared with delight, scales flashing crimson![/bold green]

[bold cyan]"Hong, lan, lv, huang, bai, hei -- you know them all!
Six colors, six keys to describing the world around you.
The foundation is set -- now we build."[/bold cyan]
""",
    "more_colors": """
[bold green]Long Long painted a rainbow arc across the sky![/bold green]

[bold cyan]"Purple, orange, pink, gray, brown -- and you can make
any shade lighter or darker with qian and shen.
Your palette is truly growing!"[/bold cyan]
""",
    "shapes": """
[bold green]Long Long carved a perfect star into the castle stone![/bold green]

[bold cyan]"Circles, squares, triangles, and beyond -- you've mastered
the logical system of Chinese shape words. Yuan xing, fang xing,
san jiao xing... the pattern will serve you well!"[/bold cyan]
""",
    "describing_with_colors": """
[bold green]Long Long unfurled a scroll of vivid descriptions![/bold green]

[bold cyan]"Hong hua, lan tian, bai yun, hei mao -- you can describe
the world in color now! Size before color before noun,
and the little word 'de' to connect it all. Beautiful!"[/bold cyan]
""",
    "colors_in_culture": """
[bold green]Long Long bowed with deep respect![/bold green]

[bold cyan]"You now understand what colors mean in Chinese culture --
not just their names, but their souls. Red for joy, white for grief,
yellow for royalty, green hats for... well, you know.
This knowledge will serve you far beyond vocabulary."[/bold cyan]
""",
}

BOSS_INTROS = {
    "basic_colors": """
Long Long arranged six gemstones in a line, each a different color.

[bold cyan]"You've met all six basic colors. Now prove you can tell
them apart -- no confusion, no hesitation!"[/bold cyan]
""",
    "more_colors": """
Long Long mixed paints furiously, creating complex shades.

[bold cyan]"Light pink? Dark purple? Show me you understand
not just the colors, but how to modify them!"[/bold cyan]
""",
    "shapes": """
Long Long scattered carved stone shapes across the table.

[bold cyan]"Circles, triangles, squares -- which is which?
Name them in Chinese and claim your title as Shape Sage!"[/bold cyan]
""",
    "describing_with_colors": """
Long Long conjured a scene full of colorful objects.

[bold cyan]"Describe what you see -- size, color, noun.
Stack those adjectives like a true Chinese speaker!"[/bold cyan]
""",
    "colors_in_culture": """
Long Long set the scene for a grand Chinese celebration.

[bold cyan]"The ultimate cultural test. What to wear, what to avoid,
what colors mean in the moments that matter most.
Show me you truly understand."[/bold cyan]
""",
}
