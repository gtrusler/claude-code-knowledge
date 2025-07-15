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
