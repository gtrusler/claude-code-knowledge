# Claude Code Gotchas

*Things that trip people up (and how to avoid them)*

## The Big Ones

### Git Worktree Confusion
**Problem**: Claude Code gets confused about which git worktree it's in
**Solution**: Always use absolute paths and verify with `pwd`

### Uncommitted Changes After "Done"
**Problem**: Claude says "I've completed the task" but changes aren't committed
**Symptom**: `git status` shows modified files
**Solution**: Always check `git status` after "completion"

### The Phantom File Edit
**Problem**: Claude thinks it edited a file but didn't
**Symptom**: Claude references changes that don't exist
**Solution**: Ask to `cat` the file to verify

## File Operations

### Directory Creation Race Conditions
**Problem**: Tries to write file before creating parent directory
**Fix**: Explicitly create directories first

### Assumed File Locations
**Problem**: Claude assumes files are in current directory
**Example**: Edits `config.json` instead of `./src/config.json`
**Prevention**: Always use full paths

## Command Execution

### Silent Failures
**Problem**: Command fails but Claude doesn't notice
**Common with**: Background processes, piped commands
**Fix**: Add explicit error checking: `command || echo "Failed"`

### Environment Assumptions
**Problem**: Assumes environment variables exist
**Example**: Uses `$HOME` without checking
**Fix**: Verify environment first

## Task Management

### The Infinite Loop Task
**Problem**: Task creates subtasks endlessly
**Solution**: Set explicit completion criteria upfront

### Context Confusion
**Problem**: Mixes up details from different parts of conversation
**Fix**: Use `/clear` liberally

## Hooks System Quirks

### Exit Code 0 Blindness
**Problem**: Claude doesn't see stdout when hook exits with 0
**Solution**: Use exit code 2 for feedback to Claude

### Matcher Patterns
**Problem**: `"*"` doesn't work as expected
**Solution**: Use empty string `""` for catch-all

## MCP Tool Gotchas

### Tool Naming Convention
**Problem**: MCP tools have specific naming pattern
**Pattern**: `mcp__<server>__<tool>`
**Example**: `mcp__memory__create_entities`

## Recovery Strategies

### When Claude Gets Stuck
1. Don't keep retrying the same approach
2. Ask: "What specifically went wrong?"
3. Often a simple `cd` or `pwd` reveals the issue

### When Context Gets Messy
1. Save current state to a file
2. `/clear`
3. Reload from file with specific goal

### When Nothing Makes Sense
- Check if you're in the right directory
- Verify git branch
- Confirm file paths are absolute
- Look for uncommitted changes

## Token and Cost Gotchas

### Compounding Token Usage
*Source: Community guide - 2024*

**Problem**: Every message reprocesses entire chat history
**Impact**: Exponentially increasing costs in long conversations
**Solution**: Use `/clear` frequently between tasks

### Model Selection Confusion
*Source: Community guide - 2024*

**Problem**: Claude Code defaults to most expensive model (Opus 4)
**Solution**: Use `/model` to switch to lighter models for simple tasks
**Strategy**: Start with powerful model for planning, switch to cheaper for implementation

## Advanced Features

### Headless Mode (API Only)
*Source: Community verification - 2025*

**Important**: Headless mode (`claude -p`) requires API access, NOT available with Claude Max subscription
**Problem**: Cannot automate Claude Code with subscription plans
**Solution**: For automation with Claude Max, consider:
- Using cloud-based solutions like Terragon
- Manual batching of tasks
- Git worktrees for parallel work

### Multi-Agent Coordination
*Source: Community guide - 2024*

**Problem**: Multiple Claude instances can conflict on same codebase
**Solution**: Use git worktrees for isolated branches per agent
**Setup**: Script to create worktree + copy `.env` and `.claude` files

### The --dangerously-skip-permissions Frustration
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

**Problem**: Constantly approving simple commands like `find` breaks flow
**Context**: You want safety but not for every trivial command
**Solution**: Consider using skip-permissions mode in isolated environments
**Warning**: Only use when you trust the context completely

## Performance Degradation

### The 50% Context Threshold
*Source: Reddit r/ClaudeAI comprehensive guide - 2025*

**Problem**: Performance tanks when context bar exceeds 50%
**Symptoms**: Claude misses details, makes more errors, slower responses
**Solution**: Use `/compact` proactively, not reactively
**Follow-up**: Always restate current task after compacting
