# DRV Rentenstatistik

## Overview

Rufe amtliche Daten der Deutschen Rentenversicherung (DRV) ab und lege sie reproduzierbar im Repo ab. Die DRV stellt keine öffentliche REST-API wie Destatis GENESIS zur Verfügung. Die Daten werden daher über folgende Wege beschafft:

- Interaktives Statistikportal: [statistik-rente.de](https://statistik-rente.de)
- Jährliche Statistikbände (PDF)
- Forschungsdatenzentrum (FDZ) der Rentenversicherung (für Mikrodaten)

## Quellenpflicht

Vor fachlicher Nutzung von DRV-Daten:

1. Quelle als Ingest erfassen (Portal oder Statistikband).
2. Rohdaten (Excel/CSV/PDF) unter `ingest/originale/` oder `analysen/daten/` ablegen.
3. Analyse- und Projektartefakte führen `source_urls` und `ingest_refs`.
4. Tabellenname, Filter, Jahrgang und Abrufdatum dokumentieren.

## Workflow

1. Kläre den Bedarf: Rentenzugang, Rentenbestand, Abschläge, Erwerbsminderung, besonders langjährig Versicherte etc.
2. Prüfe zuerst öffentliche Publikationen (`Rentenversicherung in Zahlen`, Statistikband Rentenzugang).
3. Bei Bedarf detaillierter Tabellen: Interaktives Portal nutzen (Filter: Rentenart, Alter, Abschlag, Schwerbehinderung).
4. Daten als strukturierte Tabelle (CSV/Excel) speichern.
5. Ingest oder Analyseartefakt erstellen, bevor die Daten in Modellen verwendet werden.
6. Bei sensiblen Mikrodaten: FDZ-Antrag und Datenschutzregelungen beachten.

## Helper Script

Da keine direkte API existiert, dient das Skript primär der Dokumentation und Automatisierung von Download + Extraktion.

```text
.agents/skills/drv-statistik/scripts/drv_fetch.py
```

Mögliche Befehle (Beispiel):

```bash
python3 .agents/skills/drv-statistik/scripts/drv_fetch.py download-band --jahr 2025 --typ "Rentenversicherung in Zahlen"
python3 .agents/skills/drv-statistik/scripts/drv_fetch.py extract-table --pdf "rv_in_zahlen_2025.pdf" --tabelle "Rentenzugang nach Alter"
```

## Betriebsgrenzen

- Das interaktive Portal erlaubt keine programmatische Abfrage (manuelle Bedienung notwendig).
- Große Tabellenbände sind nur als PDF verfügbar → Extraktion mit `pdfplumber` oder `tabula`.
- Mikrodaten nur über FDZ mit Antrag und Wartezeit.

## Output Standard

Nach jedem Datenabruf knapp melden:

- Quelle (Portal / Statistikband / FDZ)
- Jahrgang / Tabelle
- Ausgabe-Datei
- Ingest-Pfad
- Nächste Verwendung im Modell
