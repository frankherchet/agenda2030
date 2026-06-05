---
title: Abschmelzmodell Bestandsschutz-Zuschuss Rentenversicherung
date: 2026-06-04
type: analyse
status: offen
source_urls:
  - https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Sterbefaelle-Lebenserwartung/Publikationen/_publikationen-innen-periodensterbetafel.html
  - https://www.deutsche-rentenversicherung.de/SharedDocs/Downloads/DE/Statistiken-und-Berichte/statistikpublikationen/statistikband_rente.pdf?__blob=publicationFile&v=5
  - https://www.deutsche-rentenversicherung.de/DRV/DE/Experten/Zahlen-und-Fakten/Kennzahlen-zur-Finanzentwicklung/kennzahlen-zur-finanzentwicklung_node.html?https=1
ingest_refs:
  - ingest/links/2026-06-04-destatis-periodensterbetafeln-publikationen.md
  - ingest/dokumente/2026-06-04-destatis-sterbetafeln-2022-2024.md
  - ingest/dokumente/2026-06-04-drv-statistikband-rente-2024.md
  - ingest/links/2026-06-04-drv-finanzkennzahlen-rentenversicherung.md
data_artifacts:
  - analysen/daten/2026-06-04-drv-rentenbestand-struktur.csv
  - analysen/daten/2026-06-04-bundesmittel-zerlegung.csv
  - analysen/daten/2026-06-04-bundeszuschuss-abschmelzung.csv
scripts:
  - scripts/build_drv_renten_inputs.py
  - scripts/calc_rente_bundeszuschuss_abschmelzung.py
---

# Abschmelzmodell Bestandsschutz-Zuschuss Rentenversicherung

Stand: 2026-06-04

Reproduzierbar mit:

```bash
python3 scripts/build_drv_renten_inputs.py
python3 scripts/calc_rente_bundeszuschuss_abschmelzung.py
```

## Zweck

Diese Analyse modelliert, wie ein Bestandsschutz-Zuschuss für bereits
erworbene Rentenansprüche anhand der erwarteten Überlebendenzahl der
Bestandskohorte abschmelzen kann.

## Eingaben

- Reformstichtag: 2027
- Abschmelzbarer Startwert Bundesmittel 2025: 97,858 Mrd. Euro
- Modellierte laufende Renten aus DRV-Rentenbestand 2024: 26.086.937 Renten
- Nicht modellierte Restzeilen ohne Alter: 725 Renten
- Rentenbestandsstruktur: `analysen/daten/2026-06-04-drv-rentenbestand-struktur.csv`
- Bundesmittel-Zerlegung: `analysen/daten/2026-06-04-bundesmittel-zerlegung.csv`
- Quelle Sterblichkeit: `ingest/originale/2026-06-04-destatis-sterbetafeln-2022-2024.xlsx`
- Verwendete Tabellen: `12613-b01` männlich, `12613-b02` weiblich
- Verwendete Größen: `Überlebende - lx` und `Überlebenswahrscheinlichkeit - px` bei Alter 100
- Offene Altersgruppen: `100 und älter` und `105 und älter` werden ab dem Gruppenstart mit der Destatis-Überlebenswahrscheinlichkeit bei Alter 100 fortgeschrieben.
- Waisen- und Erziehungsrenten: mangels Geschlechtstrennung im DRV-Tabellenband je hälftig männlich/weiblich modelliert.
- Knappschaft-Bahn-See: als eigene aggregierte Trägergruppe erfasst; nicht zusätzlich modelliert, weil ihre Renten bereits in `rv_gesamt` enthalten sind.

## Modellregel

`Bestandsschutz-Zuschuss(t) = abschmelzbarer Startwert * erwartete Überlebendenzahl Bestandskohorte(t) / Bestandskohorte(2027)`

Politische Sonderkürzungen sind in diesem Modell ausgeschlossen. Der Zuschuss
sinkt nur proportional zum erwarteten Versterben der geschützten
Bestandsrentner-Kohorte.

## Ergebnisse

| Jahr | Überlebensquote Bestandskohorte | Bestandsschutz-Zuschuss | Jährliche Abschmelzung |
| --- | ---: | ---: | ---: |
| 2027 | 100,0 % | 97,858 Mrd. Euro | 0,000 Mrd. Euro |
| 2030 | 85,8 % | 83,992 Mrd. Euro | 4,582 Mrd. Euro |
| 2035 | 63,5 % | 62,165 Mrd. Euro | 4,176 Mrd. Euro |
| 2040 | 44,1 % | 43,166 Mrd. Euro | 3,538 Mrd. Euro |
| 2045 | 28,0 % | 27,441 Mrd. Euro | 2,880 Mrd. Euro |
| 2050 | 15,6 % | 15,279 Mrd. Euro | 2,105 Mrd. Euro |
| 2060 | 3,9 % | 3,863 Mrd. Euro | 0,495 Mrd. Euro |
| 2070 | 1,7 % | 1,648 Mrd. Euro | 0,111 Mrd. Euro |

Vollständige Jahreswerte:

`analysen/daten/2026-06-04-bundeszuschuss-abschmelzung.csv`

## Interpretation

- Der Zuschuss bleibt im Reformjahr vollständig erhalten.
- Danach sinkt er nur mit der erwarteten Überlebendenquote des Altbestands.
- Neue rentenwirksame Staatsleistungen ab 2027 sind zusätzlich als echte Beiträge zu finanzieren.
- Die frühere 70/30-Ersatzverteilung wurde durch DRV-Rentenbestandsdaten ersetzt.

## Restunsicherheiten

- Die Zerlegung der Bundesmittel ist in dieser Fassung eine Reformklassifikation, keine amtliche Zweckzerlegung.
- Für Knappschaft-Bahn-See liegt im DRV-Tabellenband nur eine aggregierte Trägertrennung vor.
- Sterblichkeitsverbesserungen nach 2022/2024 sind noch nicht als Sensitivität modelliert.
