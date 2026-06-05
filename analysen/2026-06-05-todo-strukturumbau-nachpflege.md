---
title: TODO Strukturumbau Nachpflege
date: 2026-06-05
type: todo
status: offen
source_urls: []
ingest_refs: []
related_artifacts:
  - analysen/2026-06-05-strukturumbau-quellen-analysen-projekte-pruefung.md
  - projekte/rentenversicherung/normstand-bedarf.md
---

# TODO Strukturumbau Nachpflege

## Erledigt

- [x] Analyse-Dateien mit maschinenlesbaren `source_urls` und `ingest_refs`
  versehen.
- [x] Rentenkonzept wegen offenem Prüferstatus auf `publish: false` setzen.
- [x] Prüfvermerk zum Strukturumbau anlegen.
- [x] Direkt im Rentenkonzept referenzierte Ingests um `Enthaltene
  Informationen` und `Jetzt extrahierte relevante Informationen` ergänzen.
- [x] Normstand-Bedarf für das Rentenprojekt als separate Matrix erfassen.
- [x] Index, Analyse-README und Log auf die Nachpflege aktualisieren.

## Offen

- [ ] Nachrangige Ingests ohne direkten Rentenprojektbezug nachmigrieren:
  - `ingest/links/2026-06-04-destatis-sterbefaelle-lebenserwartung-thema.md`
  - `ingest/links/2026-06-04-destatis-entwicklung-lebenserwartung.md`
  - `ingest/links/2026-06-04-destatis-population-projection-en.md`
  - `ingest/links/2026-06-04-destatis-demografischer-wandel.md`
  - `ingest/links/2026-06-04-bmf-sollbericht-2026.md`
  - `ingest/links/2026-06-04-bmf-bundeshaushalt-2026.md`
  - `ingest/links/2026-06-04-bmf-monatsbericht-haushalt-april-2026.md`
  - `ingest/dokumente/2026-06-04-bmf-bundeshaushalt-2026-pdf.md`
  - `ingest/dokumente/2026-06-04-bundeshaushalt-2026-zusammenfassung.md`
  - `ingest/dokumente/2026-06-04-markus-lanz-sendung-2026-06-02.md`
  - `ingest/dokumente/2026-06-04-drv-statistikband-rente-2024-quellenmetadaten.md`
- [ ] Normstand-Dateien für das Rentenprojekt anlegen, priorisiert nach
  `projekte/rentenversicherung/normstand-bedarf.md`.
- [ ] Vollständigen BMAS-Rentenversicherungsbericht 2025 als Dokument-Ingest
  erfassen, wenn das Langfristmodell prüffähig werden soll.
- [ ] Amtliche oder gutachterliche Zweckzerlegung der heutigen Bundesmittel
  beschaffen und die Reformklassifikation dagegen prüfen.

## Entscheidung

Dieses Paket erledigt die direkt projektkritische Nachpflege. Die vollständige
Normstand-Ablage bleibt ein eigenes Arbeitspaket, weil das Rentenkonzept mehr
als fünfzig konkrete Paragraphen und Artikel nennt und jede Norm einzeln mit
geltendem Stand, Abrufdatum, Quelle und Ingest-Referenz abgelegt werden muss.
