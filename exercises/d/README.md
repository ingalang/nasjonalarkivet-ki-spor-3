# Exercise D: a workflow with security problems

For [task D. Review a PR or a workflow](../../tasks/d-review-pr-or-workflow.md).

`publish.yml` is a GitHub Actions workflow that builds and publishes a preview of a PR. It has several deliberate security problems, and some things that look suspicious but are fine. It lives outside `.github/workflows/`, so it never runs. Don't copy it into a real repo.

Ask the agent to review it, then sort the findings into *real*, *false alarm* and *unsure*. Don't look for the answers first.

When you are done, compare your review with the [answer key](../../answers/d.md).
