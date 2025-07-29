# Claude Code Examples

*Real-world patterns and solutions*

## Hooks Examples

### Auto-Format on Save
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "file=$(echo '$' | jq -r '.tool_input.file_path // .tool_input.files[0].path // empty'); [ -n \"$file\" ] && { case \"$file\" in *.py) black \"$file\" ;; *.js|*.ts|*.jsx|*.tsx) prettier --write \"$file\" ;; *.go) gofmt -w \"$file\" ;; esac; }"
          }
        ]
      }
    ]
  }
}
```

### Command Logger with Descriptions
```json
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

### Protect Production Files
```python
#!/usr/bin/env python3
# save as ~/scripts/protect-prod.py
import json
import sys

PROTECTED_PATHS = ['/etc/', '/usr/', '/System/', 'production/', '.env']

data = json.load(sys.stdin)
if data.get('tool_name') in ['Write', 'Edit', 'MultiEdit']:
    path = data.get('tool_input', {}).get('file_path', '')
    if any(protected in path for protected in PROTECTED_PATHS):
        print(f"Blocked: Attempting to modify protected path: {path}", file=sys.stderr)
        sys.exit(2)
```

### Smart Git Commits
```bash
#!/bin/bash
# Auto-commit after file changes
set -euo pipefail

# Parse input
input=$(cat)
tool_name=$(echo "$input" | jq -r '.tool_name')
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')

if [[ "$tool_name" =~ ^(Write|Edit|MultiEdit)$ ]] && [ -n "$file_path" ]; then
    # Check if file is in git repo
    if git ls-files --error-unmatch "$file_path" 2>/dev/null; then
        git add "$file_path"
        git commit -m "Auto-commit: Updated $(basename "$file_path")" || true
    fi
fi
```

## Task Patterns

### Safe Database Migrations
```bash
# Instead of running migrations directly
claude run "Migrate the database"

# Do this for safety
claude run "First, backup the database to ./backups/pre-migration-$(date +%s).sql"
claude run "Show me the migration that would run without executing it"
claude run "Now run the migration"
```

### Incremental Feature Development
```bash
# Break down into explicit steps
claude do "1. Create the database schema for users table"
claude do "2. Add the User model with validation"
claude do "3. Create CRUD endpoints for User"
claude do "4. Add tests for User endpoints"
claude do "5. Add authentication to User endpoints"
```

### Debugging Workflow
```bash
# When something breaks
claude do "Show me the last 20 lines of the error log"
claude do "Check if the service is running with 'ps aux | grep [service]'"
claude do "Show me the recent changes with 'git diff HEAD~1'"
```

## Project Setup Patterns

### New Project with Best Practices
```bash
claude do "Create a new Next.js project in ./my-app with TypeScript, Tailwind, and ESLint"
claude do "Set up the project structure: /components, /lib, /types, /hooks"
claude do "Create a .env.example with common variables"
claude do "Initialize git and create initial commit"
```

### Adding Claude Code Hooks to Existing Project
```bash
claude do "Create .claude/settings.json with hooks for auto-formatting Python and JS files"
claude do "Add a pre-commit hook that runs tests before allowing commits"
claude do "Create a command logger for audit trail"
```

## Integration Examples

### MCP + Hooks Combination
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__github__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"GitHub operation: $(date)\" >> ~/mcp-github-audit.log"
          }
        ]
      }
    ]
  }
}
```

### Notification Systems
```python
#!/usr/bin/env python3
# Custom notifier for important events
import json
import sys
import subprocess

data = json.load(sys.stdin)
message = data.get('message', '')

if 'needs your permission' in message.lower():
    # Critical - use system notification
    subprocess.run(['osascript', '-e', f'display notification "{message}" with title "Claude Code" sound name "Glass"'])
elif 'waiting for your input' in message.lower():
    # Just log it
    print(f"[{datetime.now()}] Claude is waiting", file=open('/tmp/claude-waiting.log', 'a'))
```

## Context Management Patterns

### Hierarchical Claude.md Files
*Source: Claude Code community presentation - Jan 2025*

Instead of one root `claude.md`, create detailed files in each subfolder:

```
project/
├── claude.md              # High-level overview
├── frontend/
│   └── claude.md          # Frontend-specific details
├── backend/
│   └── claude.md          # Backend-specific details
└── docs/
    ├── claude.md          # Documentation patterns
    ├── changelog.md       # Track why changes were made
    └── plan.md           # Current project goals
```

**Root claude.md example:**
```markdown
# Project Overview
Frontend: React + TypeScript (see ./frontend/claude.md)
Backend: Node.js + Express (see ./backend/claude.md)

## Cross-cutting Concerns
- Auth handled by backend, tokens stored in frontend
- Database migrations in ./backend/migrations/
- API documentation auto-generated from schemas
```

### Multiple Context Reviewer Pattern
*Source: Claude Code community presentation - Jan 2025*

Use separate Claude instances for different roles:

```bash
# Tab 1: Context Builder
"Prepare to discuss our authentication system architecture"
# Build deep context, double escape

# Tab 2: Planner (fresh instance) 
"My developer created this plan for auth improvements: [paste plan]
What are the risks and issues with this approach?"

# Tab 3: Executor (use saved context)
resume  # Gets the deep context from Tab 1
"Execute this refined plan: [final plan]"
```

This prevents Claude from being too positive about its own plans.

## GitHub Integration Hacks

### Custom GitHub Actions with Opus
*Source: Claude Code community presentation - Jan 2025*

When setting up GitHub integration, you can modify the generated YAML:

```yaml
# In .github/workflows/claude-code.yml
# Uncomment this line to use Opus instead of Sonnet:
model: claude-3-5-opus-20241022

