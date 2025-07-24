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

## Context Management Patterns

### Hierarchical Claude.md Files
*Source: Claude Code community presentation - Jan 2025*

Instead of one root `claude.md`, create detailed files in each subfolder:

```
project/
├── claude.md              # High-level overview
├── frontend/
│   └── claude.md          # Frontend-specific details
├── backend/
│   └── claude.md          # Backend-specific details
└── docs/
    ├── claude.md          # Documentation patterns
    ├── changelog.md       # Track why changes were made
    └── plan.md           # Current project goals
```

**Root claude.md example:**
```markdown
# Project Overview
Frontend: React + TypeScript (see ./frontend/claude.md)
Backend: Node.js + Express (see ./backend/claude.md)

## Cross-cutting Concerns
- Auth handled by backend, tokens stored in frontend
- Database migrations in ./backend/migrations/
- API documentation auto-generated from schemas
```

### Multiple Context Reviewer Pattern
*Source: Claude Code community presentation - Jan 2025*

Use separate Claude instances for different roles:

```bash
# Tab 1: Context Builder
"Prepare to discuss our authentication system architecture"
# Build deep context, double escape

# Tab 2: Planner (fresh instance) 
"My developer created this plan for auth improvements: [paste plan]
What are the risks and issues with this approach?"

# Tab 3: Executor (use saved context)
resume  # Gets the deep context from Tab 1
"Execute this refined plan: [final plan]"
```

This prevents Claude from being too positive about its own plans.

## GitHub Integration Hacks

### Custom GitHub Actions with Opus
*Source: Claude Code community presentation - Jan 2025*

When setting up GitHub integration, you can modify the generated YAML:

```yaml
# In .github/workflows/claude-code.yml
# Uncomment this line to use Opus instead of Sonnet:
model: claude-3-5-opus-20241022

# Add OAuth support for max plan usage
auth:
  type: oauth  # Uses your max plan instead of API key
```

### Enhanced GitHub Integration
*Source: Claude Code community presentation - Jan 2025*

You can customize the GitHub integration to include MCPs and additional tooling:

```yaml
# Add MCPs to your GitHub workflow
environment:
  CUSTOM_MCPS: |
    - mcp__github__search
    - mcp__linear__tasks
    
# Point to additional config files
config_files:
  - ./docs/api-guide.md
  - ./docs/database-patterns.md
  
# Custom bash tooling access
permissions:
  - gh cli
  - docker
  - npm scripts
```

**Multi-task automation example:**
```bash
# Create multiple PRs from a list
claude do "Generate PRs for these features: auth, payments, notifications. Tag @claude in each."
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

## Multi-Agent Development Patterns

### ClaudePreference Orchestrated Development
*Source: https://github.com/penwyp/ClaudePreference - January 2025*

A comprehensive multi-agent system using three specialized Claude Code agents:

**Architecture**:
- **Orchestrator Agent**: Strategic planning, architecture decisions, workflow coordination
- **Developer Agent**: Implementation with research-informed coding practices
- **Reviewer Agent**: Quality assurance, security validation, completeness checks

**Key Features**:
- Research-driven approach with MCP tools integration
- Template-based prompt generation for consistent agent communication
- Dynamic context-aware prompts with strict quality enforcement
- Build verification with 100% functional coverage requirement
- Evidence-based decision making with external validation

**Communication Flow**:
```
Orchestrator → Developer:
- Task specification
- Recommended patterns from research
- Architecture constraints

Developer → Orchestrator:
- Complete implementation
- No TODO/stub code
- Build verification passed

Orchestrator → Reviewer:
- Code for review
- Architecture context
- Research references

Reviewer → Orchestrator:
- Detailed findings
- External validation results
- Accept/Reject decision
```

**Usage**: `/m-orchestrated-dev requirements.md`

### Claude Code Agent Farm
*Source: Hacker News Show HN - January 2025*

Parallel processing framework for running multiple Claude Code sessions:

**Key Features**:
- Run 20+ Claude Code agents simultaneously (up to 50 with max_agents config)
- Multiple workflows: Bug fixing, best practices, coordinated multi-agent development
- Advanced lock-based system prevents conflicts between parallel agents
- Real-time dashboard showing agent status and progress
- Auto-recovery: Automatically restarts agents when needed
- Git commits and structured progress documents

**Best For**:
- Large-scale code improvements
- Systematic refactoring across codebases
- Parallel implementation of independent features

## Slash Command Examples

### Event-Driven Hook Framework
*Source: https://www.haihai.ai/hooks/ - July 2025*

Build a modular event dispatcher for Claude Code actions:

```python
#!/usr/bin/env python3
# Event-driven hook handler framework
import sys
import json
import subprocess
from pathlib import Path
import re

