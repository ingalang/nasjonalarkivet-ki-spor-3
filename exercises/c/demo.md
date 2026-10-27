Follow one call from gateway to records-api: a client fetches an archive record with
GET /api/records/<id>. The three folders here are separate repos, cloned side by side. Their
READMEs are out of date, so treat the code as the source of truth and point out where a README
is wrong. Only read files in this folder.

Where is the token or identity checked, by whom, and what happens if the check fails? Cover
every way the call can fail, with the status code the client gets and which service returns it.

Write the result to docs/get-record.md with:
- a plain-language description of the call, for someone new to the team
- a Mermaid sequenceDiagram with gateway, identity and records-api as participants
- a repo/file:line reference for every step
- a list of open questions: what you couldn't find or confirm, such as config or secrets
  that aren't in these repos

Mark anything you couldn't confirm in the code. Don't describe what such a service usually does.

Work in a new branch in a separate worktree, created from the current commit. When the goal is met,
commit, push the branch and create a draft pull request.
