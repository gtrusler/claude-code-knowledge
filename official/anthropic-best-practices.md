# Claude Code Best Practices from Anthropic
*Source: https://www.anthropic.com/engineering/claude-code-best-practices - January 2025*

Official best practices from Anthropic's engineering team for using Claude Code effectively.

## Core Philosophy

Claude Code is intentionally low-level and unopinionated, providing close to raw model access without forcing specific workflows. This design philosophy creates a flexible, customizable, scriptable, and safe power tool.

## Key Best Practices

### 1. Iterative Development
- While the first version might be good, after 2-3 iterations it will typically look much better
- Give Claude the tools to see its outputs for best results
- Let Claude refine and improve based on feedback

### 2. YOLO Mode (Use with Caution)
```bash
claude --dangerously-skip-permissions
```
- Bypasses all permission checks and lets Claude work uninterrupted
- Works well for workflows like:
  - Fixing lint errors
  - Generating boilerplate code
  - Automated refactoring
- **WARNING**: Can result in data loss, system corruption, or data exfiltration
- **Safety**: Use in a container without internet access
- Reference implementation: Docker Dev Containers

### 3. Learning and Exploration
When onboarding to a new codebase:
- Use Claude Code for learning and exploration
- Ask Claude the same questions you would ask another engineer
- Treat it as a pair programming partner

### 4. Task-Oriented Approach
From the tutorials section:
- Be specific about what you want to accomplish
- Break down complex tasks into smaller steps
- Use Claude's ability to understand project structure

### 5. Extended Thinking for Complex Problems
When working on complex architectural decisions or challenging bugs:
```bash
# Trigger extended thinking
"think about potential security vulnerabilities in this approach"
"think harder about edge cases we should handle"
```
- Use intensifying phrases: "think more", "think harder", "think longer"
- Most valuable for:
  - Complex architectural decisions
  - Challenging bug investigations
  - Multi-step implementation planning

### 6. Conversation Management
```bash
# Continue most recent conversation
claude --continue

# Resume specific conversation
claude --resume abc123 "Continue the refactoring"

# List previous conversations
# Use arrow keys to navigate and select
```

### 7. Working with Images
Claude Code can analyze images in your codebase:
- Screenshots of errors
- UI mockups
- Architecture diagrams
- Database schemas

### 8. Memory Management (CLAUDE.md)
Create a `CLAUDE.md` file in your project root:
- Store project conventions
- Document frequently used commands
- Maintain important context
- Share team instructions

### 9. MCP Integration
Configure Model Context Protocol servers for extended functionality:
```bash
# Check MCP status
/mcp

# Add MCP servers
claude mcp add my-server /path/to/server

# Scope options: local (default) or project
claude mcp add shared-server -s project /path/to/server
```

## Performance Optimization Tips

### 1. Smaller Requests = Faster Responses
- One file at a time when possible
- Be specific about what you want
- Use file paths instead of descriptions

### 2. Use Search Before Reading
- For large codebases, search first
- Reduces token usage
- Speeds up response time

### 3. Clear Context Regularly
- Use `/clear` between major task switches
- Prevents context bloat
- Maintains performance

## Authors and Contributors

Written by Boris Cherny. This work draws upon best practices from across the broader Claude Code user community, whose creative approaches and workflows continue to inspire us.

Special thanks to:
- Daisy Hollman
- Ashwin Bhat
- Cat Wu
- Sid Bidasaria
- Cal Rueb
- Nodir Turakulov
- Barry Zhang
- Drew Hodun
- And many other Anthropic engineers

## Additional Insights from Community

### Double-Tap Escape (Conversation Forking)
- Double-tap `Escape` to go back in conversation history
- Edit a previous prompt
- Explore different direction without losing context
- Effectively "forks" the conversation

### The Beaver Method (Debugging)
When stuck on a bug:
1. Ask Claude to add diagnostic logs to your code
2. Run the code
3. Copy/paste logs back to Claude
4. Ask it to identify top root causes

### Plan Mode Activation
- Activate plan mode with `shift+tab` twice
- Enables more thorough evaluation and planning
- Note: This doesn't work on Windows PowerShell (known issue)

## Cost Considerations

### With Claude Max ($200/month)
- Effectively unlimited usage with generous rate limits
- Mental shift from "is this worth it?" to "how can I offload more?"
- Typical heavy user would pay ~$100/day without Max

### Rate Limit Management
Claude Code automatically switches from Opus 4 to Sonnet 4 when Max users reach usage thresholds:
- Rate limits reset every 5 hours
- Override with `/model` command at session start
- Opus reaches limits ~5x faster than Sonnet