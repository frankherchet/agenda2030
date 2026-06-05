# Ingest: Destatis 16. koordinierte Bevölkerungsvorausberechnung

## Metadaten

- Typ: Link
- Datum: 2026-06-04
- Quelle: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsvorausberechnung/annahmen_ergebnisse_16te_kBv.html
- Status: geprüft
- Index: `ingest/index/README.md`

## Kurzfassung

Destatis-Quelle zu Annahmen und Ergebnissen der 16. koordinierten
Bevölkerungsvorausberechnung. Sie liefert Szenarien zur künftigen Bevölkerung,
Altersstruktur und zum Altenquotienten. Diese Daten sind gemeinsame
Demographie-Basis für Rente, GKV, Pflege und Arbeitsmarkt.

## Kernaussagen

- Zentrale amtliche Vorausberechnung für Deutschland.
- Enthält Varianten und Annahmen bis 2070.
- Für Umlagesysteme ist der Altenquotient besonders relevant.

## Enthaltene Informationen

- Destatis-Material zur 16. koordinierten Bevölkerungsvorausberechnung mit
  Varianten, Annahmen, Altersstruktur und Altenquotient bis 2070.
- Enthält demographische Szenarien, die für Umlagesysteme wie Rente, GKV und
  Pflege als Sensitivitäten genutzt werden können.

## Jetzt extrahierte relevante Informationen

- Die Quelle trägt im Rentenprojekt die Szenarienlogik bis 2070 und die
  Einordnung des Altenquotienten.
- Die konkret im Repo genutzten Kernwerte sind in
  `ingest/dokumente/2026-06-04-destatis-demographie.md` und
  `analysen/daten/2026-06-04-demographie-kernzahlen-2024-2070.csv`
  verdichtet.

## Relevanz für agenda2030

Querschnittsquelle für demographische Belastungsrechnungen.

## Zuordnung

- Ministerien: `ministerien/arbeit-soziales/`, `ministerien/gesundheit/`
- Gesetze/Gesetzbücher: `gesetzbuecher/sgb/`
- Bundestagsdrucksachen: keine
- Themen: Demographie, Bevölkerungsvorausberechnung, Altenquotient

## Offene Fragen

- Sensitivitäten je Reformmodell aus den Varianten ableiten.

## Nächste Schritte

- Für GKV-Reform wiederverwenden.
