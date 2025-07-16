# Claude Code Official Documentation

*Last updated: 2025-07-16 14:54 UTC*
*Source: https://docs.anthropic.com/en/docs/claude-code*

This documentation is automatically scraped from Anthropic's official docs.

---

## Table of Contents

- [.Devcontainer](#.devcontainer)
- [.Gitattributes](#.gitattributes)
- [.Gitignore](#.gitignore)
- [.Npmrc](#.npmrc)
- [.Prettierignore](#.prettierignore)
- [.Prettierrc](#.prettierrc)
- [.Vscode](#.vscode)
- [3368](#3368)
- [3381](#3381)
- [3634](#3634)
- [3635](#3635)
- [3636](#3636)
- [3637](#3637)
- [3638](#3638)
- [3639](#3639)
- [3643](#3643)
- [3645](#3645)
- [3647](#3647)
- [3648](#3648)
- [3649](#3649)
- [3650](#3650)
- [712](#712)
- [Changelog.Md](#CHANGELOG.md)
- [Dockerfile](#Dockerfile)
- [License](#LICENSE)
- [Script](#Script)
- [_Errors.Py](#_errors.py)
- [Action.Yml](#action.yml)
- [Actions](#actions)
- [Activity](#activity)
- [Amazon Bedrock](#amazon-bedrock)
- [Analytics](#analytics)
- [Bash_Command_Validator_Example.Py](#bash_command_validator_example.py)
- [Bedrock Vertex](#bedrock-vertex)
- [Bedrock Vertex Proxies](#bedrock-vertex-proxies)
- [Beta](#beta)
- [Branches](#branches)
- [Bun.Lock](#bun.lock)
- [Claude Code](#claude-code)
- [Claude Code Action](#claude-code-action)
- [Claude Code Action Official](#claude-code-action-official)
- [Claude Code Base Action](#claude-code-base-action)
- [Claude Code Sdk Python](#claude-code-sdk-python)
- [Claude Pr Path Specific.Yml](#claude-pr-path-specific.yml)
- [Claude Review From Author.Yml](#claude-review-from-author.yml)
- [Claude.Yml](#claude.yml)
- [Claude_Code_Sdk](#claude_code_sdk)
- [Cli Reference](#cli-reference)
- [Commands](#commands)
- [Common Workflows](#common-workflows)
- [Contributors](#contributors)
- [Corporate Proxy](#corporate-proxy)
- [Costs](#costs)
- [Custom Properties](#custom-properties)
- [Data Usage](#data-usage)
- [Demo.Gif](#demo.gif)
- [Dependents](#dependents)
- [Devcontainer](#devcontainer)
- [Devcontainer.Json](#devcontainer.json)
- [Discussions](#discussions)
- [Examples](#examples)
- [Forks](#forks)
- [Getting Started](#getting-started)
- [Github Actions](#github-actions)
- [Google Vertex Ai](#google-vertex-ai)
- [Hooks](#hooks)
- [Hooks Guide](#hooks-guide)
- [Iam](#iam)
- [Ide Integrations](#ide-integrations)
- [Init Firewall.Sh](#init-firewall.sh)
- [Interactive Mode](#interactive-mode)
- [Issues](#issues)
- [Labels](#labels)
- [Legal And Compliance](#legal-and-compliance)
- [Llm Gateway](#llm-gateway)
- [Mcp](#mcp)
- [Memory](#memory)
- [Milestones](#milestones)
- [Monitoring Usage](#monitoring-usage)
- [Overview](#overview)
- [Package.Json](#package.json)
- [Projects](#projects)
- [Pulls](#pulls)
- [Pulse](#pulse)
- [Pyproject.Toml](#pyproject.toml)
- [Quick_Start.Py](#quick_start.py)
- [Quickstart](#quickstart)
- [Releases](#releases)
- [Scripts](#scripts)
- [Sdk](#sdk)
- [Search](#search)
- [Security](#security)
- [Settings](#settings)
- [Setup](#setup)
- [Slash Commands](#slash-commands)
- [Src](#src)
- [Stargazers](#stargazers)
- [Tags](#tags)
- [Terminal Config](#terminal-config)
- [Test](#test)
- [Test Local.Sh](#test-local.sh)
- [Test Mcp Local.Sh](#test-mcp-local.sh)
- [Tests](#tests)
- [Third Party Integrations](#third-party-integrations)
- [Troubleshooting](#troubleshooting)
- [Tsconfig.Json](#tsconfig.json)
- [Tutorials](#tutorials)
- [Types.Py](#types.py)
- [Watchers](#watchers)


---

## .Devcontainer

*Source: https://docs.anthropic.com/anthropics/claude-code/tree/main/.devcontainer*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## .Gitattributes

*Source: https://docs.anthropic.com/anthropics/claude-code/blob/main/.gitattributes*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## .Gitignore

*Source: https://docs.anthropic.com/anthropics/claude-code-action/blob/main/.gitignore*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## .Npmrc

*Source: https://docs.anthropic.com/anthropics/claude-code-action/blob/main/.npmrc*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## .Prettierignore

*Source: https://docs.anthropic.com/anthropics/claude-code-action/blob/main/.prettierignore*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## .Prettierrc

*Source: https://docs.anthropic.com/anthropics/claude-code-base-action/blob/main/.prettierrc*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## .Vscode

*Source: https://docs.anthropic.com/anthropics/claude-code/tree/main/.vscode*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## 3368

*Source: https://github.com/anthropics/claude-code/issues/3368*

[anthropics](/anthropics) 
/
**[claude-code](/anthropics/claude-code)**
Public

* [Notifications](/login?return_to=%2Fanthropics%2Fclaude-code) You must be signed in to change notification settings
* [Fork
  1.3k](/login?return_to=%2Fanthropics%2Fclaude-code)
* [Star
   23.7k](/login?return_to=%2Fanthropics%2Fclaude-code)

* [Code](/anthropics/claude-code)
* [Issues
  1.9k](/anthropics/claude-code/issues)
* [Pull requests
  13](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security


  ### Uh oh!

  There was an error while loading. Please reload this page.](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

Additional navigation options


* [Code](/anthropics/claude-code)
* [Issues](/anthropics/claude-code/issues)
* [Pull requests](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

# [BUG] Shift + Tab is not working in powershell on windows native #3368

[New issue](/login?return_to=)

Copy link

[New issue](/login?return_to=)

Copy link

Open

Open

[[BUG] Shift + Tab is not working in powershell on windows native](#top)#3368

Copy link

Assignees

[![ant-kurt](https://avatars.githubusercontent.com/u/209710463?s=64&v=4)](/ant-kurt)

Labels

[area:tui](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22area%3Atui%22)[bugSomething isn't working](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22bug%22)Something isn't working[platform:windowsIssue specifically occurs on Windows](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22platform%3Awindows%22)Issue specifically occurs on Windows

[![@Twizzes](https://avatars.githubusercontent.com/u/1242212?v=4&size=80)](https://github.com/Twizzes)

## Description

[![@Twizzes](https://avatars.githubusercontent.com/u/1242212?v=4&size=48)](https://github.com/Twizzes)

[Twizzes](https://github.com/Twizzes)

opened [on Jul 12, 2025](https://github.com/anthropics/claude-code/issues/3368#issue-3224537893)

Issue body actions

## Environment

* Platform (select one):
  + Anthropic API
  + AWS Bedrock
  + Google Vertex AI
  + Other: Windows
* Claude CLI version: 1.0.51 (Claude Code)
* Operating System: Windows 11
* Terminal: powershell

## Bug Description

Hitting Shift + Tab is not changing mode to auto accept or planning mode

## Steps to Reproduce

1. Launch `claude` on windows in powershell or cmd on windows 11
2. Press Shift + Tab

## Expected Behavior

Editing mode shifts

## Actual Behavior

Nothing changes

## Additional Context

👍React with 👍40aklevecz, enesakdereliasset, naari3, thewpguy, HaimAbeles and 35 more

## Metadata

## Metadata

### Assignees

* [![@ant-kurt](https://avatars.githubusercontent.com/u/209710463?s=64&v=4)

  ant-kurt](/ant-kurt)

### Labels

[area:tui](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22area%3Atui%22)[bugSomething isn't working](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22bug%22)Something isn't working[platform:windowsIssue specifically occurs on Windows](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22platform%3Awindows%22)Issue specifically occurs on Windows

### Type

No type

### Projects

No projects

### Milestone

No milestone

### Relationships

None yet

### Development

No branches or pull requests

## Issue actions

---

## 3381

*Source: https://github.com/anthropics/claude-code/issues/3381*

[anthropics](/anthropics) 
/
**[claude-code](/anthropics/claude-code)**
Public

* [Notifications](/login?return_to=%2Fanthropics%2Fclaude-code) You must be signed in to change notification settings
* [Fork
  1.3k](/login?return_to=%2Fanthropics%2Fclaude-code)
* [Star
   23.7k](/login?return_to=%2Fanthropics%2Fclaude-code)

* [Code](/anthropics/claude-code)
* [Issues
  1.9k](/anthropics/claude-code/issues)
* [Pull requests
  13](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security


  ### Uh oh!

  There was an error while loading. Please reload this page.](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

Additional navigation options


* [Code](/anthropics/claude-code)
* [Issues](/anthropics/claude-code/issues)
* [Pull requests](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

# Windows VS Code extension crashes Claude Code with "Error: cannot open \_claude\_fs\_right:<file>. Detail: Unable to resolve filesystem provider with relative file path '\_claude\_fs\_right:<file>'" #3381

[New issue](/login?return_to=)

Copy link

[New issue](/login?return_to=)

Copy link

Open

Open

[Windows VS Code extension crashes Claude Code with "Error: cannot open \_claude\_fs\_right:<file>. Detail: Unable to resolve filesystem provider with relative file path '\_claude\_fs\_right:<file>'"](#top)#3381

Copy link

Assignees

[![ant-kurt](https://avatars.githubusercontent.com/u/209710463?s=64&v=4)](/ant-kurt)

Labels

[area:core](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22area%3Acore%22)[area:tools](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22area%3Atools%22)[bugSomething isn't working](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22bug%22)Something isn't working[has repro](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22has%20repro%22)[platform:windowsIssue specifically occurs on Windows](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22platform%3Awindows%22)Issue specifically occurs on Windows

[![@psandler](https://avatars.githubusercontent.com/u/753716?u=74406dec4b0746aefcc6cef92a3471c3949c8c9f&v=4&size=80)](https://github.com/psandler)

## Description

[![@psandler](https://avatars.githubusercontent.com/u/753716?u=74406dec4b0746aefcc6cef92a3471c3949c8c9f&v=4&size=48)](https://github.com/psandler)

[psandler](https://github.com/psandler)

opened [on Jul 12, 2025](https://github.com/anthropics/claude-code/issues/3381#issue-3224833916)

Issue body actions

Installed Claude Code via Powershell

It can read files without issue, but this is the error it crashes with when it tries to edit the file. The actual path, which is where claude is running, id c:\projects\TennisText and the CLAUDE.md file exists. The below is the summary and conclusion claude produced.

Bug Summary:  
Claude Code internal filesystem provider fails on Windows during file edit operations. Error shows malformed path: cannot open  
claudefs\_right:c%3A%5Cprojects%5CTennisText%5CCLAUDE.md with "Unable to resolve filesystem provider with relative file path  
'\_claude\_fs\_right:c:\projects\TennisText\CLAUDE.md'".

Environment:

* Windows (platform: win32)
* Claude Code's internal Edit/Write tools fail

Reproduction:

1. Attempt any file edit using Claude's Edit or Write tools
2. Claude Code crashes with filesystem provider path resolution error

Root Cause:  
Claude Code's internal path encoding/resolution creates invalid filesystem URIs on Windows. The \_claude\_fs\_right: prefix and URL-encoded

path (c%3A%5C) suggest incorrect internal path handling.

👍React with 👍26dminGod, ppkrol, DEllingsworth, alaanescobedo, eamsdev and 21 more

## Metadata

## Metadata

### Assignees

* [![@ant-kurt](https://avatars.githubusercontent.com/u/209710463?s=64&v=4)

  ant-kurt](/ant-kurt)

### Labels

[area:core](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22area%3Acore%22)[area:tools](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22area%3Atools%22)[bugSomething isn't working](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22bug%22)Something isn't working[has repro](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22has%20repro%22)[platform:windowsIssue specifically occurs on Windows](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22platform%3Awindows%22)Issue specifically occurs on Windows

### Type

No type

### Projects

No projects

### Milestone

No milestone

### Relationships

None yet

### Development

No branches or pull requests

## Issue actions

---

## 3634

*Source: https://docs.anthropic.com/anthropics/claude-code/issues/3634*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## 3635

*Source: https://docs.anthropic.com/anthropics/claude-code/issues/3635*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## 3636

*Source: https://docs.anthropic.com/anthropics/claude-code/issues/3636*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## 3637

*Source: https://docs.anthropic.com/anthropics/claude-code/issues/3637*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## 3638

*Source: https://docs.anthropic.com/anthropics/claude-code/issues/3638*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## 3639

*Source: https://docs.anthropic.com/anthropics/claude-code/issues/3639*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## 3643

*Source: https://docs.anthropic.com/anthropics/claude-code/issues/3643*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## 3645

*Source: https://docs.anthropic.com/anthropics/claude-code/issues/3645*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## 3647

*Source: https://docs.anthropic.com/anthropics/claude-code/issues/3647*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## 3648

*Source: https://docs.anthropic.com/anthropics/claude-code/issues/3648*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## 3649

*Source: https://docs.anthropic.com/anthropics/claude-code/issues/3649*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## 3650

*Source: https://docs.anthropic.com/anthropics/claude-code/issues/3650*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## 712

*Source: https://github.com/anthropics/claude-code/issues/712*

[anthropics](/anthropics) 
/
**[claude-code](/anthropics/claude-code)**
Public

* [Notifications](/login?return_to=%2Fanthropics%2Fclaude-code) You must be signed in to change notification settings
* [Fork
  1.3k](/login?return_to=%2Fanthropics%2Fclaude-code)
* [Star
   23.7k](/login?return_to=%2Fanthropics%2Fclaude-code)

* [Code](/anthropics/claude-code)
* [Issues
  1.9k](/anthropics/claude-code/issues)
* [Pull requests
  13](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security


  ### Uh oh!

  There was an error while loading. Please reload this page.](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

Additional navigation options


* [Code](/anthropics/claude-code)
* [Issues](/anthropics/claude-code/issues)
* [Pull requests](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

# Feature request: Hooks #712

[New issue](/login?return_to=)

Copy link

[New issue](/login?return_to=)

Copy link

Closed

Closed

[Feature request: Hooks](#top)#712

Copy link

Assignees

[![dicksontsai](https://avatars.githubusercontent.com/u/3757768?s=64&u=94e7118419e9418377b92b3dcae91065ce378588&v=4)](/dicksontsai)

Labels

[enhancementNew feature or request](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22enhancement%22)New feature or request

[![@backnotprop](https://avatars.githubusercontent.com/u/7244317?u=ca99a5717dd0ce83ad6e9f39a00489f84e501fbe&v=4&size=80)](https://github.com/backnotprop)

## Description

[![@backnotprop](https://avatars.githubusercontent.com/u/7244317?u=ca99a5717dd0ce83ad6e9f39a00489f84e501fbe&v=4&size=48)](https://github.com/backnotprop)

[backnotprop](https://github.com/backnotprop)

opened [on Apr 5, 2025](https://github.com/anthropics/claude-code/issues/712#issue-2973651699)

Issue body actions

Let me hook into the lifecycle of the agent(s) execution.

As an MVP, when CC completes a task.

I'm aware that this might be counter intuitive with agentic behaviors and the developer goals. But there are simple and high value efficiencies that hooks would give me and that I don't want to rely on the agent to conduct.

👍React with 👍27agentcooper, dcolascione, freddygv, maoberlehner, onerok and 22 more❤️React with ❤️4lebe-dev, Dillonjay, teren-papercutlabs and RunJerryDev

## Metadata

## Metadata

### Assignees

* [![@dicksontsai](https://avatars.githubusercontent.com/u/3757768?s=64&u=94e7118419e9418377b92b3dcae91065ce378588&v=4)

  dicksontsai](/dicksontsai)

### Labels

[enhancementNew feature or request](https://github.com/anthropics/claude-code/issues?q=state%3Aopen%20label%3A%22enhancement%22)New feature or request

### Type

No type

### Projects

No projects

### Milestone

No milestone

### Relationships

None yet

### Development

No branches or pull requests

## Issue actions

---

## Changelog.Md

*Source: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md*

[anthropics](/anthropics) 
/
**[claude-code](/anthropics/claude-code)**
Public

* [Notifications](/login?return_to=%2Fanthropics%2Fclaude-code) You must be signed in to change notification settings
* [Fork
  1.3k](/login?return_to=%2Fanthropics%2Fclaude-code)
* [Star
   23.7k](/login?return_to=%2Fanthropics%2Fclaude-code)

* [Code](/anthropics/claude-code)
* [Issues
  1.9k](/anthropics/claude-code/issues)
* [Pull requests
  13](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security


  ### Uh oh!

  There was an error while loading. Please reload this page.](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

Additional navigation options


* [Code](/anthropics/claude-code)
* [Issues](/anthropics/claude-code/issues)
* [Pull requests](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

---

## Dockerfile

*Source: https://github.com/anthropics/claude-code/blob/main/.devcontainer/Dockerfile*

[anthropics](/anthropics) 
/
**[claude-code](/anthropics/claude-code)**
Public

* [Notifications](/login?return_to=%2Fanthropics%2Fclaude-code) You must be signed in to change notification settings
* [Fork
  1.3k](/login?return_to=%2Fanthropics%2Fclaude-code)
* [Star
   23.7k](/login?return_to=%2Fanthropics%2Fclaude-code)

* [Code](/anthropics/claude-code)
* [Issues
  1.9k](/anthropics/claude-code/issues)
* [Pull requests
  13](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security


  ### Uh oh!

  There was an error while loading. Please reload this page.](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

Additional navigation options


* [Code](/anthropics/claude-code)
* [Issues](/anthropics/claude-code/issues)
* [Pull requests](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

---

## License

*Source: https://docs.anthropic.com/anthropics/claude-code-action/blob/main/LICENSE*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Script

*Source: https://docs.anthropic.com/anthropics/claude-code/tree/main/Script*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## _Errors.Py

*Source: https://docs.anthropic.com/anthropics/claude-code-sdk-python/blob/main/src/claude_code_sdk/_errors.py*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Action.Yml

*Source: https://docs.anthropic.com/anthropics/claude-code-action/blob/main/action.yml*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Actions

*Source: https://docs.anthropic.com/anthropics/claude-code-sdk-python/actions*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Activity

*Source: https://docs.anthropic.com/anthropics/claude-code-action/activity*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Amazon Bedrock

*Source: https://docs.anthropic.com/en/docs/claude-code/amazon-bedrock*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Deployment

# Claude Code on Amazon Bedrock

Copy page

Learn about configuring Claude Code through Amazon Bedrock, including setup, IAM configuration, and troubleshooting.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [1. Enable model access](#1-enable-model-access)
* [2. Configure AWS credentials](#2-configure-aws-credentials)
* [Advanced credential configuration](#advanced-credential-configuration)
* [3. Configure Claude Code](#3-configure-claude-code)
* [4. Model configuration](#4-model-configuration)
* [IAM configuration](#iam-configuration)
* [Troubleshooting](#troubleshooting)
* [Additional resources](#additional-resources)

---

## Analytics

*Source: https://docs.anthropic.com/en/docs/claude-code/analytics*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

Administration

Analytics

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
* [Analytics](/en/docs/claude-code/analytics)

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

Administration

# Analytics

Copy page

View detailed usage insights and productivity metrics for your organization’s Claude Code deployment.

Claude Code provides an analytics dashboard that helps organizations understand developer usage patterns, track productivity metrics, and optimize their Claude Code adoption.

Analytics are currently available only for organizations using Claude Code with the Anthropic API through the Anthropic Console.

## [​](#access-analytics) Access analytics

Navigate to the analytics dashboard at [console.anthropic.com/claude\_code](https://console.anthropic.com/claude_code).

### [​](#required-roles) Required roles

* **Primary Owner**
* **Owner**
* **Billing**
* **Admin**
* **Developer**

Users with **User**, **Claude Code User** or **Membership Admin** roles cannot access analytics.

## [​](#available-metrics) Available metrics

### [​](#lines-of-code-accepted) Lines of code accepted

Total lines of code written by Claude Code that users have accepted in their sessions.

* Excludes rejected code suggestions
* Doesn’t track subsequent deletions

### [​](#suggestion-accept-rate) Suggestion accept rate

Percentage of times users accept code editing tool usage, including:

* Edit
* MultiEdit
* Write
* NotebookEdit

### [​](#activity) Activity

**users**: Number of active users in a given day (number on left Y-axis)

**sessions**: Number of active sessions in a given day (number on right Y-axis)

### [​](#spend) Spend

**users**: Number of active users in a given day (number on left Y-axis)

**spend**: Total dollars spent in a given day (number on right Y-axis)

### [​](#team-insights) Team insights

**Members**: All users who have authenticated to Claude Code

* API key users are displayed by **API key identifier**
* OAuth users are displayed by **email address**

**Avg daily spend:** Per-user average spend for the current month. For example, on July 10, this reflects the average daily spend over 10 days.

**Avg lines/day:** Per-user average of accepted code lines for the current month.

## [​](#using-analytics-effectively) Using analytics effectively

### [​](#monitor-adoption) Monitor adoption

Track team member status to identify:

* Active users who can share best practices
* Overall adoption trends across your organization

### [​](#measure-productivity) Measure productivity

Tool acceptance rates and code metrics help you:

* Understand developer satisfaction with Claude Code suggestions
* Track code generation effectiveness
* Identify opportunities for training or process improvements

## [​](#related-resources) Related resources

* [Monitoring usage with OpenTelemetry](/en/docs/claude-code/monitoring-usage) for custom metrics and alerting
* [Identity and access management](/en/docs/claude-code/iam) for role configuration

Was this page helpful?

YesNo

[Costs](/en/docs/claude-code/costs)[Settings](/en/docs/claude-code/settings)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Access analytics](#access-analytics)
* [Required roles](#required-roles)
* [Available metrics](#available-metrics)
* [Lines of code accepted](#lines-of-code-accepted)
* [Suggestion accept rate](#suggestion-accept-rate)
* [Activity](#activity)
* [Spend](#spend)
* [Team insights](#team-insights)
* [Using analytics effectively](#using-analytics-effectively)
* [Monitor adoption](#monitor-adoption)
* [Measure productivity](#measure-productivity)
* [Related resources](#related-resources)

---

## Bash_Command_Validator_Example.Py

*Source: https://github.com/anthropics/claude-code/blob/main/examples/hooks/bash_command_validator_example.py*

[anthropics](/anthropics) 
/
**[claude-code](/anthropics/claude-code)**
Public

* [Notifications](/login?return_to=%2Fanthropics%2Fclaude-code) You must be signed in to change notification settings
* [Fork
  1.3k](/login?return_to=%2Fanthropics%2Fclaude-code)
* [Star
   23.7k](/login?return_to=%2Fanthropics%2Fclaude-code)

* [Code](/anthropics/claude-code)
* [Issues
  1.9k](/anthropics/claude-code/issues)
* [Pull requests
  13](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security


  ### Uh oh!

  There was an error while loading. Please reload this page.](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

Additional navigation options


* [Code](/anthropics/claude-code)
* [Issues](/anthropics/claude-code/issues)
* [Pull requests](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

---

## Bedrock Vertex

*Source: https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Deployment

# Enterprise deployment overview

Copy page

Learn how Claude Code can integrate with various third-party services and infrastructure to meet enterprise deployment requirements.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Provider comparison](#provider-comparison)
* [Cloud providers](#cloud-providers)
* [Corporate infrastructure](#corporate-infrastructure)
* [Configuration overview](#configuration-overview)
* [Using Bedrock with corporate proxy](#using-bedrock-with-corporate-proxy)
* [Using Bedrock with LLM Gateway](#using-bedrock-with-llm-gateway)
* [Using Vertex AI with corporate proxy](#using-vertex-ai-with-corporate-proxy)
* [Using Vertex AI with LLM Gateway](#using-vertex-ai-with-llm-gateway)
* [Authentication configuration](#authentication-configuration)
* [Choosing the right deployment configuration](#choosing-the-right-deployment-configuration)
* [Direct provider access](#direct-provider-access)
* [Corporate proxy](#corporate-proxy)
* [LLM Gateway](#llm-gateway)
* [Debugging](#debugging)
* [Best practices for organizations](#best-practices-for-organizations)
* [Next steps](#next-steps)

---

## Bedrock Vertex Proxies

*Source: https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Deployment

# Enterprise deployment overview

Copy page

Learn how Claude Code can integrate with various third-party services and infrastructure to meet enterprise deployment requirements.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Provider comparison](#provider-comparison)
* [Cloud providers](#cloud-providers)
* [Corporate infrastructure](#corporate-infrastructure)
* [Configuration overview](#configuration-overview)
* [Using Bedrock with corporate proxy](#using-bedrock-with-corporate-proxy)
* [Using Bedrock with LLM Gateway](#using-bedrock-with-llm-gateway)
* [Using Vertex AI with corporate proxy](#using-vertex-ai-with-corporate-proxy)
* [Using Vertex AI with LLM Gateway](#using-vertex-ai-with-llm-gateway)
* [Authentication configuration](#authentication-configuration)
* [Choosing the right deployment configuration](#choosing-the-right-deployment-configuration)
* [Direct provider access](#direct-provider-access)
* [Corporate proxy](#corporate-proxy)
* [LLM Gateway](#llm-gateway)
* [Debugging](#debugging)
* [Best practices for organizations](#best-practices-for-organizations)
* [Next steps](#next-steps)

---

## Beta

*Source: https://docs.anthropic.com/anthropics/claude-code-action/releases/tag/beta*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Branches

*Source: https://docs.anthropic.com/anthropics/claude-code/branches*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Bun.Lock

*Source: https://docs.anthropic.com/anthropics/claude-code-action/blob/main/bun.lock*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Claude Code

*Source: https://docs.anthropic.com/s/claude-code*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Getting started

# Claude Code overview

Copy page

Learn about Claude Code, Anthropic’s agentic coding tool that lives in your terminal and helps you turn ideas into code faster than ever before.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Get started in 30 seconds](#get-started-in-30-seconds)
* [What Claude Code does for you](#what-claude-code-does-for-you)
* [Why developers love Claude Code](#why-developers-love-claude-code)
* [Next steps](#next-steps)
* [Additional resources](#additional-resources)

---

## Claude Code Action

*Source: https://github.com/anthropics/claude-code-action*

[anthropics](/anthropics) 
/
**[claude-code-action](/anthropics/claude-code-action)**
Public

* [Notifications](/login?return_to=%2Fanthropics%2Fclaude-code-action) You must be signed in to change notification settings
* [Fork
  931](/login?return_to=%2Fanthropics%2Fclaude-code-action)
* [Star
   1.9k](/login?return_to=%2Fanthropics%2Fclaude-code-action)

### License

[MIT license](/anthropics/claude-code-action/blob/main/LICENSE)

[1.9k
stars](/anthropics/claude-code-action/stargazers) [931
forks](/anthropics/claude-code-action/forks) [Branches](/anthropics/claude-code-action/branches) [Tags](/anthropics/claude-code-action/tags) [Activity](/anthropics/claude-code-action/activity)

[Star](/login?return_to=%2Fanthropics%2Fclaude-code-action)

[Notifications](/login?return_to=%2Fanthropics%2Fclaude-code-action) You must be signed in to change notification settings

* [Code](/anthropics/claude-code-action)
* [Issues
  76](/anthropics/claude-code-action/issues)
* [Pull requests
  23](/anthropics/claude-code-action/pulls)
* [Discussions](/anthropics/claude-code-action/discussions)
* [Actions](/anthropics/claude-code-action/actions)
* [Projects
  0](/anthropics/claude-code-action/projects)
* [Security


  ### Uh oh!

  There was an error while loading. Please reload this page.](/anthropics/claude-code-action/security)
* [Insights](/anthropics/claude-code-action/pulse)

Additional navigation options


* [Code](/anthropics/claude-code-action)
* [Issues](/anthropics/claude-code-action/issues)
* [Pull requests](/anthropics/claude-code-action/pulls)
* [Discussions](/anthropics/claude-code-action/discussions)
* [Actions](/anthropics/claude-code-action/actions)
* [Projects](/anthropics/claude-code-action/projects)
* [Security](/anthropics/claude-code-action/security)
* [Insights](/anthropics/claude-code-action/pulse)

# anthropics/claude-code-action

Use this GitHub action with your project

Add this Action to an existing workflow or create a new one

[View on Marketplace](/marketplace/actions/claude-code-action-official)

main

[Branches](/anthropics/claude-code-action/branches)[Tags](/anthropics/claude-code-action/tags)

Go to file

Code

Open more actions menu

## Folders and files

| Name | | Name | Last commit message | Last commit date |
| --- | --- | --- | --- | --- |
| Latest commit   History[134 Commits](/anthropics/claude-code-action/commits/main/) | | |
| [.claude/commands](/anthropics/claude-code-action/tree/main/.claude/commands "This path skips through empty directories") | | [.claude/commands](/anthropics/claude-code-action/tree/main/.claude/commands "This path skips through empty directories") |  |  |
| [.github](/anthropics/claude-code-action/tree/main/.github ".github") | | [.github](/anthropics/claude-code-action/tree/main/.github ".github") |  |  |
| [examples](/anthropics/claude-code-action/tree/main/examples "examples") | | [examples](/anthropics/claude-code-action/tree/main/examples "examples") |  |  |
| [scripts](/anthropics/claude-code-action/tree/main/scripts "scripts") | | [scripts](/anthropics/claude-code-action/tree/main/scripts "scripts") |  |  |
| [src](/anthropics/claude-code-action/tree/main/src "src") | | [src](/anthropics/claude-code-action/tree/main/src "src") |  |  |
| [test](/anthropics/claude-code-action/tree/main/test "test") | | [test](/anthropics/claude-code-action/tree/main/test "test") |  |  |
| [.gitignore](/anthropics/claude-code-action/blob/main/.gitignore ".gitignore") | | [.gitignore](/anthropics/claude-code-action/blob/main/.gitignore ".gitignore") |  |  |
| [.npmrc](/anthropics/claude-code-action/blob/main/.npmrc ".npmrc") | | [.npmrc](/anthropics/claude-code-action/blob/main/.npmrc ".npmrc") |  |  |
| [.prettierignore](/anthropics/claude-code-action/blob/main/.prettierignore ".prettierignore") | | [.prettierignore](/anthropics/claude-code-action/blob/main/.prettierignore ".prettierignore") |  |  |
| [.prettierrc](/anthropics/claude-code-action/blob/main/.prettierrc ".prettierrc") | | [.prettierrc](/anthropics/claude-code-action/blob/main/.prettierrc ".prettierrc") |  |  |
| [CLAUDE.md](/anthropics/claude-code-action/blob/main/CLAUDE.md "CLAUDE.md") | | [CLAUDE.md](/anthropics/claude-code-action/blob/main/CLAUDE.md "CLAUDE.md") |  |  |
| [CODE\_OF\_CONDUCT.md](/anthropics/claude-code-action/blob/main/CODE_OF_CONDUCT.md "CODE_OF_CONDUCT.md") | | [CODE\_OF\_CONDUCT.md](/anthropics/claude-code-action/blob/main/CODE_OF_CONDUCT.md "CODE_OF_CONDUCT.md") |  |  |
| [CONTRIBUTING.md](/anthropics/claude-code-action/blob/main/CONTRIBUTING.md "CONTRIBUTING.md") | | [CONTRIBUTING.md](/anthropics/claude-code-action/blob/main/CONTRIBUTING.md "CONTRIBUTING.md") |  |  |
| [FAQ.md](/anthropics/claude-code-action/blob/main/FAQ.md "FAQ.md") | | [FAQ.md](/anthropics/claude-code-action/blob/main/FAQ.md "FAQ.md") |  |  |
| [LICENSE](/anthropics/claude-code-action/blob/main/LICENSE "LICENSE") | | [LICENSE](/anthropics/claude-code-action/blob/main/LICENSE "LICENSE") |  |  |
| [README.md](/anthropics/claude-code-action/blob/main/README.md "README.md") | | [README.md](/anthropics/claude-code-action/blob/main/README.md "README.md") |  |  |
| [ROADMAP.md](/anthropics/claude-code-action/blob/main/ROADMAP.md "ROADMAP.md") | | [ROADMAP.md](/anthropics/claude-code-action/blob/main/ROADMAP.md "ROADMAP.md") |  |  |
| [SECURITY.md](/anthropics/claude-code-action/blob/main/SECURITY.md "SECURITY.md") | | [SECURITY.md](/anthropics/claude-code-action/blob/main/SECURITY.md "SECURITY.md") |  |  |
| [action.yml](/anthropics/claude-code-action/blob/main/action.yml "action.yml") | | [action.yml](/anthropics/claude-code-action/blob/main/action.yml "action.yml") |  |  |
| [bun.lock](/anthropics/claude-code-action/blob/main/bun.lock "bun.lock") | | [bun.lock](/anthropics/claude-code-action/blob/main/bun.lock "bun.lock") |  |  |
| [package.json](/anthropics/claude-code-action/blob/main/package.json "package.json") | | [package.json](/anthropics/claude-code-action/blob/main/package.json "package.json") |  |  |
| [tsconfig.json](/anthropics/claude-code-action/blob/main/tsconfig.json "tsconfig.json") | | [tsconfig.json](/anthropics/claude-code-action/blob/main/tsconfig.json "tsconfig.json") |  |  |
| View all files | | |

## Repository files navigation

* [README](#)
* [Code of conduct](#)
* [MIT license](#)
* [Security](#)

[![Claude Code Action responding to a comment](https://private-user-images.githubusercontent.com/199845480/446629003-1d60c2e9-82ed-4ee5-b749-f9e021c85f4d.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTI2OTU4NDcsIm5iZiI6MTc1MjY5NTU0NywicGF0aCI6Ii8xOTk4NDU0ODAvNDQ2NjI5MDAzLTFkNjBjMmU5LTgyZWQtNGVlNS1iNzQ5LWY5ZTAyMWM4NWY0ZC5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcxNlQxOTUyMjdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yOGM3MjZmMjYzOTM3OTNmOWFkMDhmMzllYTQxNzgzYmQyMDI4Y2MwZmU4NmRiZmRjM2JjYzA0YmI0MjUyMDYyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.aVnW8TpCrmn6KQbHjhVy03tvCBuOn530DIGNvIxLvxk)](https://private-user-images.githubusercontent.com/199845480/446629003-1d60c2e9-82ed-4ee5-b749-f9e021c85f4d.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTI2OTU4NDcsIm5iZiI6MTc1MjY5NTU0NywicGF0aCI6Ii8xOTk4NDU0ODAvNDQ2NjI5MDAzLTFkNjBjMmU5LTgyZWQtNGVlNS1iNzQ5LWY5ZTAyMWM4NWY0ZC5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcxNlQxOTUyMjdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yOGM3MjZmMjYzOTM3OTNmOWFkMDhmMzllYTQxNzgzYmQyMDI4Y2MwZmU4NmRiZmRjM2JjYzA0YmI0MjUyMDYyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.aVnW8TpCrmn6KQbHjhVy03tvCBuOn530DIGNvIxLvxk)

# Claude Code Action

A general-purpose [Claude Code](https://claude.ai/code) action for GitHub PRs and issues that can answer questions and implement code changes. This action listens for a trigger phrase in comments and activates Claude act on the request. It supports multiple authentication methods including Anthropic direct API, Amazon Bedrock, and Google Vertex AI.

## Features

* 🤖 **Interactive Code Assistant**: Claude can answer questions about code, architecture, and programming
* 🔍 **Code Review**: Analyzes PR changes and suggests improvements
* ✨ **Code Implementation**: Can implement simple fixes, refactoring, and even new features
* 💬 **PR/Issue Integration**: Works seamlessly with GitHub comments and PR reviews
* 🛠️ **Flexible Tool Access**: Access to GitHub APIs and file operations (additional tools can be enabled via configuration)
* 📋 **Progress Tracking**: Visual progress indicators with checkboxes that dynamically update as Claude completes tasks
* 🏃 **Runs on Your Infrastructure**: The action executes entirely on your own GitHub runner (Anthropic API calls go to your chosen provider)

## Quickstart

The easiest way to set up this action is through [Claude Code](https://claude.ai/code) in the terminal. Just open `claude` and run `/install-github-app`.

This command will guide you through setting up the GitHub app and required secrets.

**Note**:

* You must be a repository admin to install the GitHub app and add secrets
* This quickstart method is only available for direct Anthropic API users. If you're using AWS Bedrock, please see the instructions below.

### Manual Setup (Direct API)

**Requirements**: You must be a repository admin to complete these steps.

1. Install the Claude GitHub app to your repository: <https://github.com/apps/claude>
2. Add authentication to your repository secrets ([Learn how to use secrets in GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)):
   * Either `ANTHROPIC_API_KEY` for API key authentication
   * Or `CLAUDE_CODE_OAUTH_TOKEN` for OAuth token authentication (Pro and Max users can generate this by running `claude setup-token` locally)
3. Copy the workflow file from [`examples/claude.yml`](/anthropics/claude-code-action/blob/main/examples/claude.yml) into your repository's `.github/workflows/`

### Using a Custom GitHub App

If you prefer not to install the official Claude app, you can create your own GitHub App to use with this action. This gives you complete control over permissions and access.

**When you may want to use a custom GitHub App:**

* You need more restrictive permissions than the official app
* Organization policies prevent installing third-party apps
* You're using AWS Bedrock or Google Vertex AI

**Steps to create and use a custom GitHub App:**

1. **Create a new GitHub App:**

   * Go to <https://github.com/settings/apps> (for personal apps) or your organization's settings
   * Click "New GitHub App"
   * Configure the app with these minimum permissions:
     + **Repository permissions:**
       - Contents: Read & Write
       - Issues: Read & Write
       - Pull requests: Read & Write
     + **Account permissions:** None required
   * Set "Where can this GitHub App be installed?" to your preference
   * Create the app
2. **Generate and download a private key:**

   * After creating the app, scroll down to "Private keys"
   * Click "Generate a private key"
   * Download the `.pem` file (keep this secure!)
3. **Install the app on your repository:**

   * Go to the app's settings page
   * Click "Install App"
   * Select the repositories where you want to use Claude
4. **Add the app credentials to your repository secrets:**

   * Go to your repository's Settings → Secrets and variables → Actions
   * Add these secrets:
     + `APP_ID`: Your GitHub App's ID (found in the app settings)
     + `APP_PRIVATE_KEY`: The contents of the downloaded `.pem` file
5. **Update your workflow to use the custom app:**

   ```
   name: Claude with Custom App
   on:
     issue_comment:
       types: [created]
     # ... other triggers

   jobs:
     claude-response:
       runs-on: ubuntu-latest
       steps:
         # Generate a token from your custom app
         - name: Generate GitHub App token
           id: app-token
           uses: actions/create-github-app-token@v1
           with:
             app-id: ${{ secrets.APP_ID }}
             private-key: ${{ secrets.APP_PRIVATE_KEY }}

         # Use Claude with your custom app's token
         - uses: anthropics/claude-code-action@beta
           with:
             anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
             github_token: ${{ steps.app-token.outputs.token }}
             # ... other configuration
   ```

**Important notes:**

* The custom app must have read/write permissions for Issues, Pull Requests, and Contents
* Your app's token will have the exact permissions you configured, nothing more

For more information on creating GitHub Apps, see the [GitHub documentation](https://docs.github.com/en/apps/creating-github-apps).

## 📚 FAQ

Having issues or questions? Check out our [Frequently Asked Questions](/anthropics/claude-code-action/blob/main/FAQ.md) for solutions to common problems and detailed explanations of Claude's capabilities and limitations.

## Usage

Add a workflow file to your repository (e.g., `.github/workflows/claude.yml`):

```
name: Claude Assistant
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
  issues:
    types: [opened, assigned, labeled]
  pull_request_review:
    types: [submitted]

jobs:
  claude-response:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@beta
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          # Or use OAuth token instead:
          # claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          # Optional: add custom trigger phrase (default: @claude)
          # trigger_phrase: "/claude"
          # Optional: add assignee trigger for issues
          # assignee_trigger: "claude"
          # Optional: add label trigger for issues
          # label_trigger: "claude"
          # Optional: add custom environment variables (YAML format)
          # claude_env: |
          #   NODE_ENV: test
          #   DEBUG: true
          #   API_URL: https://api.example.com
          # Optional: limit the number of conversation turns
          # max_turns: "5"
          # Optional: grant additional permissions (requires corresponding GitHub token permissions)
          # additional_permissions: |
          #   actions: read
```

## Inputs

| Input | Description | Required | Default |
| --- | --- | --- | --- |
| `anthropic_api_key` | Anthropic API key (required for direct API, not needed for Bedrock/Vertex) | No\* | - |
| `claude_code_oauth_token` | Claude Code OAuth token (alternative to anthropic\_api\_key) | No\* | - |
| `direct_prompt` | Direct prompt for Claude to execute automatically without needing a trigger (for automated workflows) | No | - |
| `base_branch` | The base branch to use for creating new branches (e.g., 'main', 'develop') | No | - |
| `max_turns` | Maximum number of conversation turns Claude can take (limits back-and-forth exchanges) | No | - |
| `timeout_minutes` | Timeout in minutes for execution | No | `30` |
| `use_sticky_comment` | Use just one comment to deliver PR comments (only applies for pull\_request event workflows) | No | `false` |
| `github_token` | GitHub token for Claude to operate with. **Only include this if you're connecting a custom GitHub app of your own!** | No | - |
| `model` | Model to use (provider-specific format required for Bedrock/Vertex) | No | - |
| `fallback_model` | Enable automatic fallback to specified model when primary model is unavailable | No | - |
| `anthropic_model` | **DEPRECATED**: Use `model` instead. Kept for backward compatibility. | No | - |
| `use_bedrock` | Use Amazon Bedrock with OIDC authentication instead of direct Anthropic API | No | `false` |
| `use_vertex` | Use Google Vertex AI with OIDC authentication instead of direct Anthropic API | No | `false` |
| `allowed_tools` | Additional tools for Claude to use (the base GitHub tools will always be included) | No | "" |
| `disallowed_tools` | Tools that Claude should never use | No | "" |
| `custom_instructions` | Additional custom instructions to include in the prompt for Claude | No | "" |
| `mcp_config` | Additional MCP configuration (JSON string) that merges with the built-in GitHub MCP servers | No | "" |
| `assignee_trigger` | The assignee username that triggers the action (e.g. @claude). Only used for issue assignment | No | - |
| `label_trigger` | The label name that triggers the action when applied to an issue (e.g. "claude") | No | - |
| `trigger_phrase` | The trigger phrase to look for in comments, issue/PR bodies, and issue titles | No | `@claude` |
| `branch_prefix` | The prefix to use for Claude branches (defaults to 'claude/', use 'claude-' for dash format) | No | `claude/` |
| `claude_env` | Custom environment variables to pass to Claude Code execution (YAML format) | No | "" |
| `settings` | Claude Code settings as JSON string or path to settings JSON file | No | "" |
| `additional_permissions` | Additional permissions to enable. Currently supports 'actions: read' for viewing workflow results | No | "" |
| `experimental_allowed_domains` | Restrict network access to these domains only (newline-separated). | No | "" |
| `use_commit_signing` | Enable commit signing using GitHub's commit signature verification. When false, Claude uses standard git commands | No | `false` |

\*Required when using direct Anthropic API (default and when not using Bedrock or Vertex)

> **Note**: This action is currently in beta. Features and APIs may change as we continue to improve the integration.

### Using Custom MCP Configuration

The `mcp_config` input allows you to add custom MCP (Model Context Protocol) servers to extend Claude's capabilities. These servers merge with the built-in GitHub MCP servers.

#### Basic Example: Adding a Sequential Thinking Server

```
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    mcp_config: |
      {
        "mcpServers": {
          "sequential-thinking": {
            "command": "npx",
            "args": [
              "-y",
              "@modelcontextprotocol/server-sequential-thinking"
            ]
          }
        }
      }
    allowed_tools: "mcp__sequential-thinking__sequentialthinking" # Important: Each MCP tool from your server must be listed here, comma-separated
    # ... other inputs
```

#### Passing Secrets to MCP Servers

For MCP servers that require sensitive information like API keys or tokens, use GitHub Secrets in the environment variables:

```
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    mcp_config: |
      {
        "mcpServers": {
          "custom-api-server": {
            "command": "npx",
            "args": ["-y", "@example/api-server"],
            "env": {
              "API_KEY": "${{ secrets.CUSTOM_API_KEY }}",
              "BASE_URL": "https://api.example.com"
            }
          }
        }
      }
    # ... other inputs
```

#### Using Python MCP Servers with uv

For Python-based MCP servers managed with `uv`, you need to specify the directory containing your server:

```
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    mcp_config: |
      {
        "mcpServers": {
          "my-python-server": {
            "type": "stdio",
            "command": "uv",
            "args": [
              "--directory",
              "${{ github.workspace }}/path/to/server/",
              "run",
              "server_file.py"
            ]
          }
        }
      }
    allowed_tools: "my-python-server__<tool_name>" # Replace <tool_name> with your server's tool names
    # ... other inputs
```

For example, if your Python MCP server is at `mcp_servers/weather.py`, you would use:

```
"args":
  ["--directory", "${{ github.workspace }}/mcp_servers/", "run", "weather.py"]
```

**Important**:

* Always use GitHub Secrets (`${{ secrets.SECRET_NAME }}`) for sensitive values like API keys, tokens, or passwords. Never hardcode secrets directly in the workflow file.
* Your custom servers will override any built-in servers with the same name.

## Examples

### Ways to Tag @claude

These examples show how to interact with Claude using comments in PRs and issues. By default, Claude will be triggered anytime you mention `@claude`, but you can customize the exact trigger phrase using the `trigger_phrase` input in the workflow.

Claude will see the full PR context, including any comments.

#### Ask Questions

Add a comment to a PR or issue:

```
@claude What does this function do and how could we improve it?

```

Claude will analyze the code and provide a detailed explanation with suggestions.

#### Request Fixes

Ask Claude to implement specific changes:

```
@claude Can you add error handling to this function?

```

#### Code Review

Get a thorough review:

```
@claude Please review this PR and suggest improvements

```

Claude will analyze the changes and provide feedback.

#### Fix Bugs from Screenshots

Upload a screenshot of a bug and ask Claude to fix it:

```
@claude Here's a screenshot of a bug I'm seeing [upload screenshot]. Can you fix it?

```

Claude can see and analyze images, making it easy to fix visual bugs or UI issues.

### Custom Automations

These examples show how to configure Claude to act automatically based on GitHub events, without requiring manual @mentions.

#### Supported GitHub Events

This action supports the following GitHub events ([learn more GitHub event triggers](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)):

* `pull_request` - When PRs are opened or synchronized
* `issue_comment` - When comments are created on issues or PRs
* `pull_request_comment` - When comments are made on PR diffs
* `issues` - When issues are opened or assigned
* `pull_request_review` - When PR reviews are submitted
* `pull_request_review_comment` - When comments are made on PR reviews
* `repository_dispatch` - Custom events triggered via API (coming soon)
* `workflow_dispatch` - Manual workflow triggers (coming soon)

#### Automated Documentation Updates

Automatically update documentation when specific files change (see [`examples/claude-pr-path-specific.yml`](/anthropics/claude-code-action/blob/main/examples/claude-pr-path-specific.yml)):

```
on:
  pull_request:
    paths:
      - "src/api/**/*.ts"

steps:
  - uses: anthropics/claude-code-action@beta
    with:
      direct_prompt: |
        Update the API documentation in README.md to reflect
        the changes made to the API endpoints in this PR.
```

When API files are modified, Claude automatically updates your README with the latest endpoint documentation and pushes the changes back to the PR, keeping your docs in sync with your code.

#### Author-Specific Code Reviews

Automatically review PRs from specific authors or external contributors (see [`examples/claude-review-from-author.yml`](/anthropics/claude-code-action/blob/main/examples/claude-review-from-author.yml)):

```
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review-by-author:
    if: |
      github.event.pull_request.user.login == 'developer1' ||
      github.event.pull_request.user.login == 'external-contributor'
    steps:
      - uses: anthropics/claude-code-action@beta
        with:
          direct_prompt: |
            Please provide a thorough review of this pull request.
            Pay extra attention to coding standards, security practices,
            and test coverage since this is from an external contributor.
```

Perfect for automatically reviewing PRs from new team members, external contributors, or specific developers who need extra guidance.

## How It Works

1. **Trigger Detection**: Listens for comments containing the trigger phrase (default: `@claude`) or issue assignment to a specific user
2. **Context Gathering**: Analyzes the PR/issue, comments, code changes
3. **Smart Responses**: Either answers questions or implements changes
4. **Branch Management**: Creates new PRs for human authors, pushes directly for Claude's own PRs
5. **Communication**: Posts updates at every step to keep you informed

This action is built on top of [`anthropics/claude-code-base-action`](https://github.com/anthropics/claude-code-base-action).

## Capabilities and Limitations

### What Claude Can Do

* **Respond in a Single Comment**: Claude operates by updating a single initial comment with progress and results
* **Answer Questions**: Analyze code and provide explanations
* **Implement Code Changes**: Make simple to moderate code changes based on requests
* **Prepare Pull Requests**: Creates commits on a branch and links back to a prefilled PR creation page
* **Perform Code Reviews**: Analyze PR changes and provide detailed feedback
* **Smart Branch Handling**:
  + When triggered on an **issue**: Always creates a new branch for the work
  + When triggered on an **open PR**: Always pushes directly to the existing PR branch
  + When triggered on a **closed PR**: Creates a new branch since the original is no longer active
* **View GitHub Actions Results**: Can access workflow runs, job logs, and test results on the PR where it's tagged when `actions: read` permission is configured (see [Additional Permissions for CI/CD Integration](#additional-permissions-for-cicd-integration))

### What Claude Cannot Do

* **Submit PR Reviews**: Claude cannot submit formal GitHub PR reviews
* **Approve PRs**: For security reasons, Claude cannot approve pull requests
* **Post Multiple Comments**: Claude only acts by updating its initial comment
* **Execute Commands Outside Its Context**: Claude only has access to the repository and PR/issue context it's triggered in
* **Run Arbitrary Bash Commands**: By default, Claude cannot execute Bash commands unless explicitly allowed using the `allowed_tools` configuration
* **Perform Branch Operations**: Cannot merge branches, rebase, or perform other git operations beyond pushing commits

## Advanced Configuration

### Additional Permissions for CI/CD Integration

The `additional_permissions` input allows Claude to access GitHub Actions workflow information when you grant the necessary permissions. This is particularly useful for analyzing CI/CD failures and debugging workflow issues.

#### Enabling GitHub Actions Access

To allow Claude to view workflow run results, job logs, and CI status:

1. **Grant the necessary permission to your GitHub token**:

   * When using the default `GITHUB_TOKEN`, add the `actions: read` permission to your workflow:

   ```
   permissions:
     contents: write
     pull-requests: write
     issues: write
     actions: read # Add this line
   ```
2. **Configure the action with additional permissions**:

   ```
   - uses: anthropics/claude-code-action@beta
     with:
       anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
       additional_permissions: |
         actions: read
       # ... other inputs
   ```
3. **Claude will automatically get access to CI/CD tools**:
   When you enable `actions: read`, Claude can use the following MCP tools:

   * `mcp__github_ci__get_ci_status` - View workflow run statuses
   * `mcp__github_ci__get_workflow_run_details` - Get detailed workflow information
   * `mcp__github_ci__download_job_log` - Download and analyze job logs

#### Example: Debugging Failed CI Runs

```
name: Claude CI Helper
on:
  issue_comment:
    types: [created]

permissions:
  contents: write
  pull-requests: write
  issues: write
  actions: read # Required for CI access

jobs:
  claude-ci-helper:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@beta
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          additional_permissions: |
            actions: read
          # Now Claude can respond to "@claude why did the CI fail?"
```

**Important Notes**:

* The GitHub token must have the `actions: read` permission in your workflow
* If the permission is missing, Claude will warn you and suggest adding it
* Currently, only `actions: read` is supported, but the format allows for future extensions

### Custom Environment Variables

You can pass custom environment variables to Claude Code execution using the `claude_env` input. This is useful for CI/test setups that require specific environment variables:

```
- uses: anthropics/claude-code-action@beta
  with:
    claude_env: |
      NODE_ENV: test
      CI: true
      DATABASE_URL: postgres://test:test@localhost:5432/test_db
    # ... other inputs
```

The `claude_env` input accepts YAML format where each line defines a key-value pair. These environment variables will be available to Claude Code during execution, allowing it to run tests, build processes, or other commands that depend on specific environment configurations.

### Limiting Conversation Turns

You can use the `max_turns` parameter to limit the number of back-and-forth exchanges Claude can have during task execution. This is useful for:

* Controlling costs by preventing runaway conversations
* Setting time boundaries for automated workflows
* Ensuring predictable behavior in CI/CD pipelines

```
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    max_turns: "5" # Limit to 5 conversation turns
    # ... other inputs
```

When the turn limit is reached, Claude will stop execution gracefully. Choose a value that gives Claude enough turns to complete typical tasks while preventing excessive usage.

### Custom Tools

By default, Claude only has access to:

* File operations (reading, committing, editing files, read-only git commands)
* Comment management (creating/updating comments)
* Basic GitHub operations

Claude does **not** have access to execute arbitrary Bash commands by default. If you want Claude to run specific commands (e.g., npm install, npm test), you must explicitly allow them using the `allowed_tools` configuration:

**Note**: If your repository has a `.mcp.json` file in the root directory, Claude will automatically detect and use the MCP server tools defined there. However, these tools still need to be explicitly allowed via the `allowed_tools` configuration.

```
- uses: anthropics/claude-code-action@beta
  with:
    allowed_tools: |
      Bash(npm install)
      Bash(npm run test)
      Edit
      Replace
      NotebookEditCell
    disallowed_tools: |
      TaskOutput
      KillTask
    # ... other inputs
```

**Note**: The base GitHub tools are always included. Use `allowed_tools` to add additional tools (including specific Bash commands), and `disallowed_tools` to prevent specific tools from being used.

### Custom Model

Use a specific Claude model:

```
- uses: anthropics/claude-code-action@beta
  with:
    # model: "claude-3-5-sonnet-20241022"  # Optional: specify a different model
    # ... other inputs
```

### Network Restrictions

For enhanced security, you can restrict Claude's network access to specific domains only. This feature is particularly useful for:

* Enterprise environments with strict security policies
* Preventing access to external services
* Limiting Claude to only your internal APIs and services

When `experimental_allowed_domains` is set, Claude can only access the domains you explicitly list. You'll need to include the appropriate provider domains based on your authentication method.

#### Provider-Specific Examples

##### If using Anthropic API or subscription

```
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    # Or: claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
    experimental_allowed_domains: |
      .anthropic.com
```

##### If using AWS Bedrock

```
- uses: anthropics/claude-code-action@beta
  with:
    use_bedrock: "true"
    experimental_allowed_domains: |
      bedrock.*.amazonaws.com
      bedrock-runtime.*.amazonaws.com
```

##### If using Google Vertex AI

```
- uses: anthropics/claude-code-action@beta
  with:
    use_vertex: "true"
    experimental_allowed_domains: |
      *.googleapis.com
      vertexai.googleapis.com
```

#### Common GitHub Domains

In addition to your provider domains, you may need to include GitHub-related domains. For GitHub.com users, common domains include:

```
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    experimental_allowed_domains: |
      .anthropic.com  # For Anthropic API
      .github.com
      .githubusercontent.com
      ghcr.io
      .blob.core.windows.net
```

For GitHub Enterprise users, replace the GitHub.com domains above with your enterprise domains (e.g., `.github.company.com`, `packages.company.com`, etc.).

To determine which domains your workflow needs, you can temporarily run without restrictions and monitor the network requests, or check your GitHub Enterprise configuration for the specific services you use.

### Claude Code Settings

You can provide Claude Code settings to customize behavior such as model selection, environment variables, permissions, and hooks. Settings can be provided either as a JSON string or a path to a settings file.

#### Option 1: Settings File

```
- uses: anthropics/claude-code-action@beta
  with:
    settings: "path/to/settings.json"
    # ... other inputs
```

#### Option 2: Inline Settings

```
- uses: anthropics/claude-code-action@beta
  with:
    settings: |
      {
        "model": "claude-opus-4-20250514",
        "env": {
          "DEBUG": "true",
          "API_URL": "https://api.example.com"
        },
        "permissions": {
          "allow": ["Bash", "Read"],
          "deny": ["WebFetch"]
        },
        "hooks": {
          "PreToolUse": [{
            "matcher": "Bash",
            "hooks": [{
              "type": "command",
              "command": "echo Running bash command..."
            }]
          }]
        }
      }
    # ... other inputs
```

The settings support all Claude Code settings options including:

* `model`: Override the default model
* `env`: Environment variables for the session
* `permissions`: Tool usage permissions
* `hooks`: Pre/post tool execution hooks
* And more...

For a complete list of available settings and their descriptions, see the [Claude Code settings documentation](https://docs.anthropic.com/en/docs/claude-code/settings).

**Notes**:

* The `enableAllProjectMcpServers` setting is always set to `true` by this action to ensure MCP servers work correctly.
* If both the `model` input parameter and a `model` in settings are provided, the `model` input parameter takes precedence.
* The `allowed_tools` and `disallowed_tools` input parameters take precedence over `permissions` in settings.
* In a future version, we may deprecate individual input parameters in favor of using the settings file for all configuration.

## Cloud Providers

You can authenticate with Claude using any of these three methods:

1. Direct Anthropic API (default)
2. Amazon Bedrock with OIDC authentication
3. Google Vertex AI with OIDC authentication

For detailed setup instructions for AWS Bedrock and Google Vertex AI, see the [official documentation](https://docs.anthropic.com/en/docs/claude-code/github-actions#using-with-aws-bedrock-%26-google-vertex-ai).

**Note**:

* Bedrock and Vertex use OIDC authentication exclusively
* AWS Bedrock automatically uses cross-region inference profiles for certain models
* For cross-region inference profile models, you need to request and be granted access to the Claude models in all regions that the inference profile uses

### Model Configuration

Use provider-specific model names based on your chosen provider:

```
# For direct Anthropic API (default)
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    # ... other inputs

# For Amazon Bedrock with OIDC
- uses: anthropics/claude-code-action@beta
  with:
    model: "anthropic.claude-3-7-sonnet-20250219-beta:0" # Cross-region inference
    use_bedrock: "true"
    # ... other inputs

# For Google Vertex AI with OIDC
- uses: anthropics/claude-code-action@beta
  with:
    model: "claude-3-7-sonnet@20250219"
    use_vertex: "true"
    # ... other inputs
```

### OIDC Authentication for Bedrock and Vertex

Both AWS Bedrock and GCP Vertex AI require OIDC authentication.

```
# For AWS Bedrock with OIDC
- name: Configure AWS Credentials (OIDC)
  uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: ${{ secrets.AWS_ROLE_TO_ASSUME }}
    aws-region: us-west-2

- name: Generate GitHub App token
  id: app-token
  uses: actions/create-github-app-token@v2
  with:
    app-id: ${{ secrets.APP_ID }}
    private-key: ${{ secrets.APP_PRIVATE_KEY }}

- uses: anthropics/claude-code-action@beta
  with:
    model: "anthropic.claude-3-7-sonnet-20250219-beta:0"
    use_bedrock: "true"
    # ... other inputs

  permissions:
    id-token: write # Required for OIDC
```

```
# For GCP Vertex AI with OIDC
- name: Authenticate to Google Cloud
  uses: google-github-actions/auth@v2
  with:
    workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
    service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}

- name: Generate GitHub App token
  id: app-token
  uses: actions/create-github-app-token@v2
  with:
    app-id: ${{ secrets.APP_ID }}
    private-key: ${{ secrets.APP_PRIVATE_KEY }}

- uses: anthropics/claude-code-action@beta
  with:
    model: "claude-3-7-sonnet@20250219"
    use_vertex: "true"
    # ... other inputs

  permissions:
    id-token: write # Required for OIDC
```

## Security

### Access Control

* **Repository Access**: The action can only be triggered by users with write access to the repository
* **No Bot Triggers**: GitHub Apps and bots cannot trigger this action
* **Token Permissions**: The GitHub app receives only a short-lived token scoped specifically to the repository it's operating in
* **No Cross-Repository Access**: Each action invocation is limited to the repository where it was triggered
* **Limited Scope**: The token cannot access other repositories or perform actions beyond the configured permissions

### GitHub App Permissions

The [Claude Code GitHub app](https://github.com/apps/claude) requires these permissions:

* **Pull Requests**: Read and write to create PRs and push changes
* **Issues**: Read and write to respond to issues
* **Contents**: Read and write to modify repository files

### Commit Signing

All commits made by Claude through this action are automatically signed with commit signatures. This ensures the authenticity and integrity of commits, providing a verifiable trail of changes made by the action.

### ⚠️ Authentication Protection

**CRITICAL: Never hardcode your Anthropic API key or OAuth token in workflow files!**

Your authentication credentials must always be stored in GitHub secrets to prevent unauthorized access:

```
# CORRECT ✅
anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
# OR
claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}

# NEVER DO THIS ❌
anthropic_api_key: "sk-ant-api03-..." # Exposed and vulnerable!
claude_code_oauth_token: "oauth_token_..." # Exposed and vulnerable!
```

### Setting Up GitHub Secrets

1. Go to your repository's Settings
2. Click on "Secrets and variables" → "Actions"
3. Click "New repository secret"
4. For authentication, choose one:
   * API Key: Name: `ANTHROPIC_API_KEY`, Value: Your Anthropic API key (starting with `sk-ant-`)
   * OAuth Token: Name: `CLAUDE_CODE_OAUTH_TOKEN`, Value: Your Claude Code OAuth token (Pro and Max users can generate this by running `claude setup-token` locally)
5. Click "Add secret"

### Best Practices for Authentication

1. ✅ Always use `${{ secrets.ANTHROPIC_API_KEY }}` or `${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}` in workflows
2. ✅ Never commit API keys or tokens to version control
3. ✅ Regularly rotate your API keys and tokens
4. ✅ Use environment secrets for organization-wide access
5. ❌ Never share API keys or tokens in pull requests or issues
6. ❌ Avoid logging workflow variables that might contain keys

## Security Best Practices

**⚠️ IMPORTANT: Never commit API keys directly to your repository! Always use GitHub Actions secrets.**

To securely use your Anthropic API key:

1. Add your API key as a repository secret:

   * Go to your repository's Settings
   * Navigate to "Secrets and variables" → "Actions"
   * Click "New repository secret"
   * Name it `ANTHROPIC_API_KEY`
   * Paste your API key as the value
2. Reference the secret in your workflow:

   ```
   anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
   ```

**Never do this:**

```
# ❌ WRONG - Exposes your API key
anthropic_api_key: "sk-ant-..."
```

**Always do this:**

```
# ✅ CORRECT - Uses GitHub secrets
anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

This applies to all sensitive values including API keys, access tokens, and credentials.
We also recommend that you always use short-lived tokens when possible

## License

This project is licensed under the MIT License—see the LICENSE file for details.

## About

No description, website, or topics provided.

### Resources

[Readme](#readme-ov-file)

### License

[MIT license](#MIT-1-ov-file)

### Code of conduct

[Code of conduct](#coc-ov-file)

### Security policy

[Security policy](#security-ov-file)

### Uh oh!

There was an error while loading. Please reload this page.

[Activity](/anthropics/claude-code-action/activity)

[Custom properties](/anthropics/claude-code-action/custom-properties)

### Stars

[**1.9k**
stars](/anthropics/claude-code-action/stargazers)

### Watchers

[**17**
watching](/anthropics/claude-code-action/watchers)

### Forks

[**931**
forks](/anthropics/claude-code-action/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code-action&report=anthropics+%28user%29)

## [Releases 34](/anthropics/claude-code-action/releases)

[Claude Code Github Actions beta

Latest

May 19, 2025](/anthropics/claude-code-action/releases/tag/beta)

[+ 33 releases](/anthropics/claude-code-action/releases)

## [Packages 0](/orgs/anthropics/packages?repo_name=claude-code-action)

No packages published

### Uh oh!

There was an error while loading. Please reload this page.

## [Contributors 32](/anthropics/claude-code-action/graphs/contributors)

* [![@ashwin-ant](https://avatars.githubusercontent.com/u/178951676?s=64&v=4)](https://github.com/ashwin-ant)
* [![@ltawfik](https://avatars.githubusercontent.com/u/11431944?s=64&v=4)](https://github.com/ltawfik)
* [![@actions-user](https://avatars.githubusercontent.com/u/65916846?s=64&v=4)](https://github.com/actions-user)
* [![@claude](https://avatars.githubusercontent.com/u/81847?s=64&v=4)](https://github.com/claude)
* [![@claude[bot]](https://avatars.githubusercontent.com/in/1236702?s=64&v=4)](https://github.com/apps/claude)
* [![@tomoish](https://avatars.githubusercontent.com/u/103555868?s=64&v=4)](https://github.com/tomoish)
* [![@int128](https://avatars.githubusercontent.com/u/321266?s=64&v=4)](https://github.com/int128)
* [![@bgutschke](https://avatars.githubusercontent.com/u/890428?s=64&v=4)](https://github.com/bgutschke)
* [![@stefanoamorelli](https://avatars.githubusercontent.com/u/10986064?s=64&v=4)](https://github.com/stefanoamorelli)
* [![@np-anthropic](https://avatars.githubusercontent.com/u/199845480?s=64&v=4)](https://github.com/np-anthropic)
* [![@andrewmunsell](https://avatars.githubusercontent.com/u/357386?s=64&v=4)](https://github.com/andrewmunsell)
* [![@DavidWells](https://avatars.githubusercontent.com/u/532272?s=64&v=4)](https://github.com/DavidWells)
* [![@dioptre](https://avatars.githubusercontent.com/u/760216?s=64&v=4)](https://github.com/dioptre)
* [![@valorkin](https://avatars.githubusercontent.com/u/1107171?s=64&v=4)](https://github.com/valorkin)

[+ 18 contributors](/anthropics/claude-code-action/graphs/contributors)

## Languages

* [TypeScript
  91.6%](/anthropics/claude-code-action/search?l=typescript)
* [JavaScript
  8.0%](/anthropics/claude-code-action/search?l=javascript)
* [Shell
  0.4%](/anthropics/claude-code-action/search?l=shell)

---

## Claude Code Action Official

*Source: https://docs.anthropic.com/marketplace/actions/claude-code-action-official*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Claude Code Base Action

*Source: https://docs.anthropic.com/marketplace/actions/claude-code-base-action*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Claude Code Sdk Python

*Source: https://docs.anthropic.com/anthropics/claude-code-sdk-python*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Claude Pr Path Specific.Yml

*Source: https://docs.anthropic.com/anthropics/claude-code-action/blob/main/examples/claude-pr-path-specific.yml*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Claude Review From Author.Yml

*Source: https://docs.anthropic.com/anthropics/claude-code-action/blob/main/examples/claude-review-from-author.yml*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Claude.Yml

*Source: https://docs.anthropic.com/anthropics/claude-code-action/blob/main/examples/claude.yml*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Claude_Code_Sdk

*Source: https://docs.anthropic.com/anthropics/claude-code-sdk-python/tree/main/src/claude_code_sdk*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Cli Reference

*Source: https://docs.anthropic.com/en/docs/claude-code/cli-reference*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Reference

# CLI reference

Copy page

Complete reference for Claude Code command-line interface, including commands and flags.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [CLI commands](#cli-commands)
* [CLI flags](#cli-flags)
* [See also](#see-also)

---

## Commands

*Source: https://docs.anthropic.com/anthropics/claude-code-action/tree/main/.claude/commands*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Common Workflows

*Source: https://docs.anthropic.com/en/docs/claude-code/common-workflows*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Getting started

# Common workflows

Copy page

Learn about common workflows with Claude Code.

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

## [​](#next-steps) Next steps

[## Claude Code reference implementation

Clone our development container reference implementation.](https://github.com/anthropics/claude-code/tree/main/.devcontainer)

Was this page helpful?

YesNo

[Quickstart](/en/docs/claude-code/quickstart)[Claude Code SDK](/en/docs/claude-code/sdk)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Understand new codebases](#understand-new-codebases)
* [Get a quick codebase overview](#get-a-quick-codebase-overview)
* [Find relevant code](#find-relevant-code)
* [Fix bugs efficiently](#fix-bugs-efficiently)
* [Refactor code](#refactor-code)
* [Work with tests](#work-with-tests)
* [Create pull requests](#create-pull-requests)
* [Handle documentation](#handle-documentation)
* [Work with images](#work-with-images)
* [Reference files and directories](#reference-files-and-directories)
* [Use extended thinking](#use-extended-thinking)
* [Resume previous conversations](#resume-previous-conversations)
* [Run parallel Claude Code sessions with Git worktrees](#run-parallel-claude-code-sessions-with-git-worktrees)
* [Use Claude as a unix-style utility](#use-claude-as-a-unix-style-utility)
* [Add Claude to your verification process](#add-claude-to-your-verification-process)
* [Pipe in, pipe out](#pipe-in%2C-pipe-out)
* [Control output format](#control-output-format)
* [Create custom slash commands](#create-custom-slash-commands)
* [Create project-specific commands](#create-project-specific-commands)
* [Add command arguments with $ARGUMENTS](#add-command-arguments-with-%24arguments)
* [Create personal slash commands](#create-personal-slash-commands)
* [Next steps](#next-steps)

---

## Contributors

*Source: https://docs.anthropic.com/anthropics/claude-code-action/graphs/contributors*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Corporate Proxy

*Source: https://docs.anthropic.com/en/docs/claude-code/corporate-proxy*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Deployment

# Corporate proxy configuration

Copy page

Learn how to configure Claude Code to work with corporate proxy servers, including environment variable configuration, authentication, and SSL/TLS certificate handling.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Basic proxy configuration](#basic-proxy-configuration)
* [Environment variables](#environment-variables)
* [Authentication](#authentication)
* [Basic authentication](#basic-authentication)
* [SSL certificate issues](#ssl-certificate-issues)
* [Network access requirements](#network-access-requirements)
* [Additional resources](#additional-resources)

---

## Costs

*Source: https://docs.anthropic.com/en/docs/claude-code/costs*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Administration

# Manage costs effectively

Copy page

Learn how to track and optimize token usage and costs when using Claude Code.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Track your costs](#track-your-costs)
* [Managing costs for teams](#managing-costs-for-teams)
* [Reduce token usage](#reduce-token-usage)
* [Background token usage](#background-token-usage)

---

## Custom Properties

*Source: https://docs.anthropic.com/anthropics/claude-code-action/custom-properties*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Data Usage

*Source: https://docs.anthropic.com/en/docs/claude-code/data-usage*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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
* [Analytics](/en/docs/claude-code/analytics)

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

Resources

# Data usage

Copy page

Learn about Anthropic’s data usage policies for Claude

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
| **Statsig (Metrics)** | Default on. `DISABLE_TELEMETRY=1` to disable. | Default off. `CLAUDE_CODE_USE_VERTEX` must be 1. | Default off. `CLAUDE_CODE_USE_BEDROCK` must be 1. |
| **Sentry (Errors)** | Default on. `DISABLE_ERROR_REPORTING=1` to disable. | Default off. `CLAUDE_CODE_USE_VERTEX` must be 1. | Default off. `CLAUDE_CODE_USE_BEDROCK` must be 1. |
| **Anthropic API (`/bug` reports)** | Default on. `DISABLE_BUG_COMMAND=1` to disable. | Default off. `CLAUDE_CODE_USE_VERTEX` must be 1. | Default off. `CLAUDE_CODE_USE_BEDROCK` must be 1. |

All environment variables can be checked into `settings.json` ([read more](/en/docs/claude-code/settings)).

Was this page helpful?

YesNo

[Hooks reference](/en/docs/claude-code/hooks)[Legal and compliance](/en/docs/claude-code/legal-and-compliance)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Data policies](#data-policies)
* [Data training policy](#data-training-policy)
* [Development Partner Program](#development-partner-program)
* [Feedback transcripts](#feedback-transcripts)
* [Data retention](#data-retention)
* [Privacy safeguards](#privacy-safeguards)
* [Data flow and dependencies](#data-flow-and-dependencies)
* [Telemetry services](#telemetry-services)
* [Default behaviors by API provider](#default-behaviors-by-api-provider)

---

## Demo.Gif

*Source: https://docs.anthropic.com/anthropics/claude-code/blob/main/demo.gif*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Dependents

*Source: https://docs.anthropic.com/anthropics/claude-code/network/dependents*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Devcontainer

*Source: https://docs.anthropic.com/en/docs/claude-code/devcontainer*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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
* [Analytics](/en/docs/claude-code/analytics)

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

Deployment

# Development containers

Copy page

Learn about the Claude Code development container for teams that need consistent, secure environments.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Key features](#key-features)
* [Getting started in 4 steps](#getting-started-in-4-steps)
* [Configuration breakdown](#configuration-breakdown)
* [Security features](#security-features)
* [Customization options](#customization-options)
* [Example use cases](#example-use-cases)
* [Secure client work](#secure-client-work)
* [Team onboarding](#team-onboarding)
* [Consistent CI/CD environments](#consistent-ci%2Fcd-environments)
* [Related resources](#related-resources)

---

## Devcontainer.Json

*Source: https://github.com/anthropics/claude-code/blob/main/.devcontainer/devcontainer.json*

[anthropics](/anthropics) 
/
**[claude-code](/anthropics/claude-code)**
Public

* [Notifications](/login?return_to=%2Fanthropics%2Fclaude-code) You must be signed in to change notification settings
* [Fork
  1.3k](/login?return_to=%2Fanthropics%2Fclaude-code)
* [Star
   23.7k](/login?return_to=%2Fanthropics%2Fclaude-code)

* [Code](/anthropics/claude-code)
* [Issues
  1.9k](/anthropics/claude-code/issues)
* [Pull requests
  13](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security


  ### Uh oh!

  There was an error while loading. Please reload this page.](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

Additional navigation options


* [Code](/anthropics/claude-code)
* [Issues](/anthropics/claude-code/issues)
* [Pull requests](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

---

## Discussions

*Source: https://docs.anthropic.com/anthropics/claude-code-action/discussions*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Examples

*Source: https://docs.anthropic.com/anthropics/claude-code-action/tree/main/examples*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Forks

*Source: https://docs.anthropic.com/anthropics/claude-code-action/forks*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Getting Started

*Source: https://docs.anthropic.com/en/docs/claude-code/getting-started*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Administration

# Set up Claude Code

Copy page

Install, authenticate, and start using Claude Code on your development machine.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [System requirements](#system-requirements)
* [Standard installation](#standard-installation)
* [Windows setup](#windows-setup)
* [Alternative installation methods](#alternative-installation-methods)
* [Global npm installation](#global-npm-installation)
* [Local installation](#local-installation)
* [Native binary installation (Alpha)](#native-binary-installation-alpha)
* [Running on AWS or GCP](#running-on-aws-or-gcp)
* [Update Claude Code](#update-claude-code)
* [Auto updates](#auto-updates)
* [Update manually](#update-manually)

---

## Github Actions

*Source: https://docs.anthropic.com/_sites/docs.anthropic.com/en/docs/claude-code/github-actions*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Google Vertex Ai

*Source: https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Deployment

# Claude Code on Google Vertex AI

Copy page

Learn about configuring Claude Code through Google Vertex AI, including setup, IAM configuration, and troubleshooting.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [1. Enable Vertex AI API](#1-enable-vertex-ai-api)
* [2. Request model access](#2-request-model-access)
* [3. Configure GCP credentials](#3-configure-gcp-credentials)
* [4. Configure Claude Code](#4-configure-claude-code)
* [5. Model configuration](#5-model-configuration)
* [IAM configuration](#iam-configuration)
* [Troubleshooting](#troubleshooting)
* [Additional resources](#additional-resources)

---

## Hooks

*Source: https://docs.anthropic.com/anthropics/claude-code/tree/main/examples/hooks*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Hooks Guide

*Source: https://docs.anthropic.com/en/docs/claude-code/hooks-guide*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Build with Claude Code

# Get started with Claude Code hooks

Copy page

Learn how to customize and extend Claude Code’s behavior by registering shell commands

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Hook Events Overview](#hook-events-overview)
* [Quickstart](#quickstart)
* [Prerequisites](#prerequisites)
* [Step 1: Open hooks configuration](#step-1%3A-open-hooks-configuration)
* [Step 2: Add a matcher](#step-2%3A-add-a-matcher)
* [Step 3: Add the hook](#step-3%3A-add-the-hook)
* [Step 4: Save your configuration](#step-4%3A-save-your-configuration)
* [Step 5: Verify your hook](#step-5%3A-verify-your-hook)
* [Step 6: Test your hook](#step-6%3A-test-your-hook)
* [More Examples](#more-examples)
* [Code Formatting Hook](#code-formatting-hook)
* [Custom Notification Hook](#custom-notification-hook)
* [File Protection Hook](#file-protection-hook)
* [Learn more](#learn-more)

---

## Iam

*Source: https://docs.anthropic.com/en/docs/claude-code/iam*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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
* [Analytics](/en/docs/claude-code/analytics)

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

Administration

# Identity and Access Management

Copy page

Learn how to configure user authentication, authorization, and access controls for Claude Code in your organization.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Authentication methods](#authentication-methods)
* [Anthropic API authentication](#anthropic-api-authentication)
* [Cloud provider authentication](#cloud-provider-authentication)
* [Access control and permissions](#access-control-and-permissions)
* [Permission system](#permission-system)
* [Configuring permissions](#configuring-permissions)
* [Permission modes](#permission-modes)
* [Working directories](#working-directories)
* [Tool-specific permission rules](#tool-specific-permission-rules)
* [Enterprise managed policy settings](#enterprise-managed-policy-settings)
* [Settings precedence](#settings-precedence)
* [Additional permission control with hooks](#additional-permission-control-with-hooks)
* [Credential management](#credential-management)

---

## Ide Integrations

*Source: https://docs.anthropic.com/en/docs/claude-code/ide-integrations*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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
* [Analytics](/en/docs/claude-code/analytics)

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

Configuration

# Add Claude Code to your IDE

Copy page

Learn how to add Claude Code to your favorite IDE

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [From your IDE](#from-your-ide)
* [From external terminals](#from-external-terminals)
* [Configuration](#configuration)
* [Troubleshooting](#troubleshooting)
* [VS Code extension not installing](#vs-code-extension-not-installing)
* [JetBrains plugin not working](#jetbrains-plugin-not-working)

---

## Init Firewall.Sh

*Source: https://github.com/anthropics/claude-code/blob/main/.devcontainer/init-firewall.sh*

[anthropics](/anthropics) 
/
**[claude-code](/anthropics/claude-code)**
Public

* [Notifications](/login?return_to=%2Fanthropics%2Fclaude-code) You must be signed in to change notification settings
* [Fork
  1.3k](/login?return_to=%2Fanthropics%2Fclaude-code)
* [Star
   23.7k](/login?return_to=%2Fanthropics%2Fclaude-code)

* [Code](/anthropics/claude-code)
* [Issues
  1.9k](/anthropics/claude-code/issues)
* [Pull requests
  13](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security


  ### Uh oh!

  There was an error while loading. Please reload this page.](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

Additional navigation options


* [Code](/anthropics/claude-code)
* [Issues](/anthropics/claude-code/issues)
* [Pull requests](/anthropics/claude-code/pulls)
* [Actions](/anthropics/claude-code/actions)
* [Security](/anthropics/claude-code/security)
* [Insights](/anthropics/claude-code/pulse)

---

## Interactive Mode

*Source: https://docs.anthropic.com/en/docs/claude-code/interactive-mode*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Reference

# Interactive mode

Copy page

Complete reference for keyboard shortcuts, input modes, and interactive features in Claude Code sessions.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Keyboard shortcuts](#keyboard-shortcuts)
* [General controls](#general-controls)
* [Multiline input](#multiline-input)
* [Quick commands](#quick-commands)
* [Vim mode](#vim-mode)
* [Mode switching](#mode-switching)
* [Navigation (NORMAL mode)](#navigation-normal-mode)
* [Editing (NORMAL mode)](#editing-normal-mode)
* [Command history](#command-history)
* [See also](#see-also)

---

## Issues

*Source: https://docs.anthropic.com/anthropics/claude-code-base-action/issues*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Labels

*Source: https://docs.anthropic.com/anthropics/claude-code/labels*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Legal And Compliance

*Source: https://docs.anthropic.com/en/docs/claude-code/legal-and-compliance*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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
* [Analytics](/en/docs/claude-code/analytics)

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

Resources

# Legal and compliance

Copy page

Legal agreements, compliance certifications, and security information for Claude Code.

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

---

© Anthropic PBC. All rights reserved. Use is subject to Anthropic’s [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms).

Was this page helpful?

YesNo

[Data usage](/en/docs/claude-code/data-usage)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Legal agreements](#legal-agreements)
* [License](#license)
* [Commercial agreements](#commercial-agreements)
* [Compliance](#compliance)
* [Healthcare compliance (BAA)](#healthcare-compliance-baa)
* [Security and trust](#security-and-trust)
* [Trust and safety](#trust-and-safety)
* [Security vulnerability reporting](#security-vulnerability-reporting)

---

## Llm Gateway

*Source: https://docs.anthropic.com/_sites/docs.anthropic.com/en/docs/claude-code/llm-gateway*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Mcp

*Source: https://docs.anthropic.com/en/docs/claude-code/mcp*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Build with Claude Code

# Model Context Protocol (MCP)

Copy page

Learn how to set up MCP with Claude Code.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Configure MCP servers](#configure-mcp-servers)
* [Understanding MCP server scopes](#understanding-mcp-server-scopes)
* [Scope hierarchy and precedence](#scope-hierarchy-and-precedence)
* [Local scope](#local-scope)
* [Project scope](#project-scope)
* [User scope](#user-scope)
* [Choosing the right scope](#choosing-the-right-scope)
* [Environment variable expansion in .mcp.json](#environment-variable-expansion-in-mcp-json)
* [Authenticate with remote MCP servers](#authenticate-with-remote-mcp-servers)
* [Connect to a Postgres MCP server](#connect-to-a-postgres-mcp-server)
* [Add MCP servers from JSON configuration](#add-mcp-servers-from-json-configuration)
* [Import MCP servers from Claude Desktop](#import-mcp-servers-from-claude-desktop)
* [Use Claude Code as an MCP server](#use-claude-code-as-an-mcp-server)
* [Use MCP resources](#use-mcp-resources)
* [Reference MCP resources](#reference-mcp-resources)
* [Use MCP prompts as slash commands](#use-mcp-prompts-as-slash-commands)
* [Execute MCP prompts](#execute-mcp-prompts)

---

## Memory

*Source: https://docs.anthropic.com/en/docs/claude-code/memory*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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
* [Analytics](/en/docs/claude-code/analytics)

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

Configuration

# Manage Claude's memory

Copy page

Learn how to manage Claude Code’s memory across sessions with different memory locations and best practices.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Determine memory type](#determine-memory-type)
* [CLAUDE.md imports](#claude-md-imports)
* [How Claude looks up memories](#how-claude-looks-up-memories)
* [Quickly add memories with the # shortcut](#quickly-add-memories-with-the-%23-shortcut)
* [Directly edit memories with /memory](#directly-edit-memories-with-%2Fmemory)
* [Set up project memory](#set-up-project-memory)
* [Memory best practices](#memory-best-practices)

---

## Milestones

*Source: https://docs.anthropic.com/anthropics/claude-code/milestones*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Monitoring Usage

*Source: https://docs.anthropic.com/_sites/docs.anthropic.com/en/docs/claude-code/monitoring-usage*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Overview

*Source: https://docs.anthropic.com/anthropics/claude-code/commits/main/*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Package.Json

*Source: https://docs.anthropic.com/anthropics/claude-code-action/blob/main/package.json*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Projects

*Source: https://docs.anthropic.com/anthropics/claude-code-base-action/projects*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Pulls

*Source: https://docs.anthropic.com/anthropics/claude-code-base-action/pulls*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Pulse

*Source: https://docs.anthropic.com/anthropics/claude-code-base-action/pulse*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Pyproject.Toml

*Source: https://docs.anthropic.com/anthropics/claude-code-sdk-python/blob/main/pyproject.toml*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Quick_Start.Py

*Source: https://docs.anthropic.com/anthropics/claude-code-sdk-python/blob/main/examples/quick_start.py*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Quickstart

*Source: https://docs.anthropic.com/en/docs/claude-code/quickstart*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Getting started

# Quickstart

Copy page

Welcome to Claude Code!

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Before you begin](#before-you-begin)
* [Step 1: Install Claude Code](#step-1%3A-install-claude-code)
* [Step 2: Start your first session](#step-2%3A-start-your-first-session)
* [Step 3: Ask your first question](#step-3%3A-ask-your-first-question)
* [Step 4: Make your first code change](#step-4%3A-make-your-first-code-change)
* [Step 5: Use Git with Claude Code](#step-5%3A-use-git-with-claude-code)
* [Step 6: Fix a bug or add a feature](#step-6%3A-fix-a-bug-or-add-a-feature)
* [Step 7: Test out other common workflows](#step-7%3A-test-out-other-common-workflows)
* [Essential commands](#essential-commands)
* [Pro tips for beginners](#pro-tips-for-beginners)
* [What’s next?](#what%E2%80%99s-next%3F)
* [Getting help](#getting-help)

---

## Releases

*Source: https://docs.anthropic.com/anthropics/claude-code-action/releases*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Scripts

*Source: https://docs.anthropic.com/anthropics/claude-code-action/tree/main/scripts*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Sdk

*Source: https://docs.anthropic.com/en/docs/claude-code/sdk*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Build with Claude Code

# Claude Code SDK

Copy page

Learn about programmatically integrating Claude Code into your applications with the Claude Code SDK.

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
| `--allowedTools` | Space-separated list of allowed tools, or    string of comma-separated list of allowed tools | `claude --allowedTools mcp__slack mcp__filesystem`  `claude --allowedTools "Bash(npm install),mcp__filesystem"` |
| `--disallowedTools` | Space-separated list of denied tools, or    string of comma-separated list of denied tools | `claude --disallowedTools mcp__splunk mcp__github`  `claude --disallowedTools "Bash(git commit),mcp__github"` |
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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Authentication](#authentication)
* [Anthropic API key](#anthropic-api-key)
* [Third-Party API credentials](#third-party-api-credentials)
* [Basic SDK usage](#basic-sdk-usage)
* [Command line](#command-line)
* [TypeScript](#typescript)
* [Python](#python)
* [Advanced usage](#advanced-usage)
* [Multi-turn conversations](#multi-turn-conversations)
* [Custom system prompts](#custom-system-prompts)
* [MCP Configuration](#mcp-configuration)
* [Custom permission prompt tool](#custom-permission-prompt-tool)
* [Available CLI options](#available-cli-options)
* [Output formats](#output-formats)
* [Text output (default)](#text-output-default)
* [JSON output](#json-output)
* [Streaming JSON output](#streaming-json-output)
* [Message schema](#message-schema)
* [Input formats](#input-formats)
* [Text input (default)](#text-input-default)
* [Streaming JSON input](#streaming-json-input)
* [Examples](#examples)
* [Simple script integration](#simple-script-integration)
* [Processing files with Claude](#processing-files-with-claude)
* [Session management](#session-management)
* [Best practices](#best-practices)
* [Real-world applications](#real-world-applications)
* [Related resources](#related-resources)

---

## Search

*Source: https://docs.anthropic.com/anthropics/claude-code-base-action/search*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Security

*Source: https://docs.anthropic.com/anthropics/claude-code-base-action/security*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Settings

*Source: https://docs.anthropic.com/_sites/docs.anthropic.com/en/docs/claude-code/settings*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Setup

*Source: https://docs.anthropic.com/en/docs/claude-code/setup*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Administration

# Set up Claude Code

Copy page

Install, authenticate, and start using Claude Code on your development machine.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [System requirements](#system-requirements)
* [Standard installation](#standard-installation)
* [Windows setup](#windows-setup)
* [Alternative installation methods](#alternative-installation-methods)
* [Global npm installation](#global-npm-installation)
* [Local installation](#local-installation)
* [Native binary installation (Alpha)](#native-binary-installation-alpha)
* [Running on AWS or GCP](#running-on-aws-or-gcp)
* [Update Claude Code](#update-claude-code)
* [Auto updates](#auto-updates)
* [Update manually](#update-manually)

---

## Slash Commands

*Source: https://docs.anthropic.com/en/docs/claude-code/slash-commands*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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
* [Analytics](/en/docs/claude-code/analytics)

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

Reference

# Slash commands

Copy page

Control Claude’s behavior during an interactive session with slash commands.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Built-in slash commands](#built-in-slash-commands)
* [Custom slash commands](#custom-slash-commands)
* [Syntax](#syntax)
* [Parameters](#parameters)
* [Command types](#command-types)
* [Project commands](#project-commands)
* [Personal commands](#personal-commands)
* [Features](#features)
* [Namespacing](#namespacing)
* [Arguments](#arguments)
* [Bash command execution](#bash-command-execution)
* [File references](#file-references)
* [Thinking mode](#thinking-mode)
* [File format](#file-format)
* [MCP slash commands](#mcp-slash-commands)
* [Command format](#command-format)
* [Features](#features-2)
* [Dynamic discovery](#dynamic-discovery)
* [Arguments](#arguments-2)
* [Naming conventions](#naming-conventions)
* [Managing MCP connections](#managing-mcp-connections)
* [See also](#see-also)

---

## Src

*Source: https://docs.anthropic.com/anthropics/claude-code-action/tree/main/src*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Stargazers

*Source: https://docs.anthropic.com/anthropics/claude-code-action/stargazers*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Tags

*Source: https://docs.anthropic.com/anthropics/claude-code/tags*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Terminal Config

*Source: https://docs.anthropic.com/en/docs/claude-code/terminal-config*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Configuration

# Optimize your terminal setup

Copy page

Claude Code works best when your terminal is properly configured. Follow these guidelines to optimize your experience.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Themes and appearance](#themes-and-appearance)
* [Line breaks](#line-breaks)
* [Set up Shift+Enter (VS Code or iTerm2):](#set-up-shift%2Benter-vs-code-or-iterm2-%3A)
* [Set up Option+Enter (VS Code, iTerm2 or macOS Terminal.app):](#set-up-option%2Benter-vs-code%2C-iterm2-or-macos-terminal-app-%3A)
* [Notification setup](#notification-setup)
* [Terminal bell notifications](#terminal-bell-notifications)
* [iTerm 2 system notifications](#iterm-2-system-notifications)
* [Custom notification hooks](#custom-notification-hooks)
* [Handling large inputs](#handling-large-inputs)
* [Vim Mode](#vim-mode)

---

## Test

*Source: https://docs.anthropic.com/anthropics/claude-code-action/tree/main/test*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Test Local.Sh

*Source: https://docs.anthropic.com/anthropics/claude-code-base-action/blob/main/test-local.sh*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Test Mcp Local.Sh

*Source: https://docs.anthropic.com/anthropics/claude-code-base-action/blob/main/test-mcp-local.sh*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Tests

*Source: https://docs.anthropic.com/anthropics/claude-code-sdk-python/tree/main/tests*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Third Party Integrations

*Source: https://docs.anthropic.com/en/docs/claude-code/third-party-integrations*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

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

Deployment

# Enterprise deployment overview

Copy page

Learn how Claude Code can integrate with various third-party services and infrastructure to meet enterprise deployment requirements.

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

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

On this page

* [Provider comparison](#provider-comparison)
* [Cloud providers](#cloud-providers)
* [Corporate infrastructure](#corporate-infrastructure)
* [Configuration overview](#configuration-overview)
* [Using Bedrock with corporate proxy](#using-bedrock-with-corporate-proxy)
* [Using Bedrock with LLM Gateway](#using-bedrock-with-llm-gateway)
* [Using Vertex AI with corporate proxy](#using-vertex-ai-with-corporate-proxy)
* [Using Vertex AI with LLM Gateway](#using-vertex-ai-with-llm-gateway)
* [Authentication configuration](#authentication-configuration)
* [Choosing the right deployment configuration](#choosing-the-right-deployment-configuration)
* [Direct provider access](#direct-provider-access)
* [Corporate proxy](#corporate-proxy)
* [LLM Gateway](#llm-gateway)
* [Debugging](#debugging)
* [Best practices for organizations](#best-practices-for-organizations)
* [Next steps](#next-steps)

---

## Troubleshooting

*Source: https://docs.anthropic.com/_sites/docs.anthropic.com/en/docs/claude-code/troubleshooting*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Tsconfig.Json

*Source: https://docs.anthropic.com/anthropics/claude-code-action/blob/main/tsconfig.json*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Tutorials

*Source: https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Types.Py

*Source: https://docs.anthropic.com/anthropics/claude-code-sdk-python/blob/main/src/claude_code_sdk/types.py*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## Watchers

*Source: https://docs.anthropic.com/anthropics/claude-code-action/watchers*

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...

* [Research](https://www.anthropic.com/research)
* [Login](https://console.anthropic.com/login)
* [Support](https://support.anthropic.com/)
* [Sign up](https://console.anthropic.com/login)
* [Sign up](https://console.anthropic.com/login)

Search...

Navigation

[Welcome](/en/home)[Developer Platform](/en/docs/intro)[Claude Code](/en/docs/claude-code/overview)[Model Context Protocol (MCP)](/en/docs/mcp)[API Reference](/en/api/messages)[Resources](/en/resources/overview)[Release Notes](/en/release-notes/overview)

Build with

Learn how to get started with the Anthropic API, the Console, and Claude Code.

Ask Claude about docs…

## Developer Platform

[## Get started

Make your first API call in minutes.](/en/docs/get-started)[## Features overview

Explore the advanced features and capabilities now available in Claude.](/en/docs/build-with-claude/overview)[## API reference

Integrate and scale using our API and SDKs.](/en/api/getting-started)[## Anthropic Console

Craft and test powerful prompts directly in your browser.](https://console.anthropic.com)[## Release notes

Learn about changes and new features in Claude and the API.](/en/release-notes/overview)[## Upgrade to Claude 4

Upgrade to the latest model to access new tools and features available in Claude 4.](/en/docs/about-claude/models/migrating-to-claude-4)

## Claude Code

[## Claude Code quickstart

Get started with Claude Code.](/en/docs/claude-code/quickstart)[## Claude Code reference

Consult the Claude Code reference documentation for details on feature implementation and configuration.](/en/docs/claude-code/overview)[## Claude Code release notes

Learn about changes and new features in Claude Code.](/en/release-notes/claude-code)

## Learning resources

[## Anthropic Courses

Explore Anthropic’s educational courses and projects.](https://anthropic.skilljar.com/)[## Anthropic Cookbook

See replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[## Anthropic Quickstarts

Deployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)