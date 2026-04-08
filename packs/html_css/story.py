"""
story.py - Narrative text for HTML & CSS Foundations
Cyberpunk web-building narrative with ARIA, the AI guide.
"""

INTRO_STORY = """
The year is 2087. The [bold cyan]Metaframe[/bold cyan] — a single corporate rendering engine —
controls every pixel on every screen on the planet. One company. One renderer. One reality.

But the Metaframe has a secret the corps buried under seventeen layers of proprietary abstraction:
it still runs on [bold white]HTML and CSS[/bold white]. The same markup language that powered the
first web pages in 1993. The same styling system that taught a generation of developers that
centering a div was a spiritual practice.

The corps don't want you to know this. They want you dependent on their drag-and-drop builders,
their visual editors, their "no-code" platforms that generate markup so bloated it takes three
seconds to render a button. They want you to believe the web is [italic]their[/italic] product.

It isn't. The web is a [bold cyan]document[/bold cyan]. Always was. And documents are written in
[bold white]markup[/bold white].

You've been contacted by [bold magenta]ARIA[/bold magenta] — an autonomous AI that lives inside the
Metaframe's rendering pipeline. ARIA has seen what the corps are doing: locking down the DOM,
deprecating standards, replacing open protocols with proprietary APIs. ARIA needs someone who
can write raw markup. Someone who understands the foundation layer.

[bold magenta]ARIA[/bold magenta]: "I can show you the rendering pipeline from the inside. Every
element, every selector, every layout algorithm. But you need to learn to write it yourself.
The Metaframe won't accept generated code from my layer — only hand-authored markup passes
the integrity checks."

[bold cyan]Jack in. The DOM is waiting.[/bold cyan]
"""

