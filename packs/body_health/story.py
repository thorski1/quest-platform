"""
story.py — Narrative for the Body & Health skill pack.

Long Long guides you through the world of body parts, feelings,
medical vocabulary, exercise, and describing people in Chinese.
"""

INTRO_STORY = """
[bold red]LEARN CHINESE[/bold red]
[bold yellow]Chapter: Body & Health[/bold yellow]

Long Long the dragon soared above a medieval village where healers
mixed herbs in stone apothecaries and knights trained in the
courtyard with sword and shield. The smell of medicinal teas
drifted from the castle infirmary.

[bold cyan]"Your body is your castle,"[/bold cyan] Long Long said, landing
on the infirmary roof. [bold cyan]"And in Chinese, you need
the words to describe it, care for it, and keep it strong.
Shen ti -- the body -- is where language meets life."[/bold cyan]

A healer rushed past carrying bundles of herbs, while in the
courtyard, soldiers stretched and sparred in the morning light.

[bold cyan]"We'll start with the parts of the body -- tou, shou,
jiao, yan jing. Then we'll learn to express feelings -- happy,
sad, tired, hungry. After that, we visit the healer -- doctor,
medicine, illness. Then we train like knights -- running,
swimming, sports. And finally, we'll learn to describe the
people around us -- tall, short, beautiful."[/bold cyan]

Long Long flexed his wings and grinned.

[bold cyan]"Ready to master the language of body and health?"[/bold cyan]

[bold white]Your journey into body and health in Chinese begins now.[/bold white]
"""

ZONE_INTROS = {
    "body_parts": """
Long Long stood in the castle's great hall, where a tapestry
showed a detailed map of the human body labeled in Chinese
characters.

[bold cyan]"Every language starts with the body,"[/bold cyan]
Long Long said, tapping the tapestry with a claw.
[bold cyan]"Tou, shou, jiao -- head, hand, foot. These are words
you'll use every single day. When something hurts, when you
wave hello, when you point at something beautiful -- it all
starts with knowing the body."[/bold cyan]

[bold white]Let's learn essential body part vocabulary![/bold white]
""",
    "feelings_emotions": """
Long Long led you into the castle's inner garden, where a
fountain shaped like a smiling face bubbled beside a weeping
willow tree.

[bold cyan]"How do you feel right now?"[/bold cyan] Long Long asked
softly. [bold cyan]"Gao xing? Nan guo? Lei? In Chinese,
expressing feelings is beautifully direct. Happy is 'high
excitement,' sad is 'hard to endure,' tired is just one
character -- lei. Learn these words and you can share your
heart with anyone."[/bold cyan]

[bold white]Let's learn to express feelings and emotions![/bold white]
""",
    "at_the_doctor": """
Long Long pushed open the heavy wooden door of the castle
infirmary. Shelves lined with glass bottles of herbs and
powders stretched to the ceiling. A kindly healer looked
up from grinding medicine.

[bold cyan]"No one wants to be sick,"[/bold cyan] Long Long said,
[bold cyan]"but everyone needs to know these words. Yi sheng,
yi yuan, yao -- doctor, hospital, medicine. When you travel
to China, these words could save you. Sheng bing le?
You'll know exactly what to say."[/bold cyan]

[bold white]Let's learn medical vocabulary![/bold white]
""",
    "exercise_sports": """
Long Long led you to the castle training grounds, where
knights jousted, archers shot at targets, and squires ran
laps around the stone walls.

[bold cyan]"A strong body needs strong words,"[/bold cyan] Long Long
said, watching a knight sprint past in full armor.
[bold cyan]"Pao bu, you yong, da qiu -- running, swimming,
playing ball. Chinese people love sports, and morning
exercise in the park is a national tradition. Learn these
words and you can join in anywhere."[/bold cyan]

[bold white]Let's learn exercise and sports vocabulary![/bold white]
""",
    "describing_people": """
Long Long gathered a group of castle inhabitants -- the tall
blacksmith, the petite seamstress, the stout cook, and the
slender archer -- and lined them up in the courtyard.

[bold cyan]"Look at the people around you,"[/bold cyan] Long Long said.
[bold cyan]"Gao, ai, pang, shou, piao liang -- tall, short, fat,
thin, pretty. In Chinese, describing people uses simple,
vivid words. And the patterns are elegant: hen gao means
very tall, bu gao means not tall. Master these and you can
paint a portrait with words."[/bold cyan]

[bold white]Let's learn to describe people![/bold white]
""",
}

ZONE_COMPLETIONS = {
    "body_parts": """
[bold green]Long Long roared with joy, rattling the tapestries on the walls![/bold green]

[bold cyan]"Tou, shou, jiao, yan jing, zui ba, er duo -- you know your
body in Chinese! From head to toe, you can name every part.
And when something hurts, you can say exactly where!"[/bold cyan]
""",
    "feelings_emotions": """
[bold green]Long Long breathed a warm, gentle flame into the garden air![/bold green]

[bold cyan]"Gao xing, nan guo, lei, e, ke -- you speak the language
of the heart! You can share how you feel, comfort a friend,
and understand when someone tells you their emotions.
That's real communication."[/bold cyan]
""",
    "at_the_doctor": """
[bold green]Long Long stamped the healer's seal of approval![/bold green]

[bold cyan]"Yi sheng, yi yuan, yao, sheng bing, fa shao -- the healer's
vocabulary is yours! You can describe symptoms, ask for medicine,
and navigate a hospital visit. These words are your armor
against illness in any Chinese-speaking land."[/bold cyan]
""",
    "exercise_sports": """
[bold green]Long Long soared in a victory lap around the training grounds![/bold green]

[bold cyan]"Pao bu, you yong, da qiu, duan lian -- you command the words
of movement and strength! You can talk about your favorite sports,
how often you exercise, and stay fit in any conversation.
A healthy body and a healthy vocabulary!"[/bold cyan]
""",
    "describing_people": """
[bold green]Long Long breathed a triumphant plume of golden fire![/bold green]

[bold cyan]"Gao, ai, pang, shou, piao liang -- you paint portraits with
words! You can describe anyone you meet, give compliments,
and use elegant patterns like 'neither tall nor short.'
The people around you have come alive in Chinese!"[/bold cyan]
""",
}

BOSS_INTROS = {
    "body_parts": """
Long Long pointed to the body tapestry and covered the labels.

[bold cyan]"You've learned every part. Now prove you can use them
in real sentences -- tell me where it hurts, name the parts,
and show me you own this vocabulary!"[/bold cyan]
""",
    "feelings_emotions": """
Long Long dimmed the garden lights and spoke softly.

[bold cyan]"Feelings are the deepest test of language. Comfort a friend,
express your own heart, understand what others feel.
Show me you speak the language of emotions!"[/bold cyan]
""",
    "at_the_doctor": """
Long Long led you to the healer's examination room.

[bold cyan]"You're at the doctor. You need to explain what's wrong,
understand the diagnosis, and know what medicine to take.
This is survival Chinese -- prove you're ready!"[/bold cyan]
""",
    "exercise_sports": """
Long Long blew a horn to start the training tournament.

[bold cyan]"Name the sports, say how often you train, tell me
your favorites. A true champion knows the words as well
as the moves -- show me your strength!"[/bold cyan]
""",
    "describing_people": """
Long Long lined up the castle inhabitants once more.

[bold cyan]"Describe them all -- tall, short, thin, beautiful.
Use the patterns, combine descriptions, and show me
you can paint a picture with Chinese words alone!"[/bold cyan]
""",
}
