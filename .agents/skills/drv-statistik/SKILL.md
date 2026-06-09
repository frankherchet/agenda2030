# DRV Rentenstatistik

## Overview

Rufe amtliche Daten der Deutschen Rentenversicherung (DRV) ab und lege sie reproduzierbar im Repo ab. Die DRV stellt keine öffentliche REST-API wie Destatis GENESIS zur Verfügung. Die relevanten Datenquellen sind:

- Interaktives Statistikportal: [statistik-rente.de](https://statistik-rente.de) (Rentenzugang, Rentenbestand, Abschläge)
- Jährliche Statistikbände der DRV („Rentenversicherung in Zahlen“, „Rentenbestand und Rentenzugang“)
- Bundesagentur für Arbeit Statistik API (Beschäftigung und Rentenbezug)
- BMAS Open Data (Rentenbestandsstatistik)

## Quellenpflicht

Vor fachlicher Nutzung von DRV-Daten:

1. Quelle als Ingest erfassen (Portal, Statistikband oder BMAS).
2. Rohdaten (Excel/CSV/PDF) unter `ingest/originale/` oder `analysen/daten/` ablegen.
3. Analyse- und Projektartefakte führen `source_urls` und `ingest_refs`.
4. Tabellenname, Filter, Jahrgang und Abrufdatum dokumentieren.

## Workflow

1. Kläre den Bedarf: Rentenzugang, Rentenbestand, Abschläge, Erwerbsminderung, besonders langjährig Versicherte etc.
2. Prüfe zuerst öffentliche Publikationen (`Rentenversicherung in Zahlen`, Statistikband Rentenzugang).
3. Bei Bedarf detaillierter Tabellen: Interaktives Portal statistik-rente.de nutzen (Filter: Rentenart, Alter, Abschlag, Schwerbehinderung).
4. Daten als strukturierte Tabelle (CSV/Excel) speichern.
5. Ingest oder Analyseartefakt erstellen, bevor die Daten in Modellen verwendet werden.
6. Bei sensiblen Mikrodaten: FDZ-Antrag und Datenschutzregelungen beachten.

## Helper Script

```text
.agents/skills/drv-statistik/scripts/drv_fetch.py
```

Mögliche Befehle:

```bash
python3 .agents/skills/drv-statistik/scripts/drv_fetch.py download-band --jahr 2025
python3 .agents/skills/drv-statistik/scripts/drv_fetch.py extract-text --pdf rv_in_zahlen_2025.pdf
```

## Betriebsgrenzen

- Das interaktive Portal erlaubt keine programmatische Abfrage (manuelle Bedienung notwendig).
- Große Tabellenbände sind nur als PDF verfügbar → Extraktion mit `pdfplumber` oder `tabula`.
- Mikrodaten nur über FDZ mit Antrag und Wartezeit.

## Output Standard

Nach jedem Datenabruf knapp melden:

- Quelle (Portal / Statistikband / BMAS / BA)
- Jahrgang / Tabelle
- Ausgabe-Datei
- Ingest-Pfad
- Nächste Verwendung im Modell
