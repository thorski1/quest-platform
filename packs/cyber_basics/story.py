"""
story.py — Narrative for Cyber Fundamentals (cyber_basics skill pack).
Theme: Cyberpunk noir — CIPHER guides a recruit through the neon-lit grid.
"""

INTRO_STORY = """
[bold cyan]CIPHER TERMINAL — CYBER FUNDAMENTALS DIVISION[/bold cyan]

The grid is burning. Three megacorps went dark last night — ransomware hit
their core systems simultaneously. Payment networks frozen. Hospital records
encrypted. Traffic control systems looping. The news feeds call it an outage.
You know better.

Somewhere in the neon sprawl of Sector 7, a terminal flickers to life.
CIPHER's voice cuts through the static:

[bold cyan]"You want to run the grid? First you need to understand it.
Every system, every network, every login prompt — they all rest on the same
foundations. Break the foundation, break everything above it."[/bold cyan]

A holographic display projects five locked nodes — each pulsing with encrypted
data streams.

[bold white]"Where do I start?"[/bold white]

[bold cyan]"With the three pillars. Confidentiality. Integrity. Availability.
The CIA triad isn't just theory — it's the lens every hacker and every
defender sees the world through. Then we map the threats, decode the social
engineers, forge unbreakable keys, and learn to read the grid itself."[/bold cyan]

A pause. Neon reflections dance across the terminal.

[bold cyan]"The corps that fell last night? They skipped the fundamentals.
Don't make their mistake."[/bold cyan]

[italic]Initializing neural uplink... 5 nodes to decrypt.[/italic]
"""

ZONE_INTROS = {
    "cia_triad": (
        "[bold cyan]NODE 1 — THE THREE PILLARS[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Every security decision maps back to three properties: "
        "Confidentiality — keeping secrets secret. Integrity — ensuring data hasn't "
        "been tampered with. Availability — making sure systems are there when you "
        "need them. Lose one, and the whole grid destabilizes. Master all three, "
        "and you can read the architecture of any defense.'[/bold white]"
    ),
    "common_threats": (
        "[bold cyan]NODE 2 — THE THREAT LANDSCAPE[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Malware, ransomware, phishing, zero-days, DDoS, "
        "man-in-the-middle — the threat landscape is a warzone. Every attack has "
        "a signature, a vector, and a motive. You can't defend against what you "
        "can't name. Map the threats before they map you.'[/bold white]"
    ),
    "social_engineering": (
        "[bold cyan]NODE 3 — THE HUMAN EXPLOIT[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The strongest encryption in the world won't save you "
        "if someone talks their way past the front desk. Pretexting, baiting, "
        "tailgating, spear-phishing — social engineers hack minds, not machines. "
        "The human element is always the softest target.'[/bold white]"
    ),
    "password_security": (
        "[bold cyan]NODE 4 — THE KEY FORGE[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Password123. Admin. Qwerty. The top three passwords "
        "cracked in every breach dump. Hashing, salting, key stretching, MFA, "
        "passphrase entropy — forging a strong key is a science. A weak key is "
        "an open door with a welcome mat.'[/bold white]"
    ),
    "network_basics": (
        "[bold cyan]NODE 5 — THE GRID[/bold cyan]\n\n"
        "[bold white]CIPHER: 'Every byte of data you send crosses the grid — TCP/IP "
        "stacks, DNS lookups, routing tables, firewalls, switches. If you can't "
        "read the grid, you can't defend it. And you definitely can't hack it. "
        "Time to learn the language of packets.'[/bold white]"
    ),
}

ZONE_COMPLETIONS = {
    "cia_triad": (
        "[bold green]NODE DECRYPTED — THE THREE PILLARS[/bold green]\n\n"
        "Confidentiality, Integrity, Availability — the triad is burned into your "
        "neural map. Every firewall, every hash, every backup maps back to these three. "
        "CIPHER: 'The pillars hold. Now you see the grid like an architect.'"
    ),
    "common_threats": (
        "[bold green]NODE DECRYPTED — THE THREAT LANDSCAPE[/bold green]\n\n"
        "Malware, ransomware, phishing, zero-days, DDoS — the threat map is drawn. "
        "You know the signatures, the vectors, the kill chains. "
        "CIPHER: 'You can name every shadow in the dark. That's the first step to hunting them.'"
    ),
    "social_engineering": (
        "[bold green]NODE DECRYPTED — THE HUMAN EXPLOIT[/bold green]\n\n"
        "Pretexting, baiting, tailgating, phishing — the mind hacks are cataloged. "
        "You see the manipulation before it lands. "
        "CIPHER: 'The human firewall is the hardest to build and the easiest to bypass. "
        "Now yours is reinforced.'"
    ),
    "password_security": (
        "[bold green]NODE DECRYPTED — THE KEY FORGE[/bold green]\n\n"
        "Hashing, salting, MFA, entropy — every key you forge now is unbreakable. "
        "No more plaintext. No more reused credentials. "
        "CIPHER: 'The key forge is lit. Every door you lock stays locked.'"
    ),
    "network_basics": (
        "[bold green]NODE DECRYPTED — THE GRID[/bold green]\n\n"
        "TCP/IP, DNS, firewalls, ports, packets — you read the grid like native code. "
        "CIPHER: 'You speak the grid's language now. Every packet tells a story. "
        "Every port is a door. And you know which ones should be open.'"
    ),
}

BOSS_INTROS = {
    "cia_triad": (
        "[bold red]BOSS CHALLENGE — TRIAD BREACH ANALYSIS[/bold red]\n\n"
        "[bold white]CIPHER: 'A hospital's patient records were encrypted by ransomware. "
        "The backup server was on the same network and got hit too. Staff can't access "
        "records, surgeries are delayed. Map every CIA triad violation in this scenario "
        "and name the control that would have prevented each.'[/bold white]"
    ),
    "common_threats": (
        "[bold red]BOSS CHALLENGE — THREAT CLASSIFICATION[/bold red]\n\n"
        "[bold white]CIPHER: 'An employee clicks a link in an email. Their machine starts "
        "encrypting files. Lateral movement detected across the network. C2 traffic "
        "outbound to an unknown IP. Classify every stage of this attack using the "
        "cyber kill chain.'[/bold white]"
    ),
    "social_engineering": (
        "[bold red]BOSS CHALLENGE — THE CON ARTIST[/bold red]\n\n"
        "[bold white]CIPHER: 'Someone called the helpdesk claiming to be the CFO, "
        "said they were locked out during travel, and needed an immediate password "
        "reset on the finance system. The helpdesk complied. Identify every social "
        "engineering technique used and the verification steps that should have "
        "stopped it.'[/bold white]"
    ),
    "password_security": (
        "[bold red]BOSS CHALLENGE — CREDENTIAL BREACH AUDIT[/bold red]\n\n"
        "[bold white]CIPHER: 'A breach dump surfaces with 10 million hashed passwords. "
        "The hashes are unsalted MD5. An attacker with a rainbow table can crack 80% "
        "in hours. Explain why MD5 failed, what the correct hashing approach is, and "
        "design a credential policy that survives the next breach.'[/bold white]"
    ),
    "network_basics": (
        "[bold red]BOSS CHALLENGE — PACKET FORENSICS[/bold red]\n\n"
        "[bold white]CIPHER: 'A packet capture shows DNS queries to a domain registered "
        "yesterday, followed by large encrypted payloads to a non-standard port. "
        "Outbound only. No matching inbound requests. Analyze this traffic — what is "
        "happening, and what network controls would detect or prevent it?'[/bold white]"
    ),
}
