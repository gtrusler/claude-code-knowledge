# Claude Code Best Practices

*Community-discovered patterns that work well*

## Project Management

### Use Slash Commands Early and Often
- `/clear` - Don't let context bloat
- `/summarize` - Before major transitions
- `/status` - Regularly check what Claude thinks is happening

### Context Management
- Clear context aggressively - smaller context = better performance
- Use explicit file paths rather than "the file we just edited"
- State assumptions explicitly

## Task Execution

### Break Down Complex Tasks
Instead of: "Build a full CRUD app"
Try: "First, let's set up the database schema"

### Be Explicit About Testing
- "Run the tests" often gets skipped
- "Run `npm test` and paste the output" works better

## File Operations

### Prefer Explicit Over Implicit
- ❌ "Update the config"
- ✅ "Edit `/home/user/project/config.json` to add..."

### Watch for Path Assumptions
Claude Code sometimes assumes current directory incorrectly. Always verify with `pwd` first.

## Error Handling

### When Things Go Wrong
1. Don't immediately retry the same command
2. Ask Claude to diagnose: "What went wrong with that command?"
3. Often the fix is simpler than expected

### Common Recovery Patterns
- Git issues: Usually solved with `git add -A && git commit`
- Permission issues: Check file ownership, not just chmod
- Module not found: Verify you're in the right directory

## Performance Tips

### Speed Up Responses
- Smaller requests = faster responses
- One file at a time when possible
- Use search before asking to read large codebases

### Reduce Token Usage
- Be specific about what you want
- Use file paths instead of descriptions
- Clear context between major task switches

## Advanced Context Techniques

### Plan Mode Activation
*Source: Community guide - 2024*

Activate plan mode with `shift+tab` twice. This enables more thorough evaluation and planning before execution.

### Think Keywords for Complex Problems
*Source: Community guide - 2024*

Use computation modifiers to allocate more reasoning time:
- `think` - Basic additional computation
- `think hard` - More intensive reasoning
- `think harder` - Deep analysis
- `ultrathink` - Maximum computational allocation

Example: "Think hard about the architecture before implementing"

### The /compact Command
*Source: Community guide - 2024*

For long multi-step tasks where context is still needed:
- Use `/compact` to summarize conversation and start fresh
- Reduces token usage while retaining essential context
- Add custom instructions to the summary if needed

## Workflow Patterns

### EPCC: Explore, Plan, Code, Commit
*Source: Community guide - 2024*

1. **Explore**: Have Claude read files/URLs for context (explicitly say "don't write code yet")
2. **Plan**: Activate plan mode (`shift+tab` twice), use think keywords
3. **Implement**: Have Claude implement and verify work
4. **Commit**: Create PR and update docs

### The Beaver Method (Debugging)
*Source: Community guide - 2024*

When stuck on a bug:
1. Ask Claude to add diagnostic logs to your code
2. Run the code
3. Copy/paste logs back to Claude
4. Ask it to identify top root causes

### Double-Tap Escape (Conversation Forking)
*Source: Community guide - 2024*

- Double-tap `Escape` to go back in conversation history
- Edit a previous prompt
- Explore different direction without losing context
- Effectively "forks" the conversation
