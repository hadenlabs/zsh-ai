## Context

The zsh-ai project now has comprehensive codemap.md files documenting its architecture:
- Root codemap.md (repository atlas)
- config/codemap.md
- core/codemap.md
- internal/codemap.md
- pkg/codemap.md

AGENTS.md currently has no guidance on how agents should use these codemap files for searching or understanding the codebase.

## Goals / Non-Goals

**Goals:**
- Add a rule to AGENTS.md requiring agents to use codemap.md before performing searches
- Document the search workflow for agents
- Reference the codemap files in AGENTS.md

**Non-Goals:**
- No code changes - purely documentation update
- No changes to the codemap files themselves

## Decisions

1. **Add new section to AGENTS.md** - Created a new "Search Conventions" section in AGENTS.md that instructs agents to use codemap.md first.
2. **Reference codemap in Conventions section** - Added rule in the Conventions section of AGENTS.md stating that for searches, consult codemap.md first.

## Risks / Trade-offs

- (none - this is a low-risk documentation change)