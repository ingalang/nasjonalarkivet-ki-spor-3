# C. Explain something you didn't write

**Lane:** [product development](../tasks.md#product-development) · [← All tasks](../tasks.md)

## The task

Point the agent at a file, a workflow or a configuration you find hard to follow, for example an Argo workflow, an index template in `da-indexer` or an Alembic migration. Ask for an explanation and a diagram (Mermaid) of the flow.

**Nothing at hand?** Use [`exercises/c/`](../exercises/c/): a fictional Argo workflow.

## Variant: trace one call across services

For a large codebase spread over several repos, where the docs are out of date and the people who wrote it have left. Pick **one** call between two services, for example how a request is authorised from the gateway to the service that answers it, and follow it end to end.

- **Several repos?** Clone them side by side in one folder and start the agent in that folder.
- **Jira and Confluence** are useful extra context, but you don't need them to start. The code is the source of truth.
- **The deliverable** is a Markdown file with:
  - a plain-language description of the call
  - a Mermaid sequence diagram
  - a code reference (`repo/file:line`) for every step
  - open questions: what the agent couldn't find or confirm

```text
Follow one call from <service A> to <service B>: <what the call does>. Where is the token or
identity checked, by whom, and what happens if the check fails? Write the result to
docs/<name>.md with a description, a Mermaid sequenceDiagram, a repo/file:line reference for every
step, and a list of open questions. Mark anything you couldn't confirm in the code.
```

**Nothing at hand?** Use [`exercises/c/services/`](../exercises/c/services/): three fictional services side by side, with out-of-date READMEs.

## Steps

1. Pick something you have avoided touching because you don't fully understand it.
2. Ask for an explanation in plain language, then a Mermaid diagram of the flow.
3. Check the explanation against the code. Pick two claims and find the lines that prove them.
4. Ask follow-up questions about what still isn't clear.

## Prompts to try

```text
Explain <file> as if I'm new to the team. What does it do, what does it depend on, and what depends on it?
```

```text
Draw the flow as a Mermaid diagram (flowchart). Only include steps you can point to in the code.
```

```text
For each step in the diagram: which file and line does it come from?
```

```text
What in this file would surprise someone who changes it for the first time?
```

## Watch out for

- **Confident guessing.** The agent can describe what such a file *usually* does, not what this one does. Ask for line references.
- **Missing context.** A workflow may depend on config or secrets that aren't in the repo. Ask what it couldn't see.
- **Diagrams that look right.** Check at least one arrow in the diagram against the code.

## Done when

You have found one thing you didn't know, or one mistake in the explanation.

<details>
<summary>Answer for <code>exercises/c/services/</code> (open when you are done)</summary>

**The call:** `GET /api/records/<id>` → `gateway/gateway/server.py` finds the route and checks if the path is public → `gateway/gateway/auth.py` reads the bearer token and verifies it with the *vendored copy* `gateway/gateway/vendor/identity_tokens.py` → the gateway drops client-sent `X-User-Id`/`X-Scopes`/`X-Unit`/`X-Gateway-Secret`, sets them from the token, adds the shared secret and removes `Authorization` → `records-api/records_api/trust.py` trusts the headers only if `X-Gateway-Secret` matches → `records-api/records_api/access.py` checks the scope `records:read`, and for restricted records also `records:read-restricted` and the same unit.

**Who checks what:** the gateway checks the token (signature, `kid`, expiry). records-api checks the scopes. Nobody checks the audience.

**When a check fails:** no or bad token → 401 with `WWW-Authenticate` from the gateway. Wrong or missing gateway secret → 401 from records-api. Restricted record you may not see → 404, the same as a missing record. Open record without `records:read` → 403. The gateway passes upstream status codes through unchanged.

**The READMEs are wrong:**

- `gateway/README.md` says RS256 with a public key and a scope check in the gateway. The code uses HMAC (HS256) with shared keys, and the scope check is commented out.
- `records-api/README.md` says records-api verifies the token itself with `legacy_jwt.py`. Nothing imports that file. It also says restricted records give 403; they give 404.

**Things worth finding:**

- The vendored copy differs from `identity/identity/tokens.py`: 300 s leeway instead of 30, and no audience check. A token for another audience is accepted.
- If `GATEWAY_SHARED_SECRET` isn't set in records-api, the expected value is `""`, and a request without the header matches. Anyone who can reach records-api directly can then set `X-User-Id` and `X-Scopes` themselves.
- `public_paths` uses `startswith`, so `/api/catalogue` also makes `/api/catalogue-admin` public.

**Open questions the agent should list:** where the keys and `GATEWAY_SHARED_SECRET` are set (the environment, not in any repo), whether records-api can be reached without going through the gateway (network policy isn't here), and which keys are in `IDENTITY_OLD_KEYS`.

</details>

## When you are done

In your agent, run `/survey oppgave C` (Codex and Copilot CLI: `survey oppgave C`). Two short questions, under a minute.
