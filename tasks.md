# Tasks – track 3

The goal today is to run an agent on something real from your job. It is perfectly fine to finish just one task.

**Tip:** Always read through what the agent changed (the diff) before you accept it. Ask the agent to run the tests itself.

## Data and the secure zone

Don't put personal data, archive data that isn't public, or secrets (tokens, Vault values, `.env`) into a cloud-based agent. If you use real archive data, do it with local AI or with anonymised data. If in doubt, don't.

No suitable repo or safe data? [`exercises/`](exercises/) has made-up material for most of the tasks.

---

## 1. Everyone: teach the agent your repo

[**1. Teach the agent your repo**](tasks/1-teach-the-agent-your-repo.md): have the agent explore your repo and write an `AGENTS.md`, then check that a new session knows how to run the tests. Working with documents or data? The page has a variant for a folder of files.

---

## 2. Pick your lane, then one task

Pick the lane that is closest to your everyday work. The letters stay the same whichever lane you are in.

| Lane | For you who … | Tasks |
|---|---|---|
| [Product development](#product-development) | develop Digitalarkivet's products | A–C |
| [Platform, operations and security](#platform-operations-and-security) | run the platform, pipelines and access | D, E, L |
| [Script and data automation](#script-and-data-automation) | write your own scripts, SQL or XML to get the job done | H–K |
| [No code](#no-code) | want the agent to help with text, overviews and small tools | F–G |

### Product development

- [**A. Write tests for something that lacks them**](tasks/a-write-tests.md): tests for normal use and error cases, and at least one that fails when you break the code.
- [**B. A small change, plan first**](tasks/b-small-change-plan-first.md): the agent plans before it codes, you correct the plan, then it does the work.
- [**C. Explain something you didn't write**](tasks/c-explain-something.md): an explanation and a Mermaid diagram of a file, workflow or configuration, or of one call across services.

### Platform, operations and security

- [**D. Review a PR or a workflow**](tasks/d-review-pr-or-workflow.md): look for secrets, broad permissions and unpinned actions, and sort what it finds.
- [**E. Write a diagnostic script**](tasks/e-diagnostic-script.md): a script that only reads the status of a system you run.
- [**L. Troubleshoot from logs and metrics**](tasks/l-troubleshoot-from-signals.md): from a known symptom to a timeline, hypotheses with evidence, and the next check.

### Script and data automation

You don't need a team repo for these. Use your own scripts in a folder with `git init`, or the material in [`exercises/`](exercises/).

- [**H. Tidy up and test an old script**](tasks/h-tidy-up-old-script.md): a tidier version that gives the same result on a test file.
- [**I. Validate an XML extract**](tasks/i-validate-xml-extract.md): check an XML file against its XSD and summarise the errors.
- [**J. Make a query someone else can take over**](tasks/j-readable-sql-query.md): explain and rewrite an SQL query so a colleague understands it.
- [**K. Automate a recurring task**](tasks/k-automate-recurring-task.md): a script for something you do by hand, with a dry-run mode.

### No code

- [**F. From notes to a decision paper**](tasks/f-notes-to-decision-paper.md): from meeting notes to background, options and a recommendation.
- [**G. Build a small tool**](tasks/g-build-a-small-tool.md): a simple HTML page you can open in the browser, changed three times.

---

## 3. Wrap up: what did it give you?

Everyone ends by answering these questions, briefly and with concrete examples:

1. **The need.** What did you want to get done?
2. **The agent.** What did the agent actually do?
3. **The check.** How did you check that the result was right, and what did you find?
4. **Next step.** What would it take to use this in your job?

After each task, also run `/survey oppgave <letter>` (Codex: `survey oppgave <letter>`), as the task
page says at the bottom. At the end of the day, run `/survey slutt`.
