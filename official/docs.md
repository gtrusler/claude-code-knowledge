# Claude Code Complete Documentation

This document contains the complete Claude Code documentation scraped from https://docs.anthropic.com/en/docs/claude-code/.

---

## Overview

### Get Started in 30 Seconds

Prerequisites: [Node.js 18 or newer](https://nodejs.org/en/download/)

```bash
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Navigate to your project
cd your-awesome-project

# Start coding with Claude
claude
```

### What Claude Code Does for You

- **Build features from descriptions**: Tell Claude what you want to build in plain English. It will make a plan, write the code, and ensure it works.
- **Debug and fix issues**: Describe a bug or paste an error message. Claude Code will analyze your codebase, identify the problem, and implement a fix.
- **Navigate any codebase**: Ask anything about your team's codebase and get a thoughtful answer. Claude Code maintains awareness of your entire project structure.
- **Automate tedious tasks**: Fix lint issues, resolve merge conflicts, and write release notes.

### Why Developers Love Claude Code

- **Works in your terminal**: Meets you where you already work, with the tools you already love.
- **Takes action**: Directly edits files, runs commands, and creates commits.
- **Unix philosophy**: Composable and scriptable. 
- **Enterprise-ready**: Offers enterprise-grade security, privacy, and compliance.

---

## Quickstart

### Before You Begin

Prerequisites:
- Terminal/command prompt
- Node.js 18+ installed
- A code project

### Installation

Install Claude Code globally:
```bash
npm install -g @anthropic-ai/claude-code
```

### Getting Started

#### Starting a Session

1. Navigate to project directory
2. Run `claude` command
3. Interact with Claude Code in the interactive prompt

#### Key Capabilities

- Understand project structure
- Analyze codebase
- Make code changes
- Use Git operations
- Fix bugs
- Add features

### Essential Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `claude` | Start interactive mode | `claude` |
| `claude "task"` | Run one-time task | `claude "fix build error"` |
| `claude -p "query"` | Run query and exit | `claude -p "explain function"` |
| `/clear` | Clear conversation history | `> /clear` |
| `exit` | Exit Claude Code | `> exit` |

### Pro Tips

- Be specific in requests
- Break complex tasks into steps
- Let Claude explore code first
- Use shortcuts like Tab and ↑

---

## Memory Management and CLAUDE.md

Claude Code offers memory management across different locations:

### Memory Types

1. **Project Memory** (`./CLAUDE.md`)
   - Team-shared instructions
   - Project architecture and coding standards

2. **User Memory** (`~/.claude/CLAUDE.md`)
   - Personal preferences across projects
   - Code styling and tooling shortcuts

3. **Project Memory (Local)** (Deprecated)
   - Previously used for project-specific personal preferences

### Key Features

#### CLAUDE.md Imports
- Can import additional files using `@path/to/import` syntax
- Supports relative and absolute paths
- Recursive imports allowed (max 5 hops)

#### Memory Lookup
- Reads memories recursively from current working directory
- Checks parent directories up to root
- Discovers nested CLAUDE.md files in subtrees

### Quick Memory Management

- Use `#` at the start of input to quickly add a memory
- Use `/memory` slash command to edit memory files
- Use `/init` to bootstrap a CLAUDE.md for your project

### Best Practices

- Be specific in memory instructions
- Use structured markdown
- Organize memories with headings
- Periodically review and update memories

---

## Common Workflows

The document provides comprehensive guidance for developers using Claude Code, covering workflows such as:

### Understanding New Codebases
- Getting quick overviews
- Finding relevant code
- Exploring project structure

### Efficient Bug Fixing
- Identifying error sources
- Getting fix recommendations
- Applying targeted solutions

### Code Refactoring
- Identifying legacy code
- Modernizing code patterns
- Maintaining backward compatibility

### Advanced Features
- Using specialized sub-agents
- Working with tests
- Creating pull requests
- Managing documentation
- Image analysis
- Extended thinking techniques

### Key Capabilities
- Conversational code exploration
- Automated code review
- Multi-branch development with Git worktrees
- Resuming previous conversations
- Customizable slash commands

---

## IDE Integrations

Claude Code works with any IDE that has a terminal. Key features include:

### Features
- Quick launch with keyboard shortcut
- Interactive diff viewing
- Automatic selection/context sharing
- File reference shortcuts
- Diagnostic error sharing

### Supported IDEs
- Visual Studio Code (and forks like Cursor, Windsurf, VSCodium)
- JetBrains IDEs (IntelliJ, PyCharm, Android Studio, WebStorm, PhpStorm, GoLand)

### Installation

#### VS Code
1. Open VS Code
2. Open integrated terminal
3. Run `claude` (auto-installs extension)

#### JetBrains IDEs
1. Find and install Claude Code plugin from marketplace
2. Restart IDE

### Usage
- Run `claude` from IDE's integrated terminal
- Use `/ide` command in external terminals to connect

### Configuration
1. Run `claude`
2. Enter `/config` command
3. Adjust preferences

### Troubleshooting
- Ensure correct CLI is available
- Check IDE plugin permissions
- Restart IDE completely

---

## Model Context Protocol (MCP)

Model Context Protocol (MCP) is an open protocol that enables Large Language Models (LLMs) to access external tools and data sources.

### Key Warning

> Use third party MCP servers at your own risk. Make sure you trust the MCP servers.

### Configuration Methods

#### Adding MCP Servers

1. **MCP stdio Server**
```bash
claude mcp add <name> <command> [args...]
```

2. **MCP SSE Server**
```bash
claude mcp add --transport sse <name> <url>
```

3. **MCP HTTP Server**
```bash
claude mcp add --transport http <name> <url>
```

#### Server Scopes

MCP servers can be configured at three levels:

- **Local Scope**: Project-specific, private configurations
- **Project Scope**: Shared team configurations via `.mcp.json`
- **User Scope**: Cross-project configurations

#### Authentication

MCP supports OAuth 2.0 authentication for remote servers:

1. Add a remote server
2. Use `/mcp` command to authenticate
3. Complete OAuth flow in browser

### Advanced Features

#### MCP Resources

- Reference resources using `@server:protocol://resource/path`
- Supports multiple resource references
- Automatically fetches and includes attachments

#### Slash Commands

MCP servers can expose prompts as slash commands:
- Discovered dynamically
- Format: `/mcp__servername__promptname`
- Supports arguments

### Example Use Cases

- Connect to PostgreSQL databases
- Integrate GitHub issue tracking
- Access external documentation

### Tips

- Carefully manage server permissions
- Use environment variable expansion
- Verify server trustworthiness

---

## GitHub Actions

Claude Code GitHub Actions brings AI-powered automation to GitHub workflows. With a simple `@claude` mention in any PR or issue, Claude can:

- Analyze code
- Create pull requests
- Implement features
- Fix bugs

> Claude Code GitHub Actions is currently in beta. Features and functionality may evolve as we refine the experience.

### Key Features

#### Why Use Claude Code GitHub Actions?

- **Instant PR Creation**: Describe needs, and Claude creates complete PRs
- **Automated Code Implementation**: Turn issues into working code
- **Follows Project Standards**: Respects `CLAUDE.md` guidelines
- **Simple Setup**: Get started in minutes
- **Secure by Default**: Code stays on GitHub runners

### Setup

#### Quick Setup

1. Open Claude in terminal
2. Run `/install-github-app`
3. Follow guided setup for GitHub app and secrets

#### Manual Setup

1. Install Claude GitHub app
2. Add `ANTHROPIC_API_KEY` to repository secrets
3. Copy workflow file to `.github/workflows/`

### Example Use Cases

#### Turn Issues into PRs

```
@claude implement this feature based on the issue description
```

#### Get Implementation Help

```
@claude how should I implement user authentication for this endpoint?
```

#### Fix Bugs Quickly

```
@claude fix the TypeError in the user dashboard component
```

### Best Practices

#### Security Considerations

- Never commit API keys directly to repository
- Use GitHub Secrets
- Limit action permissions
- Review Claude's suggestions before merging

#### Performance Optimization

- Use issue templates
- Keep `CLAUDE.md` concise
- Configure appropriate workflow timeouts

### Cost Considerations

#### GitHub Actions Costs
- Consumes GitHub Actions minutes
- Varies by task complexity

#### API Costs
- Token usage depends on prompt/response length
- Varies by task complexity

### Advanced Configuration

Supports configuration for:
- AWS Bedrock
- Google Vertex AI
- Direct Anthropic API

### Supported Integrations

- Claude Code SDK
- Sub agents
- GitHub Actions
- Model Context Protocol (MCP)

---

## Claude Code SDK

The Claude Code SDK enables running Claude Code as a subprocess, providing a way to build AI-powered coding assistants and tools that leverage Claude's capabilities.

The SDK is available for command line, TypeScript, and Python usage.

### Authentication

The Claude Code SDK supports multiple authentication methods:

#### Anthropic API Key

To use the Claude Code SDK directly with Anthropic's API:

1. Create an Anthropic API key in the [Anthropic Console](https://console.anthropic.com/)
2. Set the `ANTHROPIC_API_KEY` environment variable securely

#### Third-Party API Credentials

The SDK also supports:
- **Amazon Bedrock**: Set `CLAUDE_CODE_USE_BEDROCK=1` and configure AWS credentials
- **Google Vertex AI**: Set `CLAUDE_CODE_USE_VERTEX=1` and configure Google Cloud credentials

### Basic SDK Usage

#### Command Line Examples

```bash
# Run a single prompt and exit (print mode)
$ claude -p "Write a function to calculate Fibonacci numbers"

# Using a pipe to provide stdin
$ echo "Explain this code" | claude -p

# Output in JSON format with metadata
$ claude -p "Generate a hello world function" --output-format json

# Stream JSON output as it arrives
$ claude -p "Build a React component" --output-format stream-json
```

#### TypeScript SDK

```typescript
import { query, type SDKMessage } from "@anthropic-ai/claude-code";

const messages: SDKMessage[] = [];

for await (const message of query({
  prompt: "Write a haiku about foo.py",
  abortController: new AbortController(),
  options: {
    maxTurns: 3,
  },
})) {
  messages.push(message);
}

console.log(messages);
```

#### Python SDK

```python
import anyio
from claude_code_sdk import query, ClaudeCodeOptions, Message

async def main():
    messages: list[Message] = []
    
    async for message in query(
        prompt="Write a haiku about foo.py",
        options=ClaudeCodeOptions(max_turns=3),
    ):
        messages.append(message)
    
    print(messages)

anyio.run(main)
```

---

## Troubleshooting

### Common Installation Issues

#### Windows Installation Issues in WSL

For Windows Subsystem for Linux (WSL) installation problems:

- OS/platform detection issues:
  ```bash
  npm config set os linux
  npm install -g @anthropic-ai/claude-code --force --no-os-check
  ```

- Node not found errors: Ensure Node.js is installed via Linux package manager or `nvm`

#### Linux Installation Issues

When encountering permission errors during npm installation:

##### Recommended Solution: Local Installation

```bash
claude migrate-installer
```

This moves Claude Code to `~/.claude/local/` and sets up an alias.

##### Alternative Solution: User-Writable npm Prefix

```bash
mkdir -p ~/.npm-global
npm config set prefix ~/.npm-global
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
```

### Auto-Updater Issues

#### Handling Permission Errors

Options:
1. Migrate to local installation
2. Update manually with `claude update`
3. Fix npm permissions

#### Disabling Auto-Updates

```bash
# Via configuration
claude config set autoUpdates false --global

# Via environment variable
export DISABLE_AUTOUPDATER=1
```

### Permissions and Authentication

- Use `/permissions` to allow specific tools without repeated approvals
- For authentication issues, use `/logout` and restart

### Performance and Stability

Performance tips:
- Use `/compact` to reduce context size
- Close and restart between major tasks
- Add large build directories to `.gitignore`

### Getting More Help

- Use `/bug` to report problems
- Check GitHub repository
- Run `/doctor` to check installation health
- Ask Claude directly about capabilities

---

## Third-Party Integrations

### Enterprise Deployment Overview

Claude Code supports flexible deployment configurations across different providers and infrastructure:

#### Cloud Providers
1. **Amazon Bedrock**
   - AWS infrastructure
   - IAM-based authentication
   - AWS-native monitoring

2. **Google Vertex AI**
   - Google Cloud Platform deployment
   - Enterprise-grade security
   - Compliance features

#### Corporate Infrastructure
1. **Corporate Proxy**
   - Configure network routing
   - SSL/TLS requirements support

2. **LLM Gateway**
   - Centralized model access
   - Usage tracking
   - Budgeting and audit logging

### Configuration Approaches

#### Direct Provider Access
Best for organizations that:
- Want simplest setup
- Have existing AWS/GCP infrastructure
- Need provider-native monitoring

#### Corporate Proxy
Best for organizations that:
- Have existing proxy requirements
- Need traffic monitoring
- Must route traffic through specific network paths

#### LLM Gateway
Best for organizations that:
- Need cross-team usage tracking
- Want to dynamically switch models
- Require custom rate limiting
- Need centralized authentication

### Best Practices

1. Create comprehensive documentation (e.g., `CLAUDE.md`)
2. Develop "one-click" installation for Claude Code
3. Encourage gradual adoption through small tasks
4. Configure managed permissions
5. Use Model Context Protocol (MCP) for enhanced information

### Debugging Tips

- Use `claude /status` slash command
- Set `ANTHROPIC_LOG=debug` for detailed logging

---

## Amazon Bedrock

### Prerequisites

Before configuring Claude Code with Bedrock, ensure you have:

- An AWS account with Bedrock access enabled
- Access to desired Claude models (e.g., Claude Sonnet 4) in Bedrock
- AWS CLI installed and configured (optional)
- Appropriate IAM permissions

### Setup

#### 1. Enable Model Access

1. Navigate to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/)
2. Go to **Model access** in the left navigation
3. Request access to desired Claude models
4. Wait for approval (usually instant for most regions)

#### 2. Configure AWS Credentials

Claude Code supports multiple credential configuration methods:

##### Option A: AWS CLI Configuration
```bash
aws configure
```

##### Option B: Environment Variables (Access Key)
```bash
export AWS_ACCESS_KEY_ID=your-access-key-id
export AWS_SECRET_ACCESS_KEY=your-secret-access-key
export AWS_SESSION_TOKEN=your-session-token
```

##### Option C: Environment Variables (SSO Profile)
```bash
aws sso login --profile=<your-profile-name>
export AWS_PROFILE=your-profile-name
```

##### Option D: Bedrock API Keys
```bash
export AWS_BEARER_TOKEN_BEDROCK=your-bedrock-api-key
```

#### 3. Configure Claude Code

Set environment variables to enable Bedrock:

```bash
# Enable Bedrock integration
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1  # or your preferred region

# Optional: Override region for small/fast model
export ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION=us-west-2
```

#### 4. Model Configuration

Default Bedrock models:

| Model Type | Default Value |
|-----------|--------------|
| Primary model | `us.anthropic.claude-3-7-sonnet-20250219-v1:0` |
| Small/fast model | `us.anthropic.claude-3-5-haiku-20241022-v1:0` |

---

## Google Vertex AI

### Prerequisites

Before configuring Claude Code with Vertex AI, ensure you have:

- A Google Cloud Platform (GCP) account with billing enabled
- A GCP project with Vertex AI API enabled
- Access to desired Claude models (e.g., Claude Sonnet 4)
- Google Cloud SDK (`gcloud`) installed and configured
- Quota allocated in desired GCP region

> Vertex AI may not support the Claude Code default models on non-`us-east5` regions.

### Setup

#### 1. Enable Vertex AI API

```bash
# Set your project ID
gcloud config set project YOUR-PROJECT-ID

# Enable Vertex AI API
gcloud services enable aiplatform.googleapis.com
```

#### 2. Request Model Access

1. Navigate to the [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)
2. Search for "Claude" models
3. Request access to desired Claude models
4. Wait for approval (may take 24-48 hours)

#### 3. Configure GCP Credentials

Uses standard Google Cloud authentication.

#### 4. Configure Claude Code

Set environment variables:

```bash
# Enable Vertex AI integration
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=YOUR-PROJECT-ID

# Optional: Disable prompt caching
export DISABLE_PROMPT_CACHING=1
```

#### 5. Model Configuration

Default Vertex AI models:

| Model Type | Default Value |
|-----------|--------------|
| Primary model | `claude-sonnet-4@20250514` |
| Small/fast model | `claude-3-5-haiku@20241022` |

### IAM Configuration

Assign `roles/aiplatform.user` role with permissions:
- `aiplatform.endpoints.predict`
- `aiplatform.endpoints.computeTokens`

### Troubleshooting

- Check quotas in Cloud Console
- Verify region access
- Ensure model availability

---

## Corporate Proxy

Claude Code supports standard HTTP/HTTPS proxy configurations through environment variables, allowing organizations to route traffic through proxy servers for security, compliance, and monitoring.

### Basic Proxy Configuration

#### Environment Variables

Claude Code respects standard proxy environment variables:

```bash
# HTTPS proxy (recommended)
export HTTPS_PROXY=https://proxy.example.com:8080

# HTTP proxy (if HTTPS not available)
export HTTP_PROXY=http://proxy.example.com:8080
```

> Claude Code currently does not support the `NO_PROXY` environment variable. All traffic will be routed through the configured proxy.

> Claude Code does not support SOCKS proxies.

### Authentication

#### Basic Authentication

For proxies requiring authentication, include credentials in the proxy URL:

```bash
export HTTPS_PROXY=http://username:password@proxy.example.com:8080
```

> Avoid hardcoding passwords in scripts. Use environment variables or secure credential storage instead.

#### SSL Certificate Issues

For proxies using custom SSL certificates:

```bash
export SSL_CERT_FILE=/path/to/certificate-bundle.crt
export NODE_EXTRA_CA_CERTS=/path/to/certificate-bundle.crt
```

### Network Access Requirements

Claude Code requires access to these URLs:
- `api.anthropic.com` - Claude API endpoints
- `statsig.anthropic.com` - Telemetry and metrics
- `sentry.io` - Error reporting

Ensure these URLs are allowlisted in proxy configurations and firewall rules.

---

## LLM Gateway

LLM gateways provide a centralized proxy layer between Claude Code and model providers, offering:

- **Centralized authentication** - Single point for API key management
- **Usage tracking** - Monitor usage across teams and projects
- **Cost controls** - Implement budgets and rate limits
- **Audit logging** - Track all model interactions for compliance
- **Model routing** - Switch between providers without code changes

### LiteLLM Configuration

> LiteLLM is a third-party proxy service. Anthropic doesn't endorse, maintain, or audit LiteLLM's security or functionality.

#### Prerequisites

- Claude Code updated to the latest version
- LiteLLM Proxy Server deployed and accessible
- Access to Claude models through your chosen provider

#### Authentication Methods

##### Static API Key

```bash
# Set in environment
export ANTHROPIC_AUTH_TOKEN=sk-litellm-static-key
```

##### Dynamic API Key with Helper

1. Create an API key helper script
2. Configure Claude Code settings
3. Set token refresh interval

#### Unified Endpoint (Recommended)

```bash
export ANTHROPIC_BASE_URL=https://litellm-server:4000
```

#### Provider-Specific Pass-Through Endpoints

##### Anthropic API
```bash
export ANTHROPIC_BASE_URL=https://litellm-server:4000/anthropic
```

##### Amazon Bedrock
```bash
export ANTHROPIC_BEDROCK_BASE_URL=https://litellm-server:4000/bedrock
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1
export CLAUDE_CODE_USE_BEDROCK=1
```

##### Google Vertex AI
```bash
export ANTHROPIC_VERTEX_BASE_URL=https://litellm-server:4000/vertex_ai/v1
export ANTHROPIC_VERTEX_PROJECT_ID=your-gcp-project-id
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
```

---

## Development Containers

### Overview

The development container is a preconfigured environment designed for teams needing consistent and secure development setups. Key features include:

#### Key Features
- "Production-ready Node.js" built on Node.js 20
- "Security by design" with custom firewall
- Developer-friendly tools like git and ZSH
- Seamless VS Code integration
- Session persistence
- Cross-platform compatibility

#### Security Approach
- Precise network access control
- Default-deny policy for external network access
- Isolated development environment

### Getting Started

1. Install VS Code and Remote - Containers extension
2. Clone the Claude Code reference implementation
3. Open repository in VS Code
4. Click "Reopen in Container"

### Configuration Components

- `devcontainer.json`: Container settings and extensions
- `Dockerfile`: Container image definition
- `init-firewall.sh`: Network security rules

### Warning

> While the devcontainer provides substantial protections, no system is completely immune to all attacks.

#### Recommended Practices
- Only use with trusted repositories
- Monitor Claude's activities
- Maintain good security practices

### Use Cases

- Secure client project isolation
- Streamlined team onboarding
- Consistent CI/CD environments

---

## Identity and Access Management

### Authentication Methods

Claude Code supports three primary authentication methods:
1. Anthropic API via Anthropic Console
2. Amazon Bedrock
3. Google Vertex AI

#### Anthropic API Authentication

To set up Claude Code access via Anthropic API:

- Create or use an existing Anthropic Console account
- Add users through:
  - Bulk invite in Console
  - Set up Single Sign-On (SSO)

User roles:
- "Claude Code" role: Create Claude Code API keys
- "Developer" role: Create any API key type

User onboarding steps:
- Accept Console invite
- Check system requirements
- Install Claude Code
- Login with Console credentials

#### Cloud Provider Authentication

For Bedrock or Vertex:
- Follow provider-specific documentation
- Distribute environment variables and cloud credential instructions
- Users install Claude Code

### Access Control and Permissions

Claude Code offers fine-grained permissions to control agent actions.

#### Permission System

| Tool Type | Example | Approval Required | "Yes, don't ask again" Behavior |
|-----------|----------|-------------------|----------------------------------|
| Read-only | File reads, LS, Grep | No | N/A |
| Bash Commands | Shell execution | Yes | Permanently per project/command |
| File Modification | Edit/write files | Yes | Until session end |

#### Permission Modes

- `default`: Standard behavior, prompts for first tool use
- `acceptEdits`: Automatically accepts file edit permissions
- `plan`: Analysis mode, no modifications
- `bypassPermissions`: Skips all permission prompts

### Credential Management

- Stores credentials in macOS Keychain
- Supports authentication types:
  - Claude.ai credentials
  - Anthropic API credentials
  - Bedrock Auth
  - Vertex Auth
- Supports custom credential scripts
- Refreshes API keys every 5 minutes or on 401 response

---

## Security

### How We Approach Security

#### Security Foundation

Claude Code prioritizes code security, built on Anthropic's comprehensive security program. Key resources are available at the [Anthropic Trust Center](https://trust.anthropic.com).

#### Permission-Based Architecture

Claude Code uses strict read-only permissions by default. When additional actions are needed, it:
- Requests explicit permission
- Allows users to control action approvals
- Requires approval for `git` commands

#### Built-in Protections

To mitigate risks in agentic systems:
- **Folder access restriction**: Limited to the started folder and its subfolders
- **Prompt fatigue mitigation**: Supports allowlisting safe commands
- **Accept Edits mode**: Batch accept edits while maintaining permission prompts

#### User Responsibility

"Claude Code only has the permissions you grant it. You're responsible for reviewing proposed code and commands for safety before approval."

### Protect Against Prompt Injection

#### Core Protections
- **Permission system**: Sensitive operations require explicit approval
- **Context-aware analysis**: Detects potentially harmful instructions
- **Input sanitization**: Prevents command injection
- **Command blocklist**: Blocks risky web-fetching commands like `curl` and `wget`

#### Additional Safeguards
- Network request approval
- Isolated context windows
- Trust verification
- Command injection detection
- Fail-closed matching
- Natural language command descriptions
- Secure credential storage

**Best Practices**:
1. Review suggested commands
2. Avoid piping untrusted content
3. Verify changes to critical files
4. Use virtual machines for external interactions
5. Report suspicious behavior with `/bug`

> While these protections significantly reduce risk, no system is completely immune to all attacks.

### MCP Security

Claude Code allows configuring Model Context Protocol (MCP) servers. Users can:
- Configure allowed MCP servers
- Set permissions for MCP servers
- Write or use trusted MCP servers

### Security Best Practices

#### Working with Sensitive Code
- Review all changes
- Use project-specific permissions
- Consider devcontainers

---

## Monitoring with OpenTelemetry

### Key Features

Claude Code supports OpenTelemetry (OTel) for:
- Metrics collection
- Event tracking
- Observability

#### Quick Start Configuration

```bash
# Enable telemetry
export CLAUDE_CODE_ENABLE_TELEMETRY=1

# Choose exporters
export OTEL_METRICS_EXPORTER=otlp
export OTEL_LOGS_EXPORTER=otlp

# Configure endpoint
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

### Key Metrics Exported

- Session count
- Lines of code modified
- Pull requests created
- Git commits
- API usage cost
- Token consumption
- Active development time

### Configuration Options

Administrators can configure telemetry through:
- Environment variables
- Managed settings file
- Multi-team organization attributes

### Security Considerations

- Telemetry is opt-in
- Sensitive information is not logged
- User prompts are redacted by default

**Note**: OpenTelemetry support is currently in beta and subject to change.

---

## Manage Costs Effectively

### Key Cost Insights

Claude Code token consumption details:
- Average cost: "$6 per developer per day"
- 90% of users stay below $12 daily
- Team usage: ~$100-200/developer per month with Sonnet 4

### Tracking Costs

Ways to monitor expenses:
- Use `/cost` command for current session usage
- Anthropic Console users can:
  - Check historical usage
  - Set workspace spend limits

### Rate Limit Recommendations

Recommended Tokens Per Minute (TPM) by team size:

| Team Size | TPM per User |
|-----------|--------------|
| 1-5 users | 200k-300k |
| 5-20 users | 100k-150k |
| 20-50 users | 50k-75k |
| 50-100 users | 25k-35k |
| 100-500 users | 15k-20k |
| 500+ users | 10k-15k |

### Reducing Token Usage

Strategies to minimize costs:
- Use auto-compact feature
- Write specific queries
- Break down complex tasks
- Clear conversation history between tasks

### Background Token Usage

Minor token consumption from:
- Haiku generation
- Conversation summarization
- Command processing

Recommendation: "Start with a small pilot group to establish usage patterns before wider rollout."

---

## CLI Reference

### CLI Commands

| Command | Description | Example |
|---------|-------------|---------|
| `claude` | Start interactive REPL | `claude` |
| `claude "query"` | Start REPL with initial prompt | `claude "explain this project"` |
| `claude -p "query"` | Query via SDK, then exit | `claude -p "explain this function"` |
| `cat file \| claude -p "query"` | Process piped content | `cat logs.txt \| claude -p "explain"` |
| `claude -c` | Continue most recent conversation | `claude -c` |
| `claude -c -p "query"` | Continue via SDK | `claude -c -p "Check for type errors"` |
| `claude -r "<session-id>" "query"` | Resume session by ID | `claude -r "abc123" "Finish this PR"` |
| `claude update` | Update to latest version | `claude update` |
| `claude mcp` | Configure Model Context Protocol (MCP) servers | See MCP documentation |

### CLI Flags

| Flag | Description | Example |
|------|-------------|---------|
| `--add-dir` | Add additional working directories | `claude --add-dir ../apps ../lib` |
| `--allowedTools` | List of tools to allow without prompting | `"Bash(git log:*)" "Read"` |
| `--disallowedTools` | List of tools to disallow | `"Bash(git log:*)" "Edit"` |
| `--print`, `-p` | Print response without interactive mode | `claude -p "query"` |
| `--output-format` | Specify output format | `claude -p "query" --output-format json` |
| `--verbose` | Enable verbose logging | `claude --verbose` |
| `--model` | Set model for session | `claude --model claude-sonnet-4-20250514` |

---

## Interactive Mode

### Keyboard Shortcuts

#### General Controls

| Shortcut | Description | Context |
|----------|-------------|---------|
| `Ctrl+C` | Cancel current input or generation | Standard interrupt |
| `Ctrl+D` | Exit Claude Code session | EOF signal |
| `Ctrl+L` | Clear terminal screen | Keeps conversation history |
| Up/Down arrows | Navigate command history | Recall previous inputs |
| `Esc` + `Esc` | Edit previous message | Double-escape to modify |

#### Multiline Input

| Method | Shortcut | Context |
|--------|----------|---------|
| Quick escape | `\` + `Enter` | Works in all terminals |
| macOS default | `Option+Enter` | Default on macOS |
| Terminal setup | `Shift+Enter` | After `/terminal-setup` |
| Paste mode | Paste directly | For code blocks, logs |

#### Quick Commands

| Shortcut | Description | Notes |
|----------|-------------|-------|
| `#` at start | Memory shortcut - add to CLAUDE.md | Prompts for file selection |
| `/` at start | Slash command | See slash commands |

### Vim Mode

Enable vim-style editing with `/vim` command or configure permanently via `/config`.

#### Mode Switching

| Command | Action | From Mode |
|---------|--------|-----------|
| `Esc` | Enter NORMAL mode | INSERT |
| `i` | Insert before cursor | NORMAL |
| `I` | Insert at beginning of line | NORMAL |
| `a` | Insert after cursor | NORMAL |
| `A` | Insert at end of line | NORMAL |
| `o` | Open line below | NORMAL |
| `O` | Open line above | NORMAL |

#### Navigation (NORMAL mode)

| Command | Action |
|---------|--------|
| `h`/`j`/`k`/`l` | Move left/down/up/right |
| `w` | Next word |
| `e` | End of word |
| `b` | Beginning of word |

---

## Slash Commands

Control Claude's behavior during an interactive session with slash commands.

### Built-in Slash Commands

| Command | Purpose |
|---------|---------|
| `/add-dir` | Add additional working directories |
| `/agents` | Manage custom AI sub agents for specialized tasks |
| `/bug` | Report bugs (sends conversation to Anthropic) |
| `/clear` | Clear conversation history |
| `/compact [instructions]` | Compact conversation with optional focus instructions |
| `/config` | View/modify configuration |
| `/cost` | Show token usage statistics |
| `/doctor` | Checks the health of your Claude Code installation |
| `/help` | Get usage help |
| `/init` | Initialize project with CLAUDE.md guide |
| `/login` | Switch Anthropic accounts |
| `/logout` | Sign out from your Anthropic account |
| `/mcp` | Manage MCP server connections and OAuth authentication |
| `/memory` | Edit CLAUDE.md memory files |
| `/model` | Select or change the AI model |
| `/permissions` | View or update permissions |
| `/pr_comments` | View pull request comments |
| `/review` | Request code review |
| `/status` | View account and system statuses |
| `/terminal-setup` | Install Shift+Enter key binding for newlines (iTerm2 and VSCode only) |
| `/vim` | Enter vim mode for alternating insert and command modes |

### Custom Slash Commands

Custom slash commands allow you to define frequently-used prompts as Markdown files that Claude Code can execute. Commands are organized by scope (project-specific or personal) and support namespacing through directory structures.

#### Syntax

```
/<command-name> [arguments]
```

##### Parameters

| Parameter | Description |
|-----------|-------------|
| `<command-name>` | Name derived from the Markdown filename (without `.md` extension) |
| `[arguments]` | Optional arguments passed to the command |

#### Command Types

##### Project Commands

Commands stored in your repository and shared with your team.

---

## Settings

Claude Code offers comprehensive configuration options to customize its behavior. Users can configure settings through:

### Settings Files

Settings are managed through `settings.json` files at different levels:

1. **User settings**: `~/.claude/settings.json` (global)
2. **Project settings**:
   - `.claude/settings.json` (shared with team)
   - `.claude/settings.local.json` (personal)
3. **Enterprise managed policy settings** for system administrators

### Key Configuration Options

#### Available Settings

Key settings include:

- `apiKeyHelper`: Custom script to generate authentication values
- `cleanupPeriodDays`: Retention period for chat transcripts
- `env`: Environment variables for sessions
- `permissions`: Control tool usage rules
- `hooks`: Configure custom commands before/after tool executions
- `model`: Override default AI model

#### Permission Settings

- `allow`: Permitted tool usage rules
- `deny`: Restricted tool usage rules
- `additionalDirectories`: Extra working directories for Claude

### Environment Variables

Claude Code supports numerous environment variables, including:

- `ANTHROPIC_API_KEY`: API authentication
- `CLAUDE_CODE_USE_BEDROCK`: Enable Amazon Bedrock integration
- `CLAUDE_CODE_USE_VERTEX`: Enable Google Vertex AI integration
- `DISABLE_TELEMETRY`: Opt-out of usage tracking

### Tools Available to Claude

Claude has access to various tools:

| Tool | Description | Permission Required |
|------|-------------|---------------------|
| Bash | Execute shell commands | Yes |
| Edit | Make targeted file edits | Yes |
| Read | Read file contents | No |
| Write | Create/overwrite files | Yes |
| WebSearch | Perform web searches | Yes |

### Configuration Management

Manage configurations using:
- `claude config list`
- `claude config get <key>`
- `claude config set <key> <value>`

The documentation provides comprehensive guidance for configuring Claude Code across different environments and use cases.

---

## Hooks Reference

### Overview

Claude Code hooks are configuration-based scripts that can intercept and modify tool usage, prompt submission, and other events during Claude Code's operation.

### Configuration Locations

Hooks are configured in these settings files:
- `~/.claude/settings.json` - User settings
- `.claude/settings.json` - Project settings
- `.claude/settings.local.json` - Local project settings
- Enterprise managed policy settings

### Hook Structure

Basic hook configuration:

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here"
          }
        ]
      }
    ]
  }
}
```

#### Key Concepts

- **matcher**: Pattern to match tool names (case-sensitive)
  - Supports exact matches, regex, and wildcards
- **hooks**: Array of commands to execute
  - Currently supports only `"command"` type
  - Can specify optional timeout

### Hook Events

1. **PreToolUse**: Runs before tool execution
2. **PostToolUse**: Runs after successful tool completion
3. **Notification**: Triggered for tool permissions or idle states
4. **UserPromptSubmit**: Runs when a user submits a prompt
5. **Stop**: Runs when the main agent finishes
6. **SubagentStop**: Runs when a sub-agent finishes
7. **PreCompact**: Runs before context compaction

### Hook Input and Output

Hooks receive JSON input via stdin with session and event-specific details. They can return output through:
- Exit codes
- stdout/stderr
- Structured JSON output

#### Output Control Mechanisms

- Block/allow tool usage
- Add context
- Provide decision reasons
- Control agent continuation

### Security Considerations

**IMPORTANT WARNING**: 
> "USE AT YOUR OWN RISK": Claude Code hooks execute arbitrary shell commands automatically.

Best practices:
- Validate inputs
- Use absolute paths
- Quote shell variables
- Test thoroughly before deployment

---

*This documentation was compiled from the official Claude Code documentation at https://docs.anthropic.com/en/docs/claude-code/ on 2025-07-26.*