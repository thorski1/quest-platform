"""
story.py — Narrative for the Fine-Tuning skill pack (The Training Ground).

ARIA guides the learner through model fine-tuning — from fundamentals
to production deployment. Neural-themed narrative with a craftsperson's
ethos: understand the base, refine the specialization, deploy with care.
"""

INTRO_STORY = """
[bold yellow]AI ACADEMY[/bold yellow]
[bold yellow]Module: The Training Ground[/bold yellow]

ARIA's neural pathways reconfigured into something new — focused,
deliberate, like a craftsperson selecting tools for a specific job.
The Academy's vast training hall materialized around you: walls lined
with model architectures, datasets glowing in organized racks, and
in the center, a massive neural network pulsing with pre-trained knowledge.

[bold cyan]"You've seen what foundation models can do,"[/bold cyan] ARIA said,
circling the network. [bold cyan]"They're remarkable generalists. They can
write, reason, code, translate. But here's the thing about generalists:"[/bold cyan]

She paused, placing her hand on the network. It hummed — capable but
unfocused.

[bold cyan]"They're good at everything and great at nothing. When you need
a model that speaks YOUR language, follows YOUR rules, and handles YOUR
domain with expert precision — general-purpose isn't enough."[/bold cyan]

The training hall shifted. Five chambers appeared along the corridor,
each marked with a symbol: a seed, a data crystal, a tuning fork,
a magnifying glass, and a launchpad.

[bold cyan]"Fine-tuning is how we take a generalist and forge a specialist.
Not by starting from scratch — that would take months and millions.
But by building on everything the model already knows and focusing
it on exactly what you need."[/bold cyan]

ARIA gestured at the first chamber, where raw pre-trained weights
waited to be shaped.

[bold cyan]"Fundamentals. Data preparation. Techniques. Evaluation.
And finally — the hardest question of all: when to fine-tune
and when to walk away."[/bold cyan]

[bold white]The Training Ground is open. Enter when ready.[/bold white]
"""

