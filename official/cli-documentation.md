# Claude Code Official CLI Documentation Summary
*Source: https://docs.anthropic.com/en/docs/claude-code/* - January 2025*

This document consolidates key information from the official Claude Code documentation.

## CLI Reference

### Basic Commands
| Command | Description | Example |
|---------|-------------|---------|
| `claude` | Start interactive REPL | `claude` |
| `claude "query"` | Start REPL with initial prompt | `claude "explain this project"` |
| `claude -p "query"` | Query via SDK, then exit | `claude -p "explain this function"` |
| `cat file \| claude -p "query"` | Process piped content | `cat logs.txt \| claude -p "explain"` |
| `claude -c` | Continue most recent conversation | `claude -c` |
| `claude -r "<session-id>" "query"` | Resume session by ID | `claude -r "abc123" "Finish this PR"` |
| `claude update` | Update to latest version | `claude update` |
| `claude mcp` | Configure MCP servers | See MCP section |

### CLI Flags
| Flag | Description | Example |
|------|-------------|---------|
| `--add-dir` | Add additional working directories | `claude --add-dir ../apps ../lib` |
| `--allowedTools` | Allow tools without prompting | `"Bash(git log:*)" "Write"` |
| `--disallowedTools` | Deny specific tools | `"Bash(curl:*)" "WebFetch"` |
| `--print`, `-p` | SDK mode (programmatic usage) | `claude -p "query"` |
| `--output-format` | Output format (text, json, stream-json) | `claude -p "query" --output-format json` |
| `--verbose` | Show detailed output | `claude --verbose` |
| `--max-turns` | Limit conversation turns | `claude -p --max-turns 3 "query"` |
| `--model` | Select model (sonnet/opus) | `claude --model opus` |
| `--continue` | Continue recent conversation | `claude --continue` |
| `--dangerously-skip-permissions` | Skip all permission checks | `claude --dangerously-skip-permissions` |

## Interactive Mode Features

### Keyboard Shortcuts
- `Tab`: Autocomplete file paths and commands
- `Shift+Tab`: Switch input modes (doesn't work on Windows)
- `Escape` (double-tap): Navigate conversation history
- `Ctrl+C`: Cancel current operation
- `Ctrl+D`: Exit Claude Code

### Input Modes
1. **Normal mode**: Standard input
2. **Plan mode**: Activated with Shift+Tab (where supported)
3. **Auto-accept mode**: For automated workflows

## Slash Commands

### Essential Commands
| Command | Description |
|---------|-------------|
| `/clear` | Clear conversation context |
| `/summarize` | Summarize current conversation |
| `/status` | Show current task status |
| `/config` | Configure settings |
| `/allowed-tools` | Manage tool permissions |
| `/model` | Switch between models |
| `/continue` | Continue previous conversation |
| `/mcp` | Check MCP server status |
| `/bug` | Report issues |
| `/logout` | Sign out of current session |
| `/login` | Sign in with credentials |

### Advanced Commands
| Command | Description |
|---------|-------------|
| `/compact` | Compress context for long conversations |
| `/update-memory-bank` | Update CLAUDE.md and memory files |
| `/ccusage-daily` | Show usage statistics (custom) |

## Hooks System

### Hook Structure
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here"
          }
        ]
      }
    ]
  }
}
```

### Hook Events
- `PreToolUse`: Before tool execution
- `PostToolUse`: After tool execution
- `Notification`: System notifications
- `Stop`: Task completion

### Exit Codes
- `0`: Success (output not shown to Claude)
- `1`: Failure
- `2`: Success with output shown to Claude

## Memory Management

### CLAUDE.md File
- Store project-specific instructions
- Document conventions and patterns
- Maintain context across sessions
- Located in project root

### Memory Bank Pattern
Create `memory-bank/` folder with:
- `projectbrief.md`: One-sentence description
- `techContext.md`: Tech stack and versions
- `systemPatterns.md`: Architecture patterns
- `activeContext.md`: Current task status
- `progress.md`: Overall progress

## Settings Configuration

### Settings Hierarchy
1. Enterprise policies
2. Command line arguments
3. Local project settings (`.claude/settings.local.json`)
4. Shared project settings (`.claude/settings.json`)
5. User settings (`~/.claude/settings.json`)

### Key Settings
```json
{
  "apiKeyHelper": "/bin/generate_temp_api_key.sh",
  "cleanupPeriodDays": 30,
  "env": {"FOO": "bar"},
  "includeCoAuthoredBy": true,
  "permissions": {
    "allow": ["Bash(git diff:*)"],
    "deny": ["WebFetch"],
    "additionalDirectories": ["../docs/"],
    "defaultMode": "acceptEdits",
    "disableBypassPermissionsMode": "disable"
  }
}
```

### Environment Variables
| Variable | Purpose |
|----------|---------|
| `ANTHROPIC_API_KEY` | API key for Claude SDK |
| `ANTHROPIC_MODEL` | Custom model name |
| `BASH_DEFAULT_TIMEOUT_MS` | Default bash timeout |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | Max output length |
| `DISABLE_TELEMETRY` | Opt out of telemetry |
| `MAX_THINKING_TOKENS` | Extended thinking budget |

## Tools Reference

### Available Tools
| Tool | Description | Permission Required |
|------|-------------|---------------------|
| Agent | Run sub-agents for complex tasks | No |
| Bash | Execute shell commands | Yes |
| Edit | Make targeted file edits | Yes |
| MultiEdit | Multiple edits atomically | Yes |
| Read | Read file contents | No |
| Write | Create/overwrite files | Yes |
| TodoRead/TodoWrite | Task management | No |
| WebFetch | Fetch URL content | Yes |
| WebSearch | Search the web | Yes |
| Grep | Search file contents | No |
| Glob | Find files by pattern | No |

## Cost Management

### Model Costs (Per Message)
- **Opus 4**: ~$0.30 per "Hello"
- **Sonnet 4**: ~$0.06 per "Hello"
- Heavy users: ~$100/day without Max subscription

### Claude Max Benefits
- $200/month for unlimited usage
- Automatic model switching to preserve limits
- Rate limits reset every 5 hours

## Platform-Specific Configuration

### AWS Bedrock
```bash
export CLAUDE_CODE_USE_BEDROCK=true
# Authentication handled via AWS CLI
```

### Google Vertex AI
```bash
export CLAUDE_CODE_USE_VERTEX=true
# Authentication via gcloud CLI
```

## Best Practices Summary

1. **Clear context regularly** with `/clear`
2. **Use specific file paths** instead of descriptions
3. **Break down complex tasks** into smaller steps
4. **Leverage conversation history** with `-c` and `-r` flags
5. **Configure appropriate permissions** in settings.json
6. **Use hooks for automation** of repetitive tasks
7. **Monitor usage** with cost tracking tools
8. **Implement safety measures** when using skip-permissions mode