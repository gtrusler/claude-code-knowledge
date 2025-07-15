# Claude Code Official Documentation

*Last updated: 2025-07-15 17:09 UTC*
*Source: https://docs.anthropic.com/en/docs/claude-code*

---

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

##### Build with Claude

* [Claude Code SDK](/en/docs/claude-code/sdk)
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
* [Hooks](/en/docs/claude-code/hooks)

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

* [Get started in 30 seconds](#get-started-in-30-seconds)
* [What Claude Code does for you](#what-claude-code-does-for-you)
* [Why developers love Claude Code](#why-developers-love-claude-code)
* [Next steps](#next-steps)
* [Additional resources](#additional-resources)

