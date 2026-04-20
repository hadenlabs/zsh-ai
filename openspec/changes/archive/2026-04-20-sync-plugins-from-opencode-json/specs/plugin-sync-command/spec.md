## ADDED Requirements

### Requirement: hadx-opencode-sync command exists
The system MUST provide a command named `hadx-opencode-sync` that can be executed from the command line.

#### Scenario: Command is available
- **WHEN** user runs `hadx-opencode-sync` in the terminal
- **THEN** the command executes without "command not found" error

### Requirement: Read plugins from opencode.json
The system MUST read the plugins section from the `opencode.json` configuration file.

#### Scenario: Read plugins successfully
- **WHEN** `opencode.json` contains a valid `plugins` array
- **THEN** the system SHALL parse and extract all plugin configurations

#### Scenario: No plugins section exists
- **WHEN** `opencode.json` does not contain a `plugins` section
- **THEN** the system SHALL handle gracefully without error

### Requirement: Generate documentation in docs/opencode/plugins
The system MUST generate Markdown documentation files in the `docs/opencode/plugins` directory.

#### Scenario: Create docs directory if not exists
- **WHEN** `docs/opencode/plugins` directory does not exist
- **THEN** the system SHALL create the directory structure

#### Scenario: Generate one file per plugin
- **WHEN** plugins are read from `opencode.json`
- **THEN** the system SHALL generate one `.md` file per plugin in `docs/opencode/plugins`

### Requirement: Standard documentation structure
The system MUST generate documentation files following a standardized Markdown structure.

#### Scenario: File contains required sections
- **WHEN** documentation file is generated
- **THEN** it SHALL contain sections for: plugin name, description, configuration options, and usage examples