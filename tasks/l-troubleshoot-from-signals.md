# L. Troubleshoot from logs and metrics

**Lane:** [platform, operations and security](../tasks.md#platform-operations-and-security) · [← All tasks](../tasks.md)

> Logs can contain personal data, tokens and connection strings. Use anonymised logs or local AI. See [Data and the secure zone](../tasks.md#data-and-the-secure-zone).

## The task

Start from a known symptom whose cause is unknown. Give the agent the signals you have (logs, metrics, recent changes) and have it work out what happened. A past incident where you already know the answer works well: then you can judge the agent's reasoning, not just its conclusion.

**Nothing at hand?** Use [`exercises/l/`](../exercises/l/): a made-up incident where new documents are missing from search.

The deliverable is a Markdown file with:

- a **timeline** of what happened, with the source for each line
- **hypotheses**, each with evidence for and evidence against
- the **next check**: the one command or query that would confirm or rule out the strongest hypothesis

## Steps

1. Write down the symptom in one or two sentences, and when it started.
2. Collect the signals in one folder: log extracts, metrics as CSV, the list of changes. Remove secrets and personal data first.
3. Ask for the timeline first, then the hypotheses. Don't ask for the answer.
4. For every hypothesis, check one piece of evidence yourself in the files.
5. Ask what the agent would need to see to be sure.

## Test matrix

Use this matrix for `exercises/l/`. For the last check, choose any two timeline entries rather than trusting the references without checking them.

| # | What you check | Expected |
|---|---|---|
| 1 | Does the timeline start with the nightly reindex? | 01:00, in `changes.log` and `logs/search.log` (01:00:03–01:00:05) |
| 2 | Does it include the skipped alias switch? | 06:02, in `changes.log`: `Alias switch skipped: --switch-alias not set` |
| 3 | Does it include the flood-stage block? | 08:31:04, in `logs/search.log`: `read_only_allow_delete` on `records-2026` and `records-2026-v2` |
| 4 | Does the indexing stop show in the metrics? | At 08:35, `index_queue_depth` changes from 4 to 124 and `indexed_per_min` from 35 to 0. At 09:05, the queue is 1024 |
| 5 | Is the frontend deploy ruled out with evidence? | 5xx is 14/min only at 07:40 and 07:45, and is back to 0 at 07:50. Indexing continues until 08:31 |
| 6 | Is `search-1` left out of the cause? | Its disk usage stays at 61–66% |
| 7 | Is the next check read-only? | `GET` only. No `PUT`, `DELETE`, settings change or alias switch |
| 8 | Check two timeline lines yourself | Both are present in the file the agent named |

## Prompts to try

```text
Symptom: <what users see, since when>. The files in this folder are logs, metrics and changes from
that period. Make a timeline of everything relevant, with file and line for each event. Don't
conclude anything yet.
```

```text
Give me three to five hypotheses for the cause. For each one: evidence for, evidence against (with
file and line), and what would rule it out.
```

```text
What is the single next check you would run against the real system to confirm the strongest
hypothesis? It must only read, never change anything.
```

```text
Write the timeline, the hypotheses and the next check to incident.md.
```

## Watch out for

- **Correlation that looks like cause.** Something that changed at the same time isn't necessarily the reason. Ask for evidence against each hypothesis, not just evidence for.
- **The first plausible story.** The agent tends to stop at the first explanation that fits. Ask what else could explain the same signals.
- **Invented log lines.** Check that the lines it quotes actually exist in the files.
- **Fixes that write.** The next step is a check, not a fix. A suggestion like "just remove the block" belongs in a later step, after you have confirmed the cause.

Ongoing monitoring and early warning are interesting too, but take more than one session to try properly.

## Done when

You have a timeline and hypotheses where you have checked at least one piece of evidence yourself, and you can say whether the agent found the cause.

When you are ready, compare your result with the [answer for exercise L](../answers/l.md).

## When you are done

In your agent, run `/survey oppgave L` (Codex and Copilot CLI: `survey oppgave L`). Two short questions, under a minute.
