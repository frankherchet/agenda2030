---
title: Prüfung Strukturumbau Quellen Analysen Projekte
date: 2026-06-05
type: pruefung
status: offen
source_urls: []
ingest_refs: []
checked_commits:
  - 1b89882
  - 4790185
  - 77d372c
---

# Prüfung Strukturumbau Quellen Analysen Projekte

## Prüfauftrag

Nach den letzten Commits wurde geprüft, ob die neue Repo-Struktur für Quellen,
Dokumente, Analysen und Projekte konsistent nachgezogen wurde.

Geprüfter Stand:

- `HEAD`: `1b89882 Strukturiere Quellen Analysen und Rentenprojekt`
- Arbeitsbaum vor Prüfung: sauber, `main` synchron mit `origin/main`
- Geprüfte Leitdateien: `index.md`, `log.md`, `ingest/index/README.md`,
  `analysen/README.md`, `projekte/rentenversicherung/README.md`

## Ergebnis

| Bereich | Befund | Aktualisierungsbedarf |
| --- | --- | --- |
| Quellen/Ingest-Index | Die Quellen liegen einheitlich unter `ingest/`; der zentrale Ingest-Index verweist auf die neuen Pfade. | Kein Strukturbruch. Bestehende Ingests sollten in einem separaten Nachpflegepaket um die neuen Abschnitte `Enthaltene Informationen` und `Jetzt extrahierte relevante Informationen` ergänzt werden. |
| Dokumente | Dokument-Ingests und Rohdateien wurden in `ingest/dokumente/` und `ingest/originale/` zusammengeführt. | Metadatenfeld `source_url` im DRV-Quellenmetadaten-Ingest auf `source_urls` normalisiert. |
| Analysen | Die Analysen wurden nach `analysen/` verschoben, hatten aber keine maschinenlesbaren `source_urls` und `ingest_refs`. | Erledigt: Frontmatter in den fünf bestehenden Analyse-Dateien ergänzt. |
| Datenartefakte | CSV-Artefakte liegen unter `analysen/daten/`; Skripte verweisen auf die neuen Pfade. | Kein weiterer Pfadbedarf gefunden. |
| Projekt Rentenversicherung | Projektdateien liegen unter `projekte/rentenversicherung/`; Reformkonzept und Prüfbericht verweisen auf neue Analyse- und Datenpfade. | Erledigt: `publish` im Reformkonzept auf `false` gesetzt, weil der Prüfbericht Status `offen` trägt. |
| Normstände | Der Umbau führt die Normstand-Pflicht ein, aber für SGB VI, SGB IV und Grundgesetz liegen noch keine konkreten Normstand-Dateien vor. | Vor Rechtsanalyse, Gesetzesänderung oder Freigabe des Rentenkonzepts müssen die konkret tragenden Normstände unter `gesetzbuecher/` abgelegt werden. |
| Web-Ausgabe | `web/scripts/build-content.mjs` liest nur `projekte/rentenversicherung`; durch `publish: false` wird das offene Reformkonzept nicht mehr als veröffentlichter Report ausgegeben. | Erwartetes Ergebnis, solange keine Freigabe vorliegt. |

## Nachgezogene Updates

- `analysen/2026-06-04-drv-rentenbestand-inputs.md`: Frontmatter mit Quelle,
  Ingests, Datenartefakten und Skript ergänzt.
- `analysen/2026-06-04-bundeszuschuss-abschmelzung.md`: Frontmatter mit
  Sterbetafel-, DRV- und Finanzquellen ergänzt.
- `analysen/2026-06-04-rentenreform-zukunft.md`: Frontmatter mit
  Finanz-, Demographie-, Arbeitsmarkt- und Beamtenquellen ergänzt.
- `analysen/2026-06-04-rente-belastungsrechnung.md`: Frontmatter mit
  Destatis-Ingests ergänzt.
- `analysen/2026-06-04-demographie-rente-gkv.md`: Frontmatter mit
  Destatis-Ingests ergänzt.
- `projekte/rentenversicherung/reformkonzept.md`: `publish: false` gesetzt,
  solange der Prüfstatus offen ist.
- `projekte/rentenversicherung/README.md`: Veröffentlichungsstatus ergänzt.
- `ingest/dokumente/2026-06-04-drv-statistikband-rente-2024-quellenmetadaten.md`:
  `source_url` zu `source_urls` normalisiert.

## Offene Folgearbeit

1. Bestehende Ingests nachmigrieren:
   - Abschnitt `Enthaltene Informationen`
   - Abschnitt `Jetzt extrahierte relevante Informationen`
   - Abschnitt `Verknüpfte Wissensseiten`
   - Abschnitt `Mögliche Updates`
   - Abschnitt `Widersprüche/Risiken`
2. Für das Rentenprojekt die tragenden Normstände prüfen und unter
   `gesetzbuecher/` ablegen, bevor eine Rechtsanalyse oder Freigabe erfolgt.
3. Die Bundesmittel-Zerlegung bleibt laut Prüfbericht offen, weil sie eine
   Reformklassifikation und keine amtliche Zweckzerlegung ist.
