# B. A small change, plan first

**Lane:** [product development](../tasks.md#product-development) · [← All tasks](../tasks.md)

## The task

Pick a small item from the backlog. Ask the agent for a plan *before* it changes anything. Correct the plan, then let it do the work.

## Steps

1. Pick something small: a bug, a text change, a small validation rule. Half a day of work at most.
2. Give the agent the issue text and ask for a plan, without code.
3. Correct the plan: wrong file, missing case, too much change.
4. Let it make the change, and run tests and linting.
5. Read the whole diff. Ask about every line you don't understand.

If the backlog is on GitHub, you can use `scripts/start-issue.sh` from this repo as a model, see [resources](../resources.md).

## Prompts to try

```text
Don't write code yet. Here is the issue: <paste>. Which files need to change, and why?
What could go wrong?
```

```text
The plan is approved, except <correction>. Make the change, then run the tests and the linter, and fix
what fails.
```

```text
Go through the diff with me, file by file. Why is each change needed?
```

## Watch out for

- **Scope creep.** The agent likes to tidy up nearby code. Ask it to keep the diff to what the task needs.
- **Plan and code drift apart.** Compare the diff with the plan you approved.
- **"Tests pass" without running them.** Ask to see the output.

## Done when

Tests and linting are green, and you understand every line of the diff.
