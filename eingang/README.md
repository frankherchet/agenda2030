# Eingang

Dieser Bereich sammelt neues Material, bevor daraus Maßnahmen,
Gesetzesänderungen oder Drucksachen-Zusammenfassungen entstehen.

## Struktur

- `dokumente/`: externe Dokumente, Artikel, Studien, Berichte oder Auszüge.
- `links/`: Weblinks mit kurzer Einordnung.
- `ideen/`: eigene Ideen, Hypothesen, Reformskizzen und lose Notizen.
- `originale/`: kleine Rohdateien wie JSON, CSV, TXT oder kleinere PDFs.
- `index/`: Übersichten und thematische Register.

Der globale Wissensindex `index.md` in der Repo-Wurzel katalogisiert
wiederverwendbare Wissensseiten, Reports, Auswertungen und Prüfberichte. Der
Index hier unter `eingang/index/README.md` bleibt der Quellen-Eingangsindex.
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

1. `index.md`, `log.md`, `eingang/index/README.md` und naheliegende Fachordner
   lesen, bevor neues Material eingeordnet wird.
2. Neues Material als Markdown mit `vorlagen/ingest.md` erfassen.
3. Quelle, Kernaussage und Relevanz knapp dokumentieren.
4. Als `Enthaltene Informationen` erfassen, welche Tabellen, Kapitel,
   Abschnitte, Datenfelder, Zeiträume, Normen, Akteure oder Themen die Quelle
   enthält.
5. Als `Jetzt extrahierte relevante Informationen` dokumentieren, welche
   Fakten, Zahlen, Fundstellen oder Aussagen für die aktuelle Aufgabe
   herausgezogen wurden.
6. In `eingang/index/README.md` eintragen.
7. Betroffene Ministerien, Gesetze, Wissensseiten, Reports, Auswertungen und
   mögliche nächste Schritte verlinken.
8. Kleine Rohdateien bei Bedarf unter `eingang/originale/` ablegen und im
   Ingest repo-relativ referenzieren.
9. `index.md` aktualisieren, wenn eine dauerhaft relevante Wissensseite
   entsteht oder neu verknüpft werden muss.
10. `log.md` append-only ergänzen.
11. Nur die für die weitere Arbeit notwendigen Details aufnehmen.

## Pflicht

Externe Quellen müssen vor ihrer Nutzung in Reports, Auswertungen,
Prüferberichten, Skripten oder Quellenkatalogen hier erfasst werden.
Nachgelagerte Artefakte verweisen über `ingest_refs` auf die jeweilige
Eingang-Datei.

Bei jedem Ingest muss kontextabhängig geprüft werden, ob bestehende
Wissensseiten betroffen sind. Mögliche Widersprüche, veraltete Aussagen oder
fehlende Folgearbeiten werden im Ingest sichtbar als offene Fragen oder
TODOs notiert.