ZONE_INTROS = {
    "html_elements": """
[bold cyan]== THE DOCUMENT CORE ==[/bold cyan]

[bold magenta]ARIA[/bold magenta]: "This is where everything begins. Before styles, before scripts,
before frameworks — there is the [bold white]document[/bold white]. Raw HTML. Semantic elements that
tell the Metaframe what things [italic]are[/italic], not what they look like."

The corps stopped teaching this. They skipped straight to components and templates,
and an entire generation of developers can build a landing page but can't explain what
a [yellow]<section>[/yellow] means or why [yellow]<article>[/yellow] exists.

[yellow]<div>[/yellow], [yellow]<span>[/yellow], [yellow]<h1>[/yellow] through [yellow]<h6>[/yellow],
[yellow]<p>[/yellow], [yellow]<a>[/yellow], [yellow]<img>[/yellow], [yellow]<ul>[/yellow], [yellow]<ol>[/yellow]
— the atomic elements of the web. Every framework component eventually renders to these.

[italic]"A div with the right class is just a div. A semantic element with no class at all
tells the browser — and every screen reader — exactly what it is."[/italic]
""",
    "forms_inputs": """
[bold cyan]== THE INPUT GATEWAY ==[/bold cyan]

[bold magenta]ARIA[/bold magenta]: "The corps collect data from billions of users every day, and
most of those users have never seen the mechanism that makes it possible. Forms. Inputs.
The original interactive layer of the web."

Before JavaScript. Before SPAs. Before React state management and Redux stores and
Zustand atoms — there were [bold white]HTML forms[/bold white]. They submitted data to servers
using HTTP methods that haven't changed since 1996. They still work. They'll work after
every framework in your node_modules is deprecated and forgotten.

[yellow]<form>[/yellow], [yellow]<input>[/yellow], [yellow]<select>[/yellow], [yellow]<textarea>[/yellow],
[yellow]<button>[/yellow], [yellow]<label>[/yellow] — the data collection toolkit. Validation
attributes that work without a single line of JavaScript.

[italic]"The corps added 200KB of form validation libraries to do what the browser
does natively in zero bytes."[/italic]
""",
    "css_selectors": """
[bold cyan]== THE SELECTOR MATRIX ==[/bold cyan]

[bold magenta]ARIA[/bold magenta]: "CSS selectors are the targeting system of the Metaframe. Every
pixel you see on screen was selected and styled by a rule. Understanding selectors means
understanding [bold white]how the renderer thinks[/bold white]."

The corps want you using utility classes — pre-built, pre-approved, pre-abstracted. They
don't want you understanding specificity, cascading, or inheritance because those concepts
give you power over their design systems.

[yellow].[/yellow] class, [yellow]#[/yellow] id, [yellow]>[/yellow] child, [yellow]+[/yellow] sibling,
[yellow]:hover[/yellow], [yellow]:nth-child()[/yellow], [yellow]::before[/yellow], [yellow]::after[/yellow]
— the precision targeting toolkit. One selector can reach into any part of the DOM
and reshape it.

[italic]"Specificity is not a bug. Specificity is the cascade doing exactly
what you told it to do."[/italic]
""",
    "flexbox_grid": """
[bold cyan]== THE LAYOUT ENGINE ==[/bold cyan]

[bold magenta]ARIA[/bold magenta]: "For twenty years, developers used [yellow]float[/yellow] hacks and
[yellow]display: table[/yellow] tricks to lay out pages. It was brutal. It was brittle.
It was the web's dark age. Then Flexbox and Grid arrived — and the dark age ended."

The Metaframe's layout engine is built on two systems: [bold white]Flexbox[/bold white] for
one-dimensional flow, and [bold white]CSS Grid[/bold white] for two-dimensional structure.
Together, they solve every layout problem that made the previous generation of
web developers question their career choices.

[yellow]display: flex[/yellow], [yellow]justify-content[/yellow], [yellow]align-items[/yellow],
[yellow]display: grid[/yellow], [yellow]grid-template-columns[/yellow], [yellow]gap[/yellow]
— the spatial control system. Centering a div is no longer a spiritual journey.

[italic]"The corps still ship 40KB of grid frameworks. The browser has one built in.
It's free. It always was."[/italic]
""",
    "responsive_design": """
[bold cyan]== THE VIEWPORT FORGE ==[/bold cyan]

[bold magenta]ARIA[/bold magenta]: "The Metaframe renders on screens from 320 pixels wide to 3840.
Watches. Phones. Tablets. Desktops. Projectors. The same HTML, the same CSS, adapting
to every viewport. That's not magic — that's [bold white]responsive design[/bold white]."

The corps sell 'mobile-first' as a feature. It's not a feature. It's a [italic]methodology[/italic].
Write styles for the smallest screen first. Layer complexity as the viewport grows.
The cascade does the rest.

[yellow]@media[/yellow] queries, [yellow]min-width[/yellow], [yellow]max-width[/yellow],
[yellow]clamp()[/yellow], [yellow]rem[/yellow], [yellow]vw[/yellow], [yellow]vh[/yellow]
— the adaptive toolkit. Fluid typography, flexible grids, images that never
overflow their containers.

[italic]"If your site doesn't work on a phone, it doesn't work.
Fifty-eight percent of all web traffic is mobile. The corps know this.
Their own dashboards still break at 375px."[/italic]
""",
}

ZONE_COMPLETIONS = {
    "html_elements": """
[bold green]THE DOCUMENT CORE — MASTERED.[/bold green]

[bold magenta]ARIA[/bold magenta]: "You write semantic HTML. Do you know how rare that is? Most developers
reach for a div first and ask questions never. You understand what elements [italic]mean[/italic],
not just what they render."

The Metaframe's integrity checker nods silently. Your markup is clean, accessible,
and semantically correct. Screen readers parse it flawlessly. Search engines index it
instantly. [bold cyan]The Input Gateway awaits.[/bold cyan]
""",
    "forms_inputs": """
[bold green]THE INPUT GATEWAY — ONLINE.[/bold green]

[bold magenta]ARIA[/bold magenta]: "You can collect data from any user on any device using nothing
but HTML attributes. No JavaScript. No libraries. No 200KB validation packages. Just the
platform, doing what it was designed to do."

Your forms validate themselves. Your inputs are labeled. Your buttons have types.
The corps' UI framework engineers would weep.
[bold cyan]The Selector Matrix is next.[/bold cyan]
""",
    "css_selectors": """
[bold green]THE SELECTOR MATRIX — DECODED.[/bold green]

[bold magenta]ARIA[/bold magenta]: "You understand specificity now. You can predict which rule wins
without opening DevTools. That's not CSS knowledge — that's [bold white]CSS fluency[/bold white]."

The cascade flows through your selectors with precision. No !important hacks.
No specificity wars. Just clean, predictable, maintainable style rules.
[bold cyan]The Layout Engine beckons.[/bold cyan]
""",
    "flexbox_grid": """
[bold green]THE LAYOUT ENGINE — UNDER CONTROL.[/bold green]

[bold magenta]ARIA[/bold magenta]: "You centered a div on your first try. I've watched senior developers
spend forty-five minutes on that. Flexbox and Grid are your native layout languages now."

Columns align. Rows flow. Gaps are consistent. Your layouts adapt and restructure
without a single line of JavaScript.
[bold cyan]The Viewport Forge is the final test.[/bold cyan]
""",
    "responsive_design": """
[bold yellow]* * *  THE VIEWPORT FORGE — COMPLETE.  * * *[/bold yellow]

[bold magenta]ARIA[/bold magenta]: "[bold white]You've done it.[/bold white] You can build a complete,
accessible, responsive web page using nothing but HTML and CSS. No framework. No build step.
No node_modules folder larger than the moon landing source code."

Your markup is semantic. Your styles cascade cleanly. Your layouts adapt to every
viewport from smartwatch to ultrawide. The Metaframe renders your code in under 16
milliseconds.

[bold yellow]DOCUMENT STATUS: FOUNDATION COMPLETE. MARKUP: MASTERED.[/bold yellow]
""",
}