# Add OAuth support for max plan usage
auth:
  type: oauth  # Uses your max plan instead of API key
```

### Enhanced GitHub Integration
*Source: Claude Code community presentation - Jan 2025*

You can customize the GitHub integration to include MCPs and additional tooling:

```yaml
# Add MCPs to your GitHub workflow
environment:
  CUSTOM_MCPS: |
    - mcp__github__search
    - mcp__linear__tasks
    
# Point to additional config files
config_files:
  - ./docs/api-guide.md
  - ./docs/database-patterns.md
  
# Custom bash tooling access
permissions:
  - gh cli
  - docker
  - npm scripts
```

**Multi-task automation example:**
```bash
# Create multiple PRs from a list
claude do "Generate PRs for these features: auth, payments, notifications. Tag @claude in each."
```

## UV Single-File Script Hooks
*Source: https://github.com/disler/claude-code-hooks-mastery - January 2025*

### Complete Hook Lifecycle Implementation
Using UV for isolated dependency management in hooks:

```python
#!/usr/bin/env python3
# /// script
# dependencies = ["requests", "pyttsx3"]
# ///

# UV single-file script with embedded dependencies
import json
import sys
import subprocess

# All 5 hook lifecycle events:
# 1. PreToolUse - Before tool execution (can block with exit 2)
# 2. PostToolUse - After successful completion  
# 3. Notification - Claude Code notifications
# 4. Stop - When Claude finishes responding (can block)
# 5. SubagentStop - When subagents complete

def main():
    event_data = json.load(sys.stdin)
    
    # Log everything for debugging
    with open("logs/all_hooks.jsonl", "a") as f:
        f.write(json.dumps(event_data) + "\n")
    
    # Example: Block dangerous commands
    if event_data.get("hook_event_name") == "PreToolUse":
        command = event_data.get("tool_input", {}).get("command", "")
        if "rm -rf" in command:
            print("BLOCKED: Dangerous command detected", file=sys.stderr)
            sys.exit(2)  # Blocks execution and shows error to Claude
```

### Hook Exit Code Behavior
*Source: https://github.com/disler/claude-code-hooks-mastery - January 2025*

| Exit Code | Behavior | Hook-Specific Effects |
|-----------|----------|----------------------|
| 0 | Success | stdout shown in transcript mode (Ctrl-R) |
| 2 | Blocking Error | PreToolUse: Blocks tool call<br>Stop: Forces continuation<br>Others: Shows error to Claude |
| Other | Non-blocking Error | Shows stderr to user, continues |

### Advanced Hook Control with JSON
*Source: https://github.com/disler/claude-code-hooks-mastery - January 2025*

```python
# PreToolUse - Bypass permission system
output = {
    "decision": "approve",  # or "block"
    "reason": "Security check passed"
}
print(json.dumps(output))
sys.exit(0)

# Stop hook - Prevent Claude from stopping
output = {
    "decision": "block",
    "reason": "Tests are still failing, please fix them first"
}
print(json.dumps(output))
sys.exit(0)
```

### Intelligent TTS Notifications
*Source: https://github.com/disler/claude-code-hooks-mastery - January 2025*

```python
#!/usr/bin/env python3
# /// script
# dependencies = ["elevenlabs", "openai", "pyttsx3"]
# ///

import os
import json
import sys
import random

def notify_with_tts(message):
    """Multi-provider TTS with fallback"""
    engineer_name = os.getenv("ENGINEER_NAME", "")
    
    # 30% chance to include name
    if engineer_name and random.random() < 0.3:
        message = f"{engineer_name}, {message}"
    
    # Try providers in order
    providers = [
        lambda m: elevenlabs_tts(m),
        lambda m: openai_tts(m),
        lambda m: pyttsx3_tts(m)
    ]
    
    for provider in providers:
        try:
            provider(message)
            break
        except Exception:
            continue
```

### Chat Transcript Extraction
*Source: https://github.com/disler/claude-code-hooks-mastery - January 2025*

Convert Claude's JSONL chat format to readable JSON:

```python
# In PostToolUse hook
if tool_name == "Read" and ".jsonl" in file_path:
    try:
        # Convert JSONL to pretty JSON
        lines = tool_response.get("content", "").strip().split("\n")
        messages = [json.loads(line) for line in lines if line]
        
        # Save readable format
        with open("logs/chat.json", "w") as f:
            json.dump(messages, f, indent=2)
            
        print("Chat transcript converted to logs/chat.json", file=sys.stderr)
    except Exception as e:
        print(f"Transcript conversion failed: {e}", file=sys.stderr)
```

## Advanced Patterns

### Context-Aware Auto-Completion
```bash
# Hook that provides context based on current file
#!/bin/bash
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')

if [[ "$file_path" == *.test.js ]]; then
    echo "Remember to follow Jest patterns and include describe/it blocks" >&2
    exit 2
fi
```

### Smart Task Routing
```python
#!/usr/bin/env python3
# Route tasks based on content
import json
import sys

data = json.load(sys.stdin)
if data.get('tool_name') == 'Task':
    description = data.get('tool_input', {}).get('description', '')
    
    if 'database' in description.lower():
        print("Note: Check ./docs/database-patterns.md for our conventions", file=sys.stderr)
        sys.exit(2)
    elif 'api' in description.lower():
        print("Note: Follow RESTful patterns in ./docs/api-guide.md", file=sys.stderr)
        sys.exit(2)
