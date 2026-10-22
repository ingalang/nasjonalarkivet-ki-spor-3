# A. Write tests for something that lacks them

**Lane:** [product development](../tasks.md#product-development) · [← All tasks](../tasks.md)

## The task

Find a function or an endpoint with little test coverage. Ask the agent to write tests for normal use and for error cases, and to run them. For example pytest and HTTPX against a FastAPI endpoint in AOK, or a Playwright test of a user flow in Mottak og bevaring.

**No code of your own?** Use [`exercises/a/`](../exercises/a/): a small Python module with no tests.

## Steps

1. Ask the agent which parts of the code have the least test coverage, or pick something you know lacks tests.
2. Ask it to list the cases it will test before it writes them. Add the cases it missed.
3. Let it write the tests and run them.
4. Break the code on purpose (change a condition, return the wrong value) and run the tests again.
5. Undo the break.

## Prompts to try

```text
Which functions or endpoints in this repo have little or no test coverage? Suggest three that matter.
```

```text
Before you write anything: list the test cases for <function/endpoint>, both normal use and error cases
(wrong input, missing data, no access). Don't write code yet.
```

```text
Write the tests, following how the existing tests in this repo are written. Run them and show me the result.
```

## Watch out for

- **Testing the mock.** If everything is mocked, the test only checks the mock. Ask what the test would catch if the real code broke.
- **Changing the code to make tests pass.** The task is tests, not a fix. If the agent finds a bug, have it tell you instead of fixing it quietly.
- **Tests that always pass.** That is why you break the code on purpose.

## Done when

At least one test fails if you deliberately break the code.
