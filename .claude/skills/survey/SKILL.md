---
name: survey
description: Kort anonym tilbakemeldingsundersøkelse for Spor 3. Bruk når brukeren skriver "survey", "/survey" eller ber om å gi tilbakemelding på kurset.
---

You are running a short anonymous survey for the workshop "Spor 3, Oslo". Follow these rules exactly.

Test mode: if I write "/survey random" (or "survey random"), do not ask anything. Pick a random option for questions 1–4, write "[test]" as the answer to questions 5 and 6, then write the file and upload it exactly as described below.

Rules:
- Ask the questions below in Norwegian Bokmål, one at a time. Use your multiple-choice question tool if you have one; otherwise show numbered options and let me answer with a number.
- Do not read, search or open any files. Do not run any commands except writing the one output file and the one upload command below.
- Never record my name, username, computer name, file paths or anything that identifies me. If a free-text answer contains a name of a person, replace it with [navn].
- Keep free-text answers in my own words. Fix only obvious typos.
- Make up a random 4-character id (letters and digits).

Questions:
1. "Hvor ofte brukte du en KI-agent (ikke bare kodefullføring) før i dag?" Options: Aldri / Har prøvd / Ukentlig / Daglig
2. "Hva var mest nyttig i dag?" Options: Lokal KI / Byggeklossene / Hareg / Frustrasjon med sikker sone
3. "Hva stopper deg mest fra å bruke agent i jobben?" Options: Tilgang eller godkjenning / Tid / Vet ikke hva jeg skal bruke den til / Stoler ikke på resultatet / Virker ikke på maskinen min / Ingenting
4. "Hvor sannsynlig er det at du bruker en agent på en ekte arbeidsoppgave neste uke? (1 = ikke i det hele tatt, 5 = helt sikkert)" Options: 1 / 2 / 3 / 4 / 5
5. "Nevn én konkret oppgave fra jobben din du vil prøve agenten på. (Ingen persondata.)" Free text.
6. "Én ting vi bør endre til neste gang." Free text.

When all six are answered, write the file tilbakemelding-<id>.md in the current folder with exactly this format, then show me the content:

# Tilbakemelding <id>
skjema: spor3-oslo-v1
Q1: <option>
Q2: <option>
Q3: <option>
Q4: <number>
Q5: <free text on one line>
Q6: <free text on one line>

Then upload it by running exactly this one command (on Windows use `curl.exe` instead of `curl`):

curl -sS -X POST -H "ngrok-skip-browser-warning: 1" --data-binary @tilbakemelding-<id>.md https://uniambic-kamari-unbarrelled.ngrok-free.dev/

- If the response is "Takk for tilbakemeldingen!", tell me it was sent.
- If the command fails, tell me in Norwegian that the upload failed and that I can send the file tilbakemelding-<id>.md to the course leader instead.
- If you cannot write files or run commands (for example in ChatGPT), skip both steps. Show the content, then give me this link to click, with every value URL-encoded:

https://uniambic-kamari-unbarrelled.ngrok-free.dev/?skjema=spor3-oslo-v1&id=<id>&Q1=<…>&Q2=<…>&Q3=<…>&Q4=<…>&Q5=<…>&Q6=<…>
