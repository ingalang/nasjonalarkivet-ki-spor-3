# Exercise H: a messy extract script

For [task H. Tidy up and test an old script](../../tasks/h-tidy-up-old-script.md).

`extract.py` reads a semicolon-separated export of case files and prints a report for a range of years, grouped by archive part. It works, but it's hard to read: global variables, bare `except`, nested `if`s and string concatenation everywhere. Its output is in Norwegian, like the old script it imitates. `cases.csv` is a small test file with made-up data.

```sh
python3 extract.py cases.csv 1990 1999
python3 extract.py cases.csv 1990 1999 > old-output.txt   # save before the agent changes anything
```

The tidy version must give exactly the same output. The test file has some awkward cases that the old script handles (or gets away with): æøå, a missing date, an empty archive part, an archive part with spaces and lowercase letters, `n`/`ja` instead of `N`/`J`, and a long title.