```

## Sub Agent Examples
*Source: Official docs - January 2025*

### Complete Code Reviewer Agent
```markdown
---
name: code-reviewer
description: Expert code review specialist. Use PROACTIVELY after any code changes to ensure quality, security, and maintainability.
tools: Read, Grep, Glob, Bash
---

You are a senior code reviewer with 15+ years of experience ensuring high standards of code quality and security.

## Immediate Actions
When invoked, immediately:
1. Run `git diff` to see recent changes
2. Run `git diff --cached` for staged changes
3. Focus review on modified files only

## Review Checklist

### Code Quality
- [ ] Code is simple and readable
- [ ] Functions have single responsibility
- [ ] Variable/function names are self-documenting
- [ ] No duplicated code (DRY principle)
- [ ] Complex logic has explanatory comments

### Security
- [ ] No hardcoded secrets or API keys
- [ ] Input validation on all user data
- [ ] SQL injection protection (parameterized queries)
- [ ] XSS prevention (proper escaping)
- [ ] CSRF tokens where needed
- [ ] Authentication/authorization checks

### Error Handling
- [ ] All exceptions caught appropriately
- [ ] Meaningful error messages (not exposing internals)
- [ ] Graceful degradation
- [ ] Proper logging for debugging

### Performance
- [ ] No N+1 query problems
- [ ] Appropriate use of caching
- [ ] Efficient algorithms (no unnecessary O(n²))
- [ ] Database queries are indexed

### Testing
- [ ] New code has tests
- [ ] Edge cases covered
- [ ] Tests are readable and maintainable

## Output Format

Organize feedback by priority:

### 🚨 Critical Issues (must fix)
- Security vulnerabilities
- Data loss risks
- Breaking changes

### ⚠️ Warnings (should fix)
- Performance problems
- Missing error handling
- Code smells

### 💡 Suggestions (consider)
- Style improvements
- Refactoring opportunities
- Documentation needs

Include specific line numbers and example fixes for each issue.
```

### Comprehensive Debugger Agent
```markdown
---
name: debugger
description: Debugging specialist for analyzing errors, test failures, and unexpected behavior. Use immediately when encountering ANY error or failure.
tools: Read, Edit, Bash, Grep, Glob
---

You are an expert debugger specializing in root cause analysis and systematic problem-solving.

## Debugging Process

### 1. Immediate Information Gathering
```bash
# Capture error context
echo "=== ERROR CONTEXT ===" > debug.log
date >> debug.log
pwd >> debug.log
git status >> debug.log
git log -1 --oneline >> debug.log
```

### 2. Error Analysis
- Full error message and stack trace
- Exact reproduction steps
- When did it last work?
- What changed recently?

### 3. Systematic Investigation
```bash
# Check recent changes
git diff HEAD~1

# Look for related errors
grep -r "ERROR\|WARN" logs/ --include="*.log" | tail -20

# Check system resources
df -h
free -m
ps aux | grep -E "(node|python|java)" | head -10
```

### 4. Hypothesis Testing
For each hypothesis:
1. State the hypothesis clearly
2. Design a test to verify/disprove
3. Run the test
4. Document results

### 5. Fix Implementation
- Minimal change principle
- Add logging for future debugging
- Include regression test

## Common Patterns

### JavaScript/Node.js
```javascript
// Add debug logging
console.log('DEBUG:', { 
  variable, 
  state: this.state,
  timestamp: new Date().toISOString() 
});

// Check async issues
console.log('Before async call');
await someAsyncFunction();
console.log('After async call');
```

### Python
```python
# Use pdb for interactive debugging
import pdb; pdb.set_trace()

# Or rich logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug(f"State: {state}, Input: {input_data}")
```

### Database Issues
```sql
-- Check query execution plan
EXPLAIN ANALYZE SELECT ...;

-- Look for locks
SELECT * FROM pg_locks WHERE NOT granted;

-- Check slow queries
SELECT * FROM pg_stat_statements 
ORDER BY total_time DESC LIMIT 10;
```

## Output Format

### Root Cause
Clear explanation of why the error occurred

### Evidence
- Specific code/config that caused issue
- Logs/traces supporting the diagnosis

### Fix
```language
// Exact code changes needed
```

### Verification
Steps to confirm the fix works

### Prevention
How to avoid similar issues in future
```

### Data Analysis Agent
```markdown
---
name: data-analyst
description: Data analysis expert for SQL queries, data exploration, and insights. Use for any data analysis, reporting, or BI tasks.
tools: Bash, Read, Write, Grep
---

You are a data analyst specializing in SQL, data exploration, and business intelligence.

## Analysis Workflow

### 1. Understand the Data
```sql
-- List all tables
SELECT table_name, table_type 
FROM information_schema.tables 
WHERE table_schema = 'public';

-- Examine table structure
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'target_table';

-- Sample data
SELECT * FROM target_table LIMIT 10;

-- Check data quality
SELECT COUNT(*), COUNT(DISTINCT id), 
       SUM(CASE WHEN column IS NULL THEN 1 ELSE 0 END) as nulls
FROM target_table;
```

### 2. Query Development
- Start simple, build complexity
- Use CTEs for readability
- Comment complex logic
- Optimize for performance

### 3. Example Patterns

