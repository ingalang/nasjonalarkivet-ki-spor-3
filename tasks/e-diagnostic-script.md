# E. Write a diagnostic script

**Lane:** [platform, operations and security](../tasks.md#platform-operations-and-security) · [← All tasks](../tasks.md)

## The task

Ask the agent to write a script (bash or PowerShell) that only *reads* the status of a system you run, and never changes anything.

## Steps

1. Pick something you check by hand: pods in a namespace, disk space, certificate expiry, the status of a queue.
2. Ask for a script that only reads, and that prints a short summary.
3. Ask the agent to list every command in the script and whether it can change anything.
4. Read the whole script yourself.
5. Run it against a test environment first.

## Prompts to try

```text
Write a bash script that checks <system>: <what to check>. It must only read, never change anything.
Print one line per check with OK / WARNING / ERROR, and exit with a non-zero code if anything is ERROR.
```

```text
List every command the script runs, and for each one: can it change anything? Could it under
different arguments?
```

```text
Make the script fail clearly if a tool it needs (kubectl, jq, openssl) is missing.
```

## Watch out for

- **Hidden writes.** `kubectl apply`, `rm`, `>` redirects, `--fix` flags, or a log file in the wrong place. Search the script for them.
- **The wrong environment.** A script that reads the current kubectl context can hit production. Have it print which context or host it uses.
- **Secrets in the output.** Status commands can print tokens or connection strings.

## Done when

You have read the whole script before running it.
