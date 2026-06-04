# Eingang

Dieser Bereich sammelt neues Material, bevor daraus Maßnahmen,
Gesetzesänderungen oder Drucksachen-Zusammenfassungen entstehen.

## Struktur

- `dokumente/`: externe Dokumente, Artikel, Studien, Berichte oder Auszüge.
- `links/`: Weblinks mit kurzer Einordnung.
- `ideen/`: eigene Ideen, Hypothesen, Reformskizzen und lose Notizen.
- `originale/`: kleine Rohdateien wie JSON, CSV, TXT oder kleinere PDFs.
- `index/`: Übersichten und thematische Register.

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

1. Neues Material als Markdown mit `vorlagen/ingest.md` erfassen.
2. Quelle, Kernaussage und Relevanz knapp dokumentieren.
3. In `eingang/index/README.md` eintragen.
4. Betroffene Ministerien, Gesetze und mögliche nächste Schritte verlinken.
5. Kleine Rohdateien bei Bedarf unter `eingang/originale/` ablegen und im
   Ingest repo-relativ referenzieren.
6. Nur die für die weitere Arbeit notwendigen Details aufnehmen.

## Pflicht

Externe Quellen müssen vor ihrer Nutzung in Reports, Auswertungen,
Prüferberichten, Skripten oder Quellenkatalogen hier erfasst werden.
Nachgelagerte Artefakte verweisen über `ingest_refs` auf die jeweilige
Eingang-Datei.
