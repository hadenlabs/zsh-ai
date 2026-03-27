## ADDED Requirements

### Requirement: Agents must consult codemap.md before searching codebase

AI agents SHALL consult the repository's codemap.md files before performing any code searches or exploration to understand the codebase structure and locate relevant files efficiently.

#### Scenario: Agent needs to find implementation details
- **WHEN** an agent needs to understand or locate code in the repository
- **THEN** the agent MUST first read the appropriate codemap.md file to understand the architecture before performing searches