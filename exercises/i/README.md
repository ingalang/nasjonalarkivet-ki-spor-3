# Exercise I: an XML extract and its schema

For [task I. Validate an XML extract](../../tasks/i-validate-xml-extract.md).

- `extract.xsd` is a simplified schema, loosely inspired by Noark 5. It has case files, records and documents.
- `extract.xml` is a made-up extract that is valid against the schema.

Python's standard library can't validate against an XSD. `xmllint` can, and it ships with macOS and most Linux systems:

```sh
xmllint --noout --schema extract.xsd extract.xml
```

On Windows, ask the agent what it suggests.

Copy `extract.xml` and put in errors on purpose, for example:

- a case number such as `98/300`
- a date such as `2024-13-01`
- a missing `<title>`
- a format that isn't in the list
- a checksum with uppercase letters
