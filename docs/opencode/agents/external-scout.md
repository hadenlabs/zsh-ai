<!-- Space: Projects -->
<!-- Parent: ZshAI -->
<!-- Title: OpenCode Agent - ExternalScout -->
<!-- Label: OpenCode -->
<!-- Include: docs/disclaimer.md -->

# ExternalScout

- Mode: subagent
- Source: `.opencode/agent/subagents/core/externalscout.md`
- Purpose: Fetch live, version-specific external documentation.

## How to invoke

```text
task(subagent_type="ExternalScout", description="Fetch docs", prompt="Fetch current docs for <library>: <what I need>. Context: <what I'm building>." )
```
