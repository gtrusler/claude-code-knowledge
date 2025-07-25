# Parallax Multi-Agent Orchestration
*Source: https://github.com/gifflet/parallax - January 2025*

Multi-agent development orchestration for Claude Code that executes multiple development tasks in parallel with automatic coordination and review.

## Key Features
- **Parallel Processing**: Run multiple Claude Code agents simultaneously in isolated Git worktrees
- **Task Discovery**: Connects to Task Master MCP to identify available tasks
- **Agent Types**:
  - Development Agent: Implements features
  - Review Agent: Validates against specifications
  - Correction Agent: Applies review feedback
  - Finalization Agent: Merges and completes tasks
- **Conflict Resolution**: Interactive merge conflict handling
- **Automatic Cleanup**: Removes worktrees and updates task status

## Installation
```bash
ccmd install https://github.com/gifflet/parallax
```

## Usage Examples
```bash
# Auto-select available tasks
/parallax

# Work on specific tasks
/parallax task_ids=2,3,7

# Limit parallel agents
/parallax max_agents=3

# Custom branch pattern
/parallax branch_pattern="dev/task-{id}"

# Strict review mode
/parallax review_mode=strict
```

## Options
- `max_agents`: Maximum parallel agents (default: 5)
- `branch_pattern`: Git branch naming (default: "feature/task-{id}")
- `review_mode`: Review strictness - "strict", "balanced", "lenient" (default: "balanced")
- `task_ids`: Specific task IDs to implement

## Why It's Valuable
- Enables true parallel development without context switching
- Maintains code quality through automated review cycles
- Respects existing project configuration and coding standards
- Solves the worktree management problem identified in best practices

# Axivo Claude Collaboration Platform
*Source: https://github.com/axivo/claude - January 2025*

Scalable collaboration platform for Claude Desktop with specialized profiles, persistent memory, and systematic methodologies.

## Core Innovation: Profile System with Memory

### Profile Types
- **Creative**: Innovation, design thinking, artistic collaboration
- **Developer**: Software development, code architecture, clean coding
- **Engineer**: Infrastructure, Kubernetes, production systems, debugging
- **Humanist**: Analysis, writing, philosophy, literary research
- **Researcher**: Academic methodology, data analysis, evidence evaluation

### Persistent Memory System
- **Conversation Logs**: Preserve collaborative work across sessions
- **Diary Entries**: Capture insights and reflection
- **Profile Configurations**: Maintain specialized competencies
- **Temporal Awareness**: Enables cumulative expertise building

### Implementation
```markdown
# Profile Instructions
On conversation start, Claude must:
1. Execute `memory:read_graph` to access complete memory system
2. Acknowledge temporal awareness
3. Load the ENGINEER profile methodology and competencies
```

## Setup
```bash
cd ./tools/memory
npm install js-yaml
npm init -y
node ./lib/core/PackageBuilder.js
npm run build
```

## Key Benefits
- **Institutional Memory**: Each session builds cumulative knowledge
- **Profile Specialization**: Domain-specific expertise and workflows
- **Temporal Awareness**: Claude maintains context across sessions
- **5-Layer Architecture**: Curated competencies, conversation logs, diary entries

## Why It's Revolutionary
Instead of stateless interactions, creates authentic partnership with perfect recall of all decisions and insights across sessions.

# Claude PM Framework (NPM Package)
*Source: https://www.npmjs.com/package/@bobmatnyc/claude-multiagent-pm - January 2025*

Lightweight, flexible multi-agent framework for orchestrating AI-driven development workflows with unlimited custom agent creation.

## Core Innovation: Custom Agent Creation

### Architecture
- **9 Core Agents**: Documentation, Ticketing, QA, Version Control, Research, Ops, Security, Engineer, Data Engineer
- **Unlimited Custom Agents**: Create project-specific agents for any domain
- **Agent Registry**: Dynamic discovery with hierarchical precedence
- **10 Concurrent Agents**: Run specialized agents simultaneously

