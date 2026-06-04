# Bundeshaushalt

Dieser Bereich sammelt den Bundeshaushalt als zentralen Input für
Reformvorschläge: Was nimmt der Bund ein, wofür gibt er Geld aus, und welche
Finanzierungsspielräume oder Belastungen ergeben sich daraus?

## Struktur

- `originale/`: offizielle Originaldokumente, zum Beispiel PDF-Dateien.
- `zusammenfassungen/`: kompakte Markdown-Auswertungen je Haushaltsjahr.
- `daten/`: strukturierte Tabellen, CSV-Dateien oder exportierte Datensätze.
- `index/`: Übersichten nach Jahr, Einzelplan, Aufgabenbereich oder Thema.

## Arbeitsweise

1. Offizielle Quelle dokumentieren, bevorzugt BMF, Bundeshaushalt digital,
   Bundesgesetzblatt oder Bundestag.
2. Einnahmen ohne Nettokreditaufnahme getrennt von Kreditaufnahme betrachten.
3. Soll, Ist und unterjährige Ist-Entwicklung nicht vermischen.
4. Einzelpläne, Aufgabenbereiche und ökonomische Arten getrennt erfassen.
5. Relevanz für Maßnahmen, Ministerien und Gesetzesänderungen verlinken.

## Namensschema

- Jahreszusammenfassung: `zusammenfassungen/YYYY.md`
- Datensatz: `daten/YYYY-<quelle-oder-thema>.csv`
- Original: `originale/YYYY-<quelle-oder-thema>.pdf`
