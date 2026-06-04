# Originale

Dieser Ordner enthält kleine Rohdateien, die als Ingest-Material versioniert
werden sollen.

## Zweck

- JSON-, CSV-, TXT- und kleinere PDF-Dateien aufbewahren, die später in
  Ingests, Auswertungen oder Reports nachvollziehbar referenziert werden.
- Die fachliche Einordnung bleibt in Markdown-Dateien unter `ingest/dokumente/`,
  `ingest/links/` oder `ingest/ideen/`.
- Große Binärdateien wie Videos, Audiodateien oder umfangreiche Archive bleiben
  außerhalb des Repos und werden im jeweiligen Ingest nur referenziert.

## Namensschema

```text
YYYY-MM-DD-kurzer-titel.<ext>
```

Beispiel:

```text
2026-06-04-markus-lanz-sendung-2026-06-02.json
```

## Verweise

Ingest-Dateien verweisen auf Rohdateien mit repo-relativen Pfaden, zum Beispiel:

```text
ingest/originale/2026-06-04-markus-lanz-sendung-2026-06-02.json
```
