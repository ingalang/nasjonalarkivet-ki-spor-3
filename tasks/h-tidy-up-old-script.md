# H. Tidy up and test an old script

**Lane:** [script and data automation](../tasks.md#script-and-data-automation) · [← All tasks](../tasks.md)

> Use test data or anonymised data. See [Data and the secure zone](../tasks.md#data-and-the-secure-zone).

## The task

Take a script you use often, for example an extract from Noark 5. Ask the agent to explain it, suggest a tidier version and write a test that runs it on a small test file.

**No script of your own?** Use [`exercises/h/`](../exercises/h/): a messy extract script and a test file.

**Your own script?** You don't need a team repo. Put the script in a folder, run `git init`, commit it as it is, and start the agent there.

## Steps

1. Make sure the old script is committed before the agent changes anything, so you can compare.
2. Make a small test file, with made-up or anonymised data.
3. Run the old script on the test file and save the output.
4. Ask the agent to explain the script, then to tidy it up.
5. Run the new version on the same file and compare the output with the old one.

**Let it run with `/goal`.** The old output must be saved and committed before the agent starts, so it can't regenerate it from its own version. For the exercise files this is already done: `exercises/h/` has `old-1990-1999.txt`, `old-1990.txt` and `old-2000-2005.txt`, made with the original `extract.py`. With your own script, save and commit its output yourself, and use that commit instead of `origin/main` below.

Give the agent a condition it can't talk its way around:

```text
/goal Tidy extract.py and add a test that compares its output with the old-*.txt files. Met only when, after the
last edit, all three runs are shown with diff exiting 0:
python3 extract.py cases.csv 1990 1999 | diff - old-1990-1999.txt
python3 extract.py cases.csv 1990 | diff - old-1990.txt
python3 extract.py cases.csv 2000 2005 | diff - old-2000-2005.txt
and git add -A && git diff --cached --stat origin/main lists only extract.py and the new test file (the
old-*.txt files stay as committed). Stop after 15 turns.
```

`git add -A && git diff --cached --stat origin/main` compares everything with `main` on GitHub, new files included, so it works whether or not the agent has committed. A plain `git diff --stat` would miss files the agent created but never added. Each range catches something different: the open-ended one the missing end year (the report header ends with a dash), and 2000–2005 the undated row that is still counted as skipped outside its range. See [Keep the agent going with `/goal`](../resources.md#keep-the-agent-going-with-goal).

To get the result into a draft pull request instead, add this to the end of the `/goal` text. The agent pushes a branch, so you need push access. For `exercises/h/` in this course repo, fork it first (`gh repo fork --remote`), so the pull request opens in your fork:

```text
Work in a new branch in a separate worktree. When the goal is met, commit, push the branch and create a draft
pull request.
```

Alternative to inline instructions:
```text
Follow instructions in instructions.md.
```

## Prompts to try

```text
Explain what this script does, step by step. Which inputs does it expect, and what does it write?
```

```text
Make a small test file with made-up data that exercises every branch in the script.
```

```text
Suggest a tidier version that gives exactly the same output. Then write a test that runs both the old
and the new version on the test file and compares the output.
```

## Watch out for

- **"Improvements" that change the result.** Tidier sorting, other date formats or different whitespace give a different output. The output must be identical.
- **A test file that is too nice.** Include empty fields, special characters (æøå) and a missing value.
- **Lost behaviour.** Odd lines in old scripts are often there for a reason. Ask before they are removed.

## Done when

The new version gives the same result as the old one on the test file.

## When you are done

In your agent, run `/survey oppgave H` (Codex and Copilot CLI: `survey oppgave H`). Two short questions, under a minute.
