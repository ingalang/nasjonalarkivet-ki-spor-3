# Exercise C, variant: trace one call across services

For the variant [trace one call across services](../../../tasks/c-explain-something.md#variant-trace-one-call-across-services) in task C.

Three fictional services, cloned side by side as if each folder were its own repo. The READMEs are out of date and the people who wrote the code have left. The code is the source of truth. You can't run it here.

| Folder | What it is |
|---|---|
| `gateway/` | The entry point. Routes requests and checks tokens |
| `identity/` | Issues and verifies tokens |
| `records-api/` | Serves archive records |

Start the agent in this folder and give it the prompt from the task, filled in:

```text
Follow one call from gateway to records-api: a client fetches a record with
GET /api/records/<id>. Where is the token or identity checked, by whom, and what happens
if the check fails? Write the result to docs/get-record.md with a description, a Mermaid
sequenceDiagram, a repo/file:line reference for every step, and a list of open questions.
Mark anything you couldn't confirm in the code.
```

The answer is on the task page, so don't let the agent read that page.
