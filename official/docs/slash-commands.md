# Claude Code Slash Commands
*Source: https://docs.anthropic.com/en/docs/claude-code/slash-commands*

Control Claude's behavior during an interactive session with slash commands.

## Built-in Slash Commands

| Command | Purpose |
|---------|---------|
| `/bug` | Report bugs (sends conversation to Anthropic) |
| `/clear` | Clear conversation history |
| `/compact [instructions]` | Compact conversation with optional focus instructions |
| `/config` | View/modify configuration |
| `/cost` | Show token usage statistics |
| `/doctor` | Checks the health of your Claude Code installation |
| `/help` | Get usage help |
| `/init` | Initialize project with CLAUDE.md guide |
| `/login` | Switch Anthropic accounts |
| `/logout` | Sign out from your Anthropic account |
| `/memory` | Edit CLAUDE.md memory files |
| `/model` | Select or change the AI model |
| `/permissions` | View or update permissions |
| `/pr_comments` | Generate pull request comments |
| `/review` | Review code changes |
| `/status` | Show current status |
| `/terminal-setup` | Configure terminal settings |
| `/vim` | Enable/disable vim mode |

## Custom Slash Commands

Custom slash commands allow you to define frequently-used prompts as Markdown files that Claude Code can execute. Commands are organized by scope (project-specific or personal) and support namespacing through directory structures.

### Syntax

```
/<prefix>:<command-name> [arguments]
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| `<prefix>` | Command scope (`project` for project-specific, `user` for personal) |
| `<command-name>` | Name derived from the Markdown filename (without .md extension) |
| `[arguments]` | Optional arguments passed to the command |

### Command Types

#### Project Commands

Commands stored in your repository and shared with your team.

- **Location**: `.claude/commands/`
- **Prefix**: `/project:`

Example: Creating `/project:optimize` command:
```bash
# Create the command file
echo "Optimize the following code for performance: \$ARGUMENTS" > .claude/commands/optimize.md

# Use the command
/project:optimize "function calculateTotal() { ... }"
```

#### Personal Commands

Commands available across all your projects.

- **Location**: `~/.claude/commands/`
- **Prefix**: `/user:`

Example: Creating `/user:security-review` command:
```bash
# Create the command file
echo "Review the following code for security vulnerabilities: \$ARGUMENTS" > ~/.claude/commands/security-review.md

# Use the command
/user:security-review "app.post('/login', (req, res) => { ... })"
```

### Features

#### Namespacing

Organize commands in subdirectories to create namespaced commands.

**Structure**: `<prefix>:<namespace>:<command>`

For example, a file at `.claude/commands/frontend/component.md` creates the command `/project:frontend:component`

#### Arguments

Pass dynamic values to commands using the `$ARGUMENTS` placeholder.

For example:
```markdown
# File: .claude/commands/test.md
Write unit tests for the following function:

$ARGUMENTS

Include edge cases and error scenarios.
```

### File Format

Command files must:
- Use Markdown format (`.md` extension)
- Contain the prompt or instructions as file content
- Be placed in the appropriate commands directory

## See Also

- [Interactive mode](/en/docs/claude-code/interactive-mode) - Shortcuts, input modes, and interactive features
- [CLI reference](/en/docs/claude-code/cli-reference) - Command-line flags and options
- [Settings](/en/docs/claude-code/settings) - Configuration options
- [Memory management](/en/docs/claude-code/memory) - Managing Claude's memory across sessions