# I. Validate an XML extract

**Lane:** [script and data automation](../tasks.md#script-and-data-automation) · [← All tasks](../tasks.md)

> Use test data or anonymised data. See [Data and the secure zone](../tasks.md#data-and-the-secure-zone).

## The task

Ask the agent for a script that checks an XML file against its schema (XSD) and writes the errors as a readable summary.

**No extract of your own?** Use [`exercises/i/`](../exercises/i/): a simplified schema and a valid extract.

**Your own schema?** You don't need a team repo. Put the schema and a test file in a folder, run `git init`, and start the agent there.

## Steps

1. Get the XSD and a small XML file that should be valid.
2. Ask for a script that validates the file and prints the errors with line numbers in plain language.
3. Run it on the valid file. It should report no errors.
4. Put in an error on purpose (remove a required element, a wrong date format) and run it again.

## Prompts to try

```text
Write a script that validates <file>.xml against <schema>.xsd. Print each error with line number and
a short explanation in plain language. Exit with a non-zero code if there are errors.
Use only tools that are already installed on my machine (say which ones you use).
```

```text
Make three copies of the test file, each with a different deliberate error, and show what the script
reports for each.
```

```text
Group the errors by type and show the count, so a file with a thousand errors is still readable.
```

## Watch out for

- **Well-formed is not valid.** A script that only parses the XML doesn't check the schema. Make sure the XSD is actually used.
- **Schemas that import other schemas.** The script must find the imported XSD files, usually relative to the main schema.
- **Large files.** Real extracts can be large. Ask how the script handles a file of several GB.

## Done when

The script finds an error you put in on purpose.
