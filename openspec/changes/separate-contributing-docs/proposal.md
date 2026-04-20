## Why

The current `docs/contributing.md` file contains 429 lines with multiple distinct topics (getting started, adding AI tools, styleguides, testing, code review). This monolithic structure makes it difficult for contributors to find specific information and maintain the documentation. Separating into focused documents will improve navigation and maintainability.

## What Changes

- Split `docs/contributing.md` into focused documents in `docs/contribute/`
- Create `docs/contribute/index.md` - Main contributing guide with getting started
- Create `docs/contribute/adding-tools.md` - Complete guide for adding new AI tools
- Create `docs/contribute/styleguide.md` - Git conventions, branches, code review
- Keep existing `docs/contribute/github-flow.md` as-is
- Update references in `AGENTS.md` and related documentation
- Add redirect/index from `docs/contributing.md` to new structure

## Capabilities

### New Capabilities

- `contributing-docs-structure`: Define the new documentation structure for contributions with separate focused guides

### Modified Capabilities

- None - this is a documentation reorganization only

## Impact

- Documentation files in `docs/contribute/` directory
- Reference updates in `AGENTS.md`
- No code changes required