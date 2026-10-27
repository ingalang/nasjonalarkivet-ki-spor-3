# Answer for exercise L

For [task L. Troubleshoot from logs and metrics](../tasks/l-troubleshoot-from-signals.md) and [`exercises/l/`](../exercises/l/).

Read this after investigating the incident yourself.

**Cause:** the nightly reindex (01:00) copied `records-2026` into `records-2026-v2` on `search-2`, but didn't switch the alias or delete the old index (`changes.log`: "Alias switch skipped"). The disk on `search-2` grew from 71% to past the flood-stage watermark of 95% at 08:31. The search cluster then marked the indices on that node read-only (`logs/search.log`, 08:31:04). The indexer gets `429 cluster_block_exception`, gives up after five retries and puts the batch back on the queue, so the queue grows (`logs/indexer.log`, `metrics.csv`). Reads still work, which is why search finds old documents and isn't slow.

**Red herrings:**

- The frontend deploy at 07:40 gives a short burst of 5xx and a higher p95 for a few minutes, but is over at 07:46, while indexing stops at 08:31.
- The slow token refresh and the certificate that expires in 29 days are warnings, but indexing works after both.
- The slow snapshot at 02:00 finishes without errors.
- `search-1` looks healthy, at 61–66%.

**Next check** (read only): `GET _cat/allocation?v` and `GET _cat/indices/records-2026*?v&h=index,store.size` for disk per node and index size, and `GET records-2026/_settings/index.blocks*` for the block.

**Not part of the exercise:** the fix (switch the alias, delete the old index, check that the block is lifted), and why the reindex job runs without `--switch-alias`.
