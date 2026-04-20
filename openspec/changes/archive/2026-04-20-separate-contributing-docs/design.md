## Context

The current `docs/contributing.md` is a 429-line monolithic file containing:
- Getting Started / Development workflow
- Adding New AI Tools (comprehensive guide)
- Styleguides (Git commits, branches, code review)
- Testing references
- Code submission and review process

This structure makes it difficult for contributors to quickly find the information they need.

## Goals / Non-Goals

**Goals:**
- Split monolithic `docs/contributing.md` into focused, navigable documents
- Create clear directory structure under `docs/contribute/`
- Maintain all existing content and functionality
- Update all cross-references

**Non-Goals:**
- Rewrite or enhance content (only reorganize)
- Change the overall documentation system
- Modify code or implementation

## Decisions

### 1. Directory Structure

**Decision:** Use `docs/contribute/` as the base directory for all contribution-related docs.

**Rationale:** Already exists with `github-flow.md`. Maintains logical grouping.

**Alternative considered:** Create new top-level directory - rejected because `docs/contribute/` already exists and follows the pattern of other documentation sections.

### 2. File Split Strategy

**Decision:** Split into 4 main files:

| New File | Content From contributing.md |
|----------|------------------------------|
| `docs/contribute/index.md` | Getting Started, Development, Code Submission, Code Review, Code Acceptance |
| `docs/contribute/adding-tools.md` | Adding New AI Tools (full section) |
| `docs/contribute/styleguide.md` | Git Commit Messages, Branches, Documentation, Testing |
| `docs/contribute/github-flow.md` | (already exists - keep as-is) |

**Rationale:** Each file addresses a distinct contributor need:
- `index.md` - Quick start for new contributors
- `adding-tools.md` - Detailed technical guide for developers
- `styleguide.md` - Conventions and standards
- `github-flow.md` - Git workflow reference

### 3. Redirect Strategy

**Decision:** Update `docs/contributing.md` to contain only a redirect/note pointing to the new structure.

**Rationale:** Maintains backward compatibility for any existing links while guiding users to the new structure.

### 4. Reference Updates

**Decision:** Update references in:
- `AGENTS.md` - Quick reference for AI agents
- Any internal links within the documentation

**Rationale:** Ensure all cross-references work correctly after reorganization.

## Risks / Trade-offs

- **Risk:** Existing external links to `docs/contributing.md` may break
  - **Mitigation:** Keep `docs/contributing.md` as a redirect/alias

- **Risk:** Content duplication between files
  - **Mitigation:** Use clear cross-references instead of duplication

- **Risk:** Maintaining consistency across files
  - **Mitigation:** Follow consistent heading structure and style

## Open Questions

None - the approach is straightforward documentation reorganization.