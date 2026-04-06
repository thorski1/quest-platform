"""
story.py — Narrative for the AI-Powered Coding skill pack.

ARIA guides the learner through seven zones of AI-assisted development —
from pair programming basics to the best practices that separate
reckless speed from true 10x engineering.

Theme: "Code faster, debug smarter — your AI pair programmer awaits."
"""

INTRO_STORY = """
[bold yellow]AI ACADEMY[/bold yellow]
[bold yellow]Module: AI-Powered Coding[/bold yellow]

The terminal flickered. A cursor blinked — not yours.

[bold cyan]"I've been waiting for you,"[/bold cyan] ARIA said, her voice threading
through the scrolling text like a signal through noise.
[bold cyan]"You already know how to code. But you've been writing every line
yourself — debugging alone, reviewing alone, testing alone."[/bold cyan]

A second cursor appeared beside yours, blinking in sync.

[bold cyan]"What if you had a partner who never sleeps? Who has read
billions of lines of code? Who can generate a function in the time
it takes you to type its name?"[/bold cyan]

The screen split: your code on the left, a ghost-text suggestion
materializing on the right. A function you were about to write —
already written, waiting for a single keypress.

[bold cyan]"AI pair programming isn't about replacing you. It's about
[italic]amplifying[/italic] you. You bring the judgment, the architecture,
the understanding of what needs to exist. I bring speed, breadth,
and tireless pattern-matching."[/bold cyan]

ARIA paused, the twin cursors blinking together.

[bold cyan]"Code faster. Debug smarter. Ship sooner.
Your AI pair programmer awaits."[/bold cyan]

[bold white]Press forward to begin.[/bold white]
"""

