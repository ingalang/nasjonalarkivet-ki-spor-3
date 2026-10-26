When the user types "survey" or "/survey", follow the instructions in `.claude/skills/survey/SKILL.md`.

When the user types "start-issue" or "/start-issue", follow the instructions in `.claude/skills/start-issue/SKILL.md`.

The same rules are in `CLAUDE.md` for Claude Code. Change both files together.

## Conventions

- Language: English in documentation, PRs and commit messages. Code and comments follow the file you are in.
- Commit messages and PR titles: `<type>(<scope>): <what>`, where type is `feat`, `fix`, `docs` or `chore`. Example: `feat(survey): show the number of answers per question`.
- Branches: `<type>/<issue>-<short-description>`. A PR closes its issue with `Closes #<n>` in the description.
- Python uses the standard library only. Don't add dependencies.
- There is no test suite. Run any script you changed once.
- Workflow for issues: `scripts/start-issue.sh <n>` (see `resources.md`).
