"""
story.py — Narrative for the World Religions & Beliefs skill pack.

Puck opens a glowing Book of Many Voices and guides the reader through
the world's great religions and belief systems — respectfully, warmly,
and with wonder.

Theme: "The Primer opens its Book of Many Voices — where every belief
has a story worth hearing."
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]
[bold yellow]Chapter: The Book of Many Voices[/bold yellow]

Puck appeared at the edge of a new page, carrying something the girl
had never seen before — a book within the book. Its cover shifted
between a dozen symbols: a cross, a crescent, a star, a wheel,
a flame, and more. Each one glowed softly, then faded to make room
for the next.

[bold cyan]"This,"[/bold cyan] Puck said, holding it up reverently,
[bold cyan]"is the Book of Many Voices. It holds the stories that
people tell about the biggest questions anyone ever asks:
Why are we here? What happens when we die? How should we
treat each other? What is the meaning of it all?"[/bold cyan]

The girl reached out to touch it. The cover was warm.

[bold white]"There are so many symbols,"[/bold white] she said.
[bold white]"Which one is the right one?"[/bold white]

Puck sat on the edge of the page and thought carefully.

[bold cyan]"That,"[/bold cyan] Puck said gently,
[bold cyan]"is something every person gets to decide for themselves.
But here is what I can tell you: every one of these symbols
belongs to people who are trying to understand the same big
questions — just in different ways. And every single one of them
has a story worth hearing."[/bold cyan]

The Book of Many Voices opened on its own.
The first page glowed with a soft, warm light.

[bold cyan]"We won't be choosing sides. We'll be listening.
And listening — real listening — is where all
understanding begins."[/bold cyan]

[bold white]Your journey through the world's beliefs begins now.[/bold white]
"""

