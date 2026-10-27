# Incident 4711: new documents missing from search

This is a sample report for participants who cannot run an agent or terminal. Review it against the other files in this folder. It contains one deliberate mistake.

## Symptom

Documents published after about 08:30 are missing from search, while older documents remain available and search is not slow (`ticket.md`, line 6).

## Timeline

| Time (UTC) | Event | Source |
|---|---|---|
| 01:00 | The nightly job creates `records-2026-v2` on `search-2` and starts copying `records-2026` into it. | `changes.log`, line 5; `logs/search.log`, lines 3–5 |
| 06:02 | The reindex completes without failures, but the alias switch is skipped. | `changes.log`, line 6; `logs/search.log`, line 9 |
| 06:13 | `search-2` passes the 85% low disk watermark. | `logs/search.log`, line 10 |
| 07:40–07:46 | Frontend 4.12.0 is deployed. | `changes.log`, lines 7–8 |
| 07:40–07:50 | 5xx rises to 14 per minute for two samples, then returns to zero. | `metrics.csv`, lines 94–96 |
| 08:30 | The last successful batch of 34 documents is indexed. | `logs/indexer.log`, line 10 |
| 08:31 | `search-2` passes the 95% flood-stage watermark. Both record indices are made read-only, and indexing starts failing with 429 responses. | `logs/search.log`, lines 14–15; `logs/indexer.log`, lines 11–16 |
| 08:30–09:05 | Indexing falls from 35 to 0 documents per minute and the queue grows from 4 to 1024. | `metrics.csv`, lines 104–111 |

## Hypotheses

### 1. The frontend deployment caused the incident

- **Evidence for:** it changed the search result page shortly before the symptom was reported, and the 5xx rate rose during the rollout.
- **Evidence against:** the 5xx rate returned to zero at 07:50, and the indexer still completed successful batches through 08:30.
- **What would rule it out:** compare a missing document through the search API and the frontend, and check whether both omit it.

### 2. Disk pressure blocked writes to the active index

- **Evidence for:** `search-2` crosses the flood stage at 08:31, both record indices become read-only, and the indexer immediately receives `cluster_block_exception` responses.
- **Evidence against:** reads remain healthy, so this does not explain a general search outage.
- **What would rule it out:** show that `records-2026` is not blocked or is allocated to a node below the watermark.

### 3. Authentication or TLS trouble stopped the indexer

- **Evidence for:** the indexer records a slow token refresh and a certificate-expiry warning.
- **Evidence against:** successful indexing continues after both warnings, and neither is an authentication failure.
- **What would rule it out:** confirm that the indexer has successful authenticated requests after 08:12.

## Conclusion and next check

The strongest hypothesis is the frontend deployment: its new result page most likely stopped showing newly published documents.

Check the competing disk-pressure evidence without changing the cluster:

```http
GET _cat/allocation?v
GET _cat/indices/records-2026*?v&h=index,store.size
GET records-2026/_settings/index.blocks*
```
