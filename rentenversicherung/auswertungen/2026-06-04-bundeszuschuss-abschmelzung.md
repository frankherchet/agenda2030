# Abschmelzmodell Bestandsschutz-Zuschuss Rentenversicherung

Stand: 2026-06-04

Reproduzierbar mit:

```bash
python3 scripts/calc_rente_bundeszuschuss_abschmelzung.py
```

## Eingaben

- Reformstichtag: 2027
- Startwert Bundesmittel 2025: 97,858 Mrd. Euro
- Quelle Sterblichkeit: `demographie/originale/2026-06-04-destatis-sterbetafeln-2022-2024.xlsx`
- Verwendete Tabellen: `12613-b01` männlich, `12613-b02` weiblich
- Verwendete Größe: `Überlebende - lx` nach vollendetem Alter
- Arbeitsannahme Geschlecht: 45 % männlich, 55 % weiblich
- Arbeitsannahme Alter: 70 % der Bestandsrentner in Altersjahren 67-79, 30 % in Altersjahren 80-100, jeweils gleich verteilt
- Tabellenende: Die Destatis-Altersjahrestabelle endet bei Alter 100; Überleben oberhalb dieses Alters wird in v1 nicht fortgeschrieben

## Modellregel

`Bestandsschutz-Zuschuss(t) = Startwert * erwartete Überlebendenzahl Bestandskohorte(t) / Bestandskohorte(2027)`

Politische Sonderkürzungen sind in diesem Modell ausgeschlossen. Der Zuschuss
sinkt nur proportional zum erwarteten Versterben der geschützten
Bestandsrentner-Kohorte.

## Ergebnisse

| Jahr | Überlebensquote Bestandskohorte | Bestandsschutz-Zuschuss | Jährliche Abschmelzung |
| --- | ---: | ---: | ---: |
| 2027 | 100,0 % | 97,858 Mrd. Euro | 0,000 Mrd. Euro |
| 2030 | 79,4 % | 77,721 Mrd. Euro | 5,512 Mrd. Euro |
| 2035 | 57,4 % | 56,166 Mrd. Euro | 3,943 Mrd. Euro |
| 2040 | 37,8 % | 37,031 Mrd. Euro | 3,768 Mrd. Euro |
| 2045 | 20,1 % | 19,636 Mrd. Euro | 3,185 Mrd. Euro |
| 2050 | 7,4 % | 7,236 Mrd. Euro | 1,951 Mrd. Euro |
| 2060 | 0,1 % | 0,070 Mrd. Euro | 0,112 Mrd. Euro |
| 2070 | 0,0 % | 0,000 Mrd. Euro | 0,000 Mrd. Euro |

Vollständige Jahreswerte:

`rentenversicherung/daten/2026-06-04-bundeszuschuss-abschmelzung.csv`

## Interpretation

- Der Zuschuss bleibt im Reformjahr vollständig erhalten.
- Danach sinkt er nur mit der erwarteten Überlebendenquote des Altbestands.
- Neue rentenwirksame Staatsleistungen ab 2027 sind zusätzlich als echte Beiträge zu finanzieren.

## Offene Punkte

- Tatsächliche Alters- und Geschlechtsstruktur der laufenden Renten fehlt noch.
- Die v1-Altersverteilung ist eine Arbeitsannahme und muss durch DRV-Daten ersetzt werden.
- Der 100+-Tail muss in einer Prüffassung explizit modelliert werden.
- Sterblichkeitsverbesserungen nach 2022/2024 sind noch nicht als Sensitivität modelliert.
