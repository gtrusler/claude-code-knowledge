# Claude Code Memory Management
*Source: https://docs.anthropic.com/en/docs/claude-code/memory*

Learn how to manage Claude Code's memory across sessions with different memory locations and best practices.

Claude Code can remember your preferences across sessions, like style guidelines and common commands in your workflow.

## Determine Memory Type

Claude Code offers three memory locations, each serving a different purpose:

| Memory Type | Location | Purpose | Use Case Examples |
|-------------|----------|---------|-------------------|
| Project memory | `./CLAUDE.md` | Team-shared conventions and knowledge | Project architecture, coding standards, common workflows |
| Project memory (local) | `./CLAUDE.local.md` | Personal project-specific preferences | Your sandbox URLs, preferred test data |
| User memory | `~/.claude/CLAUDE.md` | Global personal preferences | Code styling preferences, personal tooling shortcuts |

All memory files are automatically loaded into Claude Code's context when launched.

## How Claude Looks Up Memories

Claude Code reads memories recursively: starting in the cwd, Claude Code recurses up to `/` and reads any `CLAUDE.md` or `CLAUDE.local.md` files it finds. This is especially convenient when working in large repositories where you run Claude Code in `foo/bar/`, and have memories in both `foo/CLAUDE.md` and `foo/bar/CLAUDE.md`.

## Quickly Add Memories with the `#` Shortcut

The fastest way to add a memory is to start your input with the `#` character:

```
# Always use 4 spaces for indentation in Python files
```

You'll be prompted to select which memory file to store this in.

## Directly Edit Memories with `/memory`

Use the `/memory` slash command during a session to open any memory file in your system editor for more extensive additions or organization.

## Memory Best Practices

- **Be specific**: "Use 2-space indentation" is better than "Format code properly".
- **Use structure to organize**: Format each individual memory as a bullet point and group related memories under descriptive markdown headings.
- **Review periodically**: Update memories as your project evolves to ensure Claude is always using the most up to date information and context.

## Example Memory File Structure

Here's an example of a well-organized `CLAUDE.md` file:

```markdown
# Project Guidelines

## Code Style
- Use 2-space indentation for all JavaScript files
- Prefer const over let when variables won't be reassigned
- Always use semicolons in JavaScript
- Maximum line length is 100 characters

## Architecture
- Follow MVC pattern for all new features
- Place all database queries in the models/ directory
- Keep controllers thin, business logic belongs in services/

## Testing
- Write unit tests for all new functions
- Integration tests go in tests/integration/
- Aim for 80% code coverage minimum

## Git Workflow
- Create feature branches from main
- Prefix branch names with: feat/, fix/, docs/, refactor/
- Squash commits before merging
- Always run tests before pushing
```

## Memory Inheritance

When you have multiple memory files in your directory hierarchy, Claude Code combines them intelligently:

1. **User memory** (`~/.claude/CLAUDE.md`) - Loaded first, lowest priority
2. **Parent directory memories** - Loaded in order from root to current directory
3. **Current directory memory** - Loaded last, highest priority

This allows you to have general preferences at the user level, project-wide conventions at the project root, and specific overrides in subdirectories.

## Local vs Shared Memory

Use `.CLAUDE.local.md` files for:
- Personal API keys or tokens (never commit these!)
- Local development URLs
- Personal debugging preferences
- Machine-specific paths

Use `CLAUDE.md` files for:
- Team coding standards
- Project architecture decisions
- Shared workflows
- Documentation patterns

## Memory Limits and Performance

- Claude Code loads all memory files at startup
- Keep individual memory files under 10KB for best performance
- Total memory across all files should stay under 50KB
- Use clear, concise language to maximize information density

## Troubleshooting Memory Issues

If memories don't seem to be loading:
1. Check file names are exactly `CLAUDE.md` or `CLAUDE.local.md`
2. Verify files are in the correct directories
3. Ensure files are valid Markdown
4. Run `claude` with `--verbose` flag to see which memory files are loaded
5. Use `/memory` command to verify current memory state

## Advanced Memory Patterns

### Conditional Instructions
```markdown
## Platform-Specific
- On macOS: Use `open` command to open files
- On Linux: Use `xdg-open` command to open files
- On Windows: Use `start` command to open files
```

### Command Shortcuts
```markdown
## Common Commands
- To deploy: Run `npm run build && npm run deploy`
- To run tests with coverage: `npm test -- --coverage`
- To update dependencies: `npm update && npm audit fix`
```

### Context-Aware Guidelines
```markdown
## File-Specific Rules
- In components/: Use functional components with hooks
- In utils/: Pure functions only, no side effects
- In api/: Always handle errors with try-catch
```