# 1. Teach the agent your repo

**Lane:** everyone · [← All tasks](../tasks.md)

## The task

Start the agent in one of your team's repos (if you don't have one, use this repo). Let it explore, then have it write down what it found in an `AGENTS.md`, so the next session doesn't have to search for it again.

## Steps

1. Ask: "Explain what this repo does, and how I build and test it."
2. Ask it to write a short `AGENTS.md` with what it found: how to build, test and lint, and conventions it sees in the code.
3. Delete anything that is wrong or obvious. Short beats complete.
4. Start a **new** session and ask: "How do I run the tests?"

## Prompts to try

```text
Explain what this repo does, and how I build, test and lint it. Show me the commands you would run.
```

```text
Write a short AGENTS.md with how to build, test and lint, and the conventions you see in the code
(naming, folder layout, commit messages). At most 30 lines. Only include what you could not guess
from the file names.
```

```text
Which of the lines in AGENTS.md would you have figured out anyway, without the file?
```

## Variant: documents and data

Working with documents, spreadsheets or data rather than code? Build, test and lint don't fit. Start the agent in a folder with your material instead (copies or made-up files, see [Data and the secure zone](../tasks.md#data-and-the-secure-zone)), and teach it the folder.

1. Ask: "What is in this folder, and what do you think each file is for?"
2. Correct what it got wrong, then have it write an `AGENTS.md` with what the files are, where they come from, the terms you use, and what it must never change.
3. Start a **new** session and ask it to find something specific, for example "Which file has the budget for 2024?"

```text
Write a short AGENTS.md for this folder: what each kind of file is, where it comes from, words and
abbreviations we use, and which files are originals that must never be changed. At most 30 lines.
```

## Watch out for

- **Guessed commands.** The agent may write `npm test` or `pytest` because it is common, not because it is true here. Check that every command in `AGENTS.md` actually runs.
- **Too long.** A long `AGENTS.md` is read every session and costs attention. Remove what is obvious from the code.
- **Same session.** Asking the question in the session that wrote the file proves nothing. It has to be a new one.

## Done when

The new session answers correctly without searching. For the documents and data variant: it finds the right file at the first attempt.