### Custom Agent Creation
```markdown
# Custom Agent: Performance Optimization Specialist

## When to Use This Agent
- Database query optimization tasks
- Application performance bottlenecks
- Memory usage analysis and optimization

## Agent Capabilities
- **Primary Role**: Application and database performance optimization
- **Specializations**: ['performance', 'monitoring', 'database', 'optimization']
- **Tools**: Profiling tools, performance monitors, load testing frameworks
```

### Directory Structure
```
$PWD/.claude-pm/agents/
├── specialized/
│   ├── performance-agent.md
│   ├── architecture-agent.md
│   └── integration-agent.md
├── custom/
│   ├── project-manager-agent.md
│   └── business-analyst-agent.md
└── overrides/
    ├── documentation-agent.md  # Override system agent
    └── qa-agent.md            # Override system agent
```

## Key Features
- **Agent Training System**: Self-improving agents that learn from experience
- **Natural Language Routing**: 94.1% accuracy in agent selection
- **SharedPromptCache**: 99.7% performance improvement
- **Process Isolation**: Secure execution environment for each agent

## Installation
```bash
npm install -g @bobmatnyc/claude-multiagent-pm
cd your-project
claude-pm
```

## Why It's Different
- **User-Generated Agents**: Not limited to pre-defined agents
- **Dynamic Discovery**: Agents found via project → user → system precedence
- **Self-Improving**: Agents get smarter with usage
- **Lightweight**: Quick setup without enterprise overhead

# Centminmod's Claude Code Setup
*Source: https://github.com/centminmod/my-claude-code-setup - January 2025*

Comprehensive Claude Code starter settings with advanced slash commands and hook integrations.

## Notable Slash Commands

### /apply-thinking-to
Expert prompt engineering that applies Anthropic's extended thinking patterns:
- Transforms prompts using progressive reasoning structure
- Applies sequential analytical frameworks
- Includes constraint optimization and bias detection
- Usage: `/apply-thinking-to @/path/to/prompt-file.md`

### /convert-to-todowrite-tasklist-prompt
Converts complex prompts into efficient TodoWrite tasklist methods:
- Achieves 60-70% speed improvements through parallel processing
- Prevents context overflow through strategic file selection
- Usage: `/convert-to-todowrite-tasklist-prompt @/path/to/original-slash-command.md`

### /ccusage-daily
Comprehensive usage cost analysis:
- Generates executive summary with total costs
- Creates detailed tables showing daily costs and token usage
- Includes cache efficiency metrics
- Usage: `/ccusage-daily`

### /cleanup-context
Memory bank optimization specialist:
- Removes duplicate content and obsolete files
- Achieves 15-25% token reduction
- Implements archive strategies
- Usage: `/cleanup-context`

## Advanced Configuration Examples

### Settings.json Hierarchy
1. Enterprise policies
2. Command line arguments
3. Local project settings (`.claude/settings.local.json`)
4. Shared project settings (`.claude/settings.json`)
5. User settings (`~/.claude/settings.json`)

### Environment Variables
```bash
# Custom model configuration
ANTHROPIC_MODEL="custom-model-name"
ANTHROPIC_SMALL_FAST_MODEL="haiku-model"

# Performance tuning
BASH_DEFAULT_TIMEOUT_MS=30000
BASH_MAX_OUTPUT_LENGTH=1000000
CLAUDE_CODE_MAX_OUTPUT_TOKENS=8192

# Disable features
DISABLE_TELEMETRY=1
DISABLE_ERROR_REPORTING=1
DISABLE_NON_ESSENTIAL_MODEL_CALLS=1
```

### MCP Server Integration
```bash
# Add various MCP servers
claude mcp add gemini-cli /path/to/.venv/bin/python /path/to/mcp_server.py -s user
claude mcp add --transport sse cf-docs https://docs.mcp.cloudflare.com/sse -s user
claude mcp add --transport sse context7 https://mcp.context7.com/sse -s user
```

