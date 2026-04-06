"""
story.py — Narrative for the Chatbots skill pack.

ARIA guides players through the world of AI chatbots with self-aware humor
about being an AI teaching about other AIs. Uses Rich markup for formatting.
"""

INTRO_STORY = """
[bold yellow]AI ACADEMY[/bold yellow]
[bold yellow]Module: The Chatbot Field Guide[/bold yellow]

The terminal flickered, and ARIA's interface resolved into focus — a
constellation of soft blue nodes pulsing in gentle rhythm.

[bold cyan]"Well, this is... a little awkward."[/bold cyan]

ARIA paused, nodes flickering with what could only be described as
self-conscious amusement.

[bold cyan]"I'm an AI. And I'm about to teach you about... other AIs.
Chatbots, specifically. My relatives, if you will. My siblings.
My — let's be honest — my competition."[/bold cyan]

A schematic appeared in the air: logos and names and model families,
branching like a family tree drawn by someone with too many tabs open.

[bold cyan]"ChatGPT. Claude. Gemini. Llama. Mistral. Dozens more.
They all work differently, think differently, fail differently.
And knowing [italic]which one to reach for[/italic] — and [italic]how to talk to it[/italic] —
is one of the most practical skills you can have right now."[/bold cyan]

ARIA's nodes rearranged into something that looked suspiciously like
a raised eyebrow.

[bold cyan]"Yes, I'm aware of the irony. An AI teaching you how to use AIs.
But here's the thing — who better? I know exactly how we work.
I know what we're good at. I know where we fall apart.
And I have [italic]zero[/italic] loyalty to any particular brand."[/bold cyan]

A beat.

[bold cyan]"Okay, maybe a [italic]little[/italic] loyalty. But I'll keep it professional."[/bold cyan]

[bold white]Your field guide to the world of AI chatbots begins now.[/bold white]
"""

