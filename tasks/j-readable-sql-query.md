# J. Make a query someone else can take over

**Lane:** [script and data automation](../tasks.md#script-and-data-automation) · [← All tasks](../tasks.md)

> Share the query, not the data. See [Data and the secure zone](../tasks.md#data-and-the-secure-zone).

## The task

Give the agent an SQL query that only you understand. Ask it to explain the query, rewrite it to be readable and write a short description of what it returns.

**No query of your own?** Use [`exercises/j/`](../exercises/j/): an unreadable query and a SQLite test database.

**Your own query?** You don't need a team repo. Put the query in a folder, run `git init`, and start the agent there.

## Steps

1. Pick a query you would hate to hand over.
2. Ask the agent to explain it, part by part.
3. Ask for a readable version: names that say something, one CTE per step, comments where the logic is not obvious.
4. Run both versions against the same database and compare the result.
5. Give the new version and the description to a colleague.

## Prompts to try

```text
Explain this query part by part: what each join, filter and subquery does, and what one row in the
result represents. <paste query>
```

```text
Rewrite the query to be readable: CTEs with descriptive names, consistent formatting, a short comment
for each step. It must return exactly the same rows.
```

```text
Write a short description (5–10 lines) of what the query returns, which tables it reads, and when
it should be used.
```

## Watch out for

- **Same rows, really?** Rewrites can change the result through `NULL` handling, `DISTINCT` or join type. Compare row counts and a sample.
- **Dialect.** Tell the agent which database it is (PostgreSQL, Oracle, SQL Server, SQLite). Functions differ.
- **Data in the prompt.** Paste the query and the table structure, not result rows with real data.

## Done when

A colleague understands the query without asking you.
