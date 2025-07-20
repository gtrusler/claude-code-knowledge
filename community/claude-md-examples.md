# CLAUDE.md Best Practices

*Examples from real-world projects*

## What is CLAUDE.md?

A file in your project root that gives Claude Code context about your project. Think of it as Claude's instruction manual for working with your codebase.

## Core Principles

### Keep It Focused
*Source: Multiple high-quality CLAUDE.md examples - 2025*

Your CLAUDE.md should be:
- **Concise**: 200-500 lines, not 2,000+
- **Specific**: Project conventions, not general programming advice
- **Actionable**: Commands and patterns, not philosophy

### Essential Sections

#### 1. Project Overview (2-3 sentences)
```markdown
# Project Name

Brief description of what this project does and its main purpose.
Tech stack: [List key technologies]
```

#### 2. Build & Test Commands
```markdown
## Commands

- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint`
- Dev server: `npm run dev`
```

#### 3. Code Style & Conventions
```markdown
## Code Style

- Use TypeScript with strict mode
- Prefer functional components with hooks
- File naming: kebab-case for files, PascalCase for components
- Always include tests alongside implementation
```

#### 4. Project Structure
```markdown
## Structure

```
src/
├── components/     # React components
├── hooks/         # Custom hooks
├── utils/         # Helper functions
└── types/         # TypeScript types
```
```

## Real-World Examples

### Multi-Platform Development
*Source: https://github.com/touchlab/DroidconKotlin/blob/main/CLAUDE.md*

For Kotlin Multiplatform projects:
```markdown
## Gradle Commands
- `./gradlew :shared:build` - Build shared module
- `./gradlew :android:assembleDebug` - Build Android app
- `./gradlew :shared:iosX64Test` - Run iOS tests

## Platform-Specific Code
Use expect/actual pattern:
- `expect` declarations in commonMain
- `actual` implementations in platform modules
```

### Security-Focused Development
*Source: https://github.com/alexei-led/aws-mcp-server/blob/main/CLAUDE.md*

For security-sensitive projects:
```markdown
## Security Considerations

- Never commit AWS credentials
- Use environment variables for sensitive data
- Validate all user inputs
- Follow principle of least privilege
- Log security events but never log sensitive data
```

### AI-Powered Applications
*Source: https://github.com/basicmachines-co/basic-memory/blob/main/CLAUDE.md*

For AI/LLM projects:
```markdown
## AI Integration

- Use Model Context Protocol (MCP) for LLM communication
- Knowledge graph structure: entities → observations → relations
- Always version prompt templates
- Include token usage tracking
```

## Anti-Patterns to Avoid

### ❌ The Essay
```markdown
# Bad Example
This project represents our vision for the future of web development...
[500 words of philosophy]
```

### ❌ The Kitchen Sink
```markdown
# Bad Example
Here's how to write good JavaScript:
- Use const instead of let...
[Generic programming advice]
```

### ❌ The Outdated
```markdown
# Bad Example
To run tests: npm test (Note: This might not work anymore)
The API might be at localhost:3000 or 8080
```

## Advanced Patterns

### Modular Architecture
*Source: https://github.com/hashintel/hash/blob/main/CLAUDE.md*

For monorepos:
```markdown
## Repository Structure

/apps - User-facing applications
/blocks - Reusable UI components
/libs - Shared libraries
/infra - Infrastructure code

## Before Starting
Read: /libs/repo-docs/rust.md for Rust conventions
Read: /libs/repo-docs/typescript.md for TS conventions
```

### Workflow Integration
*Source: https://github.com/badass-courses/course-builder/blob/master/CLAUDE.md*

For complex workflows:
```markdown
## Development Workflow

1. Feature Development:
   - Create feature branch
   - Use Turborepo for builds
   - Test with: pnpm test:watch

2. Video Processing:
   - Upload to Mux
   - Generate subtitles with Deepgram
   - Store metadata in Sanity

3. AI Features:
   - Use instructor-js for structured outputs
   - Implement rate limiting for API calls
```

### Testing Requirements
*Source: https://github.com/expectedparrot/edsl/blob/main/CLAUDE.md*

For test-driven projects:
```markdown
## Testing Standards

- 100% test coverage required for new code
- Use pytest with fixtures
- Mock external services
- Test file naming: test_[module_name].py
- Run before commit: make test-all
```

## Integration with Other Tools

### With Hooks
```markdown
## Hooks Integration

See .claude/settings.json for:
- Auto-formatting on save
- Pre-commit validation
- Build verification
```

### With MCP Servers
```markdown
## MCP Tools Available

- memory: Store project context
- github: Repository operations
- filesystem: Advanced file operations
```

### With Custom Commands
```markdown
## Custom Commands

- /project:setup - Initialize new feature
- /project:test - Run focused tests
- /project:deploy - Deployment checklist
```

## Tips for Maintenance

1. **Update Regularly**: When you change build process, update CLAUDE.md
2. **Version Control**: Track changes to understand evolution
3. **Team Review**: Have team members verify accuracy
4. **Test It**: Give CLAUDE.md to new team member - can they understand the project?

## Examples by Project Type

### Next.js Application
```markdown
# E-Commerce Platform

Next.js 14 app with TypeScript, Tailwind, and Prisma.

## Quick Start
npm install
npm run dev
Open http://localhost:3000

## Key Patterns
- Server components by default
- Use "use client" only when needed
- API routes in app/api/
- Database queries with Prisma
```

### Python Library
```markdown
# DataProcessor

Python library for ETL operations.

## Setup
poetry install
poetry run pytest

## Standards
- Type hints required
- Docstrings in Google format
- Black formatting (line length 88)
- 100% test coverage for public APIs
```

### Mobile App
```markdown
# FitnessTracker

React Native app with Expo.

## Commands
- expo start - Start dev server
- expo build:ios - Build iOS
- eas submit - Submit to stores

## Architecture
- Redux for state management
- React Navigation for routing
- Styled Components for styling
```