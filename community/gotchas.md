# Claude Code Gotchas

*Things that trip people up (and how to avoid them)*

## Sub Agent Gotchas
*Source: Official docs - January 2025*

### Context Starts Fresh
**Problem**: Sub agents start with zero context from main conversation
**Solution**: Include all necessary context in your request

### Tool Inheritance Confusion
**Problem**: Omitting `tools:` field gives agent ALL tools (including MCP)
**Symptom**: Agent has more permissions than expected
**Fix**: Explicitly list tools if you want restrictions

### Name Conflicts
**Problem**: Project agent and user agent with same name
**Solution**: Project agents take precedence - check with `/agents`

### Performance Overhead
**Problem**: Sub agents add latency as they gather context
**Solution**: Keep prompts focused, provide specific context

### The "PROACTIVELY" Trick
**Problem**: Claude doesn't use your sub agent automatically
**Fix**: Add "use PROACTIVELY" or "MUST BE USED" to description

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

## Context Management Gotchas

### Don't Use Compact
*Source: Claude Code community presentation - Jan 2025*

**Problem**: `/compact` generates weak summaries that make Claude "dumb"
**Solution**: Use rewind instead - go back to 40% context when hitting 5%

**Better approach:**
1. Document what you've done: "Claude, summarize our progress"
2. Rewind to earlier conversation point  
3. Resume with: "Here's what I've done so far. Continue."

### Context Investment Confusion
*Source: Claude Code community presentation - Jan 2025*

**Problem**: Jumping straight to execution without building context
**Symptom**: Claude makes obvious mistakes, doesn't understand codebase patterns
**Solution**: Always invest in context first with "prepare to discuss" prompts

**Example:**
❌ "Fix this authentication bug"
✅ "Prepare to discuss how our authentication system works" → then ask for fixes

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


## Windows-Specific Issues

### Shift+Tab Not Working
*Source: https://github.com/anthropics/claude-code/issues/3368 - July 2025*

**Problem**: Shift+Tab doesn't activate plan mode on Windows PowerShell
**Environment**: Windows 11, PowerShell, Claude Code 1.0.51+
**Status**: Known issue, no current workaround
**Alternative**: Use other planning strategies or different terminal

### File Edit Crashes on Windows
*Source: https://github.com/anthropics/claude-code/issues/3381 - July 2025*

**Problem**: Edit/Write tools crash with filesystem provider error
**Error**: `cannot open _claude_fs_right:c%3A%5Cprojects...`
**Cause**: Incorrect internal path handling on Windows
**Impact**: Can read files but crashes on edit attempts
**Status**: Active bug with Windows path encoding

## Planning Gotchas

### Over-Engineering Default
*Source: Claude Code community presentation - Jan 2025*

**Problem**: Claude defaults to enterprise-ready solutions
**Symptom**: Plans include graceful fallbacks, backwards compatibility, complex abstractions
**Solution**: Explicitly tell Claude to keep it simple

**Example prompt:** "Write elegant code. No backwards compatibility. No graceful fallbacks."

### Plan Mode vs Manual Planning
*Source: Claude Code community presentation - Jan 2025*

**Problem**: Built-in plan mode often produces weak plans
**Solution**: Ask Claude to plan manually with specific constraints

**Better approach:**
- "Write function names and 1-3 sentences about what they do"
- "Write test names in 5-10 words describing behavior"
- Force architectural thinking, not implementation details

## Hooks System Quirks

### Exit Code 0 Blindness
**Problem**: Claude doesn't see stdout when hook exits with 0
**Solution**: Use exit code 2 for feedback to Claude

### Matcher Patterns
**Problem**: `"*"` doesn't work as expected
**Solution**: Use empty string `""` for catch-all

### Hook Priority Order
*Source: https://github.com/disler/claude-code-hooks-mastery - January 2025*

**Problem**: Multiple control mechanisms can conflict
**Solution**: Understand priority order:
1. `"continue": false` - Takes precedence over all
2. `"decision": "block"` - Hook-specific blocking
3. Exit Code 2 - Simple blocking via stderr
4. Other Exit Codes - Non-blocking errors

### Hook Timeout Limit
*Source: https://github.com/disler/claude-code-hooks-mastery - January 2025*

**Problem**: Hooks have 60-second execution limit
**Symptom**: Long-running hooks fail silently
**Solution**: Keep hooks lightweight, offload heavy work