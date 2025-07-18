# Claude Code Interactive Mode
*Source: https://docs.anthropic.com/en/docs/claude-code/interactive-mode*

Complete reference for keyboard shortcuts, input modes, and interactive features in Claude Code sessions.

## Keyboard Shortcuts

### General Controls

| Shortcut | Description | Context |
|----------|-------------|---------|
| Ctrl+C | Cancel current input or generation | Standard interrupt |
| Ctrl+D | Exit Claude Code session | EOF signal |
| Ctrl+L | Clear terminal screen | Keeps conversation history |
| Up/Down arrows | Navigate command history | Recall previous inputs |

### Multiline Input

| Method | Shortcut | Context |
|--------|----------|---------|
| Quick escape | `\` + Enter | Works in all terminals |
| macOS default | Option+Enter | Default on macOS |
| Terminal setup | Shift+Enter | After `/terminal-setup` |
| Paste mode | Paste directly | For code blocks, logs |

### Quick Commands

| Shortcut | Description | Notes |
|----------|-------------|-------|
| `#` at start | Memory shortcut - add to CLAUDE.md | Prompts for file selection |
| `/` at start | Slash command | See slash commands documentation |

## Vim Mode

Enable vim-style editing with `/vim` command or configure permanently via `/config`.

### Mode Switching

| Command | Action | From mode |
|---------|--------|-----------|
| Esc | Enter NORMAL mode | INSERT |
| i | Insert before cursor | NORMAL |
| I | Insert at beginning of line | NORMAL |
| a | Insert after cursor | NORMAL |
| A | Insert at end of line | NORMAL |
| o | Open line below | NORMAL |
| O | Open line above | NORMAL |

### Navigation (NORMAL mode)

| Command | Action |
|---------|--------|
| h/j/k/l | Move left/down/up/right |
| w | Next word |
| e | End of word |
| b | Previous word |
| 0 | Beginning of line |
| $ | End of line |
| ^ | First non-blank character |
| gg | Beginning of input |
| G | End of input |

### Editing (NORMAL mode)

| Command | Action |
|---------|--------|
| x | Delete character |
| dd | Delete line |
| D | Delete to end of line |
| dw/de/db | Delete word/to end/back |
| cc | Change line |
| C | Change to end of line |
| cw/ce/cb | Change word/to end/back |
| . | Repeat last change |

Configure your preferred line break behavior in terminal settings. Run `/terminal-setup` to install Shift+Enter binding for iTerm2 and VSCode terminals.

## Command History

Claude Code maintains command history for the current session:

- History is stored per working directory
- Cleared with `/clear` command
- Use Up/Down arrows to navigate (see keyboard shortcuts above)
- Ctrl+R: Reverse search through history (if supported by terminal)
- Note: History expansion (`!`) is disabled by default

## See Also

- [Slash commands](/en/docs/claude-code/slash-commands) - Interactive session commands
- [CLI reference](/en/docs/claude-code/cli-reference) - Command-line flags and options
- [Settings](/en/docs/claude-code/settings) - Configuration options
- [Memory management](/en/docs/claude-code/memory) - Managing CLAUDE.md files