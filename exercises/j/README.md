# Exercise J: an unreadable query

For [task J. Make a query someone else can take over](../../tasks/j-readable-sql-query.md).

`query.sql` finds candidates for digitisation: units that are requested, not yet digitised and not restricted. It is written the way queries often end up: implicit joins, one-letter aliases, `order by 4` and a magic `- 1` in the condition.

`make_db.py` builds a small SQLite database with made-up data to run it against:

```sh
python3 make_db.py
sqlite3 -header archive.db < query.sql
```

Without the `sqlite3` command-line tool you can run the query from Python instead:

```sh
python3 -c "import sqlite3; [print(r) for r in sqlite3.connect('archive.db').execute(open('query.sql').read())]"
```

Ask the agent to explain the query, rewrite it to be readable and check that the new version returns exactly the same rows. Run `make_db.py` again to start over with a fresh database.
