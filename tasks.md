# Tasks – track 3

The goal today is to run an agent on something real from your job. It is perfectly fine to finish just one task.

> **Data and the secure zone.** Don't put personal data, archive data that isn't public, or secrets (tokens, Vault values, `.env`) into a cloud-based agent. If you use real archive data, do it with local AI or with anonymised data. If in doubt, don't.

**Tip:** Always read through what the agent changed (the diff) before you accept it. Ask the agent to run the tests itself.

---

## 1. Everyone: teach the agent your repo

Start the agent in one of your team's repos (if you don't have one, use this repo).

1. Ask: "Explain what this repo does, and how I build and test it."
2. Ask it to write a short `AGENTS.md` with what it found: how to build, test and lint, and conventions it sees in the code.
3. Delete anything that is wrong or obvious. Short beats complete.
4. Start a **new** session and ask: "How do I run the tests?"

**Done when:** the new session answers correctly without searching.

---

## 2. Pick your lane, then one task

Pick the lane that is closest to your everyday work. The letters stay the same whichever lane you are in.

| Lane | For you who … | Tasks |
|---|---|---|
| [Product development](#product-development) | develop Digitalarkivet's products | A–C |
| [Platform, operations and security](#platform-operations-and-security) | run the platform, pipelines and access | D–E |
| [Script and data automation](#script-and-data-automation) | write your own scripts, SQL or XML to get the job done | H–K |
| [No code](#no-code) | want the agent to help with text, overviews and small tools | F–G |

### Product development

**A. Write tests for something that lacks them.**
Find a function or an endpoint with little test coverage. Ask the agent to write tests for normal use and for error cases, and to run them. For example pytest and HTTPX against a FastAPI endpoint in AOK, or a Playwright test of a user flow in Mottak og bevaring.
**Done when:** at least one test fails if you deliberately break the code.

**B. A small change, plan first.**
Pick a small item from the backlog. Ask the agent for a plan *before* it changes anything: "Don't write code yet. Which files need to change, and why?" Correct the plan, then let it do the work.
**Done when:** tests and linting are green, and you understand every line of the diff.

**C. Explain something you didn't write.**
Point the agent at a file, a workflow or a configuration you find hard to follow, for example an Argo workflow, an index template in `da-indexer` or an Alembic migration. Ask for an explanation and a diagram (Mermaid) of the flow.
**Done when:** you have found one thing you didn't know, or one mistake in the explanation.

### Platform, operations and security

**D. Review a PR or a workflow.**
Ask the agent to look for security problems in a PR or in `.github/workflows/`: secrets in plain text, permissions that are too broad, and actions not pinned to a version.
**Done when:** you have sorted the findings into *real*, *false alarm* and *unsure*.

**E. Write a diagnostic script.**
Ask the agent to write a script (bash or PowerShell) that only *reads* the status of a system you run, and never changes anything.
**Done when:** you have read the whole script before running it.

### Script and data automation

You don't need a team repo. Put your scripts or queries in a folder, run `git init`, and start the agent there. Use test data or anonymised data, never real archive data in a cloud-based agent.

**H. Tidy up and test an old script.**
Take a script you use often, for example an extract from Noark 5. Ask the agent to explain it, suggest a tidier version and write a test that runs it on a small test file.
**Done when:** the new version gives the same result as the old one on the test file.

**I. Validate an XML extract.**
Ask the agent for a script that checks an XML file against its schema (XSD) and writes the errors as a readable summary.
**Done when:** the script finds an error you put in on purpose.

**J. Make a query someone else can take over.**
Give the agent an SQL query that only you understand. Ask it to explain the query, rewrite it to be readable and write a short description of what it returns.
**Done when:** a colleague understands the query without asking you.

**K. Automate a recurring task.**
Pick something you do by hand every week or month: renaming files, merging spreadsheets, checking that files are complete. Ask the agent for a script that does it, with a dry-run mode that only shows what it would do.
**Done when:** the dry run shows the right result before you run it for real.

### No code

**F. From notes to a decision paper.**
Give the agent an unclassified note or meeting minutes, and ask for a decision paper with background, options and a recommendation.
**Done when:** the paper is good enough after at most two rounds of corrections.

**G. Build a small tool.**
Ask the agent to make a simple HTML page you can open in the browser, for example a checklist or an overview of who owns which service.
**Done when:** the page works, and you have asked the agent to change it three times.
