"""Talks to the survey-db Postgres container through psql (podman exec).

No Python driver: AGENTS.md allows the standard library only. Values are passed
as psql variables (-v) and quoted by psql with :'name', so they never become SQL.
"""
import json
import os
import subprocess

CONTAINER = os.environ.get("SURVEY_DB_CONTAINER", "survey-db")
COLUMNS = ["id", "schema", "q1", "q2", "q3", "q4", "q5", "q6"]  # received_at is set by Postgres

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS answers (
  id text NOT NULL,
  schema text NOT NULL,
  q1 text, q2 text, q3 text, q4 text, q5 text, q6 text,
  received_at timestamptz NOT NULL DEFAULT now()
);
"""


def psql(sql, **params):
    # The SQL goes in on stdin: psql only expands :'var' in script input, not in -c.
    cmd = ["podman", "exec", "-i", CONTAINER, "psql", "-U", "postgres", "-X", "-q", "-A", "-t", "-v", "ON_ERROR_STOP=1"]
    for k, v in params.items():
        cmd += ["-v", f"{k}={v}"]
    return subprocess.run(cmd, input=sql, capture_output=True, text=True, check=True).stdout


def init():
    psql(SCHEMA_SQL)


def insert(row):
    """row: dict with the keys in COLUMNS, all strings."""
    values = ", ".join(f":'{c}'" for c in COLUMNS)
    psql(f"INSERT INTO answers ({', '.join(COLUMNS)}) VALUES ({values});", **row)


def rows():
    """All answers, oldest first, in the shape dashboard.html expects."""
    out = psql("""
SELECT coalesce(json_agg(json_build_object(
  'id', id, 'Q1', q1, 'Q2', q2, 'Q3', q3, 'Q4', q4, 'Q5', q5, 'Q6', q6,
  'mottatt', to_char(received_at AT TIME ZONE 'UTC', 'YYYY-MM-DD"T"HH24:MI:SS"+00:00"')
) ORDER BY received_at), '[]') FROM answers;
""")
    return json.loads(out)
