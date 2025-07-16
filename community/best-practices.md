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

## Workflow Methodologies

### Explore, Plan, Code, Test (EPCT) Workflow
*Source: https://www.anthropic.com/engineering/claude-code-best-practices - July 2025*

Anthropic recommends this systematic workflow for thorough implementation:

1. **Explore**
   - Use parallel subagents to find and read all relevant files
   - Gather examples and identify edit targets
   - Build comprehensive understanding before coding

2. **Plan**
   - Write detailed implementation plan
   - Include tests, documentation, and UI components
   - Use web research for unclear areas
   - Pause to ask user questions if needed
   - Use "think" keywords for complex problems:
     - `think` < `think hard` < `think harder` < `ultrathink`

3. **Code**
   - Follow existing codebase style
   - Prefer clear naming over extensive comments
   - Run autoformatting when done
   - Fix reasonable linter warnings

4. **Test**
   - Use parallel subagents to run tests
   - Ensure all tests pass
   - For UX changes, use browser testing
   - If problems found, return to planning stage

5. **Write Up**
   - Create PR description with:
     - What you set out to do
     - Choices made with justifications
     - Useful commands for future developers

### Custom Command Implementation
*Source: Reddit r/ClaudeAI - July 2025*

Save as `~/.claude/commands/explore-plan-code-test.md`:
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

Usage: `/explore-plan-code-test <task description>`

### Key Insights from Community
*Source: Reddit discussion - July 2025*

- **Plan Mode Integration**: EPCT workflow may already be partially integrated into Claude Code's system prompt (low confidence)
- **Test-Driven Alternative**: Some users prefer Test before Code for TDD approach
- **Plan Persistence**: Save plans to `.md` files for resuming across sessions
- **CLAUDE.md Balance**: Keep project instructions concise - avoid essays on methodology

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

## Cost Management with Claude Max
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

### Claude Max Subscription Value
- $200/month for effectively unlimited usage (generous rate limits)
- Single "Hello" to Claude Code costs ~$0.30 without subscription
- Typical heavy user would pay ~$100/day without Max
- Mental shift: From "is this worth using Claude for?" to "how can I offload more?"

### When to Get Claude Max
- If you're thinking about per-use costs
- If you're debating between Sonnet vs Opus
- If you want to experiment freely without cost anxiety

## Parallel Agent Workflows

### The Git Worktree Problem
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

**Problem**: Running multiple agents in worktrees becomes unmanageable
- Constant context switching between branches
- IDE window confusion
- Shared resources (Docker containers) conflicts
- Management overhead grows exponentially

**Solution**: Cloud-based agents (like Terragon) that:
- Run in isolated environments
- Create fresh branches automatically
- Don't require local resource management

### Background Agent Patterns
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

Background agents excel at:
1. **Explore tasks**: "Prototype this approach" - often never merged, read like proposals
2. **One-shot tasks**: Cleanup, removing feature flags, adding test coverage
3. **Boilerplate-heavy**: Following established patterns, creating internal pages
4. **Context-heavy debugging**: Bug investigation where fix is often just a few lines

### Hybrid Local + Background Workflow
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

**Start on Background (Terragon)**:
- Almost every task starts here
- Morning: Fire off batch of tasks (even from phone via voice)
- Average ~30 tasks/day

**Finish Locally**:
- Review changes and test
- Small tweaks to existing PRs
- Create scaffolding with TODOs for agents to finish
- Interactive tasks requiring back-and-forth

### Multi-Agent Management Tips
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

1. **System is crucial**: Without good task management, you'll do worse work
2. **Morning planning**: Decide how to spend the day by firing off tasks
3. **"Inbox zero" approach**: Clear/merge/close tasks throughout the day
4. **Dashboard tracking**: Visual overview of what's left to do

### When to Abandon and Restart
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

- If agent is going down wrong path, abandon rather than course-correct
- "That's wrong" rarely helps - better to start fresh with clearer instructions
- Learn the model's strengths/weaknesses through experimentation

### Task Breakdown for Agents
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

- Create smaller, more agent-friendly tasks
- Lower cost of exploration encourages more experimentation
- Focus human time on parts requiring judgment
- Not every task needs an agent - learn when to do it yourself


## Claude Max vs API Limitations

### What Claude Max CANNOT Do
*Source: Community verification - 2025*

Claude Max subscription ($200/month) provides unlimited usage but:
- **No headless mode** (`claude -p`) - requires API access
- **No programmatic access** - interactive CLI only
- **No CI/CD integration** - can't automate in pipelines

### Automation Workarounds for Claude Max
*Source: Community patterns - 2025*

Since headless mode requires API:
1. **Cloud agents** (Terragon) - run Claude Code in cloud environments
2. **Git worktrees** - manually manage parallel instances
3. **Task batching** - queue up work for manual processing
4. **Voice input** - dictate tasks from mobile for later execution