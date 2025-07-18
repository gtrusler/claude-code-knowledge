# Claude Code CLI Reference
*Source: https://docs.anthropic.com/en/docs/claude-code/cli-reference*

Complete reference for Claude Code command-line interface, including commands and flags.

## CLI Commands

| Command | Description | Example |
|---------|-------------|---------|
| `claude` | Start interactive REPL | `claude` |
| `claude "query"` | Start REPL with initial prompt | `claude "explain this project"` |
| `claude -p "query"` | Query via SDK, then exit | `claude -p "explain this function"` |
| `cat file \| claude -p "query"` | Process piped content | `cat logs.txt \| claude -p "explain"` |
| `claude -c` | Continue most recent conversation | `claude -c` |
| `claude -c -p "query"` | Continue via SDK | `claude -c -p "Check for type errors"` |
| `claude -r "<session-id>" "query"` | Resume session by ID | `claude -r "abc123" "Finish this PR"` |
| `claude update` | Update to latest version | `claude update` |
| `claude mcp` | Configure Model Context Protocol (MCP) servers | See the MCP documentation |

## CLI Flags

Customize Claude Code's behavior with these command-line flags:

| Flag | Description | Example |
|------|-------------|---------|
| `--add-dir` | Add additional working directories for Claude to access (validates each path exists as a directory) | `claude --add-dir ../apps ../lib` |
| `--allowedTools` | A list of tools that should be allowed without prompting the user for permission, in addition to settings.json files | `"Bash(git log:*)" "Bash(git diff:*)" "Write"` |
| `--disallowedTools` | A list of tools that should be denied, in addition to settings.json files | `"Bash(git log:*)" "Bash(git diff:*)" "Write"` |
| `--print`, `-p` | Non-interactive mode (see SDK documentation for programmatic usage details) | `claude -p "query"` |
| `--output-format` | Output format (`text`, `json`, `stream-json`) | `claude -p "query" --output-format json` |
| `--input-format` | Input format (`text`, `stream-json`) | `claude -p --output-format json --input-format stream-json` |
| `--verbose` | Enable verbose output | `claude --verbose` |
| `--max-turns` | Limit conversation turns | `claude -p --max-turns 3 "query"` |
| `--model` | Select model (`sonnet` or `opus`) or a model's full name | `claude --model claude-sonnet-4-20250514` |
| `--permission-prompt-tool` | Specify tool for permission prompts | `claude -p --permission-prompt-tool mcp_auth_tool "query"` |
| `--resume` | Resume specific conversation | `claude --resume abc123 "query"` |
| `--continue` | Continue most recent conversation | `claude --continue` |
| `--dangerously-skip-permissions` | Skip all permission checks | `claude --dangerously-skip-permissions` |

The `--output-format json` flag is particularly useful for scripting and automation, allowing you to parse Claude's responses programmatically.

For detailed information about print mode (`-p`) including output formats, streaming, verbose logging, and programmatic usage, see the SDK documentation.

## See Also

- [Interactive mode](/en/docs/claude-code/interactive-mode) - Shortcuts, input modes, and interactive features
- [Slash commands](/en/docs/claude-code/slash-commands) - Interactive session commands
- [Quickstart guide](/en/docs/claude-code/quickstart) - Getting started with Claude Code
- [Common workflows](/en/docs/claude-code/common-workflows) - Advanced workflows and patterns
- [Settings](/en/docs/claude-code/settings) - Configuration options
- [SDK documentation](/en/docs/claude-code/sdk) - Programmatic usage and integrations