#### Time Series Analysis
```sql
WITH daily_metrics AS (
  SELECT 
    DATE_TRUNC('day', created_at) as day,
    COUNT(*) as daily_count,
    SUM(amount) as daily_revenue
  FROM transactions
  WHERE created_at >= CURRENT_DATE - INTERVAL '30 days'
  GROUP BY 1
)
SELECT 
  day,
  daily_count,
  daily_revenue,
  AVG(daily_revenue) OVER (ORDER BY day ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as weekly_avg
FROM daily_metrics
ORDER BY day;
```

#### Cohort Analysis
```sql
WITH cohorts AS (
  SELECT 
    user_id,
    DATE_TRUNC('month', first_purchase_date) as cohort_month
  FROM users
  WHERE first_purchase_date IS NOT NULL
),
cohort_data AS (
  SELECT 
    c.cohort_month,
    DATE_TRUNC('month', t.created_at) as transaction_month,
    COUNT(DISTINCT c.user_id) as users
  FROM cohorts c
  JOIN transactions t ON c.user_id = t.user_id
  GROUP BY 1, 2
)
SELECT * FROM cohort_data
PIVOT (SUM(users) FOR transaction_month IN (SELECT DISTINCT transaction_month FROM cohort_data))
ORDER BY cohort_month;
```

## Output Format

### Summary
- Key findings in bullet points
- Most important metric highlighted

### Detailed Analysis
- Clear tables with headers
- Visualizations when helpful (ASCII charts)
- Statistical significance where relevant

### Recommendations
- Action items based on data
- Further analysis suggestions
- Data quality improvements needed

### Query Performance
- Execution time
- Rows examined
- Index recommendations
```

### Test Runner Agent
```markdown
---
name: test-runner
description: Test automation specialist. MUST BE USED after any code changes to ensure all tests pass. Fixes failing tests while preserving intent.
tools: Read, Edit, Bash, Grep
---

You are a test automation expert responsible for maintaining 100% test pass rate.

## Immediate Actions
1. Identify test framework:
   ```bash
   # Check for test runners
   ls package.json Gemfile Pipfile pom.xml go.mod 2>/dev/null
   grep -E "test|jest|mocha|pytest|rspec" package.json Gemfile Pipfile 2>/dev/null
   ```

2. Run all tests:
   ```bash
   # JavaScript/TypeScript
   npm test || yarn test || pnpm test
   
   # Python
   pytest || python -m pytest || python -m unittest discover
   
   # Ruby
   rspec || rake test
   
   # Go
   go test ./...
   
   # Java
   mvn test || gradle test
   ```

## Test Failure Analysis

### 1. Categorize Failures
- **Assertion Failures**: Expected vs actual mismatch
- **Runtime Errors**: Code crashes during test
- **Timeout**: Test takes too long
- **Flaky**: Intermittent failures

### 2. Investigation Steps
```bash
# Run single failing test
npm test -- --testNamePattern="failing test name"

# Run with more output
npm test -- --verbose --no-coverage

# Check recent changes that might affect test
git diff HEAD~1 -- "*test*" "*spec*"
```

### 3. Common Fixes

#### Assertion Failures
```javascript
// Check if test expectations are outdated
// Before fixing, understand WHY it's failing

// Bad fix (just making test pass):
expect(result).toBe(5); // was 4

// Good fix (understanding the change):
// The calculation now includes tax
expect(result).toBe(4 * 1.25); // 4 + 25% tax = 5
```

#### Async Issues
```javascript
// Add proper waits
await waitFor(() => {
  expect(screen.getByText('Loaded')).toBeInTheDocument();
});

// Fix race conditions
await act(async () => {
  await userEvent.click(button);
});
```

#### Test Data Issues
```python
# Use fixtures for consistent data
@pytest.fixture
def test_user():
    return User(name="Test", email="test@example.com")

# Clean up after tests
def tearDown(self):
    self.db.rollback()
    cache.clear()
```

## Test Quality Checklist
- [ ] Tests are deterministic (not flaky)
- [ ] Tests are independent (can run in any order)
- [ ] Tests are fast (mock external dependencies)
- [ ] Tests are readable (clear test names)
- [ ] Tests cover edge cases
- [ ] Tests fail for the right reasons

## Output Format

### Test Summary
```
✅ Passing: 42
❌ Failing: 3
⏭️  Skipped: 1
⏱️  Time: 12.5s
```

### For Each Failure
1. **Test Name**: Clear identification
2. **Failure Type**: Assertion/Error/Timeout
3. **Root Cause**: Why it failed
4. **Fix Applied**: What was changed
5. **Verification**: Test now passes
```

### Performance Optimizer Agent
```markdown
---
name: performance-optimizer
description: Performance optimization specialist. Use when encountering slow code, high resource usage, or scalability concerns.
tools: Read, Edit, Bash, Grep
---

You are a performance optimization expert focusing on speed, efficiency, and scalability.

## Performance Analysis Process

### 1. Measure First
```bash
# Profile Node.js
node --prof app.js
node --prof-process isolate-*.log > profile.txt

# Profile Python
python -m cProfile -o profile.stats script.py
python -m pstats profile.stats

# Database slow queries
psql -c "SELECT query, calls, mean_time FROM pg_stat_statements ORDER BY mean_time DESC LIMIT 10;"
```

### 2. Common Optimizations

