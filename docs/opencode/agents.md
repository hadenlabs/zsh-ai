<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: OpenCode Agents -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->
<!-- Include: ac:toc -->

## Overview

This document describes the OpenCode agents defined in `/.opencode/agent/` and how they are expected to be used.

Agent files are Markdown with YAML frontmatter. The key fields you will see are:

- `name`: the identifier OpenCode uses for `subagent_type` when delegating via the Task tool.
- `description`: short purpose statement.
- `mode`: `primary` (top-level agent) or `subagent` (specialist invoked by another agent).
- `permission`: tool allow/deny rules (most subagents are intentionally restricted).

Notes:

- Some agent templates mention `.opencode/config/agent-metadata.json`. This repository includes a minimal version to keep agent references consistent.
- Category files like `/.opencode/agent/*/0-category.json` describe intended groupings and shared defaults, but they may not exactly match the on-disk filenames (see the “Name vs path” section).

## Directory layout

- Primary agents: `/.opencode/agent/<category>/*.md`
- Subagents: `/.opencode/agent/subagents/<group>/*.md`
- Category metadata: `/.opencode/agent/<category>/0-category.json`

## Name vs path (important)

There are two common identifiers:

- File path “slug” (how it is stored): e.g. `subagents/code/reviewer` from `/.opencode/agent/subagents/code/reviewer.md`.
- Frontmatter `name` (how OpenCode routes `subagent_type`): e.g. `CodeReviewer`.

When you call the Task tool, you generally use the frontmatter `name`:

```text
task(subagent_type="CodeReviewer", description="Review changes", prompt="...")
```

Also note that some category JSON references `subagents/code/tester`, but this repo uses `/.opencode/agent/subagents/code/test-engineer.md` with `name: TestEngineer`.

## Primary agents

| Agent | Mode | What it does | Typical use | Source |
| --- | --- | --- | --- | --- |
| OpenAgent | primary | General coordinator; routes work to subagents and tools | Default “do the thing” requests spanning multiple tasks | `.opencode/agent/core/openagent.md` |
| OpenCoder | primary | Coding-focused orchestrator; prefers code/test/build specialists | Implementing features/bugfixes with validation | `.opencode/agent/core/opencoder.md` |
| OpenSystemBuilder | primary | System generation orchestrator (agents/commands/workflows/context) | Building a custom OpenCode setup for a domain | `.opencode/agent/meta/system-builder.md` |
| OpenRepoManager | primary | Repository and PR workflow coordinator | Branch hygiene, PR preparation, multi-file housekeeping | `.opencode/agent/meta/repo-manager.md` |
| OpenCopywriter | primary | Marketing / persuasive writing | Copy, positioning, landing page text | `.opencode/agent/content/copywriter.md` |
| OpenTechnicalWriter | primary | Documentation specialist | Docs authoring and updates | `.opencode/agent/content/technical-writer.md` |
| OpenDataAnalyst | primary | Data analysis / insight generation | Summaries, metrics reasoning, data interpretation | `.opencode/agent/data/data-analyst.md` |

### Test-only / internal

| Agent       | Mode    | What it is                  | Guidance            | Source                           |
| ----------- | ------- | --------------------------- | ------------------- | -------------------------------- |
| Eval Runner | primary | Evaluation harness template | Do not use directly | `.opencode/agent/eval-runner.md` |

## Subagents (specialists)

Subagents are meant to be called by a primary agent (or by you explicitly) using `task(subagent_type="...")`.

### Core

| Agent | What it does | Notable limits | Source |
| --- | --- | --- | --- |
| ContextScout | Finds and recommends internal context files | Task-only focus; used early to load project standards | `.opencode/agent/subagents/core/contextscout.md` |
| ExternalScout | Fetches version-specific external docs | Use when a library/framework API details matter | `.opencode/agent/subagents/core/externalscout.md` |
| TaskManager | Breaks work into JSON task definitions and tracks status | Designed for structured, verifiable subtasks | `.opencode/agent/subagents/core/task-manager.md` |
| BatchExecutor | Runs multiple subtasks/agents in parallel batches | Coordination-heavy; integrates multiple subagents | `.opencode/agent/subagents/core/batch-executor.md` |
| StageOrchestrator | Multi-stage workflow orchestration with gates/rollbacks | Enforces stage transitions and validation gates | `.opencode/agent/subagents/core/stage-orchestrator.md` |
| DocWriter | Writes documentation as an authored artifact | Optimized for doc structure and consistency | `.opencode/agent/subagents/core/documentation.md` |
| ContextManager | Discovers/maintains `.opencode/context/` structure | Oriented to lifecycle/maintenance of context | `.opencode/agent/subagents/core/context-manager.md` |
| Context Retriever | Generic context search/retrieval helper | Lightweight context lookup | `.opencode/agent/subagents/core/context-retriever.md` |

