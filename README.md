# Quest Platform

**The unified educational gaming platform — all 6 games, one login, 130 chapters.**

This is the single-deployment version of Quest Engine that serves all games as courses within one app.

## Games

| Category | Game | Chapters |
|----------|------|----------|
| Kids (5-12) | The Primer | 44 |
| DevOps | NEXUS Quest | 41 |
| AI/ML | AI Academy | 12 |
| Language | Learn Chinese | 11 |
| Language | Learn Spanish | 11 |
| Language | Learn Japanese | 11 |
| **Total** | | **130 chapters, 5,931 challenges** |

## Deploy

```bash
vercel --prod
```

## Local Dev

```bash
pip install -r requirements.txt
python -c "from api.index import app; import uvicorn; uvicorn.run(app, port=8080)"
```

## Architecture

The platform imports all 6 game packages and loads their skill packs into a single Quest Engine hub. Categories group packs by subject area on the landing page.

Built on [Quest Engine](https://github.com/thorski1/quest-engine).
