# C. Explain something you didn't write

**Lane:** [product development](../tasks.md#product-development) · [← All tasks](../tasks.md)

## The task

Point the agent at a file, a workflow or a configuration you find hard to follow, for example an Argo workflow, an index template in `da-indexer` or an Alembic migration. Ask for an explanation and a diagram (Mermaid) of the flow.

**Nothing at hand?** Use [`exercises/c/`](../exercises/c/): a fictional Argo workflow.

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
