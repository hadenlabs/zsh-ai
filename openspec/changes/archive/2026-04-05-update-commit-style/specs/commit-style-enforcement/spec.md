## ADDED Requirements

### Requirement: Goji uses jasper.toml configuration
The goji commit tool SHALL read and respect the configuration defined in jasper.toml, including format, style, signoff, and subject length limits.

#### Scenario: Goji reads jasper.toml
- **WHEN** goji is invoked without explicit configuration flags
- **THEN** it uses settings from jasper.toml (format: `<type> <emoji> (<scope>): <subject>`, style: github, signoff: true, subjectMaxLength: 100)

### Requirement: Commit follows goji format
Commit messages SHALL follow the format `<type> <emoji> (<scope>): <subject>` as specified in jasper.toml.

#### Scenario: Valid commit format
- **WHEN** developer creates a commit with goji using valid type, emoji, scope, and subject
- **THEN** commit message follows `<type> <emoji> (<scope>): <subject>` format

#### Scenario: Invalid commit format rejected
- **WHEN** developer attempts commit with invalid format
- **THEN** goji rejects the commit and displays validation error

### Requirement: Signoff is automatically added
Commits SHALL include a Signed-off-by footer when created through goji.

#### Scenario: Signoff added to commit
- **WHEN** developer creates commit via goji
- **THEN** commit includes `Signed-off-by:` footer line

### Requirement: Subject length is validated
Commit subjects SHALL be validated against the maximum length of 100 characters.

#### Scenario: Subject within limit
- **WHEN** developer creates commit with subject under 100 characters
- **THEN** commit is accepted

#### Scenario: Subject exceeds limit
- **WHEN** developer creates commit with subject over 100 characters
- **THEN** goji rejects the commit and shows length validation error