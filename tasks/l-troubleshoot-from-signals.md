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

<details>
<summary>Answer for <code>exercises/l/</code> (open when you are done)</summary>

**Cause:** the nightly reindex (01:00) copied `records-2026` into `records-2026-v2` on `search-2`, but didn't switch the alias or delete the old index (`changes.log`: "Alias switch skipped"). The disk on `search-2` grew from 71 % to past the flood stage watermark of 95 % at 08:31. The search cluster then marked the indices on that node read-only (`search.log`, 08:31:04). The indexer gets `429 cluster_block_exception`, gives up after five retries and puts the batch back on the queue, so the queue grows (`indexer.log`, `metrics.csv`). Reads still work, which is why search finds old documents and isn't slow.

**Red herrings:**

- The frontend deploy at 07:40: gives a short burst of 5xx and a higher p95 for a few minutes, but is over at 07:46, while indexing stops at 08:31.
- The slow token refresh and the certificate that expires in 29 days: warnings, but indexing works after both.
- The slow snapshot at 02:00: finishes without errors.
- `search-1` looks healthy, at 61–65 %.

**Next check** (read only): `GET _cat/allocation?v` and `GET _cat/indices/records-2026*?v&h=index,store.size` for disk per node and index size, and `GET records-2026/_settings/index.blocks*` for the block.

**Not part of the exercise:** the fix (switch the alias, delete the old index, check that the block is lifted), and why the reindex job runs without `--switch-alias`.

</details>

## When you are done

In your agent, run `/survey oppgave L` (Codex and Copilot CLI: `survey oppgave L`). Two short questions, under a minute.
