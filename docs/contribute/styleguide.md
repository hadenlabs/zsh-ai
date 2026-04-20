# Styleguide

## Git Commit Messages

Your commit messages should serve these 3 important purposes:

- To speed up the reviewing process.
- To provide the least amount of necessary documentation
- To help the future maintainers.

Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0) to make `git log`{.interpreted-text role="command"} easier to follow. We use commitlint to enforce the format (See [commitlint](https://github.com/conventional-changelog/commitlint)).

### Format

The commit message format is defined in [`jasper.toml`](../../jasper.toml):

```text
<type> <emoji> (<scope>): <subject>
```

### Types

Commit types (with emojis and descriptions) and allowed scopes are defined in [`.goji.json`](../../.goji.json).

### Examples

See [`.goji.json`](../../.goji.json) for examples of each commit type.

**Keep it short and simple!**

## Branches

See [Github Flow](./github-flow.md).

## Documentation

Documentation is a part of the zsh-ai code base. You can find the documentation files in the `doc/` subdirectory of the [main repository](https://github.com/hadenlabs/zsh-ai). This means that the contribution process is the same for both the source code and documentation.

## Testing

See [Testing](./testing.md).