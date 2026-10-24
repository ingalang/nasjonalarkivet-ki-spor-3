# Nasjonalarkivet – KI spor 3

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
- **Codex or Claude Code**, installed and logged in. Both need a paid plan, and neither needs Node.js.
  - [Codex CLI](https://github.com/openai/codex) needs ChatGPT Plus, Pro, Business, Edu or Enterprise. Install it, then run `codex` to log in:
    - macOS/Linux: `curl -fsSL https://chatgpt.com/codex/install.sh | sh`
    - Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"`
  - [Claude Code](https://code.claude.com/docs/en/setup) needs Claude Pro, Max, Team or Enterprise. Install it, then run `claude` to log in:
    - macOS/Linux: `curl -fsSL https://claude.ai/install.sh | bash`
    - Windows (PowerShell): `irm https://claude.ai/install.ps1 | iex`
  - Open a new terminal after installing, and check with `codex --version` or `claude --version`.
  - If the installer is blocked, or you already have Node.js 22 or later, you can use npm instead: `npm install -g @openai/codex` or `npm install -g @anthropic-ai/claude-code`.

## Getting started

1. Log in to GitHub: `gh auth login`, and check with `gh auth status`.
2. Clone the repo: `gh repo clone olemp/nasjonalarkivet-ki-spor-3`
   On Windows, Git checks out `.agents/skills` as a text file unless `core.symlinks` is on. Write
   `codex "survey start"` as above (it works through `AGENTS.md`); `$survey` and `$start-issue` do not.
3. Pick a nickname for the day. In this folder, run `claude "/survey start"` or `codex "survey start"`.
   Choose something that is not your name, and use the same nickname for the rest of the day.
4. Read through the [resources](resources.md)
5. Get going on the [tasks](tasks.md)

## Feedback

After each task, run the line at the bottom of the task page, for example `/survey oppgave H`
(Codex: `survey oppgave H`). It takes under a minute.

Give us feedback at the end of the day, under your nickname. Run one of these in this folder:

**Codex**

```bash
codex "survey slutt"
```

**Claude Code**

```bash
claude "/survey slutt"
```

**ChatGPT or no terminal:** Paste the contents of [`.claude/skills/survey/SKILL.md`](.claude/skills/survey/SKILL.md) into a new conversation and write `/survey slutt`. You will get a link to click instead of a command.

Questions or suggestions? Open an issue or contact the course lead.