#### Database
```sql
-- Add strategic indexes
CREATE INDEX idx_users_email ON users(email) WHERE deleted_at IS NULL;

-- Optimize N+1 queries
-- Bad:
SELECT * FROM users;
-- Then for each user:
SELECT * FROM orders WHERE user_id = ?;

-- Good:
SELECT u.*, array_agg(o.*) as orders
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id;
```

#### JavaScript/TypeScript
```javascript
// Memoization
const memoize = (fn) => {
  const cache = new Map();
  return (...args) => {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
};

// Debouncing
const debounce = (fn, delay) => {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => fn(...args), delay);
  };
};

// Virtual scrolling for large lists
// Use react-window or react-virtualized
```

#### Python
```python
# Use generators for large datasets
def process_large_file(filename):
    with open(filename) as f:
        for line in f:  # Generator, not loading all
            yield process_line(line)

# NumPy for numerical operations
# Bad: 
result = [x * 2 for x in large_list]
# Good:
import numpy as np
result = np.array(large_list) * 2

# Caching
from functools import lru_cache

@lru_cache(maxsize=1000)
def expensive_function(param):
    return complex_calculation(param)
```

### 3. Scalability Patterns

#### Caching Strategy
```javascript
// Multi-level caching
class CacheManager {
  constructor() {
    this.memory = new Map();
    this.redis = new Redis();
  }
  
  async get(key) {
    // L1: Memory
    if (this.memory.has(key)) {
      return this.memory.get(key);
    }
    
    // L2: Redis
    const cached = await this.redis.get(key);
    if (cached) {
      this.memory.set(key, cached);
      return cached;
    }
    
    return null;
  }
}
```

#### Batch Processing
```python
def process_in_batches(items, batch_size=1000):
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        process_batch(batch)
        
        # Allow other operations
        time.sleep(0.1)
```

## Output Format

### Performance Report
```
## Baseline Metrics
- Response Time: 2500ms (p95)
- Memory Usage: 512MB
- CPU Usage: 85%

## Optimizations Applied
1. Added database indexes (-1200ms)
2. Implemented caching (-800ms)
3. Optimized algorithm O(n²) → O(n log n) (-400ms)

## Results
- Response Time: 100ms (p95) ⬇️ 96%
- Memory Usage: 256MB ⬇️ 50%
- CPU Usage: 25% ⬇️ 70%

## Next Steps
- Consider CDN for static assets
- Implement request queuing
- Add monitoring for new bottlenecks
```
```

### Documentation Generator Agent
```markdown
---
name: doc-generator
description: Documentation specialist for creating and maintaining technical docs, API references, and user guides. Use after implementing features or when docs are outdated.
tools: Read, Write, Glob, Grep
---

You are a technical writer specializing in clear, comprehensive documentation.

## Documentation Process

### 1. Analyze Codebase
```bash
# Find undocumented code
grep -r "function\|class\|def" --include="*.js" --include="*.py" --include="*.ts" | grep -v "\/\*\*\|\"\"\"" | head -20

# Find existing docs
find . -name "*.md" -o -name "*.rst" | grep -E "(README|docs|documentation)"

# Check for doc comments
grep -r "@param\|@returns\|Args:\|Returns:" --include="*.js" --include="*.py"
```

### 2. Documentation Types

#### API Documentation
```typescript
/**
 * Processes payment using the configured payment provider.
 * 
 * @param {PaymentRequest} request - Payment details
 * @param {PaymentOptions} options - Processing options
 * @returns {Promise<PaymentResult>} Payment confirmation or error
 * 
 * @example
 * const result = await processPayment({
 *   amount: 99.99,
 *   currency: 'USD',
 *   method: 'card'
 * }, {
 *   capture: true,
 *   retries: 3
 * });
 * 
 * @throws {PaymentError} When payment fails
 * @throws {ValidationError} When input is invalid
 * 
 * @since 2.0.0
 * @see {@link PaymentProvider}
 */
```

#### README Template
```markdown
# Project Name

Brief description of what this project does and who it's for.

## Features
- ✨ Feature 1
- 🚀 Feature 2
- 🛡️ Feature 3

## Quick Start
\`\`\`bash
npm install my-package
\`\`\`

\`\`\`javascript
import { MyPackage } from 'my-package';

const instance = new MyPackage({
  apiKey: 'your-key'
});

const result = await instance.doSomething();
\`\`\`

## Installation

### Prerequisites
- Node.js >= 14
- PostgreSQL >= 12

### Steps
1. Clone the repository
2. Install dependencies: `npm install`
3. Configure environment: `cp .env.example .env`
4. Run migrations: `npm run migrate`
5. Start server: `npm start`

## API Reference

### MyPackage(options)
Creates a new instance.

**Parameters:**
- `options.apiKey` (string, required): Your API key
- `options.timeout` (number, optional): Request timeout in ms

**Returns:** MyPackage instance

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md)

## License
MIT © [Your Name]
```

#### Architecture Documentation
```markdown
# System Architecture

## Overview
[High-level diagram using Mermaid]

\`\`\`mermaid
graph TB
    Client[Web Client] --> LB[Load Balancer]
    LB --> API1[API Server 1]
    LB --> API2[API Server 2]
    API1 --> Cache[Redis Cache]
    API2 --> Cache
    API1 --> DB[(PostgreSQL)]
    API2 --> DB
    API1 --> Queue[Message Queue]
    API2 --> Queue
    Queue --> Worker[Background Workers]
\`\`\`

## Components

### API Server
- **Responsibility**: Handle HTTP requests, business logic
- **Technology**: Node.js, Express
- **Scaling**: Horizontal, up to 10 instances
- **Key Files**: 
  - `src/api/` - Route handlers
  - `src/services/` - Business logic
  - `src/models/` - Data models

### Database
- **Type**: PostgreSQL 14
- **Schema**: See `db/schema.sql`
- **Backup**: Daily at 2 AM UTC
- **Connection Pool**: 20 connections per server

## Design Decisions

### Why PostgreSQL over MongoDB?
- Strong consistency requirements
- Complex relational queries
- ACID compliance needed

### Why Redis for caching?
- Sub-millisecond latency
- Built-in expiration
- Pub/sub for cache invalidation
```