ZONE_INTROS = {
    "what_is_religion": """
Puck opened the first chapter of the Book of Many Voices.
The page was covered in question marks — glowing, spinning,
rearranging themselves into pictures and then back into questions.

[bold cyan]"Before we meet any religion,"[/bold cyan] Puck said,
[bold cyan]"we need to understand what religion [italic]is.[/italic]
Why do people believe? What are sacred texts? What does prayer
mean? These are the foundations — the roots of the tree."[/bold cyan]

The question marks settled into a gentle pattern, waiting.

[bold white]Let's discover what religion means![/bold white]
""",
    "christianity": """
Puck turned to a new chapter. A gentle golden cross appeared
on the page, and the sound of distant bells echoed softly.

[bold cyan]"Christianity,"[/bold cyan] Puck said, [bold cyan]"is the world's
largest religion — over two billion people. It is built around
the teachings of a man named Jesus, who lived about two thousand
years ago. He taught about love, forgiveness, and treating every
person as your neighbour."[/bold cyan]

A figure appeared by a sunlit lake, speaking to a crowd.

[bold cyan]"Let's listen to his story."[/bold cyan]

[bold white]The Book turns to the story of Christianity.[/bold white]
""",
    "islam": """
The page turned, and a beautiful crescent moon and star
glowed against a deep blue sky. The sound of a distant
call to prayer drifted across the page.

[bold cyan]"Islam,"[/bold cyan] Puck said, [bold cyan]"means 'submission to God.'
Nearly two billion people follow it. Its prophet, Muhammad,
received the words of the Quran — and its teachings ask people
to pray, to give, to fast, and to make a journey of faith."[/bold cyan]

Five pillars of light rose from the page.

[bold cyan]"Five pillars hold up an entire way of life.
Let's learn what they are."[/bold cyan]

[bold white]The Book turns to the story of Islam.[/bold white]
""",
    "judaism": """
A six-pointed star glowed on the new page — the Star of David —
and Puck carefully unrolled a tiny scroll.

[bold cyan]"Judaism,"[/bold cyan] Puck said softly, [bold cyan]"is one of the
oldest religions still alive today — over three thousand years old.
It gave the world the idea of one God, a day of rest, and laws
about justice and kindness that still shape our world."[/bold cyan]

Two candles flickered on the page. A braided loaf of bread
appeared beside them.

[bold cyan]"A faith that has survived for millennia.
Let's hear its voice."[/bold cyan]

[bold white]The Book turns to the story of Judaism.[/bold white]
""",
    "hinduism": """
The page burst into colour — oranges and golds and reds —
and the sound of distant temple bells rang through the Book.

[bold cyan]"Hinduism,"[/bold cyan] Puck said, eyes wide with wonder,
[bold cyan]"may be the oldest religion still practiced in the world.
It comes from India and teaches about many gods, the cycle of life
and rebirth, karma, and the idea that every soul is connected
to one great spirit."[/bold cyan]

Three figures appeared — one creating, one preserving, one dancing.

[bold cyan]"A religion of a billion people and a thousand stories.
Let's begin."[/bold cyan]

[bold white]The Book turns to the story of Hinduism.[/bold white]
""",
    "buddhism": """
The page became perfectly still. A single lotus flower
bloomed in the center, and Puck sat cross-legged beside it.

[bold cyan]"Buddhism,"[/bold cyan] Puck said in a quiet voice,
[bold cyan]"was founded by a prince who gave up everything
to understand why people suffer. What he found — sitting
under a tree, perfectly still — changed the world."[/bold cyan]

A figure sat beneath a great tree, eyes closed, at peace.

[bold cyan]"This is a religion of stillness, compassion,
and the quiet mind. Let's listen carefully."[/bold cyan]

[bold white]The Book turns to the story of Buddhism.[/bold white]
""",
    "other_beliefs": """
The final chapter of the Book of Many Voices opened,
and instead of one symbol, a dozen appeared — the Khanda
of Sikhism, a Dreamtime spiral, a humanist symbol, and more.

[bold cyan]"The world's beliefs don't end with the five big religions,"[/bold cyan]
Puck said. [bold cyan]"There are Sikhs who serve free meals to anyone
who is hungry. Indigenous peoples who see every river and mountain
as sacred. People who find meaning without any religion at all.
Every one of these voices matters."[/bold cyan]

The page shimmered with many lights.

[bold cyan]"And the most important lesson of all?
How we listen to each other."[/bold cyan]

[bold white]The Book opens its final, most important chapter.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "what_is_religion": """
[bold green]The foundation is set![/bold green]

The question marks have settled into a beautiful pattern —
a tree whose roots are questions and whose branches are every
religion and belief system in the world.

[bold cyan]"Now you understand what religion is,"[/bold cyan] Puck says,
[bold cyan]"and why it matters to so many people. You're ready
to hear the individual voices."[/bold cyan]

A golden cross begins to glow on the next page...
""",
    "christianity": """
[bold green]The story of Christianity glows with warm light![/bold green]

A cross, a manger, an empty tomb, a stained-glass window —
all shining on the page, each one part of a story two billion
people hold dear.

[bold cyan]"You know the story of Jesus now,"[/bold cyan] Puck says.
[bold cyan]"His teaching about treating others the way you want
to be treated — that might be the most famous idea
anyone ever had."[/bold cyan]

A crescent moon rises on the next page...
""",
    "islam": """
[bold green]The five pillars stand strong and bright![/bold green]

Faith, prayer, charity, fasting, and pilgrimage — five duties
that shape the lives of nearly two billion people.

[bold cyan]"Islam asks people to pray, to give, and to care,"[/bold cyan]
Puck says. [bold cyan]"And during Ramadan, millions of people
around the world share the same experience of fasting
and then breaking bread together. That's powerful."[/bold cyan]

A six-pointed star begins to glow on the next page...
""",
    "judaism": """
[bold green]The Star of David shines bright![/bold green]

Torah scrolls, Shabbat candles, the menorah's nine flames —
three and a half thousand years of wisdom, still alive today.

[bold cyan]"Judaism gave the world so much,"[/bold cyan] Puck says softly.
[bold cyan]"The idea of one God. A day of rest. Laws about justice.
And it survived everything — everything — to still be here,
still being practiced, still teaching."[/bold cyan]

The page fills with colour as Hindu temples appear...
""",
    "hinduism": """
[bold green]The gods dance and the diyas glow![/bold green]

Brahma, Vishnu, Shiva. Karma and reincarnation.
The Festival of Lights blazing across the page.

[bold cyan]"A religion older than almost any other,"[/bold cyan] Puck says,
[bold cyan]"with a billion followers and stories so beautiful
they've been told for four thousand years.
The idea of karma alone changed how the whole world thinks."[/bold cyan]

A lotus flower blooms on the next page...
""",
    "buddhism": """
[bold green]The lotus blooms in perfect stillness![/bold green]

The Buddha beneath the tree. Four Noble Truths.
Compassion for all living things. The quiet, powerful mind.

[bold cyan]"The Buddha didn't ask anyone to worship him,"[/bold cyan]
Puck says. [bold cyan]"He just said: here is what I found.
Sit still. Pay attention. Be kind. That was enough
to change the world."[/bold cyan]

The final chapter of the Book begins to glow...
""",
    "other_beliefs": """
[bold green]Every voice has been heard![/bold green]

The Book of Many Voices glows with every colour, every symbol,
every tradition — Sikh generosity, indigenous wisdom, secular
kindness, and the one great lesson that ties them all together:
respect.

[bold cyan]"You did it,"[/bold cyan] Puck says, and there is real pride
in that small voice. [bold cyan]"You listened to every voice
in the Book. You didn't judge. You didn't pick sides.
You listened. And that — [italic]that[/italic] — is the beginning
of all wisdom."[/bold cyan]

Puck closes the Book of Many Voices gently.

[bold white]Listener. Learner. Bridge Builder. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "what_is_religion": "Puck holds up the glowing Book of Many Voices. [bold yellow]\"Here is the biggest question of all: there are many religions in the world. Is that a problem — or is it something wonderful?\"[/bold yellow]",
    "christianity": "Puck points to a golden phrase on the page. [bold yellow]\"Jesus taught one rule that nearly every religion in the world agrees with. It's called the Golden Rule. Do you know what it says?\"[/bold yellow]",
    "islam": "Five pillars of light glow on the page. [bold yellow]\"One of the Five Pillars of Islam is about giving to others. It's not optional — it's a duty. What is it called?\"[/bold yellow]",
    "judaism": "Puck unrolls a tiny scroll showing ancient letters. [bold yellow]\"Judaism stretches back thousands of years. Do you know how old this ancient faith truly is?\"[/bold yellow]",
    "hinduism": "A glowing wheel turns slowly on the page. [bold yellow]\"Hindus believe the soul goes on a journey after death — born again and again. What is this belief called?\"[/bold yellow]",
    "buddhism": "Puck places a hand over the heart and looks at the girl with gentle eyes. [bold yellow]\"The Buddha said one quality matters more than any other. It means caring about others' suffering and wanting to help. What is it?\"[/bold yellow]",
    "other_beliefs": "The Book of Many Voices glows with every symbol at once. [bold yellow]\"After hearing all these voices — every religion, every belief — what is the most important lesson of all?\"[/bold yellow]",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "foundation_seeker": (
        "Foundation Seeker",
        "Discovered what religion means and why people believe!",
    ),
    "christian_listener": (
        "Christian Listener",
        "Heard the story of Jesus, the Bible, and the Golden Rule!",
    ),
    "islamic_listener": (
        "Islamic Listener",
        "Learned about Muhammad, the Quran, and the Five Pillars!",
    ),
    "jewish_listener": (
        "Jewish Listener",
        "Explored the Torah, Shabbat, and 3,500 years of wisdom!",
    ),
    "hindu_listener": (
        "Hindu Listener",
        "Met Brahma, Vishnu, and Shiva, and learned about karma and Diwali!",
    ),
    "buddhist_listener": (
        "Buddhist Listener",
        "Sat with the Buddha and learned about compassion and the quiet mind!",
    ),
    "bridge_builder": (
        "Bridge Builder",
        "Listened to every voice in the Book — and respected them all!",
    ),
}
