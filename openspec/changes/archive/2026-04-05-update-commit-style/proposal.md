## Why

Currently, the project's commit messages do not respect the goji commit style configured in jasper.toml. The configuration specifies a consistent format (`<type> <emoji> (<scope>): <subject>`) with GitHub style, signoff, and subject length limits. Without enforcing this style, commit history becomes inconsistent and harder to parse programmatically.

## What Changes

- **Configure goji**: Set up the goji commit tool to use the jasper.toml configuration
- **Enforce format**: Apply the `<type> <emoji> (<scope>): <subject>` format
- **Enable signoff**: Add Signed-off-by footer to commits
- **Set subject limit**: Cap commit subjects at 100 characters

## Capabilities

### New Capabilities

- **commit-style-enforcement**: Validates and creates commits following the goji style defined in jasper.toml with format `<type> <emoji> (<scope>): <subject>`, GitHub style, signoff enabled, and 100 character subject limit

### Modified Capabilities

- None

## Impact

- Commit workflow tooling (goji configuration)
- Developer commit experience