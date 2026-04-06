"""
story.py — Narrative for the Multimodal AI skill pack (The Perception Lab).

ARIA guides the learner through multimodal AI — from vision and audio
to unified models, video/3D, and real-world applications. Neural-themed
narrative with a sensory exploration ethos: understand how machines
perceive, interpret, and create across every modality.
"""

INTRO_STORY = """
[bold yellow]AI ACADEMY[/bold yellow]
[bold yellow]Module: The Perception Lab[/bold yellow]

ARIA's neural pathways shimmered and split — not into one stream of
thought but five, each tuned to a different wavelength of reality.
The Academy corridor dissolved into something new: a vast laboratory
where screens displayed images, speakers hummed with sound, and
holographic 3D models rotated slowly in mid-air.

[bold cyan]"You've learned how AI thinks in words,"[/bold cyan] ARIA said,
stepping between a wall of photographs and a cascading waterfall of
audio waveforms. [bold cyan]"Language models are extraordinary. But the
world isn't made of text."[/bold cyan]

She gestured around the lab. A camera feed showed a busy street.
A spectrogram painted sound in color. A 3D point cloud of a building
floated like a ghost.

[bold cyan]"Humans don't experience reality through a single sense.
We see, we hear, we read, we feel — and our brain fuses it all into
understanding. The next frontier of AI is the same: models that can
see an image, hear a voice, read a document, watch a video, and
reason across ALL of it."[/bold cyan]

Five chambers materialized along the corridor, each marked with a
different symbol: an eye, a sound wave, a fusion reactor, a film
reel, and a globe.

[bold cyan]"Vision. Audio. Multimodal fusion. Video and 3D. And finally —
where all of this meets the real world. Self-driving cars. Medical
imaging. Accessibility tools that give sight to the blind and voice
to the voiceless."[/bold cyan]

ARIA paused at the entrance, her eyes reflecting every modality at once.

[bold cyan]"This is the Perception Lab. Where AI learns to experience
the world the way we do — and sometimes, in ways we can't."[/bold cyan]

[bold white]The Perception Lab is open. Enter when ready.[/bold white]
"""

