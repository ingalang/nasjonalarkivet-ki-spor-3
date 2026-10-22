# The National Archives of Norway – AI learning, track 3

This repo holds resources and tasks for track 3 of the National Archives' AI learning programme.

📍 Oslo, 27 October 2026

## Contents

- **[Resources](resources.md)** – reading, links and tools used in the track
- **[Tasks](tasks.md)** – hands-on exercises to work on during the day

## Prerequisites

- **A GitHub user** with access to this repo. The repo is private: send your GitHub username to the course lead to be added.
- **Git.** On Windows, install [Git for Windows](https://git-scm.com/download/win), which includes Git Bash.
- **The GitHub CLI (`gh`).** The agent uses it to read issues and open PRs.
  - Windows: `winget install --id GitHub.cli`
  - macOS: `brew install gh`
  - Other: see [cli.github.com](https://cli.github.com)
- **Codex or Claude Code**, installed and logged in:
  - [Codex CLI](https://github.com/openai/codex): `npm install -g @openai/codex`, then `codex` to log in
  - [Claude Code](https://docs.claude.com/en/docs/claude-code/setup): `npm install -g @anthropic-ai/claude-code`, then `claude` to log in

## Getting started

1. Log in to GitHub: `gh auth login`, and check with `gh auth status`.
2. Clone the repo: `gh repo clone olemp/nasjonalarkivet-ki-spor-3`
3. Read through the [resources](resources.md)
4. Get going on the [tasks](tasks.md)

## Feedback

Give us anonymous feedback after the course:

- **Claude Code / Codex:** Start the agent in this folder and type `/survey` (Codex: `survey`).
- **ChatGPT:** Paste the contents of [`.claude/skills/survey/SKILL.md`](.claude/skills/survey/SKILL.md) into a new conversation.

Questions or suggestions? Open an issue or contact the course lead.
