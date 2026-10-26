---
name: start-issue
description: Starts work on a GitHub issue in its own branch and worktree, with the brainstorm or autopilot template. Use when the user types "start-issue", "/start-issue <n>" or asks to start on an issue.
---

Create a worktree for a GitHub issue with `scripts/start-issue.sh`.

1. Find the issue number and the mode in what the user wrote, for example `/start-issue 12 autopilot`. The mode is `brainstorm` (default) or `autopilot`. If the issue number is missing, ask for it and the mode in the same question.
2. Run from the repo root, with `--autopilot` only in autopilot mode, and `--codex` if you are Codex or `--claude` if you are Claude Code:

   ```sh
   bash scripts/start-issue.sh <n> [--autopilot] [--codex|--claude] --no-start
   ```

   On Windows in PowerShell, `bash` may be missing or point to WSL. Use Git Bash directly instead:
   `& "$env:ProgramFiles\Git\bin\bash.exe" scripts/start-issue.sh <n> ... --no-start`

3. If the command fails, show the error and stop. Common causes: `gh` is not logged in (`gh auth login`), or the issue doesn't exist.
4. Otherwise, show the user the worktree folder and branch, and the command the script printed for starting the agent in a new terminal window. In autopilot mode, also show the `/goal` line the script printed, word for word, to paste once the new session is open. Briefly explain what happens in the mode:
   - **brainstorm**: the agent makes a plan, opens a draft PR with the plan and waits for approval before writing code.
   - **autopilot**: the agent goes from issue to finished draft PR without asking.

Don't start on the issue itself in this session. The work happens in the worktree.
