# GENESIS RESTful/JSON API Reference

Quelle: `https://genesis.destatis.de/genesisWS/rest/2020/GOJsonApi.json`,
OpenAPI `GENESIS-Online RESTful-JSON-API` Version `1.0.0`.

## Base

```text
https://genesis.destatis.de/genesisWS/rest/2020
```

Die Swagger UI liegt unter:

```text
https://genesis.destatis.de/genesisWS/swagger-ui/index.html
```

## Auth

Die OpenAPI beschreibt `username` und `password` als Header-Parameter. Die
Antwortobjekte führen die genutzten Parameter ebenfalls auf. Das
Helper-Skript sendet Zugangsdaten daher als Header und als Formparameter, damit
es mit der Swagger-Praxis kompatibel bleibt. Secrets nie ausgeben.

## Common Parameters

- `language`: meist `de` oder `en`
- `area`: häufig `free`, `all` oder ähnlich laut API-Kontext
- `pagelength`: z.B. `25`, `100`
- `selection`: Filter-/Suchauswahl für Katalogdienste
- `name`: Tabellen-, Cube-, Statistik-, Variable-, Wert- oder Zeitreihencode
- `startyear`, `endyear`, `timeslices`: Zeitfilter für Datenabrufe
- `regionalvariable`, `regionalkey`: regionale Filter
- `classifyingvariable1..5`, `classifyingkey1..5`: sachliche Filter
- `format`: bei File-Endpunkten z.B. `ffcsv`

## Find

| Methode | Pfad | Zweck | Parameter |
| --- | --- | --- | --- |
| POST | `/find/find` | Objekte zu Suchbegriff finden | `term`, `category`, `pagelength`, `language` |

Hinweis: Für breite Suche `category=Alle` verwenden. Beispiel:

```bash
python3 .agents/skills/destatis-genesis/scripts/genesis_fetch.py find --term "geburten" --category Alle --pagelength 100
```

Das Ergebnis kann `Cubes`, `Statistics`, `Tables`, `Timeseries` und
`Variables` enthalten. Für fachliche Arbeit im Repo meist zuerst passende
`Tables` oder `Cubes` auswählen, danach Metadaten prüfen.

## Catalogue

| Methode | Pfad | Zweck | Parameter |
| --- | --- | --- | --- |
| POST | `/catalogue/cubes` | Cubes listen | `selection`, `area`, `pagelength`, `language` |
| POST | `/catalogue/cubes2statistic` | Cubes zu Statistik | `name`, `selection`, `area`, `pagelength`, `language` |
| POST | `/catalogue/cubes2variable` | Cubes zu Variable | `name`, `selection`, `area`, `pagelength`, `language` |
| POST | `/catalogue/jobs` | Jobs listen | `selection`, `searchcriterion`, `sortcriterion`, `type`, `pagelength`, `language` |
| POST | `/catalogue/modifieddata` | geänderte Daten | `selection`, `type`, `date`, `pagelength`, `language` |
| GET/POST | `/catalogue/qualitysigns` | Qualitätszeichen | `language` |
| POST | `/catalogue/results` | Ergebnisobjekte | `selection`, `area`, `pagelength`, `language` |
| POST | `/catalogue/statistics` | Statistiken listen | `selection`, `searchcriterion`, `sortcriterion`, `pagelength`, `language` |
| POST | `/catalogue/statistics2variable` | Statistiken zu Variable | `name`, `selection`, `area`, `searchcriterion`, `sortcriterion`, `pagelength`, `language` |
| POST | `/catalogue/tables` | Tabellen listen | `selection`, `area`, `searchcriterion`, `sortcriterion`, `pagelength`, `language` |
| POST | `/catalogue/tables2statistic` | Tabellen zu Statistik | `name`, `selection`, `area`, `pagelength`, `language` |
| POST | `/catalogue/tables2variable` | Tabellen zu Variable | `name`, `selection`, `area`, `pagelength`, `language` |
| POST | `/catalogue/terms` | Begriffe listen | `selection`, `pagelength`, `language` |
| POST | `/catalogue/timeseries` | Zeitreihen listen | `selection`, `area`, `pagelength`, `language` |
| POST | `/catalogue/timeseries2statistic` | Zeitreihen zu Statistik | `name`, `selection`, `area`, `pagelength`, `language` |
| POST | `/catalogue/timeseries2variable` | Zeitreihen zu Variable | `name`, `selection`, `area`, `pagelength`, `language` |
| POST | `/catalogue/values` | Werte listen | `selection`, `area`, `searchcriterion`, `sortcriterion`, `pagelength`, `language` |
| POST | `/catalogue/values2variable` | Werte zu Variable | `name`, `selection`, `area`, `searchcriterion`, `sortcriterion`, `pagelength`, `language` |
| POST | `/catalogue/variables` | Variablen listen | `selection`, `area`, `searchcriterion`, `sortcriterion`, `type`, `pagelength`, `language` |
| POST | `/catalogue/variables2statistic` | Variablen zu Statistik | `name`, `selection`, `area`, `searchcriterion`, `sortcriterion`, `type`, `pagelength`, `language` |

