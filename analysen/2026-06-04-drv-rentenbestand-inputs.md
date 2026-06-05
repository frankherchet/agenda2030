---
title: DRV-Rentenbestand Inputs fuer Abschmelzmodell
date: 2026-06-04
type: analyse
status: arbeitsfassung
source_urls:
  - https://www.deutsche-rentenversicherung.de/SharedDocs/Downloads/DE/Statistiken-und-Berichte/statistikpublikationen/statistikband_rente.pdf?__blob=publicationFile&v=5
ingest_refs:
  - ingest/dokumente/2026-06-04-drv-statistikband-rente-2024.md
  - ingest/dokumente/2026-06-04-drv-statistikband-rente-2024-quellenmetadaten.md
data_artifacts:
  - analysen/daten/2026-06-04-drv-rentenbestand-struktur.csv
  - analysen/daten/2026-06-04-bundesmittel-zerlegung.csv
scripts:
  - scripts/build_drv_renten_inputs.py
---

# DRV-Rentenbestand Inputs für Abschmelzmodell

Stand: 2026-06-04

Quelle: `ingest/originale/2026-06-04-drv-statistikband-rente-2024.pdf`

## Zweck

Diese Analyse extrahiert aus dem DRV-Statistikband die Rentenbestandsstruktur
und eine Reformklassifikation der Bundesmittel als Input für das
Abschmelzmodell des Bestandsschutz-Zuschusses.

## Summen

| Gruppe | Renten |
| --- | ---: |
| erwerbsminderungsrente | 1.747.402 |
| altersrente | 18.919.641 |
| hinterbliebenenrente | 5.420.619 |
| gesamt | 26.087.662 |

## Hinweise

- Altersrenten und Erwerbsminderungsrenten sind nach Geschlecht getrennt.
- Hinterbliebenenrenten werden über Witwen-/Witwerrenten geschlechtsnah zugeordnet; Waisen- und Erziehungsrenten bleiben `unbekannt`.
- Knappschaft-Bahn-See ist im Tabellenband nur aggregiert nach Träger übernommen, nicht alters- und geschlechtsspezifisch.
- `100 und älter` beziehungsweise `105 und älter` werden als offene Altersgruppen für die Tail-Regel markiert.
