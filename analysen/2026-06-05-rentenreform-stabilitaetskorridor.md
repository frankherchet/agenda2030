---
title: Rentenreform Stabilitaetskorridor
date: 2026-06-05
type: analyse
status: arbeitsfassung
source_urls:
  - https://www.deutsche-rentenversicherung.de/DRV/DE/Experten/Zahlen-und-Fakten/Kennzahlen-zur-Finanzentwicklung/kennzahlen-zur-finanzentwicklung_node.html?https=1
  - https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsvorausberechnung/annahmen_ergebnisse_16te_kBv.html
  - https://www.bmas.de/SharedDocs/Downloads/DE/Rente/rentenversicherungsbericht-2025.pdf?__blob=publicationFile&v=3
ingest_refs:
  - ingest/links/2026-06-04-drv-finanzkennzahlen-rentenversicherung.md
  - ingest/dokumente/2026-06-04-destatis-demographie.md
  - ingest/dokumente/2026-06-05-bmas-rentenversicherungsbericht-2025.md
data_artifacts:
  - analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor.csv
  - analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor-annahmen.csv
scripts:
  - scripts/calc_rentenreform_stabilitaetskorridor.py
related_projects:
  - projekte/rentenversicherung/reformkonzept.md
---

# Rentenreform Stabilitaetskorridor

Reproduzierbar mit:

```bash
python3 scripts/calc_rentenreform_stabilitaetskorridor.py
```

## Zweck

Diese Analyse berechnet, wie viel Rentenvolumen maximal finanzierbar ist,
wenn die Reform rein umlagefinanziert bleibt, neue Entgeltpunkte nur aus
Einzahlungen entstehen und der Beitragssatz politisch stabil gehalten
werden soll.

## Modell

- Beitragsbasis: Status quo plus schrittweise Erwerbstätigenbasis aus dem
  bestehenden Zukunftsmodell; Neubeamte wirken darin als zusätzliche Beitragsbasis und spätere Rentenlast.
- Bundesmittel: nur abschmelzender Bestandsschutz-Zuschuss für Altlasten.
- Beitragssatz-Korridore: 20 %, 22 % und 24 %.
- Leistungsfaktor: maximal finanzierbares Ausgabenvolumen geteilt durch
  Referenzausgaben des bisherigen Rentenpfads.

## Kernergebnis moderate Variante

| Korridor | Jahr | leistbares Volumen | Referenzausgaben | Leistungsfaktor | Luecke vs. Referenz |
| --- | ---: | ---: | ---: | ---: | ---: |
| ziel_20_prozent | 2035 | 502,6 Mrd. Euro | 611,1 Mrd. Euro | 82,2 % | 108,6 Mrd. Euro |
| ziel_20_prozent | 2039 | 522,6 Mrd. Euro | 711,8 Mrd. Euro | 73,4 % | 189,1 Mrd. Euro |
| ziel_20_prozent | 2050 | 621,8 Mrd. Euro | 914,8 Mrd. Euro | 68,0 % | 293,0 Mrd. Euro |
| ziel_20_prozent | 2070 | 939,7 Mrd. Euro | 1443,7 Mrd. Euro | 65,1 % | 504,0 Mrd. Euro |
| stabil_22_prozent | 2035 | 546,2 Mrd. Euro | 611,1 Mrd. Euro | 89,4 % | 64,9 Mrd. Euro |
| stabil_22_prozent | 2039 | 569,8 Mrd. Euro | 711,8 Mrd. Euro | 80,1 % | 142,0 Mrd. Euro |
| stabil_22_prozent | 2050 | 681,9 Mrd. Euro | 914,8 Mrd. Euro | 74,5 % | 232,9 Mrd. Euro |
| stabil_22_prozent | 2070 | 1032,5 Mrd. Euro | 1443,7 Mrd. Euro | 71,5 % | 411,2 Mrd. Euro |
| obergrenze_24_prozent | 2035 | 589,8 Mrd. Euro | 611,1 Mrd. Euro | 96,5 % | 21,3 Mrd. Euro |
| obergrenze_24_prozent | 2039 | 616,9 Mrd. Euro | 711,8 Mrd. Euro | 86,7 % | 94,9 Mrd. Euro |
| obergrenze_24_prozent | 2050 | 741,9 Mrd. Euro | 914,8 Mrd. Euro | 81,1 % | 172,9 Mrd. Euro |
| obergrenze_24_prozent | 2070 | 1125,4 Mrd. Euro | 1443,7 Mrd. Euro | 77,9 % | 318,4 Mrd. Euro |

## Szenariovergleich 2070

| Szenario | 20 % | 22 % | 24 % |
| --- | ---: | ---: | ---: |
| jung | 74,5 % | 81,9 % | 89,2 % |
| moderat | 65,1 % | 71,5 % | 77,9 % |
| alt | 56,4 % | 62,0 % | 67,5 % |

## Interpretation

Im moderaten Szenario finanziert ein 22-%-Korridor 2035 rund 89 %
des Referenzpfads, 2039 rund 80 %, 2050 rund 75 % und 2070 rund
72 %. Ein 24-%-Korridor verbessert die Lage, reicht aber 2070 im
moderaten Szenario nur für rund 78 % des Referenzpfads.

Folgerung für das Reformkonzept: Eine hohe Rente bei stabilen
Beitragssätzen braucht eine automatische Budgetregel. Innerhalb des
Beitragssatzkorridors wird der Rentenwert so hoch wie möglich gesetzt;
neue Entgeltpunkte entstehen nur durch Beiträge. Politische
Rentenwirkungen müssen durch echte Beiträge öffentlicher Träger
finanziert werden und dürfen den Korridor nicht verdeckt belasten.
