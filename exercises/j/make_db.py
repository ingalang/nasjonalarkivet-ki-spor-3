"""Build archive.db with made-up data for task J.

Run: python3 make_db.py
"""

import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("archive.db")

SCHEMA = """
CREATE TABLE creator (id INTEGER PRIMARY KEY, name TEXT NOT NULL, county TEXT);
CREATE TABLE series (id INTEGER PRIMARY KEY, creator_id INTEGER REFERENCES creator(id), code TEXT, title TEXT);
CREATE TABLE unit (id INTEGER PRIMARY KEY, series_id INTEGER REFERENCES series(id), ref TEXT,
                   year_from INTEGER, year_to INTEGER, restricted INTEGER DEFAULT 0, digitised INTEGER DEFAULT 0);
CREATE TABLE request (id INTEGER PRIMARY KEY, unit_id INTEGER REFERENCES unit(id), requested TEXT, status TEXT);
"""

CREATORS = [
    (1, "Fjordvik kommune", "Vestland"),
    (2, "Åsen skolestyre", "Trøndelag"),
    (3, "Nordli lensmannskontor", "Nordland"),
    (4, "Sørby sorenskriveri", None),
]
SERIES = [
    (1, 1, "A", "Møtebøker"),
    (2, 1, "D", "Saksarkiv"),
    (3, 2, "A", "Møtebøker"),
    (4, 3, "F", "Forhørsprotokoller"),
    (5, 4, "G", "Skifteprotokoller"),
]
UNITS = [
    (1, 1, "L0001", 1950, 1959, 0, 1),
    (2, 1, "L0002", 1960, 1969, 0, 0),
    (3, 2, "L0001", 1985, 1990, 1, 0),
    (4, 3, "L0001", 1920, 1935, 0, 1),
    (5, 4, "L0001", 1901, 1910, 0, 0),
    (6, 4, "L0002", 1911, 1925, 0, 0),
    (7, 5, "L0001", 1850, 1870, 0, 1),
    (8, 5, "L0002", 1871, 1890, 0, 0),
]
REQUESTS = [
    (1, 2, "2024-01-10", "open"),
    (2, 2, "2024-02-03", "open"),
    (3, 5, "2024-02-11", "open"),
    (4, 3, "2024-03-01", "rejected"),
    (5, 6, "2024-03-15", "open"),
    (6, 6, "2024-03-16", "cancelled"),
    (7, 8, "2024-04-02", "open"),
    (8, 8, "2024-04-20", "open"),
    (9, 8, "2024-05-05", "open"),
    (10, 1, "2024-05-06", "done"),
]

DB.unlink(missing_ok=True)
with sqlite3.connect(DB) as con:
    con.executescript(SCHEMA)
    con.executemany("INSERT INTO creator VALUES (?, ?, ?)", CREATORS)
    con.executemany("INSERT INTO series VALUES (?, ?, ?, ?)", SERIES)
    con.executemany("INSERT INTO unit VALUES (?, ?, ?, ?, ?, ?, ?)", UNITS)
    con.executemany("INSERT INTO request VALUES (?, ?, ?, ?)", REQUESTS)
print(f"Wrote {DB}")
