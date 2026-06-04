# Demographische Belastungsrechnung Rentenversicherung

Stand: 2026-06-04

Reproduzierbar mit:

```bash
python3 scripts/calc_demographie_rente.py
```

Datenquelle: `analysen/daten/2026-06-04-demographie-kernzahlen-2024-2070.csv`

## Zweck

Diese Analyse berechnet aus den demographischen Eingangsdaten zentrale
Belastungskennzahlen für Rentenreformmodelle, damit Altenquotient und
Erwerbsbevölkerung nicht in jedem Konzept neu hergeleitet werden müssen.

## Eingabewerte

| Jahr | Variante | Kennzahl | Wert |
| --- | --- | --- | ---: |
| 2024 | Ausgangswert | Bevölkerung insgesamt | 83,577 Mio. |
| 2024 | Ausgangswert | Personen im Erwerbsalter 20-66 | 51,2 Mio. |
| 2024 | Ausgangswert | Anteil 67 Jahre und älter | 20 % |
| 2024 | Ausgangswert | Altenquotient 20-66 / 67+ | 33 |
| 2035 | alle Varianten | Anteil 67 Jahre und älter | 25 % |
| 2038 | Spannweite Varianten | Personen ab 67 Jahren | 20,5 bis 21,3 Mio. |
| 2038 | Variante 5 G3L1W3 | Altenquotient 20-66 / 67+ | 43 |
| 2038 | Variante 2 G2L2W2 | Altenquotient 20-66 / 67+ | 45 |
| 2038 | Variante 4 G1L3W1 | Altenquotient 20-66 / 67+ | 47 |
| 2070 | Variante 5 G3L1W3 | Altenquotient 20-66 / 67+ | 43 |
| 2070 | Variante 2 G2L2W2 | Altenquotient 20-66 / 67+ | 51 |
| 2070 | Variante 4 G1L3W1 | Altenquotient 20-66 / 67+ | 61 |
| 2070 | Spannweite Varianten | Personen im Erwerbsalter 20-66 | 37,1 bis 45,3 Mio. |

## Rechenergebnisse

| Rechnung | Formel | Ergebnis |
| --- | --- | ---: |
| Altenquotient 2038 Variante 5 G3L1W3 | `(43 - 33) / 33` | 30,3 % |
| Altenquotient 2038 Variante 2 G2L2W2 | `(45 - 33) / 33` | 36,4 % |
| Altenquotient 2038 Variante 4 G1L3W1 | `(47 - 33) / 33` | 42,4 % |
| Altenquotient 2070 Variante 5 G3L1W3 | `(43 - 33) / 33` | 30,3 % |
| Altenquotient 2070 Variante 2 G2L2W2 | `(51 - 33) / 33` | 54,5 % |
| Altenquotient 2070 Variante 4 G1L3W1 | `(61 - 33) / 33` | 84,8 % |
| Erwerbsbevölkerung 2070 günstigerer Randwert | `(45,3 - 51,2) / 51,2` | -11,5 % |
| Erwerbsbevölkerung 2070 ungünstigerer Randwert | `(37,1 - 51,2) / 51,2` | -27,5 % |

## Interpretation

- In der moderaten Variante steigt der Altenquotient bis 2038 um 36,4 % und bis 2070 um 54,5 % gegenüber 2024.
- Selbst die relativ junge Variante liegt 2070 mit einem Altenquotienten von 43 klar über dem Ausgangswert 2024 von 33.
- Die Bevölkerung im Alter 20-66 sinkt bis 2070 je nach Randwert um 11,5 % bis 27,5 % gegenüber 2024.
