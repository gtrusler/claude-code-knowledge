# Claude Code Changelog

*Tracking notable updates to Claude Code*

## Format
Each entry includes:
- Date discovered
- Feature/change
- Source (if available)
- Impact notes

---

## 2025

### July 2025
- **Windows Issues Identified**:
  - Shift+Tab not working in PowerShell (Issue #3368)
  - File edit crashes with filesystem provider error (Issue #3381)
- **Cost Management Features**: Automatic Opus→Sonnet switching for Max users
- **Extended Thinking Prompts**: "think harder", "think longer" for deep reasoning
- *Source: GitHub issues + Anthropic documentation*

### January 2025
- **Sub Agents Feature Released** (`/agents` command):
  - Specialized AI assistants with custom prompts
  - Separate context windows preserve main conversation
  - Project (`.claude/agents/`) and user (`~/.claude/agents/`) levels
  - Configurable tool permissions per agent
  - Interactive creation and management interface
- **Multi-Agent Tools Released**:
  - Parallax: Parallel agent orchestration in Git worktrees
  - Axivo Claude: Profile system with persistent memory
  - Claude PM Framework: Unlimited custom agent creation
- **Advanced Slash Commands**:
  - `/apply-thinking-to`: Expert prompt engineering
  - `/convert-to-todowrite-tasklist-prompt`: 60-70% speed improvements
  - `/cleanup-context`: 15-25% token reduction
- **Explore-Plan-Code-Test (EPCT) Workflow** documented by Anthropic
- **Sub-task with agents** keyword for parallel file operations
- **Claude Max Limitations** clarified - no headless mode with subscription
- **Memory-bank Pattern** popularized for complex projects
- *Source: GitHub repositories + NPM packages + Anthropic blog + Official docs*

## 2024

### December 2024
- **Hooks System** introduced - customize Claude Code behavior with shell commands
- **MCP (Model Context Protocol)** support - integrate with external tools
- **Plan Mode** (`shift+tab` twice) - enables thorough evaluation before execution
- **Think Keywords** - `think`, `think hard`, `think harder`, `ultrathink` for more computation
- **Double-tap Escape** - fork conversations by going back in history
- **`--dangerously-skip-permissions`** flag - bypass all permission checks
- *Source: Official docs + Community discoveries*

### November 2024
- Initial Claude Code release
- **Headless Mode** (`claude -p`) for non-interactive automation - API only
- `/compact` command for context summarization
- `-continue` flag to reload previous conversations
- **Directory-based Settings**: User, project, and local settings hierarchy
- *Source: Anthropic announcement + Community guide*

---

## Key Discoveries Timeline

### Performance Optimizations
- **99.7% improvement** via SharedPromptCache (Claude PM Framework)
- **60-70% speed gains** through parallel TodoWrite patterns
- **15-25% token reduction** with context cleanup strategies

### Multi-Agent Evolution
1. **Single Agent Era** (Nov 2024): Basic Claude Code
2. **Worktree Pattern** (Dec 2024): Manual parallel agents
3. **Orchestration Tools** (Jan 2025): Parallax, PM Framework
4. **Profile Systems** (Jan 2025): Axivo's persistent memory

### Cost Management Evolution
1. **Pay-per-use** (~$100/day for heavy users)
2. **Claude Max** ($200/month unlimited)
3. **Auto-switching** (Opus→Sonnet at thresholds)
4. **Cloud solutions** (Terragon for background agents)

---

*Entries are added as features are discovered and verified by the community*