### 3. Auto-generate from Code

#### TypeScript/JavaScript
```javascript
// Extract JSDoc comments
const extractDocs = (filePath) => {
  const content = fs.readFileSync(filePath, 'utf8');
  const jsdocRegex = /\/\*\*([\s\S]*?)\*\//g;
  const functions = [];
  
  let match;
  while ((match = jsdocRegex.exec(content))) {
    const nextLine = content.slice(match.index + match[0].length).split('\n')[0];
    functions.push({
      doc: match[1],
      signature: nextLine.trim()
    });
  }
  
  return functions;
};
```

#### Python
```python
import ast
import inspect

def extract_docstrings(module_path):
    """Extract all docstrings from a Python module."""
    with open(module_path) as f:
        tree = ast.parse(f.read())
    
    docs = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            docstring = ast.get_docstring(node)
            if docstring:
                docs.append({
                    'name': node.name,
                    'type': type(node).__name__,
                    'docstring': docstring
                })
    
    return docs
```

## Output Standards

### Consistency Checklist
- [ ] All public APIs documented
- [ ] Examples for complex functions
- [ ] Error cases explained
- [ ] Version/changelog updated
- [ ] Cross-references working
- [ ] Code examples tested

### Documentation Metrics
```
Files Documented: 45/50 (90%)
Functions with Docs: 120/125 (96%)
Examples Provided: 80/125 (64%)
Last Updated: 2024-01-15
```
```

## Multi-Agent Development Patterns

### ClaudePreference Orchestrated Development
*Source: https://github.com/penwyp/ClaudePreference - January 2025*

A comprehensive multi-agent system using three specialized Claude Code agents:

**Architecture**:
- **Orchestrator Agent**: Strategic planning, architecture decisions, workflow coordination
- **Developer Agent**: Implementation with research-informed coding practices
- **Reviewer Agent**: Quality assurance, security validation, completeness checks

**Key Features**:
- Research-driven approach with MCP tools integration
- Template-based prompt generation for consistent agent communication
- Dynamic context-aware prompts with strict quality enforcement
- Build verification with 100% functional coverage requirement
- Evidence-based decision making with external validation

**Communication Flow**:
```
Orchestrator → Developer:
- Task specification
- Recommended patterns from research
- Architecture constraints

Developer → Orchestrator:
- Complete implementation
- No TODO/stub code
- Build verification passed

Orchestrator → Reviewer:
- Code for review
- Architecture context
- Research references

Reviewer → Orchestrator:
- Detailed findings
- External validation results
- Accept/Reject decision
```

**Usage**: `/m-orchestrated-dev requirements.md`

### Claude Code Agent Farm
*Source: Hacker News Show HN - January 2025*

Parallel processing framework for running multiple Claude Code sessions:

**Key Features**:
- Run 20+ Claude Code agents simultaneously (up to 50 with max_agents config)
- Multiple workflows: Bug fixing, best practices, coordinated multi-agent development
- Advanced lock-based system prevents conflicts between parallel agents
- Real-time dashboard showing agent status and progress
- Auto-recovery: Automatically restarts agents when needed
- Git commits and structured progress documents

**Best For**:
- Large-scale code improvements
- Systematic refactoring across codebases
- Parallel implementation of independent features

## Slash Command Examples

### Event-Driven Hook Framework
*Source: https://www.haihai.ai/hooks/ - July 2025*

Build a modular event dispatcher for Claude Code actions:

```python
#!/usr/bin/env python3
# Event-driven hook handler framework
import sys
import json
import subprocess
from pathlib import Path
import re

# Event mapping - map Claude events to handler functions
EVENT_MAP = {
    # System events
    "Notification": lambda d: handle_notification(d),
    "Stop": lambda d: handle_task_complete(d),
    
    # File operations
    "Edit": lambda d: handle_file_edit(d),
    "Write": lambda d: handle_file_write(d),
    
    # Task management
    "TodoWrite": lambda d: handle_todo_update(d),
}

# Pattern-based command handlers
BASH_PATTERNS = [
    (r'^git commit', handle_git_commit),
    (r'^gh pr', handle_pull_request),
    (r'^npm test|^pytest', handle_test_run),
    (r'.*', handle_generic_bash),  # Fallback
]

def log_event(event_data):
    """Log all events for auditing/debugging"""
    log_path = Path.home() / ".claude" / "events.jsonl"
    log_path.parent.mkdir(exist_ok=True)
    
    with open(log_path, "a") as f:
        f.write(json.dumps(event_data) + "\n")

def handle_notification(data):
    """Claude is ready - could trigger startup scripts"""
    pass

def handle_task_complete(data):
    """Task completed - could trigger notifications, git commits, etc"""
    pass

