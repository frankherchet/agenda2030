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

- Reformstichtag: 2030
- Brückenjahre 2027-2029 bleiben vor Reformstart als Status-quo-Phase erhalten.
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

`Bestandsschutz-Zuschuss(t) = abschmelzbarer Startwert * erwartete Überlebendenzahl Bestandskohorte(t) / Bestandskohorte(2030)`

Politische Sonderkürzungen sind in diesem Modell ausgeschlossen. Der Zuschuss
sinkt nur proportional zum erwarteten Versterben der geschützten
Bestandsrentner-Kohorte.

## Ergebnisse

| Jahr | Überlebensquote Bestandskohorte | Bestandsschutz-Zuschuss | Jährliche Abschmelzung |
| --- | ---: | ---: | ---: |
| 2027 | 100,0 % | 97,858 Mrd. Euro | 0,000 Mrd. Euro |
| 2028 | 100,0 % | 97,858 Mrd. Euro | 0,000 Mrd. Euro |
| 2029 | 100,0 % | 97,858 Mrd. Euro | 0,000 Mrd. Euro |
| 2030 | 100,0 % | 97,858 Mrd. Euro | 0,000 Mrd. Euro |
| 2035 | 76,6 % | 75,003 Mrd. Euro | 4,461 Mrd. Euro |
| 2040 | 55,4 % | 54,176 Mrd. Euro | 3,932 Mrd. Euro |
| 2045 | 37,3 % | 36,483 Mrd. Euro | 3,276 Mrd. Euro |
| 2050 | 22,6 % | 22,104 Mrd. Euro | 2,596 Mrd. Euro |
| 2060 | 5,8 % | 5,670 Mrd. Euro | 0,854 Mrd. Euro |
| 2070 | 2,1 % | 2,024 Mrd. Euro | 0,160 Mrd. Euro |

Vollständige Jahreswerte:

`analysen/daten/2026-06-04-bundeszuschuss-abschmelzung.csv`

## Interpretation

- Der Zuschuss bleibt in den Brückenjahren 2027-2029 vollständig erhalten und startet 2030 auf dem Ausgangsniveau.
- Danach sinkt er nur mit der erwarteten Überlebendenquote des Altbestands.
- Neue rentenwirksame Staatsleistungen ab 2030 sind zusätzlich als echte Beiträge zu finanzieren.
- Die frühere 70/30-Ersatzverteilung wurde durch DRV-Rentenbestandsdaten ersetzt.

## Restunsicherheiten

- Die Zerlegung der Bundesmittel ist in dieser Fassung eine Reformklassifikation, keine amtliche Zweckzerlegung.
- Für Knappschaft-Bahn-See liegt im DRV-Tabellenband nur eine aggregierte Trägertrennung vor.
- Sterblichkeitsverbesserungen nach 2022/2024 sind noch nicht als Sensitivität modelliert.
