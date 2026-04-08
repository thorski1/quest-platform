"""
zones.py - All zone and challenge data for HTML & CSS Foundations
5 zones x 8 challenges = 40 challenges total
"""

ZONE_ORDER = [
    "html_elements",
    "forms_inputs",
    "css_selectors",
    "flexbox_grid",
    "responsive_design",
]

ZONES = {
    # ── Zone 1: HTML Elements ────────────────────────────────────
    "html_elements": {
        "id": "html_elements",
        "name": "The Document Core",
        "subtitle": "HTML Elements & Semantics",
        "color": "cyan",
        "icon": "</>",
        "challenges": [
            {
                "id": "html_1",
                "type": "quiz",
                "question": "Which HTML element represents the main heading of a page?",
                "options": ["<h1>", "<header>", "<title>", "<head>"],
                "answer": "a",
                "lesson": (
                    "<h1> is the top-level heading element.\n\n"
                    "HTML has six heading levels: <h1> through <h6>.\n"
                    "<h1> is the most important (main heading).\n"
                    "<h6> is the least important (sub-sub-sub heading).\n\n"
                    "Note: <header> is a container for introductory content.\n"
                    "<title> sets the browser tab text.\n"
                    "<head> contains metadata, not visible content."
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["It's a heading tag with a number.", "The number indicates priority — 1 is highest."],
            },
            {
                "id": "html_2",
                "type": "quiz",
                "question": "Which element creates a hyperlink to another page?",
                "options": ["<link>", "<a>", "<href>", "<nav>"],
                "answer": "b",
                "lesson": (
                    "<a> (anchor) creates hyperlinks.\n\n"
                    "Syntax: <a href=\"https://example.com\">Link text</a>\n\n"
                    "Key attributes:\n"
                    "  href    — the URL to link to\n"
                    "  target  — where to open (_blank for new tab)\n"
                    "  rel     — relationship (noopener, noreferrer)\n\n"
                    "Note: <link> is for linking stylesheets/resources in <head>."
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["It stands for 'anchor'.", "Single letter tag."],
            },
            {
                "id": "html_3",
                "type": "quiz",
                "question": "What is the correct HTML element for an unordered (bulleted) list?",
                "options": ["<ol>", "<list>", "<ul>", "<li>"],
                "answer": "c",
                "lesson": (
                    "<ul> creates an unordered (bulleted) list.\n\n"
                    "List elements:\n"
                    "  <ul>  — unordered list (bullets)\n"
                    "  <ol>  — ordered list (numbers)\n"
                    "  <li>  — list item (goes inside <ul> or <ol>)\n\n"
                    "Example:\n"
                    "  <ul>\n"
                    "    <li>Item one</li>\n"
                    "    <li>Item two</li>\n"
                    "  </ul>"
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["'u' stands for 'unordered'.", "Two-letter tag."],
            },
            {
                "id": "html_4",
                "type": "quiz",
                "question": "Which semantic element should wrap the main content of a page?",
                "options": ["<div>", "<section>", "<main>", "<body>"],
                "answer": "c",
                "lesson": (
                    "<main> identifies the dominant content of the <body>.\n\n"
                    "Semantic landmarks:\n"
                    "  <main>     — primary page content (one per page)\n"
                    "  <header>   — introductory content or navigation\n"
                    "  <footer>   — footer content\n"
                    "  <nav>      — navigation links\n"
                    "  <section>  — thematic grouping of content\n"
                    "  <article>  — self-contained composition\n\n"
                    "Screen readers use these landmarks for navigation."
                ),
                "xp": 75,
                "difficulty": "medium",
                "hints": ["It's a semantic HTML5 element.", "Its name literally describes what it contains."],
            },
            {
                "id": "html_5",
                "type": "quiz",
                "question": "Which attribute is REQUIRED on an <img> element for accessibility?",
                "options": ["src", "alt", "title", "width"],
                "answer": "b",
                "lesson": (
                    "The alt attribute provides alternative text for images.\n\n"
                    "Syntax: <img src=\"photo.jpg\" alt=\"Description of image\">\n\n"
                    "Why alt matters:\n"
                    "  - Screen readers read it aloud for blind users\n"
                    "  - Displays when the image fails to load\n"
                    "  - Search engines use it to understand images\n\n"
                    "For decorative images, use alt=\"\" (empty but present).\n"
                    "Never omit alt entirely — it's an accessibility violation."
                ),
                "xp": 75,
                "difficulty": "medium",
                "hints": ["It's about accessibility.", "It provides text when the image can't be seen."],
            },
            {
                "id": "html_6",
                "type": "quiz",
                "question": "What is the difference between <div> and <span>?",
                "options": [
                    "<div> is block-level; <span> is inline",
                    "<div> is inline; <span> is block-level",
                    "<div> is semantic; <span> is not",
                    "There is no difference",
                ],
                "answer": "a",
                "lesson": (
                    "<div> is a block-level container. <span> is an inline container.\n\n"
                    "Block elements:\n"
                    "  - Start on a new line\n"
                    "  - Take full available width\n"
                    "  - Examples: <div>, <p>, <h1>, <section>\n\n"
                    "Inline elements:\n"
                    "  - Flow within text, no line break\n"
                    "  - Only take needed width\n"
                    "  - Examples: <span>, <a>, <strong>, <em>\n\n"
                    "Neither <div> nor <span> is semantic — use them when\n"
                    "no semantic element fits."
                ),
                "xp": 75,
                "difficulty": "medium",
                "hints": ["Think about how they affect the flow of content.", "One starts a new line; one doesn't."],
            },
            {
                "id": "html_7",
                "type": "quiz",
                "question": "Which element should you use for a self-contained piece of content like a blog post?",
                "options": ["<section>", "<div>", "<article>", "<aside>"],
                "answer": "c",
                "lesson": (
                    "<article> represents a self-contained composition.\n\n"
                    "Use <article> when the content makes sense on its own:\n"
                    "  - Blog posts\n"
                    "  - News articles\n"
                    "  - Forum posts\n"
                    "  - Product cards\n\n"
                    "<section> is for thematic grouping within a page.\n"
                    "<aside> is for tangentially related content (sidebars).\n"
                    "<div> has no semantic meaning at all."
                ),
                "xp": 100,
                "difficulty": "hard",
                "hints": ["Think about syndication — could this content stand alone?", "Its name matches what a blog post is."],
            },
            {
                "id": "html_8",
                "type": "quiz",
                "question": "What does the 'doctype' declaration (<!DOCTYPE html>) tell the browser?",
                "options": [
                    "Which version of HTML to use",
                    "To render in standards mode, not quirks mode",
                    "The character encoding of the page",
                    "Where to find the stylesheet",
                ],
                "answer": "b",
                "lesson": (
                    "<!DOCTYPE html> triggers standards mode rendering.\n\n"
                    "Without it, browsers fall back to 'quirks mode' —\n"
                    "emulating bugs from the 1990s for backward compatibility.\n\n"
                    "The modern doctype is simple: <!DOCTYPE html>\n"
                    "Older doctypes referenced DTD URLs and were much longer.\n\n"
                    "Always place <!DOCTYPE html> as the very first line.\n"
                    "It's not an HTML element — it's a processing instruction."
                ),
                "xp": 100,
                "difficulty": "hard",
                "hints": ["It's about rendering mode.", "Without it, browsers behave unpredictably."],
            },
        ],
    },
    # ── Zone 2: Forms & Inputs ───────────────────────────────────
    "forms_inputs": {
        "id": "forms_inputs",
        "name": "The Input Gateway",
        "subtitle": "Forms, Inputs & Validation",
        "color": "green",
        "icon": ">>",
        "challenges": [
            {
                "id": "form_1",
                "type": "quiz",
                "question": "Which attribute specifies where form data is sent when submitted?",
                "options": ["method", "action", "target", "enctype"],
                "answer": "b",
                "lesson": (
                    "The action attribute specifies the URL that processes the form.\n\n"
                    "Syntax: <form action=\"/submit\" method=\"POST\">\n\n"
                    "Key form attributes:\n"
                    "  action   — URL to send data to\n"
                    "  method   — HTTP method (GET or POST)\n"
                    "  enctype  — encoding type for file uploads\n"
                    "  target   — where to display the response\n\n"
                    "If action is omitted, the form submits to the current page URL."
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["It's the destination URL.", "Think 'where does the action happen?'"],
            },
            {
                "id": "form_2",
                "type": "quiz",
                "question": "What input type creates a password field that hides typed characters?",
                "options": ["text", "hidden", "password", "secret"],
                "answer": "c",
                "lesson": (
                    "type=\"password\" masks input characters with dots or asterisks.\n\n"
                    "Syntax: <input type=\"password\" name=\"pwd\">\n\n"
                    "Common input types:\n"
                    "  text      — single-line text\n"
                    "  password  — masked text\n"
                    "  email     — email with validation\n"
                    "  number    — numeric input with spinners\n"
                    "  tel       — telephone number\n"
                    "  url       — URL with validation\n\n"
                    "Note: type=\"hidden\" makes the field invisible entirely,\n"
                    "not just masked."
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["The type name matches what the field contains.", "It's literally called what it protects."],
            },
            {
                "id": "form_3",
                "type": "quiz",
                "question": "Which HTML attribute makes a form field mandatory before submission?",
                "options": ["mandatory", "required", "validate", "notempty"],
                "answer": "b",
                "lesson": (
                    "The required attribute prevents form submission if the field is empty.\n\n"
                    "Syntax: <input type=\"email\" required>\n\n"
                    "Built-in validation attributes:\n"
                    "  required    — field must not be empty\n"
                    "  minlength   — minimum character count\n"
                    "  maxlength   — maximum character count\n"
                    "  min / max   — numeric range limits\n"
                    "  pattern     — regex pattern to match\n\n"
                    "The browser validates these natively — no JavaScript needed."
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["It's a boolean attribute.", "The name says exactly what it does."],
            },
            {
                "id": "form_4",
                "type": "quiz",
                "question": "What is the purpose of the <label> element in a form?",
                "options": [
                    "It styles the input field",
                    "It associates text with a form control for accessibility",
                    "It validates the input",
                    "It groups related inputs",
                ],
                "answer": "b",
                "lesson": (
                    "<label> associates descriptive text with a form control.\n\n"
                    "Two ways to associate:\n"
                    "  1. Wrapping:  <label>Name <input type=\"text\"></label>\n"
                    "  2. for/id:   <label for=\"name\">Name</label>\n"
                    "               <input id=\"name\" type=\"text\">\n\n"
                    "Why labels matter:\n"
                    "  - Screen readers announce the label when the input is focused\n"
                    "  - Clicking the label focuses/toggles the input\n"
                    "  - Larger click target on mobile devices\n\n"
                    "Every input needs a label. No exceptions."
                ),
                "xp": 75,
                "difficulty": "medium",
                "hints": ["Think about accessibility.", "It tells users (and screen readers) what an input is for."],
            },
            {
                "id": "form_5",
                "type": "quiz",
                "question": "Which input type provides a native date picker in modern browsers?",
                "options": ["text", "date", "calendar", "datetime"],
                "answer": "b",
                "lesson": (
                    "type=\"date\" renders a native date picker widget.\n\n"
                    "Date/time input types:\n"
                    "  date            — date picker (YYYY-MM-DD)\n"
                    "  time            — time picker (HH:MM)\n"
                    "  datetime-local  — date + time picker\n"
                    "  month           — month/year picker\n"
                    "  week            — week/year picker\n\n"
                    "These provide native UI without JavaScript libraries.\n"
                    "The value format is always ISO standard regardless of\n"
                    "the displayed locale format."
                ),
                "xp": 75,
                "difficulty": "medium",
                "hints": ["The type name is straightforward.", "Modern HTML has native date controls."],
            },
            {
                "id": "form_6",
                "type": "quiz",
                "question": "What does the 'pattern' attribute do on an <input> element?",
                "options": [
                    "Sets a visual pattern/texture on the input",
                    "Validates input against a regular expression",
                    "Auto-formats the input text",
                    "Restricts which keys can be pressed",
                ],
                "answer": "b",
                "lesson": (
                    "The pattern attribute validates input against a regex.\n\n"
                    "Syntax: <input type=\"text\" pattern=\"[A-Za-z]{3}\">\n\n"
                    "Examples:\n"
                    "  pattern=\"[0-9]{5}\"        — 5-digit zip code\n"
                    "  pattern=\"[A-Z]{2}[0-9]{4}\" — 2 letters + 4 digits\n"
                    "  pattern=\".{8,}\"           — at least 8 characters\n\n"
                    "Use the title attribute to explain the expected format:\n"
                    "  <input pattern=\"[0-9]{5}\" title=\"Five digit zip code\">\n\n"
                    "The browser shows the title text in the validation tooltip."
                ),
                "xp": 100,
                "difficulty": "hard",
                "hints": ["Think about regex.", "It's client-side validation without JavaScript."],
            },
            {
                "id": "form_7",
                "type": "quiz",
                "question": "Which element lets users select from a predefined list while still allowing free text input?",
                "options": ["<select>", "<datalist>", "<optgroup>", "<fieldset>"],
                "answer": "b",
                "lesson": (
                    "<datalist> provides autocomplete suggestions for an input.\n\n"
                    "Syntax:\n"
                    "  <input list=\"browsers\">\n"
                    "  <datalist id=\"browsers\">\n"
                    "    <option value=\"Chrome\">\n"
                    "    <option value=\"Firefox\">\n"
                    "    <option value=\"Safari\">\n"
                    "  </datalist>\n\n"
                    "Unlike <select>, the user can type anything — the\n"
                    "datalist only suggests, it doesn't restrict.\n\n"
                    "<select> forces a choice from fixed options.\n"
                    "<datalist> offers suggestions with free text fallback."
                ),
                "xp": 100,
                "difficulty": "hard",
                "hints": ["It combines dropdown suggestions with free text.", "It's linked to an input via the 'list' attribute."],
            },
            {
                "id": "form_8",
                "type": "quiz",
                "question": "What enctype must be set on a form to upload files?",
                "options": [
                    "application/json",
                    "multipart/form-data",
                    "text/plain",
                    "application/x-www-form-urlencoded",
                ],
                "answer": "b",
                "lesson": (
                    "multipart/form-data is required for file uploads.\n\n"
                    "Form encoding types:\n"
                    "  application/x-www-form-urlencoded  — default, key=value pairs\n"
                    "  multipart/form-data                — for file uploads\n"
                    "  text/plain                         — unencoded (rarely used)\n\n"
                    "Syntax:\n"
                    "  <form enctype=\"multipart/form-data\" method=\"POST\">\n"
                    "    <input type=\"file\" name=\"upload\">\n"
                    "    <button type=\"submit\">Upload</button>\n"
                    "  </form>\n\n"
                    "Without multipart/form-data, the file content won't be sent."
                ),
                "xp": 100,
                "difficulty": "hard",
                "hints": ["Think about how binary data gets encoded.", "The name suggests multiple parts of data."],
            },
        ],
    },
    # ── Zone 3: CSS Selectors ────────────────────────────────────
    "css_selectors": {
        "id": "css_selectors",
        "name": "The Selector Matrix",
        "subtitle": "CSS Selectors & Specificity",
        "color": "magenta",
        "icon": "{}",
        "challenges": [
            {
                "id": "css_1",
                "type": "quiz",
                "question": "Which CSS selector targets all elements with the class 'active'?",
                "options": ["#active", ".active", "active", "*active"],
                "answer": "b",
                "lesson": (
                    "A dot (.) prefix selects elements by class name.\n\n"
                    "Selector types:\n"
                    "  .classname   — class selector\n"
                    "  #idname      — ID selector\n"
                    "  element      — type selector (p, div, h1)\n"
                    "  *            — universal selector (all elements)\n\n"
                    "Example: .active { color: green; }\n"
                    "This styles every element with class=\"active\".\n\n"
                    "Classes can be reused on multiple elements.\n"
                    "IDs must be unique per page."
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["The prefix character is a punctuation mark.", "Think dot-notation."],
            },
            {
                "id": "css_2",
                "type": "quiz",
                "question": "What does the CSS selector 'div > p' target?",
                "options": [
                    "All <p> elements inside a <div>",
                    "Only <p> elements that are direct children of a <div>",
                    "The <div> that comes after a <p>",
                    "All <div> and <p> elements",
                ],
                "answer": "b",
                "lesson": (
                    "The > combinator selects direct children only.\n\n"
                    "Combinators:\n"
                    "  div p    — descendant (any depth)\n"
                    "  div > p  — child (direct only)\n"
                    "  div + p  — adjacent sibling (immediately after)\n"
                    "  div ~ p  — general sibling (any sibling after)\n\n"
                    "Example: ul > li targets only the top-level <li> elements,\n"
                    "not <li> elements nested inside sub-lists."
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["The > symbol implies a parent-child relationship.", "It's more specific than just a space."],
            },
            {
                "id": "css_3",
                "type": "quiz",
                "question": "Which pseudo-class applies styles when a user hovers over an element?",
                "options": [":focus", ":active", ":hover", ":visited"],
                "answer": "c",
                "lesson": (
                    ":hover applies when the cursor is over an element.\n\n"
                    "Common pseudo-classes:\n"
                    "  :hover    — mouse is over the element\n"
                    "  :focus    — element has keyboard focus\n"
                    "  :active   — element is being clicked/pressed\n"
                    "  :visited  — link has been visited\n"
                    "  :first-child  — first child of its parent\n"
                    "  :last-child   — last child of its parent\n"
                    "  :nth-child(n) — nth child of its parent\n\n"
                    "Pseudo-classes start with a single colon.\n"
                    "Pseudo-elements start with double colons (::)."
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["It's named after the mouse action.", "Starts with a colon."],
            },
            {
                "id": "css_4",
                "type": "quiz",
                "question": "In CSS specificity, which has the HIGHEST priority?",
                "options": [
                    "Class selector (.btn)",
                    "ID selector (#submit)",
                    "Element selector (button)",
                    "Universal selector (*)",
                ],
                "answer": "b",
                "lesson": (
                    "Specificity hierarchy (highest to lowest):\n\n"
                    "  1. Inline styles       (style=\"...\")    — 1,0,0,0\n"
                    "  2. ID selectors         (#id)            — 0,1,0,0\n"
                    "  3. Class/pseudo-class   (.class, :hover) — 0,0,1,0\n"
                    "  4. Element/pseudo-elem  (div, ::before)  — 0,0,0,1\n"
                    "  5. Universal selector   (*)              — 0,0,0,0\n\n"
                    "!important overrides all specificity (use sparingly).\n\n"
                    "When specificity is equal, the last rule in source order wins."
                ),
                "xp": 75,
                "difficulty": "medium",
                "hints": ["Think about the specificity hierarchy.", "The hash symbol implies uniqueness."],
            },
            {
                "id": "css_5",
                "type": "quiz",
                "question": "What does the selector 'input[type=\"email\"]' target?",
                "options": [
                    "All <input> elements",
                    "Only <input> elements with type attribute set to 'email'",
                    "All elements with type='email'",
                    "The <email> element inside an <input>",
                ],
                "answer": "b",
                "lesson": (
                    "Attribute selectors target elements by their attributes.\n\n"
                    "Attribute selector syntax:\n"
                    "  [attr]         — has the attribute\n"
                    "  [attr=\"val\"]   — attribute equals value\n"
                    "  [attr^=\"val\"]  — attribute starts with value\n"
                    "  [attr$=\"val\"]  — attribute ends with value\n"
                    "  [attr*=\"val\"]  — attribute contains value\n"
                    "  [attr~=\"val\"]  — attribute contains word\n\n"
                    "Example: a[href$=\".pdf\"] targets all links to PDF files."
                ),
                "xp": 75,
                "difficulty": "medium",
                "hints": ["Square brackets indicate attribute matching.", "It's filtering by a specific attribute value."],
            },
            {
                "id": "css_6",
                "type": "quiz",
                "question": "What is the difference between ::before and :before in CSS?",
                "options": [
                    "::before is the correct modern syntax; :before is legacy",
                    "They target different elements",
                    ":before is for pseudo-classes; ::before is for pseudo-elements",
                    "::before has higher specificity",
                ],
                "answer": "a",
                "lesson": (
                    "Double colon (::) is the correct syntax for pseudo-elements.\n\n"
                    "CSS3 introduced :: to distinguish:\n"
                    "  :  — pseudo-classes (:hover, :focus, :nth-child)\n"
                    "  :: — pseudo-elements (::before, ::after, ::first-line)\n\n"
                    "Browsers still support single-colon :before for backwards\n"
                    "compatibility, but :: is the standard.\n\n"
                    "Common pseudo-elements:\n"
                    "  ::before      — insert content before element\n"
                    "  ::after       — insert content after element\n"
                    "  ::first-line  — style first line of text\n"
                    "  ::placeholder — style input placeholder text"
                ),
                "xp": 100,
                "difficulty": "hard",
                "hints": ["It's about CSS evolution.", "One is the modern standard; the other is legacy."],
            },
            {
                "id": "css_7",
                "type": "quiz",
                "question": "Which selector targets every third <li> element?",
                "options": [
                    "li:nth-child(3)",
                    "li:nth-child(3n)",
                    "li:every(3)",
                    "li:child(3)",
                ],
                "answer": "b",
                "lesson": (
                    ":nth-child(3n) selects every element at position 3, 6, 9...\n\n"
                    "nth-child formulas:\n"
                    "  :nth-child(3)    — only the 3rd child\n"
                    "  :nth-child(3n)   — every 3rd (3, 6, 9...)\n"
                    "  :nth-child(2n)   — every even child\n"
                    "  :nth-child(2n+1) — every odd child\n"
                    "  :nth-child(odd)  — same as 2n+1\n"
                    "  :nth-child(even) — same as 2n\n"
                    "  :nth-child(n+4)  — 4th child and beyond\n\n"
                    "The 'n' variable counts from 0: 0, 1, 2, 3..."
                ),
                "xp": 100,
                "difficulty": "hard",
                "hints": ["You need a formula, not just a number.", "The 'n' makes it repeat."],
            },
            {
                "id": "css_8",
                "type": "quiz",
                "question": "If a <p> has class='note' inside a <div> with id='content', which selector is MOST specific?",
                "options": [
                    "p.note",
                    "#content p",
                    "div p.note",
                    "#content .note",
                ],
                "answer": "d",
                "lesson": (
                    "Specificity is calculated by counting selector components.\n\n"
                    "  p.note         → 0,0,1,1  (1 class + 1 element)\n"
                    "  #content p     → 0,1,0,1  (1 ID + 1 element)\n"
                    "  div p.note     → 0,0,1,2  (1 class + 2 elements)\n"
                    "  #content .note → 0,1,1,0  (1 ID + 1 class)\n\n"
                    "#content .note wins because the ID column (0,1,x,x)\n"
                    "outweighs any number of classes, and it also has a class.\n\n"
                    "ID > class > element. Always compare left to right."
                ),
                "xp": 100,
                "difficulty": "hard",
                "hints": ["Calculate the specificity of each option.", "IDs have more weight than classes."],
            },
        ],
    },
    # ── Zone 4: Flexbox & Grid ───────────────────────────────────
    "flexbox_grid": {
        "id": "flexbox_grid",
        "name": "The Layout Engine",
        "subtitle": "Flexbox & CSS Grid",
        "color": "yellow",
        "icon": "[]",
        "challenges": [
            {
                "id": "flex_1",
                "type": "quiz",
                "question": "What CSS property turns an element into a flex container?",
                "options": ["flex: 1", "display: flex", "flex-direction: row", "position: flex"],
                "answer": "b",
                "lesson": (
                    "display: flex creates a flex container.\n\n"
                    "Once set, all direct children become flex items.\n\n"
                    "Default behavior:\n"
                    "  - Items flow in a row (flex-direction: row)\n"
                    "  - Items don't wrap (flex-wrap: nowrap)\n"
                    "  - Items stretch to fill container height\n\n"
                    "display: inline-flex creates an inline flex container\n"
                    "(doesn't take full width).\n\n"
                    "Flexbox is one-dimensional: row OR column."
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["It's a display property value.", "Two words: display and flex."],
            },
            {
                "id": "flex_2",
                "type": "quiz",
                "question": "Which property centers flex items horizontally in a row layout?",
                "options": ["align-items: center", "justify-content: center", "text-align: center", "margin: auto"],
                "answer": "b",
                "lesson": (
                    "justify-content aligns items along the main axis.\n\n"
                    "In a row layout (default):\n"
                    "  justify-content → horizontal alignment\n"
                    "  align-items     → vertical alignment\n\n"
                    "justify-content values:\n"
                    "  flex-start    — pack to the start\n"
                    "  flex-end      — pack to the end\n"
                    "  center        — center items\n"
                    "  space-between — equal space between items\n"
                    "  space-around  — equal space around items\n"
                    "  space-evenly  — equal space everywhere\n\n"
                    "The 'main axis' flips when flex-direction is column."
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["Justify handles the main axis.", "Main axis in row layout is horizontal."],
            },
            {
                "id": "flex_3",
                "type": "quiz",
                "question": "How do you center an item both horizontally AND vertically with Flexbox?",
                "options": [
                    "justify-content: center; align-items: center",
                    "text-align: center; vertical-align: middle",
                    "margin: 0 auto; padding: 50%",
                    "position: absolute; top: 50%; left: 50%",
                ],
                "answer": "a",
                "lesson": (
                    "Combine justify-content and align-items for full centering.\n\n"
                    "The centering recipe:\n"
                    "  .container {\n"
                    "    display: flex;\n"
                    "    justify-content: center;  /* main axis */\n"
                    "    align-items: center;       /* cross axis */\n"
                    "  }\n\n"
                    "Alternative (single item): place-items: center;\n"
                    "This is shorthand for align-items + justify-items.\n\n"
                    "For Grid: display: grid; place-items: center;\n"
                    "Both achieve the same result."
                ),
                "xp": 75,
                "difficulty": "medium",
                "hints": ["You need two properties — one for each axis.", "justify for main, align for cross."],
            },
            {
                "id": "flex_4",
                "type": "quiz",
                "question": "What CSS property creates a grid container?",
                "options": ["display: grid", "grid-template: auto", "position: grid", "layout: grid"],
                "answer": "a",
                "lesson": (
                    "display: grid creates a CSS Grid container.\n\n"
                    "CSS Grid is two-dimensional: rows AND columns.\n\n"
                    "Basic grid setup:\n"
                    "  .container {\n"
                    "    display: grid;\n"
                    "    grid-template-columns: 1fr 1fr 1fr;\n"
                    "    grid-template-rows: auto;\n"
                    "    gap: 1rem;\n"
                    "  }\n\n"
                    "Key difference from Flexbox:\n"
                    "  Flexbox = one axis (row or column)\n"
                    "  Grid    = two axes (rows and columns)\n\n"
                    "Use Flexbox for components, Grid for page layouts."
                ),
                "xp": 75,
                "difficulty": "medium",
                "hints": ["Same pattern as Flexbox.", "It's a display property value."],
            },
            {
                "id": "flex_5",
                "type": "quiz",
                "question": "What does 'fr' stand for in 'grid-template-columns: 1fr 2fr'?",
                "options": ["frame", "fraction", "free", "format"],
                "answer": "b",
                "lesson": (
                    "fr stands for 'fraction' of available space.\n\n"
                    "In grid-template-columns: 1fr 2fr;\n"
                    "  - Total fractions: 1 + 2 = 3\n"
                    "  - Column 1 gets 1/3 of space\n"
                    "  - Column 2 gets 2/3 of space\n\n"
                    "fr works like flex-grow but for grid tracks.\n\n"
                    "Mixing units:\n"
                    "  grid-template-columns: 200px 1fr;\n"
                    "  → Fixed 200px sidebar, fluid main content\n\n"
                    "  grid-template-columns: repeat(3, 1fr);\n"
                    "  → Three equal columns"
                ),
                "xp": 75,
                "difficulty": "medium",
                "hints": ["It's about dividing space.", "Think fractional units."],
            },
            {
                "id": "flex_6",
                "type": "quiz",
                "question": "Which property adds consistent spacing between grid or flex items?",
                "options": ["margin", "padding", "gap", "spacing"],
                "answer": "c",
                "lesson": (
                    "gap adds space between grid/flex items (not around them).\n\n"
                    "Syntax:\n"
                    "  gap: 1rem;          — equal row and column gaps\n"
                    "  gap: 1rem 2rem;     — row-gap column-gap\n"
                    "  row-gap: 1rem;      — only row gaps\n"
                    "  column-gap: 2rem;   — only column gaps\n\n"
                    "gap works on both Grid and Flexbox containers.\n\n"
                    "Unlike margin, gap only applies between items,\n"
                    "never on the outer edges. This eliminates the\n"
                    "classic 'negative margin hack' for gutters."
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["It's a newer CSS property.", "Three letters, means space between."],
            },
            {
                "id": "flex_7",
                "type": "quiz",
                "question": "How do you make a flex item grow to fill available space?",
                "options": ["width: 100%", "flex-grow: 1", "flex-basis: auto", "align-self: stretch"],
                "answer": "b",
                "lesson": (
                    "flex-grow controls how much a flex item grows.\n\n"
                    "flex-grow values:\n"
                    "  0  — don't grow (default)\n"
                    "  1  — grow equally with other flex-grow: 1 items\n"
                    "  2  — grow twice as much as flex-grow: 1 items\n\n"
                    "The flex shorthand: flex: grow shrink basis\n"
                    "  flex: 1;       → flex: 1 1 0%\n"
                    "  flex: 0 0 auto → don't grow, don't shrink, natural size\n\n"
                    "flex-shrink: controls how much an item shrinks\n"
                    "flex-basis: sets the initial size before growing/shrinking"
                ),
                "xp": 100,
                "difficulty": "hard",
                "hints": ["The property name says what it does.", "It's about growing, not stretching."],
            },
            {
                "id": "flex_8",
                "type": "quiz",
                "question": "What does 'grid-template-columns: repeat(auto-fill, minmax(250px, 1fr))' create?",
                "options": [
                    "Exactly 250px wide columns",
                    "A responsive grid that auto-creates columns of at least 250px",
                    "A single column that is 250px to 100% wide",
                    "An infinite number of columns",
                ],
                "answer": "b",
                "lesson": (
                    "This is the holy grail of responsive grids — no media queries needed.\n\n"
                    "Breaking it down:\n"
                    "  repeat(auto-fill, ...) — create as many columns as fit\n"
                    "  minmax(250px, 1fr)     — each column: min 250px, max 1fr\n\n"
                    "Behavior:\n"
                    "  - Wide viewport: many columns side by side\n"
                    "  - Narrow viewport: fewer columns, items wrap\n"
                    "  - Below 250px viewport: single column\n\n"
                    "auto-fill vs auto-fit:\n"
                    "  auto-fill — keeps empty tracks\n"
                    "  auto-fit  — collapses empty tracks (items stretch)"
                ),
                "xp": 100,
                "difficulty": "hard",
                "hints": ["auto-fill creates as many tracks as fit.", "minmax sets a size range per column."],
            },
        ],
    },
    # ── Zone 5: Responsive Design ────────────────────────────────
    "responsive_design": {
        "id": "responsive_design",
        "name": "The Viewport Forge",
        "subtitle": "Responsive Design & Media Queries",
        "color": "blue",
        "icon": "<>",
        "challenges": [
            {
                "id": "resp_1",
                "type": "quiz",
                "question": "Which meta tag is essential for responsive design on mobile devices?",
                "options": [
                    "<meta charset=\"utf-8\">",
                    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">",
                    "<meta name=\"mobile\" content=\"true\">",
                    "<meta http-equiv=\"responsive\">",
                ],
                "answer": "b",
                "lesson": (
                    "The viewport meta tag controls how the page scales on mobile.\n\n"
                    "Without it, mobile browsers render at ~980px width and\n"
                    "zoom out — making everything tiny.\n\n"
                    "The standard tag:\n"
                    "  <meta name=\"viewport\"\n"
                    "        content=\"width=device-width, initial-scale=1\">\n\n"
                    "  width=device-width — match the screen width\n"
                    "  initial-scale=1    — no zoom on load\n\n"
                    "This tag goes in the <head> of every responsive page."
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["It's a meta tag.", "It tells the browser about the viewport."],
            },
            {
                "id": "resp_2",
                "type": "quiz",
                "question": "What does a 'mobile-first' CSS approach mean?",
                "options": [
                    "Only design for mobile devices",
                    "Write base styles for mobile, then add complexity with min-width queries",
                    "Use max-width media queries for everything",
                    "Disable features on desktop",
                ],
                "answer": "b",
                "lesson": (
                    "Mobile-first: base styles are for the smallest screen.\n\n"
                    "Approach:\n"
                    "  1. Write CSS for mobile (no media query)\n"
                    "  2. Add complexity with @media (min-width: ...)\n\n"
                    "Example:\n"
                    "  .grid { display: block; }  /* mobile: stacked */\n"
                    "  @media (min-width: 768px) {\n"
                    "    .grid { display: grid; grid-template-columns: 1fr 1fr; }\n"
                    "  }\n\n"
                    "Why mobile-first?\n"
                    "  - Simpler base styles\n"
                    "  - Less CSS to override\n"
                    "  - Better performance on weaker devices"
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["Start with the smallest screen.", "min-width queries add complexity upward."],
            },
            {
                "id": "resp_3",
                "type": "quiz",
                "question": "Which CSS unit is relative to the root element's font size?",
                "options": ["em", "rem", "px", "vw"],
                "answer": "b",
                "lesson": (
                    "rem stands for 'root em' — relative to <html> font size.\n\n"
                    "Relative units:\n"
                    "  rem — relative to root font size (usually 16px)\n"
                    "  em  — relative to parent element's font size\n"
                    "  %   — relative to parent's dimension\n"
                    "  vw  — 1% of viewport width\n"
                    "  vh  — 1% of viewport height\n\n"
                    "Why rem over em?\n"
                    "  em compounds: nested elements multiply sizes\n"
                    "  rem is predictable: always relative to one value\n\n"
                    "Default: 1rem = 16px (unless html font-size is changed)."
                ),
                "xp": 50,
                "difficulty": "easy",
                "hints": ["The 'r' stands for 'root'.", "It's like em but more predictable."],
            },
            {
                "id": "resp_4",
                "type": "quiz",
                "question": "What is the correct syntax for a media query that applies above 768px?",
                "options": [
                    "@media screen (768px) { }",
                    "@media (min-width: 768px) { }",
                    "@screen (width > 768px) { }",
                    "@breakpoint (768px) { }",
                ],
                "answer": "b",
                "lesson": (
                    "@media (min-width: 768px) activates when viewport >= 768px.\n\n"
                    "Media query syntax:\n"
                    "  @media (condition) { rules }\n\n"
                    "Common breakpoints:\n"
                    "  480px  — large phones\n"
                    "  768px  — tablets\n"
                    "  1024px — laptops\n"
                    "  1200px — desktops\n\n"
                    "Combining conditions:\n"
                    "  @media (min-width: 768px) and (max-width: 1024px)\n"
                    "  → applies only between 768px and 1024px\n\n"
                    "Modern syntax: @media (width >= 768px) — range syntax."
                ),
                "xp": 75,
                "difficulty": "medium",
                "hints": ["It starts with @media.", "min-width is the mobile-first approach."],
            },
            {
                "id": "resp_5",
                "type": "quiz",
                "question": "Which CSS function creates fluid typography that scales with the viewport?",
                "options": ["calc()", "clamp()", "var()", "min()"],
                "answer": "b",
                "lesson": (
                    "clamp(min, preferred, max) sets a responsive value.\n\n"
                    "Syntax: clamp(minimum, preferred, maximum)\n\n"
                    "Example — fluid font size:\n"
                    "  font-size: clamp(1rem, 2.5vw, 2rem);\n"
                    "  → Never smaller than 1rem\n"
                    "  → Scales with 2.5% of viewport width\n"
                    "  → Never larger than 2rem\n\n"
                    "This replaces complex media query breakpoints\n"
                    "for font sizes, widths, and spacing.\n\n"
                    "Related functions:\n"
                    "  min() — returns the smaller value\n"
                    "  max() — returns the larger value"
                ),
                "xp": 75,
                "difficulty": "medium",
                "hints": ["It takes three arguments: min, preferred, max.", "It 'clamps' a value within a range."],
            },
            {
                "id": "resp_6",
                "type": "quiz",
                "question": "How do you prevent images from overflowing their container?",
                "options": [
                    "img { max-width: 100%; height: auto; }",
                    "img { width: 100vw; }",
                    "img { overflow: hidden; }",
                    "img { position: absolute; }",
                ],
                "answer": "a",
                "lesson": (
                    "max-width: 100% + height: auto = responsive images.\n\n"
                    "The responsive image pattern:\n"
                    "  img {\n"
                    "    max-width: 100%;  /* never wider than container */\n"
                    "    height: auto;     /* maintain aspect ratio */\n"
                    "  }\n\n"
                    "For modern layouts, also consider:\n"
                    "  img { width: 100%; object-fit: cover; }\n"
                    "  → Fills container, crops if needed\n\n"
                    "  img { aspect-ratio: 16/9; object-fit: cover; }\n"
                    "  → Maintains specific ratio\n\n"
                    "The <picture> element provides art direction for\n"
                    "different screen sizes with <source> elements."
                ),
                "xp": 75,
                "difficulty": "medium",
                "hints": ["Limit the maximum width.", "Preserve the aspect ratio."],
            },
            {
                "id": "resp_7",
                "type": "quiz",
                "question": "What is a CSS container query and how does it differ from a media query?",
                "options": [
                    "Container queries check the viewport; media queries check the element",
                    "Container queries respond to a parent container's size, not the viewport",
                    "Container queries only work with grid layouts",
                    "There is no difference; they are aliases",
                ],
                "answer": "b",
                "lesson": (
                    "Container queries respond to a parent's size, not the viewport.\n\n"
                    "Setup:\n"
                    "  .parent { container-type: inline-size; }\n\n"
                    "Usage:\n"
                    "  @container (min-width: 400px) {\n"
                    "    .child { display: flex; }\n"
                    "  }\n\n"
                    "Why this matters:\n"
                    "  Media queries: 'how wide is the VIEWPORT?'\n"
                    "  Container queries: 'how wide is the PARENT?'\n\n"
                    "Container queries enable truly reusable components\n"
                    "that adapt to where they're placed, not just the screen."
                ),
                "xp": 100,
                "difficulty": "hard",
                "hints": ["Think about component-level responsiveness.", "It checks the parent, not the screen."],
            },
            {
                "id": "resp_8",
                "type": "quiz",
                "question": "What does 'prefers-color-scheme: dark' detect in a media query?",
                "options": [
                    "The website's current theme setting",
                    "The user's operating system dark mode preference",
                    "Whether the screen brightness is low",
                    "The background color of the page",
                ],
                "answer": "b",
                "lesson": (
                    "prefers-color-scheme detects the OS-level dark/light preference.\n\n"
                    "Usage:\n"
                    "  @media (prefers-color-scheme: dark) {\n"
                    "    body { background: #1a1a1a; color: #eee; }\n"
                    "  }\n\n"
                    "Other preference media queries:\n"
                    "  prefers-reduced-motion  — user wants less animation\n"
                    "  prefers-contrast        — user wants more contrast\n"
                    "  prefers-reduced-data    — user wants less data usage\n\n"
                    "These enable inclusive, accessible design that\n"
                    "respects user preferences without JavaScript."
                ),
                "xp": 100,
                "difficulty": "hard",
                "hints": ["It's about user preferences.", "It detects an OS-level setting."],
            },
        ],
    },
}