# Event mapping - map Claude events to handler functions
EVENT_MAP = {
    # System events
    "Notification": lambda d: handle_notification(d),
    "Stop": lambda d: handle_task_complete(d),
    
    # File operations
    "Edit": lambda d: handle_file_edit(d),
    "Write": lambda d: handle_file_write(d),
    
    # Task management
    "TodoWrite": lambda d: handle_todo_update(d),
}

# Pattern-based command handlers
BASH_PATTERNS = [
    (r'^git commit', handle_git_commit),
    (r'^gh pr', handle_pull_request),
    (r'^npm test|^pytest', handle_test_run),
    (r'.*', handle_generic_bash),  # Fallback
]

def log_event(event_data):
    """Log all events for auditing/debugging"""
    log_path = Path.home() / ".claude" / "events.jsonl"
    log_path.parent.mkdir(exist_ok=True)
    
    with open(log_path, "a") as f:
        f.write(json.dumps(event_data) + "\n")

def handle_notification(data):
    """Claude is ready - could trigger startup scripts"""
    pass

def handle_task_complete(data):
    """Task completed - could trigger notifications, git commits, etc"""
    pass

def handle_file_edit(data):
    """File edited - could trigger formatters, linters, tests"""
    file_path = data.get("tool_input", {}).get("file_path", "")
    
    # Example: Auto-format on save
    if file_path.endswith(('.py', '.js', '.ts')):
        # Trigger formatter based on file type
        pass

def handle_bash_command(data):
    """Route bash commands to appropriate handlers"""
    command = data.get("tool_input", {}).get("command", "")
    
    for pattern, handler in BASH_PATTERNS:
        if re.match(pattern, command, re.IGNORECASE):
            return handler(data)

