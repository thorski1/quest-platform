"""
story.py — Narrative for The Art Studio skill pack.
"""

INTRO_STORY = """
[bold cyan]Puck fluttered to a doorway covered in colorful handprints.[/bold cyan]

[bold yellow]"Welcome,"[/bold yellow] Puck said, [bold yellow]"to the Art Studio."[/bold yellow]

Inside, every surface was covered with paintings, drawings, sculptures, and collages.
Colors everywhere. Brushes soaking in jars. Clay drying on wooden boards.

[bold yellow]"Art is the oldest language in the world,"[/bold yellow] Puck said quietly.
[bold yellow]"Before people had writing — before there were letters or numbers —
they drew pictures on cave walls to share what they'd seen, what they loved,
what they feared."[/bold yellow]

On one wall hung a copy of the Mona Lisa. On another, The Starry Night.
In the corner, a small clay figure looked like it was dancing.

[bold white]"Am I going to learn to paint like that?"[/bold white]

[bold yellow]"You're going to learn to SEE like that,"[/bold yellow] Puck said.
[bold yellow]"That's how all of it starts."[/bold yellow]

A blank canvas waited on an easel in the center of the room.

[bold white]The Studio is open. Let's explore![/bold white]
"""

ZONE_INTROS = {
    "colors_and_mixing": (
        "[bold cyan]THE COLOR GARDEN[/bold cyan]\n\n"
        "[bold yellow]'Every color in the world started as three,' Puck says, "
        "floating between jars of red, yellow, and blue paint. "
        "'Mix them. Blend them. Change them. "
        "From just three colors, the whole world is possible!'[/bold yellow]"
    ),
    "shapes_and_patterns": (
        "[bold cyan]THE PATTERN ROOM[/bold cyan]\n\n"
        "[bold yellow]'Look around you,' Puck says. 'Shapes everywhere. "
        "In tiles. In leaves. In windows. In fabric. "
        "Artists see the world as shapes — and patterns are shapes that dance together.'[/bold yellow]"
    ),
    "art_tools": (
        "[bold cyan]THE SUPPLY CLOSET[/bold cyan]\n\n"
        "[bold yellow]'A great artist knows their tools,' Puck says, opening a closet "
        "full of brushes, pencils, watercolors, and clay. "
        "'Let's find out what each one does — and what each one is best for.'[/bold yellow]"
    ),
    "famous_artwork": (
        "[bold cyan]THE GREAT GALLERY[/bold cyan]\n\n"
        "[bold yellow]'Come look,' Puck says. The walls of this room hold the most "
        "famous images in human history. "
        "'These pictures changed the world — or at least how people see it. "
        "Let's learn their names, their stories, and why they still matter.'[/bold yellow]"
    ),
    "art_elements": (
        "[bold cyan]THE ELEMENTS ROOM[/bold cyan]\n\n"
        "[bold yellow]'Every painting — every drawing — is built from the same things,' "
        "Puck says. 'Line. Shape. Color. Texture. Space. "
        "Once you can NAME them, you can use them on purpose. "
        "That is what separates art from accident.'[/bold yellow]"
    ),
    "famous_artists": (
        "[bold cyan]THE ARTISTS' HALL[/bold cyan]\n\n"
        "[bold yellow]'These are the people who changed what art could be,' Puck says. "
        "'A genius in Italy. A woman in Mexico. A boy from Brooklyn. "
        "They didn't just make pictures — they changed how the world saw itself.'[/bold yellow]"
    ),
    "art_styles_through_history": (
        "[bold cyan]THE TIME GALLERY[/bold cyan]\n\n"
        "[bold yellow]'Art has been changing for 40,000 years,' Puck says, "
        "floating past paintings that seem to stretch back through time. "
        "'Cave walls. Cathedral ceilings. Soup cans. Melting clocks. "
        "Each era invented something new — and left it for us to find.'[/bold yellow]"
    ),
    "music_and_rhythm": (
        "[bold cyan]THE MUSIC ROOM[/bold cyan]\n\n"
        "[bold yellow]'Close your eyes,' Puck says. A faint melody drifts through the air. "
        "'Art isn't just what you SEE. It's what you hear. "
        "Music is color for your ears — rhythm, melody, harmony, all painting "
        "pictures you can only feel.'[/bold yellow]"
    ),
    "photography_and_film": (
        "[bold cyan]THE DARKROOM[/bold cyan]\n\n"
        "[bold yellow]'Imagine,' Puck says, 'being the first person to capture "
        "a real moment in time — to freeze it forever on paper. "
        "Photography changed everything: how we see ourselves, "
        "how we remember history, how we tell stories.'[/bold yellow]"
    ),
    "dance_and_theater": (
        "[bold cyan]THE STAGE[/bold cyan]\n\n"
        "[bold yellow]The curtain rises. Puck sits on the edge of the stage, "
        "feet dangling over the footlights. "
        "'Art doesn't just live in galleries or concert halls,' Puck says. "
        "'Sometimes it lives in the body — in movement, in gesture, in a voice "
        "filling a silent theater. Dance and theater are as old as fire.'[/bold yellow]"
    ),
    "architecture_and_design": (
        "[bold cyan]THE BLUEPRINT ROOM[/bold cyan]\n\n"
        "[bold yellow]The walls of the Art Studio shift and expand into something like a drafting room — "
        "blueprints pinned everywhere, tiny models of bridges, towers, domes, and arches. "
        "Puck floats among them, tracing a finger along a drawing of the Eiffel Tower. "
        "'Every great building began as a dream,' Puck says quietly. "
        "'And then someone had to do the math.'[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "colors_and_mixing": (
        "[bold green]ZONE COMPLETE — THE COLOR GARDEN![/bold green]\n\n"
        "Primary colors, secondary colors, warm and cool — you understand how color works. "
        "[bold yellow]'Every sunset, every painting, every rainbow — "
        "now you know the rules behind all of it!'[/bold yellow]"
    ),
    "shapes_and_patterns": (
        "[bold green]ZONE COMPLETE — THE PATTERN ROOM![/bold green]\n\n"
        "Shapes, symmetry, tessellations — you see the geometry in art now. "
        "[bold yellow]'Look at a tiled floor or a quilt and you'll never see it the same way again!'[/bold yellow]"
    ),
    "art_tools": (
        "[bold green]ZONE COMPLETE — THE SUPPLY CLOSET![/bold green]\n\n"
        "Pencils, watercolors, canvas, collage, perspective — the tools are no longer mysterious. "
        "[bold yellow]'Now you know what artists mean when they talk about their materials!'[/bold yellow]"
    ),
    "famous_artwork": (
        "[bold green]ZONE COMPLETE — THE GREAT GALLERY![/bold green]\n\n"
        "Mona Lisa, Starry Night, David, Water Lilies, Guernica — you know them now. "
        "[bold yellow]'These aren't just pictures. They're conversations across centuries.'[/bold yellow]"
    ),
    "art_elements": (
        "[bold green]ZONE COMPLETE — THE ELEMENTS ROOM![/bold green]\n\n"
        "Line, texture, foreground, contrast, negative space, proportion — "
        "the vocabulary of visual art is yours. "
        "[bold yellow]'Now you can TALK about what you see. That changes everything.'[/bold yellow]"
    ),
    "famous_artists": (
        "[bold green]ZONE COMPLETE — THE ARTISTS' HALL![/bold green]\n\n"
        "Da Vinci, Kahlo, Monet, O'Keeffe, Picasso, Basquiat — and now you. "
        "[bold yellow]'Everyone who ever made art started somewhere. "
        "Maybe this is where your story starts.'[/bold yellow]"
    ),
    "art_styles_through_history": (
        "[bold green]ZONE COMPLETE — THE TIME GALLERY![/bold green]\n\n"
        "Cave art, Renaissance, Baroque, Abstract, Pop Art, Surrealism — "
        "40,000 years of human creativity, explored! "
        "[bold yellow]'You can walk into any museum now and know when and why things were made.'[/bold yellow]"
    ),
    "music_and_rhythm": (
        "[bold green]ZONE COMPLETE — THE MUSIC ROOM![/bold green]\n\n"
        "Notes, beats, instruments, Mozart, Beethoven, jazz — your ears are open! "
        "[bold yellow]'Music is the art that lives in time itself. "
        "Now every song you hear has a little more meaning.'[/bold yellow]"
    ),
    "photography_and_film": (
        "[bold green]ZONE COMPLETE — THE DARKROOM![/bold green]\n\n"
        "Pixels, frames, composition, history's first photographs — you understand how images work! "
        "[bold yellow]'Every photo you take from now on — think about the rule of thirds. "
        "Think about the light. Think about the story you are telling.'[/bold yellow]"
    ),
    "dance_and_theater": (
        "[bold green]ZONE COMPLETE — THE STAGE![/bold green]\n\n"
        "Ballet, hip-hop, Greek masks, musicals, Indian classical dance — "
        "the performing arts are yours to explore! "
        "[bold yellow]'The body is an instrument. The stage is a canvas. "
        "And a story told live, in the same room as the audience, "
        "is magic that no screen can quite copy.'[/bold yellow]"
    ),
    "architecture_and_design": (
        "[bold green]ZONE COMPLETE — THE BLUEPRINT ROOM![/bold green]\n\n"
        "Pyramids, the Eiffel Tower, suspension bridges, the Sagrada Família — "
        "you understand how great buildings come to be! "
        "[bold yellow]'Every building you walk into from now on, "
        "look at the shapes that hold it up. "
        "Someone dreamed them, drew them, and built them. "
        "And now you know how.'[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "colors_and_mixing": (
        "[bold red]BOSS CHALLENGE — THE FULL COLOR WHEEL[/bold red]\n\n"
        "[bold yellow]'Name every primary color, every secondary color, "
        "and tell me which colors are warm and which are cool. "
        "The whole palette — no hints!'[/bold yellow]"
    ),
    "shapes_and_patterns": (
        "[bold red]BOSS CHALLENGE — THE MASTER PATTERN[/bold red]\n\n"
        "[bold yellow]'Symmetry, tessellation, organic vs geometric shapes — "
        "I'm going to test all of it. "
        "Show me you really understand how shapes work in art.'[/bold yellow]"
    ),
    "art_tools": (
        "[bold red]BOSS CHALLENGE — THE ARTIST'S CHOICE[/bold red]\n\n"
        "[bold yellow]'For each project, what tool is best? "
        "A portrait? A mosaic? A protest image? "
        "Explain your choices like a real artist would.'[/bold yellow]"
    ),
    "famous_artwork": (
        "[bold red]BOSS CHALLENGE — THE GALLERY GUIDE[/bold red]\n\n"
        "[bold yellow]'Pretend you are a museum guide. "
        "Tell me about every famous work we studied — "
        "who made it, when, and why it matters.'[/bold yellow]"
    ),
    "art_elements": (
        "[bold red]BOSS CHALLENGE — THE CRITICAL EYE[/bold red]\n\n"
        "[bold yellow]'Look at this painting in your mind: a stormy sky, "
        "a figure in the foreground, swirling lines, bold contrast. "
        "Name every element of art at work in it.'[/bold yellow]"
    ),
    "famous_artists": (
        "[bold red]BOSS CHALLENGE — THE ARTIST MATCH[/bold red]\n\n"
        "[bold yellow]'I will describe a style — you match it to an artist. "
        "Da Vinci to Basquiat. Every artist we met, every style we studied. "
        "Let's see if they stayed with you.'[/bold yellow]"
    ),
    "art_styles_through_history": (
        "[bold red]BOSS CHALLENGE — ART THROUGH TIME[/bold red]\n\n"
        "[bold yellow]'Cave art. Renaissance. Impressionism. Cubism. Pop Art. Surrealism. "
        "I'll name a style — you tell me when it happened and what made it special. "
        "40,000 years of creativity, all in your head now!'[/bold yellow]"
    ),
    "music_and_rhythm": (
        "[bold red]BOSS CHALLENGE — THE CONCERT HALL[/bold red]\n\n"
        "[bold yellow]'Notes, tempos, instrument families, and the greatest composers in history. "
        "I'll play music detective — can you name the clues? "
        "Show me you truly listened.'[/bold yellow]"
    ),
    "photography_and_film": (
        "[bold red]BOSS CHALLENGE — BEHIND THE LENS[/bold red]\n\n"
        "[bold yellow]'Exposure, pixels, frames per second, composition rules, the history of cameras. "
        "From the first cave painting to the latest digital photo — "
        "what does it mean to truly SEE and capture a moment?'[/bold yellow]"
    ),
    "dance_and_theater": (
        "[bold red]BOSS CHALLENGE — THE FINAL CURTAIN[/bold red]\n\n"
        "[bold yellow]'Ballet or hip-hop? Tragedy or comedy? Mudra or musical? "
        "Tell me the story of performing arts — from ancient Greek masks "
        "to a Broadway stage to a street corner in New York. "
        "The audience is waiting.'[/bold yellow]"
    ),
    "architecture_and_design": (
        "[bold red]BOSS CHALLENGE — THE GRAND DESIGN[/bold red]\n\n"
        "[bold yellow]'You are the architect. You have one challenge: "
        "explain why the triangle is stronger than a rectangle, "
        "name two buildings that prove great design follows function, "
        "and tell me what the Sagrada Família, the Pyramids, "
        "and the Golden Gate Bridge have in common. "
        "Build your answer as if it will stand for a thousand years.'[/bold yellow]"
    ),
}
