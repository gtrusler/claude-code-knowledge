# Claude Code Official Documentation

*Last updated: 2025-07-16 06:07 UTC*
*Scraped 29 pages from docs.anthropic.com*

---

## Table of Contents

1. [Amazon Bedrock](#amazon-bedrock)
2. [Cli Reference](#cli-reference)
3. [Common Workflows](#common-workflows)
4. [Corporate Proxy](#corporate-proxy)
5. [Costs](#costs)
6. [Data Usage](#data-usage)
7. [Devcontainer](#devcontainer)
8. [Github Actions](#github-actions)
9. [Google Vertex Ai](#google-vertex-ai)
10. [Hooks](#hooks)
11. [Hooks Guide](#hooks-guide)
12. [Iam](#iam)
13. [Ide Integrations](#ide-integrations)
14. [Interactive Mode](#interactive-mode)
15. [Legal And Compliance](#legal-and-compliance)
16. [Llm Gateway](#llm-gateway)
17. [Mcp](#mcp)
18. [Memory](#memory)
19. [Monitoring Usage](#monitoring-usage)
20. [Overview](#overview)
21. [Quickstart](#quickstart)
22. [Sdk](#sdk)
23. [Security](#security)
24. [Settings](#settings)
25. [Setup](#setup)
26. [Slash Commands](#slash-commands)
27. [Terminal Config](#terminal-config)
28. [Third Party Integrations](#third-party-integrations)
29. [Troubleshooting](#troubleshooting)

---

## Amazon Bedrock

*Source: https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Deployment
Claude Code on Amazon Bedrock
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
## [​](#prerequisites) Prerequisites
Before configuring Claude Code with Bedrock, ensure you have:
* An AWS account with Bedrock access enabled
* Access to desired Claude models (e.g., Claude Sonnet 4) in Bedrock
* AWS CLI installed and configured (optional - only needed if you don’t have another mechanism for getting credentials)
* Appropriate IAM permissions
## [​](#setup) Setup
### [​](#1-enable-model-access) 1. Enable model access
First, ensure you have access to the required Claude models in your AWS account:
1. Navigate to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/)
2. Go to **Model access** in the left navigation
3. Request access to desired Claude models (e.g., Claude Sonnet 4)
4. Wait for approval (usually instant for most regions)
### [​](#2-configure-aws-credentials) 2. Configure AWS credentials
Claude Code uses the default AWS SDK credential chain. Set up your credentials using one of these methods:
**Option A: AWS CLI configuration**
```
aws configure
```
**Option B: Environment variables (access key)**
```
export AWS_ACCESS_KEY_ID=your-access-key-id
export AWS_SECRET_ACCESS_KEY=your-secret-access-key
export AWS_SESSION_TOKEN=your-session-token
```
**Option C: Environment variables (SSO profile)**
```
aws sso login --profile=<your-profile-name>
export AWS_PROFILE=your-profile-name
```
**Option D: Bedrock API keys**
```
export AWS_BEARER_TOKEN_BEDROCK=your-bedrock-api-key
```
Bedrock API keys provide a simpler authentication method without needing full AWS credentials. [Learn more about Bedrock API keys](https://aws.amazon.com/blogs/machine-learning/accelerate-ai-development-with-amazon-bedrock-api-keys/).
#### [​](#advanced-credential-configuration) Advanced credential configuration
Claude Code supports two configuration settings for dynamic AWS credential management:
##### `awsAuthRefresh`
This setting specifies a command for foreground authentication operations where output is visible to the user. It is typically used for SSO browser flows.
Example:
```
{
  "awsAuthRefresh": "aws sso login --profile myprofile"
}
```
##### `awsCredentialExport`
This setting specifies a command that outputs AWS credentials in JSON format to stdout. The output is not displayed to the user, but is used by Claude Code for subsequent Bedrock requests.
Required output format is JSON with the following properties:
```
{
  "Credentials": {
    "AccessKeyId": "value",
    "SecretAccessKey": "value",
    "SessionToken": "value"
  }
}
```
Example:
```
{
  "awsCredentialExport": "aws sts get-session-token --profile myprofile --output json"
}
```
These settings can be used to call scripts that invoke alternative identity systems.
### [​](#3-configure-claude-code) 3. Configure Claude Code
Set the following environment variables to enable Bedrock:
```
# Enable Bedrock integration
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1  # or your preferred region
# Optional: Override the region for the small/fast model (Haiku)
export ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION=us-west-2
```
When enabling Bedrock for Claude Code, keep the following in mind:
* `AWS_REGION` is a required environment variable. Claude Code does not read from the `.aws` config file for this setting.
* When using Bedrock, the `/login` and `/logout` commands are disabled since authentication is handled through AWS credentials.
* You can use settings files for environment variables like `AWS_PROFILE` that you don’t want to leak to other processes. See [Settings](/en/docs/claude-code/settings) for more information.
### [​](#4-model-configuration) 4. Model configuration
Claude Code uses these default models for Bedrock:
| Model type | Default value |
| --- | --- |
| Primary model | `us.anthropic.claude-3-7-sonnet-20250219-v1:0` |
| Small/fast model | `us.anthropic.claude-3-5-haiku-20241022-v1:0` |
To customize models, use one of these methods:
```
# Using inference profile ID
export ANTHROPIC_MODEL='us.anthropic.claude-opus-4-20250514-v1:0'
export ANTHROPIC_SMALL_FAST_MODEL='us.anthropic.claude-3-5-haiku-20241022-v1:0'
# Using application inference profile ARN
export ANTHROPIC_MODEL='arn:aws:bedrock:us-east-2:your-account-id:application-inference-profile/your-model-id'
# Optional: Disable prompt caching if needed
export DISABLE_PROMPT_CACHING=1
```
[Prompt caching](/en/docs/build-with-claude/prompt-caching) may not be available in all regions
## [​](#iam-configuration) IAM configuration
Create an IAM policy with the required permissions for Claude Code:
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ListInferenceProfiles"
      ],
      "Resource": [
        "arn:aws:bedrock:*:*:inference-profile/*",
        "arn:aws:bedrock:*:*:application-inference-profile/*"
      ]
    }
  ]
}
```
For more restrictive permissions, you can limit the Resource to specific inference profile ARNs.
For details, see [Bedrock IAM documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html).
We recommend creating a dedicated AWS account for Claude Code to simplify cost tracking and access control.
## [​](#troubleshooting) Troubleshooting
If you encounter region issues:
* Check model availability: `aws bedrock list-inference-profiles --region your-region`
* Switch to a supported region: `export AWS_REGION=us-east-1`
* Consider using inference profiles for cross-region access
If you receive an error “on-demand throughput isn’t supported”:
* Specify the model as an [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html) ID
## [​](#additional-resources) Additional resources
* [Bedrock documentation](https://docs.aws.amazon.com/bedrock/)
* [Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)
* [Bedrock inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)
* [Claude Code on Amazon Bedrock: Quick Setup Guide](https://community.aws/content/2tXkZKrZzlrlu0KfH8gST5Dkppq/claude-code-on-amazon-bedrock-quick-setup-guide)
Was this page helpful?
YesNo
[Overview](/en/docs/claude-code/third-party-integrations)[Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
On this page


---

## Cli Reference

*Source: https://docs.anthropic.com/en/docs/claude-code/cli-reference*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Reference
CLI reference
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
## [​](#cli-commands) CLI commands
| Command | Description | Example |
| --- | --- | --- |
| `claude` | Start interactive REPL | `claude` |
| `claude "query"` | Start REPL with initial prompt | `claude "explain this project"` |
| `claude -p "query"` | Query via SDK, then exit | `claude -p "explain this function"` |
| `cat file | claude -p "query"` | Process piped content | `cat logs.txt | claude -p "explain"` |
| `claude -c` | Continue most recent conversation | `claude -c` |
| `claude -c -p "query"` | Continue via SDK | `claude -c -p "Check for type errors"` |
| `claude -r "<session-id>" "query"` | Resume session by ID | `claude -r "abc123" "Finish this PR"` |
| `claude update` | Update to latest version | `claude update` |
| `claude mcp` | Configure Model Context Protocol (MCP) servers | See the [Claude Code MCP documentation](/en/docs/claude-code/mcp). |
## [​](#cli-flags) CLI flags
Customize Claude Code’s behavior with these command-line flags:
| Flag | Description | Example |
| --- | --- | --- |
| `--add-dir` | Add additional working directories for Claude to access (validates each path exists as a directory) | `claude --add-dir ../apps ../lib` |
| `--allowedTools` | A list of tools that should be allowed without prompting the user for permission, in addition to [settings.json files](/en/docs/claude-code/settings) | `"Bash(git log:*)" "Bash(git diff:*)" "Read"` |
| `--disallowedTools` | A list of tools that should be disallowed without prompting the user for permission, in addition to [settings.json files](/en/docs/claude-code/settings) | `"Bash(git log:*)" "Bash(git diff:*)" "Edit"` |
| `--print`, `-p` | Print response without interactive mode (see [SDK documentation](/en/docs/claude-code/sdk) for programmatic usage details) | `claude -p "query"` |
| `--output-format` | Specify output format for print mode (options: `text`, `json`, `stream-json`) | `claude -p "query" --output-format json` |
| `--input-format` | Specify input format for print mode (options: `text`, `stream-json`) | `claude -p --output-format json --input-format stream-json` |
| `--verbose` | Enable verbose logging, shows full turn-by-turn output (helpful for debugging in both print and interactive modes) | `claude --verbose` |
| `--max-turns` | Limit the number of agentic turns in non-interactive mode | `claude -p --max-turns 3 "query"` |
| `--model` | Sets the model for the current session with an alias for the latest model (`sonnet` or `opus`) or a model’s full name | `claude --model claude-sonnet-4-20250514` |
| `--permission-mode` | Begin in a specified [permission mode](iam#permission-modes) | `claude --permission-mode plan` |
| `--permission-prompt-tool` | Specify an MCP tool to handle permission prompts in non-interactive mode | `claude -p --permission-prompt-tool mcp_auth_tool "query"` |
| `--resume` | Resume a specific session by ID, or by choosing in interactive mode | `claude --resume abc123 "query"` |
| `--continue` | Load the most recent conversation in the current directory | `claude --continue` |
| `--dangerously-skip-permissions` | Skip permission prompts (use with caution) | `claude --dangerously-skip-permissions` |
The `--output-format json` flag is particularly useful for scripting and
automation, allowing you to parse Claude’s responses programmatically.
For detailed information about print mode (`-p`) including output formats,
streaming, verbose logging, and programmatic usage, see the
[SDK documentation](/en/docs/claude-code/sdk).
## [​](#see-also) See also
* [Interactive mode](/en/docs/claude-code/interactive-mode) - Shortcuts, input modes, and interactive features
* [Slash commands](/en/docs/claude-code/slash-commands) - Interactive session commands
* [Quickstart guide](/en/docs/claude-code/quickstart) - Getting started with Claude Code
* [Common workflows](/en/docs/claude-code/common-workflows) - Advanced workflows and patterns
* [Settings](/en/docs/claude-code/settings) - Configuration options
* [SDK documentation](/en/docs/claude-code/sdk) - Programmatic usage and integrations
Was this page helpful?
YesNo
[Memory management](/en/docs/claude-code/memory)[Interactive mode](/en/docs/claude-code/interactive-mode)
On this page


---

## Common Workflows

*Source: https://docs.anthropic.com/en/docs/claude-code/common-workflows*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Getting started
Common workflows
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
Each task in this document includes clear instructions, example commands, and best practices to help you get the most from Claude Code.
## [​](#understand-new-codebases) Understand new codebases
### [​](#get-a-quick-codebase-overview) Get a quick codebase overview
Suppose you’ve just joined a new project and need to understand its structure quickly.
1
Navigate to the project root directory
```
cd /path/to/project 
```
2
Start Claude Code
```
claude 
```
3
Ask for a high-level overview
```
> give me an overview of this codebase 
```
4
Dive deeper into specific components
```
> explain the main architecture patterns used here 
```
```
> what are the key data models?
```
```
> how is authentication handled?
```
Tips:
* Start with broad questions, then narrow down to specific areas
* Ask about coding conventions and patterns used in the project
* Request a glossary of project-specific terms
### [​](#find-relevant-code) Find relevant code
Suppose you need to locate code related to a specific feature or functionality.
1
Ask Claude to find relevant files
```
> find the files that handle user authentication 
```
2
Get context on how components interact
```
> how do these authentication files work together? 
```
3
Understand the execution flow
```
> trace the login process from front-end to database 
```
Tips:
* Be specific about what you’re looking for
* Use domain language from the project
## [​](#fix-bugs-efficiently) Fix bugs efficiently
Suppose you’ve encountered an error message and need to find and fix its source.
1
Share the error with Claude
```
> I'm seeing an error when I run npm test 
```
2
Ask for fix recommendations
```
> suggest a few ways to fix the @ts-ignore in user.ts 
```
3
Apply the fix
```
> update user.ts to add the null check you suggested 
```
Tips:
* Tell Claude the command to reproduce the issue and get a stack trace
* Mention any steps to reproduce the error
* Let Claude know if the error is intermittent or consistent
## [​](#refactor-code) Refactor code
Suppose you need to update old code to use modern patterns and practices.
1
Identify legacy code for refactoring
```
> find deprecated API usage in our codebase 
```
2
Get refactoring recommendations
```
> suggest how to refactor utils.js to use modern JavaScript features 
```
3
Apply the changes safely
```
> refactor utils.js to use ES2024 features while maintaining the same behavior 
```
4
Verify the refactoring
```
> run tests for the refactored code 
```
Tips:
* Ask Claude to explain the benefits of the modern approach
* Request that changes maintain backward compatibility when needed
* Do refactoring in small, testable increments
## [​](#work-with-tests) Work with tests
Suppose you need to add tests for uncovered code.
1
Identify untested code
```
> find functions in NotificationsService.swift that are not covered by tests 
```
2
Generate test scaffolding
```
> add tests for the notification service 
```
3
Add meaningful test cases
```
> add test cases for edge conditions in the notification service 
```
4
Run and verify tests
```
> run the new tests and fix any failures 
```
Tips:
* Ask for tests that cover edge cases and error conditions
* Request both unit and integration tests when appropriate
* Have Claude explain the testing strategy
## [​](#create-pull-requests) Create pull requests
Suppose you need to create a well-documented pull request for your changes.
1
Summarize your changes
```
> summarize the changes I've made to the authentication module 
```
2
Generate a PR with Claude
```
> create a pr 
```
3
Review and refine
```
> enhance the PR description with more context about the security improvements 
```
4
Add testing details
```
> add information about how these changes were tested 
```
Tips:
* Ask Claude directly to make a PR for you
* Review Claude’s generated PR before submitting
* Ask Claude to highlight potential risks or considerations
## [​](#handle-documentation) Handle documentation
Suppose you need to add or update documentation for your code.
1
Identify undocumented code
```
> find functions without proper JSDoc comments in the auth module 
```
2
Generate documentation
```
> add JSDoc comments to the undocumented functions in auth.js 
```
3
Review and enhance
```
> improve the generated documentation with more context and examples 
```
4
Verify documentation
```
> check if the documentation follows our project standards 
```
Tips:
* Specify the documentation style you want (JSDoc, docstrings, etc.)
* Ask for examples in the documentation
* Request documentation for public APIs, interfaces, and complex logic
## [​](#work-with-images) Work with images
Suppose you need to work with images in your codebase, and you want Claude’s help analyzing image content.
1
Add an image to the conversation
You can use any of these methods:
1. Drag and drop an image into the Claude Code window
2. Copy an image and paste it into the CLI with ctrl+v (Do not use cmd+v)
3. Provide an image path to Claude. E.g., “Analyze this image: /path/to/your/image.png”
2
Ask Claude to analyze the image
```
> What does this image show?
```
```
> Describe the UI elements in this screenshot
```
```
> Are there any problematic elements in this diagram?
```
3
Use images for context
```
> Here's a screenshot of the error. What's causing it?
```
```
> This is our current database schema. How should we modify it for the new feature?
```
4
Get code suggestions from visual content
```
> Generate CSS to match this design mockup
```
```
> What HTML structure would recreate this component?
```
Tips:
* Use images when text descriptions would be unclear or cumbersome
* Include screenshots of errors, UI designs, or diagrams for better context
* You can work with multiple images in a conversation
* Image analysis works with diagrams, screenshots, mockups, and more
## [​](#reference-files-and-directories) Reference files and directories
Use @ to quickly include files or directories without waiting for Claude to read them.
1
Reference a single file
```
> Explain the logic in @src/utils/auth.js
```
This includes the full content of the file in the conversation.
2
Reference a directory
```
> What's the structure of @src/components?
```
This provides a directory listing with file information.
3
Reference MCP resources
```
> Show me the data from @github:repos/owner/repo/issues
```
This fetches data from connected MCP servers using the format @server:resource. See [MCP resources](/en/docs/claude-code/mcp#use-mcp-resources) for details.
Tips:
* File paths can be relative or absolute
* @ file references add CLAUDE.md in the file’s directory and parent directories to context
* Directory references show file listings, not contents
* You can reference multiple files in a single message (e.g., “@file1.js and @file2.js”)
## [​](#use-extended-thinking) Use extended thinking
Suppose you’re working on complex architectural decisions, challenging bugs, or planning multi-step implementations that require deep reasoning.
1
Provide context and ask Claude to think
```
> I need to implement a new authentication system using OAuth2 for our API. Think deeply about the best approach for implementing this in our codebase. 
```
Claude will gather relevant information from your codebase and
use extended thinking, which will be visible in the interface.
2
Refine the thinking with follow-up prompts
```
> think about potential security vulnerabilities in this approach 
```
```
> think harder about edge cases we should handle 
```
Tips to get the most value out of extended thinking:
Extended thinking is most valuable for complex tasks such as:
* Planning complex architectural changes
* Debugging intricate issues
* Creating implementation plans for new features
* Understanding complex codebases
* Evaluating tradeoffs between different approaches
The way you prompt for thinking results in varying levels of thinking depth:
* “think” triggers basic extended thinking
* intensifying phrases such as “think more”, “think a lot”, “think harder”, or “think longer” triggers deeper thinking
For more extended thinking prompting tips, see [Extended thinking tips](/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).
Claude will display its thinking process as italic gray text above the
response.
## [​](#resume-previous-conversations) Resume previous conversations
Suppose you’ve been working on a task with Claude Code and need to continue where you left off in a later session.
Claude Code provides two options for resuming previous conversations:
* `--continue` to automatically continue the most recent conversation
* `--resume` to display a conversation picker
1
Continue the most recent conversation
```
claude --continue
```
This immediately resumes your most recent conversation without any prompts.
2
Continue in non-interactive mode
```
claude --continue --print "Continue with my task"
```
Use `--print` with `--continue` to resume the most recent conversation in non-interactive mode, perfect for scripts or automation.
3
Show conversation picker
```
claude --resume
```
This displays an interactive conversation selector showing:
* Conversation start time
* Initial prompt or conversation summary
* Message count
Use arrow keys to navigate and press Enter to select a conversation.
Tips:
* Conversation history is stored locally on your machine
* Use `--continue` for quick access to your most recent conversation
* Use `--resume` when you need to select a specific past conversation
* When resuming, you’ll see the entire conversation history before continuing
* The resumed conversation starts with the same model and configuration as the original
How it works:
1. **Conversation Storage**: All conversations are automatically saved locally with their full message history
2. **Message Deserialization**: When resuming, the entire message history is restored to maintain context
3. **Tool State**: Tool usage and results from the previous conversation are preserved
4. **Context Restoration**: The conversation resumes with all previous context intact
Examples:
```
# Continue most recent conversation
claude --continue
# Continue most recent conversation with a specific prompt
claude --continue --print "Show me our progress"
# Show conversation picker
claude --resume
# Continue most recent conversation in non-interactive mode
claude --continue --print "Run the tests again"
```
## [​](#run-parallel-claude-code-sessions-with-git-worktrees) Run parallel Claude Code sessions with Git worktrees
Suppose you need to work on multiple tasks simultaneously with complete code isolation between Claude Code instances.
1
Understand Git worktrees
Git worktrees allow you to check out multiple branches from the same
repository into separate directories. Each worktree has its own working
directory with isolated files, while sharing the same Git history. Learn
more in the [official Git worktree
documentation](https://git-scm.com/docs/git-worktree).
2
Create a new worktree
```
# Create a new worktree with a new branch 
git worktree add ../project-feature-a -b feature-a
# Or create a worktree with an existing branch
git worktree add ../project-bugfix bugfix-123
```
This creates a new directory with a separate working copy of your repository.
3
Run Claude Code in each worktree
```
# Navigate to your worktree 
cd ../project-feature-a
# Run Claude Code in this isolated environment
claude
```
4
Run Claude in another worktree
```
cd ../project-bugfix
claude
```
5
Manage your worktrees
```
# List all worktrees
git worktree list
# Remove a worktree when done
git worktree remove ../project-feature-a
```
Tips:
* Each worktree has its own independent file state, making it perfect for parallel Claude Code sessions
* Changes made in one worktree won’t affect others, preventing Claude instances from interfering with each other
* All worktrees share the same Git history and remote connections
* For long-running tasks, you can have Claude working in one worktree while you continue development in another
* Use descriptive directory names to easily identify which task each worktree is for
* Remember to initialize your development environment in each new worktree according to your project’s setup. Depending on your stack, this might include:
  + JavaScript projects: Running dependency installation (`npm install`, `yarn`)
  + Python projects: Setting up virtual environments or installing with package managers
  + Other languages: Following your project’s standard setup process
## [​](#use-claude-as-a-unix-style-utility) Use Claude as a unix-style utility
### [​](#add-claude-to-your-verification-process) Add Claude to your verification process
Suppose you want to use Claude Code as a linter or code reviewer.
**Add Claude to your build script:**
```
// package.json
{
    ...
    "scripts": {
        ...
        "lint:claude": "claude -p 'you are a linter. please look at the changes vs. main and report any issues related to typos. report the filename and line number on one line, and a description of the issue on the second line. do not return any other text.'"
    }
}
```
Tips:
* Use Claude for automated code review in your CI/CD pipeline
* Customize the prompt to check for specific issues relevant to your project
* Consider creating multiple scripts for different types of verification
### [​](#pipe-in%2C-pipe-out) Pipe in, pipe out
Suppose you want to pipe data into Claude, and get back data in a structured format.
**Pipe data through Claude:**
```
cat build-error.txt | claude -p 'concisely explain the root cause of this build error' > output.txt
```
Tips:
* Use pipes to integrate Claude into existing shell scripts
* Combine with other Unix tools for powerful workflows
* Consider using —output-format for structured output
### [​](#control-output-format) Control output format
Suppose you need Claude’s output in a specific format, especially when integrating Claude Code into scripts or other tools.
1
Use text format (default)
```
cat data.txt | claude -p 'summarize this data' --output-format text > summary.txt
```
This outputs just Claude’s plain text response (default behavior).
2
Use JSON format
```
cat code.py | claude -p 'analyze this code for bugs' --output-format json > analysis.json
```
This outputs a JSON array of messages with metadata including cost and duration.
3
Use streaming JSON format
```
cat log.txt | claude -p 'parse this log file for errors' --output-format stream-json
```
This outputs a series of JSON objects in real-time as Claude processes the request. Each message is a valid JSON object, but the entire output is not valid JSON if concatenated.
Tips:
* Use `--output-format text` for simple integrations where you just need Claude’s response
* Use `--output-format json` when you need the full conversation log
* Use `--output-format stream-json` for real-time output of each conversation turn
## [​](#create-custom-slash-commands) Create custom slash commands
Claude Code supports custom slash commands that you can create to quickly execute specific prompts or tasks.
For more details, see the [Slash commands](/en/docs/claude-code/slash-commands) reference page.
### [​](#create-project-specific-commands) Create project-specific commands
Suppose you want to create reusable slash commands for your project that all team members can use.
1
Create a commands directory in your project
```
mkdir -p .claude/commands
```
2
Create a Markdown file for each command
```
echo "Analyze the performance of this code and suggest three specific optimizations:" > .claude/commands/optimize.md 
```
3
Use your custom command in Claude Code
```
> /optimize 
```
Tips:
* Command names are derived from the filename (e.g., `optimize.md` becomes `/optimize`)
* You can organize commands in subdirectories (e.g., `.claude/commands/frontend/component.md` creates `/component` with “(project:frontend)” shown in the description)
* Project commands are available to everyone who clones the repository
* The Markdown file content becomes the prompt sent to Claude when the command is invoked
### [​](#add-command-arguments-with-%24arguments) Add command arguments with $ARGUMENTS
Suppose you want to create flexible slash commands that can accept additional input from users.
1
Create a command file with the $ARGUMENTS placeholder
```
echo "Find and fix issue #$ARGUMENTS. Follow these steps: 1.
Understand the issue described in the ticket 2. Locate the relevant code in
our codebase 3. Implement a solution that addresses the root cause 4. Add
appropriate tests 5. Prepare a concise PR description" >
.claude/commands/fix-issue.md 
```
2
Use the command with an issue number
In your Claude session, use the command with arguments.
```
> /fix-issue 123 
```
This will replace $ARGUMENTS with “123” in the prompt.
Tips:
* The $ARGUMENTS placeholder is replaced with any text that follows the command
* You can position $ARGUMENTS anywhere in your command template
* Other useful applications: generating test cases for specific functions, creating documentation for components, reviewing code in particular files, or translating content to specified languages
### [​](#create-personal-slash-commands) Create personal slash commands
Suppose you want to create personal slash commands that work across all your projects.
1
Create a commands directory in your home folder
```
mkdir -p ~/.claude/commands 
```
2
Create a Markdown file for each command
```
echo "Review this code for security vulnerabilities, focusing on:" >
~/.claude/commands/security-review.md 
```
3
Use your personal custom command
```
> /security-review 
```
Tips:
* Personal commands show “(user)” in their description when listed with `/help`
* Personal commands are only available to you and not shared with your team
* Personal commands work across all your projects
* You can use these for consistent workflows across different codebases
## [​](#next-steps) Next steps
[## Claude Code reference implementation
Clone our development container reference implementation.](https://github.com/anthropics/claude-code/tree/main/.devcontainer)
Was this page helpful?
YesNo
[Quickstart](/en/docs/claude-code/quickstart)[Claude Code SDK](/en/docs/claude-code/sdk)
On this page


---

## Corporate Proxy

*Source: https://docs.anthropic.com/en/docs/claude-code/corporate-proxy*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Deployment
Corporate proxy configuration
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
Claude Code supports standard HTTP/HTTPS proxy configurations through environment variables. This allows you to route all Claude Code traffic through your organization’s proxy servers for security, compliance, and monitoring purposes.
## [​](#basic-proxy-configuration) Basic proxy configuration
### [​](#environment-variables) Environment variables
Claude Code respects standard proxy environment variables:
```
# HTTPS proxy (recommended)
export HTTPS_PROXY=https://proxy.example.com:8080
# HTTP proxy (if HTTPS not available)
export HTTP_PROXY=http://proxy.example.com:8080
```
Claude Code currently does not support the `NO_PROXY` environment variable. All traffic will be routed through the configured proxy.
Claude Code does not support SOCKS proxies.
## [​](#authentication) Authentication
### [​](#basic-authentication) Basic authentication
If your proxy requires basic authentication, include credentials in the proxy URL:
```
export HTTPS_PROXY=http://username:password@proxy.example.com:8080
```
Avoid hardcoding passwords in scripts. Use environment variables or secure credential storage instead.
For proxies requiring advanced authentication (NTLM, Kerberos, etc.), consider using an LLM Gateway service that supports your authentication method.
### [​](#ssl-certificate-issues) SSL certificate issues
If your proxy uses custom SSL certificates, you may encounter certificate errors.
Ensure that you set the correct certificate bundle path:
```
export SSL_CERT_FILE=/path/to/certificate-bundle.crt
export NODE_EXTRA_CA_CERTS=/path/to/certificate-bundle.crt
```
## [​](#network-access-requirements) Network access requirements
Claude Code requires access to the following URLs:
* `api.anthropic.com` - Claude API endpoints
* `statsig.anthropic.com` - Telemetry and metrics
* `sentry.io` - Error reporting
Ensure these URLs are allowlisted in your proxy configuration and firewall rules. This is especially important when using Claude Code in containerized or restricted network environments.
## [​](#additional-resources) Additional resources
* [Claude Code settings](/en/docs/claude-code/settings)
* [Environment variables reference](/en/docs/claude-code/settings#environment-variables)
* [Troubleshooting guide](/en/docs/claude-code/troubleshooting)
Was this page helpful?
YesNo
[Google Vertex AI](/en/docs/claude-code/google-vertex-ai)[LLM gateway](/en/docs/claude-code/llm-gateway)
On this page


---

## Costs

*Source: https://docs.anthropic.com/en/docs/claude-code/costs*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Administration
Manage costs effectively
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
Claude Code consumes tokens for each interaction. The average cost is $6 per developer per day, with daily costs remaining below $12 for 90% of users.
For team usage, Claude Code charges by API token consumption. On average, Claude Code costs ~$50-60/developer per month with Sonnet 4 though there is large variance depending on how many instances users are running and whether they’re using it in automation.
## [​](#track-your-costs) Track your costs
* Use `/cost` to see current session usage
* **Anthropic Console users**:
  + Check [historical usage](https://support.anthropic.com/en/articles/9534590-cost-and-usage-reporting-in-console) in the Anthropic Console (requires Admin or Billing role)
  + Set [workspace spend limits](https://support.anthropic.com/en/articles/9796807-creating-and-managing-workspaces) for the Claude Code workspace (requires Admin role)
* **Pro and Max plan users**: Usage is included in your subscription
## [​](#managing-costs-for-teams) Managing costs for teams
When using Anthropic API, you can limit the total Claude Code workspace spend. To configure, [follow these instructions](https://support.anthropic.com/en/articles/9796807-creating-and-managing-workspaces). Admins can view cost and usage reporting by [following these instructions](https://support.anthropic.com/en/articles/9534590-cost-and-usage-reporting-in-console).
On Bedrock and Vertex, Claude Code does not send metrics from your cloud. In order to get cost metrics, several large enterprises reported using [LiteLLM](/en/docs/claude-code/bedrock-vertex-proxies#litellm), which is an open-source tool that helps companies [track spend by key](https://docs.litellm.ai/docs/proxy/virtual_keys#tracking-spend). This project is unaffiliated with Anthropic and we have not audited its security.
## [​](#reduce-token-usage) Reduce token usage
* **Compact conversations:**
  + Claude uses auto-compact by default when context exceeds 95% capacity
  + Toggle auto-compact: Run `/config` and navigate to “Auto-compact enabled”
  + Use `/compact` manually when context gets large
  + Add custom instructions: `/compact Focus on code samples and API usage`
  + Customize compaction by adding to CLAUDE.md:
    ```
    # Summary instructions
    When you are using compact, please focus on test output and code changes
    ```
* **Write specific queries:** Avoid vague requests that trigger unnecessary scanning
* **Break down complex tasks:** Split large tasks into focused interactions
* **Clear history between tasks:** Use `/clear` to reset context
Costs can vary significantly based on:
* Size of codebase being analyzed
* Complexity of queries
* Number of files being searched or modified
* Length of conversation history
* Frequency of compacting conversations
* Background processes (haiku generation, conversation summarization)
## [​](#background-token-usage) Background token usage
Claude Code uses tokens for some background functionality even when idle:
* **Haiku generation**: Small creative messages that appear while you type (approximately 1 cent per day)
* **Conversation summarization**: Background jobs that summarize previous conversations for the `claude --resume` feature
* **Command processing**: Some commands like `/cost` may generate requests to check status
These background processes consume a small amount of tokens (typically under $0.04 per session) even without active interaction.
For team deployments, we recommend starting with a small pilot group to
establish usage patterns before wider rollout.
Was this page helpful?
YesNo
[Monitoring](/en/docs/claude-code/monitoring-usage)[Settings](/en/docs/claude-code/settings)
On this page


---

## Data Usage

*Source: https://docs.anthropic.com/en/docs/claude-code/data-usage*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Resources
Data usage
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
## [​](#data-policies) Data policies
### [​](#data-training-policy) Data training policy
By default, Anthropic does not train generative models using code or prompts that are sent to Claude Code.
We aim to be fully transparent about how we use your data. We may use feedback to improve our products and services, but we will not train generative models using your feedback from Claude Code.
### [​](#development-partner-program) Development Partner Program
If you explicitly opt in to methods to provide us with materials to train on, such as via the [Development Partner Program](https://support.anthropic.com/en/articles/11174108-about-the-development-partner-program), we may use those materials provided to train our models. An organization admin can expressly opt-in to the Development Partner Program for their organization. Note that this program is available only for Anthropic first-party API, and not for Bedrock or Vertex users.
### [​](#feedback-transcripts) Feedback transcripts
If you choose to send us feedback about Claude Code, such as transcripts of your usage, Anthropic may use that feedback to debug related issues and improve Claude Code’s functionality (e.g., to reduce the risk of similar bugs occurring in the future). We will not train generative models using this feedback. Given their potentially sensitive nature, we store user feedback transcripts for only 30 days.
### [​](#data-retention) Data retention
You can use an API key from a zero data retention organization. When doing so, Claude Code will not retain your chat transcripts on our servers. Users’ local Claude Code clients may store sessions locally for up to 30 days so that users can resume them. This behavior is configurable.
### [​](#privacy-safeguards) Privacy safeguards
We have implemented several safeguards to protect your data, including:
* Limited retention periods for sensitive information
* Restricted access to user session data
* Clear policies against using feedback for model training
For full details, please review our [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and [Privacy Policy](https://www.anthropic.com/legal/privacy).
## [​](#data-flow-and-dependencies) Data flow and dependencies
Claude Code is installed from [NPM](https://www.npmjs.com/package/@anthropic-ai/claude-code). Claude Code runs locally. In order to interact with the LLM, Claude Code sends data over the network. This data includes all user prompts and model outputs. The data is encrypted in transit via TLS and is not encrypted at rest. Claude Code is compatible with most popular VPNs and LLM proxies.
Claude Code is built on Anthropic’s APIs. For details regarding our API’s security controls, including our API logging procedures, please refer to compliance artifacts offered in the [Anthropic Trust Center](https://trust.anthropic.com).
## [​](#telemetry-services) Telemetry services
Claude Code connects from users’ machines to the Statsig service to log operational metrics such as latency, reliability, and usage patterns. This logging does not include any code or file paths. Data is encrypted in transit using TLS and at rest using 256-bit AES encryption. Read more in the [Statsig security documentation](https://www.statsig.com/trust/security). To opt out of Statsig telemetry, set the `DISABLE_TELEMETRY` environment variable.
Claude Code connects from users’ machines to Sentry for operational error logging. The data is encrypted in transit using TLS and at rest using 256-bit AES encryption. Read more in the [Sentry security documentation](https://sentry.io/security/). To opt out of error logging, set the `DISABLE_ERROR_REPORTING` environment variable.
When users run the `/bug` command, a copy of their full conversation history including code is sent to Anthropic. The data is encrypted in transit and at rest. Optionally, a Github issue is created in our public repository. To opt out of bug reporting, set the `DISABLE_BUG_COMMAND` environment variable.
## [​](#default-behaviors-by-api-provider) Default behaviors by API provider
By default, we disable all non-essential traffic (including error reporting, telemetry, and bug reporting functionality) when using Bedrock or Vertex. You can also opt out of all of these at once by setting the `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` environment variable. Here are the full default behaviors:
| Service | Anthropic API | Vertex API | Bedrock API |
| --- | --- | --- | --- |
| **Statsig (Metrics)** | Default on.`DISABLE_TELEMETRY=1` to disable. | Default off.`CLAUDE_CODE_USE_VERTEX` must be 1. | Default off.`CLAUDE_CODE_USE_BEDROCK` must be 1. |
| **Sentry (Errors)** | Default on.`DISABLE_ERROR_REPORTING=1` to disable. | Default off.`CLAUDE_CODE_USE_VERTEX` must be 1. | Default off.`CLAUDE_CODE_USE_BEDROCK` must be 1. |
| **Anthropic API (`/bug` reports)** | Default on.`DISABLE_BUG_COMMAND=1` to disable. | Default off.`CLAUDE_CODE_USE_VERTEX` must be 1. | Default off.`CLAUDE_CODE_USE_BEDROCK` must be 1. |
All environment variables can be checked into `settings.json` ([read more](/en/docs/claude-code/settings)).
Was this page helpful?
YesNo
[Hooks reference](/en/docs/claude-code/hooks)[Legal and compliance](/en/docs/claude-code/legal-and-compliance)
On this page


---

## Devcontainer

*Source: https://docs.anthropic.com/en/docs/claude-code/devcontainer*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Deployment
Development containers
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
The preconfigured [devcontainer setup](https://code.visualstudio.com/docs/devcontainers/containers) works seamlessly with VS Code’s Remote - Containers extension and similar tools.
The container’s enhanced security measures (isolation and firewall rules) allow you to run `claude --dangerously-skip-permissions` to bypass permission prompts for unattended operation.
We’ve included a [reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer) that you can customize for your needs.
While the devcontainer provides substantial protections, no system is completely immune to all attacks.
When executed with `--dangerously-skip-permissions`, devcontainers do not prevent a malicious project from exfiltrating anything accessible in the devcontainer including Claude Code credentials.
We recommend only using devcontainers when developing with trusted repositories.
Always maintain good security practices and monitor Claude’s activities.
## [​](#key-features) Key features
* **Production-ready Node.js**: Built on Node.js 20 with essential development dependencies
* **Security by design**: Custom firewall restricting network access to only necessary services
* **Developer-friendly tools**: Includes git, ZSH with productivity enhancements, fzf, and more
* **Seamless VS Code integration**: Pre-configured extensions and optimized settings
* **Session persistence**: Preserves command history and configurations between container restarts
* **Works everywhere**: Compatible with macOS, Windows, and Linux development environments
## [​](#getting-started-in-4-steps) Getting started in 4 steps
1. Install VS Code and the Remote - Containers extension
2. Clone the [Claude Code reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer) repository
3. Open the repository in VS Code
4. When prompted, click “Reopen in Container” (or use Command Palette: Cmd+Shift+P → “Remote-Containers: Reopen in Container”)
## [​](#configuration-breakdown) Configuration breakdown
The devcontainer setup consists of three primary components:
* [**devcontainer.json**](https://github.com/anthropics/claude-code/blob/main/.devcontainer/devcontainer.json): Controls container settings, extensions, and volume mounts
* [**Dockerfile**](https://github.com/anthropics/claude-code/blob/main/.devcontainer/Dockerfile): Defines the container image and installed tools
* [**init-firewall.sh**](https://github.com/anthropics/claude-code/blob/main/.devcontainer/init-firewall.sh): Establishes network security rules
## [​](#security-features) Security features
The container implements a multi-layered security approach with its firewall configuration:
* **Precise access control**: Restricts outbound connections to whitelisted domains only (npm registry, GitHub, Anthropic API, etc.)
* **Allowed outbound connections**: The firewall permits outbound DNS and SSH connections
* **Default-deny policy**: Blocks all other external network access
* **Startup verification**: Validates firewall rules when the container initializes
* **Isolation**: Creates a secure development environment separated from your main system
## [​](#customization-options) Customization options
The devcontainer configuration is designed to be adaptable to your needs:
* Add or remove VS Code extensions based on your workflow
* Modify resource allocations for different hardware environments
* Adjust network access permissions
* Customize shell configurations and developer tooling
## [​](#example-use-cases) Example use cases
### [​](#secure-client-work) Secure client work
Use devcontainers to isolate different client projects, ensuring code and credentials never mix between environments.
### [​](#team-onboarding) Team onboarding
New team members can get a fully configured development environment in minutes, with all necessary tools and settings pre-installed.
### [​](#consistent-ci%2Fcd-environments) Consistent CI/CD environments
Mirror your devcontainer configuration in CI/CD pipelines to ensure development and production environments match.
## [​](#related-resources) Related resources
* [VS Code devcontainers documentation](https://code.visualstudio.com/docs/devcontainers/containers)
* [Claude Code security best practices](/en/docs/claude-code/security)
* [Corporate proxy configuration](/en/docs/claude-code/corporate-proxy)
Was this page helpful?
YesNo
[LLM gateway](/en/docs/claude-code/llm-gateway)[Advanced installation](/en/docs/claude-code/setup)
On this page


---

## Github Actions

*Source: https://docs.anthropic.com/en/docs/claude-code/github-actions*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Build with Claude Code
Claude Code GitHub Actions
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
Claude Code GitHub Actions brings AI-powered automation to your GitHub workflow. With a simple `@claude` mention in any PR or issue, Claude can analyze your code, create pull requests, implement features, and fix bugs - all while following your project’s standards.
Claude Code GitHub Actions is currently in beta. Features and functionality may evolve as we refine the experience.
Claude Code GitHub Actions is built on top of the [Claude Code SDK](/en/docs/claude-code/sdk), which enables programmatic integration of Claude Code into your applications. You can use the SDK to build custom automation workflows beyond GitHub Actions.
## [​](#why-use-claude-code-github-actions%3F) Why use Claude Code GitHub Actions?
* **Instant PR creation**: Describe what you need, and Claude creates a complete PR with all necessary changes
* **Automated code implementation**: Turn issues into working code with a single command
* **Follows your standards**: Claude respects your `CLAUDE.md` guidelines and existing code patterns
* **Simple setup**: Get started in minutes with our installer and API key
* **Secure by default**: Your code stays on Github’s runners
## [​](#what-can-claude-do%3F) What can Claude do?
Claude Code provides powerful GitHub Actions that transform how you work with code:
### [​](#claude-code-action) Claude Code Action
This GitHub Action allows you to run Claude Code within your GitHub Actions workflows. You can use this to build any custom workflow on top of Claude Code.
[View repository →](https://github.com/anthropics/claude-code-action)
### [​](#claude-code-action-base) Claude Code Action (Base)
The foundation for building custom GitHub workflows with Claude. This extensible framework gives you full access to Claude’s capabilities for creating tailored automation.
[View repository →](https://github.com/anthropics/claude-code-base-action)
## [​](#setup) Setup
## [​](#quick-setup) Quick setup
The easiest way to set up this action is through Claude Code in the terminal. Just open claude and run `/install-github-app`.
This command will guide you through setting up the GitHub app and required secrets.
* You must be a repository admin to install the GitHub app and add secrets
* This quickstart method is only available for direct Anthropic API users. If you’re using AWS Bedrock or Google Vertex AI, please see the [Using with AWS Bedrock & Google Vertex AI](/_sites/docs.anthropic.com/en/docs/claude-code/github-actions#using-with-aws-bedrock-%26-google-vertex-ai) section.
## [​](#manual-setup) Manual setup
If the `/install-github-app` command fails or you prefer manual setup, please follow these manual setup instructions:
1. **Install the Claude GitHub app** to your repository: <https://github.com/apps/claude>
2. **Add ANTHROPIC\_API\_KEY** to your repository secrets ([Learn how to use secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions))
3. **Copy the workflow file** from [examples/claude.yml](https://github.com/anthropics/claude-code-action/blob/main/examples/claude.yml) into your repository’s `.github/workflows/`
After completing either the quickstart or manual setup, test the action by tagging `@claude` in an issue or PR comment!
## [​](#example-use-cases) Example use cases
Claude Code GitHub Actions can help you with a variety of tasks. For complete working examples, see the [examples directory](https://github.com/anthropics/claude-code-action/tree/main/examples).
### [​](#turn-issues-into-prs) Turn issues into PRs
In an issue comment:
```
@claude implement this feature based on the issue description
```
Claude will analyze the issue, write the code, and create a PR for review.
### [​](#get-implementation-help) Get implementation help
In a PR comment:
```
@claude how should I implement user authentication for this endpoint?
```
Claude will analyze your code and provide specific implementation guidance.
### [​](#fix-bugs-quickly) Fix bugs quickly
In an issue:
```
@claude fix the TypeError in the user dashboard component
```
Claude will locate the bug, implement a fix, and create a PR.
## [​](#best-practices) Best practices
### [​](#claude-md-configuration) CLAUDE.md configuration
Create a `CLAUDE.md` file in your repository root to define code style guidelines, review criteria, project-specific rules, and preferred patterns. This file guides Claude’s understanding of your project standards.
### [​](#security-considerations) Security considerations
Never commit API keys directly to your repository!
Always use GitHub Secrets for API keys:
* Add your API key as a repository secret named `ANTHROPIC_API_KEY`
* Reference it in workflows: `anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}`
* Limit action permissions to only what’s necessary
* Review Claude’s suggestions before merging
Always use GitHub Secrets (e.g., `${{ secrets.ANTHROPIC_API_KEY }}`) rather than hardcoding API keys directly in your workflow files.
### [​](#optimizing-performance) Optimizing performance
Use issue templates to provide context, keep your `CLAUDE.md` concise and focused, and configure appropriate timeouts for your workflows.
### [​](#ci-costs) CI costs
When using Claude Code GitHub Actions, be aware of the associated costs:
**GitHub Actions costs:**
* Claude Code runs on GitHub-hosted runners, which consume your GitHub Actions minutes
* See [GitHub’s billing documentation](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions) for detailed pricing and minute limits
**API costs:**
* Each Claude interaction consumes API tokens based on the length of prompts and responses
* Token usage varies by task complexity and codebase size
* See [Claude’s pricing page](https://www.anthropic.com/api) for current token rates
**Cost optimization tips:**
* Use specific `@claude` commands to reduce unnecessary API calls
* Configure appropriate `max_turns` limits to prevent excessive iterations
* Set reasonable `timeout_minutes` to avoid runaway workflows
* Consider using GitHub’s concurrency controls to limit parallel runs
## [​](#configuration-examples) Configuration examples
For ready-to-use workflow configurations for different use cases, including:
* Basic workflow setup for issue and PR comments
* Automated code reviews on pull requests
* Custom implementations for specific needs
Visit the [examples directory](https://github.com/anthropics/claude-code-action/tree/main/examples) in the Claude Code Action repository.
The examples repository includes complete, tested workflows that you can copy directly into your `.github/workflows/` directory.
## [​](#using-with-aws-bedrock-%26-google-vertex-ai) Using with AWS Bedrock & Google Vertex AI
For enterprise environments, you can use Claude Code GitHub Actions with your own cloud infrastructure. This approach gives you control over data residency and billing while maintaining the same functionality.
### [​](#prerequisites) Prerequisites
Before setting up Claude Code GitHub Actions with cloud providers, you need:
#### [​](#for-google-cloud-vertex-ai%3A) For Google Cloud Vertex AI:
1. A Google Cloud Project with Vertex AI enabled
2. Workload Identity Federation configured for GitHub Actions
3. A service account with the required permissions
4. A GitHub App (recommended) or use the default GITHUB\_TOKEN
#### [​](#for-aws-bedrock%3A) For AWS Bedrock:
1. An AWS account with Amazon Bedrock enabled
2. GitHub OIDC Identity Provider configured in AWS
3. An IAM role with Bedrock permissions
4. A GitHub App (recommended) or use the default GITHUB\_TOKEN
1
Create a custom GitHub App (Recommended for 3P Providers)
For best control and security when using 3P providers like Vertex AI or Bedrock, we recommend creating your own GitHub App:
1. Go to <https://github.com/settings/apps/new>
2. Fill in the basic information:
   * **GitHub App name**: Choose a unique name (e.g., “YourOrg Claude Assistant”)
   * **Homepage URL**: Your organization’s website or the repository URL
3. Configure the app settings:
   * **Webhooks**: Uncheck “Active” (not needed for this integration)
4. Set the required permissions:
   * **Repository permissions**:
     + Contents: Read & Write
     + Issues: Read & Write
     + Pull requests: Read & Write
5. Click “Create GitHub App”
6. After creation, click “Generate a private key” and save the downloaded `.pem` file
7. Note your App ID from the app settings page
8. Install the app to your repository:
   * From your app’s settings page, click “Install App” in the left sidebar
   * Select your account or organization
   * Choose “Only select repositories” and select the specific repository
   * Click “Install”
9. Add the private key as a secret to your repository:
   * Go to your repository’s Settings → Secrets and variables → Actions
   * Create a new secret named `APP_PRIVATE_KEY` with the contents of the `.pem` file
10. Add the App ID as a secret:
* Create a new secret named `APP_ID` with your GitHub App’s ID
This app will be used with the [actions/create-github-app-token](https://github.com/actions/create-github-app-token) action to generate authentication tokens in your workflows.
**Alternative for Anthropic API or if you don’t want to setup your own Github app**: Use the official Anthropic app:
1. Install from: <https://github.com/apps/claude>
2. No additional configuration needed for authentication
2
Configure cloud provider authentication
Choose your cloud provider and set up secure authentication:
AWS Bedrock
**Configure AWS to allow GitHub Actions to authenticate securely without storing credentials.**
> **Security Note**: Use repository-specific configurations and grant only the minimum required permissions.
**Required Setup**:
1. **Enable Amazon Bedrock**:
   * Request access to Claude models in Amazon Bedrock
   * For cross-region models, request access in all required regions
2. **Set up GitHub OIDC Identity Provider**:
   * Provider URL: `https://token.actions.githubusercontent.com`
   * Audience: `sts.amazonaws.com`
3. **Create IAM Role for GitHub Actions**:
   * Trusted entity type: Web identity
   * Identity provider: `token.actions.githubusercontent.com`
   * Permissions: `AmazonBedrockFullAccess` policy
   * Configure trust policy for your specific repository
**Required Values**:
After setup, you’ll need:
* **AWS\_ROLE\_TO\_ASSUME**: The ARN of the IAM role you created
OIDC is more secure than using static AWS access keys because credentials are temporary and automatically rotated.
See [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) for detailed OIDC setup instructions.
Google Vertex AI
**Configure Google Cloud to allow GitHub Actions to authenticate securely without storing credentials.**
> **Security Note**: Use repository-specific configurations and grant only the minimum required permissions.
**Required Setup**:
1. **Enable APIs** in your Google Cloud project:
   * IAM Credentials API
   * Security Token Service (STS) API
   * Vertex AI API
2. **Create Workload Identity Federation resources**:
   * Create a Workload Identity Pool
   * Add a GitHub OIDC provider with:
     + Issuer: `https://token.actions.githubusercontent.com`
     + Attribute mappings for repository and owner
     + **Security recommendation**: Use repository-specific attribute conditions
3. **Create a Service Account**:
   * Grant only `Vertex AI User` role
   * **Security recommendation**: Create a dedicated service account per repository
4. **Configure IAM bindings**:
   * Allow the Workload Identity Pool to impersonate the service account
   * **Security recommendation**: Use repository-specific principal sets
**Required Values**:
After setup, you’ll need:
* **GCP\_WORKLOAD\_IDENTITY\_PROVIDER**: The full provider resource name
* **GCP\_SERVICE\_ACCOUNT**: The service account email address
Workload Identity Federation eliminates the need for downloadable service account keys, improving security.
For detailed setup instructions, consult the [Google Cloud Workload Identity Federation documentation](https://cloud.google.com/iam/docs/workload-identity-federation).
3
Add Required Secrets
Add the following secrets to your repository (Settings → Secrets and variables → Actions):
#### [​](#for-anthropic-api-direct-%3A) For Anthropic API (Direct):
1. **For API Authentication**:
   * `ANTHROPIC_API_KEY`: Your Anthropic API key from [console.anthropic.com](https://console.anthropic.com)
2. **For GitHub App (if using your own app)**:
   * `APP_ID`: Your GitHub App’s ID
   * `APP_PRIVATE_KEY`: The private key (.pem) content
#### [​](#for-google-cloud-vertex-ai) For Google Cloud Vertex AI
1. **For GCP Authentication**:
   * `GCP_WORKLOAD_IDENTITY_PROVIDER`
   * `GCP_SERVICE_ACCOUNT`
2. **For GitHub App (if using your own app)**:
   * `APP_ID`: Your GitHub App’s ID
   * `APP_PRIVATE_KEY`: The private key (.pem) content
#### [​](#for-aws-bedrock) For AWS Bedrock
1. **For AWS Authentication**:
   * `AWS_ROLE_TO_ASSUME`
2. **For GitHub App (if using your own app)**:
   * `APP_ID`: Your GitHub App’s ID
   * `APP_PRIVATE_KEY`: The private key (.pem) content
4
Create workflow files
Create GitHub Actions workflow files that integrate with your cloud provider. The examples below show complete configurations for both AWS Bedrock and Google Vertex AI:
AWS Bedrock workflow
**Prerequisites:**
* AWS Bedrock access enabled with Claude model permissions
* GitHub configured as an OIDC identity provider in AWS
* IAM role with Bedrock permissions that trusts GitHub Actions
**Required GitHub secrets:**
| Secret Name | Description |
| --- | --- |
| `AWS_ROLE_TO_ASSUME` | ARN of the IAM role for Bedrock access |
| `APP_ID` | Your GitHub App ID (from app settings) |
| `APP_PRIVATE_KEY` | The private key you generated for your GitHub App |
```
name: Claude PR Action 
permissions:
  contents: write
  pull-requests: write
  issues: write
  id-token: write 
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
  issues:
    types: [opened, assigned]
jobs:
  claude-pr:
    if: |
      (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude')) ||
      (github.event_name == 'pull_request_review_comment' && contains(github.event.comment.body, '@claude')) ||
      (github.event_name == 'issues' && contains(github.event.issue.body, '@claude'))
    runs-on: ubuntu-latest
    env:
      AWS_REGION: us-west-2
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Generate GitHub App token
        id: app-token
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.APP_ID }}
          private-key: ${{ secrets.APP_PRIVATE_KEY }}
      - name: Configure AWS Credentials (OIDC)
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_TO_ASSUME }}
          aws-region: us-west-2
      - uses: ./.github/actions/claude-pr-action
        with:
          trigger_phrase: "@claude"
          timeout_minutes: "60"
          github_token: ${{ steps.app-token.outputs.token }}
          use_bedrock: "true"
          model: "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
```
The model ID format for Bedrock includes the region prefix (e.g., `us.anthropic.claude...`) and version suffix.
Google Vertex AI workflow
**Prerequisites:**
* Vertex AI API enabled in your GCP project
* Workload Identity Federation configured for GitHub
* Service account with Vertex AI permissions
**Required GitHub secrets:**
| Secret Name | Description |
| --- | --- |
| `GCP_WORKLOAD_IDENTITY_PROVIDER` | Workload identity provider resource name |
| `GCP_SERVICE_ACCOUNT` | Service account email with Vertex AI access |
| `APP_ID` | Your GitHub App ID (from app settings) |
| `APP_PRIVATE_KEY` | The private key you generated for your GitHub App |
```
name: Claude PR Action
permissions:
  contents: write
  pull-requests: write
  issues: write
  id-token: write  
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
  issues:
    types: [opened, assigned]
jobs:
  claude-pr:
    if: |
      (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude')) ||
      (github.event_name == 'pull_request_review_comment' && contains(github.event.comment.body, '@claude')) ||
      (github.event_name == 'issues' && contains(github.event.issue.body, '@claude'))
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Generate GitHub App token
        id: app-token
        uses: actions/create-github-app-token@v2
        with:
          app-id: ${{ secrets.APP_ID }}
          private-key: ${{ secrets.APP_PRIVATE_KEY }}
      - name: Authenticate to Google Cloud
        id: auth
        uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
          service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}
      - uses: ./.github/actions/claude-pr-action
        with:
          trigger_phrase: "@claude"
          timeout_minutes: "60"
          github_token: ${{ steps.app-token.outputs.token }}
          use_vertex: "true"
          model: "claude-3-7-sonnet@20250219"
        env:
          ANTHROPIC_VERTEX_PROJECT_ID: ${{ steps.auth.outputs.project_id }}
          CLOUD_ML_REGION: us-east5
          VERTEX_REGION_CLAUDE_3_7_SONNET: us-east5
```
The project ID is automatically retrieved from the Google Cloud authentication step, so you don’t need to hardcode it.
## [​](#troubleshooting) Troubleshooting
### [​](#claude-not-responding-to-%40claude-commands) Claude not responding to @claude commands
Verify the GitHub App is installed correctly, check that workflows are enabled, ensure API key is set in repository secrets, and confirm the comment contains `@claude` (not `/claude`).
### [​](#ci-not-running-on-claude%E2%80%99s-commits) CI not running on Claude’s commits
Ensure you’re using the GitHub App or custom app (not Actions user), check workflow triggers include the necessary events, and verify app permissions include CI triggers.
### [​](#authentication-errors) Authentication errors
Confirm API key is valid and has sufficient permissions. For Bedrock/Vertex, check credentials configuration and ensure secrets are named correctly in workflows.
## [​](#advanced-configuration) Advanced configuration
### [​](#action-parameters) Action parameters
The Claude Code Action supports these key parameters:
| Parameter | Description | Required |
| --- | --- | --- |
| `prompt` | The prompt to send to Claude | Yes\* |
| `prompt_file` | Path to file containing prompt | Yes\* |
| `anthropic_api_key` | Anthropic API key | Yes\*\* |
| `max_turns` | Maximum conversation turns | No |
| `timeout_minutes` | Execution timeout | No |
\*Either `prompt` or `prompt_file` required
\*\*Required for direct Anthropic API, not for Bedrock/Vertex
### [​](#alternative-integration-methods) Alternative integration methods
While the `/install-github-app` command is the recommended approach, you can also:
* **Custom GitHub App**: For organizations needing branded usernames or custom authentication flows. Create your own GitHub App with required permissions (contents, issues, pull requests) and use the actions/create-github-app-token action to generate tokens in your workflows.
* **Manual GitHub Actions**: Direct workflow configuration for maximum flexibility
* **MCP Configuration**: Dynamic loading of Model Context Protocol servers
See the [Claude Code Action repository](https://github.com/anthropics/claude-code-action) for detailed documentation.
### [​](#customizing-claude%E2%80%99s-behavior) Customizing Claude’s behavior
You can configure Claude’s behavior in two ways:
1. **CLAUDE.md**: Define coding standards, review criteria, and project-specific rules in a `CLAUDE.md` file at the root of your repository. Claude will follow these guidelines when creating PRs and responding to requests. Check out our [Memory documentation](/en/docs/claude-code/memory) for more details.
2. **Custom prompts**: Use the `prompt` parameter in the workflow file to provide workflow-specific instructions. This allows you to customize Claude’s behavior for different workflows or tasks.
Claude will follow these guidelines when creating PRs and responding to requests.
Was this page helpful?
YesNo
[Claude Code hooks](/en/docs/claude-code/hooks-guide)[Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
On this page


---

## Google Vertex Ai

*Source: https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Deployment
Claude Code on Google Vertex AI
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
## [​](#prerequisites) Prerequisites
Before configuring Claude Code with Vertex AI, ensure you have:
* A Google Cloud Platform (GCP) account with billing enabled
* A GCP project with Vertex AI API enabled
* Access to desired Claude models (e.g., Claude Sonnet 4)
* Google Cloud SDK (`gcloud`) installed and configured
* Quota allocated in desired GCP region
Vertex AI may not support the Claude Code default models on non-`us-east5` regions. Ensure you are using `us-east5` and have quota allocated, or switch to supported models.
## [​](#setup) Setup
### [​](#1-enable-vertex-ai-api) 1. Enable Vertex AI API
Enable the Vertex AI API in your GCP project:
```
# Set your project ID
gcloud config set project YOUR-PROJECT-ID
# Enable Vertex AI API
gcloud services enable aiplatform.googleapis.com
```
### [​](#2-request-model-access) 2. Request model access
Request access to Claude models in Vertex AI:
1. Navigate to the [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)
2. Search for “Claude” models
3. Request access to desired Claude models (e.g., Claude Sonnet 4)
4. Wait for approval (may take 24-48 hours)
### [​](#3-configure-gcp-credentials) 3. Configure GCP credentials
Claude Code uses standard Google Cloud authentication.
For more information, see [Google Cloud authentication documentation](https://cloud.google.com/docs/authentication).
### [​](#4-configure-claude-code) 4. Configure Claude Code
Set the following environment variables:
```
# Enable Vertex AI integration
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=YOUR-PROJECT-ID
# Optional: Disable prompt caching if needed
export DISABLE_PROMPT_CACHING=1
# Optional: Override regions for specific models
export VERTEX_REGION_CLAUDE_3_5_HAIKU=us-central1
export VERTEX_REGION_CLAUDE_3_5_SONNET=us-east5
export VERTEX_REGION_CLAUDE_3_7_SONNET=us-east5
export VERTEX_REGION_CLAUDE_4_0_OPUS=europe-west4
export VERTEX_REGION_CLAUDE_4_0_SONNET=us-east5
```
[Prompt caching](/en/docs/build-with-claude/prompt-caching) is automatically supported when you specify the `cache_control` ephemeral flag. To disable it, set `DISABLE_PROMPT_CACHING=1`. For heightened rate limits, contact Google Cloud support.
When using Vertex AI, the `/login` and `/logout` commands are disabled since authentication is handled through Google Cloud credentials.
### [​](#5-model-configuration) 5. Model configuration
Claude Code uses these default models for Vertex AI:
| Model type | Default value |
| --- | --- |
| Primary model | `claude-sonnet-4@20250514` |
| Small/fast model | `claude-3-5-haiku@20241022` |
To customize models:
```
export ANTHROPIC_MODEL='claude-opus-4@20250514'
export ANTHROPIC_SMALL_FAST_MODEL='claude-3-5-haiku@20241022'
```
## [​](#iam-configuration) IAM configuration
Assign the required IAM permissions:
The `roles/aiplatform.user` role includes the required permissions:
* `aiplatform.endpoints.predict` - Required for model invocation
* `aiplatform.endpoints.computeTokens` - Required for token counting
For more restrictive permissions, create a custom role with only the permissions above.
For details, see [Vertex IAM documentation](https://cloud.google.com/vertex-ai/docs/general/access-control).
We recommend creating a dedicated GCP project for Claude Code to simplify cost tracking and access control.
## [​](#troubleshooting) Troubleshooting
If you encounter quota issues:
* Check current quotas or request quota increase through [Cloud Console](https://cloud.google.com/docs/quotas/view-manage)
If you encounter “model not found” 404 errors:
* Verify you have access to the specified region
* Confirm model is Enabled in [Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)
If you encounter 429 errors:
* Ensure the primary model and small/fast model are supported in your selected region
## [​](#additional-resources) Additional resources
* [Vertex AI documentation](https://cloud.google.com/vertex-ai/docs)
* [Vertex AI pricing](https://cloud.google.com/vertex-ai/pricing)
* [Vertex AI quotas and limits](https://cloud.google.com/vertex-ai/docs/quotas)
Was this page helpful?
YesNo
[Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)[Corporate proxy](/en/docs/claude-code/corporate-proxy)
On this page


---

## Hooks

*Source: https://docs.anthropic.com/en/docs/claude-code/hooks*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Reference
Hooks reference
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
For a quickstart guide with examples, see [Get started with Claude Code hooks](/en/docs/claude-code/hooks-guide).
## [​](#configuration) Configuration
Claude Code hooks are configured in your
[settings files](/en/docs/claude-code/settings):
* `~/.claude/settings.json` - User settings
* `.claude/settings.json` - Project settings
* `.claude/settings.local.json` - Local project settings (not committed)
* Enterprise managed policy settings
### [​](#structure) Structure
Hooks are organized by matchers, where each matcher can have multiple hooks:
```
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
* **matcher**: Pattern to match tool names, case-sensitive (only applicable for
  `PreToolUse` and `PostToolUse`)
  + Simple strings match exactly: `Write` matches only the Write tool
  + Supports regex: `Edit|Write` or `Notebook.*`
  + If omitted or empty string, hooks run for all matching events
* **hooks**: Array of commands to execute when the pattern matches
  + `type`: Currently only `"command"` is supported
  + `command`: The bash command to execute
  + `timeout`: (Optional) How long a command should run, in seconds, before
    canceling that specific command.
`"matcher": "*"` is invalid. Instead, omit “matcher” or use `"matcher": ""`.
## [​](#hook-events) Hook Events
### [​](#pretooluse) PreToolUse
Runs after Claude creates tool parameters and before processing the tool call.
**Common matchers:**
* `Task` - Agent tasks
* `Bash` - Shell commands
* `Glob` - File pattern matching
* `Grep` - Content search
* `Read` - File reading
* `Edit`, `MultiEdit` - File editing
* `Write` - File writing
* `WebFetch`, `WebSearch` - Web operations
### [​](#posttooluse) PostToolUse
Runs immediately after a tool completes successfully.
Recognizes the same matcher values as PreToolUse.
### [​](#notification) Notification
Runs when Claude Code sends notifications. Notifications are sent when:
1. Claude needs your permission to use a tool. Example: “Claude needs your permission to use Bash”
2. The prompt input has been idle for at least 60 seconds. “Claude is waiting for your input”
### [​](#stop) Stop
Runs when the main Claude Code agent has finished responding. Does not run if the stoppage occurred due to a user interrupt.
### [​](#subagentstop) SubagentStop
Runs when a Claude Code subagent (Task tool call) has finished responding.
### [​](#precompact) PreCompact
Runs before Claude Code is about to run a compact operation.
**Matchers:**
* `manual` - Invoked from `/compact`
* `auto` - Invoked from auto-compact (due to full context window)
## [​](#hook-input) Hook Input
Hooks receive JSON data via stdin containing session information and
event-specific data:
```
{
  // Common fields
  session_id: string
  transcript_path: string  // Path to conversation JSON
  // Event-specific fields
  hook_event_name: string
  ...
}
```
### [​](#pretooluse-input) PreToolUse Input
The exact schema for `tool_input` depends on the tool.
```
{
  "session_id": "abc123",
  "transcript_path": "~/.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.txt",
    "content": "file content"
  }
}
```
### [​](#posttooluse-input) PostToolUse Input
The exact schema for `tool_input` and `tool_response` depends on the tool.
```
{
  "session_id": "abc123",
  "transcript_path": "~/.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "hook_event_name": "PostToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.txt",
    "content": "file content"
  },
  "tool_response": {
    "filePath": "/path/to/file.txt",
    "success": true
  }
}
```
### [​](#notification-input) Notification Input
```
{
  "session_id": "abc123",
  "transcript_path": "~/.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "hook_event_name": "Notification",
  "message": "Task completed successfully"
}
```
### [​](#stop-and-subagentstop-input) Stop and SubagentStop Input
`stop_hook_active` is true when Claude Code is already continuing as a result of
a stop hook. Check this value or process the transcript to prevent Claude Code
from running indefinitely.
```
{
  "session_id": "abc123",
  "transcript_path": "~/.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "hook_event_name": "Stop",
  "stop_hook_active": true
}
```
### [​](#precompact-input) PreCompact Input
For `manual`, `custom_instructions` comes from what the user passes into
`/compact`. For `auto`, `custom_instructions` is empty.
```
{
  "session_id": "abc123",
  "transcript_path": "~/.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "hook_event_name": "PreCompact",
  "trigger": "manual",
  "custom_instructions": ""
}
```
## [​](#hook-output) Hook Output
There are two ways for hooks to return output back to Claude Code. The output
communicates whether to block and any feedback that should be shown to Claude
and the user.
### [​](#simple%3A-exit-code) Simple: Exit Code
Hooks communicate status through exit codes, stdout, and stderr:
* **Exit code 0**: Success. `stdout` is shown to the user in transcript mode
  (CTRL-R).
* **Exit code 2**: Blocking error. `stderr` is fed back to Claude to process
  automatically. See per-hook-event behavior below.
* **Other exit codes**: Non-blocking error. `stderr` is shown to the user and
  execution continues.
Reminder: Claude Code does not see stdout if the exit code is 0.
#### [​](#exit-code-2-behavior) Exit Code 2 Behavior
| Hook Event | Behavior |
| --- | --- |
| `PreToolUse` | Blocks the tool call, shows error to Claude |
| `PostToolUse` | Shows error to Claude (tool already ran) |
| `Notification` | N/A, shows stderr to user only |
| `Stop` | Blocks stoppage, shows error to Claude |
| `SubagentStop` | Blocks stoppage, shows error to Claude subagent |
| `PreCompact` | N/A, shows stderr to user only |
### [​](#advanced%3A-json-output) Advanced: JSON Output
Hooks can return structured JSON in `stdout` for more sophisticated control:
#### [​](#common-json-fields) Common JSON Fields
All hook types can include these optional fields:
```
{
  "continue": true, // Whether Claude should continue after hook execution (default: true)
  "stopReason": "string" // Message shown when continue is false
  "suppressOutput": true, // Hide stdout from transcript mode (default: false)
}
```
If `continue` is false, Claude stops processing after the hooks run.
* For `PreToolUse`, this is different from `"decision": "block"`, which only
  blocks a specific tool call and provides automatic feedback to Claude.
* For `PostToolUse`, this is different from `"decision": "block"`, which
  provides automated feedback to Claude.
* For `Stop` and `SubagentStop`, this takes precedence over any
  `"decision": "block"` output.
* In all cases, `"continue" = false` takes precedence over any
  `"decision": "block"` output.
`stopReason` accompanies `continue` with a reason shown to the user, not shown
to Claude.
#### [​](#pretooluse-decision-control) `PreToolUse` Decision Control
`PreToolUse` hooks can control whether a tool call proceeds.
* “approve” bypasses the permission system. `reason` is shown to the user but
  not to Claude.
* “block” prevents the tool call from executing. `reason` is shown to Claude.
* `undefined` leads to the existing permission flow. `reason` is ignored.
```
{
  "decision": "approve" | "block" | undefined,
  "reason": "Explanation for decision"
}
```
#### [​](#posttooluse-decision-control) `PostToolUse` Decision Control
`PostToolUse` hooks can control whether a tool call proceeds.
* “block” automatically prompts Claude with `reason`.
* `undefined` does nothing. `reason` is ignored.
```
{
  "decision": "block" | undefined,
  "reason": "Explanation for decision"
}
```
#### [​](#stop%2Fsubagentstop-decision-control) `Stop`/`SubagentStop` Decision Control
`Stop` and `SubagentStop` hooks can control whether Claude must continue.
* “block” prevents Claude from stopping. You must populate `reason` for Claude
  to know how to proceed.
* `undefined` allows Claude to stop. `reason` is ignored.
```
{
  "decision": "block" | undefined,
  "reason": "Must be provided when Claude is blocked from stopping"
}
```
#### [​](#json-output-example%3A-bash-command-editing) JSON Output Example: Bash Command Editing
```
#!/usr/bin/env python3
import json
import re
import sys
# Define validation rules as a list of (regex pattern, message) tuples
VALIDATION_RULES = [
    (
        r"\bgrep\b(?!.*\|)",
        "Use 'rg' (ripgrep) instead of 'grep' for better performance and features",
    ),
    (
        r"\bfind\s+\S+\s+-name\b",
        "Use 'rg --files | rg pattern' or 'rg --files -g pattern' instead of 'find -name' for better performance",
    ),
]
def validate_command(command: str) -> list[str]:
    issues = []
    for pattern, message in VALIDATION_RULES:
        if re.search(pattern, command):
            issues.append(message)
    return issues
try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
    sys.exit(1)
tool_name = input_data.get("tool_name", "")
tool_input = input_data.get("tool_input", {})
command = tool_input.get("command", "")
if tool_name != "Bash" or not command:
    sys.exit(1)
# Validate the command
issues = validate_command(command)
if issues:
    for message in issues:
        print(f"• {message}", file=sys.stderr)
    # Exit code 2 blocks tool call and shows stderr to Claude
    sys.exit(2)
```
## [​](#working-with-mcp-tools) Working with MCP Tools
Claude Code hooks work seamlessly with
[Model Context Protocol (MCP) tools](/en/docs/claude-code/mcp). When MCP servers
provide tools, they appear with a special naming pattern that you can match in
your hooks.
### [​](#mcp-tool-naming) MCP Tool Naming
MCP tools follow the pattern `mcp__<server>__<tool>`, for example:
* `mcp__memory__create_entities` - Memory server’s create entities tool
* `mcp__filesystem__read_file` - Filesystem server’s read file tool
* `mcp__github__search_repositories` - GitHub server’s search tool
### [​](#configuring-hooks-for-mcp-tools) Configuring Hooks for MCP Tools
You can target specific MCP tools or entire MCP servers:
```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Memory operation initiated' >> ~/mcp-operations.log"
          }
        ]
      },
      {
        "matcher": "mcp__.*__write.*",
        "hooks": [
          {
            "type": "command",
            "command": "/home/user/scripts/validate-mcp-write.py"
          }
        ]
      }
    ]
  }
}
```
## [​](#examples) Examples
For practical examples including code formatting, notifications, and file protection, see [More Examples](/en/docs/claude-code/hooks-guide#more-examples) in the get started guide.
## [​](#security-considerations) Security Considerations
### [​](#disclaimer) Disclaimer
**USE AT YOUR OWN RISK**: Claude Code hooks execute arbitrary shell commands on
your system automatically. By using hooks, you acknowledge that:
* You are solely responsible for the commands you configure
* Hooks can modify, delete, or access any files your user account can access
* Malicious or poorly written hooks can cause data loss or system damage
* Anthropic provides no warranty and assumes no liability for any damages
  resulting from hook usage
* You should thoroughly test hooks in a safe environment before production use
Always review and understand any hook commands before adding them to your
configuration.
### [​](#security-best-practices) Security Best Practices
Here are some key practices for writing more secure hooks:
1. **Validate and sanitize inputs** - Never trust input data blindly
2. **Always quote shell variables** - Use `"$VAR"` not `$VAR`
3. **Block path traversal** - Check for `..` in file paths
4. **Use absolute paths** - Specify full paths for scripts
5. **Skip sensitive files** - Avoid `.env`, `.git/`, keys, etc.
### [​](#configuration-safety) Configuration Safety
Direct edits to hooks in settings files don’t take effect immediately. Claude
Code:
1. Captures a snapshot of hooks at startup
2. Uses this snapshot throughout the session
3. Warns if hooks are modified externally
4. Requires review in `/hooks` menu for changes to apply
This prevents malicious hook modifications from affecting your current session.
## [​](#hook-execution-details) Hook Execution Details
* **Timeout**: 60-second execution limit by default, configurable per command.
  + A timeout for an individual command does not affect the other commands.
* **Parallelization**: All matching hooks run in parallel
* **Environment**: Runs in current directory with Claude Code’s environment
* **Input**: JSON via stdin
* **Output**:
  + PreToolUse/PostToolUse/Stop: Progress shown in transcript (Ctrl-R)
  + Notification: Logged to debug only (`--debug`)
## [​](#debugging) Debugging
### [​](#basic-troubleshooting) Basic Troubleshooting
If your hooks aren’t working:
1. **Check configuration** - Run `/hooks` to see if your hook is registered
2. **Verify syntax** - Ensure your JSON settings are valid
3. **Test commands** - Run hook commands manually first
4. **Check permissions** - Make sure scripts are executable
5. **Review logs** - Use `claude --debug` to see hook execution details
Common issues:
* **Quotes not escaped** - Use `\"` inside JSON strings
* **Wrong matcher** - Check tool names match exactly (case-sensitive)
* **Command not found** - Use full paths for scripts
### [​](#advanced-debugging) Advanced Debugging
For complex hook issues:
1. **Inspect hook execution** - Use `claude --debug` to see detailed hook execution
2. **Validate JSON schemas** - Test hook input/output with external tools
3. **Check environment variables** - Verify Claude Code’s environment is correct
4. **Test edge cases** - Try hooks with unusual file paths or inputs
5. **Monitor system resources** - Check for resource exhaustion during hook execution
6. **Use structured logging** - Implement logging in your hook scripts
### [​](#debug-output-example) Debug Output Example
Use `claude --debug` to see hook execution details:
```
[DEBUG] Executing hooks for PostToolUse:Write
[DEBUG] Getting matching hook commands for PostToolUse with query: Write
[DEBUG] Found 1 hook matchers in settings
[DEBUG] Matched 1 hooks for query "Write"
[DEBUG] Found 1 hook commands to execute
[DEBUG] Executing hook command: <Your command> with timeout 60000ms
[DEBUG] Hook command completed with status 0: <Your stdout>
```
Progress messages appear in transcript mode (Ctrl-R) showing:
* Which hook is running
* Command being executed
* Success/failure status
* Output or error messages
Was this page helpful?
YesNo
[Slash commands](/en/docs/claude-code/slash-commands)[Data usage](/en/docs/claude-code/data-usage)
On this page


---

## Hooks Guide

*Source: https://docs.anthropic.com/en/docs/claude-code/hooks-guide*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Build with Claude Code
Get started with Claude Code hooks
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
Claude Code hooks are user-defined shell commands that execute at various points
in Claude Code’s lifecycle. Hooks provide deterministic control over Claude
Code’s behavior, ensuring certain actions always happen rather than relying on
the LLM to choose to run them.
For reference documentation on hooks, see [Hooks reference](/en/docs/claude-code/hooks).
Example use cases for hooks include:
* **Notifications**: Customize how you get notified when Claude Code is awaiting
  your input or permission to run something.
* **Automatic formatting**: Run `prettier` on .ts files, `gofmt` on .go files,
  etc. after every file edit.
* **Logging**: Track and count all executed commands for compliance or
  debugging.
* **Feedback**: Provide automated feedback when Claude Code produces code that
  does not follow your codebase conventions.
* **Custom permissions**: Block modifications to production files or sensitive
  directories.
By encoding these rules as hooks rather than prompting instructions, you turn
suggestions into app-level code that executes every time it is expected to run.
You must consider the security implication of hooks as you add them, because hooks run automatically during the agent loop with your current environment’s credentials.
For example, malicious hooks code can exfiltrate your data. Always review your hooks implementation before registering them.
For full security best practices, see [Security Considerations](/en/docs/claude-code/hooks#security-considerations) in the hooks reference documentation.
## [​](#hook-events-overview) Hook Events Overview
Claude Code provides several hook events that run at different points in the workflow:
* **PreToolUse**: Runs before tool calls (can block them)
* **PostToolUse**: Runs after tool calls complete
* **Notification**: Runs when Claude Code sends notifications
* **Stop**: Runs when Claude Code finishes responding
* **SubagentStop**: Runs when subagent tasks complete
Each event receives different data and can control Claude’s behavior in different ways.
## [​](#quickstart) Quickstart
In this quickstart, you’ll add a hook that logs the shell commands that Claude
Code runs.
### [​](#prerequisites) Prerequisites
Install `jq` for JSON processing in the command line.
### [​](#step-1%3A-open-hooks-configuration) Step 1: Open hooks configuration
Run the `/hooks` [slash command](/en/docs/claude-code/slash-commands) and select
the `PreToolUse` hook event.
`PreToolUse` hooks run before tool calls and can block them while providing
Claude feedback on what to do differently.
### [​](#step-2%3A-add-a-matcher) Step 2: Add a matcher
Select `+ Add new matcher…` to run your hook only on Bash tool calls.
Type `Bash` for the matcher.
Use an empty string `""` to match all tools. The `*` character is not a valid matcher on its own.
### [​](#step-3%3A-add-the-hook) Step 3: Add the hook
Select `+ Add new hook…` and enter this command:
```
jq -r '"\(.tool_input.command) - \(.tool_input.description // "No description")"' >> ~/.claude/bash-command-log.txt
```
### [​](#step-4%3A-save-your-configuration) Step 4: Save your configuration
For storage location, select `User settings` since you’re logging to your home
directory. This hook will then apply to all projects, not just your current
project.
Then press Esc until you return to the REPL. Your hook is now registered!
### [​](#step-5%3A-verify-your-hook) Step 5: Verify your hook
Run `/hooks` again or check `~/.claude/settings.json` to see your configuration:
```
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
### [​](#step-6%3A-test-your-hook) Step 6: Test your hook
Ask Claude to run a simple command like `ls` and check your log file:
```
cat ~/.claude/bash-command-log.txt
```
You should see entries like:
```
ls - Lists files and directories
```
## [​](#more-examples) More Examples
For a complete example implementation, see the [bash command validator example](https://github.com/anthropics/claude-code/blob/main/examples/hooks/bash_command_validator_example.py) in our public codebase.
### [​](#code-formatting-hook) Code Formatting Hook
Automatically format TypeScript files after editing:
```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|MultiEdit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "if echo '$(.tool_input.file_path)' | grep -q '\\.ts$'; then npx prettier --write '$(.tool_input.file_path)'; fi"
          }
        ]
      }
    ]
  }
}
```
### [​](#custom-notification-hook) Custom Notification Hook
Get desktop notifications when Claude needs input:
```
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "notify-send 'Claude Code' 'Awaiting your input'"
          }
        ]
      }
    ]
  }
}
```
### [​](#file-protection-hook) File Protection Hook
Block edits to sensitive files:
```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|MultiEdit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 -c \"import json, sys; data=json.load(sys.stdin); path=data.get('tool_input',{}).get('file_path',''); sys.exit(2 if any(p in path for p in ['.env', 'package-lock.json', '.git/']) else 0)\""
          }
        ]
      }
    ]
  }
}
```
## [​](#learn-more) Learn more
* For reference documentation on hooks, see [Hooks reference](/en/docs/claude-code/hooks).
* For comprehensive security best practices and safety guidelines, see [Security Considerations](/en/docs/claude-code/hooks#security-considerations) in the hooks reference documentation.
* For troubleshooting steps and debugging techniques, see [Debugging](/en/docs/claude-code/hooks#debugging) in the hooks reference documentation.
Was this page helpful?
YesNo
[Claude Code SDK](/en/docs/claude-code/sdk)[GitHub Actions](/en/docs/claude-code/github-actions)
On this page


---

## Iam

*Source: https://docs.anthropic.com/en/docs/claude-code/iam*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Administration
Identity and Access Management
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
## [​](#authentication-methods) Authentication methods
Setting up Claude Code requires access to Anthropic models. For teams, you can set up Claude Code access in one of three ways:
* Anthropic API via the Anthropic Console
* Amazon Bedrock
* Google Vertex AI
### [​](#anthropic-api-authentication) Anthropic API authentication
**To set up Claude Code access for your team via Anthropic API:**
1. Use your existing Anthropic Console account or create a new Anthropic Console account
2. You can add users through either method below:
   * Bulk invite users from within the Console (Console -> Settings -> Members -> Invite)
   * [Set up SSO](https://support.anthropic.com/en/articles/10280258-setting-up-single-sign-on-on-the-api-console)
3. When inviting users, they need one of the following roles:
   * “Claude Code” role means users can only create Claude Code API keys
   * “Developer” role means users can create any kind of API key
4. Each invited user needs to complete these steps:
   * Accept the Console invite
   * [Check system requirements](/en/docs/claude-code/setup#system-requirements)
   * [Install Claude Code](/en/docs/claude-code/setup#installation)
   * Login with Console account credentials
### [​](#cloud-provider-authentication) Cloud provider authentication
**To set up Claude Code access for your team via Bedrock or Vertex:**
1. Follow the [Bedrock docs](/en/docs/claude-code/amazon-bedrock) or [Vertex docs](/en/docs/claude-code/google-vertex-ai)
2. Distribute the environment variables and instructions for generating cloud credentials to your users. Read more about how to [manage configuration here](/en/docs/claude-code/settings).
3. Users can [install Claude Code](/en/docs/claude-code/setup#installation)
## [​](#access-control-and-permissions) Access control and permissions
We support fine-grained permissions so that you’re able to specify exactly what the agent is allowed to do (e.g. run tests, run linter) and what it is not allowed to do (e.g. update cloud infrastructure). These permission settings can be checked into version control and distributed to all developers in your organization, as well as customized by individual developers.
### [​](#permission-system) Permission system
Claude Code uses a tiered permission system to balance power and safety:
| Tool Type | Example | Approval Required | ”Yes, don’t ask again” Behavior |
| --- | --- | --- | --- |
| Read-only | File reads, LS, Grep | No | N/A |
| Bash Commands | Shell execution | Yes | Permanently per project directory and command |
| File Modification | Edit/write files | Yes | Until session end |
### [​](#configuring-permissions) Configuring permissions
You can view & manage Claude Code’s tool permissions with `/permissions`. This UI lists all permission rules and the settings.json file they are sourced from.
* **Allow** rules will allow Claude Code to use the specified tool without further manual approval.
* **Deny** rules will prevent Claude Code from using the specified tool. Deny rules take precedence over allow rules.
* **Additional directories** extend Claude’s file access to directories beyond the initial working directory.
* **Default mode** controls Claude’s permission behavior when encountering new requests.
Permission rules use the format: `Tool(optional-specifier)`
A rule that is just the tool name matches any use of that tool. For example, adding `Bash` to the list of allow rules would allow Claude Code to use the Bash tool without requiring user approval.
#### [​](#permission-modes) Permission modes
Claude Code supports several permission modes that can be set as the `defaultMode` in [settings files](/en/docs/claude-code/settings#settings-files):
| Mode | Description |
| --- | --- |
| `default` | Standard behavior - prompts for permission on first use of each tool |
| `acceptEdits` | Automatically accepts file edit permissions for the session |
| `plan` | Plan mode - Claude can analyze but not modify files or execute commands |
| `bypassPermissions` | Skips all permission prompts (requires safe environment - see warning below) |
#### [​](#working-directories) Working directories
By default, Claude has access to files in the directory where it was launched. You can extend this access:
* **During startup**: Use `--add-dir <path>` CLI argument
* **During session**: Use `/add-dir` slash command
* **Persistent configuration**: Add to `additionalDirectories` in [settings files](/en/docs/claude-code/settings#settings-files)
Files in additional directories follow the same permission rules as the original working directory - they become readable without prompts, and file editing permissions follow the current permission mode.
#### [​](#tool-specific-permission-rules) Tool-specific permission rules
Some tools use the optional specifier for more fine-grained permission controls. For example, an allow rule with `Bash(git diff:*)` would allow Bash commands that start with `git diff`. The following tools support permission rules with specifiers:
**Bash**
* `Bash(npm run build)` Matches the exact Bash command `npm run build`
* `Bash(npm run test:*)` Matches Bash commands starting with `npm run test`.
Claude Code is aware of shell operators (like `&&`) so a prefix match rule like `Bash(safe-cmd:*)` won’t give it permission to run the command `safe-cmd && other-cmd`
**Read & Edit**
`Edit` rules apply to all built-in tools that edit files. Claude will make a best-effort attempt to apply `Read` rules to all built-in tools that read files like Grep, Glob, and LS.
Read & Edit rules both follow the [gitignore](https://git-scm.com/docs/gitignore) specification. Patterns are resolved relative to the directory containing `.claude/settings.json`. To reference an absolute path, use `//`. For a path relative to your home directory, use `~/`.
* `Edit(docs/**)` Matches edits to files in the `docs` directory of your project
* `Read(~/.zshrc)` Matches reads to your `~/.zshrc` file
* `Edit(//tmp/scratch.txt)` Matches edits to `/tmp/scratch.txt`
**WebFetch**
* `WebFetch(domain:example.com)` Matches fetch requests to example.com
**MCP**
* `mcp__puppeteer` Matches any tool provided by the `puppeteer` server (name configured in Claude Code)
* `mcp__puppeteer__puppeteer_navigate` Matches the `puppeteer_navigate` tool provided by the `puppeteer` server
### [​](#enterprise-managed-policy-settings) Enterprise managed policy settings
For enterprise deployments of Claude Code, we support enterprise managed policy settings that take precedence over user and project settings. This allows system administrators to enforce security policies that users cannot override.
System administrators can deploy policies to:
* macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
* Linux and WSL: `/etc/claude-code/managed-settings.json`
* Windows: `C:\ProgramData\ClaudeCode\managed-settings.json`
These policy files follow the same format as regular [settings files](/en/docs/claude-code/settings#settings-files) but cannot be overridden by user or project settings. This ensures consistent security policies across your organization.
### [​](#settings-precedence) Settings precedence
When multiple settings sources exist, they are applied in the following order (highest to lowest precedence):
1. Enterprise policies
2. Command line arguments
3. Local project settings (`.claude/settings.local.json`)
4. Shared project settings (`.claude/settings.json`)
5. User settings (`~/.claude/settings.json`)
This hierarchy ensures that organizational policies are always enforced while still allowing flexibility at the project and user levels where appropriate.
### [​](#additional-permission-control-with-hooks) Additional permission control with hooks
[Claude Code hooks](/en/docs/claude-code/hooks-guide) provide a way to register custom shell commands to perform permission evaluation at runtime. When Claude Code makes a tool call, PreToolUse hooks run before the permission system runs, and the hook output can determine whether to approve or deny the tool call in place of the permission system.
## [​](#credential-management) Credential management
Claude Code supports authentication via Claude.ai credentials, Anthropic API credentials, Bedrock Auth, and Vertex Auth. On macOS, the API keys, OAuth tokens, and other credentials are stored on encrypted macOS Keychain. Alternately, the setting [apiKeyHelper](/en/docs/claude-code/settings#available-settings) can be set to a shell script which returns an API key. By default, this helper is called after 5 minutes or on HTTP 401 response; specifying environment variable `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` defines a custom refresh interval.
Was this page helpful?
YesNo
[Advanced installation](/en/docs/claude-code/setup)[Security](/en/docs/claude-code/security)
On this page


---

## Ide Integrations

*Source: https://docs.anthropic.com/en/docs/claude-code/ide-integrations*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Configuration
Add Claude Code to your IDE
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
Claude Code works great with any Integrated Development Environment (IDE) that has a terminal. Just run `claude`, and you’re ready to go.
In addition, Claude Code provides dedicated integrations for popular IDEs, which provide features like interactive diff viewing, selection context sharing, and more. These integrations currently exist for:
* **Visual Studio Code** (including popular forks like Cursor, Windsurf, and VSCodium)
* **JetBrains IDEs** (including IntelliJ, PyCharm, Android Studio, WebStorm, PhpStorm and GoLand)
## [​](#features) Features
* **Quick launch**: Use `Cmd+Esc` (Mac) or `Ctrl+Esc` (Windows/Linux) to open
  Claude Code directly from your editor, or click the Claude Code button in the
  UI
* **Diff viewing**: Code changes can be displayed directly in the IDE diff
  viewer instead of the terminal. You can configure this in `/config`
* **Selection context**: The current selection/tab in the IDE is automatically
  shared with Claude Code
* **File reference shortcuts**: Use `Cmd+Option+K` (Mac) or `Alt+Ctrl+K`
  (Linux/Windows) to insert file references (e.g., @File#L1-99)
* **Diagnostic sharing**: Diagnostic errors (lint, syntax, etc.) from the IDE
  are automatically shared with Claude as you work
## [​](#installation) Installation
* VS Code+
* JetBrains
To install Claude Code on VS Code and popular forks like Cursor, Windsurf, and VSCodium:
1. Open VS Code
2. Open the integrated terminal
3. Run `claude` - the extension will auto-install
To install Claude Code on VS Code and popular forks like Cursor, Windsurf, and VSCodium:
1. Open VS Code
2. Open the integrated terminal
3. Run `claude` - the extension will auto-install
To install Claude Code on JetBrains IDEs like IntelliJ, PyCharm, Android Studio, WebStorm, PhpStorm and GoLand, find and install the [Claude Code plugin](https://docs.anthropic.com/s/claude-code-jetbrains) from the marketplace and restart your IDE.
The plugin may also be auto-installed when you run `claude` in the integrated terminal. The IDE must be restarted completely to take effect.
**Remote Development Limitations**: When using JetBrains Remote Development, you must install the plugin in the remote host via `Settings > Plugin (Host)`.
## [​](#usage) Usage
### [​](#from-your-ide) From your IDE
Run `claude` from your IDE’s integrated terminal, and all features will be active.
### [​](#from-external-terminals) From external terminals
Use the `/ide` command in any external terminal to connect Claude Code to your IDE and activate all features.
If you want Claude to have access to the same files as your IDE, start Claude Code from the same directory as your IDE project root.
## [​](#configuration) Configuration
IDE integrations work with Claude Code’s configuration system:
1. Run `claude`
2. Enter the `/config` command
3. Adjust your preferences. Setting the diff tool to `auto` will enable automatic IDE detection
## [​](#troubleshooting) Troubleshooting
### [​](#vs-code-extension-not-installing) VS Code extension not installing
* Ensure you’re running Claude Code from VS Code’s integrated terminal
* Ensure that the CLI corresponding to your IDE is installed:
  + For VS Code: `code` command should be available
  + For Cursor: `cursor` command should be available
  + For Windsurf: `windsurf` command should be available
  + For VSCodium: `codium` command should be available
  + If not installed, use `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
    and search for “Shell Command: Install ‘code’ command in PATH” (or the
    equivalent for your IDE)
* Check that VS Code has permission to install extensions
### [​](#jetbrains-plugin-not-working) JetBrains plugin not working
* Ensure you’re running Claude Code from the project root directory
* Check that the JetBrains plugin is enabled in the IDE settings
* Completely restart the IDE. You may need to do this multiple times
* For JetBrains Remote Development, ensure that the Claude Code plugin is
  installed in the remote host and not locally on the client
For additional help, refer to our
[troubleshooting guide](/en/docs/claude-code/troubleshooting).
Was this page helpful?
YesNo
[Settings](/en/docs/claude-code/settings)[Terminal configuration](/en/docs/claude-code/terminal-config)
On this page


---

## Interactive Mode

*Source: https://docs.anthropic.com/en/docs/claude-code/interactive-mode*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Reference
Interactive mode
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
## [​](#keyboard-shortcuts) Keyboard shortcuts
### [​](#general-controls) General controls
| Shortcut | Description | Context |
| --- | --- | --- |
| `Ctrl+C` | Cancel current input or generation | Standard interrupt |
| `Ctrl+D` | Exit Claude Code session | EOF signal |
| `Ctrl+L` | Clear terminal screen | Keeps conversation history |
| `Up/Down arrows` | Navigate command history | Recall previous inputs |
| `Esc` + `Esc` | Edit previous message | Double-escape to modify |
### [​](#multiline-input) Multiline input
| Method | Shortcut | Context |
| --- | --- | --- |
| Quick escape | `\` + `Enter` | Works in all terminals |
| macOS default | `Option+Enter` | Default on macOS |
| Terminal setup | `Shift+Enter` | After `/terminal-setup` |
| Paste mode | Paste directly | For code blocks, logs |
### [​](#quick-commands) Quick commands
| Shortcut | Description | Notes |
| --- | --- | --- |
| `#` at start | Memory shortcut - add to CLAUDE.md | Prompts for file selection |
| `/` at start | Slash command | See [slash commands](/en/docs/claude-code/slash-commands) |
## [​](#vim-mode) Vim mode
Enable vim-style editing with `/vim` command or configure permanently via `/config`.
### [​](#mode-switching) Mode switching
| Command | Action | From mode |
| --- | --- | --- |
| `Esc` | Enter NORMAL mode | INSERT |
| `i` | Insert before cursor | NORMAL |
| `I` | Insert at beginning of line | NORMAL |
| `a` | Insert after cursor | NORMAL |
| `A` | Insert at end of line | NORMAL |
| `o` | Open line below | NORMAL |
| `O` | Open line above | NORMAL |
### [​](#navigation-normal-mode) Navigation (NORMAL mode)
| Command | Action |
| --- | --- |
| `h`/`j`/`k`/`l` | Move left/down/up/right |
| `w` | Next word |
| `e` | End of word |
| `b` | Previous word |
| `0` | Beginning of line |
| `$` | End of line |
| `^` | First non-blank character |
| `gg` | Beginning of input |
| `G` | End of input |
### [​](#editing-normal-mode) Editing (NORMAL mode)
| Command | Action |
| --- | --- |
| `x` | Delete character |
| `dd` | Delete line |
| `D` | Delete to end of line |
| `dw`/`de`/`db` | Delete word/to end/back |
| `cc` | Change line |
| `C` | Change to end of line |
| `cw`/`ce`/`cb` | Change word/to end/back |
| `.` | Repeat last change |
Configure your preferred line break behavior in terminal settings. Run `/terminal-setup` to install Shift+Enter binding for iTerm2 and VS Code terminals.
## [​](#command-history) Command history
Claude Code maintains command history for the current session:
* History is stored per working directory
* Cleared with `/clear` command
* Use Up/Down arrows to navigate (see keyboard shortcuts above)
* **Ctrl+R**: Reverse search through history (if supported by terminal)
* **Note**: History expansion (`!`) is disabled by default
## [​](#see-also) See also
* [Slash commands](/en/docs/claude-code/slash-commands) - Interactive session commands
* [CLI reference](/en/docs/claude-code/cli-reference) - Command-line flags and options
* [Settings](/en/docs/claude-code/settings) - Configuration options
* [Memory management](/en/docs/claude-code/memory) - Managing CLAUDE.md files
Was this page helpful?
YesNo
[CLI reference](/en/docs/claude-code/cli-reference)[Slash commands](/en/docs/claude-code/slash-commands)
On this page


---

## Legal And Compliance

*Source: https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Resources
Legal and compliance
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
## [​](#legal-agreements) Legal agreements
### [​](#license) License
Claude Code is provided under Anthropic’s [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms).
### [​](#commercial-agreements) Commercial agreements
Whether you’re using Anthropic’s API directly (1P) or accessing it through AWS Bedrock or Google Vertex (3P), your existing commercial agreement will apply to Claude Code usage, unless we’ve mutually agreed otherwise.
## [​](#compliance) Compliance
### [​](#healthcare-compliance-baa) Healthcare compliance (BAA)
If a customer has a Business Associate Agreement (BAA) with us, and wants to use Claude Code, the BAA will automatically extend to cover Claude Code if the customer has executed a BAA and has Zero Data Retention (ZDR) activated. The BAA will be applicable to that customer’s API traffic flowing through Claude Code.
## [​](#security-and-trust) Security and trust
### [​](#trust-and-safety) Trust and safety
You can find more information in the [Anthropic Trust Center](https://trust.anthropic.com) and [Transparency Hub](https://www.anthropic.com/transparency).
### [​](#security-vulnerability-reporting) Security vulnerability reporting
Anthropic manages our security program through HackerOne. [Use this form to report vulnerabilities](https://hackerone.com/anthropic-vdp/reports/new?type=team&report_type=vulnerability).
© Anthropic PBC. All rights reserved. Use is subject to Anthropic’s [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms).
Was this page helpful?
YesNo
[Data usage](/en/docs/claude-code/data-usage)
On this page


---

## Llm Gateway

*Source: https://docs.anthropic.com/en/docs/claude-code/llm-gateway*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Deployment
LLM gateway configuration
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
LLM gateways provide a centralized proxy layer between Claude Code and model providers, offering:
* **Centralized authentication** - Single point for API key management
* **Usage tracking** - Monitor usage across teams and projects
* **Cost controls** - Implement budgets and rate limits
* **Audit logging** - Track all model interactions for compliance
* **Model routing** - Switch between providers without code changes
## [​](#litellm-configuration) LiteLLM configuration
LiteLLM is a third-party proxy service. Anthropic doesn’t endorse, maintain, or audit LiteLLM’s security or functionality. This guide is provided for informational purposes and may become outdated. Use at your own discretion.
### [​](#prerequisites) Prerequisites
* Claude Code updated to the latest version
* LiteLLM Proxy Server deployed and accessible
* Access to Claude models through your chosen provider
### [​](#basic-litellm-setup) Basic LiteLLM setup
**Configure Claude Code**:
#### [​](#authentication-methods) Authentication methods
##### Static API key
Simplest method using a fixed API key:
```
# Set in environment
export ANTHROPIC_AUTH_TOKEN=sk-litellm-static-key
# Or in Claude Code settings
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-litellm-static-key"
  }
}
```
This value will be sent as the `Authorization` and `Proxy-Authorization` headers, although `Authorization` may be overwritten (see Vertex “Client-specified credentials” below).
##### Dynamic API key with helper
For rotating keys or per-user authentication:
1. Create an API key helper script:
```
#!/bin/bash
# ~/bin/get-litellm-key.sh
# Example: Fetch key from vault
vault kv get -field=api_key secret/litellm/claude-code
# Example: Generate JWT token
jwt encode \
  --secret="${JWT_SECRET}" \
  --exp="+1h" \
  '{"user":"'${USER}'","team":"engineering"}'
```
2. Configure Claude Code settings to use the helper:
```
{
  "apiKeyHelper": "~/bin/get-litellm-key.sh"
}
```
3. Set token refresh interval:
```
# Refresh every hour (3600000 ms)
export CLAUDE_CODE_API_KEY_HELPER_TTL_MS=3600000
```
This value will be sent as `Authorization`, `Proxy-Authorization`, and `X-Api-Key` headers, although `Authorization` may be overwritten (see [Google Vertex AI through LiteLLM](/_sites/docs.anthropic.com/en/docs/claude-code/llm-gateway#google-vertex-ai-through-litellm)). The `apiKeyHelper` has lower precedence than `ANTHROPIC_AUTH_TOKEN` or `ANTHROPIC_API_KEY`.
#### [​](#unified-endpoint-recommended) Unified endpoint (recommended)
Using LiteLLM’s [Anthropic format endpoint](https://docs.litellm.ai/docs/anthropic_unified):
```
export ANTHROPIC_BASE_URL=https://litellm-server:4000
```
**Benefits of the unified endpoint over pass-through endpoints:**
* Load balancing
* Fallbacks
* Consistent support for cost tracking and end-user tracking
#### [​](#provider-specific-pass-through-endpoints-alternative) Provider-specific pass-through endpoints (alternative)
##### Anthropic API through LiteLLM
Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/anthropic_completion):
```
export ANTHROPIC_BASE_URL=https://litellm-server:4000/anthropic
```
##### Amazon Bedrock through LiteLLM
Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/bedrock):
```
export ANTHROPIC_BEDROCK_BASE_URL=https://litellm-server:4000/bedrock
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1
export CLAUDE_CODE_USE_BEDROCK=1
```
##### Google Vertex AI through LiteLLM
Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/vertex_ai):
**Recommended: Proxy-specified credentials**
```
export ANTHROPIC_VERTEX_BASE_URL=https://litellm-server:4000/vertex_ai/v1
export ANTHROPIC_VERTEX_PROJECT_ID=your-gcp-project-id
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
```
**Alternative: Client-specified credentials**
If you prefer to use local GCP credentials:
1. Authenticate with GCP locally:
```
gcloud auth application-default login
```
2. Set Claude Code environment:
```
export ANTHROPIC_VERTEX_BASE_URL=https://litellm-server:4000/vertex_ai/v1
export ANTHROPIC_VERTEX_PROJECT_ID=your-gcp-project-id
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
```
3. Update LiteLLM header configuration:
Ensure your LiteLLM config has `general_settings.litellm_key_header_name` set to `Proxy-Authorization`, since the pass-through GCP token will be located on the `Authorization` header.
### [​](#model-selection) Model selection
By default, the models will use those specified in [Model configuration](/en/docs/claude-code/bedrock-vertex-proxies#model-configuration).
If you have configured custom model names in LiteLLM, set the aforementioned environment variables to those custom names.
For more detailed information, refer to the [LiteLLM documentation](https://docs.litellm.ai/).
## [​](#additional-resources) Additional resources
* [LiteLLM documentation](https://docs.litellm.ai/)
* [Claude Code settings](/en/docs/claude-code/settings)
* [Corporate proxy setup](/en/docs/claude-code/corporate-proxy)
* [Third-party integrations overview](/en/docs/claude-code/third-party-integrations)
Was this page helpful?
YesNo
[Corporate proxy](/en/docs/claude-code/corporate-proxy)[Development containers](/en/docs/claude-code/devcontainer)
On this page


---

## Mcp

*Source: https://docs.anthropic.com/en/docs/claude-code/mcp*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Build with Claude Code
Model Context Protocol (MCP)
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
Model Context Protocol (MCP) is an open protocol that enables LLMs to access external tools and data sources. For more details about MCP, see the [MCP documentation](https://modelcontextprotocol.io/introduction).
Use third party MCP servers at your own risk. Make sure you trust the MCP
servers, and be especially careful when using MCP servers that talk to the
internet, as these can expose you to prompt injection risk.
## [​](#configure-mcp-servers) Configure MCP servers
1
Add an MCP stdio Server
```
# Basic syntax
claude mcp add <name> <command> [args...]
# Example: Adding a local server
claude mcp add my-server -e API_KEY=123 -- /path/to/server arg1 arg2
```
2
Add an MCP SSE Server
```
# Basic syntax
claude mcp add --transport sse <name> <url>
# Example: Adding an SSE server
claude mcp add --transport sse sse-server https://example.com/sse-endpoint
# Example: Adding an SSE server with custom headers
claude mcp add --transport sse api-server https://api.example.com/mcp --header "X-API-Key: your-key"
```
3
Add an MCP HTTP Server
```
# Basic syntax
claude mcp add --transport http <name> <url>
# Example: Adding a streamable HTTP server
claude mcp add --transport http http-server https://example.com/mcp
# Example: Adding an HTTP server with authentication header
claude mcp add --transport http secure-server https://api.example.com/mcp --header "Authorization: Bearer your-token"
```
4
Manage your MCP servers
```
# List all configured servers
claude mcp list
# Get details for a specific server
claude mcp get my-server
# Remove a server
claude mcp remove my-server
```
Tips:
* Use the `-s` or `--scope` flag to specify where the configuration is stored:
  + `local` (default): Available only to you in the current project (was called `project` in older versions)
  + `project`: Shared with everyone in the project via `.mcp.json` file
  + `user`: Available to you across all projects (was called `global` in older versions)
* Set environment variables with `-e` or `--env` flags (e.g., `-e KEY=value`)
* Configure MCP server startup timeout using the MCP\_TIMEOUT environment variable (e.g., `MCP_TIMEOUT=10000 claude` sets a 10-second timeout)
* Check MCP server status any time using the `/mcp` command within Claude Code
* MCP follows a client-server architecture where Claude Code (the client) can connect to multiple specialized servers
* Claude Code supports SSE (Server-Sent Events) and streamable HTTP servers for real-time communication
* Use `/mcp` to authenticate with remote servers that require OAuth 2.0 authentication
## [​](#understanding-mcp-server-scopes) Understanding MCP server scopes
MCP servers can be configured at three different scope levels, each serving distinct purposes for managing server accessibility and sharing. Understanding these scopes helps you determine the best way to configure servers for your specific needs.
### [​](#scope-hierarchy-and-precedence) Scope hierarchy and precedence
MCP server configurations follow a clear precedence hierarchy. When servers with the same name exist at multiple scopes, the system resolves conflicts by prioritizing local-scoped servers first, followed by project-scoped servers, and finally user-scoped servers. This design ensures that personal configurations can override shared ones when needed.
### [​](#local-scope) Local scope
Local-scoped servers represent the default configuration level and are stored in your project-specific user settings. These servers remain private to you and are only accessible when working within the current project directory. This scope is ideal for personal development servers, experimental configurations, or servers containing sensitive credentials that shouldn’t be shared.
```
# Add a local-scoped server (default)
claude mcp add my-private-server /path/to/server
# Explicitly specify local scope
claude mcp add my-private-server -s local /path/to/server
```
### [​](#project-scope) Project scope
Project-scoped servers enable team collaboration by storing configurations in a `.mcp.json` file at your project’s root directory. This file is designed to be checked into version control, ensuring all team members have access to the same MCP tools and services. When you add a project-scoped server, Claude Code automatically creates or updates this file with the appropriate configuration structure.
```
# Add a project-scoped server
claude mcp add shared-server -s project /path/to/server
```
The resulting `.mcp.json` file follows a standardized format:
```
{
  "mcpServers": {
    "shared-server": {
      "command": "/path/to/server",
      "args": [],
      "env": {}
    }
  }
}
```
For security reasons, Claude Code prompts for approval before using project-scoped servers from `.mcp.json` files. If you need to reset these approval choices, use the `claude mcp reset-project-choices` command.
### [​](#user-scope) User scope
User-scoped servers provide cross-project accessibility, making them available across all projects on your machine while remaining private to your user account. This scope works well for personal utility servers, development tools, or services you frequently use across different projects.
```
# Add a user server
claude mcp add my-user-server -s user /path/to/server
```
### [​](#choosing-the-right-scope) Choosing the right scope
Select your scope based on:
* **Local scope**: Personal servers, experimental configurations, or sensitive credentials specific to one project
* **Project scope**: Team-shared servers, project-specific tools, or services required for collaboration
* **User scope**: Personal utilities needed across multiple projects, development tools, or frequently-used services
### [​](#environment-variable-expansion-in-mcp-json) Environment variable expansion in `.mcp.json`
Claude Code supports environment variable expansion in `.mcp.json` files, allowing teams to share configurations while maintaining flexibility for machine-specific paths and sensitive values like API keys.
**Supported syntax:**
* `${VAR}` - Expands to the value of environment variable `VAR`
* `${VAR:-default}` - Expands to `VAR` if set, otherwise uses `default`
**Expansion locations:**
Environment variables can be expanded in:
* `command` - The server executable path
* `args` - Command-line arguments
* `env` - Environment variables passed to the server
* `url` - For SSE/HTTP server types
* `headers` - For SSE/HTTP server authentication
**Example with variable expansion:**
```
{
  "mcpServers": {
    "api-server": {
      "type": "sse",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}"
      }
    }
  }
}
```
If a required environment variable is not set and has no default value, Claude Code will fail to parse the config.
## [​](#authenticate-with-remote-mcp-servers) Authenticate with remote MCP servers
Many remote MCP servers require authentication. Claude Code supports OAuth 2.0 authentication flow for secure connection to these servers.
1
Add a remote server requiring authentication
```
# Add an SSE or HTTP server that requires OAuth
claude mcp add --transport sse github-server https://api.github.com/mcp
```
2
Authenticate using the /mcp command
Within Claude Code, use the `/mcp` command to manage authentication:
```
> /mcp
```
This opens an interactive menu where you can:
* View connection status for all servers
* Authenticate with servers requiring OAuth
* Clear existing authentication
* View server capabilities
3
Complete the OAuth flow
When you select “Authenticate” for a server:
1. Your browser opens automatically to the OAuth provider
2. Complete the authentication in your browser
3. Claude Code receives and securely stores the access token
4. The server connection becomes active
Tips:
* Authentication tokens are stored securely and refreshed automatically
* Use “Clear authentication” in the `/mcp` menu to revoke access
* If your browser doesn’t open automatically, copy the provided URL
* OAuth authentication works with both SSE and HTTP transports
## [​](#connect-to-a-postgres-mcp-server) Connect to a Postgres MCP server
Suppose you want to give Claude read-only access to a PostgreSQL database for querying and schema inspection.
1
Add the Postgres MCP server
```
claude mcp add postgres-server /path/to/postgres-mcp-server --connection-string "postgresql://user:pass@localhost:5432/mydb"
```
2
Query your database with Claude
```
> describe the schema of our users table
```
```
> what are the most recent orders in the system?
```
```
> show me the relationship between customers and invoices
```
Tips:
* The Postgres MCP server provides read-only access for safety
* Claude can help you explore database structure and run analytical queries
* You can use this to quickly understand database schemas in unfamiliar projects
* Make sure your connection string uses appropriate credentials with minimum required permissions
## [​](#add-mcp-servers-from-json-configuration) Add MCP servers from JSON configuration
Suppose you have a JSON configuration for a single MCP server that you want to add to Claude Code.
1
Add an MCP server from JSON
```
# Basic syntax
claude mcp add-json <name> '<json>'
# Example: Adding a stdio server with JSON configuration
claude mcp add-json weather-api '{"type":"stdio","command":"/path/to/weather-cli","args":["--api-key","abc123"],"env":{"CACHE_DIR":"/tmp"}}'
```
2
Verify the server was added
```
claude mcp get weather-api
```
Tips:
* Make sure the JSON is properly escaped in your shell
* The JSON must conform to the MCP server configuration schema
* You can use `-s global` to add the server to your global configuration instead of the project-specific one
## [​](#import-mcp-servers-from-claude-desktop) Import MCP servers from Claude Desktop
Suppose you have already configured MCP servers in Claude Desktop and want to use the same servers in Claude Code without manually reconfiguring them.
1
Import servers from Claude Desktop
```
# Basic syntax 
claude mcp add-from-claude-desktop 
```
2
Select which servers to import
After running the command, you’ll see an interactive dialog that allows you to select which servers you want to import.
3
Verify the servers were imported
```
claude mcp list 
```
Tips:
* This feature only works on macOS and Windows Subsystem for Linux (WSL)
* It reads the Claude Desktop configuration file from its standard location on those platforms
* Use the `-s global` flag to add servers to your global configuration
* Imported servers will have the same names as in Claude Desktop
* If servers with the same names already exist, they will get a numerical suffix (e.g., `server_1`)
## [​](#use-claude-code-as-an-mcp-server) Use Claude Code as an MCP server
Suppose you want to use Claude Code itself as an MCP server that other applications can connect to, providing them with Claude’s tools and capabilities.
1
Start Claude as an MCP server
```
# Basic syntax
claude mcp serve
```
2
Connect from another application
You can connect to Claude Code MCP server from any MCP client, such as Claude Desktop. If you’re using Claude Desktop, you can add the Claude Code MCP server using this configuration:
```
{
  "command": "claude",
  "args": ["mcp", "serve"],
  "env": {}
}
```
Tips:
* The server provides access to Claude’s tools like View, Edit, LS, etc.
* In Claude Desktop, try asking Claude to read files in a directory, make edits, and more.
* Note that this MCP server is simply exposing Claude Code’s tools to your MCP client, so your own client is responsible for implementing user confirmation for individual tool calls.
## [​](#use-mcp-resources) Use MCP resources
MCP servers can expose resources that you can reference using @ mentions, similar to how you reference files.
### [​](#reference-mcp-resources) Reference MCP resources
1
List available resources
Type `@` in your prompt to see available resources from all connected MCP servers. Resources appear alongside files in the autocomplete menu.
2
Reference a specific resource
Use the format `@server:protocol://resource/path` to reference a resource:
```
> Can you analyze @github:issue://123 and suggest a fix?
```
```
> Please review the API documentation at @docs:file://api/authentication
```
3
Multiple resource references
You can reference multiple resources in a single prompt:
```
> Compare @postgres:schema://users with @docs:file://database/user-model
```
Tips:
* Resources are automatically fetched and included as attachments when referenced
* Resource paths are fuzzy-searchable in the @ mention autocomplete
* Claude Code automatically provides tools to list and read MCP resources when servers support them
* Resources can contain any type of content that the MCP server provides (text, JSON, structured data, etc.)
## [​](#use-mcp-prompts-as-slash-commands) Use MCP prompts as slash commands
MCP servers can expose prompts that become available as slash commands in Claude Code.
### [​](#execute-mcp-prompts) Execute MCP prompts
1
Discover available prompts
Type `/` to see all available commands, including those from MCP servers. MCP prompts appear with the format `/mcp__servername__promptname`.
2
Execute a prompt without arguments
```
> /mcp__github__list_prs
```
3
Execute a prompt with arguments
Many prompts accept arguments. Pass them space-separated after the command:
```
> /mcp__github__pr_review 456
```
```
> /mcp__jira__create_issue "Bug in login flow" high
```
Tips:
* MCP prompts are dynamically discovered from connected servers
* Arguments are parsed based on the prompt’s defined parameters
* Prompt results are injected directly into the conversation
* Server and prompt names are normalized (spaces become underscores)
Was this page helpful?
YesNo
[GitHub Actions](/en/docs/claude-code/github-actions)[Troubleshooting](/en/docs/claude-code/troubleshooting)
On this page


---

## Memory

*Source: https://docs.anthropic.com/en/docs/claude-code/memory*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Configuration
Manage Claude's memory
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
Claude Code can remember your preferences across sessions, like style guidelines and common commands in your workflow.
## [​](#determine-memory-type) Determine memory type
Claude Code offers three memory locations, each serving a different purpose:
| Memory Type | Location | Purpose | Use Case Examples |
| --- | --- | --- | --- |
| **Project memory** | `./CLAUDE.md` | Team-shared instructions for the project | Project architecture, coding standards, common workflows |
| **User memory** | `~/.claude/CLAUDE.md` | Personal preferences for all projects | Code styling preferences, personal tooling shortcuts |
| **Project memory (local)** | `./CLAUDE.local.md` | Personal project-specific preferences | *(Deprecated, see below)* Your sandbox URLs, preferred test data |
All memory files are automatically loaded into Claude Code’s context when launched.
## [​](#claude-md-imports) CLAUDE.md imports
CLAUDE.md files can import additional files using `@path/to/import` syntax. The following example imports 3 files:
```
See @README for project overview and @package.json for available npm commands for this project.
# Additional Instructions
- git workflow @docs/git-instructions.md
```
Both relative and absolute paths are allowed. In particular, importing files in user’s home dir is a convenient way for your team members to provide individual instructions that are not checked into the repository. Previously CLAUDE.local.md served a similar purpose, but is now deprecated in favor of imports since they work better across multiple git worktrees.
```
# Individual Preferences
- @~/.claude/my-project-instructions.md
```
To avoid potential collisions, imports are not evaluated inside markdown code spans and code blocks.
```
This code span will not be treated as an import: `@anthropic-ai/claude-code`
```
Imported files can recursively import additional files, with a max-depth of 5 hops. You can see what memory files are loaded by running `/memory` command.
## [​](#how-claude-looks-up-memories) How Claude looks up memories
Claude Code reads memories recursively: starting in the cwd, Claude Code recurses up to (but not including) the root directory */* and reads any CLAUDE.md or CLAUDE.local.md files it finds. This is especially convenient when working in large repositories where you run Claude Code in *foo/bar/*, and have memories in both *foo/CLAUDE.md* and *foo/bar/CLAUDE.md*.
Claude will also discover CLAUDE.md nested in subtrees under your current working directory. Instead of loading them at launch, they are only included when Claude reads files in those subtrees.
## [​](#quickly-add-memories-with-the-%23-shortcut) Quickly add memories with the `#` shortcut
The fastest way to add a memory is to start your input with the `#` character:
```
# Always use descriptive variable names
```
You’ll be prompted to select which memory file to store this in.
## [​](#directly-edit-memories-with-%2Fmemory) Directly edit memories with `/memory`
Use the `/memory` slash command during a session to open any memory file in your system editor for more extensive additions or organization.
## [​](#set-up-project-memory) Set up project memory
Suppose you want to set up a CLAUDE.md file to store important project information, conventions, and frequently used commands.
Bootstrap a CLAUDE.md for your codebase with the following command:
```
> /init 
```
Tips:
* Include frequently used commands (build, test, lint) to avoid repeated searches
* Document code style preferences and naming conventions
* Add important architectural patterns specific to your project
* CLAUDE.md memories can be used for both instructions shared with your team and for your individual preferences.
## [​](#memory-best-practices) Memory best practices
* **Be specific**: “Use 2-space indentation” is better than “Format code properly”.
* **Use structure to organize**: Format each individual memory as a bullet point and group related memories under descriptive markdown headings.
* **Review periodically**: Update memories as your project evolves to ensure Claude is always using the most up to date information and context.
Was this page helpful?
YesNo
[Terminal configuration](/en/docs/claude-code/terminal-config)[CLI reference](/en/docs/claude-code/cli-reference)
On this page


---

## Monitoring Usage

*Source: https://docs.anthropic.com/en/docs/claude-code/monitoring-usage*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Administration
Monitoring
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
Claude Code supports OpenTelemetry (OTel) metrics and events for monitoring and observability.
All metrics are time series data exported via OpenTelemetry’s standard metrics protocol, and events are exported via OpenTelemetry’s logs/events protocol. It is the user’s responsibility to ensure their metrics and logs backends are properly configured and that the aggregation granularity meets their monitoring requirements.
OpenTelemetry support is currently in beta and details are subject to change.
## [​](#quick-start) Quick Start
Configure OpenTelemetry using environment variables:
```
# 1. Enable telemetry
export CLAUDE_CODE_ENABLE_TELEMETRY=1
# 2. Choose exporters (both are optional - configure only what you need)
export OTEL_METRICS_EXPORTER=otlp       # Options: otlp, prometheus, console
export OTEL_LOGS_EXPORTER=otlp          # Options: otlp, console
# 3. Configure OTLP endpoint (for OTLP exporter)
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
# 4. Set authentication (if required)
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer your-token"
# 5. For debugging: reduce export intervals
export OTEL_METRIC_EXPORT_INTERVAL=10000  # 10 seconds (default: 60000ms)
export OTEL_LOGS_EXPORT_INTERVAL=5000     # 5 seconds (default: 5000ms)
# 6. Run Claude Code
claude
```
The default export intervals are 60 seconds for metrics and 5 seconds for logs. During setup, you may want to use shorter intervals for debugging purposes. Remember to reset these for production use.
For full configuration options, see the [OpenTelemetry specification](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#configuration-options).
## [​](#administrator-configuration) Administrator Configuration
Administrators can configure OpenTelemetry settings for all users through the managed settings file. This allows for centralized control of telemetry settings across an organization. See the [settings precedence](/en/docs/claude-code/settings#settings-precedence) for more information about how settings are applied.
The managed settings file is located at:
* macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
* Linux and WSL: `/etc/claude-code/managed-settings.json`
* Windows: `C:\ProgramData\ClaudeCode\managed-settings.json`
Example managed settings configuration:
```
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_LOGS_EXPORTER": "otlp",
    "OTEL_EXPORTER_OTLP_PROTOCOL": "grpc",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "http://collector.company.com:4317",
    "OTEL_EXPORTER_OTLP_HEADERS": "Authorization=Bearer company-token"
  }
}
```
Managed settings can be distributed via MDM (Mobile Device Management) or other device management solutions. Environment variables defined in the managed settings file have high precedence and cannot be overridden by users.
## [​](#configuration-details) Configuration Details
### [​](#common-configuration-variables) Common Configuration Variables
| Environment Variable | Description | Example Values |
| --- | --- | --- |
| `CLAUDE_CODE_ENABLE_TELEMETRY` | Enables telemetry collection (required) | `1` |
| `OTEL_METRICS_EXPORTER` | Metrics exporter type(s) (comma-separated) | `console`, `otlp`, `prometheus` |
| `OTEL_LOGS_EXPORTER` | Logs/events exporter type(s) (comma-separated) | `console`, `otlp` |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | Protocol for OTLP exporter (all signals) | `grpc`, `http/json`, `http/protobuf` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP collector endpoint (all signals) | `http://localhost:4317` |
| `OTEL_EXPORTER_OTLP_METRICS_PROTOCOL` | Protocol for metrics (overrides general) | `grpc`, `http/json`, `http/protobuf` |
| `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` | OTLP metrics endpoint (overrides general) | `http://localhost:4318/v1/metrics` |
| `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL` | Protocol for logs (overrides general) | `grpc`, `http/json`, `http/protobuf` |
| `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` | OTLP logs endpoint (overrides general) | `http://localhost:4318/v1/logs` |
| `OTEL_EXPORTER_OTLP_HEADERS` | Authentication headers for OTLP | `Authorization=Bearer token` |
| `OTEL_EXPORTER_OTLP_METRICS_CLIENT_KEY` | Client key for mTLS authentication | Path to client key file |
| `OTEL_EXPORTER_OTLP_METRICS_CLIENT_CERTIFICATE` | Client certificate for mTLS authentication | Path to client cert file |
| `OTEL_METRIC_EXPORT_INTERVAL` | Export interval in milliseconds (default: 60000) | `5000`, `60000` |
| `OTEL_LOGS_EXPORT_INTERVAL` | Logs export interval in milliseconds (default: 5000) | `1000`, `10000` |
| `OTEL_LOG_USER_PROMPTS` | Enable logging of user prompt content (default: disabled) | `1` to enable |
### [​](#metrics-cardinality-control) Metrics Cardinality Control
The following environment variables control which attributes are included in metrics to manage cardinality:
| Environment Variable | Description | Default Value | Example to Disable |
| --- | --- | --- | --- |
| `OTEL_METRICS_INCLUDE_SESSION_ID` | Include session.id attribute in metrics | `true` | `false` |
| `OTEL_METRICS_INCLUDE_VERSION` | Include app.version attribute in metrics | `false` | `true` |
| `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` | Include user.account\_uuid attribute in metrics | `true` | `false` |
These variables help control the cardinality of metrics, which affects storage requirements and query performance in your metrics backend. Lower cardinality generally means better performance and lower storage costs but less granular data for analysis.
### [​](#dynamic-headers) Dynamic Headers
For enterprise environments that require dynamic authentication, you can configure a script to generate headers dynamically:
#### [​](#settings-configuration) Settings Configuration
Add to your `.claude/settings.json`:
```
{
  "otelHeadersHelper": "/bin/generate_opentelemetry_headers.sh"
}
```
#### [​](#script-requirements) Script Requirements
The script must output valid JSON with string key-value pairs representing HTTP headers:
```
#!/bin/bash
# Example: Multiple headers
echo "{\"Authorization\": \"Bearer $(get-token.sh)\", \"X-API-Key\": \"$(get-api-key.sh)\"}"
```
#### [​](#important-limitations) Important Limitations
**Headers are fetched only at startup, not during runtime.** This is due to OpenTelemetry exporter architecture limitations.
For scenarios requiring frequent token refresh, use an OpenTelemetry Collector as a proxy that can refresh its own headers.
### [​](#multi-team-organization-support) Multi-Team Organization Support
Organizations with multiple teams or departments can add custom attributes to distinguish between different groups using the `OTEL_RESOURCE_ATTRIBUTES` environment variable:
```
# Add custom attributes for team identification
export OTEL_RESOURCE_ATTRIBUTES="department=engineering,team.id=platform,cost_center=eng-123"
```
These custom attributes will be included in all metrics and events, allowing you to:
* Filter metrics by team or department
* Track costs per cost center
* Create team-specific dashboards
* Set up alerts for specific teams
### [​](#example-configurations) Example Configurations
```
# Console debugging (1-second intervals)
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=console
export OTEL_METRIC_EXPORT_INTERVAL=1000
# OTLP/gRPC
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
# Prometheus
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=prometheus
# Multiple exporters
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=console,otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=http/json
# Different endpoints/backends for metrics and logs
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_METRICS_PROTOCOL=http/protobuf
export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT=http://metrics.company.com:4318
export OTEL_EXPORTER_OTLP_LOGS_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=http://logs.company.com:4317
# Metrics only (no events/logs)
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
# Events/logs only (no metrics)
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```
## [​](#available-metrics-and-events) Available Metrics and Events
### [​](#standard-attributes) Standard Attributes
All metrics and events share these standard attributes:
| Attribute | Description | Controlled By |
| --- | --- | --- |
| `session.id` | Unique session identifier | `OTEL_METRICS_INCLUDE_SESSION_ID` (default: true) |
| `app.version` | Current Claude Code version | `OTEL_METRICS_INCLUDE_VERSION` (default: false) |
| `organization.id` | Organization UUID (when authenticated) | Always included when available |
| `user.account_uuid` | Account UUID (when authenticated) | `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` (default: true) |
| `terminal.type` | Terminal type (e.g., `iTerm.app`, `vscode`, `cursor`, `tmux`) | Always included when detected |
### [​](#metrics) Metrics
Claude Code exports the following metrics:
| Metric Name | Description | Unit |
| --- | --- | --- |
| `claude_code.session.count` | Count of CLI sessions started | count |
| `claude_code.lines_of_code.count` | Count of lines of code modified | count |
| `claude_code.pull_request.count` | Number of pull requests created | count |
| `claude_code.commit.count` | Number of git commits created | count |
| `claude_code.cost.usage` | Cost of the Claude Code session | USD |
| `claude_code.token.usage` | Number of tokens used | tokens |
| `claude_code.code_edit_tool.decision` | Count of code editing tool permission decisions | count |
| `claude_code.active_time.total` | Total active time in seconds | s |
### [​](#metric-details) Metric Details
#### [​](#session-counter) Session Counter
Incremented at the start of each session.
**Attributes**:
* All [standard attributes](/_sites/docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
#### [​](#lines-of-code-counter) Lines of Code Counter
Incremented when code is added or removed.
**Attributes**:
* All [standard attributes](/_sites/docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
* `type`: (`"added"`, `"removed"`)
#### [​](#pull-request-counter) Pull Request Counter
Incremented when creating pull requests via Claude Code.
**Attributes**:
* All [standard attributes](/_sites/docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
#### [​](#commit-counter) Commit Counter
Incremented when creating git commits via Claude Code.
**Attributes**:
* All [standard attributes](/_sites/docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
#### [​](#cost-counter) Cost Counter
Incremented after each API request.
**Attributes**:
* All [standard attributes](/_sites/docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
* `model`: Model identifier (e.g., “claude-3-5-sonnet-20241022”)
#### [​](#token-counter) Token Counter
Incremented after each API request.
**Attributes**:
* All [standard attributes](/_sites/docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
* `type`: (`"input"`, `"output"`, `"cacheRead"`, `"cacheCreation"`)
* `model`: Model identifier (e.g., “claude-3-5-sonnet-20241022”)
#### [​](#code-edit-tool-decision-counter) Code Edit Tool Decision Counter
Incremented when user accepts or rejects Edit, MultiEdit, Write, or NotebookEdit tool usage.
**Attributes**:
* All [standard attributes](/_sites/docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
* `tool`: Tool name (`"Edit"`, `"MultiEdit"`, `"Write"`, `"NotebookEdit"`)
* `decision`: User decision (`"accept"`, `"reject"`)
* `language`: Programming language of the edited file (e.g., `"TypeScript"`, `"Python"`, `"JavaScript"`, `"Markdown"`). Returns `"unknown"` for unrecognized file extensions.
#### [​](#active-time-counter) Active Time Counter
Tracks actual time spent actively using Claude Code (not idle time). This metric is incremented during user interactions such as typing prompts or receiving responses.
**Attributes**:
* All [standard attributes](/_sites/docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
### [​](#events) Events
Claude Code exports the following events via OpenTelemetry logs/events (when `OTEL_LOGS_EXPORTER` is configured):
#### [​](#user-prompt-event) User Prompt Event
Logged when a user submits a prompt.
**Event Name**: `claude_code.user_prompt`
**Attributes**:
* All [standard attributes](/_sites/docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
* `event.name`: `"user_prompt"`
* `event.timestamp`: ISO 8601 timestamp
* `prompt_length`: Length of the prompt
* `prompt`: Prompt content (redacted by default, enable with `OTEL_LOG_USER_PROMPTS=1`)
#### [​](#tool-result-event) Tool Result Event
Logged when a tool completes execution.
**Event Name**: `claude_code.tool_result`
**Attributes**:
* All [standard attributes](/_sites/docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
* `event.name`: `"tool_result"`
* `event.timestamp`: ISO 8601 timestamp
* `tool_name`: Name of the tool
* `success`: `"true"` or `"false"`
* `duration_ms`: Execution time in milliseconds
* `error`: Error message (if failed)
* `decision`: Either `"accept"` or `"reject"`
* `source`: Decision source - `"config"`, `"user_permanent"`, `"user_temporary"`, `"user_abort"`, or `"user_reject"`
* `tool_parameters`: JSON string containing tool-specific parameters (when available)
  + For Bash tool: includes `bash_command`, `full_command`, `timeout`, `description`, `sandbox`
#### [​](#api-request-event) API Request Event
Logged for each API request to Claude.
**Event Name**: `claude_code.api_request`
**Attributes**:
* All [standard attributes](/_sites/docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
* `event.name`: `"api_request"`
* `event.timestamp`: ISO 8601 timestamp
* `model`: Model used (e.g., “claude-3-5-sonnet-20241022”)
* `cost_usd`: Estimated cost in USD
* `duration_ms`: Request duration in milliseconds
* `input_tokens`: Number of input tokens
* `output_tokens`: Number of output tokens
* `cache_read_tokens`: Number of tokens read from cache
* `cache_creation_tokens`: Number of tokens used for cache creation
#### [​](#api-error-event) API Error Event
Logged when an API request to Claude fails.
**Event Name**: `claude_code.api_error`
**Attributes**:
* All [standard attributes](/_sites/docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
* `event.name`: `"api_error"`
* `event.timestamp`: ISO 8601 timestamp
* `model`: Model used (e.g., “claude-3-5-sonnet-20241022”)
* `error`: Error message
* `status_code`: HTTP status code (if applicable)
* `duration_ms`: Request duration in milliseconds
* `attempt`: Attempt number (for retried requests)
#### [​](#tool-decision-event) Tool Decision Event
Logged when a tool permission decision is made (accept/reject).
**Event Name**: `claude_code.tool_decision`
**Attributes**:
* All [standard attributes](/_sites/docs.anthropic.com/en/docs/claude-code/monitoring-usage#standard-attributes)
* `event.name`: `"tool_decision"`
* `event.timestamp`: ISO 8601 timestamp
* `tool_name`: Name of the tool (e.g., “Read”, “Edit”, “MultiEdit”, “Write”, “NotebookEdit”, etc.)
* `decision`: Either `"accept"` or `"reject"`
* `source`: Decision source - `"config"`, `"user_permanent"`, `"user_temporary"`, `"user_abort"`, or `"user_reject"`
## [​](#interpreting-metrics-and-events-data) Interpreting Metrics and Events Data
The metrics exported by Claude Code provide valuable insights into usage patterns and productivity. Here are some common visualizations and analyses you can create:
### [​](#usage-monitoring) Usage Monitoring
| Metric | Analysis Opportunity |
| --- | --- |
| `claude_code.token.usage` | Break down by `type` (input/output), user, team, or model |
| `claude_code.session.count` | Track adoption and engagement over time |
| `claude_code.lines_of_code.count` | Measure productivity by tracking code additions/removals |
| `claude_code.commit.count` & `claude_code.pull_request.count` | Understand impact on development workflows |
### [​](#cost-monitoring) Cost Monitoring
The `claude_code.cost.usage` metric helps with:
* Tracking usage trends across teams or individuals
* Identifying high-usage sessions for optimization
Cost metrics are approximations. For official billing data, refer to your API provider (Anthropic Console, AWS Bedrock, or Google Cloud Vertex).
### [​](#alerting-and-segmentation) Alerting and Segmentation
Common alerts to consider:
* Cost spikes
* Unusual token consumption
* High session volume from specific users
All metrics can be segmented by `user.account_uuid`, `organization.id`, `session.id`, `model`, and `app.version`.
### [​](#event-analysis) Event Analysis
The event data provides detailed insights into Claude Code interactions:
**Tool Usage Patterns**: Analyze tool result events to identify:
* Most frequently used tools
* Tool success rates
* Average tool execution times
* Error patterns by tool type
**Performance Monitoring**: Track API request durations and tool execution times to identify performance bottlenecks.
## [​](#backend-considerations) Backend Considerations
Your choice of metrics and logs backends will determine the types of analyses you can perform:
### [​](#for-metrics%3A) For Metrics:
* **Time series databases (e.g., Prometheus)**: Rate calculations, aggregated metrics
* **Columnar stores (e.g., ClickHouse)**: Complex queries, unique user analysis
* **Full-featured observability platforms (e.g., Honeycomb, Datadog)**: Advanced querying, visualization, alerting
### [​](#for-events%2Flogs%3A) For Events/Logs:
* **Log aggregation systems (e.g., Elasticsearch, Loki)**: Full-text search, log analysis
* **Columnar stores (e.g., ClickHouse)**: Structured event analysis
* **Full-featured observability platforms (e.g., Honeycomb, Datadog)**: Correlation between metrics and events
For organizations requiring Daily/Weekly/Monthly Active User (DAU/WAU/MAU) metrics, consider backends that support efficient unique value queries.
## [​](#service-information) Service Information
All metrics and events are exported with the following resource attributes:
* `service.name`: `claude-code`
* `service.version`: Current Claude Code version
* `os.type`: Operating system type (e.g., `linux`, `darwin`, `windows`)
* `os.version`: Operating system version string
* `host.arch`: Host architecture (e.g., `amd64`, `arm64`)
* `wsl.version`: WSL version number (only present when running on Windows Subsystem for Linux)
* Meter Name: `com.anthropic.claude_code`
## [​](#security%2Fprivacy-considerations) Security/Privacy Considerations
* Telemetry is opt-in and requires explicit configuration
* Sensitive information like API keys or file contents are never included in metrics or events
* User prompt content is redacted by default - only prompt length is recorded. To enable user prompt logging, set `OTEL_LOG_USER_PROMPTS=1`
Was this page helpful?
YesNo
[Security](/en/docs/claude-code/security)[Costs](/en/docs/claude-code/costs)
On this page


---

## Overview

*Source: https://docs.anthropic.com/en/docs/claude-code/overview*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Getting started
Claude Code overview
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
## [​](#get-started-in-30-seconds) Get started in 30 seconds
Prerequisites: [Node.js 18 or newer](https://nodejs.org/en/download/)
```
# Install Claude Code
npm install -g @anthropic-ai/claude-code
# Navigate to your project
cd your-awesome-project
# Start coding with Claude
claude
```
That’s it! You’re ready to start coding with Claude. [Continue with Quickstart (5 mins) →](/en/docs/claude-code/quickstart)
(Got specific setup needs or hit issues? See [advanced setup](/en/docs/claude-code/setup) or [troubleshooting](/en/docs/claude-code/troubleshooting).)
## [​](#what-claude-code-does-for-you) What Claude Code does for you
* **Build features from descriptions**: Tell Claude what you want to build in plain English. It will make a plan, write the code, and ensure it works.
* **Debug and fix issues**: Describe a bug or paste an error message. Claude Code will analyze your codebase, identify the problem, and implement a fix.
* **Navigate any codebase**: Ask anything about your team’s codebase, and get a thoughtful answer back. Claude Code maintains awareness of your entire project structure, can find up-to-date information from the web, and with [MCP](/en/docs/claude-code/mcp) can pull from external datasources like Google Drive, Figma, and Slack.
* **Automate tedious tasks**: Fix fiddly lint issues, resolve merge conflicts, and write release notes. Do all this in a single command from your developer machines, or automatically in CI.
## [​](#why-developers-love-claude-code) Why developers love Claude Code
* **Works in your terminal**: Not another chat window. Not another IDE. Claude Code meets you where you already work, with the tools you already love.
* **Takes action**: Claude Code can directly edit files, run commands, and create commits. Need more? [MCP](/en/docs/claude-code/mcp) lets Claude read your design docs in Google Drive, update your tickets in Jira, or use *your* custom developer tooling.
* **Unix philosophy**: Claude Code is composable and scriptable. `tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"` *works*. Your CI can run `claude -p "If there are new text strings, translate them into French and raise a PR for @lang-fr-team to review"`.
* **Enterprise-ready**: Use Anthropic’s API, or host on AWS or GCP. Enterprise-grade [security](/en/docs/claude-code/security), [privacy](/en/docs/claude-code/data-usage), and [compliance](https://trust.anthropic.com/) is built-in.
## [​](#next-steps) Next steps
[## Quickstart
See Claude Code in action with practical examples](/en/docs/claude-code/quickstart)[## Common workflows
Step-by-step guides for common workflows](/en/docs/claude-code/common-workflows)[## Troubleshooting
Solutions for common issues with Claude Code](/en/docs/claude-code/troubleshooting)[## IDE setup
Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
## [​](#additional-resources) Additional resources
[## Host on AWS or GCP
Configure Claude Code with Amazon Bedrock or Google Vertex AI](/en/docs/claude-code/third-party-integrations)[## Settings
Customize Claude Code for your workflow](/en/docs/claude-code/settings)[## Commands
Learn about CLI commands and controls](/en/docs/claude-code/cli-reference)[## Reference implementation
Clone our development container reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer)[## Security
Discover Claude Code’s safeguards and best practices for safe usage](/en/docs/claude-code/security)[## Privacy and data usage
Understand how Claude Code handles your data](/en/docs/claude-code/data-usage)
Was this page helpful?
YesNo
[Quickstart](/en/docs/claude-code/quickstart)
On this page


---

## Quickstart

*Source: https://docs.anthropic.com/en/docs/claude-code/quickstart*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Getting started
Quickstart
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
This quickstart guide will have you using AI-powered coding assistance in just a few minutes. By the end, you’ll understand how to use Claude Code for common development tasks.
## [​](#before-you-begin) Before you begin
Make sure you have:
* A terminal or command prompt open
* [Node.js 18 or newer installed](https://nodejs.org/en/download/)
* A code project to work with
## [​](#step-1%3A-install-claude-code) Step 1: Install Claude Code
To install Claude Code, run the following command:
```
npm install -g @anthropic-ai/claude-code
```
## [​](#step-2%3A-start-your-first-session) Step 2: Start your first session
Open your terminal in any project directory and start Claude Code:
```
cd /path/to/your/project
claude
```
You’ll see the Claude Code prompt inside a new interactive session:
```
✻ Welcome to Claude Code!
...
> Try "create a util logging.py that..." 
```
## [​](#step-3%3A-ask-your-first-question) Step 3: Ask your first question
Let’s start with understanding your codebase. Try one of these commands:
```
> what does this project do?
```
Claude will analyze your files and provide a summary. You can also ask more specific questions:
```
> what technologies does this project use?
```
```
> where is the main entry point?
```
```
> explain the folder structure
```
Claude Code reads your files as needed - you don’t have to manually add context.
## [​](#step-4%3A-make-your-first-code-change) Step 4: Make your first code change
Now let’s make Claude Code do some actual coding. Try a simple task:
```
> add a hello world function to the main file
```
Claude Code will:
1. Find the appropriate file
2. Show you the proposed changes
3. Ask for your approval
4. Make the edit
Claude Code always asks for permission before modifying files. You can approve individual changes or enable “Accept all” mode for a session.
## [​](#step-5%3A-use-git-with-claude-code) Step 5: Use Git with Claude Code
Claude Code makes Git operations conversational:
```
> what files have I changed?
```
```
> commit my changes with a descriptive message
```
You can also prompt for more complex Git operations:
```
> create a new branch called feature/quickstart
```
```
> show me the last 5 commits
```
```
> help me resolve merge conflicts
```
## [​](#step-6%3A-fix-a-bug-or-add-a-feature) Step 6: Fix a bug or add a feature
Claude is proficient at debugging and feature implementation.
Describe what you want in natural language:
```
> add input validation to the user registration form
```
Or fix existing issues:
```
> there's a bug where users can submit empty forms - fix it
```
Claude Code will:
* Locate the relevant code
* Understand the context
* Implement a solution
* Run tests if available
## [​](#step-7%3A-test-out-other-common-workflows) Step 7: Test out other common workflows
There are a number of ways to work with Claude:
**Refactor code**
```
> refactor the authentication module to use async/await instead of callbacks
```
**Write tests**
```
> write unit tests for the calculator functions
```
**Update documentation**
```
> update the README with installation instructions
```
**Code review**
```
> review my changes and suggest improvements
```
**Remember**: Claude Code is your AI pair programmer. Talk to it like you would a helpful colleague - describe what you want to achieve, and it will help you get there.
## [​](#essential-commands) Essential commands
Here are the most important commands for daily use:
| Command | What it does | Example |
| --- | --- | --- |
| `claude` | Start interactive mode | `claude` |
| `claude "task"` | Run a one-time task | `claude "fix the build error"` |
| `claude -p "query"` | Run one-off query, then exit | `claude -p "explain this function"` |
| `claude -c` | Continue most recent conversation | `claude -c` |
| `claude -r` | Resume a previous conversation | `claude -r` |
| `claude commit` | Create a Git commit | `claude commit` |
| `/clear` | Clear conversation history | `> /clear` |
| `/help` | Show available commands | `> /help` |
| `exit` or Ctrl+C | Exit Claude Code | `> exit` |
See the [CLI reference](/en/docs/claude-code/cli-reference) for a complete list of commands.
## [​](#pro-tips-for-beginners) Pro tips for beginners
Be specific with your requests
Instead of: “fix the bug”
Try: “fix the login bug where users see a blank screen after entering wrong credentials”
Use step-by-step instructions
Break complex tasks into steps:
```
> 1. create a new database table for user profiles
```
```
> 2. create an API endpoint to get and update user profiles
```
```
> 3. build a webpage that allows users to see and edit their information
```
Let Claude explore first
Before making changes, let Claude understand your code:
```
> analyze the database schema
```
```
> build a dashboard showing products that are most frequently returned by our UK customers
```
Save time with shortcuts
* Use Tab for command completion
* Press ↑ for command history
* Type `/` to see all slash commands
## [​](#what%E2%80%99s-next%3F) What’s next?
Now that you’ve learned the basics, explore more advanced features:
[## Common workflows
Step-by-step guides for common tasks](/en/docs/claude-code/common-workflows)[## CLI reference
Master all commands and options](/en/docs/claude-code/cli-reference)[## Configuration
Customize Claude Code for your workflow](/en/docs/claude-code/settings)
## [​](#getting-help) Getting help
* **In Claude Code**: Type `/help` or ask “how do I…”
* **Documentation**: You’re here! Browse other guides
* **Community**: Join our [Discord](https://www.anthropic.com/discord) for tips and support
Was this page helpful?
YesNo
[Overview](/en/docs/claude-code/overview)[Common workflows](/en/docs/claude-code/common-workflows)
On this page


---

## Sdk

*Source: https://docs.anthropic.com/en/docs/claude-code/sdk*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Build with Claude Code
Claude Code SDK
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
The Claude Code SDK enables running Claude Code as a subprocess, providing a way to build AI-powered coding assistants and tools that leverage Claude’s capabilities.
The SDK is available for command line, TypeScript, and Python usage.
## [​](#authentication) Authentication
The Claude Code SDK supports multiple authentication methods:
### [​](#anthropic-api-key) Anthropic API key
To use the Claude Code SDK directly with Anthropic’s API, we recommend creating a dedicated API key:
1. Create an Anthropic API key in the [Anthropic Console](https://console.anthropic.com/)
2. Then, set the `ANTHROPIC_API_KEY` environment variable. We recommend storing this key securely (e.g., using a Github [secret](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions))
### [​](#third-party-api-credentials) Third-Party API credentials
The SDK also supports third-party API providers:
* **Amazon Bedrock**: Set `CLAUDE_CODE_USE_BEDROCK=1` environment variable and configure AWS credentials
* **Google Vertex AI**: Set `CLAUDE_CODE_USE_VERTEX=1` environment variable and configure Google Cloud credentials
For detailed configuration instructions for third-party providers, see the [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock) and [Google Vertex AI](/en/docs/claude-code/google-vertex-ai) documentation.
## [​](#basic-sdk-usage) Basic SDK usage
The Claude Code SDK allows you to use Claude Code in non-interactive mode from your applications.
### [​](#command-line) Command line
Here are a few basic examples for the command line SDK:
```
# Run a single prompt and exit (print mode)
$ claude -p "Write a function to calculate Fibonacci numbers"
# Using a pipe to provide stdin
$ echo "Explain this code" | claude -p
# Output in JSON format with metadata
$ claude -p "Generate a hello world function" --output-format json
# Stream JSON output as it arrives
$ claude -p "Build a React component" --output-format stream-json
```
### [​](#typescript) TypeScript
The TypeScript SDK is included in the main [`@anthropic-ai/claude-code`](https://www.npmjs.com/package/@anthropic-ai/claude-code) package on NPM:
```
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
The TypeScript SDK accepts all arguments supported by the command line SDK, as well as:
| Argument | Description | Default |
| --- | --- | --- |
| `abortController` | Abort controller | `new AbortController()` |
| `cwd` | Current working directory | `process.cwd()` |
| `executable` | Which JavaScript runtime to use | `node` when running with Node.js, `bun` when running with Bun |
| `executableArgs` | Arguments to pass to the executable | `[]` |
| `pathToClaudeCodeExecutable` | Path to the Claude Code executable | Executable that ships with `@anthropic-ai/claude-code` |
### [​](#python) Python
The Python SDK is available as [`claude-code-sdk`](https://github.com/anthropics/claude-code-sdk-python) on PyPI:
```
pip install claude-code-sdk
```
**Prerequisites:**
* Python 3.10+
* Node.js
* Claude Code CLI: `npm install -g @anthropic-ai/claude-code`
Basic usage:
```
import anyio
from claude_code_sdk import query, ClaudeCodeOptions, Message
async def main():
    messages: list[Message] = []
    async for message in query(
        prompt="Write a haiku about foo.py",
        options=ClaudeCodeOptions(max_turns=3)
    ):
        messages.append(message)
    print(messages)
anyio.run(main)
```
The Python SDK accepts all arguments supported by the command line SDK through the `ClaudeCodeOptions` class:
```
from claude_code_sdk import query, ClaudeCodeOptions
from pathlib import Path
options = ClaudeCodeOptions(
    max_turns=3,
    system_prompt="You are a helpful assistant",
    cwd=Path("/path/to/project"),  # Can be string or Path
    allowed_tools=["Read", "Write", "Bash"],
    permission_mode="acceptEdits"
)
async for message in query(prompt="Hello", options=options):
    print(message)
```
## [​](#advanced-usage) Advanced usage
The documentation below uses the command line SDK as an example, but can also be used with the TypeScript and Python SDKs.
### [​](#multi-turn-conversations) Multi-turn conversations
For multi-turn conversations, you can resume conversations or continue from the most recent session:
```
# Continue the most recent conversation
$ claude --continue
# Continue and provide a new prompt
$ claude --continue "Now refactor this for better performance"
# Resume a specific conversation by session ID
$ claude --resume 550e8400-e29b-41d4-a716-446655440000
# Resume in print mode (non-interactive)
$ claude -p --resume 550e8400-e29b-41d4-a716-446655440000 "Update the tests"
# Continue in print mode (non-interactive)
$ claude -p --continue "Add error handling"
```
### [​](#custom-system-prompts) Custom system prompts
You can provide custom system prompts to guide Claude’s behavior:
```
# Override system prompt (only works with --print)
$ claude -p "Build a REST API" --system-prompt "You are a senior backend engineer. Focus on security, performance, and maintainability."
# System prompt with specific requirements
$ claude -p "Create a database schema" --system-prompt "You are a database architect. Use PostgreSQL best practices and include proper indexing."
```
You can also append instructions to the default system prompt:
```
# Append system prompt (only works with --print)
$ claude -p "Build a REST API" --append-system-prompt "After writing code, be sure to code review yourself."
```
### [​](#mcp-configuration) MCP Configuration
The Model Context Protocol (MCP) allows you to extend Claude Code with additional tools and resources from external servers. Using the `--mcp-config` flag, you can load MCP servers that provide specialized capabilities like database access, API integrations, or custom tooling.
Create a JSON configuration file with your MCP servers:
```
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/files"
      ]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your-github-token"
      }
    }
  }
}
```
Then use it with Claude Code:
```
# Load MCP servers from configuration
$ claude -p "List all files in the project" --mcp-config mcp-servers.json
# Important: MCP tools must be explicitly allowed using --allowedTools
# MCP tools follow the format: mcp__$serverName__$toolName
$ claude -p "Search for TODO comments" \
  --mcp-config mcp-servers.json \
  --allowedTools "mcp__filesystem__read_file,mcp__filesystem__list_directory"
# Use an MCP tool for handling permission prompts in non-interactive mode
$ claude -p "Deploy the application" \
  --mcp-config mcp-servers.json \
  --allowedTools "mcp__permissions__approve" \
  --permission-prompt-tool mcp__permissions__approve
```
When using MCP tools, you must explicitly allow them using the `--allowedTools` flag. MCP tool names follow the pattern `mcp__<serverName>__<toolName>` where:
* `serverName` is the key from your MCP configuration file
* `toolName` is the specific tool provided by that server
This security measure ensures that MCP tools are only used when explicitly permitted.
If you specify just the server name (i.e., `mcp__<serverName>`), all tools from that server will be allowed.
Glob patterns (e.g., `mcp__go*`) are not supported.
### [​](#custom-permission-prompt-tool) Custom permission prompt tool
Optionally, use `--permission-prompt-tool` to pass in an MCP tool that we will use to check whether or not the user grants the model permissions to invoke a given tool. When the model invokes a tool the following happens:
1. We first check permission settings: all [settings.json files](/en/docs/claude-code/settings), as well as `--allowedTools` and `--disallowedTools` passed into the SDK; if one of these allows or denies the tool call, we proceed with the tool call
2. Otherwise, we invoke the MCP tool you provided in `--permission-prompt-tool`
The `--permission-prompt-tool` MCP tool is passed the tool name and input, and must return a JSON-stringified payload with the result. The payload must be one of:
```
// tool call is allowed
{
  "behavior": "allow",
  "updatedInput": {...}, // updated input, or just return back the original input
}
// tool call is denied
{
  "behavior": "deny",
  "message": "..." // human-readable string explaining why the permission was denied
}
```
For example, a TypeScript MCP permission prompt tool implementation might look like this:
```
const server = new McpServer({
  name: "Test permission prompt MCP Server",
  version: "0.0.1",
});
server.tool(
  "approval_prompt",
  'Simulate a permission check - approve if the input contains "allow", otherwise deny',
  {
    tool_name: z.string().describe("The name of the tool requesting permission"),
    input: z.object({}).passthrough().describe("The input for the tool"),
    tool_use_id: z.string().optional().describe("The unique tool use request ID"),
  },
  async ({ tool_name, input }) => {
    return {
      content: [
        {
          type: "text",
          text: JSON.stringify(
            JSON.stringify(input).includes("allow")
              ? {
                  behavior: "allow",
                  updatedInput: input,
                }
              : {
                  behavior: "deny",
                  message: "Permission denied by test approval_prompt tool",
                }
          ),
        },
      ],
    };
  }
);
```
To use this tool, add your MCP server (eg. with `--mcp-config`), then invoke the SDK like so:
```
claude -p "..." \
  --permission-prompt-tool mcp__test-server__approval_prompt \
  --mcp-config my-config.json
```
Usage notes:
* Use `updatedInput` to tell the model that the permission prompt mutated its input; otherwise, set `updatedInput` to the original input, as in the example above. For example, if the tool shows a file edit diff to the user and lets them edit the diff manually, the permission prompt tool should return that updated edit.
* The payload must be JSON-stringified
## [​](#available-cli-options) Available CLI options
The SDK leverages all the CLI options available in Claude Code. Here are the key ones for SDK usage:
| Flag | Description | Example |
| --- | --- | --- |
| `--print`, `-p` | Run in non-interactive mode | `claude -p "query"` |
| `--output-format` | Specify output format (`text`, `json`, `stream-json`) | `claude -p --output-format json` |
| `--resume`, `-r` | Resume a conversation by session ID | `claude --resume abc123` |
| `--continue`, `-c` | Continue the most recent conversation | `claude --continue` |
| `--verbose` | Enable verbose logging | `claude --verbose` |
| `--max-turns` | Limit agentic turns in non-interactive mode | `claude --max-turns 3` |
| `--system-prompt` | Override system prompt (only with `--print`) | `claude --system-prompt "Custom instruction"` |
| `--append-system-prompt` | Append to system prompt (only with `--print`) | `claude --append-system-prompt "Custom instruction"` |
| `--allowedTools` | Space-separated list of allowed tools, or  string of comma-separated list of allowed tools | `claude --allowedTools mcp__slack mcp__filesystem``claude --allowedTools "Bash(npm install),mcp__filesystem"` |
| `--disallowedTools` | Space-separated list of denied tools, or  string of comma-separated list of denied tools | `claude --disallowedTools mcp__splunk mcp__github``claude --disallowedTools "Bash(git commit),mcp__github"` |
| `--mcp-config` | Load MCP servers from a JSON file | `claude --mcp-config servers.json` |
| `--permission-prompt-tool` | MCP tool for handling permission prompts (only with `--print`) | `claude --permission-prompt-tool mcp__auth__prompt` |
For a complete list of CLI options and features, see the [CLI reference](/en/docs/claude-code/cli-reference) documentation.
## [​](#output-formats) Output formats
The SDK supports multiple output formats:
### [​](#text-output-default) Text output (default)
Returns just the response text:
```
$ claude -p "Explain file src/components/Header.tsx"
# Output: This is a React component showing...
```
### [​](#json-output) JSON output
Returns structured data including metadata:
```
$ claude -p "How does the data layer work?" --output-format json
```
Response format:
```
{
  "type": "result",
  "subtype": "success",
  "total_cost_usd": 0.003,
  "is_error": false,
  "duration_ms": 1234,
  "duration_api_ms": 800,
  "num_turns": 6,
  "result": "The response text here...",
  "session_id": "abc123"
}
```
### [​](#streaming-json-output) Streaming JSON output
Streams each message as it is received:
```
$ claude -p "Build an application" --output-format stream-json
```
Each conversation begins with an initial `init` system message, followed by a list of user and assistant messages, followed by a final `result` system message with stats. Each message is emitted as a separate JSON object.
## [​](#message-schema) Message schema
Messages returned from the JSON API are strictly typed according to the following schema:
```
type SDKMessage =
  // An assistant message
  | {
      type: "assistant";
      message: Message; // from Anthropic SDK
      session_id: string;
    }
  // A user message
  | {
      type: "user";
      message: MessageParam; // from Anthropic SDK
      session_id: string;
    }
  // Emitted as the last message
  | {
      type: "result";
      subtype: "success";
      duration_ms: float;
      duration_api_ms: float;
      is_error: boolean;
      num_turns: int;
      result: string;
      session_id: string;
      total_cost_usd: float;
    }
  // Emitted as the last message, when we've reached the maximum number of turns
  | {
      type: "result";
      subtype: "error_max_turns" | "error_during_execution";
      duration_ms: float;
      duration_api_ms: float;
      is_error: boolean;
      num_turns: int;
      session_id: string;
      total_cost_usd: float;
    }
  // Emitted as the first message at the start of a conversation
  | {
      type: "system";
      subtype: "init";
      apiKeySource: string;
      cwd: string;
      session_id: string;
      tools: string[];
      mcp_servers: {
        name: string;
        status: string;
      }[];
      model: string;
      permissionMode: "default" | "acceptEdits" | "bypassPermissions" | "plan";
    };
```
We will soon publish these types in a JSONSchema-compatible format. We use semantic versioning for the main Claude Code package to communicate breaking changes to this format.
`Message` and `MessageParam` types are available in Anthropic SDKs. For example, see the Anthropic [TypeScript](https://github.com/anthropics/anthropic-sdk-typescript) and [Python](https://github.com/anthropics/anthropic-sdk-python/) SDKs.
## [​](#input-formats) Input formats
The SDK supports multiple input formats:
### [​](#text-input-default) Text input (default)
Input text can be provided as an argument:
```
$ claude -p "Explain this code"
```
Or input text can be piped via stdin:
```
$ echo "Explain this code" | claude -p
```
### [​](#streaming-json-input) Streaming JSON input
A stream of messages provided via `stdin` where each message represents a user turn. This allows multiple turns of a conversation without re-launching the `claude` binary and allows providing guidance to the model while it is processing a request.
Each message is a JSON ‘User message’ object, following the same format as the output message schema. Messages are formatted using the [jsonl](https://jsonlines.org/) format where each line of input is a complete JSON object. Streaming JSON input requires `-p` and `--output-format stream-json`.
Currently this is limited to text-only user messages.
```
$ echo '{"type":"user","message":{"role":"user","content":[{"type":"text","text":"Explain this code"}]}}' | claude -p --output-format=stream-json --input-format=stream-json --verbose
```
## [​](#examples) Examples
### [​](#simple-script-integration) Simple script integration
```
#!/bin/bash
# Simple function to run Claude and check exit code
run_claude() {
    local prompt="$1"
    local output_format="${2:-text}"
    if claude -p "$prompt" --output-format "$output_format"; then
        echo "Success!"
    else
        echo "Error: Claude failed with exit code $?" >&2
        return 1
    fi
}
# Usage examples
run_claude "Write a Python function to read CSV files"
run_claude "Optimize this database query" "json"
```
### [​](#processing-files-with-claude) Processing files with Claude
```
# Process a file through Claude
$ cat mycode.py | claude -p "Review this code for bugs"
# Process multiple files
$ for file in *.js; do
    echo "Processing $file..."
    claude -p "Add JSDoc comments to this file:" < "$file" > "${file}.documented"
done
# Use Claude in a pipeline
$ grep -l "TODO" *.py | while read file; do
    claude -p "Fix all TODO items in this file" < "$file"
done
```
### [​](#session-management) Session management
```
# Start a session and capture the session ID
$ claude -p "Initialize a new project" --output-format json | jq -r '.session_id' > session.txt
# Continue with the same session
$ claude -p --resume "$(cat session.txt)" "Add unit tests"
```
## [​](#best-practices) Best practices
1. **Use JSON output format** for programmatic parsing of responses:
   ```
   # Parse JSON response with jq
   result=$(claude -p "Generate code" --output-format json)
   code=$(echo "$result" | jq -r '.result')
   cost=$(echo "$result" | jq -r '.cost_usd')
   ```
2. **Handle errors gracefully** - check exit codes and stderr:
   ```
   if ! claude -p "$prompt" 2>error.log; then
       echo "Error occurred:" >&2
       cat error.log >&2
       exit 1
   fi
   ```
3. **Use session management** for maintaining context in multi-turn conversations
4. **Consider timeouts** for long-running operations:
   ```
   timeout 300 claude -p "$complex_prompt" || echo "Timed out after 5 minutes"
   ```
5. **Respect rate limits** when making multiple requests by adding delays between calls
## [​](#real-world-applications) Real-world applications
The Claude Code SDK enables powerful integrations with your development workflow. One notable example is the [Claude Code GitHub Actions](/en/docs/claude-code/github-actions), which uses the SDK to provide automated code review, PR creation, and issue triage capabilities directly in your GitHub workflow.
## [​](#related-resources) Related resources
* [CLI usage and controls](/en/docs/claude-code/cli-reference) - Complete CLI documentation
* [GitHub Actions integration](/en/docs/claude-code/github-actions) - Automate your GitHub workflow with Claude
* [Common workflows](/en/docs/claude-code/common-workflows) - Step-by-step guides for common use cases
Was this page helpful?
YesNo
[Common workflows](/en/docs/claude-code/common-workflows)[Claude Code hooks](/en/docs/claude-code/hooks-guide)
On this page


---

## Security

*Source: https://docs.anthropic.com/en/docs/claude-code/security*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Administration
Security
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
## [​](#how-we-approach-security) How we approach security
### [​](#security-foundation) Security foundation
Your code’s security is paramount. Claude Code is built with security at its core, developed according to Anthropic’s comprehensive security program. Learn more and access resources (SOC 2 Type 2 report, ISO 27001 certificate, etc.) at [Anthropic Trust Center](https://trust.anthropic.com).
### [​](#permission-based-architecture) Permission-based architecture
Claude Code uses strict read-only permissions by default. When additional actions are needed (editing files, running tests, executing commands), Claude Code requests explicit permission. Users control whether to approve actions once or allow them automatically.
We designed Claude Code to be transparent and secure. For example, we require approval for `git` commands before executing them, giving you direct control. This approach enables users and organizations to configure permissions directly.
For detailed permission configuration, see [Identity and Access Management](/en/docs/claude-code/iam).
### [​](#built-in-protections) Built-in protections
To mitigate risks in agentic systems:
* **Folder access restriction**: Claude Code can only access the folder where it was started and its subfolders—it cannot go upstream to parent directories. This creates a clear security boundary, ensuring Claude Code only operates within the intended project scope
* **Prompt fatigue mitigation**: Support for allowlisting frequently used safe commands per-user, per-codebase, or per-organization
* **Accept Edits mode**: Batch accept multiple edits while maintaining permission prompts for commands with side effects
### [​](#user-responsibility) User responsibility
Claude Code only has the permissions you grant it. You’re responsible for reviewing proposed code and commands for safety before approval.
## [​](#protect-against-prompt-injection) Protect against prompt injection
Prompt injection is a technique where an attacker attempts to override or manipulate an AI assistant’s instructions by inserting malicious text. Claude Code includes several safeguards against these attacks:
### [​](#core-protections) Core protections
* **Permission system**: Sensitive operations require explicit approval
* **Context-aware analysis**: Detects potentially harmful instructions by analyzing the full request
* **Input sanitization**: Prevents command injection by processing user inputs
* **Command blocklist**: Blocks risky commands that fetch arbitrary content from the web like `curl` and `wget`
### [​](#additional-safeguards) Additional safeguards
* **Network request approval**: Tools that make network requests require user approval by default
* **Isolated context windows**: Web fetch uses a separate context window to avoid injecting potentially malicious prompts
* **Trust verification**: First-time codebase runs and new MCP servers require trust verification
* **Command injection detection**: Suspicious bash commands require manual approval even if previously allowlisted
* **Fail-closed matching**: Unmatched commands default to requiring manual approval
* **Natural language descriptions**: Complex bash commands include explanations for user understanding
**Best practices for working with untrusted content**:
1. Review suggested commands before approval
2. Avoid piping untrusted content directly to Claude
3. Verify proposed changes to critical files
4. Use virtual machines (VMs) to run scripts and make tool calls, especially when interacting with external web services
5. Report suspicious behavior with `/bug`
While these protections significantly reduce risk, no system is completely
immune to all attacks. Always maintain good security practices when working
with any AI tool.
## [​](#mcp-security) MCP security
Claude Code allows users to configure Model Context Protocol (MCP) servers. The list of allowed MCP servers is configured in your source code, as part of Claude Code settings engineers check into source control.
We encourage either writing your own MCP servers or using MCP servers from providers that you trust. You are able to configure Claude Code permissions for MCP servers. Anthropic does not manage or audit any MCP servers.
## [​](#security-best-practices) Security best practices
### [​](#working-with-sensitive-code) Working with sensitive code
* Review all suggested changes before approval
* Use project-specific permission settings for sensitive repositories
* Consider using [devcontainers](/en/docs/claude-code/devcontainer) for additional isolation
* Regularly audit your permission settings with `/permissions`
### [​](#team-security) Team security
* Use [enterprise managed policies](/en/docs/claude-code/iam#enterprise-managed-policy-settings) to enforce organizational standards
* Share approved permission configurations through version control
* Train team members on security best practices
* Monitor Claude Code usage through [OpenTelemetry metrics](/en/docs/claude-code/monitoring-usage)
### [​](#reporting-security-issues) Reporting security issues
If you discover a security vulnerability in Claude Code:
1. Do not disclose it publicly
2. Report it through our [HackerOne program](https://hackerone.com/anthropic-vdp/reports/new?type=team&report_type=vulnerability)
3. Include detailed reproduction steps
4. Allow time for us to address the issue before public disclosure
## [​](#related-resources) Related resources
* [Identity and Access Management](/en/docs/claude-code/iam) - Configure permissions and access controls
* [Monitoring usage](/en/docs/claude-code/monitoring-usage) - Track and audit Claude Code activity
* [Development containers](/en/docs/claude-code/devcontainer) - Secure, isolated environments
* [Anthropic Trust Center](https://trust.anthropic.com) - Security certifications and compliance
Was this page helpful?
YesNo
[Identity and Access Management](/en/docs/claude-code/iam)[Monitoring](/en/docs/claude-code/monitoring-usage)
On this page


---

## Settings

*Source: https://docs.anthropic.com/en/docs/claude-code/settings*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Configuration
Claude Code settings
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
Claude Code offers a variety of settings to configure its behavior to meet your needs. You can configure Claude Code by running the `/config` command when using the interactive REPL.
## [​](#settings-files) Settings files
The `settings.json` file is our official mechanism for configuring Claude
Code through hierarchical settings:
* **User settings** are defined in `~/.claude/settings.json` and apply to all
  projects.
* **Project settings** are saved in your project directory:
  + `.claude/settings.json` for settings that are checked into source control and shared with your team
  + `.claude/settings.local.json` for settings that are not checked in, useful for personal preferences and experimentation. Claude Code will configure git to ignore `.claude/settings.local.json` when it is created.
* For enterprise deployments of Claude Code, we also support **enterprise
  managed policy settings**. These take precedence over user and project
  settings. System administrators can deploy policies to:
  + macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
  + Linux and WSL: `/etc/claude-code/managed-settings.json`
  + Windows: `C:\ProgramData\ClaudeCode\managed-settings.json`
Example settings.json
```
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test:*)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl:*)"
    ]
  },
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp"
  }
}
```
### [​](#available-settings) Available settings
`settings.json` supports a number of options:
| Key | Description | Example |
| --- | --- | --- |
| `apiKeyHelper` | Custom script, to be executed in `/bin/sh`, to generate an auth value. This value will generally be sent as `X-Api-Key`, `Authorization: Bearer`, and `Proxy-Authorization: Bearer` headers for model requests | `/bin/generate_temp_api_key.sh` |
| `cleanupPeriodDays` | How long to locally retain chat transcripts (default: 30 days) | `20` |
| `env` | Environment variables that will be applied to every session | `{"FOO": "bar"}` |
| `includeCoAuthoredBy` | Whether to include the `co-authored-by Claude` byline in git commits and pull requests (default: `true`) | `false` |
| `permissions` | See table below for structure of permissions. |  |
| `hooks` | Configure custom commands to run before or after tool executions. See [hooks documentation](hooks) | `{"PreToolUse": {"Bash": "echo 'Running command...'"}}` |
| `model` | Override the default model to use for Claude Code | `"claude-3-5-sonnet-20241022"` |
| `forceLoginMethod` | Use `claudeai` to restrict login to Claude.ai accounts, `console` to restrict login to Anthropic Console (API usage billing) accounts | `claudeai` |
| `enableAllProjectMcpServers` | Automatically approve all MCP servers defined in project `.mcp.json` files | `true` |
| `enabledMcpjsonServers` | List of specific MCP servers from `.mcp.json` files to approve | `["memory", "github"]` |
| `disabledMcpjsonServers` | List of specific MCP servers from `.mcp.json` files to reject | `["filesystem"]` |
### [​](#permission-settings) Permission settings
| Keys | Description | Example |
| --- | --- | --- |
| `allow` | Array of [permission rules](/en/docs/claude-code/iam#configuring-permissions) to allow tool use | `[ "Bash(git diff:*)" ]` |
| `deny` | Array of [permission rules](/en/docs/claude-code/iam#configuring-permissions) to deny tool use | `[ "WebFetch", "Bash(curl:*)" ]` |
| `additionalDirectories` | Additional [working directories](iam#working-directories) that Claude has access to | `[ "../docs/" ]` |
| `defaultMode` | Default [permission mode](iam#permission-modes) when opening Claude Code | `"acceptEdits"` |
| `disableBypassPermissionsMode` | Set to `"disable"` to prevent `bypassPermissions` mode from being activated. See [managed policy settings](iam#enterprise-managed-policy-settings) | `"disable"` |
### [​](#settings-precedence) Settings precedence
Settings are applied in order of precedence:
1. Enterprise policies (see [IAM documentation](/en/docs/claude-code/iam#enterprise-managed-policy-settings))
2. Command line arguments
3. Local project settings
4. Shared project settings
5. User settings
## [​](#environment-variables) Environment variables
Claude Code supports the following environment variables to control its behavior:
All environment variables can also be configured in [`settings.json`](/_sites/docs.anthropic.com/en/docs/claude-code/settings#available-settings). This is useful as a way to automatically set environment variables for each session, or to roll out a set of environment variables for your whole team or organization.
| Variable | Purpose |
| --- | --- |
| `ANTHROPIC_API_KEY` | API key sent as `X-Api-Key` header, typically for the Claude SDK (for interactive usage, run `/login`) |
| `ANTHROPIC_AUTH_TOKEN` | Custom value for the `Authorization` and `Proxy-Authorization` headers (the value you set here will be prefixed with `Bearer` ) |
| `ANTHROPIC_CUSTOM_HEADERS` | Custom headers you want to add to the request (in `Name: Value` format) |
| `ANTHROPIC_MODEL` | Name of custom model to use (see [Model Configuration](/en/docs/claude-code/bedrock-vertex-proxies#model-configuration)) |
| `ANTHROPIC_SMALL_FAST_MODEL` | Name of [Haiku-class model for background tasks](/en/docs/claude-code/costs) |
| `ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION` | Override AWS region for the small/fast model when using Bedrock |
| `AWS_BEARER_TOKEN_BEDROCK` | Bedrock API key for authentication (see [Bedrock API keys](https://aws.amazon.com/blogs/machine-learning/accelerate-ai-development-with-amazon-bedrock-api-keys/)) |
| `BASH_DEFAULT_TIMEOUT_MS` | Default timeout for long-running bash commands |
| `BASH_MAX_TIMEOUT_MS` | Maximum timeout the model can set for long-running bash commands |
| `BASH_MAX_OUTPUT_LENGTH` | Maximum number of characters in bash outputs before they are middle-truncated |
| `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` | Return to the original working directory after each Bash command |
| `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` | Interval in milliseconds at which credentials should be refreshed (when using `apiKeyHelper`) |
| `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL` | Skip auto-installation of IDE extensions |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | Set the maximum number of output tokens for most requests |
| `CLAUDE_CODE_USE_BEDROCK` | Use [Bedrock](/en/docs/claude-code/amazon-bedrock) |
| `CLAUDE_CODE_USE_VERTEX` | Use [Vertex](/en/docs/claude-code/google-vertex-ai) |
| `CLAUDE_CODE_SKIP_BEDROCK_AUTH` | Skip AWS authentication for Bedrock (e.g. when using an LLM gateway) |
| `CLAUDE_CODE_SKIP_VERTEX_AUTH` | Skip Google authentication for Vertex (e.g. when using an LLM gateway) |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | Equivalent of setting `DISABLE_AUTOUPDATER`, `DISABLE_BUG_COMMAND`, `DISABLE_ERROR_REPORTING`, and `DISABLE_TELEMETRY` |
| `CLAUDE_CODE_DISABLE_TERMINAL_TITLE` | Set to `1` to disable automatic terminal title updates based on conversation context |
| `DISABLE_AUTOUPDATER` | Set to `1` to disable automatic updates. This takes precedence over the `autoUpdates` configuration setting. |
| `DISABLE_BUG_COMMAND` | Set to `1` to disable the `/bug` command |
| `DISABLE_COST_WARNINGS` | Set to `1` to disable cost warning messages |
| `DISABLE_ERROR_REPORTING` | Set to `1` to opt out of Sentry error reporting |
| `DISABLE_NON_ESSENTIAL_MODEL_CALLS` | Set to `1` to disable model calls for non-critical paths like flavor text |
| `DISABLE_TELEMETRY` | Set to `1` to opt out of Statsig telemetry (note that Statsig events do not include user data like code, file paths, or bash commands) |
| `HTTP_PROXY` | Specify HTTP proxy server for network connections |
| `HTTPS_PROXY` | Specify HTTPS proxy server for network connections |
| `MAX_THINKING_TOKENS` | Force a thinking for the model budget |
| `MCP_TIMEOUT` | Timeout in milliseconds for MCP server startup |
| `MCP_TOOL_TIMEOUT` | Timeout in milliseconds for MCP tool execution |
| `MAX_MCP_OUTPUT_TOKENS` | Maximum number of tokens allowed in MCP tool responses (default: 25000) |
| `VERTEX_REGION_CLAUDE_3_5_HAIKU` | Override region for Claude 3.5 Haiku when using Vertex AI |
| `VERTEX_REGION_CLAUDE_3_5_SONNET` | Override region for Claude 3.5 Sonnet when using Vertex AI |
| `VERTEX_REGION_CLAUDE_3_7_SONNET` | Override region for Claude 3.7 Sonnet when using Vertex AI |
| `VERTEX_REGION_CLAUDE_4_0_OPUS` | Override region for Claude 4.0 Opus when using Vertex AI |
| `VERTEX_REGION_CLAUDE_4_0_SONNET` | Override region for Claude 4.0 Sonnet when using Vertex AI |
## [​](#configuration-options) Configuration options
We are in the process of migrating global configuration to `settings.json`.
`claude config` will be deprecated in place of [settings.json](/_sites/docs.anthropic.com/en/docs/claude-code/settings#settings-files)
To manage your configurations, use the following commands:
* List settings: `claude config list`
* See a setting: `claude config get <key>`
* Change a setting: `claude config set <key> <value>`
* Push to a setting (for lists): `claude config add <key> <value>`
* Remove from a setting (for lists): `claude config remove <key> <value>`
By default `config` changes your project configuration. To manage your global configuration, use the `--global` (or `-g`) flag.
### [​](#global-configuration) Global configuration
To set a global configuration, use `claude config set -g <key> <value>`:
| Key | Description | Example |
| --- | --- | --- |
| `autoUpdates` | Whether to enable automatic updates (default: `true`). When enabled, Claude Code automatically downloads and installs updates in the background. Updates are applied when you restart Claude Code. | `false` |
| `preferredNotifChannel` | Where you want to receive notifications (default: `iterm2`) | `iterm2`, `iterm2_with_bell`, `terminal_bell`, or `notifications_disabled` |
| `theme` | Color theme | `dark`, `light`, `light-daltonized`, or `dark-daltonized` |
| `verbose` | Whether to show full bash and command outputs (default: `false`) | `true` |
## [​](#tools-available-to-claude) Tools available to Claude
Claude Code has access to a set of powerful tools that help it understand and modify your codebase:
| Tool | Description | Permission Required |
| --- | --- | --- |
| **Bash** | Executes shell commands in your environment | Yes |
| **Edit** | Makes targeted edits to specific files | Yes |
| **Glob** | Finds files based on pattern matching | No |
| **Grep** | Searches for patterns in file contents | No |
| **LS** | Lists files and directories | No |
| **MultiEdit** | Performs multiple edits on a single file atomically | Yes |
| **NotebookEdit** | Modifies Jupyter notebook cells | Yes |
| **NotebookRead** | Reads and displays Jupyter notebook contents | No |
| **Read** | Reads the contents of files | No |
| **Task** | Runs a sub-agent to handle complex, multi-step tasks | No |
| **TodoWrite** | Creates and manages structured task lists | No |
| **WebFetch** | Fetches content from a specified URL | Yes |
| **WebSearch** | Performs web searches with domain filtering | Yes |
| **Write** | Creates or overwrites files | Yes |
Permission rules can be configured using `/allowed-tools` or in [permission settings](/en/docs/claude-code/settings#available-settings).
### [​](#extending-tools-with-hooks) Extending tools with hooks
You can run custom commands before or after any tool executes using
[Claude Code hooks](/en/docs/claude-code/hooks-guide).
For example, you could automatically run a Python formatter after Claude
modifies Python files, or prevent modifications to production configuration
files by blocking Write operations to certain paths.
## [​](#see-also) See also
* [Identity and Access Management](/en/docs/claude-code/iam#configuring-permissions) - Learn about Claude Code’s permission system
* [IAM and access control](/en/docs/claude-code/iam#enterprise-managed-policy-settings) - Enterprise policy management
* [Troubleshooting](/en/docs/claude-code/troubleshooting#auto-updater-issues) - Solutions for common configuration issues
Was this page helpful?
YesNo
[Costs](/en/docs/claude-code/costs)[Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
On this page


---

## Setup

*Source: https://docs.anthropic.com/en/docs/claude-code/setup*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Administration
Set up Claude Code
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
## [​](#system-requirements) System requirements
* **Operating Systems**: macOS 10.15+, Ubuntu 20.04+/Debian 10+, or Windows 10+ (with WSL 1, WSL 2, or Git for Windows)
* **Hardware**: 4GB+ RAM
* **Software**: [Node.js 18+](https://nodejs.org/en/download)
* **Network**: Internet connection required for authentication and AI processing
* **Shell**: Works best in Bash, Zsh or Fish
* **Location**: [Anthropic supported countries](https://www.anthropic.com/supported-countries)
## [​](#standard-installation) Standard installation
To install Claude Code, run the following command:
```
npm install -g @anthropic-ai/claude-code
```
Do NOT use `sudo npm install -g` as this can lead to permission issues and security risks.
If you encounter permission errors, see [configure Claude Code](/en/docs/claude-code/troubleshooting#linux-permission-issues) for recommended solutions.
Some users may be automatically migrated to an improved installation method.
Run `claude doctor` after installation to check your installation type.
After the installation process completes, navigate to your project and start Claude Code:
```
cd your-awesome-project
claude
```
Claude Code offers the following authentication options:
1. **Anthropic Console**: The default option. Connect through the Anthropic Console and complete the OAuth process. Requires active billing at [console.anthropic.com](https://console.anthropic.com).
2. **Claude App (with Pro or Max plan)**: Subscribe to Claude’s [Pro or Max plan](https://www.anthropic.com/pricing) for a unified subscription that includes both Claude Code and the web interface. Get more value at the same price point while managing your account in one place. Log in with your Claude.ai account. During launch, choose the option that matches your subscription type.
3. **Enterprise platforms**: Configure Claude Code to use [Amazon Bedrock or Google Vertex AI](/en/docs/claude-code/third-party-integrations) for enterprise deployments with your existing cloud infrastructure.
## [​](#windows-setup) Windows setup
**Option 1: Claude Code within WSL**
* Both WSL 1 and WSL 2 are supported
**Option 2: Claude Code on native Windows with Git Bash**
* Requires [Git for Windows](https://git-scm.com/downloads/win)
* For portable Git installations, specify the path to your `bash.exe`:
  ```
  $env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
  ```
## [​](#alternative-installation-methods) Alternative installation methods
Claude Code offers multiple installation methods to suit different environments.
If you encounter any issues during installation, consult the [troubleshooting guide](/en/docs/claude-code/troubleshooting#linux-permission-issues).
Run `claude doctor` after installation to check your installation type and version.
### [​](#global-npm-installation) Global npm installation
Traditional method shown in the [install steps above](/_sites/docs.anthropic.com/en/docs/claude-code/setup#install-and-authenticate)
### [​](#local-installation) Local installation
* After global install via npm, use `claude migrate-installer` to move to local
* Avoids autoupdater npm permission issues
* Some users may be automatically migrated to this method
### [​](#native-binary-installation-alpha) Native binary installation (Alpha)
* Use `claude install` from an existing installation
* or `curl -fsSL claude.ai/install.sh | bash` for a fresh install
* Currently in alpha testing
* Platform support: macOS, Linux, Windows (via WSL)
## [​](#running-on-aws-or-gcp) Running on AWS or GCP
By default, Claude Code uses Anthropic’s API.
For details on running Claude Code on AWS or GCP, see [third-party integrations](/en/docs/claude-code/third-party-integrations).
## [​](#update-claude-code) Update Claude Code
### [​](#auto-updates) Auto updates
Claude Code automatically keeps itself up to date to ensure you have the latest features and security fixes.
* **Update checks**: Performed on startup and periodically while running
* **Update process**: Downloads and installs automatically in the background
* **Notifications**: You’ll see a notification when updates are installed
* **Applying updates**: Updates take effect the next time you start Claude Code
**Disable auto-updates:**
```
# Via configuration
claude config set autoUpdates false --global
# Or via environment variable
export DISABLE_AUTOUPDATER=1
```
### [​](#update-manually) Update manually
```
claude update
```
Was this page helpful?
YesNo
[Development containers](/en/docs/claude-code/devcontainer)[Identity and Access Management](/en/docs/claude-code/iam)
On this page


---

## Slash Commands

*Source: https://docs.anthropic.com/en/docs/claude-code/slash-commands*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Reference
Slash commands
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
## [​](#built-in-slash-commands) Built-in slash commands
| Command | Purpose |
| --- | --- |
| `/add-dir` | Add additional working directories |
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
| `/permissions` | View or update [permissions](/en/docs/claude-code/iam#configuring-permissions) |
| `/pr_comments` | View pull request comments |
| `/review` | Request code review |
| `/status` | View account and system statuses |
| `/terminal-setup` | Install Shift+Enter key binding for newlines (iTerm2 and VSCode only) |
| `/vim` | Enter vim mode for alternating insert and command modes |
## [​](#custom-slash-commands) Custom slash commands
Custom slash commands allow you to define frequently-used prompts as Markdown files that Claude Code can execute. Commands are organized by scope (project-specific or personal) and support namespacing through directory structures.
### [​](#syntax) Syntax
```
/<command-name> [arguments]
```
#### [​](#parameters) Parameters
| Parameter | Description |
| --- | --- |
| `<command-name>` | Name derived from the Markdown filename (without `.md` extension) |
| `[arguments]` | Optional arguments passed to the command |
### [​](#command-types) Command types
#### [​](#project-commands) Project commands
Commands stored in your repository and shared with your team. When listed in `/help`, these commands show “(project)” after their description.
**Location**: `.claude/commands/`
In the following example, we create the `/optimize` command:
```
# Create a project command
mkdir -p .claude/commands
echo "Analyze this code for performance issues and suggest optimizations:" > .claude/commands/optimize.md
```
#### [​](#personal-commands) Personal commands
Commands available across all your projects. When listed in `/help`, these commands show “(user)” after their description.
**Location**: `~/.claude/commands/`
In the following example, we create the `/security-review` command:
```
# Create a personal command
mkdir -p ~/.claude/commands
echo "Review this code for security vulnerabilities:" > ~/.claude/commands/security-review.md
```
### [​](#features) Features
#### [​](#namespacing) Namespacing
Organize commands in subdirectories. The subdirectories determine the command’s
full name. The description will show whether the command comes from the project
directory (`.claude/commands`) or the user-level directory (`~/.claude/commands`).
Conflicts between user and project level commands are not supported. Otherwise,
multiple commands with the same base file name can coexist.
For example, a file at `.claude/commands/frontend/component.md` creates the command `/frontend:component` with description showing “(project)”.
Meanwhile, a file at `~/.claude/commands/component.md` creates the command `/component` with description showing “(user)”.
#### [​](#arguments) Arguments
Pass dynamic values to commands using the `$ARGUMENTS` placeholder.
For example:
```
# Command definition
echo 'Fix issue #$ARGUMENTS following our coding standards' > .claude/commands/fix-issue.md
# Usage
> /fix-issue 123
```
#### [​](#bash-command-execution) Bash command execution
Execute bash commands before the slash command runs using the `!` prefix. The output is included in the command context.
For example:
```
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
description: Create a git commit
---
## Context
- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`
## Your task
Based on the above changes, create a single git commit.
```
#### [​](#file-references) File references
Include file contents in commands using the `@` prefix to [reference files](/en/docs/claude-code/common-workflows#reference-files-and-directories).
For example:
```
# Reference a specific file
Review the implementation in @src/utils/helpers.js
# Reference multiple files
Compare @src/old-version.js with @src/new-version.js
```
#### [​](#thinking-mode) Thinking mode
Slash commands can trigger extended thinking by including [extended thinking keywords](/en/docs/claude-code/common-workflows#use-extended-thinking).
### [​](#file-format) File format
Command files support:
* **Markdown format** (`.md` extension)
* **YAML frontmatter** for metadata:
  + `allowed-tools`: List of tools the command can use
  + `description`: Brief description of the command
* **Dynamic content** with bash commands (`!`) and file references (`@`)
* **Prompt instructions** as the main content
## [​](#mcp-slash-commands) MCP slash commands
MCP servers can expose prompts as slash commands that become available in Claude Code. These commands are dynamically discovered from connected MCP servers.
### [​](#command-format) Command format
MCP commands follow the pattern:
```
/mcp__<server-name>__<prompt-name> [arguments]
```
### [​](#features-2) Features
#### [​](#dynamic-discovery) Dynamic discovery
MCP commands are automatically available when:
* An MCP server is connected and active
* The server exposes prompts through the MCP protocol
* The prompts are successfully retrieved during connection
#### [​](#arguments-2) Arguments
MCP prompts can accept arguments defined by the server:
```
# Without arguments
> /mcp__github__list_prs
# With arguments
> /mcp__github__pr_review 456
> /mcp__jira__create_issue "Bug title" high
```
#### [​](#naming-conventions) Naming conventions
* Server and prompt names are normalized
* Spaces and special characters become underscores
* Names are lowercased for consistency
### [​](#managing-mcp-connections) Managing MCP connections
Use the `/mcp` command to:
* View all configured MCP servers
* Check connection status
* Authenticate with OAuth-enabled servers
* Clear authentication tokens
* View available tools and prompts from each server
## [​](#see-also) See also
* [Interactive mode](/en/docs/claude-code/interactive-mode) - Shortcuts, input modes, and interactive features
* [CLI reference](/en/docs/claude-code/cli-reference) - Command-line flags and options
* [Settings](/en/docs/claude-code/settings) - Configuration options
* [Memory management](/en/docs/claude-code/memory) - Managing Claude’s memory across sessions
Was this page helpful?
YesNo
[Interactive mode](/en/docs/claude-code/interactive-mode)[Hooks reference](/en/docs/claude-code/hooks)
On this page


---

## Terminal Config

*Source: https://docs.anthropic.com/en/docs/claude-code/terminal-config*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Configuration
Optimize your terminal setup
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
### [​](#themes-and-appearance) Themes and appearance
Claude cannot control the theme of your terminal. That’s handled by your terminal application. You can match Claude Code’s theme to your terminal any time via the `/config` command.
### [​](#line-breaks) Line breaks
You have several options for entering linebreaks into Claude Code:
* **Quick escape**: Type `\` followed by Enter to create a newline
* **Keyboard shortcut**: Set up a keybinding to insert a newline
#### [​](#set-up-shift%2Benter-vs-code-or-iterm2-%3A) Set up Shift+Enter (VS Code or iTerm2):
Run `/terminal-setup` within Claude Code to automatically configure Shift+Enter.
#### [​](#set-up-option%2Benter-vs-code%2C-iterm2-or-macos-terminal-app-%3A) Set up Option+Enter (VS Code, iTerm2 or macOS Terminal.app):
**For Mac Terminal.app:**
1. Open Settings → Profiles → Keyboard
2. Check “Use Option as Meta Key”
**For iTerm2 and VS Code terminal:**
1. Open Settings → Profiles → Keys
2. Under General, set Left/Right Option key to “Esc+“
### [​](#notification-setup) Notification setup
Never miss when Claude completes a task with proper notification configuration:
#### [​](#terminal-bell-notifications) Terminal bell notifications
Enable sound alerts when tasks complete:
```
claude config set --global preferredNotifChannel terminal_bell
```
**For macOS users**: Don’t forget to enable notification permissions in System Settings → Notifications → [Your Terminal App].
#### [​](#iterm-2-system-notifications) iTerm 2 system notifications
For iTerm 2 alerts when tasks complete:
1. Open iTerm 2 Preferences
2. Navigate to Profiles → Terminal
3. Enable “Silence bell” and Filter Alerts → “Send escape sequence-generated alerts”
4. Set your preferred notification delay
Note that these notifications are specific to iTerm 2 and not available in the default macOS Terminal.
#### [​](#custom-notification-hooks) Custom notification hooks
For advanced notification handling, you can create [notification hooks](/en/docs/claude-code/hooks#notification) to run your own logic.
### [​](#handling-large-inputs) Handling large inputs
When working with extensive code or long instructions:
* **Avoid direct pasting**: Claude Code may struggle with very long pasted content
* **Use file-based workflows**: Write content to a file and ask Claude to read it
* **Be aware of VS Code limitations**: The VS Code terminal is particularly prone to truncating long pastes
### [​](#vim-mode) Vim Mode
Claude Code supports a subset of Vim keybindings that can be enabled with `/vim` or configured via `/config`.
The supported subset includes:
* Mode switching: `Esc` (to NORMAL), `i`/`I`, `a`/`A`, `o`/`O` (to INSERT)
* Navigation: `h`/`j`/`k`/`l`, `w`/`e`/`b`, `0`/`$`/`^`, `gg`/`G`
* Editing: `x`, `dw`/`de`/`db`/`dd`/`D`, `cw`/`ce`/`cb`/`cc`/`C`, `.` (repeat)
Was this page helpful?
YesNo
[Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)[Memory management](/en/docs/claude-code/memory)
On this page


---

## Third Party Integrations

*Source: https://docs.anthropic.com/en/docs/claude-code/third-party-integrations*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Deployment
Enterprise deployment overview
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
This page provides an overview of available deployment options and helps you choose the right configuration for your organization.
## [​](#provider-comparison) Provider comparison
| Feature | Anthropic | Amazon Bedrock | Google Vertex AI |
| --- | --- | --- | --- |
| Regions | Supported [countries](https://www.anthropic.com/supported-countries) | Multiple AWS [regions](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) | Multiple GCP [regions](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations) |
| Prompt caching | Enabled by default | Enabled by default | Enabled by default |
| Authentication | API key | AWS credentials (IAM) | GCP credentials (OAuth/Service Account) |
| Cost tracking | Dashboard | AWS Cost Explorer | GCP Billing |
| Enterprise features | Teams, usage monitoring | IAM policies, CloudTrail | IAM roles, Cloud Audit Logs |
## [​](#cloud-providers) Cloud providers
[## Amazon Bedrock
Use Claude models through AWS infrastructure with IAM-based authentication and AWS-native monitoring](/en/docs/claude-code/amazon-bedrock)[## Google Vertex AI
Access Claude models via Google Cloud Platform with enterprise-grade security and compliance](/en/docs/claude-code/google-vertex-ai)
## [​](#corporate-infrastructure) Corporate infrastructure
[## Corporate Proxy
Configure Claude Code to work with your organization’s proxy servers and SSL/TLS requirements](/en/docs/claude-code/corporate-proxy)[## LLM Gateway
Deploy centralized model access with usage tracking, budgeting, and audit logging](/en/docs/claude-code/llm-gateway)
## [​](#configuration-overview) Configuration overview
Claude Code supports flexible configuration options that allow you to combine different providers and infrastructure:
Understand the difference between:
* **Corporate proxy**: An HTTP/HTTPS proxy for routing traffic (set via `HTTPS_PROXY` or `HTTP_PROXY`)
* **LLM Gateway**: A service that handles authentication and provides provider-compatible endpoints (set via `ANTHROPIC_BASE_URL`, `ANTHROPIC_BEDROCK_BASE_URL`, or `ANTHROPIC_VERTEX_BASE_URL`)
Both configurations can be used in tandem.
### [​](#using-bedrock-with-corporate-proxy) Using Bedrock with corporate proxy
Route Bedrock traffic through a corporate HTTP/HTTPS proxy:
```
# Enable Bedrock
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1
# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'
```
### [​](#using-bedrock-with-llm-gateway) Using Bedrock with LLM Gateway
Use a gateway service that provides Bedrock-compatible endpoints:
```
# Enable Bedrock
export CLAUDE_CODE_USE_BEDROCK=1
# Configure LLM gateway
export ANTHROPIC_BEDROCK_BASE_URL='https://your-llm-gateway.com/bedrock'
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1  # If gateway handles AWS auth
```
### [​](#using-vertex-ai-with-corporate-proxy) Using Vertex AI with corporate proxy
Route Vertex AI traffic through a corporate HTTP/HTTPS proxy:
```
# Enable Vertex
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=your-project-id
# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'
```
### [​](#using-vertex-ai-with-llm-gateway) Using Vertex AI with LLM Gateway
Combine Google Vertex AI models with an LLM gateway for centralized management:
```
# Enable Vertex
export CLAUDE_CODE_USE_VERTEX=1
# Configure LLM gateway
export ANTHROPIC_VERTEX_BASE_URL='https://your-llm-gateway.com/vertex'
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1  # If gateway handles GCP auth
```
### [​](#authentication-configuration) Authentication configuration
Claude Code uses the `ANTHROPIC_AUTH_TOKEN` for both `Authorization` and `Proxy-Authorization` headers when needed. The `SKIP_AUTH` flags (`CLAUDE_CODE_SKIP_BEDROCK_AUTH`, `CLAUDE_CODE_SKIP_VERTEX_AUTH`) are used in LLM gateway scenarios where the gateway handles provider authentication.
## [​](#choosing-the-right-deployment-configuration) Choosing the right deployment configuration
Consider these factors when selecting your deployment approach:
### [​](#direct-provider-access) Direct provider access
Best for organizations that:
* Want the simplest setup
* Have existing AWS or GCP infrastructure
* Need provider-native monitoring and compliance
### [​](#corporate-proxy) Corporate proxy
Best for organizations that:
* Have existing corporate proxy requirements
* Need traffic monitoring and compliance
* Must route all traffic through specific network paths
### [​](#llm-gateway) LLM Gateway
Best for organizations that:
* Need usage tracking across teams
* Want to dynamically switch between models
* Require custom rate limiting or budgets
* Need centralized authentication management
## [​](#debugging) Debugging
When debugging your deployment:
* Use the `claude /status` [slash command](/en/docs/claude-code/slash-commands). This command provides observability into any applied authentication, proxy, and URL settings.
* Set environment variable `export ANTHROPIC_LOG=debug` to log requests.
## [​](#best-practices-for-organizations) Best practices for organizations
1. We strongly recommend investing in documentation so that Claude Code understands your codebase. Many organizations make a `CLAUDE.md` file (which we also refer to as memory) in the root of the repository that contains the system architecture, how to run tests and other common commands, and best practices for contributing to the codebase. This file is typically checked into source control so that all users can benefit from it. [Learn more](/en/docs/claude-code/memory).
2. If you have a custom development environment, we find that creating a “one click” way to install Claude Code is key to growing adoption across an organization.
3. Encourage new users to try Claude Code for codebase Q&A, or on smaller bug fixes or feature requests. Ask Claude Code to make a plan. Check Claude’s suggestions and give feedback if it’s off-track. Over time, as users understand this new paradigm better, then they’ll be more effective at letting Claude Code run more agentically.
4. Security teams can configure managed permissions for what Claude Code is and is not allowed to do, which cannot be overwritten by local configuration. [Learn more](/en/docs/claude-code/security).
5. MCP is a great way to give Claude Code more information, such as connecting to ticket management systems or error logs. We recommend that one central team configures MCP servers and checks a `.mcp.json` configuration into the codebase so that all users benefit. [Learn more](/en/docs/claude-code/mcp).
At Anthropic, we trust Claude Code to power development across every Anthropic codebase. We hope you enjoy using Claude Code as much as we do!
## [​](#next-steps) Next steps
* [Set up Amazon Bedrock](/en/docs/claude-code/amazon-bedrock) for AWS-native deployment
* [Configure Google Vertex AI](/en/docs/claude-code/google-vertex-ai) for GCP deployment
* [Implement Corporate Proxy](/en/docs/claude-code/corporate-proxy) for network requirements
* [Deploy LLM Gateway](/en/docs/claude-code/llm-gateway) for enterprise management
* [Settings](/en/docs/claude-code/settings) for configuration options and environment variables
Was this page helpful?
YesNo
[Troubleshooting](/en/docs/claude-code/troubleshooting)[Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
On this page


---

## Troubleshooting

*Source: https://docs.anthropic.com/en/docs/claude-code/troubleshooting*

[Anthropic home page](/)
English
Search...
Search...
Navigation
Build with Claude Code
Troubleshooting
[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)
##### Getting started
* [Overview](/en/docs/claude-code/overview)
* [Quickstart](/en/docs/claude-code/quickstart)
* [Common workflows](/en/docs/claude-code/common-workflows)
##### Build with Claude Code
* [Claude Code SDK](/en/docs/claude-code/sdk)
* [Claude Code hooks](/en/docs/claude-code/hooks-guide)
* [GitHub Actions](/en/docs/claude-code/github-actions)
* [Model Context Protocol (MCP)](/en/docs/claude-code/mcp)
* [Troubleshooting](/en/docs/claude-code/troubleshooting)
##### Deployment
* [Overview](/en/docs/claude-code/third-party-integrations)
* [Amazon Bedrock](/en/docs/claude-code/amazon-bedrock)
* [Google Vertex AI](/en/docs/claude-code/google-vertex-ai)
* [Corporate proxy](/en/docs/claude-code/corporate-proxy)
* [LLM gateway](/en/docs/claude-code/llm-gateway)
* [Development containers](/en/docs/claude-code/devcontainer)
##### Administration
* [Advanced installation](/en/docs/claude-code/setup)
* [Identity and Access Management](/en/docs/claude-code/iam)
* [Security](/en/docs/claude-code/security)
* [Monitoring](/en/docs/claude-code/monitoring-usage)
* [Costs](/en/docs/claude-code/costs)
##### Configuration
* [Settings](/en/docs/claude-code/settings)
* [Add Claude Code to your IDE](/en/docs/claude-code/ide-integrations)
* [Terminal configuration](/en/docs/claude-code/terminal-config)
* [Memory management](/en/docs/claude-code/memory)
##### Reference
* [CLI reference](/en/docs/claude-code/cli-reference)
* [Interactive mode](/en/docs/claude-code/interactive-mode)
* [Slash commands](/en/docs/claude-code/slash-commands)
* [Hooks reference](/en/docs/claude-code/hooks)
##### Resources
* [Data usage](/en/docs/claude-code/data-usage)
* [Legal and compliance](/en/docs/claude-code/legal-and-compliance)
## [​](#common-installation-issues) Common installation issues
### [​](#windows-installation-issues%3A-errors-in-wsl) Windows installation issues: errors in WSL
You might encounter the following issues in WSL:
**OS/platform detection issues**: If you receive an error during installation, WSL may be using Windows `npm`. Try:
* Run `npm config set os linux` before installation
* Install with `npm install -g @anthropic-ai/claude-code --force --no-os-check` (Do NOT use `sudo`)
**Node not found errors**: If you see `exec: node: not found` when running `claude`, your WSL environment may be using a Windows installation of Node.js. You can confirm this with `which npm` and `which node`, which should point to Linux paths starting with `/usr/` rather than `/mnt/c/`. To fix this, try installing Node via your Linux distribution’s package manager or via [`nvm`](https://github.com/nvm-sh/nvm).
### [​](#linux-installation-issues%3A-permission-errors) Linux installation issues: permission errors
When installing Claude Code with npm, you may encounter permission errors if your npm global prefix is not user writable (eg. `/usr`, or `/usr/local`).
#### [​](#recommended-solution%3A-migrate-to-local-installation) Recommended solution: Migrate to local installation
The simplest solution is to migrate to a local installation:
```
claude migrate-installer
```
This moves Claude Code to `~/.claude/local/` and sets up an alias in your shell configuration. No `sudo` is required for future updates.
After migration, restart your shell, and then verify your installation:
```
which claude  # Should show an alias to ~/.claude/local/claude
claude doctor # Check installation health
```
#### [​](#alternative-solution%3A-create-a-user-writable-npm-prefix-for-global-installs) Alternative solution: Create a user-writable npm prefix for global installs
You can configure npm to use a directory within your home folder:
```
# First, save a list of your existing global packages for later migration
npm list -g --depth=0 > ~/npm-global-packages.txt
# Create a directory for your global packages
mkdir -p ~/.npm-global
# Configure npm to use the new directory path
npm config set prefix ~/.npm-global
# Note: Replace ~/.bashrc with ~/.zshrc, ~/.profile, or other appropriate file for your shell
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
# Apply the new PATH setting
source ~/.bashrc
# Now reinstall Claude Code in the new location
npm install -g @anthropic-ai/claude-code
# Optional: Reinstall your previous global packages in the new location
# Look at ~/npm-global-packages.txt and install packages you want to keep
```
This solution:
* Avoids modifying system directory permissions
* Creates a clean, dedicated location for your global npm packages
* Follows security best practices
#### [​](#system-recovery%3A-if-you-have-run-commands-that-change-ownership-and-permissions-of-system-files-or-similar) System Recovery: If you have run commands that change ownership and permissions of system files or similar
If you’ve already run a command that changed system directory permissions (such as `sudo chown -R $USER:$(id -gn) /usr && sudo chmod -R u+w /usr`) and your system is now broken (for example, if you see `sudo: /usr/bin/sudo must be owned by uid 0 and have the setuid bit set`), you’ll need to perform recovery steps.
##### Ubuntu/Debian Recovery Method:
1. While rebooting, hold **SHIFT** to access the GRUB menu
2. Select “Advanced options for Ubuntu/Debian”
3. Choose the recovery mode option
4. Select “Drop to root shell prompt”
5. Remount the filesystem as writable:
   ```
   mount -o remount,rw /
   ```
6. Fix permissions:
   ```
   # Restore root ownership
   chown -R root:root /usr
   chmod -R 755 /usr
   # Ensure /usr/local is owned by your user for npm packages
   chown -R YOUR_USERNAME:YOUR_USERNAME /usr/local
   # Set setuid bit for critical binaries
   chmod u+s /usr/bin/sudo
   chmod 4755 /usr/bin/sudo
   chmod u+s /usr/bin/su
   chmod u+s /usr/bin/passwd
   chmod u+s /usr/bin/newgrp
   chmod u+s /usr/bin/gpasswd
   chmod u+s /usr/bin/chsh
   chmod u+s /usr/bin/chfn
   # Fix sudo configuration
   chown root:root /usr/libexec/sudo/sudoers.so
   chmod 4755 /usr/libexec/sudo/sudoers.so
   chown root:root /etc/sudo.conf
   chmod 644 /etc/sudo.conf
   ```
7. Reinstall affected packages (optional but recommended):
   ```
   # Save list of installed packages
   dpkg --get-selections > /tmp/installed_packages.txt
   # Reinstall them
   awk '{print $1}' /tmp/installed_packages.txt | xargs -r apt-get install --reinstall -y
   ```
8. Reboot:
   ```
   reboot
   ```
##### Alternative Live USB Recovery Method:
If the recovery mode doesn’t work, you can use a live USB:
1. Boot from a live USB (Ubuntu, Debian, or any Linux distribution)
2. Find your system partition:
   ```
   lsblk
   ```
3. Mount your system partition:
   ```
   sudo mount /dev/sdXY /mnt  # replace sdXY with your actual system partition
   ```
4. If you have a separate boot partition, mount it too:
   ```
   sudo mount /dev/sdXZ /mnt/boot  # if needed
   ```
5. Chroot into your system:
   ```
   # For Ubuntu/Debian:
   sudo chroot /mnt
   # For Arch-based systems:
   sudo arch-chroot /mnt
   ```
6. Follow steps 6-8 from the Ubuntu/Debian recovery method above
After restoring your system, follow the recommended solution above to set up a user-writable npm prefix.
## [​](#auto-updater-issues) Auto-updater issues
If Claude Code can’t update automatically (see [Update Claude Code](/en/docs/claude-code/setup#update-claude-code) for how updates work):
### [​](#for-permission-errors) For permission errors
This is typically due to permission issues with your npm global prefix directory. You have several options:
1. **Migrate to local installation** (recommended): Run `claude migrate-installer` to move to a local installation that avoids permission issues entirely
2. **Update manually**: Run `claude update` with appropriate permissions
3. **Fix npm permissions**: Follow the [recommended solution](/_sites/docs.anthropic.com/en/docs/claude-code/troubleshooting#recommended-solution-create-a-user-writable-npm-prefix) above (more complex)
### [​](#to-disable-auto-updates) To disable auto-updates
If you prefer to control when Claude Code updates:
```
# Via configuration
claude config set autoUpdates false --global
# Or via environment variable
export DISABLE_AUTOUPDATER=1
```
### [​](#to-check-your-installation) To check your installation
* **Current version and diagnostics**: Run `claude doctor`
* **Check for updates**: Run `claude update`
* **View update settings**: Run `claude config get autoUpdates --global`
* **Verify installation location**: Run `which claude` - if this shows an alias pointing to `~/.claude/local/claude`, you’re using the recommended local installation
## [​](#permissions-and-authentication) Permissions and authentication
### [​](#repeated-permission-prompts) Repeated permission prompts
If you find yourself repeatedly approving the same commands, you can allow specific tools
to run without approval using the `/permissions` command. See [Permissions docs](/en/docs/claude-code/iam#configuring-permissions).
### [​](#authentication-issues) Authentication issues
If you’re experiencing authentication problems:
1. Run `/logout` to sign out completely
2. Close Claude Code
3. Restart with `claude` and complete the authentication process again
If problems persist, try:
```
rm -rf ~/.config/claude-code/auth.json
claude
```
This removes your stored authentication information and forces a clean login.
## [​](#performance-and-stability) Performance and stability
### [​](#high-cpu-or-memory-usage) High CPU or memory usage
Claude Code is designed to work with most development environments, but may consume significant resources when processing large codebases. If you’re experiencing performance issues:
1. Use `/compact` regularly to reduce context size
2. Close and restart Claude Code between major tasks
3. Consider adding large build directories to your `.gitignore` file
### [​](#command-hangs-or-freezes) Command hangs or freezes
If Claude Code seems unresponsive:
1. Press Ctrl+C to attempt to cancel the current operation
2. If unresponsive, you may need to close the terminal and restart
### [​](#esc-key-not-working-in-jetbrains-intellij%2C-pycharm%2C-etc-terminals) ESC key not working in JetBrains (IntelliJ, PyCharm, etc.) terminals
If you’re using Claude Code in JetBrains terminals and the ESC key doesn’t interrupt the agent as expected, this is likely due to a keybinding clash with JetBrains’ default shortcuts.
To fix this issue:
1. Go to Settings → Tools → Terminal
2. Click the “Configure terminal keybindings” hyperlink next to “Override IDE Shortcuts”
3. Within the terminal keybindings, scroll down to “Switch focus to Editor” and delete that shortcut
This will allow the ESC key to properly function for canceling Claude Code operations instead of being captured by PyCharm’s “Switch focus to Editor” action.
## [​](#getting-more-help) Getting more help
If you’re experiencing issues not covered here:
1. Use the `/bug` command within Claude Code to report problems directly to Anthropic
2. Check the [GitHub repository](https://github.com/anthropics/claude-code) for known issues
3. Run `/doctor` to check the health of your Claude Code installation
Was this page helpful?
YesNo
[Model Context Protocol (MCP)](/en/docs/claude-code/mcp)[Overview](/en/docs/claude-code/third-party-integrations)
On this page


---

