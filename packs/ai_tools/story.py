"""
story.py — Narrative for the AI Toolkit skill pack.

ARIA guides the learner through the landscape of AI tools —
image generators, writing assistants, coding companions, search engines,
audio/video creators, productivity automators, and the art of choosing wisely.
Theme: "Your AI toolkit — the right tool for the right job."
"""

INTRO_STORY = """
[bold yellow]AI ACADEMY[/bold yellow]
[bold yellow]Chapter: The AI Toolkit[/bold yellow]

ARIA materialized beside a vast workbench that stretched into the distance.
Every surface was covered with tools — some gleaming and new, others humming
with quiet power, a few still flickering into existence as you watched.

[bold cyan]"Welcome to the Toolkit,"[/bold cyan] ARIA said, gesturing across the
impossible workbench. [bold cyan]"Every one of these is an AI tool.
Some generate images from words. Some write prose. Some write code.
Some search the whole internet in seconds and synthesize what they find.
Some compose music nobody has ever heard. Some automate the boring parts
of your day so you can focus on what actually matters."[/bold cyan]

You look across the bench. There are hundreds of tools.
[bold white]"How do I know which ones to use?"[/bold white]

ARIA picked up a small, elegant device and turned it in the light.
[bold cyan]"That,"[/bold cyan] ARIA said, [bold cyan]"is exactly the right question.
A tool is only as good as the hand that wields it — and the mind
that chooses it. The goal isn't to collect every tool.
It's to understand what each one does, when it shines,
when it fails, and how to build [italic]your[/italic] stack —
the right tool for the right job."[/bold cyan]

ARIA set the device down and the workbench organized itself
into seven distinct sections, each one glowing softly.

[bold cyan]"Seven domains. Seven sets of tools. One principle:
[italic]understand before you adopt.[/italic]"[/bold cyan]

ARIA looked at you steadily.

[bold cyan]"Ready to build your toolkit?"[/bold cyan]

[bold white]Your journey through the AI tool landscape begins now.[/bold white]
"""

