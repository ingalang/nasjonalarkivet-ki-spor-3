# K. Automate a recurring task

**Lane:** [script and data automation](../tasks.md#script-and-data-automation) · [← All tasks](../tasks.md)

> Use test data or anonymised data. See [Data and the secure zone](../tasks.md#data-and-the-secure-zone).

## The task

Pick something you do by hand every week or month: renaming files, merging spreadsheets, checking that files are complete. Ask the agent for a script that does it, with a dry-run mode that only shows what it would do.

**Nothing to hand?** Use [`exercises/k/`](../exercises/k/): a folder of files with messy names, and the renaming routine to automate.

**Your own task?** You don't need a team repo. Make a folder, run `git init`, and start the agent there.

## Steps

1. Describe the task as you do it today, step by step.
2. Make a test folder with copies or made-up files, never the real ones.
3. Ask for a script with a dry-run mode, and make dry run the default.
4. Run the dry run and check every line it prints.
5. Run it for real on the test folder, and check the result.

## Prompts to try

```text
Every month I <task, step by step>. Write a script that does this. Dry run must be the default:
it only prints what it would do. It only changes files when I pass --apply.
```

```text
Make a test folder with made-up files that cover the normal case and the awkward ones
(names with spaces and æøå, a file that already exists, an empty file).
```

```text
What happens if the script stops halfway? Can I run it again safely?
```

## Watch out for

- **Dry run that isn't dry.** Check that nothing is changed without `--apply`, for example with `git status` before and after.
- **Overwriting.** Renaming or moving onto a file that already exists can lose data. Ask the script to stop instead.
- **Real files on the first run.** Use the test folder until the dry run looks right.

## Done when

The dry run shows the right result before you run it for real.
