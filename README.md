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
official/                    # Anthropic documentation
├── docs/                   # Complete official documentation
│   ├── cli-reference.md    # CLI commands and flags
│   ├── interactive-mode.md # Keyboard shortcuts and features
│   ├── slash-commands.md   # Built-in and custom commands
│   ├── hooks.md           # Hooks system reference
│   └── memory.md          # Memory management guide
├── docs.md                # Auto-scraped overview (GitHub Action)
├── anthropic-best-practices.md  # Official best practices
├── cli-documentation.md   # Consolidated CLI guide
└── changelog.md           # Notable updates timeline

community/                 # Manually curated insights
├── best-practices.md     # Proven patterns that work
├── gotchas.md           # Things the docs don't tell you
├── examples.md          # Real-world usage patterns
└── multi-agent-tools.md # Advanced orchestration tools
```

## Quick Reference

### Essential Documentation
- **[CLI Reference](official/docs/cli-reference.md)** - All commands and flags
- **[Interactive Mode](official/docs/interactive-mode.md)** - Keyboard shortcuts, vim mode
- **[Slash Commands](official/docs/slash-commands.md)** - Built-in and custom commands
- **[Hooks System](official/docs/hooks.md)** - Automation and customization
- **[Memory Management](official/docs/memory.md)** - CLAUDE.md best practices

### Community Resources
- **[Best Practices](community/best-practices.md)** - What actually works
- **[Gotchas](community/gotchas.md)** - Common issues and solutions
- **[Examples](community/examples.md)** - Real-world patterns
- **[Multi-Agent Tools](community/multi-agent-tools.md)** - Parallax, Axivo, PM Framework

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

## Recent Highlights

### January 2025
- Complete official documentation added (CLI, hooks, memory, etc.)
- Multi-agent orchestration tools documented (Parallax, Axivo, PM Framework)
- Windows-specific issues identified
- Advanced slash commands from community

### Key Discoveries
- 99.7% performance improvement via caching (PM Framework)
- 60-70% speed gains with parallel TodoWrite
- Custom agent creation patterns
- Profile systems with persistent memory

## Daily Updates

GitHub Action scrapes official docs daily at 6 AM UTC. Community updates happen as discovered.