## Data

| Methode | Pfad | Zweck | Wichtige Parameter |
| --- | --- | --- | --- |
| POST | `/data/table` | Tabelle abrufen | `name`, `area`, `structureinformation`, `compress`, `transpose`, `contents`, `startyear`, `endyear`, `timeslices`, Filtervariablen, `job`, `stand`, `language` |
| POST | `/data/tablefile` | Tabelle als Datei | wie `table` plus `format`, `quality` |
| POST | `/data/cube` | Cube abrufen | `name`, `area`, `values`, `metadata`, `additionals`, `contents`, Zeit- und Filterparameter, `format`, `stand`, `language` |
| POST | `/data/cubefile` | Cube als Datei | wie `cube` |
| POST | `/data/timeseries` | Zeitreihe abrufen | `name`, `area`, `compress`, `transpose`, `contents`, Zeit- und Filterparameter, `job`, `stand`, `language` |
| POST | `/data/timeseriesfile` | Zeitreihe als Datei | wie `timeseries` plus `format` |
| POST | `/data/result` | Ergebnis abrufen | `name`, `area`, `compress`, `language` |
| POST | `/data/resultfile` | Ergebnis als Datei | `name`, `area`, `compress`, `format`, `quality`, `language` |
| POST | `/data/chart2table` | Chart zu Tabelle | `name`, `area`, Chart- und Filterparameter |
| POST | `/data/chart2timeseries` | Chart zu Zeitreihe | `name`, `area`, Chart- und Filterparameter |
| POST | `/data/chart2result` | Chart zu Ergebnis | `name`, `area`, Chartparameter |
| POST | `/data/map2table` | Karte zu Tabelle | `name`, `area`, Karten- und Filterparameter |
| POST | `/data/map2timeseries` | Karte zu Zeitreihe | `name`, `area`, Karten- und Filterparameter |
| POST | `/data/map2result` | Karte zu Ergebnis | `name`, `area`, Kartenparameter |

Für Repo-Arbeit bevorzugt `tablefile` mit `format=ffcsv`, wenn eine
maschinenlesbare CSV-artige Datei benötigt wird. JSON-Antworten von `table`
sind gut für Metadatenprüfung und Debugging.

## Metadata

| Methode | Pfad | Zweck | Parameter |
| --- | --- | --- | --- |
| POST | `/metadata/cube` | Cube-Metadaten | `name`, `area`, `language` |
| POST | `/metadata/statistic` | Statistik-Metadaten | `name`, `area`, `language` |
| POST | `/metadata/table` | Tabellen-Metadaten | `name`, `area`, `language` |
| POST | `/metadata/timeseries` | Zeitreihen-Metadaten | `name`, `area`, `language` |
| POST | `/metadata/value` | Wert-Metadaten | `name`, `area`, `language` |
| POST | `/metadata/variable` | Variablen-Metadaten | `name`, `area`, `language` |

## Hello/Profile

| Methode | Pfad | Zweck | Parameter |
| --- | --- | --- | --- |
| POST | `/helloworld/logincheck` | Accountdaten testen | `language` |
| GET | `/helloworld/whoami` | Verbindung testen | keine |
| POST | `/profile/password` | Passwort ändern | `new`, `repeat`, `language` |
| POST | `/profile/removeResult` | Ergebnis löschen | `name`, `area`, `language` |

`profile/password` nicht automatisiert verwenden, außer der User verlangt es
ausdrücklich. Niemals neue Passwörter in Dateien oder Logs schreiben.

## Geburten-Beispiel

Bei `find --term "geburten" --category Alle --pagelength 100` erscheinen u.a.
für die Geburtenstatistik:

- `12612-0001`: Lebendgeborene Deutschland, Jahre, Geschlecht
- `12612-0002`: Lebendgeborene Deutschland, Monate, Geschlecht
- `12612-0005`: Lebendgeborene Deutschland, Jahre, Alter der Mutter,
  Lebendgeburtenfolge
- `12612-0008`: Geburtenziffern je 1000 Frauen, Deutschland, Jahre, Alter
- `12612-0009`: Zusammengefasste Geburtenziffern je Frau, Deutschland, Jahre,
  Altersgruppen
- `12612-0100`: Lebendgeborene Bundesländer, Jahre, Geschlecht

Vor Nutzung immer `metadata-table --name <code>` ausführen und Parameter,
Zeitraum sowie Variablen dokumentieren.
