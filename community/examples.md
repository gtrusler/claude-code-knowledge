# Claude Code Examples

*Real-world patterns and solutions*

## Hooks Examples

### Auto-Format on Save
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "file=$(echo '$' | jq -r '.tool_input.file_path // .tool_input.files[0].path // empty'); [ -n \"$file\" ] && { case \"$file\" in *.py) black \"$file\" ;; *.js|*.ts|*.jsx|*.tsx) prettier --write \"$file\" ;; *.go) gofmt -w \"$file\" ;; esac; }"
          }
        ]
      }
    ]
  }
}
```

### Command Logger with Descriptions
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '\"\\(.tool_input.command) - \\(.tool_input.description // \"No description\")\"' >> ~/.claude/bash-command-log.txt"
          }
        ]
      }
    ]
  }
}
```

### Protect Production Files
```python
#!/usr/bin/env python3
# save as ~/scripts/protect-prod.py
import json
import sys

PROTECTED_PATHS = ['/etc/', '/usr/', '/System/', 'production/', '.env']

data = json.load(sys.stdin)
if data.get('tool_name') in ['Write', 'Edit', 'MultiEdit']:
    path = data.get('tool_input', {}).get('file_path', '')
    if any(protected in path for protected in PROTECTED_PATHS):
        print(f"Blocked: Attempting to modify protected path: {path}", file=sys.stderr)
        sys.exit(2)
```

### Smart Git Commits
```bash
#!/bin/bash
# Auto-commit after file changes
set -euo pipefail

# Parse input
input=$(cat)
tool_name=$(echo "$input" | jq -r '.tool_name')
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')

if [[ "$tool_name" =~ ^(Write|Edit|MultiEdit)$ ]] && [ -n "$file_path" ]; then
    # Check if file is in git repo
    if git ls-files --error-unmatch "$file_path" 2>/dev/null; then
        git add "$file_path"
        git commit -m "Auto-commit: Updated $(basename "$file_path")" || true
    fi
fi
```

## Task Patterns

### Safe Database Migrations
```bash
# Instead of running migrations directly
claude run "Migrate the database"

# Do this for safety
claude run "First, backup the database to ./backups/pre-migration-$(date +%s).sql"
claude run "Show me the migration that would run without executing it"
claude run "Now run the migration"
```

### Incremental Feature Development
```bash
# Break down into explicit steps
claude do "1. Create the database schema for users table"
claude do "2. Add the User model with validation"
claude do "3. Create CRUD endpoints for User"
claude do "4. Add tests for User endpoints"
claude do "5. Add authentication to User endpoints"
```

### Debugging Workflow
```bash
# When something breaks
claude do "Show me the last 20 lines of the error log"
claude do "Check if the service is running with 'ps aux | grep [service]'"
claude do "Show me the recent changes with 'git diff HEAD~1'"
```

## Project Setup Patterns

### New Project with Best Practices
```bash
claude do "Create a new Next.js project in ./my-app with TypeScript, Tailwind, and ESLint"
claude do "Set up the project structure: /components, /lib, /types, /hooks"
claude do "Create a .env.example with common variables"
claude do "Initialize git and create initial commit"
```

### Adding Claude Code Hooks to Existing Project
```bash
claude do "Create .claude/settings.json with hooks for auto-formatting Python and JS files"
claude do "Add a pre-commit hook that runs tests before allowing commits"
claude do "Create a command logger for audit trail"
```

## Integration Examples

### MCP + Hooks Combination
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__github__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"GitHub operation: $(date)\" >> ~/mcp-github-audit.log"
          }
        ]
      }
    ]
  }
}
```

### Notification Systems
```python
#!/usr/bin/env python3
# Custom notifier for important events
import json
import sys
import subprocess

data = json.load(sys.stdin)
message = data.get('message', '')

if 'needs your permission' in message.lower():
    # Critical - use system notification
    subprocess.run(['osascript', '-e', f'display notification "{message}" with title "Claude Code" sound name "Glass"'])
elif 'waiting for your input' in message.lower():
    # Just log it
    print(f"[{datetime.now()}] Claude is waiting", file=open('/tmp/claude-waiting.log', 'a'))
```

## Advanced Patterns

### Context-Aware Auto-Completion
```bash
# Hook that provides context based on current file
#!/bin/bash
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')

if [[ "$file_path" == *.test.js ]]; then
    echo "Remember to follow Jest patterns and include describe/it blocks" >&2
    exit 2
fi
```

### Smart Task Routing
```python
#!/usr/bin/env python3
# Route tasks based on content
import json
import sys

data = json.load(sys.stdin)
if data.get('tool_name') == 'Task':
    description = data.get('tool_input', {}).get('description', '')
    
    if 'database' in description.lower():
        print("Note: Check ./docs/database-patterns.md for our conventions", file=sys.stderr)
        sys.exit(2)
    elif 'api' in description.lower():
        print("Note: Follow RESTful patterns in ./docs/api-guide.md", file=sys.stderr)
        sys.exit(2)
```
