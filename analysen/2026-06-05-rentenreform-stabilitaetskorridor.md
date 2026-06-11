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
  bestehenden Zukunftsmodell; Neubeamte wirken darin ab 2030 als zusätzliche Beitragsbasis und spätere Rentenlast, unterstellt mit 0,75-Nachbesetzungsquote.
- Bundesmittel: 2027-2029 Brückenphase, danach abschmelzender Bestandsschutz-Zuschuss für Altlasten.
- Beitragssatz-Korridore: 20 %, 22 % und 24 %.
- Leistungsfaktor: maximal finanzierbares Ausgabenvolumen geteilt durch
  Referenzausgaben des bisherigen Rentenpfads.
- Brückenjahre 2027-2029 sind modelliert, aber noch nicht reformwirksam.

## Kernergebnis moderate Variante

| Korridor | Jahr | leistbares Volumen | Referenzausgaben | Leistungsfaktor | Luecke vs. Referenz |
| --- | ---: | ---: | ---: | ---: | ---: |
| ziel_20_prozent | 2030 | 480,9 Mrd. Euro | 494,3 Mrd. Euro | 97,3 % | 13,5 Mrd. Euro |
| ziel_20_prozent | 2035 | 514,2 Mrd. Euro | 611,1 Mrd. Euro | 84,1 % | 97,0 Mrd. Euro |
| ziel_20_prozent | 2039 | 532,4 Mrd. Euro | 711,8 Mrd. Euro | 74,8 % | 179,3 Mrd. Euro |
| ziel_20_prozent | 2050 | 625,4 Mrd. Euro | 914,8 Mrd. Euro | 68,4 % | 289,4 Mrd. Euro |
| ziel_20_prozent | 2070 | 930,9 Mrd. Euro | 1443,7 Mrd. Euro | 64,5 % | 512,8 Mrd. Euro |
| stabil_22_prozent | 2030 | 518,8 Mrd. Euro | 494,3 Mrd. Euro | 105,0 % | -24,5 Mrd. Euro |
| stabil_22_prozent | 2035 | 557,7 Mrd. Euro | 611,1 Mrd. Euro | 91,3 % | 53,5 Mrd. Euro |
| stabil_22_prozent | 2039 | 579,4 Mrd. Euro | 711,8 Mrd. Euro | 81,4 % | 132,4 Mrd. Euro |
| stabil_22_prozent | 2050 | 685,1 Mrd. Euro | 914,8 Mrd. Euro | 74,9 % | 229,7 Mrd. Euro |
| stabil_22_prozent | 2070 | 1022,9 Mrd. Euro | 1443,7 Mrd. Euro | 70,8 % | 420,9 Mrd. Euro |
| obergrenze_24_prozent | 2030 | 556,7 Mrd. Euro | 494,3 Mrd. Euro | 112,6 % | -62,4 Mrd. Euro |
| obergrenze_24_prozent | 2035 | 601,2 Mrd. Euro | 611,1 Mrd. Euro | 98,4 % | 9,9 Mrd. Euro |
| obergrenze_24_prozent | 2039 | 626,4 Mrd. Euro | 711,8 Mrd. Euro | 88,0 % | 85,4 Mrd. Euro |
| obergrenze_24_prozent | 2050 | 744,9 Mrd. Euro | 914,8 Mrd. Euro | 81,4 % | 169,9 Mrd. Euro |
| obergrenze_24_prozent | 2070 | 1114,8 Mrd. Euro | 1443,7 Mrd. Euro | 77,2 % | 328,9 Mrd. Euro |

## Szenariovergleich 2070

| Szenario | 20 % | 22 % | 24 % |
| --- | ---: | ---: | ---: |
| jung | 73,8 % | 81,1 % | 88,4 % |
| moderat | 64,5 % | 70,8 % | 77,2 % |
| alt | 55,9 % | 61,4 % | 66,9 % |

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
