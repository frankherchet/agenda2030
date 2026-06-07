---
name: destatis-genesis
description: Nutzt die Destatis GENESIS-Online RESTful/JSON-API für reproduzierbare amtliche Datenabrufe im agenda2030-Repo, insbesondere Bevölkerung, Altersstruktur, Erwerbstätigkeit und weitere Destatis-Tabellen. Use when the user asks to use GENESIS, Destatis API, Destatis-Daten abrufen, Tabellen suchen, amtliche Destatis-Daten importieren, or fetch Bevölkerung/Erwerbstätigkeit/Demographie data for analyses or reform models.
---

# Destatis GENESIS

## Overview

Rufe amtliche Destatis-Daten über die GENESIS-Online RESTful/JSON-API ab und
lege sie reproduzierbar im Repo ab. Zugangsdaten werden nie gespeichert oder
committet.

## Secrets

- Niemals Benutzername, Passwort oder Token in Dateien, Commits, Logs oder
  Antworten schreiben.
- Nutze lokale Umgebungsvariablen:
  - `DESTATIS_USER`
  - `DESTATIS_PASSWORD`
  - optional `DESTATIS_TOKEN`, falls der lokale Account Tokenzugriff nutzt
- Wenn Zugangsdaten fehlen, Skript/Anleitung vorbereiten und den User bitten,
  die ENV-Werte lokal zu setzen.

## Quellenpflicht

Vor fachlicher Nutzung eines API-Ergebnisses:

1. API-Quelle als Ingest referenzieren:
   `ingest/links/2026-06-06-destatis-genesis-api.md`
2. Rohantwort oder strukturierte Ausgabe versionierbar ablegen:
   - kleine JSON/CSV: `ingest/originale/` oder `analysen/daten/`
   - zweckgebundene Modellinputs: `analysen/daten/`
3. Analyse-/Projektdateien führen `source_urls` und `ingest_refs`.
4. Tabellenname, Parameter, Sprache, Abrufdatum und Ausgabeformat dokumentieren.

## Workflow

1. Kläre Zweck: Katalogsuche, Metadaten, Tabellenabruf oder Modellinput.
2. Suche passende Tabellen zuerst über GENESIS-Katalog/Find.
3. Prüfe Metadaten der Tabelle: Variablen, Zeit, regionale Ebene, Werte.
4. Rufe Daten mit klar dokumentierten Parametern ab.
5. Speichere Ergebnis als CSV/JSON unter `analysen/daten/` oder
   `ingest/originale/`.
6. Erzeuge oder aktualisiere ein Ingest/Analyseartefakt, bevor die Daten in
   Rechnungen genutzt werden.
7. Bei Rentenmodellen klar trennen:
   - Destatis kann Bevölkerung, Demographie und teils Erwerbsdaten liefern.
   - DRV-spezifische Rentenzugänge, Abschläge und Erwerbsminderung brauchen
     separate DRV-/Statistik-Rente-Quellen.

## Helper Script

Nutze bei API-Arbeiten bevorzugt:

```text
.agents/skills/destatis-genesis/scripts/genesis_fetch.py
```

Typische Aufrufe:

```bash
python3 .agents/skills/destatis-genesis/scripts/genesis_fetch.py logincheck
python3 .agents/skills/destatis-genesis/scripts/genesis_fetch.py find --term "geburten" --category Alle --pagelength 100
python3 .agents/skills/destatis-genesis/scripts/genesis_fetch.py table --name 12411-0005 --output analysen/daten/destatis-12411-0005.json
python3 .agents/skills/destatis-genesis/scripts/genesis_fetch.py metadata-table --name 12411-0005
python3 .agents/skills/destatis-genesis/scripts/genesis_fetch.py post catalogue/tables --param selection=12612 --param pagelength=100
```

Das Skript liest `DESTATIS_USER`/`DESTATIS_PASSWORD` aus der Umgebung und
sendet POST-Anfragen an `https://genesis.destatis.de/genesisWS/rest/2020`.
Parameter bei
Bedarf mit `--param key=value` ergänzen.

## API Reference

Die komplette Swagger-Datei wird nicht in `SKILL.md` geladen. Lade bei Bedarf
die kompakte Referenz:

```text
.agents/skills/destatis-genesis/references/api.md
```

Diese Referenz enthält die aus `GOJsonApi.json` extrahierten Endpunkte,
Parametergruppen und Beispiele wie die Geburten-Suche.

## Betriebsgrenzen

- GENESIS begrenzt parallele Requests. Bei mehr als drei parallelen Abrufen
  kann Fehlercode `6` erscheinen.
- Wenn Fehlercode `6` erscheint, zuerst `logincheck` ausführen. Der Dienst
  beendet damit länger als 15 Minuten laufende Requests und gibt die Session
  wieder frei.
- Batch-Abrufe sequenziell oder in kleinen Paketen ausführen; keine großen
  parallelen `multi_tool_use`-Abfragen gegen GENESIS starten.

## Output Standard

Nach einem Abruf knapp melden:

- genutzte Tabelle/Methode,
- Ausgabe-Datei,
- Ingest-Pfad,
- zentrale Parameter,
- ob Zugangsdaten fehlten oder der Abruf erfolgreich war,
- nächste Modell-/Analyseverwendung.
