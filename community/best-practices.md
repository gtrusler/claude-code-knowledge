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

## Custom Slash Commands

### Simple Hello World Command
*Source: https://github.com/hesreallyhim/awesome-claude-code - 2025*

Create `~/.claude/commands/say-hello.md`:
```markdown
# /say-hello

Print "Hello, world!" to the console and confirm the command system is working.
```

Usage: `/say-hello`

### Create Your Own Commands
*Source: Community patterns - 2025*

Commands are just markdown files in `~/.claude/commands/`:
- File name becomes command name (with `project:` prefix)
- Content is instructions for Claude
- Use `$ARGUMENTS` placeholder for user input
- Keep instructions clear and specific

## Modular CLAUDE.md Architecture
*Source: https://github.com/oxygen-fragment/claude-modular - July 2025*

### The Problem with Monolithic CLAUDE.md
- 2,000-5,000 word files that Claude mostly ignores
- Burns tokens loading everything on every request
- Claude gets overwhelmed and misses important instructions

### Modular Command System
*Discovered by Reddit user with ADHD optimizing for focus*

Instead of one massive CLAUDE.md, use 20+ specific command files:```
~/.claude/commands/
├── project-create-feature.md
├── dev-code-review.md
├── test-generate-tests.md
└── deploy-prepare-release.md
```

### Command Structure
```xml
<instructions>
  <requirements>What you need to not break everything</requirements>
  <execution>Step-by-step so Claude doesn't get creative</execution>
  <validation>How to know if it worked</validation>
  <examples>Real examples because abstract is useless</examples>
</instructions>
```

### Results
- **50-80% fewer tokens** per session
- **Consistent command following** - Claude actually does what you ask
- **Sub-30 second setup** for new projects
- **200 lines** in main CLAUDE.md vs 2,000+

### Implementation
1. Create `~/.claude/commands/` directory
2. Add command files with XML structure
3. Reduce main CLAUDE.md to project-specific context only
4. Use commands like: `/project:create-feature auth-system`

### Why It Works
- **Progressive disclosure** - Claude only loads what it needs
- **Specific context** - No vague "be helpful" instructions
- **XML structure** - Claude follows this format consistently
- **Just-in-time loading** - Commands load only when called

### Integration with MCP
Works seamlessly with MCP servers:
- Linear
- Notion
- Memory
- Filesystem
- Gemini (being added)

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

[Full workflow details in the command file]
```

Usage: `/explore-plan-code-test <task description>`

### Key Insights from Community
*Source: Reddit discussion - July 2025*

- **Plan Mode Integration**: EPCT workflow may already be partially integrated into Claude Code's system prompt (low confidence)
- **Test-Driven Alternative**: Some users prefer Test before Code for TDD approach
- **Plan Persistence**: Save plans to `.md` files for resuming across sessions
- **CLAUDE.md Balance**: Keep project instructions concise - avoid essays on methodology

## The Golden Rule: Treat Claude as an Amnesiac Expert
*Source: Reddit r/ClaudeAI comprehensive guide - 2025*

Claude Code is incredibly talented but forgets context every few minutes. Your primary job is building a perfect external brain that allows it to "regain its memory" and get to work at any moment.

## Project Setup Fundamentals

### The Core Rulebook (CLAUDE.md)
*Source: Reddit r/ClaudeAI comprehensive guide - 2025*

Create `CLAUDE.md` in your project root with essential rules at the top:
- "Development must follow TDD methodology"
- "All implementation must strictly follow steps in PLAN.md"
- "Primary tech stack is [X, Y, Z]. Do not introduce other libraries unless specified"

Keep it concise - this isn't a place for essays on methodology.

### The External Brain (memory-bank/ Folder)
*Source: Reddit r/ClaudeAI comprehensive guide - 2025*

The most critical component for complex projects. Create `memory-bank/` with:
- `projectbrief.md` - One-sentence project description
- `techContext.md` - Tech stack and versions
- `systemPatterns.md` - Architecture and design patterns
- `activeContext.md` - Current task and what's next
- `progress.md` - Overall project status

### Session Management Pattern
*Source: Reddit r/ClaudeAI comprehensive guide - 2025*

**End Session**: "Please update activeContext.md and progress.md to summarize our work and outline next steps"

**Start Session**: "Hello, let's continue the project. Please start by reading all files in CLAUDE.md and the memory-bank/ folder to fully understand the current project state"

## Planning Excellence

### The Checklist-Driven Plan (PLAN.md)
*Source: Reddit r/ClaudeAI comprehensive guide - 2025*

Each item must be a complete, executable prompt:
```markdown
- [ ] Prompt: "In the file `models/task.py`, create the Pydantic data model for 'Task', including id, title, description, and is_completed fields."
- [ ] Prompt: "In `database/crud.py`, write the function to create a new task and save it to the database."
- [ ] Prompt: "For the 'create a new task' function, write a failing unit test and save it in `tests/test_crud.py`."
```

### Cross-Examine Your Plan
*Source: Reddit r/ClaudeAI comprehensive guide - 2025*

Paste PLAN.md into another AI (Gemini, GPT-4) and ask: "This plan was written by another AI. As a critical senior engineer, what potential problems or risks do you see?"

Catches blind spots and assumptions.

## Implementation Discipline

### Be a Reviewer, Not a Chat Buddy
*Source: Reddit r/ClaudeAI comprehensive guide - 2025*

Review Claude's code like a PR from a junior:
- **95% correct**: Accept and tweak yourself
- **Clear flaws**: DON'T chat to fix - reject entirely, improve PLAN.md, retry

This prevents context pollution from back-and-forth debugging.

### The Magic Words
*Source: Reddit r/ClaudeAI comprehensive guide - 2025*

- **`ultrathink`**: Add to prompts for complex planning/analysis
- **`sub-task with agents`**: When reading/writing many files at once

### UI First, Logic Second
*Source: Reddit r/ClaudeAI comprehensive guide - 2025*

For apps with UI: Build interface with dummy data first, then implement backend. This clarifies requirements before diving into logic.

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

## Anti-Patterns (What Never to Do)
*Source: Reddit r/ClaudeAI comprehensive guide - 2025*

- ❌ **Vague Prompts**: "Make it look better" → ✅ "Change the 'Submit' button on the contact page to blue (#3498db)"
- ❌ **Dumping Whole Files**: Worst mistake for performance → ✅ Use file paths and line numbers (@src/api.py:15-30)
- ❌ **Asking AI to Design Whole System**: Architect first → ✅ Let LLM implement the pieces
- ❌ **Trusting "It Compiles" = "It Works"**: Always verify → ✅ Test, test, test again
- ❌ **"Vibe Coding" for Production**: Only for exploration → ✅ Creates mountains of technical debt

## The Context Bar Warning
*Source: Reddit r/ClaudeAI comprehensive guide - 2025*

Watch the context usage bar religiously:
- **>50%**: Performance degrades noticeably
- **Solution**: Use `/compact` command
- **Follow-up**: Immediately restate current task to refocus

This is more critical than most realize - degraded performance leads to missed details and errors.