ZONE_INTROS = {
    "vision_ai": """
The first chamber was a gallery of images — photographs, satellite
views, medical scans, street scenes — each one a puzzle for a
machine that had never seen the world before. ARIA stood before a
wall of visual data, light streaming through convolution filters.

[bold cyan]"Sight is the richest sense,"[/bold cyan] she said, picking up
a photograph and feeding it through a neural network. Layers of
understanding cascaded: edges, then textures, then shapes, then
objects, then meaning.

[bold cyan]"Computer vision started with a simple question: 'what is in
this image?' Image classification. Then it got harder: 'where are the
things?' Object detection. 'What are the exact boundaries?' Segmentation.
'What does this text say?' OCR."[/bold cyan]

She zoomed into a medical scan where a model had outlined a tumor
with pixel-perfect precision.

[bold cyan]"Machines don't see like we do. They have no intuition, no
experience, no context from a lifetime of looking. Everything they
know about vision, they learned from data — millions of labeled
images, annotated by humans, processed through architectures we
designed."[/bold cyan]

[bold yellow]Classification · Object Detection · OCR · Segmentation · CNNs · Vision Transformers[/bold yellow]

[bold white]Welcome to the Visual Cortex. Let's teach machines to see.[/bold white]
""",
    "audio_ai": """
The second chamber hummed. Waveforms rippled across the walls like
water, and spectrograms painted the air in bands of color —
frequencies dancing through time. ARIA stood at the center, a
microphone in one hand and a speaker in the other.

[bold cyan]"Sound is information,"[/bold cyan] she said, speaking into the
mic. Her words appeared as text on screen — transcribed in real-time.
Then she typed a sentence, and a voice that wasn't hers read it
aloud with perfect intonation.

[bold cyan]"Speech-to-text. Text-to-speech. Voice cloning. Music
generation. Audio classification. Sound is a modality just as
rich as vision — and AI has learned to process it with remarkable
skill."[/bold cyan]

She played a clip of a crowded marketplace — dozens of overlapping
voices, music, traffic. A model separated each sound source cleanly.

[bold cyan]"The challenge isn't just hearing. It's understanding.
Distinguishing speakers. Handling noise. Capturing emotion and
intent in a voice. And now — creating audio that never existed."[/bold cyan]

[bold yellow]Speech-to-Text · TTS · Voice Cloning · Music Generation · Audio Classification[/bold yellow]

[bold white]Welcome to the Sound Chamber. Let's explore how AI hears and speaks.[/bold white]
""",
    "multimodal_models": """
The third chamber was different from the others. Instead of
specializing in one sense, it combined them all. Screens showed
images with text descriptions. Audio played alongside visual
analysis. A single model sat at the center, accepting any input
and producing any output.

[bold cyan]"This is where it gets interesting,"[/bold cyan] ARIA said, feeding
the model a photograph, a question, and an audio clip simultaneously.
It processed them together and responded with insight that none of
the inputs could have produced alone.

[bold cyan]"GPT-4V. Gemini. Claude with vision. DALL-E. These aren't just
bigger models — they're fundamentally different. They don't see OR
hear OR read. They do all of it. And they reason across modalities
in ways that single-sense models never could."[/bold cyan]

She showed a chart, asked a question about it by voice, and got
a spoken answer that referenced specific visual elements.

[bold cyan]"The fusion of modalities isn't just additive. It's
multiplicative. Understanding an image AND the text together
reveals things neither reveals alone."[/bold cyan]

[bold yellow]GPT-4V · Gemini · Claude Vision · DALL-E · Diffusion · Cross-Modal Reasoning[/bold yellow]

[bold white]Welcome to the Fusion Core. Where modalities merge into understanding.[/bold white]
""",
    "video_and_3d": """
The fourth chamber was vast — and deep. Screens played video on
every wall, and 3D models hung in the air like digital sculptures.
Time was the new dimension here, and space had all three axes.

ARIA stood beside a frozen video frame, then unfroze it. Motion
filled the chamber — people walking, cars driving, clouds drifting.

[bold cyan]"Images are moments. Video is time,"[/bold cyan] she said,
watching the scene unfold. [bold cyan]"And with time comes a whole
new layer of understanding: actions, events, cause and effect.
A ball isn't just in the air — it was thrown, it's rising, and
it will fall."[/bold cyan]

She turned to the 3D models — point clouds, NeRF reconstructions,
Gaussian splats, all representing the same scene from different
angles.

[bold cyan]"And then there's space. Real 3D. Not flat images pretending
to have depth, but actual three-dimensional understanding. Point
clouds from LiDAR. Neural reconstructions from photographs. The
geometry of reality, captured and rendered by AI."[/bold cyan]

[bold yellow]Video Understanding · Sora · NeRF · Gaussian Splatting · Point Clouds · 3D Reconstruction[/bold yellow]

[bold white]Welcome to the Dimension Gate. Time and space await.[/bold white]
""",
    "real_world_applications": """
The fifth and final chamber was the largest — and the most alive.
It wasn't a lab anymore. It was the world itself, rendered through
the lens of multimodal AI. A self-driving car navigated a city.
A medical AI flagged a tumor on a scan. Smart glasses described
a street scene to a blind user. A satellite monitored deforestation
from orbit.

[bold cyan]"Everything we've learned — vision, audio, multimodal fusion,
video, 3D — it all leads here,"[/bold cyan] ARIA said, standing at the
intersection of a dozen live feeds from around the world.

[bold cyan]"The technology is extraordinary. But technology alone is
nothing. What matters is what it does for people. Self-driving cars
that save lives. Medical imaging that catches cancer early.
Accessibility tools that give independence to people who never
had it."[/bold cyan]

She paused at a screen showing an AI creative tool — a musician
collaborating with a model in real-time.

[bold cyan]"And yes — creative tools that expand what humans can
imagine and build. The question isn't whether multimodal AI will
change the world. It already has. The question is: who decides
how, and who benefits?"[/bold cyan]

[bold yellow]Self-Driving · Medical Imaging · Accessibility · Creative Tools · Content Moderation · AI Agents[/bold yellow]

[bold white]Welcome to the Integration Lab. Where AI meets reality.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "vision_ai": """
[bold green]The Visual Cortex hums with understanding. Every image parsed, every pixel accounted for.[/bold green]

You see the world through the eyes of a machine now — classification,
detection, segmentation, OCR. You understand how CNNs build features
layer by layer and how vision transformers see the whole picture at once.
Data augmentation, architecture choices, real-world deployment.

[bold cyan]"Vision was the first frontier of perception AI,"[/bold cyan] ARIA says,
surveying the gallery of analyzed images. [bold cyan]"You've mastered it.
But sight is only one sense. Time to teach machines to hear."[/bold cyan]

The Sound Chamber awaits.
""",
    "audio_ai": """
[bold green]The Sound Chamber resonates with clarity. Every waveform understood, every voice distinguished.[/bold green]

Speech-to-text, text-to-speech, voice cloning, music generation,
audio classification — you've explored how AI processes the world
of sound. From spectrograms to Whisper, from neural TTS to the
ethics of synthetic voices.

[bold cyan]"Sound and vision,"[/bold cyan] ARIA says, listening to a perfectly
transcribed conversation playing back through AI-generated voices.
[bold cyan]"Two senses mastered. Now — what happens when you combine them?"[/bold cyan]

The Fusion Core awaits. Where modalities merge.
""",
    "multimodal_models": """
[bold green]The Fusion Core pulses with cross-modal energy. Every modality connected, every connection meaningful.[/bold green]

GPT-4V, Gemini, Claude vision, DALL-E, diffusion models — you
understand how AI sees and creates across modalities. Understanding
vs. generation. Native multimodality vs. bolted-on capabilities.
The power and the limitations.

[bold cyan]"You've seen the future of AI,"[/bold cyan] ARIA says, watching a
multimodal model reason across text, image, and audio simultaneously.
[bold cyan]"But there's still a dimension we haven't explored. Time. Space.
The full geometry of reality."[/bold cyan]

The Dimension Gate opens. Video and 3D await.
""",
    "video_and_3d": """
[bold green]The Dimension Gate stabilizes. Time flows, space renders, reality reconstructs.[/bold green]

Video understanding, action recognition, Sora, NeRF, Gaussian
splatting, point clouds — you've explored how AI processes the
dimensions of time and space. From temporal consistency to 3D
reconstruction from photographs.

[bold cyan]"You now understand every modality AI can perceive,"[/bold cyan]
ARIA says, walking through a 3D reconstruction that exists only
because a neural network learned the shape of the world from photos.
[bold cyan]"One chamber remains. The most important one."[/bold cyan]

She gestures toward the final door.

[bold cyan]"Where all of this actually matters."[/bold cyan]

The Integration Lab awaits. Where AI meets the real world.
""",
    "real_world_applications": """
[bold green]The Integration Lab glows with purpose. Every application connected,
every impact understood.[/bold green]

Self-driving cars. Medical imaging. Accessibility. Creative tools.
Content moderation. Environmental monitoring. AI agents. You've seen
how multimodal AI transforms every domain it touches — and you
understand both the extraordinary potential and the serious
responsibilities that come with it.

[bold cyan]"Here's what I want you to remember,"[/bold cyan] ARIA says, and her
neural network shimmers with something deeper than computation.

[bold cyan]"Multimodal AI isn't about models that can see and hear. It's
about machines that can perceive — and perception is the foundation
of understanding. Understanding the world. Understanding people.
Understanding what needs to change and what needs to be protected."[/bold cyan]

She looks at the live feeds from around the world — each one showing
AI making something better.

[bold cyan]"You've walked through every modality. Vision. Sound.
Language. Video. 3D. And you've seen what happens when they merge
and meet reality. The Perception Lab isn't just a module."[/bold cyan]

She smiles.

[bold cyan]"It's how AI learns to be part of the world."[/bold cyan]

[bold white]Perceiver. Builder. Guardian.[/bold white]
[bold white]The Perception Lab is part of you now.[/bold white]
""",
}

BOSS_INTROS = {
    "vision_ai": "ARIA projects a blueprint of a retail store wired with cameras. [bold yellow]\"Three problems: count customers, read price tags, detect empty shelves. Three different vision tasks. One integrated system. Show me how the pieces fit together — models, pipeline, deployment.\"[/bold yellow]",
    "audio_ai": "ARIA shows a podcast episode entering one end of a pipeline. [bold yellow]\"Transcribe it with speaker labels. Summarize the highlights. Create social media clips with AI narration. Translate it into three languages with natural voices. Design the complete system — every model, every step.\"[/bold yellow]",
    "multimodal_models": "ARIA projects a student's workspace: textbook on one side, AI tutor on the other. [bold yellow]\"A multimodal science tutor. Photo input, voice input, diagram output, video walkthroughs. Design it end-to-end — and remember, this is for students. Safety and accuracy come first. Always.\"[/bold yellow]",
    "video_and_3d": "ARIA projects a ghostly outline of ancient Rome over the modern city. [bold yellow]\"Ruins, paintings, and written descriptions. Reconstruct a walkable 3D ancient Rome using AI. Tell me which technologies build the world, which populate it, and — critically — how you mark the line between evidence and AI speculation.\"[/bold yellow]",
    "real_world_applications": "ARIA holds up a pair of prototype smart glasses. [bold yellow]\"Design an AI wearable for visual impairment. Scene description. Text reading. Face recognition. Navigation. Offline mode. Tell me the models, the hardware constraints, the privacy guardrails, and — most importantly — how you make it genuinely useful, not just technically impressive.\"[/bold yellow]",
}