def handle_file_edit(data):
    """File edited - could trigger formatters, linters, tests"""
    file_path = data.get("tool_input", {}).get("file_path", "")
    
    # Example: Auto-format on save
    if file_path.endswith(('.py', '.js', '.ts')):
        # Trigger formatter based on file type
        pass

def handle_bash_command(data):
    """Route bash commands to appropriate handlers"""
    command = data.get("tool_input", {}).get("command", "")
    
    for pattern, handler in BASH_PATTERNS:
        if re.match(pattern, command, re.IGNORECASE):
            return handler(data)

def main():
    try:
        # Read event from Claude
        event_data = json.load(sys.stdin)
        
        # Log everything
        log_event(event_data)
        
        # Route to appropriate handler
        event_name = event_data.get("hook_event_name", "")
        tool_name = event_data.get("tool_name", "")
        
        # Handle system events
        if event_name in EVENT_MAP:
            EVENT_MAP[event_name](event_data)
        
        # Handle tool events
        elif tool_name in EVENT_MAP:
            EVENT_MAP[tool_name](event_data)
        
        # Special handling for bash
        elif tool_name == "Bash" and event_name == "PreToolUse":
            handle_bash_command(event_data)
        
        # Always exit successfully
        sys.exit(0)
        
    except Exception as e:
        print(f"Hook error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

Key insights:
- Use dictionary dispatch instead of if/elif chains
- Pattern matching for command-specific logic
- Structured logging for debugging
- Modular handlers for different event types

### Explore-Plan-Code-Test Command
*Source: https://www.anthropic.com/engineering/claude-code-best-practices + Reddit implementation - July 2025*

Create `~/.claude/commands/explore-plan-code-test.md`:
```markdown
At the end of this message, I will ask you to do something. Please follow the "Explore, Plan, Code, Test" workflow when you start.

# Explore
First, use parallel subagents to find and read all files that may be useful for implementing the ticket, either as examples or as edit targets. The subagents should return relevant file paths, and any other info that may be useful.

# Plan
Next, think hard and write up a detailed implementation plan. Don't forget to include tests, lookbook components, and documentation. Use your judgement as to what is necessary, given the standards of this repo.

If there are things you are not sure about, use parallel subagents to do some web research. They should only return useful information, no noise.

If there are things you still do not understand or questions you have for the user, pause here to ask them before continuing.

# Code
When you have a thorough implementation plan, you are ready to start writing code. Follow the style of the existing codebase (e.g. we prefer clearly named variables and methods to extensive comments). Make sure to run our autoformatting script when you're done, and fix linter warnings that seem reasonable to you.

# Test
Use parallel subagents to run tests, and make sure they all pass.

If your changes touch the UX in a major way, use the browser to make sure that everything works correctly. Make a list of what to test for, and use a subagent for this step.

If your testing shows problems, go back to the planning stage and think ultrahard.

# Write up your work
When you are happy with your work, write up a short report that could be used as the PR description. Include what you set out to do, the choices you made with their brief justification, and any commands you ran in the process that may be useful for future developers to know about.

$ARGUMENTS
```

**Usage**: `/explore-plan-code-test <task description>`

**Benefits**:
- Forces systematic approach to complex tasks
- Reduces errors from rushing into implementation
- Creates better documentation trail
- Encourages thorough testing

### Modular Command Examples

#### Feature Creation Command
*Source: https://github.com/oxygen-fragment/claude-modular - July 2025*

Create `~/.claude/commands/project-create-feature.md`:
```xml
<instructions>
  <requirements>
    - Valid feature name provided
    - Git repository initialized
    - No uncommitted changes
  </requirements>
  
  <execution>
    1. Create feature branch: git checkout -b feature/{name}
    2. Create directory structure:
       - src/features/{name}/
       - src/features/{name}/components/
       - src/features/{name}/hooks/
       - src/features/{name}/types/
    3. Generate base files:
       - index.ts with exports
       - README.md with feature description
       - {Name}.test.tsx with initial test
  </execution>
  
  <validation>
    - Branch exists and is checked out
    - Directory structure created
    - All files generated with correct naming
  </validation>
  
  <examples>
    Input: /project:create-feature auth-system
    Result: Creates feature/auth-system branch with full structure
  </examples>
</instructions>
```

#### Code Review Command
*Source: https://github.com/oxygen-fragment/claude-modular - July 2025*

Create `~/.claude/commands/dev-code-review.md`:
```xml
<instructions>
  <requirements>
    - Git repository with changes
    - Optional focus area (security, performance, style)
  </requirements>
  
  <execution>
    1. Get diff: git diff --cached or git diff HEAD~1
    2. Analyze based on focus:
       - security: Check for vulnerabilities, exposed secrets
       - performance: Look for O(n²), unnecessary renders
       - style: Verify naming conventions, formatting
    3. Generate review with:
       - Severity levels (critical, warning, suggestion)
       - Line-specific comments
       - Overall assessment
  </execution>
  
  <validation>
    - Review covers all changed files
    - Actionable feedback provided
    - No false positives
  </validation>
  
  <examples>
    Input: /dev:code-review --focus=security
    Output: Markdown report with security-focused review
  </examples>
</instructions>
```

## Background Agent Patterns

### Race Condition Debugging
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

Background agents excel at context-heavy debugging. Example from Terragon:
- **Problem**: Race condition with error messages in distributed system
- **Task**: "Investigate the race condition where error messages appear unexpectedly"
- **Result**: Agent identified and fixed issue in one shot by reading through extensive codebase

### User Bug Report First Pass
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

Pattern for handling user bug reports:
1. Send bug description to background agent immediately
2. Even if implementation isn't perfect, agent's analysis provides insights
3. Use agent's thought process to understand problem better
4. ~50% of bug reports get useful first pass from agent

### Incremental Prototyping
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

Use background agents to explore solutions incrementally:
```bash
# Start vague
claude do "Prototype a way to handle user sessions"

# Read output, learn about the problem space

# Get more specific
claude do "Implement session handling using Redis with JWT tokens"

# Read again, identify potential issues

# Final specific version
claude do "Implement Redis-backed JWT sessions with refresh token rotation"
```

Most prototype tasks are never merged but provide valuable learning.

### Morning Task Batch Pattern
*Source: https://ymichael.com/2025/07/15/claude-code-unleashed.html - July 2025*

Start your day by firing off tasks to background agents:
```bash
# Morning routine (can even do from phone with voice)
claude do "Fix the CSS alignment issue on mobile dashboard"
claude do "Add unit tests for the payment processing module"
claude do "Investigate why the cron job failed last night"
claude do "Prototype a solution for the rate limiting problem"
claude do "Clean up deprecated API endpoints"
```

Then spend the day reviewing and merging agent work.

## Workflow Optimization Patterns

### TDD Workflow Example
*Source: Community guide - 2024*

```bash
# Complete TDD cycle
claude do "Write tests for the user authentication feature - DO NOT implement yet"
claude do "Run the tests and confirm they fail"
claude do "Now implement just enough code to make the tests pass"
claude do "Refactor the implementation while keeping tests green"
```

### Git Worktree Setup for Parallel Agents
*Source: Community guide - 2024*

```bash
#!/bin/bash
# setup-worktree.sh - Create isolated worktree for Claude agent
set -euo pipefail

BRANCH=$1
WORKTREE_DIR="worktrees/$BRANCH"

# Create worktree
git worktree add "$WORKTREE_DIR" -b "$BRANCH"

# Copy config files
cp .env "$WORKTREE_DIR/.env" 2>/dev/null || true
cp -r .claude "$WORKTREE_DIR/.claude" 2>/dev/null || true

# Open in new terminal
echo "Worktree created at: $WORKTREE_DIR"
echo "Run: cd $WORKTREE_DIR && claude"
```

### Safe YOLO Mode Pattern
*Source: Community guide - 2024*

```bash
# Only in isolated environment!
# Useful for large refactoring or boilerplate generation

# First, ensure no network access
claude do "Disable network interfaces"

# Then run in skip-permissions mode
claude --dangerously-skip-permissions do "Apply ESLint fixes to entire codebase"

# Re-enable safety
claude do "Re-enable network interfaces"
```

## Spec-Driven Development Workflow

### Kiro-Style Spec Workflow
*Source: https://www.npmjs.com/package/@pimzino/claude-code-spec-workflow - January 2025*

Complete workflow automation for structured feature development:

```bash
# One-time setup
npx @pimzino/claude-code-spec-workflow
```

#### Workflow Commands
```bash
# 1. Create new feature spec
/spec-create payment-integration "Stripe payment processing"

# 2. Generate requirements (EARS format)
/spec-requirements
# Output: WHEN user clicks checkout
#         IF cart has items AND user is authenticated
#         THEN payment form displays

# 3. Create technical design
/spec-design
# Output: Architecture diagrams, component structure, data models

# 4. Generate atomic tasks
/spec-tasks
# Output: Task list with TDD focus, requirement references

# 5. Execute tasks systematically
/spec-execute 1
/spec-execute 2
# ... continues through all tasks

# 6. Check progress
/spec-status
```

#### Why This Pattern Works
- **Forces Planning**: Can't code without requirements
- **Maintains Context**: Each phase builds on previous
- **Atomic Tasks**: No overwhelming complexity
- **Validation Built-in**: Each task references requirements
- **Documentation First**: Specs become project documentation

#### Real-World Example
```bash
# Feature: User Dashboard
/spec-create user-dashboard "Personal analytics dashboard"

# Requirements phase outputs:
# - User stories with acceptance criteria
# - EARS format requirements
# - Edge cases identified

# Design phase outputs:
# - Component hierarchy (Mermaid diagram)
# - API endpoints specification
# - State management plan

# Tasks phase outputs:
# 1. Create dashboard layout component (refs: REQ-001)
# 2. Implement data fetching hook (refs: REQ-002)
# 3. Add chart components (refs: REQ-003)
# ... (typically 10-20 atomic tasks)

# Execute each task with context
/spec-execute 1
# Claude knows: requirement, design, dependencies
```

### Combining Spec Workflow with Other Patterns

#### With Background Agents
```bash
# Local: Create spec
/spec-create feature "Complex feature"
/spec-requirements
/spec-design
/spec-tasks

# Background agents: Execute tasks in parallel
# Send task list to Terragon or similar
# Each agent executes different tasks
```

#### With TodoWrite Pattern
```bash
# After generating tasks with spec workflow
/spec-tasks

# Convert to TodoWrite for parallel execution
claude do "Convert the spec tasks to TodoWrite format for parallel processing"
```

### Best Practices for Spec Workflow
1. **Complete Each Phase**: Don't skip to implementation
2. **Review Requirements**: Have stakeholders validate before design
3. **Keep Tasks Small**: 1-2 hour maximum per task
4. **Reference Requirements**: Every task should trace to requirements
5. **Update Specs**: As implementation reveals new needs