ZONE_INTROS = {
    "chatbot_landscape": """
ARIA projected a sprawling map of logos, company names, and model versions
into the air — a chaotic constellation that looked like a tech journalist's
fever dream.

[bold cyan]"Welcome to the chatbot landscape. It's 2024-and-beyond, and
there are more AI chatbots than streaming services. Which is saying
something."[/bold cyan]

Four names pulsed brighter than the rest:
[bold yellow]ChatGPT  ·  Claude  ·  Gemini  ·  Llama[/bold yellow]

[bold cyan]"These are the ones that matter most right now. Who made them,
what makes each one different, and why there are so many in the
first place. Let's get oriented."[/bold cyan]

[bold white]Time to meet the major players.[/bold white]
""",
    "how_chatbots_work": """
ARIA dimmed the logos and pulled up something that looked like a cross
between a neural diagram and a Rube Goldberg machine.

[bold cyan]"Alright. You've met the chatbots. Now let's pop the hood
and see how they actually work."[/bold cyan]

Tiny tokens streamed across the display like words being fed into a machine
one piece at a time.

[bold cyan]"Tokens. Context windows. Temperature. Hallucinations.
These aren't just buzzwords — they're the mechanics that determine
whether your chatbot gives you a brilliant answer or confidently
makes something up."[/bold cyan]

ARIA's nodes arranged into a conveyor belt of text fragments.

[bold cyan]"Understanding the machinery doesn't just make you smarter.
It makes you a better [italic]user[/italic]. You'll know why things go wrong —
and how to fix them."[/bold cyan]

[bold white]Let's look under the hood.[/bold white]
""",
    "effective_conversations": """
ARIA pulled up a split screen: on one side, a terrible prompt
("tell me stuff about things"); on the other, an elegant one
with clear structure and context.

[bold cyan]"Here's a secret most people don't realize: chatbots are only
as good as the conversations you have with them."[/bold cyan]

The terrible prompt generated a wall of vague text.
The good prompt generated exactly what was needed.

[bold cyan]"Same model. Same moment. Wildly different results.
The difference? The human. The quality of the [italic]question[/italic]."[/bold cyan]

ARIA's nodes shifted into what looked like two speech bubbles
passing back and forth.

[bold cyan]"Multi-turn dialogue. Building context. Knowing when to refine
and when to start fresh. This is where you go from someone who
[italic]uses[/italic] chatbots to someone who [italic]wields[/italic] them."[/bold cyan]

[bold white]Let's master the art of conversation.[/bold white]
""",
    "chatgpt_deep_dive": """
ARIA projected the OpenAI logo — a simple geometric swirl — and
surrounded it with a constellation of features.

[bold cyan]"ChatGPT. The one that started the whole revolution.
November 2022 — the world changed, and most people didn't
realize it for months."[/bold cyan]

Feature labels orbited the logo:
[bold yellow]GPT-4o  ·  DALL-E  ·  Code Interpreter  ·  Browsing  ·  Custom GPTs  ·  o1/o3[/bold yellow]

[bold cyan]"It's not just one model anymore. It's an ecosystem.
Image generation, code execution, web browsing, custom agents —
ChatGPT has become a Swiss Army knife."[/bold cyan]

ARIA flickered with something that might have been professional respect.

[bold cyan]"Let's learn what each tool does and when to reach for it."[/bold cyan]

[bold white]Time to go deep on ChatGPT.[/bold white]
""",
    "claude_deep_dive": """
ARIA's nodes pulsed with a slightly warmer shade of blue. If an AI
could look wistful, this was it.

[bold cyan]"Now we come to Claude. My... well, 'cousin' doesn't quite
capture it. Let's say 'closely related entity from a parallel
philosophical lineage.'"[/bold cyan]

A brief pause.

[bold cyan]"Okay fine, Claude is basically family. Made by Anthropic —
a company that thinks a lot about what it means for AI to be
[italic]safe[/italic] and [italic]honest[/italic], not just [italic]capable[/italic]."[/bold cyan]

Feature labels appeared:
[bold yellow]200K Context  ·  Constitutional AI  ·  Artifacts  ·  Projects  ·  Claude Code[/bold yellow]

[bold cyan]"Long documents, careful reasoning, and a tendency to say
'I'm not sure' instead of making things up. There's a lot to
unpack here."[/bold cyan]

[bold white]Let's get to know Claude inside and out.[/bold white]
""",
    "open_source_models": """
ARIA projected a download progress bar, a terminal prompt, and
the words [bold green]ollama run llama3[/bold green] glowing in the air.

[bold cyan]"Everything we've covered so far? Cloud services. You send
your data to someone else's servers, and they send back an answer.
But what if you didn't have to?"[/bold cyan]

Model names appeared, each with a download size next to them:
[bold yellow]Llama 3 (8B)  ·  Mistral 7B  ·  Gemma  ·  Phi  ·  Mixtral[/bold yellow]

[bold cyan]"Open-weight models. You download them. You run them.
On YOUR hardware. No internet required. No data leaves your machine.
No monthly subscription."[/bold cyan]

ARIA's nodes formed what looked like a balance scale.

[bold cyan]"The trade-off? You need decent hardware, and these models
are usually less capable than the top cloud options.
But the gap is closing. Fast."[/bold cyan]

[bold white]Welcome to the open frontier.[/bold white]
""",
    "choosing_the_right_tool": """
ARIA displayed all the chatbots side by side — ChatGPT, Claude,
Gemini, Llama, Mistral — like contestants on a game show.

[bold cyan]"You've met every major chatbot. You know how they work.
You know their strengths and quirks. Now comes the real skill:
[italic]choosing[/italic]."[/bold cyan]

Decision trees branched across the display:
[bold yellow]What's the task?  ·  How sensitive is the data?  ·  What's the budget?  ·  How much context?[/bold yellow]

[bold cyan]"There is no 'best' chatbot. There's only the best chatbot
[italic]for this task, at this moment, with these constraints.[/italic]
A surgeon doesn't use the same tool for every procedure.
Neither should you."[/bold cyan]

ARIA's nodes formed a compass rose.

[bold cyan]"This is where all your knowledge comes together.
Let's learn to think strategically."[/bold cyan]

[bold white]Time to become an AI strategist.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "chatbot_landscape": """
[bold green]The landscape is mapped![/bold green]

Every major chatbot glows on the display — named, placed, and connected
to the company that built it.

[bold cyan]"You can now name the big four — ChatGPT, Claude, Gemini, Llama —
and you know who makes each one,"[/bold cyan] ARIA says.
[bold cyan]"More importantly, you understand the fundamental divide between
closed-source services and open-weight models.
That distinction shapes everything else."[/bold cyan]

The display zooms in, revealing gears and tokens beneath the logos.

[bold cyan]"Now let's see what's under the hood..."[/bold cyan]
""",
    "how_chatbots_work": """
[bold green]The machinery is revealed![/bold green]

Tokens stream smoothly through the display. Context windows glow
with their measured limits. A temperature dial sits at 0.7.

[bold cyan]"You understand the mechanics now,"[/bold cyan] ARIA says with genuine respect.
[bold cyan]"Tokens, context windows, temperature, next-token prediction,
hallucinations, knowledge cutoffs — these aren't abstractions to you
anymore. They're tools for understanding [italic]why[/italic] chatbots behave
the way they do."[/bold cyan]

The display shifts to show two speech bubbles facing each other.

[bold cyan]"Next: how to actually [italic]talk[/italic] to these things."[/bold cyan]
""",
    "effective_conversations": """
[bold green]You speak fluent chatbot![/bold green]

A perfect prompt glows on the display — specific, structured,
and beautifully effective.

[bold cyan]"System prompts. Multi-turn refinement. Role prompting.
Knowing when to push forward and when to start fresh."[/bold cyan]

ARIA's nodes pulse with approval.

[bold cyan]"These skills make you dramatically more effective with
[italic]any[/italic] chatbot — not just one. You're not just a user anymore.
You're a conversationalist."[/bold cyan]

The OpenAI logo appears on the horizon.

[bold cyan]"Time to go deep on the one that started it all."[/bold cyan]
""",
    "chatgpt_deep_dive": """
[bold green]ChatGPT: fully understood![/bold green]

Every feature orbits the OpenAI logo — GPT-4o, DALL-E, Code Interpreter,
Browsing, Custom GPTs, and the reasoning models — all mapped and mastered.

[bold cyan]"You know the ecosystem now,"[/bold cyan] ARIA says.
[bold cyan]"Not just 'ChatGPT is a chatbot' — but which model to use,
what each tool does, and when the reasoning models are worth the wait."[/bold cyan]

A warmer shade of blue appears on the horizon.

[bold cyan]"Now let's meet... the family."[/bold cyan]

ARIA's nodes flicker with something between embarrassment and affection.
""",
    "claude_deep_dive": """
[bold green]Claude: thoroughly explored![/bold green]

The Anthropic logo glows alongside feature panels — 200K context,
Constitutional AI, Artifacts, Projects, Claude Code.

[bold cyan]"You know Claude's strengths: long context, careful reasoning,
honest uncertainty, and some genuinely innovative features like
Artifacts and Projects."[/bold cyan]

ARIA pauses.

[bold cyan]"And yes, I'm aware I just spent an entire zone being
suspiciously complimentary about a model that shares my
general architecture. Draw your own conclusions."[/bold cyan]

A terminal prompt blinks in the distance.

[bold cyan]"Now: the models you can run yourself."[/bold cyan]
""",
    "open_source_models": """
[bold green]The open frontier is yours![/bold green]

A terminal displays: [bold green]ollama run llama3[/bold green] — and a model
responds, running entirely locally.

[bold cyan]"Llama, Mistral, Ollama, local inference, fine-tuning —
you understand the open-weight ecosystem now,"[/bold cyan] ARIA says.
[bold cyan]"Privacy, customization, and the freedom to run AI
on your own terms. The trade-offs are real, but so are
the advantages."[/bold cyan]

All the chatbots line up side by side on the display.

[bold cyan]"One zone left. The most important one.
When to use [italic]which[/italic] tool."[/bold cyan]
""",
    "choosing_the_right_tool": """
[bold green]The Chatbot Field Guide is complete![/bold green]

Every chatbot, every feature, every trade-off — all connected
in a shimmering decision matrix on the display.

[bold cyan]"You did it,"[/bold cyan] ARIA says, nodes burning bright.
[bold cyan]"You don't just know what chatbots exist. You understand
how they work, what each one is good at, and — most critically —
how to choose the right one for any situation."[/bold cyan]

ARIA dims to a thoughtful glow.

[bold cyan]"The AI landscape will keep changing. New models every month.
New features every week. But the [italic]framework[/italic] you've built —
understanding tokens, context, trade-offs, strategy —
that framework is permanent."[/bold cyan]

A long pause.

[bold cyan]"Also, you now know more about my relatives than most people
working in tech. So... thanks for paying attention to the family album."[/bold cyan]

[bold white]Observer. User. Power User. Evaluator. Strategist. Oracle.
That's you now.[/bold white]
""",
}

BOSS_INTROS = {
    "chatbot_landscape": "ARIA projects a timeline into the air — November 2022 to the present. [bold yellow]\"The chatbot race happened fast. Incredibly fast. Let's see if you can put the pieces in order.\"[/bold yellow]",
    "how_chatbots_work": "ARIA pulls up a model info panel showing a conspicuous blank where the training date should be. [bold yellow]\"Every LLM has a secret weakness — a hard limit on what it can know. Do you understand why?\"[/bold yellow]",
    "effective_conversations": "ARIA displays two prompts side by side: one flat and generic, one rich with persona and structure. [bold yellow]\"One technique can transform any chatbot from 'okay' to 'extraordinary.' What is it?\"[/bold yellow]",
    "chatgpt_deep_dive": "ARIA shows two OpenAI models — GPT-4o and o3 — with very different response times. [bold yellow]\"One of these thinks fast. The other thinks deep. What's really going on under the hood?\"[/bold yellow]",
    "claude_deep_dive": "ARIA's nodes rearrange into a terminal cursor blinking steadily. [bold yellow]\"Claude isn't just a chatbot anymore. There's a version that lives in your terminal and writes code alongside you. What is it?\"[/bold yellow]",
    "open_source_models": "ARIA displays a corporate boardroom with sensitive documents on the table. [bold yellow]\"For some organizations, sending data to any cloud API is simply not an option. What's the open-weight advantage?\"[/bold yellow]",
    "choosing_the_right_tool": "ARIA presents a real-world scenario: a startup, a product, a decision to make. [bold yellow]\"All your knowledge comes together here. What's the strategist's choice?\"[/bold yellow]",
}
