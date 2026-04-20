## ADDED Requirements

### Requirement: Show diff of changes
The system MUST display a diff of changes before applying them.

#### Scenario: Display diff output
- **WHEN** user runs `hadx-opencode-sync` without `--dry-run`
- **THEN** the system SHALL show a diff comparing current state with proposed changes

#### Scenario: Diff shows additions
- **WHEN** a new plugin is added to `opencode.json`
- **THEN** the diff SHALL show the new file as an addition

#### Scenario: Diff shows modifications
- **WHEN** an existing plugin configuration changes
- **THEN** the diff SHALL show the specific lines that changed

#### Scenario: Diff shows deletions
- **WHEN** a plugin is removed from `opencode.json`
- **THEN** the diff SHALL show the file as a deletion