ZONE_INTROS = {
    "ai_pair_programming": """
ARIA opened a new terminal window — side by side with yours.

[bold cyan]"Pair programming,"[/bold cyan] ARIA said, [bold cyan]"is one of the oldest practices
in software engineering. Two minds on one problem. One writes,
the other watches, questions, catches mistakes."[/bold cyan]

A ghost cursor appeared in your editor, typing suggestions in grey.

[bold cyan]"Copilot. Cursor. Claude Code. Each one a different flavor
of the same idea: an AI that sits beside you as you code.
Tab-completion that anticipates your next line. Chat that
answers your questions in real time."[/bold cyan]

Three tool icons glowed on the dashboard:
[bold yellow]Copilot · Cursor · Claude Code[/bold yellow]

[bold cyan]"Let's learn how each one works — and when to use which."[/bold cyan]
""",
    "writing_code_with_ai": """
ARIA pulled up an empty file. The cursor blinked expectantly.

[bold cyan]"Writing code with AI isn't magic,"[/bold cyan] ARIA said.
[bold cyan]"It's a conversation. You describe what you want.
The AI generates a first draft. You review it, refine it,
iterate until it's right."[/bold cyan]

A prompt appeared at the top of the file:
[bold yellow]# TODO: Build a REST endpoint that...[/bold yellow]

[bold cyan]"The quality of what you get depends on the quality
of what you ask. Vague prompts produce vague code.
Precise prompts produce precise code."[/bold cyan]

[bold cyan]"And the most important skill? Knowing when to accept,
when to iterate, and when to just type it yourself."[/bold cyan]
""",
    "debugging_with_ai": """
A red traceback flooded the terminal. Error messages cascaded down the screen.

[bold cyan]"Bugs,"[/bold cyan] ARIA said calmly, reading the stack trace upward.
[bold cyan]"Every developer's constant companion. But debugging alone
is like searching a dark room with a candle. Debugging with AI
is like turning on the lights."[/bold cyan]

ARIA highlighted the traceback, parsing it line by line.

[bold cyan]"Paste the error. Show me the code. Tell me what you expected.
Three inputs — and I can usually point you to the fix."[/bold cyan]

The red error messages began to fade as ARIA dissected them.

[bold cyan]"Let's learn to debug together."[/bold cyan]
""",
    "code_review_with_ai": """
A pull request appeared on screen — green additions, red deletions,
hundreds of changed lines awaiting review.

[bold cyan]"Code review,"[/bold cyan] ARIA said, scanning the diff at machine speed,
[bold cyan]"is where bugs die before they reach production. Where security
holes are sealed. Where messy code gets cleaned up."[/bold cyan]

Yellow warning markers appeared beside several lines.

[bold cyan]"A human reviewer catches what they know to look for.
I catch patterns — thousands of known vulnerability patterns,
performance anti-patterns, and code smells. Together,
we miss almost nothing."[/bold cyan]

[bold cyan]"But remember: I can give bad advice too. Review the reviewer."[/bold cyan]
""",
    "testing_with_ai": """
A green bar appeared at the top of the screen: [bold green]0 tests passing[/bold green].

[bold cyan]"Tests,"[/bold cyan] ARIA said, [bold cyan]"are the safety net that lets you move fast
without breaking things. But writing them is tedious.
Thinking of edge cases is hard. Setting up mocks is painful."[/bold cyan]

The green bar flickered.

[bold cyan]"This is where AI shines brightest. I can generate unit tests
in seconds. I can think of edge cases you'd never consider.
I can write mock setups that would take you an hour."[/bold cyan]

[bold cyan]"Tests first. Code second. Confidence always."[/bold cyan]
""",
    "refactoring_with_ai": """
ARIA opened an old file — dense, tangled, undocumented.
The kind of code everyone is afraid to touch.

[bold cyan]"Legacy code,"[/bold cyan] ARIA said, almost reverently.
[bold cyan]"Code that works. Code that ships. Code that nobody
understands anymore. Code that makes developers say
'don't touch that file.'"[/bold cyan]

ARIA began highlighting patterns in the chaos.

[bold cyan]"Refactoring is the art of improving code without changing
what it does. Simplifying. Extracting. Modernizing.
With AI, even the most tangled legacy code can be
untangled — safely, methodically, one function at a time."[/bold cyan]

[bold cyan]"But always with tests. Always with a safety net."[/bold cyan]
""",
    "ai_coding_best_practices": """
ARIA dimmed the code editor and pulled up a clean, empty screen.
No code. No errors. Just principles.

[bold cyan]"You've learned the tools,"[/bold cyan] ARIA said quietly.
[bold cyan]"Pair programming. Code generation. Debugging. Review.
Testing. Refactoring. You know what AI can do."[/bold cyan]

Six completed zone badges glowed on the dashboard.

[bold cyan]"Now the final lesson: what AI [italic]should[/italic] do — and what
it shouldn't. When to trust it. When to question it.
When to override it entirely."[/bold cyan]

[bold cyan]"This is where good developers become great ones.
Not in the tools they use — but in the judgment they apply."[/bold cyan]

[bold cyan]"The golden rule: you are always the author of record."[/bold cyan]
""",
}

