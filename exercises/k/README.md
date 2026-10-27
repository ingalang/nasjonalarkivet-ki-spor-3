# Exercise K: files with messy names

For [task K. Automate a recurring task](../../tasks/k-automate-recurring-task.md).

`inbox/` holds small fictional files with names like those you get from scanners, email and colleagues. The routine you want to automate:

> Every month, rename the files in the inbox to `YYYY-MM-DD_description.ext`: the date from the name when there is one, a short description in lower case with `-` instead of spaces, and the file extension in lower case. Files without a date in the name are left alone and listed at the end.

Example: `Møtereferat 12.01.2024.docx` → `2024-01-12_motereferat.docx`.

There are awkward cases on purpose:

- dates in three formats
- æøå
- double spaces
- `(1)` copies
- an uppercase extension
- files without a date

Two files end up with the same new name. Inspect their contents before deciding whether they are duplicates and what should happen next.

Ask for dry run as the default. Use `git status` to see what happened after a real run, and `git restore inbox` and `git clean -fd inbox` to start over.
