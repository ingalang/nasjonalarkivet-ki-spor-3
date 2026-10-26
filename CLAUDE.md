Skills live in `.claude/skills/`. Run them with `/survey` and `/start-issue`.

The same rules are in `AGENTS.md` for Codex and Copilot. Change both files together.

## Conventions

- Language: English in documentation, PRs and commit messages. Code and comments follow the file you are in.
- Commit messages and PR titles: `<type>(<scope>): <what>`, where type is `feat`, `fix`, `docs` or `chore`. Example: `feat(survey): show the number of answers per question`.
- Branches: `<type>/<issue>-<short-description>`. A PR closes its issue with `Closes #<n>` in the description.
- Python uses the standard library only. Don't add dependencies.
- There is no test suite. Run any script you changed once.
- Workflow for issues: `scripts/start-issue.sh <n>` (see `resources.md`).
