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
- `12211-0004`: Mikrozensus 2025, Erwerbstaetige nach Geschlecht,
  Altersgruppen und Stellung im Beruf.

## Brueckenparameter Erwerb

- Erwerbstaetigenquote 65 bis unter 75: 16.5 %.
- Vergleichswert Erwerbstaetigenquote 65+: 10.2 %.
- Erwerbspersonenquote 65+: 10.4 %.
- Senior-Wage-Faktor: 0,85 als konservativer Abschlag auf volle
  Beitragswirkung.

Die Altersjahrgaenge sind damit empirisch. Die Erwerbsquote bleibt
mangels oeffentlich gefundener feinjaehriger GENESIS-Erwerbsquoten ein
transparenter Brueckenparameter. Gegenueber der Vorfassung wird nicht
mehr `65 Jahre und mehr`, sondern die naehere amtliche Gruppe
`65 bis unter 75 Jahre` verwendet.

## Ergebnis

| Jahr | Variante | Rentenalter | Nicht in Rente Mio. | Effektive Beitragszahler Mio. |
| ---: | --- | --- | ---: | ---: |
| 2035 | moderat | status_quo_67 (67.000) | 0.000 | 0.000 |
| 2035 | moderat | lebenserwartung_2zu1 (68.000) | 1.201 | 0.169 |
| 2035 | moderat | daenemarknah (69.000) | 2.413 | 0.339 |
| 2039 | moderat | status_quo_67 (67.000) | 0.000 | 0.000 |
| 2039 | moderat | lebenserwartung_2zu1 (68.400) | 1.365 | 0.192 |
| 2039 | moderat | daenemarknah (69.800) | 2.829 | 0.397 |
| 2050 | moderat | status_quo_67 (67.000) | 0.000 | 0.000 |
| 2050 | moderat | lebenserwartung_2zu1 (69.500) | 2.522 | 0.354 |
| 2050 | moderat | daenemarknah (70.667) | 3.667 | 0.515 |
| 2070 | moderat | status_quo_67 (67.000) | 0.000 | 0.000 |
| 2070 | moderat | lebenserwartung_2zu1 (71.500) | 4.230 | 0.594 |
| 2070 | moderat | daenemarknah (72.000) | 4.711 | 0.662 |

## Sensitivitaet 2070

| Variante | Szenario | Nicht in Rente Mio. | Effektive Beitragszahler Mio. |
| --- | --- | ---: | ---: |
| relativ alte Bevoelkerung | lebenserwartung_2zu1 | 4.067 | 0.571 |
| relativ alte Bevoelkerung | daenemarknah | 4.537 | 0.637 |
| Geburtenrate, Lebenserwartung und Wanderungssaldo moderat | lebenserwartung_2zu1 | 4.230 | 0.594 |
| Geburtenrate, Lebenserwartung und Wanderungssaldo moderat | daenemarknah | 4.711 | 0.662 |
| relativ junge Bevoelkerung | lebenserwartung_2zu1 | 4.370 | 0.614 |
| relativ junge Bevoelkerung | daenemarknah | 4.861 | 0.683 |

## Einordnung

Der fruehere Prüferblocker `synthetische Altersjahrkohorten` ist damit
fuer die Bevoelkerungsseite bearbeitet: die betroffenen Jahrgaenge
67 bis 72 stammen aus GENESIS. Die Korrektur vom 2026-06-07 nutzt in
`12421-0002` ausschliesslich die Geschlechtszeile `Insgesamt`; die
Vorfassung hatte maennlich, weiblich und Insgesamt zusammengezählt.
Nicht vollstaendig erledigt ist die Arbeitsmarktseite, weil GENESIS
oeffentlich keine feinjaehrigen Erwerbsquoten fuer 67 bis 72 liefert.
Fuer eine Freigabe sollte entweder ein Mikrozensus-Sondertabellenzugang,
DRV-Rentenzugangsdaten oder eine andere amtliche Quelle fuer
altersscharfe Erwerbsbeteiligung ergaenzt werden.