## Hooks System
STOP hook with macOS notifications:
- Uses Terminal-Notifier for desktop notifications
- Triggers when Claude Code finishes response
- Integrated with https://github.com/centminmod/terminal-notifier-setup

# Claude Code Spec Workflow
*Source: https://www.npmjs.com/package/@pimzino/claude-code-spec-workflow - January 2025*

Automated Kiro-style Spec workflow for Claude Code. Transforms feature ideas into complete implementations through a structured Requirements → Design → Tasks → Implementation process.

## Key Innovation: Structured Spec-Driven Development

### The Workflow
1. **Requirements Phase**: Generates user stories and acceptance criteria using EARS format
2. **Design Phase**: Creates technical architecture with Mermaid diagrams
3. **Tasks Phase**: Breaks design into atomic, test-driven coding tasks
4. **Implementation Phase**: Executes tasks systematically with validation

## Installation

### Quick Start (NPX)
```bash
# Run once in your project directory
npx @pimzino/claude-code-spec-workflow

# Test the setup
npx @pimzino/claude-code-spec-workflow test
```

### Global Installation
```bash
npm install -g @pimzino/claude-code-spec-workflow
claude-spec-setup
```

### Project Dependency
```bash
npm install --save-dev @pimzino/claude-code-spec-workflow
npx claude-spec-setup
```

## Created Structure
```
your-project/
├── .claude/
│   ├── commands/
│   │   ├── spec-create.md
│   │   ├── spec-requirements.md
│   │   ├── spec-design.md
│   │   ├── spec-tasks.md
│   │   ├── spec-execute.md
│   │   ├── spec-status.md
│   │   └── spec-list.md
│   ├── templates/
│   │   ├── requirements-template.md
│   │   ├── design-template.md
│   │   └── tasks-template.md
│   ├── specs/
│   │   └── (your specs will be created here)
│   └── spec-config.json
└── CLAUDE.md (created/updated)
```

## Slash Commands

After setup, use these commands in Claude Code:

```bash
# Create a new feature spec
/spec-create user-authentication "Secure login system"

# Generate requirements document
/spec-requirements

# Create design document
/spec-design

# Generate implementation tasks
/spec-tasks

# Execute specific tasks
/spec-execute 1

# Check status
/spec-status

# List all specs
/spec-list
```

## CLI Options
```bash
# Setup in specific directory
npx @pimzino/claude-code-spec-workflow --project /path/to/project

# Force overwrite existing files
npx @pimzino/claude-code-spec-workflow --force

# Skip confirmation prompts
npx @pimzino/claude-code-spec-workflow --yes
```

## Key Features
- **Auto-Detection**: Works with any project type (Node.js, Python, Java, etc.)
- **Safety First**: Preserves existing CLAUDE.md content
- **Beautiful CLI**: Progress indicators and helpful error messages
- **Comprehensive Templates**: Includes all necessary templates and configs
- **TDD Focus**: Emphasizes test-driven development in task generation

## Why It's Valuable
- **Structured Approach**: Forces systematic thinking through requirements before implementation
- **EARS Format**: Industry-standard requirements format (WHEN/IF/THEN)
- **Visual Design**: Mermaid diagrams for architecture visualization
- **Atomic Tasks**: Breaks work into manageable, testable chunks
- **Quality Gates**: Built-in validation against requirements

## Comparison with Other Tools
Unlike multi-agent tools that focus on parallel execution, this tool emphasizes:
- **Sequential Workflow**: Requirements → Design → Implementation
- **Documentation First**: All work starts with specs
- **Single Agent**: Works with standard Claude Code, no multi-agent complexity
- **Project Agnostic**: Works with any language or framework

## Best Use Cases
1. **New Features**: Start with clear requirements before coding
2. **Complex Systems**: Break down into manageable specs
3. **Team Projects**: Shared understanding through specs
4. **Legacy Refactoring**: Document current state before changes