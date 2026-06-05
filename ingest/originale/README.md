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

## Aktuelle Rohdateien

- `2026-06-04-markus-lanz-sendung-2026-06-02.json`
- `2026-06-04-drv-statistikband-rente-2024.pdf`
- `2026-06-04-destatis-sterbetafeln-2022-2024.xlsx`
- `2026-06-05-bmas-rentenversicherungsbericht-2025.pdf`
- `2026-06-05-drv-rentenupdate-10-bundeszuschuesse-nbl-2025.pdf`
- `2026-06-05-bundestag-drs-21-1419-nicht-beitragsgedeckte-leistungen.pdf`