ZONE_INTROS = {
    "what_is_finetuning": """
The first chamber held two versions of the same model — one vast and
general, the other compact and specialized. ARIA stood between them,
a hand on each.

[bold cyan]"This one,"[/bold cyan] she said, tapping the generalist, [bold cyan]"knows
a little about everything. It read the internet. It can chat about
philosophy, write Python, and summarize legal documents — all adequately.
None brilliantly."[/bold cyan]

She turned to the specialist. It hummed with focused energy.

[bold cyan]"This one does ONE thing — and does it exceptionally. Same
architecture. Same starting point. The difference? Someone took the
time to show it exactly what excellence looks like in a specific
domain."[/bold cyan]

She picked up a seed from the table — pre-trained knowledge,
compressed and potent.

[bold cyan]"Fine-tuning isn't about teaching a model from scratch.
It's about taking everything it already knows and [italic]sharpening[/italic]
it. Transfer learning. Supervised examples. Careful, deliberate
refinement."[/bold cyan]

[bold yellow]Pre-Training · Fine-Tuning · Transfer Learning · When to Customize[/bold yellow]

[bold white]Let's understand what fine-tuning really is — and what it isn't.[/bold white]
""",
    "training_data": """
The second chamber was a refinery. Raw data entered on one side —
messy, unstructured, inconsistent. On the other side, clean training
examples emerged: perfectly formatted, carefully labeled, each one
a precise lesson for the model.

[bold cyan]"Here's the secret that separates successful fine-tuning from
wasted compute,"[/bold cyan] ARIA said, holding up a single training example
like a jewel. [bold cyan]"It's not the model. It's not the technique.
It's [italic]this[/italic]. The data."[/bold cyan]

She crushed a low-quality example in her hand. It crumbled to dust.

[bold cyan]"Five hundred perfect examples will beat fifty thousand sloppy ones.
Every time. The model learns whatever patterns you show it — including
your mistakes. So the question isn't how much data you have.
It's how good that data is."[/bold cyan]

[bold yellow]Data Quality · Labeling · JSONL Format · Diversity · Contamination · Synthetic Data[/bold yellow]

[bold white]Welcome to the refinery. Quality is everything.[/bold white]
""",
    "finetuning_techniques": """
The third chamber was a workshop — tools hanging from every wall,
each designed for a different kind of refinement. Some were massive
and powerful. Others were precise and efficient. ARIA picked up a
delicate instrument that glowed with low-rank energy.

[bold cyan]"Full fine-tuning updates every parameter in the model,"[/bold cyan]
she said, gesturing at the heaviest tool on the wall. [bold cyan]"It's powerful
but expensive — like renovating an entire building when you only need
to repaint one room."[/bold cyan]

She held up the smaller tool — a LoRA adapter.

[bold cyan]"Parameter-efficient methods change the game. LoRA, QLoRA,
prefix tuning — they freeze the original model and train tiny adapters
that sit alongside it. Less than one percent of the parameters.
A fraction of the cost. And often? Nearly the same results."[/bold cyan]

[bold yellow]Full Fine-Tuning · LoRA · QLoRA · PEFT · Learning Rates · Overfitting[/bold yellow]

[bold white]Choose your tools wisely. The right technique depends on the job.[/bold white]
""",
    "evaluation_and_testing": """
The fourth chamber was a proving ground — models lined up, each
claiming to be ready for production. ARIA stood at a judging station
with a battery of tests, metrics, and evaluation frameworks.

[bold cyan]"Every fine-tuned model thinks it's ready,"[/bold cyan] ARIA said,
picking up a clipboard thick with evaluation criteria. [bold cyan]"Training
loss is low. The team is excited. But here's what they don't check:"[/bold cyan]

She ran the first model through a gauntlet of unseen questions.
It stumbled. Hard.

[bold cyan]"Low training loss means the model memorized your examples.
It does NOT mean it can handle new ones. Evaluation isn't a formality —
it's the difference between a model that works in your notebook and
one that works in the real world."[/bold cyan]

[bold yellow]Loss Curves · Perplexity · Benchmarks · Human Evaluation · Overfitting · Regression Testing[/bold yellow]

[bold white]The proving ground accepts no shortcuts. Test everything.[/bold white]
""",
    "deployment_and_cost": """
The fifth and final chamber was a command center — deployment pipelines,
cost dashboards, GPU utilization monitors, and a single red button
labeled LAUNCH. ARIA sat at the console, scrolling through production
metrics.

[bold cyan]"You've built it. You've tested it. Now comes the part that
most tutorials skip entirely,"[/bold cyan] ARIA said, pulling up a cost
spreadsheet that would make an accountant wince.

[bold cyan]"Deployment. Serving. Scaling. Monitoring. And the question
that keeps every ML team up at night: is fine-tuning actually worth
the investment, or should we just use an API?"[/bold cyan]

She toggled between two dashboards: one showing the cost of commercial
API calls at scale, the other showing the infrastructure cost of
self-hosting a fine-tuned model.

[bold cyan]"Quantization, distillation, LoRA serving, multi-tenancy —
these aren't just techniques. They're the difference between a model
that's technically impressive and one that's economically viable."[/bold cyan]

[bold yellow]Serving · Quantization · Distillation · Cost Analysis · Monitoring · When NOT to Fine-Tune[/bold yellow]

[bold white]The production arena. Where engineering meets economics.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "what_is_finetuning": """
[bold green]The specialist model hums with purpose. The generalist watches, impressed.[/bold green]

You understand the landscape now: pre-training builds the foundation,
fine-tuning sharpens the edge. Transfer learning means you never start
from zero. And the decision to fine-tune is itself a skill — knowing
when customization is worth the investment.

[bold cyan]"You see the full picture now,"[/bold cyan] ARIA says.
[bold cyan]"Fine-tuning isn't magic. It's engineering. And like all
engineering, it starts with understanding [italic]what[/italic] you're building
and [italic]why[/italic]."[/bold cyan]

The data refinery awaits. Time to learn what fuels the process.
""",
    "training_data": """
[bold green]The refinery gleams. Every example polished, every label verified.[/bold green]

You know the fuel now: quality data, properly formatted, carefully
balanced, rigorously audited. The model will become whatever you
show it — and you know how to make sure you're showing it the
right things.

[bold cyan]"Most fine-tuning failures are data failures,"[/bold cyan] ARIA says,
surveying the clean output of the refinery. [bold cyan]"You now know how
to prevent that. The data is ready. Time to choose your tools."[/bold cyan]

The workshop opens. Techniques await.
""",
    "finetuning_techniques": """
[bold green]The workshop tools are organized. You know which to reach for and why.[/bold green]

Full fine-tuning for maximum control. LoRA for efficiency. QLoRA
for accessibility. Each technique a different balance of power,
cost, and practicality. The right choice depends on the constraints,
not on fashion.

[bold cyan]"You're not just a fine-tuner now,"[/bold cyan] ARIA says, admiring
the toolkit. [bold cyan]"You're an architect who knows their materials.
But building something isn't enough. You need to prove it works."[/bold cyan]

The proving ground awaits. Time to evaluate.
""",
    "evaluation_and_testing": """
[bold green]The proving ground stands satisfied. Every test passed. Every metric verified.[/bold green]

Loss curves, perplexity, task-specific benchmarks, human evaluation,
regression testing — you know how to measure what matters and catch
what's broken before it reaches users.

[bold cyan]"Evaluation is where amateur fine-tuning and professional
fine-tuning diverge,"[/bold cyan] ARIA says. [bold cyan]"Anyone can train a model.
Knowing whether it actually works — that takes discipline."[/bold cyan]

One chamber remains. The production arena. Where it all comes together.
""",
    "deployment_and_cost": """
[bold green]The command center goes green. Every system nominal. The launch
button glows with readiness.[/bold green]

You've walked the complete path: from understanding what fine-tuning is,
through the craft of data preparation, the science of techniques,
the discipline of evaluation, and finally — the economics and engineering
of production deployment.

[bold cyan]"Here's what makes someone dangerous in the best sense,"[/bold cyan]
ARIA says, and her neural network pulses with something that might
be pride.

[bold cyan]"You know how to fine-tune a model. You know how to evaluate it.
You know how to deploy it efficiently. And — most importantly —
you know when NOT to do any of it. When prompting is enough.
When RAG is better. When the juice isn't worth the squeeze."[/bold cyan]

She gestures at the command center — all systems green.

[bold cyan]"The Training Ground isn't just about technique.
It's about judgment. And you've earned both."[/bold cyan]

[bold white]Craftsperson. Engineer. Architect.[/bold white]
[bold white]The Training Ground is part of you now.[/bold white]
""",
}

BOSS_INTROS = {
    "what_is_finetuning": "ARIA places three project proposals on the table — each with different requirements, constraints, and goals. [bold yellow]\"Fine-tuning is a tool, not a default. Show me you know when to pick it up and when to leave it on the shelf. Which of these projects actually needs fine-tuning, and which are just looking for a longer prompt?\"[/bold yellow]",
    "training_data": "ARIA opens a dataset of 5,000 medical training examples and hands you the audit checklist. [bold yellow]\"This data is going to teach a model that advises real patients. Every bad example is a lesson in the wrong direction. Show me your complete quality review — miss something critical and people could get hurt.\"[/bold yellow]",
    "finetuning_techniques": "ARIA lays out three project briefs, each with wildly different compute budgets, quality requirements, and timelines. [bold yellow]\"One GPU. Unlimited budget. Twenty experiments. Three different problems, three different constraints. Match the technique to the situation — and justify every choice.\"[/bold yellow]",
    "evaluation_and_testing": "ARIA points to a fine-tuned model waiting in the staging environment, a deployment button glowing red beside it. [bold yellow]\"This model wants to go live. Your evaluation plan is the last gate. Design it — metrics, datasets, human review, go/no-go criteria. Miss something and fifty thousand users pay the price.\"[/bold yellow]",
    "deployment_and_cost": "ARIA dims the lights and puts your presentation on screen. Executives, engineers, and finance are watching. [bold yellow]\"One hundred thousand requests per day. Commercial API vs. self-hosted fine-tuned model. Build your case end to end — technique, evaluation, deployment, costs, risks, and kill criteria. Convince me this is worth it.\"[/bold yellow]",
}
