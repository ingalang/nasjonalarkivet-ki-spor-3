# F. From notes to a decision paper

**Lane:** [no code](../tasks.md#no-code) · [← All tasks](../tasks.md)

> Only unclassified notes. See [Data and the secure zone](../tasks.md#data-and-the-secure-zone).

## The task

Give the agent an unclassified note or meeting minutes, and ask for a decision paper with background, options and a recommendation.

**No notes at hand?** Use [`exercises/f/`](../exercises/f/): made-up notes from a meeting about the digitisation queue.

## Steps

1. Pick notes or minutes where a decision is still open.
2. Remove names and anything that isn't meant to leave the building.
3. Tell the agent who will read the paper and what they need to decide.
4. Ask for a draft, then correct it. Count the rounds.

## Prompts to try

```text
Here are notes from a meeting: <paste>. Write a decision paper of at most one page for <who> with:
background, the decision that is needed, two or three options with pros and cons, and a recommendation.
```

```text
Before you write: what is unclear in the notes, and what do you need to know from me?
```

```text
Which claims in the paper are not in the notes? Mark them.
```

## Watch out for

- **Made-up facts.** The agent fills in gaps with things that sound right. Ask it to mark everything that isn't in the notes.
- **A recommendation without support.** Check that the recommendation follows from the options, not from the agent's taste.
- **Too long.** Ask for a length limit up front.

## Done when

The paper is good enough after at most two rounds of corrections.
