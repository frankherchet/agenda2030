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
  bestehenden Zukunftsmodell; Neubeamte wirken darin ab 2030 als zusätzliche Beitragsbasis und spätere Rentenlast, unterstellt mit 0,8-Nachbesetzungsquote.
- Bundesmittel: 2027-2029 Brückenphase, danach abschmelzender Bestandsschutz-Zuschuss für Altlasten.
- Beitragssatz-Korridore: 20 %, 22 % und 24 %.
- Leistungsfaktor: maximal finanzierbares Ausgabenvolumen geteilt durch
  Referenzausgaben des bisherigen Rentenpfads.
- Brückenjahre 2027-2029 sind modelliert, aber noch nicht reformwirksam.

## Kernergebnis moderate Variante

| Korridor | Jahr | leistbares Volumen | Referenzausgaben | Leistungsfaktor | Luecke vs. Referenz |
| --- | ---: | ---: | ---: | ---: | ---: |
| ziel_20_prozent | 2030 | 480,9 Mrd. Euro | 494,3 Mrd. Euro | 97,3 % | 13,4 Mrd. Euro |
| ziel_20_prozent | 2035 | 514,3 Mrd. Euro | 611,1 Mrd. Euro | 84,2 % | 96,8 Mrd. Euro |
| ziel_20_prozent | 2039 | 532,7 Mrd. Euro | 711,8 Mrd. Euro | 74,8 % | 179,1 Mrd. Euro |
| ziel_20_prozent | 2050 | 626,0 Mrd. Euro | 914,8 Mrd. Euro | 68,4 % | 288,8 Mrd. Euro |
| ziel_20_prozent | 2070 | 932,8 Mrd. Euro | 1443,7 Mrd. Euro | 64,6 % | 511,0 Mrd. Euro |
| stabil_22_prozent | 2030 | 518,8 Mrd. Euro | 494,3 Mrd. Euro | 105,0 % | -24,5 Mrd. Euro |
| stabil_22_prozent | 2035 | 557,8 Mrd. Euro | 611,1 Mrd. Euro | 91,3 % | 53,3 Mrd. Euro |
| stabil_22_prozent | 2039 | 579,7 Mrd. Euro | 711,8 Mrd. Euro | 81,4 % | 132,1 Mrd. Euro |
| stabil_22_prozent | 2050 | 685,8 Mrd. Euro | 914,8 Mrd. Euro | 75,0 % | 229,0 Mrd. Euro |
| stabil_22_prozent | 2070 | 1024,9 Mrd. Euro | 1443,7 Mrd. Euro | 71,0 % | 418,9 Mrd. Euro |
| obergrenze_24_prozent | 2030 | 556,8 Mrd. Euro | 494,3 Mrd. Euro | 112,6 % | -62,4 Mrd. Euro |
| obergrenze_24_prozent | 2035 | 601,3 Mrd. Euro | 611,1 Mrd. Euro | 98,4 % | 9,8 Mrd. Euro |
| obergrenze_24_prozent | 2039 | 626,7 Mrd. Euro | 711,8 Mrd. Euro | 88,0 % | 85,1 Mrd. Euro |
| obergrenze_24_prozent | 2050 | 745,6 Mrd. Euro | 914,8 Mrd. Euro | 81,5 % | 169,2 Mrd. Euro |
| obergrenze_24_prozent | 2070 | 1117,0 Mrd. Euro | 1443,7 Mrd. Euro | 77,4 % | 326,8 Mrd. Euro |

## Szenariovergleich 2070

| Szenario | 20 % | 22 % | 24 % |
| --- | ---: | ---: | ---: |
| jung | 74,0 % | 81,3 % | 88,6 % |
| moderat | 64,6 % | 71,0 % | 77,4 % |
| alt | 56,0 % | 61,5 % | 67,0 % |

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
