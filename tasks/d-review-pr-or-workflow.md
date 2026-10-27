# D. Review a PR or a workflow

**Lane:** [platform, operations and security](../tasks.md#platform-operations-and-security) · [← All tasks](../tasks.md)

## The task

Ask the agent to look for security problems in a PR or in `.github/workflows/`: secrets in plain text, permissions that are too broad, and actions not pinned to a version.

**No PR or workflow at hand?** Use [`exercises/d/`](../exercises/d/): a workflow with deliberate security problems. Check the [answers](../answers/d.md) when you are done.

## Steps

1. Pick a PR, or the workflows in a repo you run.
2. Ask for a review with a fixed list of things to look for, and a severity for each finding.
3. Sort every finding into *real*, *false alarm* and *unsure*.
4. For the *unsure* ones, ask the agent to explain how they could be exploited.

## Prompts to try

```text
Review .github/workflows/ for security problems: secrets in plain text, permissions that are too broad
(missing permissions block, write-all), actions not pinned to a commit SHA, and untrusted input
(PR titles, branch names) used in run steps. For each finding: file, line, severity and why.
```

```text
Review this PR for security problems: gh pr diff <n>. Only report what you can point to in the diff.
```

```text
For finding <n>: how would someone actually exploit this? What would they need access to?
```

## Watch out for

- **Lots of noise.** The agent tends to report everything. A fixed list and "only what you can point to" helps.
- **Missing context.** It can't see repo settings, branch protection or org secrets. Something can look dangerous in the file and be safe in practice, or the other way round.
- **Secrets in the prompt.** Don't paste tokens or Vault values to show it what you mean.

## Done when

You have sorted the findings into *real*, *false alarm* and *unsure*.

## When you are done

In your agent, run `/survey oppgave D` (Codex and Copilot CLI: `survey oppgave D`). Two short questions, under a minute.
