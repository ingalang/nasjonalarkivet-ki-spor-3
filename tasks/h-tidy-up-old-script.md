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
