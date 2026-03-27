## Why

Currently, AI agents searching for information in the codebase must rely on direct file reading or grep searches, which can be inefficient and miss architectural context. With the newly created codemap.md files documenting the repository structure, agents should leverage this architectural knowledge for more efficient and context-aware searches.

## What Changes

- Add a new rule to AGENTS.md requiring agents to use codemap.md as the first reference for understanding repository structure and locating code
- Agents must consult codemap.md before performing broad code searches
- Create reference to codemap.md in AGENTS.md search conventions

## Capabilities

### New Capabilities

- `codemap-search-rule`: Rule requiring agents to consult codemap.md files before performing codebase searches

### Modified Capabilities

- (none - this is a documentation/process change, not a spec-level behavior change)

## Impact

- AGENTS.md: New section with codemap search rule
- Documentation improvement for agent behavior consistency
- No code changes required