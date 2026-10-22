# Brainstorm: #{{ISSUE}}

Help me find a solution for **#{{ISSUE}}**, and build it once I have approved the plan.

## Context

1. Read `AGENTS.md`. Its rules apply to everything you do.
2. Read the issue: `gh issue view {{ISSUE}} --comments`.
3. You are in your own worktree on the branch `{{BRANCH}}`. Stay on that branch.

## 1. Plan (stop for approval)

- Explore the issue and the code it touches. Where the issue is unclear, ask me questions **one at a time** before you propose anything.
- Write the plan: approach, files that change, what gets tested, and open questions.
- Push the branch (`git push -u origin {{BRANCH}}`) and open a **draft** PR into `main`. The title follows the commit format in `AGENTS.md`, and the description starts with `Closes #{{ISSUE}}`.
- Post the plan as **one** comment on the PR. When the plan changes, update that same comment.
- **Stop here.** Don't write code until I have said the plan is approved.

## 2. Build

- Make the change in small commits, one logical change per commit.
- Run the tests and linting as `AGENTS.md` says, and fix what fails.
- Read through the whole diff (`git diff origin/main...HEAD`) as if you were the reviewer, and fix what you find.
- Push.

## 3. Hand over

Update the PR description (write it to a file and use `gh pr edit --body-file`):

- `Closes #{{ISSUE}}`
- **What changed**, short and concrete
- **How it was verified**: the commands you ran and the result. Say honestly what you couldn't run.
- **Decisions** you made along the way, and why
- **Not done**: things you noticed that are outside the issue

End with the link to the PR.

## Never

Merge, mark the PR ready, close the issue, force push or change `main`. The PR stays a draft until I have looked at it.