def main():
    try:
        # Read event from Claude
        event_data = json.load(sys.stdin)
        
        # Log everything
        log_event(event_data)
        
        # Route to appropriate handler
        event_name = event_data.get("hook_event_name", "")
        tool_name = event_data.get("tool_name", "")
        
        # Handle system events
        if event_name in EVENT_MAP:
            EVENT_MAP[event_name](event_data)
        
        # Handle tool events
        elif tool_name in EVENT_MAP:
            EVENT_MAP[tool_name](event_data)
        
        # Special handling for bash
        elif tool_name == "Bash" and event_name == "PreToolUse":
            handle_bash_command(event_data)
        
        # Always exit successfully
        sys.exit(0)
        
    except Exception as e:
        print(f"Hook error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

Key insights:
- Use dictionary dispatch instead of if/elif chains
- Pattern matching for command-specific logic
- Structured logging for debugging
- Modular handlers for different event types

### Explore-Plan-Code-Test Command
*Source: https://www.anthropic.com/engineering/claude-code-best-practices + Reddit implementation - July 2025*

Create `~/.claude/commands/explore-plan-code-test.md`:
```markdown
At the end of this message, I will ask you to do something. Please follow the "Explore, Plan, Code, Test" workflow when you start.

# Explore
First, use parallel subagents to find and read all files that may be useful for implementing the ticket, either as examples or as edit targets. The subagents should return relevant file paths, and any other info that may be useful.

# Plan
Next, think hard and write up a detailed implementation plan. Don't forget to include tests, lookbook components, and documentation. Use your judgement as to what is necessary, given the standards of this repo.

If there are things you are not sure about, use parallel subagents to do some web research. They should only return useful information, no noise.

If there are things you still do not understand or questions you have for the user, pause here to ask them before continuing.

# Code
When you have a thorough implementation plan, you are ready to start writing code. Follow the style of the existing codebase (e.g. we prefer clearly named variables and methods to extensive comments). Make sure to run our autoformatting script when you're done, and fix linter warnings that seem reasonable to you.

# Test
Use parallel subagents to run tests, and make sure they all pass.

If your changes touch the UX in a major way, use the browser to make sure that everything works correctly. Make a list of what to test for, and use a subagent for this step.

If your testing shows problems, go back to the planning stage and think ultrahard.

# Write up your work
When you are happy with your work, write up a short report that could be used as the PR description. Include what you set out to do, the choices you made with their brief justification, and any commands you ran in the process that may be useful for future developers to know about.

$ARGUMENTS
```

**Usage**: `/explore-plan-code-test <task description>`

**Benefits**:
- Forces systematic approach to complex tasks
- Reduces errors from rushing into implementation
- Creates better documentation trail
- Encourages thorough testing

### Modular Command Examples

#### Feature Creation Command
*Source: https://github.com/oxygen-fragment/claude-modular - July 2025*

Create `~/.claude/commands/project-create-feature.md`:
```xml
<instructions>
  <requirements>
    - Valid feature name provided
    - Git repository initialized
    - No uncommitted changes
  </requirements>
  
  <execution>
    1. Create feature branch: git checkout -b feature/{name}
    2. Create directory structure:
       - src/features/{name}/
       - src/features/{name}/components/
       - src/features/{name}/hooks/
       - src/features/{name}/types/
    3. Generate base files:
       - index.ts with exports
       - README.md with feature description
       - {Name}.test.tsx with initial test
  </execution>
  
  <validation>
    - Branch exists and is checked out
    - Directory structure created
    - All files generated with correct naming
  </validation>
  
  <examples>
    Input: /project:create-feature auth-system
    Result: Creates feature/auth-system branch with full structure
  </examples>
</instructions>
```

#### Code Review Command
*Source: https://github.com/oxygen-fragment/claude-modular - July 2025*

Create `~/.claude/commands/dev-code-review.md`:
```xml
<instructions>
  <requirements>
    - Git repository with changes
    - Optional focus area (security, performance, style)
  </requirements>
  
  <execution>
    1. Get diff: git diff --cached or git diff HEAD~1
    2. Analyze based on focus:
       - security: Check for vulnerabilities, exposed secrets
       - performance: Look for O(n²), unnecessary renders
       - style: Verify naming conventions, formatting
    3. Generate review with:
       - Severity levels (critical, warning, suggestion)
       - Line-specific comments
       - Overall assessment
  </execution>
  
  <validation>
    - Review covers all changed files
    - Actionable feedback provided
    - No false positives
  </validation>
  
  <examples>
    Input: /dev:code-review --focus=security
    Output: Markdown report with security-focused review
  </examples>
</instructions>
```

## Background Agent Patterns

### Race Condition Debugging
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

Background agents excel at context-heavy debugging. Example from Terragon:
- **Problem**: Race condition with error messages in distributed system
- **Task**: "Investigate the race condition where error messages appear unexpectedly"
- **Result**: Agent identified and fixed issue in one shot by reading through extensive codebase

### User Bug Report First Pass
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

Pattern for handling user bug reports:
1. Send bug description to background agent immediately
2. Even if implementation isn't perfect, agent's analysis provides insights
3. Use agent's thought process to understand problem better
4. ~50% of bug reports get useful first pass from agent

### Incremental Prototyping
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

Use background agents to explore solutions incrementally:
```bash
# Start vague
claude do "Prototype a way to handle user sessions"

# Read output, learn about the problem space

# Get more specific
claude do "Implement session handling using Redis with JWT tokens"

# Read again, identify potential issues

# Final specific version
claude do "Implement Redis-backed JWT sessions with refresh token rotation"
```

Most prototype tasks are never merged but provide valuable learning.

### Morning Task Batch Pattern
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

Start your day by firing off tasks to background agents:
```bash
# Morning routine (can even do from phone with voice)
claude do "Fix the CSS alignment issue on mobile dashboard"
claude do "Add unit tests for the payment processing module"
claude do "Investigate why the cron job failed last night"
claude do "Prototype a solution for the rate limiting problem"
claude do "Clean up deprecated API endpoints"
```

Then spend the day reviewing and merging agent work.

## Workflow Optimization Patterns

### TDD Workflow Example
*Source: Community guide - 2024*

```bash
# Complete TDD cycle
claude do "Write tests for the user authentication feature - DO NOT implement yet"
claude do "Run the tests and confirm they fail"
claude do "Now implement just enough code to make the tests pass"
claude do "Refactor the implementation while keeping tests green"
```

### Git Worktree Setup for Parallel Agents
*Source: Community guide - 2024*

```bash
#!/bin/bash
# setup-worktree.sh - Create isolated worktree for Claude agent
set -euo pipefail

BRANCH=$1
WORKTREE_DIR="worktrees/$BRANCH"

# Create worktree
git worktree add "$WORKTREE_DIR" -b "$BRANCH"

# Copy config files
cp .env "$WORKTREE_DIR/.env" 2>/dev/null || true
cp -r .claude "$WORKTREE_DIR/.claude" 2>/dev/null || true

# Open in new terminal
echo "Worktree created at: $WORKTREE_DIR"
echo "Run: cd $WORKTREE_DIR && claude"
```

### Safe YOLO Mode Pattern
*Source: Community guide - 2024*

```bash
# Only in isolated environment!
# Useful for large refactoring or boilerplate generation

# First, ensure no network access
claude do "Disable network interfaces"

# Then run in skip-permissions mode
claude --dangerously-skip-permissions do "Apply ESLint fixes to entire codebase"

# Re-enable safety
claude do "Re-enable network interfaces"
```