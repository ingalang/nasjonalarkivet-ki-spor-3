# Oppgaver – spor 3

Målet i dag er å få kjørt en agent på noe ekte fra jobben din. Det er helt greit å bare bli ferdig med én oppgave.

> **Data og sikker sone.** Ikke legg personopplysninger, arkivdata som ikke er offentlige, eller hemmeligheter (tokens, Vault-verdier, `.env`) i en skybasert agent. Bruker du ekte arkivdata, gjør du det med lokal KI eller med anonymiserte data. Er du i tvil, la være.

**Tips:** Les alltid gjennom det agenten har endret (diffen) før du godtar det. Be agenten kjøre testene selv.

---

## 1. Alle: lær agenten repoet ditt

Start agenten i et av teamets repoer (har du ikke et, bruk dette repoet).

1. Spør: «Forklar hva dette repoet gjør, og hvordan jeg bygger og tester det.»
2. Be den skrive en kort `AGENTS.md` med det den fant: hvordan man bygger, tester og linter, og konvensjoner den ser i koden.
3. Stryk det som er feil eller åpenbart. Kort er bedre enn komplett.
4. Start en **ny** økt og spør: «Hvordan kjører jeg testene?»

**Ferdig når:** den nye økten svarer riktig uten å lete.

---

## 2. Velg én oppgave

### Har du kode

**A. Skriv tester for noe som mangler det.**
Finn en funksjon eller et endepunkt med lite testdekning. Be agenten skrive tester for vanlig bruk og for feiltilfeller, og kjøre dem.
**Ferdig når:** minst én test feiler hvis du med vilje ødelegger koden.

**B. En liten endring, med plan først.**
Velg en liten sak fra backloggen. Be agenten om en plan *før* den endrer noe: «Ikke skriv kode ennå. Hvilke filer må endres, og hvorfor?» Rett planen, og la den så gjøre jobben.
**Ferdig når:** testene og linting er grønne, og du forstår hver linje i diffen.

**C. Forklar noe du ikke har skrevet selv.**
Pek agenten på en fil, en workflow (for eksempel GitHub Actions eller Argo) eller en konfigurasjon du synes er uoversiktlig. Be om en forklaring og et diagram (Mermaid) over flyten.
**Ferdig når:** du har funnet én ting du ikke visste, eller én feil i forklaringen.

### Drift og sikkerhet

**D. Gå gjennom en PR eller en workflow.**
Be agenten se etter sikkerhetsproblemer i en PR eller i `.github/workflows/`: hemmeligheter i klartekst, for vide tilganger og actions som ikke er låst til en versjon.
**Ferdig når:** du har sortert funnene i *ekte*, *falsk alarm* og *usikker*.

**E. Lag et diagnoseskript.**
Be agenten skrive et skript (bash eller PowerShell) som bare *leser* status for et system du drifter, og aldri endrer noe.
**Ferdig når:** du har lest hele skriptet før du kjørte det.

### Uten kode

**F. Fra notat til beslutningsgrunnlag.**
Gi agenten et ugradert notat eller møtereferat, og be om et beslutningsnotat med bakgrunn, alternativer og anbefaling.
**Ferdig når:** notatet er godt nok etter maks to runder med retting.

**G. Bygg et lite verktøy.**
Be agenten lage en enkel HTML-side du kan åpne i nettleseren, for eksempel en sjekkliste eller en oversikt over hvem som eier hvilken tjeneste.
**Ferdig når:** siden virker, og du har bedt agenten endre den tre ganger.
