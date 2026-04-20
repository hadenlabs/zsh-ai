## ADDED Requirements

### Requirement: Support --dry-run mode
The system MUST support a `--dry-run` flag that shows what would be done without making any changes.

#### Scenario: Dry-run shows planned changes
- **WHEN** user runs `hadx-opencode-sync --dry-run`
- **THEN** the system SHALL display the planned changes without modifying any files

#### Scenario: Dry-run does not modify files
- **WHEN** user runs `hadx-opencode-sync --dry-run`
- **THEN** no files in `docs/opencode/plugins` SHALL be created or modified

### Requirement: Preview mode output
The system MUST provide clear output indicating that preview mode is active.

#### Scenario: Preview mode indicator
- **WHEN** `--dry-run` flag is used
- **THEN** the output SHALL include a clear indicator that preview mode is enabled