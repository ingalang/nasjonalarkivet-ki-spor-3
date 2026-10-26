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

## Keep the agent going with `/goal`

`/goal <condition>` keeps the agent working turn after turn until the condition holds, instead of stopping to ask you. The condition is what makes it safe: without one, the agent decides for itself when it is done.

| | Who decides the goal is met | How to set a limit |
|---|---|---|
| [Claude Code](https://code.claude.com/docs/en/goal) | A separate small model, after every turn. It only reads the conversation and doesn't run anything itself. | Put it in the condition, for example `or stop after 20 turns` |
| Codex | The agent itself, after checking its own work. `/goal pause`, `resume` and `clear` control it. | An optional token budget. Check `codex --help` for your version; older versions need `goals = true` under `[features]` in `~/.codex/config.toml` |
| [Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/autopilot) | No `/goal`. Autopilot (Shift+Tab, `/autopilot`, or `--autopilot` with `-p`) runs until the agent thinks it is done. | `--max-autopilot-continues=<n>` |

A good condition has four parts:

1. **One end state you can measure**: tests pass, a command exits 0, a file exists.
2. **The check that proves it**, written out so it shows in the conversation: "`python3 -m py_compile survey/*.py` exits 0".
3. **What must not change on the way**: "no existing test file is modified", "`main` is untouched".
4. **A limit**: "stop after 20 turns". In Claude Code the evaluator judges this from the conversation, so it is a soft limit: keep an eye on it, or stop the session yourself.

Then make the important limits real, not just written down. The agent, or the model judging it, only sees what is printed. A protected `main`, required checks and a hook that blocks edits to the tests hold even when the condition doesn't.

When the goal isn't met within the limit, the condition or the task is usually wrong. Rewrite it and start a new session rather than raising the limit.

`scripts/start-issue.sh --autopilot` prints a ready-made `/goal` for the issue.
