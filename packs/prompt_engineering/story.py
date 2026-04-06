"""
story.py — Narrative for the Prompt Engineering skill pack.

ARIA guides the learner through the art of speaking to machines —
from first contact through mastery, unlocking the full power
of language models through precise, thoughtful communication.
"""

INTRO_STORY = """
[bold yellow]AI ACADEMY[/bold yellow]
[bold yellow]Module: The Prompt Playbook[/bold yellow]

A soft chime sounded as the terminal came to life. Lines of light traced
the outline of a figure — not quite human, not quite hologram — standing
at the threshold of a vast digital workspace.

[bold cyan]"I'm ARIA,"[/bold cyan] the figure said, voice warm and precise.
[bold cyan]"Adaptive Reasoning and Instruction Architect.
And I have a question for you."[/bold cyan]

The workspace shimmered. A single blinking cursor appeared, floating
in the center of the room like a heartbeat.

[bold cyan]"Do you know what that is?"[/bold cyan] ARIA gestured to the cursor.
[bold cyan]"It's a prompt. The starting point of every conversation
between a human and an AI. The words you type into that space
shape everything that comes back."[/bold cyan]

ARIA waved a hand and the cursor expanded into a cascade of examples —
prompts and responses, good and bad, brilliant and broken.

[bold cyan]"Most people type whatever comes to mind and hope for the best.
But the ones who understand how to [italic]craft[/italic] a prompt —
how to be clear, specific, strategic — they get something
entirely different back."[/bold cyan]

ARIA turned to face you directly.

[bold cyan]"I'm going to teach you the art of speaking to machines.
And by the end, you won't just be talking to AI.
You'll be [italic]directing[/italic] it."[/bold cyan]

The cursor blinked once more.

[bold white]Your training begins now.[/bold white]
"""

