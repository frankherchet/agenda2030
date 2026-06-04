# Destatis-Demographie: Altersstruktur und Bevölkerungsvorausberechnung

## Metadaten

- Datum der Ablage: 2026-06-04
- Hauptquelle: Statistisches Bundesamt (Destatis)
- Status: zitierfähige Inputquelle
- Relevanz: Rentenversicherung, gesetzliche Krankenversicherung,
  Pflegeversicherung, Arbeitsmarkt und Bundeshaushalt
- Ingest-Referenzen:
  - `eingang/links/2026-06-04-destatis-bevoelkerung-altersgruppen-2024.md`
  - `eingang/links/2026-06-04-destatis-bevoelkerungsvorausberechnung-16.md`
  - `eingang/links/2026-06-04-destatis-presse-16-bevoelkerungsvorausberechnung.md`
  - `eingang/links/2026-06-04-destatis-demografischer-wandel.md`
  - `eingang/links/2026-06-04-destatis-population-projection-en.md`

## Quellen

- Bevölkerung nach Altersgruppen 2011 bis 2024:
  https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/Tabellen/bevoelkerung-altersgruppen-deutschland-absulut-basis-2022.html
- 16. koordinierte Bevölkerungsvorausberechnung:
  https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsvorausberechnung/annahmen_ergebnisse_16te_kBv.html
- Pressemitteilung zur 16. koordinierten Bevölkerungsvorausberechnung:
  https://www.destatis.de/DE/Presse/Pressemitteilungen/2025/12/PD25_446_12.html
- Destatis-Themenseite demografischer Wandel:
  https://www.destatis.de/DE/Themen/Querschnitt/Demografischer-Wandel/demografie-mitten-im-wandel.html
- Destatis Population projection, englische Themenseite:
  https://www.destatis.de/EN/Themes/Society-Environment/Population/Population-Projection/_node.html

## Kurzfassung

Deutschland steht bis Mitte der 2030er-Jahre vor einer deutlichen Verschiebung
des Verhältnisses von Erwerbsbevölkerung zu Rentenalter. Destatis erwartet in
allen Varianten der 16. koordinierten Bevölkerungsvorausberechnung, dass 2035
ein Viertel der Bevölkerung 67 Jahre oder älter sein wird. Der Altenquotient
für 20- bis 66-Jährige gegenüber Personen ab 67 steigt von 33 im Jahr 2024 auf
43 bis 47 im Jahr 2038; 2070 liegt er je nach Variante bei 43, 51 oder 61. Für
Rente und GKV ist damit nicht nur die Zahl älterer Menschen relevant, sondern
auch die schrumpfende Zahl potenzieller Beitragszahler.

## Kernzahlen Bestand 2024

| Kennzahl | Wert |
| --- | ---: |
| Bevölkerung insgesamt | 83.577.140 |
| unter 20 Jahre | 15.585.942 |
| 20 bis unter 40 Jahre | 20.261.235 |
| 40 bis unter 60 Jahre | 22.245.996 |
| 60 bis unter 80 Jahre | 19.429.128 |
| 80 bis unter 100 Jahre | 6.036.938 |
| 100 Jahre und mehr | 17.901 |

Quelle: Destatis Bevölkerungsfortschreibung nach Altersgruppen, Stand 2024.

## Vorausberechnung und Quotienten

| Jahr | Variante | Kennzahl | Wert |
| --- | --- | --- | ---: |
| 2024 | Ausgangswert | Altenquotient 20-66 / 67+ | 33 |
| 2035 | alle Varianten | Anteil 67+ | 25 % |
| 2038 | Variante 5 G3L1W3 | Altenquotient 20-66 / 67+ | 43 |
| 2038 | Variante 2 G2L2W2 | Altenquotient 20-66 / 67+ | 45 |
| 2038 | Variante 4 G1L3W1 | Altenquotient 20-66 / 67+ | 47 |
| 2070 | Variante 5 G3L1W3 | Altenquotient 20-66 / 67+ | 43 |
| 2070 | Variante 2 G2L2W2 | Altenquotient 20-66 / 67+ | 51 |
| 2070 | Variante 4 G1L3W1 | Altenquotient 20-66 / 67+ | 61 |

Der Altenquotient misst Personen ab 67 Jahren je 100 Personen im Erwerbsalter
von 20 bis 66 Jahren. Er ist für umlagefinanzierte Sozialversicherungen eine
zentrale Belastungskennzahl.

Für die Gesamtbevölkerung 2070 nennt Destatis je nach betrachteter
Variantenauswahl unterschiedliche Spannweiten: Über alle 27 Varianten reicht
sie von 63,9 bis 86,5 Mio. Menschen; die kompakte Destatis-Themenseite weist
für ausgewählte Kernvarianten 68,7 bis 80,7 Mio. Menschen aus.

## Relevanz für Rentenversicherung

- Weniger Erwerbspersonen pro Rentenbeziehendem erhöhen den Druck auf
  Beitragssatz, Rentenniveau, Bundesmittel oder Renteneintrittsalter.
- Der Babyboomer-Übergang in den Ruhestand wirkt besonders stark bis Ende der
  2030er-Jahre.
- Eine Reform mit Beitragsklarheit muss definieren, wie staatlich gewünschte
  Rentenpunkte finanziert werden, wenn die Beitragsbasis schrumpft.

## Relevanz für gesetzliche Krankenversicherung

- Der Anteil älterer Menschen steigt, während der Anteil potenzieller
  Beitragszahler sinkt.
- Höhere Altersgruppen sind für Gesundheits- und Pflegeausgaben strukturell
  relevanter.
- GKV-Reformen sollten dieselben Demographieannahmen nutzen wie Rentenreformen,
  damit Belastungen nicht zwischen Systemen verschoben werden.

## Datenablage

Die strukturierten Kernwerte stehen in:

`demographie/daten/2026-06-04-demographie-kernzahlen-2024-2070.csv`

## Offene Punkte

- Für konkrete Reformrechnungen werden später feinere Altersjahre oder
  5-Jahres-Gruppen benötigt.
- Regionale Unterschiede sind in v1 noch nicht abgebildet.
- Eurostat/OECD/UN-Vergleiche sind bewusst nicht Teil dieser ersten Quelle.
