# Exercise A: a module with no tests

For [task A. Write tests for something that lacks them](../../tasks/a-write-tests.md).

`archive_ref.py` has three small functions:

- `parse_ref` splits an archive reference such as `RA/EA-4001/F/Fa/L0012` into its parts.
- `whole_years` counts the whole years between two dates.
- `is_open` says whether a record is past its access period (60 years by default).

There are no tests. Try it:

```sh
python3 archive_ref.py
```

Ask the agent to write tests with `unittest` from the standard library (no pytest needed), both for normal use and for error cases. Think about leap days, a reference with lowercase letters or extra spaces, and dates on the exact boundary.
