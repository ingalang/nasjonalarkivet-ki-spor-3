# Resources – track 3

## Four points to take with you

1. **Agents can carry out connected tasks.** Not just one answer, but plan, do, check and report back.
2. **Speed doesn't replace clarifying.** The agent works faster than you, but someone still has to decide what is wanted, and settle what is unclear.
3. **Your expertise is what judges the result.** The agent can sound sure and be wrong. You are the one who knows what is right.
4. **Agents can help you into unfamiliar code and documentation.** Use them to find your way around, and check what they say against the source.

## From issue to PR with an agent

`scripts/start-issue.sh` creates a branch and a worktree for a GitHub issue, and starts the agent with ready-made instructions:

```sh
bash scripts/start-issue.sh 12              # brainstorm: the agent plans, waits for approval, then builds
bash scripts/start-issue.sh 12 --autopilot  # autopilot: from issue to draft PR without asking
bash scripts/start-issue.sh 12 --codex      # Codex (the default)
bash scripts/start-issue.sh 12 --claude     # Claude Code instead of Codex
```

In Claude Code or Codex you can instead type `/start-issue 12` or `/start-issue 12 autopilot` (Codex: `$start-issue 12`). That creates the worktree and gives you the command to start the agent in a new window.

The agent follows `AGENTS.md`, opens a draft PR with the plan as a comment, and writes the PR description at the end. It never merges. The templates are in `scripts/templates/`. Requires `gh` (logged in) and bash. On Windows, bash comes with Git for Windows; run the script from Git Bash (not PowerShell or WSL). Clean up afterwards with `git worktree remove .worktrees/<name>`.

The same workflow works when the deliverable is analysis or documentation, such as an explanation of a service call or a troubleshooting report. The result is a Markdown file in the PR, with references to the sources it builds on.
