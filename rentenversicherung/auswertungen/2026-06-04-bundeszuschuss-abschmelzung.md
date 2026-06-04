# Abschmelzmodell Bestandsschutz-Zuschuss Rentenversicherung

Stand: 2026-06-04

Reproduzierbar mit:

```bash
python3 scripts/build_drv_renten_inputs.py
python3 scripts/calc_rente_bundeszuschuss_abschmelzung.py
```

## Eingaben

- Reformstichtag: 2027
- Abschmelzbarer Startwert Bundesmittel 2025: 97,858 Mrd. Euro
- Modellierte laufende Renten aus DRV-Rentenbestand 2024: 26.086.937 Renten
- Nicht modellierte Restzeilen ohne Alter: 725 Renten
- Rentenbestandsstruktur: `rentenversicherung/daten/2026-06-04-drv-rentenbestand-struktur.csv`
- Bundesmittel-Zerlegung: `rentenversicherung/daten/2026-06-04-bundesmittel-zerlegung.csv`
- Quelle Sterblichkeit: `demographie/originale/2026-06-04-destatis-sterbetafeln-2022-2024.xlsx`
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

`rentenversicherung/daten/2026-06-04-bundeszuschuss-abschmelzung.csv`

## Interpretation

- Der Zuschuss bleibt im Reformjahr vollständig erhalten.
- Danach sinkt er nur mit der erwarteten Überlebendenquote des Altbestands.
- Neue rentenwirksame Staatsleistungen ab 2027 sind zusätzlich als echte Beiträge zu finanzieren.
- Die frühere 70/30-Ersatzverteilung wurde durch DRV-Rentenbestandsdaten ersetzt.

## Restunsicherheiten

- Die Zerlegung der Bundesmittel ist in dieser Fassung eine Reformklassifikation, keine amtliche Zweckzerlegung.
- Für Knappschaft-Bahn-See liegt im DRV-Tabellenband nur eine aggregierte Trägertrennung vor.
- Sterblichkeitsverbesserungen nach 2022/2024 sind noch nicht als Sensitivität modelliert.
