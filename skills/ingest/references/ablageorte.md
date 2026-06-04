# Ablageorte für Ingest

## Standardfälle

- Bundestagsdrucksache: `bundestag-drucksachen/zusammenfassungen/BT-<wahlperiode>-<nummer>.md`
- Allgemeines Dokument: `eingang/dokumente/YYYY-MM-DD-<slug>.md`
- Link: `eingang/links/YYYY-MM-DD-<slug>.md`
- Idee oder Reformnotiz: `eingang/ideen/YYYY-MM-DD-<slug>.md`

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