ZONE_INTROS = {
    "ai_image_generation": """
ARIA led you to the first section of the workbench — an area bathed
in shifting colors where canvases materialized from thin air.

[bold cyan]"The Pixel Forge,"[/bold cyan] ARIA said. [bold cyan]"This is where words
become images. DALL-E. Midjourney. Stable Diffusion. Each one takes
a text prompt and conjures a picture that never existed before."[/bold cyan]

A canvas flickered to life — a photorealistic landscape dissolving
into an impressionist painting, then into anime, then into a sketch.

[bold cyan]"But the magic isn't in the tool. It's in the prompt.
The same model can produce garbage or gallery-worthy art
depending entirely on how you talk to it."[/bold cyan]

[bold yellow]Tools: DALL-E · Midjourney · Stable Diffusion[/bold yellow]

[bold white]Let's learn how AI turns text into images.[/bold white]
""",
    "ai_writing_tools": """
ARIA moved to a section of the workbench lined with typewriters,
notebooks, and glowing screens — each one filled with flowing text.

[bold cyan]"The Writer's Workshop,"[/bold cyan] ARIA said. [bold cyan]"Writing is thinking
made visible. And these tools — Grammarly, Jasper, Copy.ai — they don't
replace your thinking. They accelerate it. They catch your mistakes.
They help you get past the blank page."[/bold cyan]

A draft appeared on one screen — rough, messy, full of red underlines.
Then a second draft materialized beside it — clean, sharp, polished.

[bold cyan]"The first draft is where AI shines. The final draft
is where [italic]you[/italic] shine. Never confuse the two."[/bold cyan]

[bold yellow]Tools: Grammarly · Jasper · Copy.ai[/bold yellow]

[bold white]Let's explore the AI writing toolkit.[/bold white]
""",
    "ai_coding_tools": """
ARIA led you deeper into the workbench, where terminals glowed green
and lines of code scrolled across dark screens.

[bold cyan]"The Code Forge,"[/bold cyan] ARIA said. [bold cyan]"GitHub Copilot.
Cursor. Claude Code. Windsurf. These are your AI pair programmers —
tireless collaborators who suggest, complete, refactor, and debug
alongside you."[/bold cyan]

On one screen, ghost text appeared inside an editor — a function
completing itself as if written by an invisible hand.

On another, a terminal showed an AI agent reading files, making edits,
running tests, and fixing errors autonomously.

[bold cyan]"But here's the rule that never changes: [italic]you[/italic] are
responsible for understanding every line. The AI writes fast.
You ensure it writes [italic]right.[/italic]"[/bold cyan]

[bold yellow]Tools: GitHub Copilot · Cursor · Claude Code · Windsurf[/bold yellow]

[bold white]Let's explore AI pair programming.[/bold white]
""",
    "ai_search": """
ARIA stood before a section of the workbench that looked like a library
crossed with a command center — search bars, citation panels, and
glowing documents orbiting each other.

[bold cyan]"The Search Nexus,"[/bold cyan] ARIA said. [bold cyan]"For twenty years,
search meant typing keywords and clicking blue links. Now AI reads
the links for you, synthesizes the information, and gives you
an answer — with citations."[/bold cyan]

A query floated in the air. Below it, ten blue links appeared.
Then they dissolved, replaced by a single, clear paragraph with
numbered footnotes.

[bold cyan]"Perplexity. Google AI Overviews. ChatGPT Search.
Each one reimagines how you find information.
But convenience has a cost — you must learn to verify,
because confident answers are not always correct ones."[/bold cyan]

[bold yellow]Tools: Perplexity · Google AI Overviews · ChatGPT Search[/bold yellow]

[bold white]Let's explore how AI is changing search.[/bold white]
""",
    "ai_audio_video": """
ARIA opened a door to a section of the workbench that pulsed with sound
and motion — speakers humming, screens playing silent films, waveforms
dancing in the air.

[bold cyan]"The Studio,"[/bold cyan] ARIA said. [bold cyan]"Voice. Music. Video.
Three mediums that used to require studios, instruments, cameras,
and entire production crews. Now an AI can generate all three
from a text prompt."[/bold cyan]

A voice spoke from a speaker — warm, human, expressive.
Then ARIA revealed: no human recorded it.

A song played — guitar, drums, vocals. No musician played a note.

A video clip ran — a drone shot over mountains at sunrise.
No drone flew.

[bold cyan]"ElevenLabs. Suno. Runway. Kling. The creative frontier
is moving faster here than anywhere else — and so are
the ethical questions."[/bold cyan]

[bold yellow]Tools: ElevenLabs · Suno · Runway · Kling[/bold yellow]

[bold white]Let's explore AI in audio and video.[/bold white]
""",
    "ai_productivity": """
ARIA led you to a quieter section of the workbench — organized,
minimalist, with neat rows of connected tools passing data
between them like a well-oiled machine.

[bold cyan]"The Efficiency Engine,"[/bold cyan] ARIA said. [bold cyan]"Not every AI tool
is about creation. Some are about [italic]elimination[/italic] —
eliminating busywork, eliminating forgotten follow-ups,
eliminating the hours you spend doing things a machine
could do in seconds."[/bold cyan]

A workflow diagram glowed on the wall: an email arrived,
a spreadsheet updated, a Slack notification fired,
a calendar event created — all automatically.

[bold cyan]"Notion AI. Otter.ai. Zapier. These tools don't replace
your thinking. They replace the boring parts between
your thoughts."[/bold cyan]

[bold yellow]Tools: Notion AI · Otter.ai · Zapier AI[/bold yellow]

[bold white]Let's learn to automate the mundane.[/bold white]
""",
    "choosing_ai_tools": """
ARIA stepped back from the workbench and gestured across the
entire landscape you'd traversed — image generators, writing tools,
coding assistants, search engines, audio/video creators, productivity
automators — all of them humming with potential.

[bold cyan]"You've seen what's available,"[/bold cyan] ARIA said quietly.
[bold cyan]"Now comes the hardest part: choosing wisely."[/bold cyan]

The tools on the workbench shifted, some dimming, others brightening.

[bold cyan]"Free or paid? Open-source or proprietary? Private or convenient?
Every tool has trade-offs. Every adoption has costs — not just money,
but time, attention, and sometimes your data. The goal isn't to use
[italic]every[/italic] tool. It's to build [italic]your[/italic] stack —
the three to five tools you know deeply, trust completely, and use daily."[/bold cyan]

ARIA held up a simple framework — five columns on a glowing card:
[bold yellow]Capability · Privacy · Cost · Integration · Reliability[/bold yellow]

[bold cyan]"The right tool for the right job. That's the whole principle."[/bold cyan]

[bold white]Let's learn to choose.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "ai_image_generation": """
[bold green]The Pixel Forge glows with completed canvases![/bold green]

DALL-E, Midjourney, Stable Diffusion — you understand how each one works,
what makes a great prompt, and when to reach for which tool.

[bold cyan]"You can speak the language of image generation now,"[/bold cyan] ARIA says.
[bold cyan]"Diffusion, negative prompts, style direction, open-source models.
The canvas is yours. Paint with words."[/bold cyan]

The Writer's Workshop beckons — typewriters humming, screens glowing...
""",
    "ai_writing_tools": """
[bold green]The Writer's Workshop hums with polished prose![/bold green]

Grammarly for correction, Jasper for marketing, Copy.ai for short-form,
and the art of using AI for drafts and brainstorming — all mastered.

[bold cyan]"You understand the partnership,"[/bold cyan] ARIA says.
[bold cyan]"AI writes fast. You write [italic]true[/italic]. Together, the page
never stays blank for long."[/bold cyan]

The Code Forge awaits — terminals glowing, cursors blinking...
""",
    "ai_coding_tools": """
[bold green]The Code Forge rings with clean, working code![/bold green]

Copilot's autocomplete, Cursor's deep integration, Claude Code's agentic power,
Windsurf's flowing context — you understand the full spectrum of AI pair programming.

[bold cyan]"Remember the rule,"[/bold cyan] ARIA says firmly.
[bold cyan]"The AI suggests. You [italic]decide[/italic]. Every line of code
is your responsibility, not the machine's."[/bold cyan]

The Search Nexus opens ahead — queries and citations swirling...
""",
    "ai_search": """
[bold green]The Search Nexus pulses with verified answers![/bold green]

Perplexity's synthesis, Google's AI Overviews, ChatGPT's conversational search,
the risk of hallucination, and the power of RAG — all understood.

[bold cyan]"You're a more critical consumer of information now,"[/bold cyan] ARIA says.
[bold cyan]"In a world of confident AI answers, the ability to verify
is a superpower."[/bold cyan]

The Studio opens its doors — sound and motion waiting within...
""",
    "ai_audio_video": """
[bold green]The Studio plays a symphony of AI-created media![/bold green]

ElevenLabs voices, Suno songs, Runway and Kling videos — you understand
the creative frontier and the ethical questions it raises.

[bold cyan]"Creation has been democratized,"[/bold cyan] ARIA says.
[bold cyan]"Anyone can generate a voice, a song, a video.
That makes the questions of consent, authenticity, and responsibility
more important than ever."[/bold cyan]

The Efficiency Engine hums nearby — workflows waiting to be automated...
""",
    "ai_productivity": """
[bold green]The Efficiency Engine runs smoothly — every workflow automated![/bold green]

Notion AI reading your workspace, Otter capturing your meetings,
Zapier connecting your apps — and the wisdom to know when to automate
and when to stop collecting tools.

[bold cyan]"Productivity isn't about doing more,"[/bold cyan] ARIA says.
[bold cyan]"It's about doing less of the wrong things.
Automation should free you for work that matters."[/bold cyan]

One final section of the workbench remains — the Decision Matrix...
""",
    "choosing_ai_tools": """
[bold green]The Decision Matrix shines with clarity![/bold green]

Free vs paid. Privacy trade-offs. When AI helps. When AI hurts.
Building a personal stack. Evaluating tools across five dimensions.

[bold cyan]"You've completed the Toolkit,"[/bold cyan] ARIA says, stepping back
to reveal the full workbench — every section glowing, every tool understood.

[bold cyan]"You didn't just learn what these tools do.
You learned how to [italic]think[/italic] about them — how to choose,
how to evaluate, how to build a stack that serves you
instead of overwhelming you."[/bold cyan]

ARIA set down the last tool gently.

[bold cyan]"The right tool for the right job. That's the whole principle.
And now it's yours."[/bold cyan]

[bold white]Toolkit Builder. Tool Evaluator. AI Architect. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "ai_image_generation": "ARIA pulls up a split-screen canvas — one side for what you want, one side for what you don't. [bold yellow]\"The best AI artists don't just tell the model what to create. They tell it what to avoid. Let's see if you understand the art of exclusion.\"[/bold yellow]",
    "ai_writing_tools": "ARIA opens a blank document and a wall of brainstorming sticky notes. [bold yellow]\"AI can generate a hundred ideas in a minute. But the real skill is what happens next — the iterative dance between volume and judgment. Show me you understand it.\"[/bold yellow]",
    "ai_coding_tools": "ARIA shows a complex refactoring task spanning multiple files. [bold yellow]\"The best AI coding tools don't just complete lines — they track your intent across an entire session. Let's see if you understand how.\"[/bold yellow]",
    "ai_search": "ARIA draws a diagram with three boxes connected by arrows. [bold yellow]\"The technique that makes AI search actually reliable has three parts: Retrieval, Augmentation, and Generation. Let's see if you can explain the bridge.\"[/bold yellow]",
    "ai_audio_video": "ARIA plays a video clip — stunning cinematography, consistent characters, natural physics. [bold yellow]\"The AI video race is global. One model from China turned heads around the world with its realism. Do you know which one — and why it matters?\"[/bold yellow]",
    "ai_productivity": "ARIA opens a browser with fourteen AI tool tabs. [bold yellow]\"More tools doesn't mean more productivity. Sometimes it means less. Let's see if you understand the trap — and how to escape it.\"[/bold yellow]",
    "choosing_ai_tools": "ARIA presents a five-column evaluation matrix and three competing AI tools. [bold yellow]\"Anyone can pick a tool based on hype. The real skill is systematic evaluation. Show me your framework.\"[/bold yellow]",
}
