# Claude Code Knowledge Repository

Living documentation of Claude Code capabilities, best practices, and community knowledge.

## Purpose

Claude Code documentation is scattered across:
- Official docs (often behind the actual features)
- YouTube tutorials
- Reddit threads
- Twitter/X posts
- Personal experiments

This repo consolidates that knowledge in one place, updated daily.

## Structure

```
official/          # Auto-scraped from Anthropic docs
├── docs.md       # Daily sync via GitHub Action
└── changelog.md  # Notable updates

community/         # Manually curated insights
├── best-practices.md  # Proven patterns that work
├── gotchas.md        # Things the docs don't tell you
└── examples.md       # Real-world usage patterns
```

## How to Use

### For Your Projects
Add this repo to your Claude Desktop project knowledge:
1. Clone locally: `git clone https://github.com/gtrusler/claude-code-knowledge`
2. In Claude Desktop: Add folder to project knowledge
3. Updates sync automatically via git pull

### For Contributing
1. Find valuable Claude Code content
2. Share with the curator project (see below)
3. Curator extracts insights and commits

## Curator Setup

Create a dedicated Claude Desktop project:
- Name: "Claude Code Knowledge Curator"
- Knowledge: This repo
- Prompt: "You curate Claude Code knowledge. Extract valuable insights, ignore noise, update the repo."

## What Belongs Here

✅ **Include:**
- Undocumented features
- Non-obvious workflows
- Performance tips
- Integration patterns
- Common pitfalls and solutions

❌ **Exclude:**
- Basic getting started (covered in official docs)
- Speculation or rumors
- Outdated information
- Personal preferences without justification

## Daily Updates

GitHub Action scrapes official docs daily at 6 AM UTC. Community updates happen as discovered.
