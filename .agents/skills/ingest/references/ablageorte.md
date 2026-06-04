# Ablageorte für Ingest

## Standardfälle

- Bundestagsdrucksache: `ingest/dokumente/YYYY-MM-DD-bt-<wahlperiode>-<nummer>-<slug>.md`
- Allgemeines Dokument: `ingest/dokumente/YYYY-MM-DD-<slug>.md`
- Link: `ingest/links/YYYY-MM-DD-<slug>.md`
- Idee oder Reformnotiz: `ingest/ideen/YYYY-MM-DD-<slug>.md`

## Zuordnungen

- Fachliche Zuständigkeit: vorhandenen Ordner unter `ministerien/` verlinken.
- Rechtsänderung: vorhandenen Ordner unter `gesetzbuecher/` verlinken.
- Noch unklarer Rechtsbezug: `gesetzbuecher/weitere-gesetze/` nennen.

## Slug-Regeln

- lowercase
- kurze deutsche oder fachliche Begriffe
- Leerzeichen durch `-`
- Umlaute umschreiben: `ä` -> `ae`, `ö` -> `oe`, `ü` -> `ue`, `ß` -> `ss`
- keine Satzzeichen außer Bindestrich
