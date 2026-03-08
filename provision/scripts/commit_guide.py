#!/usr/bin/env python3

import sys


def _read_toml(path):
    try:
        import tomllib  # py3.11+
    except ModuleNotFoundError:
        print("Python 3.11+ is required (tomllib missing)", file=sys.stderr)
        raise

    with open(path, "rb") as f:
        return tomllib.load(f)


def main():
    cfg = _read_toml("infobot.toml")

    commit = cfg.get("commit", {})
    issue = cfg.get("issueTracking", {})
    issue_branch = issue.get("branch", {}) if isinstance(issue.get("branch", {}), dict) else {}
    providers = (commit.get("providers", {}) if isinstance(commit.get("providers", {}), dict) else {})

    style = commit.get("style", "jira")
    fmt = commit.get("format", "<emoji> <type>(<scope>): <subject>")
    signoff = bool(commit.get("signoff", True))

    print("Commit tool: goji (.goji.json)")
    print("Agent config: infobot.toml")
    print(f"Commit style: {style}")
    print(f"Format: {fmt}")
    print(f"Sign-off: {'required' if signoff else 'optional'}")
    print("")

    if style == "jira":
        key = issue.get("projectKey", "AR")
        rx = (issue.get("keyRegexOverride", "") or "").strip() or f"^{key}-[0-9]+$"
        brx_override = (issue_branch.get("jiraKeyRegexOverride", "") or "").strip()
        brx_from_key = bool(issue_branch.get("jiraKeyFromProjectKey", True))
        if brx_override:
            brx = brx_override
        elif brx_from_key:
            brx = f"({key}-[0-9]+)"
        else:
            brx = "([A-Z][A-Z0-9]+-[0-9]+)"
        print("Jira style: subject must include a Jira key")
        print(f"- Project key: {key}")
        print(f"- Regex: {rx}")
        print(f"- Branch extract regex: {brx}")
        print(f"- Branch example: feature/{key}-123-short-desc")
        print(f"- Example: feat(core): {key}-123 add opencode MCP docs")
        return 0

    if style == "github":
        rx = providers.get("github", {}).get("issueRegex", "\\(#[0-9]+\\)$")
        brx = issue_branch.get("githubIssueNumberRegex", "(?:^|/)([0-9]+)(?:-|$)")
        print("GitHub style: subject may reference an issue number")
        print(f"- Regex: {rx}")
        print(f"- Branch extract regex: {brx}")
        print("- Branch example: feature/123-short-desc")
        print("- Example: fix 🐛 (core): handle missing env var (#123)")
        print("- Optional body line: Fixes #123")
        return 0

    if style == "gitlab":
        rx = providers.get("gitlab", {}).get("issueRegex", "\\(#[0-9]+\\)$")
        brx = issue_branch.get("gitlabIssueNumberRegex", "(?:^|/)([0-9]+)(?:-|$)")
        print("GitLab style: subject may reference an issue number")
        print(f"- Regex: {rx}")
        print(f"- Branch extract regex: {brx}")
        print("- Branch example: feature/123-short-desc")
        print("- Example: fix 🐛 (core): handle missing env var (#123)")
        print("- Optional body line: Closes #123")
        return 0

    print("Unknown commit.style (supported: github|gitlab|jira)", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
