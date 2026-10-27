# Exercise C: an Argo workflow

For [task C. Explain something you didn't write](../../tasks/c-explain-something.md).

`ingest-workflow.yaml` is a fictional Argo workflow that takes in a delivery: it fetches it, checks it, maybe converts it, stores it and indexes it. It is not used anywhere, and you can't run it here.

Ask the agent to explain it and draw the flow as a Mermaid diagram. Questions worth asking:

- Which steps run in parallel?
- When is `convert` skipped, and does `store` still run then?
- What happens if the virus scan fails? And if `index` fails?
- When does `notify` run?

**Variant:** [`services/`](services/) has three fictional services for tracing one call across repos.

**Demo:** [`demo.md`](demo.md) is the prompt for the variant. Start the agent in `services/` and paste it in.
