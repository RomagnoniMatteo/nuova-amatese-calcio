# Nuova Amatese Calcio — sito ufficiale

Sito Vue 3 + Vite per la Nuova Amatese Calcio A.S.D.: il focus è invitare le persone a
venire a giocare (contatti, campo, affitto del 5 a 5), con in più la lore Pokémon-themed
della squadra — storia a episodi, podcast e un pokédex "segreto" che si sblocca dentro
la pagina Prima Squadra. I contenuti si sbloccano da soli in base alla data, senza
bisogno di un backend: basta un file JSON per tipo di contenuto.

## Sviluppo locale

```bash
npm install
npm run dev
```

Apri l'indirizzo mostrato in terminale (di solito http://localhost:5173).

> **Windows + PowerShell**: se `npm install` dà errore di "execution policy disabilitata",
> apri PowerShell come amministratore e lancia `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`,
> oppure usa il Prompt dei comandi (cmd.exe) al posto di PowerShell.

## Build di produzione

```bash
npm run build
npm run preview   # per controllare la build in locale
```

## Come funziona lo sblocco temporale

Ogni episodio, puntata podcast o carta pokédex ha un campo data in formato ISO
(`"YYYY-MM-DD"`) dentro i file in `src/data/`:

- `src/data/episodes.json` → campo `date`
- `src/data/podcasts.json` → campo `date`
- `src/data/pokedex.json` → campo `unlockDate`

Il contenuto diventa visibile automaticamente non appena la data del visitatore
raggiunge quella indicata (vedi `src/composables/useUnlock.js`). Per pubblicare
qualcosa prima o dopo, basta modificare la data nel JSON e ricompilare/ripubblicare
il sito — non serve toccare i componenti.

**Nota sulle date:** le date degli episodi della "Storia" derivano da quelle scritte
nel documento originale (stagione da fine giugno 2026 ad aprile 2027). Le date delle
puntate podcast senza una data esplicita nel testo sono state stimate in sequenza:
correggile liberamente in `raw/podcasts.txt` (o direttamente in `src/data/podcasts.json`)
per farle combaciare con il calendario reale.

## Il pokédex è "nascosto"

Non esiste più una pagina `/pokedex` a sé stante. Le carte vivono in
`src/data/pokedex.json` con un `playerId` che le collega a un giocatore in
`src/data/players.json`. Nella pagina **Prima Squadra**:

- se la carta di un giocatore non è ancora sbloccata (`unlockDate` futura), sotto al suo
  nome compare solo un avviso "scheda ancora segreta" con la data di sblocco;
- appena la data arriva, compare un pulsante "Apri scheda pokédex" che mostra le
  informazioni della carta in un **modal** (`src/components/PokedexModal.vue`), senza
  lasciare la pagina.

Per aggiungere una carta a un giocatore che ancora non ce l'ha, aggiungi una voce in
`pokedex.json` con lo stesso `playerId` usato in `players.json`.

## Instagram per ogni episodio

Ogni episodio in `src/data/episodes.json` ha un campo `instagramUrl`. Il comportamento
nella pagina dell'episodio (`EpisodioView.vue`) dipende da quel campo:

- **`instagramUrl` vuoto (`null`)** → viene mostrato solo un pulsante che porta al
  profilo Instagram generale, e il testo del dialogo resta visibile normalmente qui sul sito.
- **`instagramUrl` valorizzato con il permalink del post reale** → viene mostrato
  l'**embed ufficiale di Instagram** (`src/components/InstagramEmbed.vue`), che carica
  il post direttamente da Instagram tramite lo script ufficiale `embed.js` — leggero e
  caricato solo quando serve, non aumenta la dimensione della build. In questo caso il
  testo del dialogo locale viene nascosto di default dietro un pulsante "mostra anche il
  testo qui sul sito", così il contenuto "vive" davvero su Instagram e il sito resta
  leggero, con il testo come rete di sicurezza per accessibilità o per chi non usa Instagram.

Per collegare un episodio al suo post reale, apri `src/data/episodes.json`, trova
l'episodio e incolla l'URL del permalink Instagram (es. `https://www.instagram.com/p/XXXXXXX/`)
nel campo `instagramUrl`.

Se rigeneri `episodes.json` con `raw/build_data.py` (vedi sotto), gli `instagramUrl`
già inseriti a mano vengono preservati automaticamente.

## Rigenerare i dati da testo grezzo (opzionale)

Le cartelle `raw/story.txt` e `raw/podcasts.txt` contengono il copione originale in un
formato semplice a blocchi separati da `###`. Lo script `raw/build_data.py` li
trasforma in `src/data/episodes.json` e `src/data/podcasts.json`. Se preferisci scrivere
nuovi episodi direttamente in italiano/testo invece che in JSON:

```bash
python3 raw/build_data.py
```

Formato di un blocco episodio in `story.txt`:

```
30 giugno
## 05. TITOLO DELL'EPISODIO
**[Didascalia di scena tra doppie parentesi quadre e asterischi.]**
→ **PERSONAGGIO:** battuta.
→ **ALTRO PERSONAGGIO:** [...]
###
```

Formato di un blocco podcast in `podcasts.txt`:

```
2026-09-18 | Titolo della puntata
-> Cenda: battuta.
-> Ospite: risposta.
###
```

In alternativa puoi ignorare lo script e scrivere/incollare direttamente dentro
`src/data/episodes.json` / `src/data/podcasts.json` seguendo lo schema esistente.

## Aggiungere o modificare contenuti

- **Giocatori/staff**: `src/data/players.json`, `src/data/staff.json`
- **Pokédex**: `src/data/pokedex.json` (aggiungi una card con `unlockDate` e `playerId`
  per farla comparire come sblocco nella pagina Prima Squadra)
- **Info società / Dove siamo**: `src/data/club.json` (indirizzi, contatti, orari
  segreteria, social — recuperati dal sito ufficiale Wix)

Tutti i file sono semplici array di oggetti (o un oggetto unico per `club.json`):
aggiungere una voce nuova richiede solo di copiare la struttura di una voce esistente.

## Deploy su GitHub Pages

Il repo include `.github/workflows/deploy.yml`: ad ogni push su `main` la pipeline
compila il sito e lo pubblica su GitHub Pages automaticamente.

Passi una tantum:

1. Crea un repository su GitHub e pusha questo progetto.
2. Su GitHub vai in **Settings → Pages** e imposta **Source: GitHub Actions**.
3. Ad ogni push su `main`, il sito sarà pubblicato su
   `https://<tuo-utente>.github.io/<nome-repo>/`.

Non serve configurare il `base` di Vite: `vite.config.js` usa un percorso relativo
(`base: './'`) e il router usa l'hash (`/#/storia`) proprio per funzionare su
qualunque sotto-percorso senza configurazione aggiuntiva.

## Struttura del progetto

```
src/
  components/       DialogueScript.vue, LockedCard.vue, PokedexModal.vue, InstagramEmbed.vue
  composables/       useUnlock.js — logica di sblocco temporale
  data/              *.json — tutti i contenuti del sito (incluso club.json)
  router/            definizione delle rotte
  styles/            tokens.css (palette/tipografia), global.css
  views/             Home, Squadra, Storia, Episodio, Podcast, PodcastEpisodio, DoveSiamo
raw/                 testo grezzo + script di conversione in JSON
public/               favicon
src/assets/images/    immagini fornite (spogliatoio, pokédex, podcast)
```

