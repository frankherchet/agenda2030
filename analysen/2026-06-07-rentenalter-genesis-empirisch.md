---
title: Empirisches Rentenaltermodell mit GENESIS-Altersjahrgaengen
date: 2026-06-07
type: analyse
status: arbeitsfassung
publish: false
source_urls:
  - https://genesis.destatis.de/genesisWS/swagger-ui/index.html
ingest_refs:
  - ingest/links/2026-06-06-destatis-genesis-api.md
  - ingest/dokumente/2026-06-07-destatis-genesis-demographie-rente-tabellen.md
data_artifacts:
  - analysen/daten/2026-06-07-rentenalter-genesis-empirisch-altersjahre.csv
  - analysen/daten/2026-06-07-rentenalter-genesis-empirisch-summary.csv
scripts:
  - scripts/calc_rentenalter_genesis_empirisch.py
related_projects:
  - projekte/rentenversicherung/reformkonzept.md
---

# Empirisches Rentenaltermodell mit GENESIS-Altersjahrgaengen

## Zweck

Diese Analyse ersetzt im Rentenalterblock die pauschale
`0,95 Mio. je Altersjahr`-Kohorte durch amtliche GENESIS-Altersjahrgaenge
aus der 16. koordinierten Bevoelkerungsvorausberechnung.

## Datenbasis

- `12411-0005`: Bevoelkerung Deutschland nach Altersjahren bis 31.12.2024.
- `12421-0002`: vorausberechneter Bevoelkerungsstand Deutschland nach
  Altersjahren, Geschlecht und Variante bis 31.12.2070.
- `12211-0002`: Mikrozensus 2025, Erwerbstaetige und Erwerbspersonen
  in Hauptwohnsitzhaushalten nach Altersgruppen.

## Brueckenparameter Erwerb

- Erwerbstaetigenquote 65+: 10.2 %. 
- Erwerbspersonenquote 65+: 10.4 %. 
- Senior-Wage-Faktor: 0,85 als konservativer Abschlag auf volle
  Beitragswirkung.

Die Altersjahrgaenge sind damit empirisch. Die Erwerbsquote bleibt
mangels oeffentlich gefundener feinjaehriger GENESIS-Erwerbsquoten ein
transparenter Brueckenparameter aus der amtlichen Altersgruppe `65 Jahre
und mehr`.

## Ergebnis

| Jahr | Variante | Rentenalter | Nicht in Rente Mio. | Effektive Beitragszahler Mio. |
| ---: | --- | --- | ---: | ---: |
| 2035 | moderat | status_quo_67 (67.000) | 0.000 | 0.000 |
| 2035 | moderat | lebenserwartung_2zu1 (68.000) | 2.403 | 0.209 |
| 2035 | moderat | daenemarknah (69.000) | 4.826 | 0.419 |
| 2039 | moderat | status_quo_67 (67.000) | 0.000 | 0.000 |
| 2039 | moderat | lebenserwartung_2zu1 (68.400) | 2.731 | 0.237 |
| 2039 | moderat | daenemarknah (69.800) | 5.658 | 0.491 |
| 2050 | moderat | status_quo_67 (67.000) | 0.000 | 0.000 |
| 2050 | moderat | lebenserwartung_2zu1 (69.500) | 5.044 | 0.438 |
| 2050 | moderat | daenemarknah (70.667) | 7.334 | 0.637 |
| 2070 | moderat | status_quo_67 (67.000) | 0.000 | 0.000 |
| 2070 | moderat | lebenserwartung_2zu1 (71.500) | 8.459 | 0.734 |
| 2070 | moderat | daenemarknah (72.000) | 9.422 | 0.818 |

## Sensitivitaet 2070

| Variante | Szenario | Nicht in Rente Mio. | Effektive Beitragszahler Mio. |
| --- | --- | ---: | ---: |
| relativ alte Bevoelkerung | lebenserwartung_2zu1 | 8.133 | 0.706 |
| relativ alte Bevoelkerung | daenemarknah | 9.074 | 0.788 |
| Geburtenrate, Lebenserwartung und Wanderungssaldo moderat | lebenserwartung_2zu1 | 8.459 | 0.734 |
| Geburtenrate, Lebenserwartung und Wanderungssaldo moderat | daenemarknah | 9.422 | 0.818 |
| relativ junge Bevoelkerung | lebenserwartung_2zu1 | 8.741 | 0.759 |
| relativ junge Bevoelkerung | daenemarknah | 9.721 | 0.844 |

## Einordnung

Der fruehere Prüferblocker `synthetische Altersjahrkohorten` ist damit
fuer die Bevoelkerungsseite bearbeitet: die betroffenen Jahrgaenge
67 bis 72 stammen aus GENESIS. Nicht vollstaendig erledigt ist die
Arbeitsmarktseite, weil GENESIS in der oeffentlichen Suche keine
feinjaehrigen Erwerbsquoten fuer 67 bis 72 geliefert hat. Fuer eine
Freigabe sollte entweder ein Mikrozensus-Sondertabellenzugang,
DRV-Rentenzugangsdaten oder eine andere amtliche Quelle fuer
altersscharfe Erwerbsbeteiligung ergaenzt werden.
