# Exercise L: new documents missing from search

For [task L. Troubleshoot from logs and metrics](../../tasks/l-troubleshoot-from-signals.md).

A made-up incident from a made-up morning. The symptom is known, the cause isn't. Everything here is fictional, so it is safe to use with a cloud-based agent.

| File | What it is |
|---|---|
| `ticket.md` | The symptom, as the service desk got it |
| `changes.log` | Deploys, config changes and scheduled jobs from the day before and the morning itself |
| `metrics.csv` | Disk, indexing queue, search traffic and errors every 5 minutes, 00:00–10:00 |
| `logs/indexer.log` | The service that puts new documents into the search index |
| `logs/search.log` | The search cluster (two nodes, `search-1` and `search-2`) |

All times are UTC. Not everything that looks odd has anything to do with the problem.

Start the agent in this folder. The answer is on the task page, so don't let the agent read that page.
