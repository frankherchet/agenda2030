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
  bestehenden Zukunftsmodell; Neubeamte wirken darin ab 2030 als zusätzliche Beitragsbasis und spätere Rentenlast.
- Bundesmittel: 2027-2029 Brückenphase, danach abschmelzender Bestandsschutz-Zuschuss für Altlasten.
- Beitragssatz-Korridore: 20 %, 22 % und 24 %.
- Leistungsfaktor: maximal finanzierbares Ausgabenvolumen geteilt durch
  Referenzausgaben des bisherigen Rentenpfads.
- Brückenjahre 2027-2029 sind modelliert, aber noch nicht reformwirksam.

## Kernergebnis moderate Variante

| Korridor | Jahr | leistbares Volumen | Referenzausgaben | Leistungsfaktor | Luecke vs. Referenz |
| --- | ---: | ---: | ---: | ---: | ---: |
| ziel_20_prozent | 2030 | 481,0 Mrd. Euro | 494,3 Mrd. Euro | 97,3 % | 13,3 Mrd. Euro |
| ziel_20_prozent | 2035 | 514,9 Mrd. Euro | 611,1 Mrd. Euro | 84,3 % | 96,3 Mrd. Euro |
| ziel_20_prozent | 2039 | 533,7 Mrd. Euro | 711,8 Mrd. Euro | 75,0 % | 178,1 Mrd. Euro |
| ziel_20_prozent | 2050 | 628,6 Mrd. Euro | 914,8 Mrd. Euro | 68,7 % | 286,2 Mrd. Euro |
| ziel_20_prozent | 2070 | 940,1 Mrd. Euro | 1443,7 Mrd. Euro | 65,1 % | 503,7 Mrd. Euro |
| stabil_22_prozent | 2030 | 518,9 Mrd. Euro | 494,3 Mrd. Euro | 105,0 % | -24,6 Mrd. Euro |
| stabil_22_prozent | 2035 | 558,4 Mrd. Euro | 611,1 Mrd. Euro | 91,4 % | 52,7 Mrd. Euro |
| stabil_22_prozent | 2039 | 580,8 Mrd. Euro | 711,8 Mrd. Euro | 81,6 % | 131,0 Mrd. Euro |
| stabil_22_prozent | 2050 | 688,7 Mrd. Euro | 914,8 Mrd. Euro | 75,3 % | 226,1 Mrd. Euro |
| stabil_22_prozent | 2070 | 1032,9 Mrd. Euro | 1443,7 Mrd. Euro | 71,5 % | 410,8 Mrd. Euro |
| obergrenze_24_prozent | 2030 | 556,9 Mrd. Euro | 494,3 Mrd. Euro | 112,7 % | -62,6 Mrd. Euro |
| obergrenze_24_prozent | 2035 | 602,0 Mrd. Euro | 611,1 Mrd. Euro | 98,5 % | 9,1 Mrd. Euro |
| obergrenze_24_prozent | 2039 | 627,9 Mrd. Euro | 711,8 Mrd. Euro | 88,2 % | 83,9 Mrd. Euro |
| obergrenze_24_prozent | 2050 | 748,8 Mrd. Euro | 914,8 Mrd. Euro | 81,9 % | 166,0 Mrd. Euro |
| obergrenze_24_prozent | 2070 | 1125,7 Mrd. Euro | 1443,7 Mrd. Euro | 78,0 % | 318,0 Mrd. Euro |

## Szenariovergleich 2070

| Szenario | 20 % | 22 % | 24 % |
| --- | ---: | ---: | ---: |
| jung | 74,5 % | 81,9 % | 89,3 % |
| moderat | 65,1 % | 71,5 % | 78,0 % |
| alt | 56,4 % | 62,0 % | 67,6 % |

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
