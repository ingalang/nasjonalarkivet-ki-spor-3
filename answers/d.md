# Answer for exercise D

For [task D. Review a PR or a workflow](../tasks/d-review-pr-or-workflow.md) and [`exercises/d/`](../exercises/d/).

Read this after reviewing the workflow yourself.

- `pull_request_target` together with checking out the PR's code: code from a fork runs with access to secrets.
- `permissions: write-all`: far more access than the job needs.
- The password is in plain text in the file.
- `actions/checkout@v4` and `some-org/deploy-preview@main` are not pinned to a commit SHA. `@main` from an unknown org is the worst one.
- The PR title is put straight into a `run` step: a title like `"; curl … | sh; "` runs as a command.
- `actions/setup-python` *is* pinned to a SHA. That one is fine.
- `GITHUB_TOKEN` used through `secrets.` in an `env` block is the normal way, and fine in itself. The problem is the permissions it has here.
