# Zukunftsmodell Rentenreform 2027-2070

Stand: 2026-06-04

Reproduzierbar mit:

```bash
python3 scripts/calc_rentenreform_zukunft.py
```

## Zweck

Diese Analyse modelliert die Finanzierungswirkung des Reformprojekts
Rentenversicherung bis 2070 und vergleicht Status quo, abschmelzende
Bundesmittel und erweiterte Erwerbstätigenbasis.

## Quellen und Ingests

- `ingest/links/2026-06-04-drv-finanzkennzahlen-rentenversicherung.md`
- `ingest/links/2026-06-04-destatis-bevoelkerungsvorausberechnung-16.md`
- `ingest/links/2026-06-04-destatis-arbeitsmarkt-eckzahlen-2025.md`
- `ingest/links/2026-06-04-destatis-oeffentlicher-dienst-2024.md`
- `ingest/links/2026-06-04-bmas-rentenversicherungsbericht-2025.md`
- `analysen/daten/2026-06-04-bundeszuschuss-abschmelzung.csv`

## Modellcharakter

Dieses v1-Modell ist ein Finanzierungsmodell, kein vollständiges
versicherungsmathematisches Rentenzugangsmodell. Es zeigt, wie sich
Beitragssätze verändern, wenn Ausgaben mit Demographie und Rentenanpassung
wachsen, heutige Bundesmittel nur noch als Bestandsschutz abschmelzen und
die Beitragsbasis durch eine Erwerbstätigenversicherung erweitert wird.

Nicht quantifiziert sind in v1 Einsparungen aus künftig wegfallenden
unbezahlten Rentenpunkten; diese Regel wirkt langfristig zusätzlich, braucht
aber eine eigene Normen- und Volumenzerlegung.

## Kernergebnis

| Szenario | Jahr | Status quo: Beitragssatz | Reform ohne neue Basis | Reform mit Erwerbstätigenbasis | Reform-Zusatzbasis |
| --- | ---: | ---: | ---: | ---: | ---: |
| jung | 2027 | 18,4 % | 18,5 % | 18,5 % | 0,0 Mrd. Euro |
| jung | 2035 | 21,9 % | 25,6 % | 24,0 % | 132,7 Mrd. Euro |
| jung | 2040 | 23,4 % | 28,6 % | 26,8 % | 159,3 Mrd. Euro |
| jung | 2050 | 23,2 % | 29,7 % | 27,5 % | 230,2 Mrd. Euro |
| jung | 2060 | 23,0 % | 29,8 % | 27,4 % | 326,4 Mrd. Euro |
| jung | 2070 | 22,8 % | 29,6 % | 26,9 % | 456,9 Mrd. Euro |
| moderat | 2027 | 18,6 % | 18,7 % | 18,7 % | 0,0 Mrd. Euro |
| moderat | 2035 | 22,8 % | 26,6 % | 25,0 % | 130,1 Mrd. Euro |
| moderat | 2040 | 24,7 % | 30,2 % | 28,2 % | 154,6 Mrd. Euro |
| moderat | 2050 | 25,1 % | 32,1 % | 29,8 % | 218,9 Mrd. Euro |
| moderat | 2060 | 25,6 % | 33,1 % | 30,5 % | 303,7 Mrd. Euro |
| moderat | 2070 | 26,1 % | 33,9 % | 30,9 % | 415,6 Mrd. Euro |
| alt | 2027 | 18,8 % | 18,9 % | 18,9 % | 0,0 Mrd. Euro |
| alt | 2035 | 23,6 % | 27,5 % | 25,9 % | 127,6 Mrd. Euro |
| alt | 2040 | 25,9 % | 31,7 % | 29,7 % | 150,2 Mrd. Euro |
| alt | 2050 | 27,2 % | 34,7 % | 32,2 % | 207,8 Mrd. Euro |
| alt | 2060 | 28,6 % | 37,0 % | 34,0 % | 281,2 Mrd. Euro |
| alt | 2070 | 30,2 % | 39,2 % | 35,7 % | 374,2 Mrd. Euro |

## Interpretation

- Bei anteilig fortgeschriebenen Bundesmitteln steigt der rechnerische Beitragssatz im moderaten Szenario bis 2070 auf rund 26,1 %.
- Wenn heutige Bundesmittel wie beschlossen nur mit dem Altbestand abschmelzen und keine neue Beitragsbasis entsteht, steigt der Finanzierungsdruck deutlich stärker.
- Die Erwerbstätigenbasis dämpft den Beitragssatzanstieg, kompensiert den demographischen Druck aber in v1 nicht vollständig.
- Eine stabile Rente ist rechnerisch nur darstellbar, wenn Beitragssatz, echte staatliche Beiträge, Erwerbsbasis und Leistungsindexierung gemeinsam festgelegt werden.

## Artefakte

- Jahreswerte: `analysen/daten/2026-06-04-rentenreform-zukunft-modell.csv`
- Annahmen: `analysen/daten/2026-06-04-rentenreform-zukunft-annahmen.csv`

## Restunsicherheiten

- Keine vollständige Neurentner-Kohortenrechnung.
- Keine amtliche Zweckzerlegung der nicht beitragsgedeckten Leistungen.
- Einkommen von Selbstständigen und Neubeamten nur als Bemessungsfaktor modelliert.
- Sterblichkeitsverbesserungen nach 2022/2024 sind nicht enthalten.