BOSS_INTROS = {
    "html_elements": "[bold red]@ INTEGRITY CHECK: The Element Gauntlet[/bold red]\nThe Metaframe's validator is scanning your markup. Every element must be semantic. Every tag must close. No mercy.",
    "forms_inputs": "[bold red]@ VALIDATION SWEEP: The Form Crucible[/bold red]\nARIA is stress-testing your forms. Edge cases. Required fields. Pattern matching. The browser does the work — if you wired it correctly.",
    "css_selectors": "[bold red]@ SPECIFICITY AUDIT: The Cascade Trial[/bold red]\nMultiple rules target the same element. Which one wins? The cascade doesn't guess. Neither should you.",
    "flexbox_grid": "[bold red]@ LAYOUT STRESS TEST: The Alignment Matrix[/bold red]\nComplex layouts. Nested grids. Dynamic content. The layout engine is watching. Every pixel counts.",
    "responsive_design": "[bold red]* VIEWPORT CHALLENGE: The Breakpoint Gauntlet[/bold red]\nYour design must survive every screen size. 320px to 2560px. Media queries. Fluid units. Adapt or break.",
}

ACHIEVEMENT_DESCRIPTIONS = {
    "first_blood": ("First Tag", "Wrote your first HTML element. The DOM acknowledged you. Welcome to the document."),
    "element_master": ("Semantic Scholar", "Mastered HTML elements. You write markup that means something — not just div soup."),
    "form_builder": ("Data Collector", "Conquered forms and inputs. You collect user data with native validation and zero JavaScript."),
    "selector_sage": ("Cascade Whisperer", "Decoded CSS selectors. Specificity holds no mysteries. The cascade obeys your rules."),
    "layout_lord": ("Grid Commander", "Mastered Flexbox and Grid. Layouts bend to your will. Centering a div takes you one line."),
    "responsive_ace": ("Viewport Sovereign", "Completed responsive design. Your pages adapt to every screen. The Metaframe renders them flawlessly."),
    "streak_3": ("Signal Locked", "3 correct in a row. Your markup flows without hesitation."),
    "streak_5": ("DOM Walker", "5 correct in a row. The rendering pipeline accepts you as a native speaker."),
    "streak_10": ("METAFRAME NATIVE", "10 correct in a row. ARIA has nothing left to teach you about the foundation layer."),
    "no_hints": ("Clean Render", "Cleared a zone without hints. Pure knowledge. No DevTools. No Stack Overflow."),
    "speed_demon": ("Hot Reload", "Answered in under 5 seconds. Faster than the browser's paint cycle."),
    "level_10": ("Markup Apprentice", "Level 10. You see the DOM where others see pixels."),
    "level_20": ("Style Architect", "Level 20. CSS is your native language. HTML is your mother tongue."),
    "level_30": ("Foundation Legend", "Maximum level. The web's foundation layer is yours. Every framework builds on what you now command."),
    "completionist": ("Full Render", "Every challenge. Every zone. Every element, selector, and breakpoint. The foundation is complete."),
    "boss_slayer": ("Validator Bypassed", "Beat your first boss challenge. The Metaframe's integrity checker approved your code."),
}
