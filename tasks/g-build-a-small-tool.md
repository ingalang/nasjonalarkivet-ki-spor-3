# G. Build a small tool

**Lane:** [no code](../tasks.md#no-code) · [← All tasks](../tasks.md)

## The task

Ask the agent to make a simple HTML page you can open in the browser, for example a checklist or an overview of who owns which service.

## Steps

1. Decide what the page is for and who uses it.
2. Ask for one HTML file that works without a server or installation.
3. Open it in the browser and try it.
4. Ask for three changes, one at a time, and check the page after each one.

## Prompts to try

```text
Make a single HTML file I can open in the browser: a checklist for <routine>. I can tick items off,
and the ticks are kept when I reload the page. No server, nothing to install.
```

```text
Make an HTML page with an overview of who owns which service. Put the data in a list at the top of
the file so I can edit it myself. Add a search box.
```

```text
Change: <what>. Don't change anything else.
```

**Compare layouts first (Claude Code).** Before the agent builds the page, have it show you two or three clickable mockups as one private claude.ai artifact. Pick one, then ask for the HTML file. The artifact is stored on claude.ai, so use made-up data only.

```text
Before you build anything: make three clickable mockups of <the page>, as one artifact with a switcher so I
can compare them in the browser. Make them genuinely different layouts, not just different colours. Use
made-up data. Write two sentences under each option: what it does well and its weak spot. Wait until I have
picked one.
```

```text
Build option <B> as a single HTML file I can open in the browser. No server, nothing to install.
```

## Watch out for

- **External dependencies.** A page that loads scripts from the internet may not work on a locked-down machine. Ask for everything in one file.
- **Data that disappears.** Data saved in the browser only exists on your machine, in that browser.
- **Changes that break something else.** Test the whole page after each change, not only the new part.

## Done when

The page works, and you have asked the agent to change it three times.

## When you are done

In your agent, run `/survey oppgave G` (Codex and Copilot CLI: `survey oppgave G`). Two short questions, under a minute.
