# DRV Rentenstatistik

## Overview

Rufe amtliche Daten der Deutschen Rentenversicherung (DRV) ab und lege sie reproduzierbar im Repo ab. Die DRV stellt keine öffentliche REST-API wie Destatis GENESIS zur Verfügung. Die relevanten Datenquellen sind:

- Interaktives Statistikportal: [statistik-rente.de](https://statistik-rente.de)
- Jährliche Statistikbände der DRV
- Bundesagentur für Arbeit Statistik API
- BMAS Open Data (Rentenbestandsstatistik)

## Setup

Benötigte Python-Pakete:

```bash
uv pip install pdfplumber openpyxl pandas
```

Empfohlene Ausführung (reproduzierbar):

```bash
uv run --with pdfplumber --with openpyxl --with pandas \
  python .agents/skills/drv-statistik/scripts/drv_fetch.py download-band --jahr 2025
```

## Quellenpflicht

Vor fachlicher Nutzung von DRV-Daten:

1. Quelle als Ingest erfassen.
2. Rohdaten unter `ingest/originale/` oder `analysen/daten/` ablegen.
3. Analyse- und Projektartefakte führen `source_urls` und `ingest_refs`.
4. Tabellenname, Filter, Jahrgang und Abrufdatum dokumentieren.

## Workflow

1. Kläre den Bedarf (Rentenzugang, Abschläge, Erwerbsminderung etc.).
2. Öffentliche Publikationen prüfen (`Rentenversicherung in Zahlen`).
3. Bei Bedarf detaillierter Tabellen: Interaktives Portal oder BMAS Open Data nutzen.
4. Daten als strukturierte Tabelle speichern.
5. Ingest oder Analyseartefakt erstellen.

## Helper Script

```text
.agents/skills/drv-statistik/scripts/drv_fetch.py
```

Mögliche Befehle:

```bash
python3 .agents/skills/drv-statistik/scripts/drv_fetch.py download-band --jahr 2025
python3 .agents/skills/drv-statistik/scripts/drv_fetch.py download-bmas
python3 .agents/skills/drv-statistik/scripts/drv_fetch.py extract-text --pdf rv_in_zahlen_2025.pdf
```

## Betriebsgrenzen

- Interaktives Portal erlaubt keine programmatische Abfrage.
- Große Tabellenbände nur als PDF → Extraktion mit `pdfplumber`.
- Mikrodaten nur über FDZ mit Antrag.

## Output Standard

Nach jedem Datenabruf knapp melden:

- Quelle
- Jahrgang / Tabelle
- Ausgabe-Datei
- Ingest-Pfad
- Nächste Verwendung im Modell
