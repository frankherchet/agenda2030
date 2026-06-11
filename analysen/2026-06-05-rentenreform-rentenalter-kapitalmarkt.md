---
title: Rentenreform Rentenalter-Kopplung und Kapitalmarktbaustein
date: 2026-06-05
type: analyse
status: arbeitsfassung
source_urls:
  - https://www.pensionsmyndigheten.se/other-languages/english-engelska/english-engelska/retirement-age
  - https://www.etk.fi/en/finnish-pension-system/pensions/determining-the-life-expectancy-coefficient-and-retirement-age/determining-the-retirement-age-for-the-old-age-pension/
  - https://bm.dk/nyheder/pressemeddelelser/2025/05/forhoejelse-af-folkepensionsalderen-i-2040-sikrer-velfaerden
  - https://star.dk/da/ydelser/pension-og-efterloen/folkepension-tidlig-pension-foertidspension-og-seniorpension/folkepension/folkepensionsalderen-nu-og-fremover/
  - https://www.pensionsmyndigheten.se/forsta-din-pension/valj-och-byt-fonder/forvalet-ap7safa
  - https://www.ap7.se/english/ap7-safa/
  - https://www.msci.com/World
  - https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/12/oecd-pensions-outlook-2024_6ac7d5fd/51510909-en.pdf
ingest_refs:
  - ingest/links/2026-06-05-schweden-richtalter-rente-lebenserwartung.md
  - ingest/links/2026-06-05-finnland-rentenalter-lebenserwartung.md
  - ingest/links/2026-06-05-daenemark-folkepensionsalter-lebenserwartung.md
  - ingest/links/2026-06-05-schweden-ap7-safa-premium-pension.md
  - ingest/links/2026-06-05-msci-world-index.md
  - ingest/dokumente/2026-06-05-oecd-pensions-outlook-2024-kapitalmarkt-defaults.md
data_artifacts:
  - analysen/daten/2026-06-05-rentenreform-rentenalter-kapital.csv
  - analysen/daten/2026-06-05-rentenreform-rentenalter-kapital-annahmen.csv
  - analysen/daten/2026-06-05-rentenreform-kapitalmarktbaustein.csv
scripts:
  - scripts/calc_rentenreform_rentenalter_kapital.py
related_projects:
  - projekte/rentenversicherung/reformkonzept.md
---

# Rentenreform Rentenalter-Kopplung und Kapitalmarktbaustein

Reproduzierbar mit:

```bash
python3 scripts/calc_rentenreform_rentenalter_kapital.py
```

## Zweck

Diese Analyse ergaenzt das Reformkonzept um zwei Szenarien: spaeterer
Renteneintritt durch Kopplung an die Lebenserwartung und ein zusaetzlicher
kapitalgedeckter Baustein nach schwedisch inspiriertem Default-Modell.
Die Modelljahre 2027 bis 2029 sind Brückenjahre; die Reform wirkt ab 1.1.2030.

## Renteneintrittsalter-Szenarien

| Szenario | Logik |
| --- | --- |
| status_quo_67 | Regelaltersgrenze bleibt modellhaft bei 67. |
| finnland_ratio_light | Langsame Kopplung: 68 ab 2035, 69 ab 2045, 70 ab 2055, 71 ab 2065. |
| daenemark_2040 | Harte Kopplung: 68 ab 2030, 69 ab 2035, 70 ab 2040, 72 bis 2070. |

## Beitragssatzwirkung im moderaten Demographieszenario

| Jahr | Status quo 67 | Finnland-nahe Kopplung | Daenemark-nahe Kopplung |
| ---: | ---: | ---: | ---: |
| 2030 | 20,7 % | 20,1 % | 19,0 % |
| 2035 | 24,5 % | 22,7 % | 21,0 % |
| 2039 | 27,6 % | 25,0 % | 22,5 % |
| 2040 | 27,9 % | 25,0 % | 22,4 % |
| 2050 | 29,7 % | 24,9 % | 22,8 % |
| 2060 | 30,6 % | 23,9 % | 22,4 % |
| 2070 | 31,2 % | 23,3 % | 21,6 % |

## Kapitalmarktbaustein

Der Kapitalmarktbaustein wird als zusaetzlicher Beitrag gerechnet. Eine
Umleitung bestehender Umlagebeitraege wuerde die heutige Rentenkasse
zunaechst schwaechen und passt deshalb nicht zum Ziel stabiler
Beitragssaetze.

| Zusatzbeitrag | reale Rendite | Kapital nach 40 Jahren | Zusatzrente pro Monat, 20 Jahre |
| ---: | ---: | ---: | ---: |
| 1,0 % | 1,0 % | 25393,54 Euro | 117,27 Euro |
| 1,0 % | 3,0 % | 39166,43 Euro | 219,38 Euro |
| 1,0 % | 5,0 % | 62748,23 Euro | 419,59 Euro |
| 2,0 % | 1,0 % | 50787,08 Euro | 234,53 Euro |
| 2,0 % | 3,0 % | 78332,86 Euro | 438,77 Euro |
| 2,0 % | 5,0 % | 125496,47 Euro | 839,18 Euro |
| 3,0 % | 1,0 % | 76180,61 Euro | 351,80 Euro |
| 3,0 % | 3,0 % | 117499,29 Euro | 658,15 Euro |
| 3,0 % | 5,0 % | 188244,70 Euro | 1258,77 Euro |

## Einordnung

- Eine Lebenserwartungs-Kopplung verbessert die Umlage deutlich, weil sie
  gleichzeitig Ausgaben senkt und Beitragsjahre erhoeht. Sie ersetzt aber
  keine breite Beitragsbasis und keine Budgetregel.
- Eine daenemarknahe harte Kopplung wirkt staerker, ist aber sozial
  konflikttraechtiger und braucht Schutzregeln fuer lange Versicherungszeiten
  und gesundheitlich belastende Arbeit.
- Ein Kapitalmarktbaustein kann individuelle Zusatzrente schaffen, muss aber
  als Zusatzbeitrag, mit niedrigem Kostenlimit, breiter Streuung,
  Lebenszyklus-Default und klarer Auszahlungsphase geregelt werden.
- MSCI World ist eine moegliche Benchmark fuer entwickelte Maerkte, aber kein
  Produkt. Fuer einen deutschen Default waere auch ein breiterer All-World-
  Ansatz inklusive Schwellenlaender zu pruefen.