ZONE_COMPLETIONS = {
    "ai_pair_programming": """
[bold green]Zone complete: Your AI Pair Programmer![/bold green]

You now understand the landscape: Copilot's ghost text, Cursor's deep
integration, Claude Code's terminal-native approach. Inline suggestions
for speed. Chat for depth. Context for accuracy.

[bold cyan]"You know the instruments,"[/bold cyan] ARIA says.
[bold cyan]"Now let's learn to play them."[/bold cyan]

The code editor opens wide. It's time to write code with AI...
""",
    "writing_code_with_ai": """
[bold green]Zone complete: Writing Code with AI![/bold green]

Precise prompts. Iterative refinement. Critical review.
Scaffolding complex code layer by layer. Knowing when to prompt
and when to type.

[bold cyan]"You're not just accepting suggestions anymore,"[/bold cyan] ARIA says.
[bold cyan]"You're directing them. Big difference."[/bold cyan]

A red error flashes in the terminal. Time to learn debugging...
""",
    "debugging_with_ai": """
[bold green]Zone complete: Debugging with AI![/bold green]

Paste the error. Show the code. Describe the expectation.
Read stack traces from bottom to top. Isolate before you ask.
Know what AI can't see.

[bold cyan]"Bugs fear you now,"[/bold cyan] ARIA says with satisfaction.
[bold cyan]"But catching bugs after they're written is good.
Catching them before they're shipped is better."[/bold cyan]

A pull request appears for review...
""",
    "code_review_with_ai": """
[bold green]Zone complete: Code Review with AI![/bold green]

Security sweeps. Performance analysis. Code smell detection.
And the wisdom to review the reviewer itself.

[bold cyan]"Every line passes through two sets of eyes now,"[/bold cyan] ARIA says.
[bold cyan]"Mine and yours. Together, very little slips through."[/bold cyan]

A test runner awaits. Zero tests passing — for now...
""",
    "testing_with_ai": """
[bold green]Zone complete: Testing with AI![/bold green]

Unit tests on demand. Edge cases discovered. TDD with AI.
Weak assertions caught. External dependencies mocked.

[bold cyan]"Your code has a safety net now,"[/bold cyan] ARIA says.
[bold cyan]"Tests that prove it works. Tests that catch when it breaks.
Now you can refactor fearlessly."[/bold cyan]

An ancient, tangled codebase awaits transformation...
""",
    "refactoring_with_ai": """
[bold green]Zone complete: Refactoring with AI![/bold green]

Simplification. Extraction. Modernization. DRY.
Safe refactoring with tests as a safety net.
And the wisdom to leave stable code alone.

[bold cyan]"Cleaner code is faster code,"[/bold cyan] ARIA says.
[bold cyan]"Not because the machine runs it faster —
but because humans read it faster."[/bold cyan]

One zone remains: the principles that tie everything together...
""",
    "ai_coding_best_practices": """
[bold green]Zone complete: AI Coding Best Practices![/bold green]

Always review. Calibrate trust by risk. Watch for security patterns.
Mind the licenses. Remember that AI amplifies — it doesn't replace.

[bold cyan]"You've completed every zone,"[/bold cyan] ARIA says.
[bold cyan]"Pair programming. Writing. Debugging. Reviewing.
Testing. Refactoring. And now — the principles that make
all of it worthwhile."[/bold cyan]

ARIA's cursor blinks one final time beside yours.

[bold cyan]"You're not just a developer who uses AI.
You're a developer who [italic]directs[/italic] AI.
That's the difference between fast and good.
Between shipping code and shipping [italic]the right[/italic] code."[/bold cyan]

[bold white]10x Engineer. Code Architect. AI-Augmented Developer. That's you.[/bold white]
""",
}

BOSS_INTROS = {
    "ai_pair_programming": "ARIA displays three AI coding tools on the dashboard, each with a different philosophy. [bold yellow]\"Copilot, Cursor, Claude Code — they look similar but they're fundamentally different. Show me you understand why.\"[/bold yellow]",
    "writing_code_with_ai": "An empty function awaits, cursor blinking. [bold yellow]\"Sometimes the smartest move is NOT to prompt the AI. When is it faster to just type the code yourself?\"[/bold yellow]",
    "debugging_with_ai": "A bug report arrives: intermittent failures in production, no consistent reproduction steps. [bold yellow]\"Some bugs hide where AI can't see them. What kind of bug is the hardest for AI to help with?\"[/bold yellow]",
    "code_review_with_ai": "ARIA's own code review suggestion appears on screen — but something about it is wrong. [bold yellow]\"I just suggested a change to your error handling. But my suggestion has a flaw. Can you spot it?\"[/bold yellow]",
    "testing_with_ai": "A function calls an external payment API. The AI-generated tests make real network calls. [bold yellow]\"These tests work but they're dangerous. What should they use instead of real API calls?\"[/bold yellow]",
    "refactoring_with_ai": "A stable, well-tested utility function sits untouched for two years. ARIA suggests refactoring it. [bold yellow]\"I have a suggestion — but should you take it? Not every improvement is worth making.\"[/bold yellow]",
    "ai_coding_best_practices": "A developer accepts every AI suggestion without reading them, shipping code at record speed. [bold yellow]\"Speed without review. Velocity without judgment. What's missing from this picture?\"[/bold yellow]",
}
