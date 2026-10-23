# Exercise I: an XML extract and its schema

For [task I. Validate an XML extract](../../tasks/i-validate-xml-extract.md).

- `extract.xsd` is a simplified schema, loosely inspired by Noark 5. It has case files, records and documents.
- `extract.xml` is a made-up extract that is valid against the schema.

Python's standard library can't validate against an XSD. Use one of these to check that the schema and the extract work on your machine before you start. Neither needs anything installed, and both print each error with its line number.

**macOS and Linux:** `xmllint` ships with macOS and most Linux systems.

```sh
xmllint --noout --schema extract.xsd extract.xml
```

**Windows:** PowerShell can validate with .NET, which is already on the machine. Run this in PowerShell from this folder:

```powershell
$s = New-Object System.Xml.XmlReaderSettings
$s.ValidationType = "Schema"
[void]$s.Schemas.Add([System.Xml.Schema.XmlSchema]::Read([System.Xml.XmlReader]::Create((Resolve-Path extract.xsd).Path), $null))
$s.add_ValidationEventHandler({ Write-Host "Line $($_.Exception.LineNumber): $($_.Message)" })
$r = [System.Xml.XmlReader]::Create((Resolve-Path extract.xml).Path, $s); while ($r.Read()) {}; $r.Close()
```

Swap `extract.xml` for your own copy to check it. Tell the agent which of the two you use, so the script builds on a tool that is already there.

Copy `extract.xml` and put in errors on purpose, for example:

- a case number such as `98/300`
- a date such as `2024-13-01`
- a missing `<title>`
- a format that isn't in the list
- a checksum with uppercase letters

Put each error in its own copy of `extract.xml`, or in a different record. Once a record has an element missing or out of order, the validator stops checking the rest of that record, so a second error in it isn't reported.