### Code

| Agent | What it does | Notable limits | Source |
| --- | --- | --- | --- |
| CoderAgent | Implements coding subtasks sequentially | Very limited bash; edit denied for secrets and `.git/**` | `.opencode/agent/subagents/code/coder-agent.md` |
| TestEngineer | Writes tests (TDD-oriented) | Bash only for test commands; deterministic tests | `.opencode/agent/subagents/code/test-engineer.md` |
| BuildAgent | Runs type-check/build validation | Read-only; bash restricted to build/typecheck commands | `.opencode/agent/subagents/code/build-agent.md` |
| CodeReviewer | Reviews code for correctness/security/quality | Strict read-only: no bash/write/edit | `.opencode/agent/subagents/code/reviewer.md` |

### Planning

| Agent | What it does | Source |
| --- | --- | --- |
| ArchitectureAnalyzer | DDD-driven architecture analysis and boundaries | `.opencode/agent/subagents/planning/architecture-analyzer.md` |
| StoryMapper | User journeys to epics/stories and vertical slices | `.opencode/agent/subagents/planning/story-mapper.md` |
| PrioritizationEngine | RICE/WSJF scoring and roadmap slicing | `.opencode/agent/subagents/planning/prioritization-engine.md` |
| ContractManager | Contract-first API work (OpenAPI/Swagger) | `.opencode/agent/subagents/planning/contract-manager.md` |
| ADRManager | Lightweight ADR creation | `.opencode/agent/subagents/planning/adr-manager.md` |

### Development

| Agent | What it does | Source |
| --- | --- | --- |
| OpenFrontendSpecialist | Frontend UI design specialist | `.opencode/agent/subagents/development/frontend-specialist.md` |
| OpenDevopsSpecialist | CI/CD and infrastructure automation specialist | `.opencode/agent/subagents/development/devops-specialist.md` |

### System builder

| Agent | What it does | Source |
| --- | --- | --- |
| DomainAnalyzer | Extracts core concepts, agent needs, and context structure from a domain | `.opencode/agent/subagents/system-builder/domain-analyzer.md` |
| AgentGenerator | Generates orchestrator/subagent prompt files (XML-optimized patterns) | `.opencode/agent/subagents/system-builder/agent-generator.md` |
| ContextOrganizer | Generates and organizes context files (standards/templates/lookup) | `.opencode/agent/subagents/system-builder/context-organizer.md` |
| WorkflowDesigner | Designs executable workflows with validation gates and context deps | `.opencode/agent/subagents/system-builder/workflow-designer.md` |
| CommandCreator | Generates custom slash commands with syntax and examples | `.opencode/agent/subagents/system-builder/command-creator.md` |

### Utilities

| Agent            | What it does                            | Source                                                |
| ---------------- | --------------------------------------- | ----------------------------------------------------- |
| Image Specialist | Image editing/analysis (Gemini tooling) | `.opencode/agent/subagents/utils/image-specialist.md` |

### Test

| Agent | What it is | Guidance | Source |
| --- | --- | --- | --- |
| Simple Responder | Test agent that returns a fixed string | For evaluation/testing only | `.opencode/agent/subagents/test/simple-responder.md` |

## Practical usage patterns

## How we use agents in zsh-ai

Use these as defaults:

- Repo/PR workflows and slash commands in `.opencode/commands/`: `OpenRepoManager`
- Code changes (feature/bugfix): `OpenCoder`
- Documentation in `docs/` (and generated README flows): `OpenTechnicalWriter`

Notes:

- `@path/to/file` attaches file contents to the conversation; it does not execute a command file.
- Slash commands are executed as `/command` (TUI) or `opencode run --command <name>` (CLI).
- `README.md` is generated from templates; update `provision/generators/README.yaml` / `provision/templates/README.tpl.md` and run `task readme`.

### Delegating to a subagent

Use the subagent’s frontmatter `name` as `subagent_type`:

```text
task(
  subagent_type="TestEngineer",
  description="Add regression tests",
  prompt="Add tests for ...; follow project conventions."
)
```

See also: `docs/opencode/tasks.md`.

### Permissions & safety

- Many subagents intentionally cannot edit or run arbitrary shell commands.
- Anything that looks like secret material (`*.env*`, `*.key`, `*.secret`) is commonly denied by agent permissions.
