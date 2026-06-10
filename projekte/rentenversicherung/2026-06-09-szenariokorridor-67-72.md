---
title: Szenariokorridor Rentenzugang 67-72 Jahre (Arbeitsfassung)
date: 2026-06-09
type: reformmodell
status: arbeitsfassung
publish: false
source_urls:
  - https://www.deutsche-rentenversicherung.de/SharedDocs/Downloads/DE/Statistiken-und-Berichte/statistikpublikationen/statistikband_rente.pdf?__blob=publicationFile&v=5
  - https://statistik-rente.de/drv/extern/rente/rentenbestand/
  - https://www.bmas.de/SharedDocs/Downloads/DE/Rente/rentenversicherungsbericht-2025.pdf?__blob=publicationFile&v=3
ingest_refs:
  - ingest/dokumente/2026-06-04-drv-statistikband-rente-2024.md
  - ingest/links/2026-06-04-statistik-rente-rentenbestand.md
  - ingest/dokumente/2026-06-05-bmas-rentenversicherungsbericht-2025.md
data_artifacts:
  - analysen/daten/drv_rentenzugang_67-72_final.csv
related_project:
  - projekte/rentenversicherung/reformkonzept.md
---

# Szenariokorridor Rentenzugang 67-72 Jahre

## Status

Arbeitsfassung mit heuristischer Datenbruecke. Die Datei bildet keine
amtlichen Erwerbsquoten ab, sondern einen Szenariokorridor fuer
Rentenzugangsarten und Abschlaege auf Basis vorhandener DRV-/BMAS-Quellen und
einer abgeleiteten CSV-Arbeitsdatei.

## Datengrundlage

- Arbeitsdatei: `analysen/daten/drv_rentenzugang_67-72_final.csv`
- Quellenbasis: DRV-Statistikband, statistik-rente.de, BMAS
  Rentenversicherungsbericht 2025
- Methodik: keine amtliche Rentenzugangsstatistik 67 bis 72 im Repo
  vorhanden; die CSV ist daher eine heuristische Bruecke fuer die
  Sensitivitaet, keine freigabefaehige Enddatengrundlage

## Kernerkenntnisse aus der Arbeitsdatei

- Ab 70 Jahren steigt der Anteil der Erwerbsminderungsrente deutlich.
- Der Anteil klassischer Altersrenten sinkt mit zunehmendem Alter.
- Durchschnittliche Abschlaege steigen in der Arbeitsdatei moderat an.

## Sensitivitätsanalyse (drei Szenarien)

| Alter | Niedrig (pessimistisch) | Mittel (Basis) | Hoch (optimistisch) | Auswirkung auf Kosten |
|-------|--------------------------|----------------|---------------------|-----------------------|
| 67    | 42 %                    | 48 %           | 54 %                | +3,2 % / -2,8 %       |
| 68    | 35 %                    | 42 %           | 49 %                | +4,1 % / -3,5 %       |
| 69    | 28 %                    | 35 %           | 42 %                | +5,0 % / -4,2 %       |
| 70    | 22 %                    | 29 %           | 36 %                | +6,8 % / -5,1 %       |
| 71    | 17 %                    | 24 %           | 31 %                | +7,9 % / -5,8 %       |
| 72    | 13 %                    | 20 %           | 27 %                | +9,2 % / -6,4 %       |

Das Mittel-Szenario dient als Basissensitivitaet fuer die weitere
Reformdiskussion, nicht als abschliessend validierte Parameterisierung.

## Auswirkung auf das Reformmodell

Die bisherige Vorstellung eines relativ stabilen Altersrentenanteils ab 67
ist fuer die Arbeitsrechnung zu eng. Wenn ab hoeheren Altern mehr
Erwerbsminderungsfaelle und andere Rentenzugangsarten auftreten, veraendert
das Kostenbild und die Abschlagslogik.

## Offener Punkt

Der Szenariokorridor ist erst dann freigabefaehig, wenn die heuristische
Arbeitsdatei durch echte DRV-Rentenzugangsdaten ersetzt oder gegen solche
validiert wird.
