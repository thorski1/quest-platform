"""
Quest Platform — Unified deployment serving ALL games as courses.

One app, one login, all 130 chapters across 6 games.
Deployed to Vercel as a single serverless function.
"""

import os
import sys
from pathlib import Path

# Add quest-engine to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Point at all game skill-packs directories
_GAMES = {
    "kids": {
        "label": "Kids (Ages 5-12)",
        "packs_dir": os.environ.get("PRIMER_PACKS_DIR", ""),
        "names": [
            "letters", "numbers", "science", "kindness", "geography",
            "math_advanced", "history", "art", "coding_basics", "space",
            "music", "animals", "words", "cooking", "body", "money",
            "environment", "thinking", "telling_time", "inventions",
            "oceans", "civics", "emotions", "measurement", "safety",
            "dinosaurs", "weather", "maps", "famous_people", "religions",
            "planets", "logic", "shapes", "sports", "simple_machines",
            "reading", "writing", "cultures", "health", "basic_math",
            "electricity", "plants", "insects", "astronomy",
        ],
    },
    "devops": {
        "label": "DevOps & Engineering",
        "packs_dir": os.environ.get("NEXUS_PACKS_DIR", ""),
        "names": [
            "bash", "ssh", "vim", "git", "docker", "postgres",
            "python", "regex", "linux", "kubernetes", "aws", "terraform",
            "networking", "security", "cicd", "observability", "databases",
            "golang", "api_design", "rust", "system_design", "typescript",
            "data_engineering", "shell_scripting", "cloud_native", "web_dev",
            "python_advanced", "dns_http", "ml_engineering", "linux_internals",
            "redis", "testing", "graphql", "microservices", "message_queues",
            "git_advanced", "auth", "monitoring", "containers", "iac",
            "sql_advanced",
        ],
    },
    "ai": {
        "label": "AI & Machine Learning",
        "packs_dir": os.environ.get("AI_PACKS_DIR", ""),
        "names": [
            "ai_basics", "prompt_engineering", "chatbots", "ai_tools",
            "ai_ethics", "ai_for_work", "ai_coding", "ai_agents",
            "ai_safety", "ai_rag", "ai_finetuning", "ai_multimodal",
        ],
    },
    "chinese": {
        "label": "Learn Chinese",
        "packs_dir": os.environ.get("CHINESE_PACKS_DIR", ""),
        "names": [
            "pinyin", "greetings", "numbers_chinese", "food_drink",
            "family", "daily_life", "travel", "culture",
            "colors_shapes", "weather_time", "body_health",
        ],
    },
    "spanish": {
        "label": "Learn Spanish",
        "packs_dir": os.environ.get("SPANISH_PACKS_DIR", ""),
        "names": [
            "basics", "greetings_es", "numbers_es", "food_es",
            "family_es", "travel_es", "daily_es", "culture_es",
            "colors_clothing", "weather_es", "restaurant_es",
        ],
    },
    "japanese": {
        "label": "Learn Japanese",
        "packs_dir": os.environ.get("JAPANESE_PACKS_DIR", ""),
        "names": [
            "hiragana", "katakana", "greetings_jp", "numbers_jp",
            "food_jp", "daily_jp", "travel_jp", "culture_jp",
            "colors_nature", "shopping_jp", "directions_jp",
        ],
    },
}


def create_app():
    """Build the unified platform app."""
    from engine.skill_pack import load_packs_from_dirs
    from engine.web.hub import create_hub_app

    # Load all packs from all games
    pack_configs = []
    for category_id, cfg in _GAMES.items():
        packs_dir = cfg["packs_dir"]
        if not packs_dir or not Path(packs_dir).exists():
            continue
        pack_configs.append({
            "packs_dir": packs_dir,
            "names": cfg["names"],
            "category": cfg["label"],
        })

    if not pack_configs:
        # Auto-detect from installed packages
        import importlib
        package_map = {
            "primer_game": "kids",
            "nexus_quest": "devops",
            "ai_academy": "ai",
            "learn_chinese": "chinese",
            "learn_spanish": "spanish",
            "learn_japanese": "japanese",
        }
        for pkg, category_id in package_map.items():
            try:
                mod = importlib.import_module(pkg)
                pkg_dir = Path(mod.__file__).parent / "skill-packs"
                if pkg_dir.exists() and category_id in _GAMES:
                    pack_configs.append({
                        "packs_dir": str(pkg_dir),
                        "names": _GAMES[category_id]["names"],
                        "category": _GAMES[category_id]["label"],
                    })
            except ImportError:
                pass

    if not pack_configs:
        # Last resort: try relative paths (local dev)
        base = Path(__file__).parent.parent.parent
        for game_dir, category_id in [
            ("primer/primer_game/skill-packs", "kids"),
            ("nexus-quest/nexus_quest/skill-packs", "devops"),
            ("ai-academy/ai_academy/skill-packs", "ai"),
            ("learn-chinese/learn_chinese/skill-packs", "chinese"),
            ("learn-spanish/learn_spanish/skill-packs", "spanish"),
            ("learn-japanese/learn_japanese/skill-packs", "japanese"),
        ]:
            full_path = base / game_dir
            if full_path.exists() and category_id in _GAMES:
                pack_configs.append({
                    "packs_dir": str(full_path),
                    "names": _GAMES[category_id]["names"],
                    "category": _GAMES[category_id]["label"],
                })

    all_packs = load_packs_from_dirs(pack_configs)

    if not all_packs:
        # Minimal fallback app
        from starlette.applications import Starlette
        from starlette.responses import HTMLResponse
        from starlette.routing import Route

        async def home(request):
            return HTMLResponse("<h1>Quest Platform</h1><p>No packs found. Set env vars for pack directories.</p>")

        return Starlette(routes=[Route("/", home)])

    return create_hub_app(all_packs)


app = create_app()
