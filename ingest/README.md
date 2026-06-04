# Ingest

Dieser Bereich sammelt Quellenmaterial, bevor daraus Analysen, Maßnahmen,
Gesetzesänderungen oder Projektartefakte entstehen.

## Struktur

- `dokumente/`: externe Dokumente, Artikel, Studien, Berichte oder Auszüge.
- `links/`: Weblinks mit kurzer Einordnung.
- `ideen/`: eigene Ideen, Hypothesen, Reformskizzen und lose Notizen.
- `originale/`: kleine Rohdateien wie JSON, CSV, TXT oder kleinere PDFs.
- `index/`: Übersichten und thematische Register.

Der globale Wissensindex `index.md` in der Repo-Wurzel katalogisiert
wiederverwendbare Wissensseiten, Analysen, Projekte und Prüfberichte. Der
Index hier unter `ingest/index/README.md` bleibt der Ingest-Quellenindex.
Das chronologische Arbeitslog steht in `log.md`.

## Namensschema

Markdown-Dateien sollten nach Datum und kurzem Slug benannt werden:

```text
YYYY-MM-DD-kurzer-titel.md
```

Beispiel:

```text
2026-06-04-planungsbeschleunigung-bau.md
```

## Arbeitsweise

1. `index.md`, `log.md`, `ingest/index/README.md` und naheliegende Analysen,
   Projekte, Ministerien oder Gesetzbücher lesen, bevor neues Material
   eingeordnet wird.
2. Neues Material als Markdown mit `vorlagen/ingest.md` erfassen.
3. Quelle, Kernaussage und Relevanz knapp dokumentieren.
4. Als `Enthaltene Informationen` erfassen, welche Tabellen, Kapitel,
   Abschnitte, Datenfelder, Zeiträume, Normen, Akteure oder Themen die Quelle
   enthält.
5. Als `Jetzt extrahierte relevante Informationen` dokumentieren, welche
   Fakten, Zahlen, Fundstellen oder Aussagen für die aktuelle Aufgabe
   herausgezogen wurden.
6. In `ingest/index/README.md` eintragen.
7. Betroffene Ministerien, Gesetze, Wissensseiten, Analysen, Projekte und
   mögliche nächste Schritte verlinken.
8. Kleine Rohdateien bei Bedarf unter `ingest/originale/` ablegen und im
   Ingest repo-relativ referenzieren.
9. `index.md` aktualisieren, wenn eine dauerhaft relevante Wissensseite
   entsteht oder neu verknüpft werden muss.
10. `log.md` append-only ergänzen.
11. Nur die für die weitere Arbeit notwendigen Details aufnehmen.

## Pflicht

Externe Quellen müssen vor ihrer Nutzung in Analysen, Projekten,
Prüferberichten, Skripten oder Quellenkatalogen hier erfasst werden.
Nachgelagerte Artefakte verweisen über `ingest_refs` auf die jeweilige
Ingest-Datei.

Bei jedem Ingest muss kontextabhängig geprüft werden, ob bestehende
Wissensseiten betroffen sind. Mögliche Widersprüche, veraltete Aussagen oder
fehlende Folgearbeiten werden im Ingest sichtbar als offene Fragen oder
TODOs notiert.
