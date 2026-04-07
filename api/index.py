"""
Quest Platform — Unified deployment serving ALL games as courses.

One app, one login, all 130 chapters across 6 games.
Packs are bundled directly in the packs/ directory.
"""

import os
import sys
from pathlib import Path

_ROOT = Path(__file__).parent.parent
_PACKS_DIR = _ROOT / "packs"

# Category mapping: pack_id -> category label
_CATEGORIES = {}

# Kids (Primer)
for p in [
    "letters", "numbers", "science", "kindness", "geography",
    "math_advanced", "history", "art", "coding_basics", "space",
    "music", "animals", "words", "cooking", "body", "money",
    "environment", "thinking", "telling_time", "inventions",
    "oceans", "civics", "emotions", "measurement", "safety",
    "dinosaurs", "weather", "maps", "famous_people", "religions",
    "planets", "logic", "shapes", "sports", "simple_machines",
    "reading", "writing", "cultures", "health", "basic_math",
    "electricity", "plants", "insects", "astronomy", "countries", "robotics", "brain", "python_kids", "ocean_explore", "earth_science",
]:
    _CATEGORIES[p] = "Kids (Ages 5-12)"

# DevOps (NEXUS)
for p in [
    "bash", "ssh", "vim", "git", "docker", "postgres",
    "python", "regex", "linux", "kubernetes", "aws", "terraform",
    "networking", "security", "cicd", "observability", "databases",
    "golang", "api_design", "rust", "system_design", "typescript",
    "data_engineering", "shell_scripting", "cloud_native", "web_dev",
    "python_advanced", "dns_http", "ml_engineering", "linux_internals",
    "redis", "testing", "graphql", "microservices", "message_queues",
    "git_advanced", "auth", "monitoring", "containers", "iac",
    "sql_advanced", "devsecops", "platform_eng", "sre", "k8s_advanced",
]:
    _CATEGORIES[p] = "DevOps & Engineering"

# AI (AI Academy)
for p in [
    "ai_basics", "prompt_engineering", "chatbots", "ai_tools",
    "ai_ethics", "ai_for_work", "ai_coding", "ai_agents",
    "ai_safety", "ai_rag", "ai_finetuning", "ai_multimodal", "ai_agents_adv",
]:
    _CATEGORIES[p] = "AI & Machine Learning"

# Languages
for p in ["pinyin", "greetings", "numbers_chinese", "food_drink",
           "family", "daily_life", "travel", "culture",
           "colors_shapes", "weather_time", "body_health", "transport", "school"]:
    _CATEGORIES[p] = "Learn Chinese"

for p in ["basics", "greetings_es", "numbers_es", "food_es",
           "family_es", "travel_es", "daily_es", "culture_es",
           "colors_clothing", "weather_es", "restaurant_es", "directions_es", "health_es"]:
    _CATEGORIES[p] = "Learn Spanish"

for p in ["hiragana", "katakana", "greetings_jp", "numbers_jp",
           "food_jp", "daily_jp", "travel_jp", "culture_jp",
           "colors_nature", "shopping_jp", "directions_jp", "family_jp", "weather_jp"]:
    _CATEGORIES[p] = "Learn Japanese"

# Ordered category display
_CATEGORY_ORDER = [
    "Kids (Ages 5-12)",
    "DevOps & Engineering",
    "AI & Machine Learning",
    "Learn Chinese",
    "Learn Spanish",
    "Learn Japanese",
]


def create_app():
    try:
        from engine.skill_pack import load_skill_pack
        from engine.web.hub import create_hub_app
    except ImportError as e:
        from starlette.applications import Starlette
        from starlette.responses import HTMLResponse
        from starlette.routing import Route
        err = str(e)
        async def home(request):
            return HTMLResponse(f"<h1>Import Error</h1><pre>{err}</pre>")
        return Starlette(routes=[Route("/", home), Route("/{path:path}", home)])

    all_packs = []
    errors = []
    for cat in _CATEGORY_ORDER:
        pack_ids = [pid for pid, c in _CATEGORIES.items() if c == cat]
        for pid in pack_ids:
            try:
                pack = load_skill_pack(pid, packs_dir=str(_PACKS_DIR))
                pack.category = cat
                all_packs.append(pack)
            except Exception as e:
                errors.append(f"{pid}: {e}")

    if not all_packs:
        from starlette.applications import Starlette
        from starlette.responses import HTMLResponse
        from starlette.routing import Route

        async def home(request):
            return HTMLResponse(
                "<h1>Quest Platform — Debug</h1>"
                f"<p>Packs dir: {_PACKS_DIR}</p>"
                f"<p>Exists: {_PACKS_DIR.exists()}</p>"
                f"<p>Categories: {len(_CATEGORIES)}</p>"
                f"<p>Errors ({len(errors)}):</p><pre>{'<br>'.join(errors[:20])}</pre>"
            )
        return Starlette(routes=[Route("/", home), Route("/{path:path}", home)])

    return create_hub_app(all_packs)


app = create_app()