ZONE_INTROS = {
    "what_is_a_prompt": """
ARIA opened a clean terminal — nothing but a blinking cursor on a dark screen.

[bold cyan]"Before you can master prompts,"[/bold cyan] ARIA said,
[bold cyan]"you need to understand what they actually are.
A prompt is your input — the text you give to an AI.
And the AI's response is its output."[/bold cyan]

The screen split: [bold yellow]INPUT[/bold yellow] on the left, [bold yellow]OUTPUT[/bold yellow] on the right.

[bold cyan]"It sounds simple. But the relationship between input and output
is where all the magic — and all the frustration — lives.
Let's start at the very beginning."[/bold cyan]

[bold white]Welcome to First Contact.[/bold white]
""",
    "clarity_and_specificity": """
ARIA pulled up two prompts side by side on the terminal.

The first: [dim]'Write something about space.'[/dim]
The second: [bold green]'Write a 200-word overview of the James Webb Space Telescope's key discoveries in 2024, written for a general audience.'[/bold green]

[bold cyan]"Same topic. Wildly different results."[/bold cyan] ARIA traced
the difference with a finger. [bold cyan]"The first is a wish.
The second is a blueprint. In prompt engineering,
specificity isn't optional — it's the whole game."[/bold cyan]

[bold white]Time to sharpen your words.[/bold white]
""",
    "role_prompting": """
ARIA stepped aside, and three different versions of ARIA appeared —
one in a lab coat, one in a business suit, one in an artist's smock.

[bold cyan]"Same AI. Three different roles."[/bold cyan] The original ARIA gestured
to each copy. [bold cyan]"When you tell an AI to 'act as' someone,
you're not just giving it a costume. You're reshaping its entire
perspective — vocabulary, priorities, depth, tone."[/bold cyan]

The three copies spoke the same fact, each in their own voice:
science, business, art. Same information, three different worlds.

[bold cyan]"Roles are one of the most powerful tools in your kit.
Let's learn to wield them."[/bold cyan]

[bold white]Welcome to the Persona Engine.[/bold white]
""",
    "few_shot_examples": """
ARIA laid out three cards on the workspace, each showing an input
and an output connected by an arrow.

[bold cyan]"Humans learn by example,"[/bold cyan] ARIA said. [bold cyan]"And so do language models —
in a different way. When you show an AI two or three examples
of what you want, it picks up the pattern and applies it
to new inputs."[/bold cyan]

A fourth card appeared, blank on the output side.

[bold cyan]"This is few-shot prompting. You show the pattern.
The AI completes it. And the results are often
better than any instruction you could write."[/bold cyan]

[bold white]Let's learn to show, not just tell.[/bold white]
""",
    "chain_of_thought": """
ARIA drew a problem on the screen — a word problem with numbers,
conditions, and a question mark at the end.

[bold cyan]"If I ask the AI to answer this directly,"[/bold cyan] ARIA said,
[bold cyan]"it might get it right. Or it might jump to a wrong conclusion.
But if I ask it to think step by step..."[/bold cyan]

The answer unfolded in stages — each step building on the last,
each assumption made visible, each calculation shown.

[bold cyan]"Chain-of-thought prompting forces the AI to show its work.
And when it shows its work, it makes fewer mistakes."[/bold cyan]

[bold white]Let's learn to think — step by step.[/bold white]
""",
    "system_prompts": """
ARIA opened a door marked [bold red]CONTROL ROOM[/bold red] and stepped inside.

Banks of switches and dials lined the walls — each one labeled:
[bold yellow]PERSONA · RULES · FORMAT · BOUNDARIES · TONE[/bold yellow]

[bold cyan]"User messages are what people say to the AI,"[/bold cyan] ARIA explained,
gesturing to a stream of conversation flowing through the center.
[bold cyan]"But system messages are the rules that govern HOW
the AI responds. They're the director's instructions —
set before the conversation even begins."[/bold cyan]

ARIA flipped a switch. The AI's entire behavior shifted.

[bold cyan]"In the control room, you don't just talk to the AI.
You configure it."[/bold cyan]

[bold white]Welcome to the Control Room.[/bold white]
""",
    "advanced_techniques": """
ARIA opened a toolbox that hummed with energy. Inside, instruments
glowed with different colors — each one a different capability.

[bold cyan]"You've learned to write clear prompts, assign roles,
give examples, and structure reasoning,"[/bold cyan] ARIA said.
[bold cyan]"Now it's time for the power tools. Temperature control.
Structured output. JSON mode. Meta-prompting."[/bold cyan]

ARIA picked up a dial labeled [bold yellow]TEMPERATURE[/bold yellow] and turned it slowly.
The AI's responses shifted from precise and predictable
to wild and creative.

[bold cyan]"These are the tools that separate casual users
from prompt engineers."[/bold cyan]

[bold white]Time to open the advanced toolkit.[/bold white]
""",
    "prompt_debugging": """
ARIA pulled up a prompt on the screen — and the output next to it
was [bold red]completely wrong[/bold red].

[bold cyan]"This,"[/bold cyan] ARIA said calmly, [bold cyan]"is reality. Prompts fail.
Outputs hallucinate. Users try to break your system.
And your job — as a prompt engineer — is to diagnose
what went wrong and fix it."[/bold cyan]

A diagnostic overlay appeared, highlighting the prompt's
ambiguities, missing constraints, and conflicting instructions.

[bold cyan]"Debugging prompts is a skill. Iterating is a discipline.
And understanding prompt injection is a necessity.
This is where you become a professional."[/bold cyan]

[bold white]Welcome to Debug Mode.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "what_is_a_prompt": """
[bold green]First Contact complete![/bold green]

You understand the fundamentals: prompts are input, responses are output,
LLMs predict tokens, and context windows have limits.

[bold cyan]"You've learned how the machine listens,"[/bold cyan] ARIA says.
[bold cyan]"Now it's time to learn how to speak clearly."[/bold cyan]

The terminal sharpens. The next zone awaits...
""",
    "clarity_and_specificity": """
[bold green]Say What You Mean — mastered![/bold green]

Specific beats vague. Format beats freeform. Constraints beat chaos.
You've learned the most important lesson in prompting: precision is power.

[bold cyan]"Your prompts have edges now,"[/bold cyan] ARIA says.
[bold cyan]"Sharp, clear, and purposeful. Let's see what happens
when you give the AI a persona to inhabit."[/bold cyan]
""",
    "role_prompting": """
[bold green]The Persona Engine — activated![/bold green]

You can now assign roles, frame expertise, set tone,
and understand the limits of persona prompting.

[bold cyan]"The AI can be anyone you need it to be,"[/bold cyan] ARIA says.
[bold cyan]"But you're the director. And now you know how to cast."[/bold cyan]

Example cards begin to glow. The next technique is Show, Don't Tell...
""",
    "few_shot_examples": """
[bold green]Show, Don't Tell — complete![/bold green]

You've learned the power of examples: pattern matching,
style transfer, classification, and the art of diverse demonstrations.

[bold cyan]"Sometimes the best instruction is no instruction at all,"[/bold cyan] ARIA says.
[bold cyan]"Just examples. The AI sees the pattern and runs with it."[/bold cyan]

A chain of logic links appears. Step-by-step reasoning awaits...
""",
    "chain_of_thought": """
[bold green]Think Step by Step — mastered![/bold green]

You can now guide the AI through structured reasoning,
break down complex problems, and separate thought from answer.

[bold cyan]"You've taught the AI to show its work,"[/bold cyan] ARIA says.
[bold cyan]"And in doing so, you've made it smarter.
Now let's go deeper — into the control room."[/bold cyan]
""",
    "system_prompts": """
[bold green]The Control Room — unlocked![/bold green]

System messages, behavioral guardrails, instruction hierarchies,
conversation memory — you now understand the architecture
of AI behavior configuration.

[bold cyan]"You're not just prompting anymore,"[/bold cyan] ARIA says.
[bold cyan]"You're engineering. Time for the advanced toolkit."[/bold cyan]
""",
    "advanced_techniques": """
[bold green]Power Tools — equipped![/bold green]

Temperature, JSON mode, structured output, creative constraints,
meta-prompting — you now have the full professional toolkit.

[bold cyan]"You have every tool a prompt engineer needs,"[/bold cyan] ARIA says.
[bold cyan]"One more step: learning what to do when things break."[/bold cyan]

A red light flashes. Debug Mode is calling...
""",
    "prompt_debugging": """
[bold green]Debug Mode — complete. All zones mastered![/bold green]

You can diagnose prompt failures, iterate methodically,
spot hallucinations, defend against injection, and think
like a professional prompt engineer.

[bold cyan]"You've done it,"[/bold cyan] ARIA says quietly. The workspace
glows with everything you've built — every technique,
every insight, every tool.

[bold cyan]"You don't just talk to AI anymore.
You speak its language. You shape its behavior.
You get exactly what you want back."[/bold cyan]

ARIA steps aside. The terminal is yours.

[bold white]Prompt Architect. Conversation Designer. AI Whisperer.[/bold white]
[bold white]That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "what_is_a_prompt": "ARIA splits a sentence into glowing fragments. [bold yellow]\"Everything the AI reads — and everything it generates — is made of these. What are they called?\"[/bold yellow]",
    "clarity_and_specificity": "ARIA shows a prompt producing unwanted output. [bold yellow]\"The AI keeps doing what you didn't ask for. How do you fix it — not by changing what you want, but by saying what you don't?\"[/bold yellow]",
    "role_prompting": "ARIA removes all costumes. [bold yellow]\"A role can make the AI sound like an expert. But does it make the AI right? What's the most important thing to understand about role prompting?\"[/bold yellow]",
    "few_shot_examples": "ARIA fans out a set of examples. [bold yellow]\"Three examples. But are they teaching the full picture — or just one corner of it? Quality of examples matters more than quantity.\"[/bold yellow]",
    "chain_of_thought": "ARIA presents a complex problem. [bold yellow]\"The AI needs to think deeply — but you only need the final answer. Can you have both: thorough reasoning AND a clean result?\"[/bold yellow]",
    "system_prompts": "ARIA stands at the control room's main panel. [bold yellow]\"The system says one thing. The user says another. When instructions conflict — who wins?\"[/bold yellow]",
    "advanced_techniques": "ARIA holds up a recursive mirror. [bold yellow]\"What if the best way to write a prompt... is to ask the AI to write it for you?\"[/bold yellow]",
    "prompt_debugging": "ARIA steps back from the terminal. [bold yellow]\"This is the final test. Not a technique — a mindset. What separates someone who uses AI from someone who truly engineers with it?\"[/bold yellow]",
}
