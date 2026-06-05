---
title: Bundesmittel-Zweckzerlegung Rente
date: 2026-06-05
type: analyse
status: arbeitsfassung
source_urls:
  - https://rentenupdate.drv-bund.de/SharedDocs/Dokumente/2025/10_Bundeszuschuesse_nbL/rentenupdate_10_Bundeszuschuesse_nbL_lang.pdf?__blob=publicationFile&v=4
  - https://dserver.bundestag.de/btd/21/014/2101419.pdf
ingest_refs:
  - ingest/dokumente/2026-06-05-drv-rentenupdate-bundeszuschuesse-nicht-beitragsgedeckte-leistungen-2025.md
  - ingest/dokumente/2026-06-05-bundestag-drs-21-1419-nicht-beitragsgedeckte-leistungen.md
data_artifacts:
  - analysen/daten/2026-06-04-bundesmittel-zerlegung.csv
related_project:
  - projekte/rentenversicherung/reformkonzept.md
---

# Bundesmittel-Zweckzerlegung Rente

## Zweck

Diese Analyse beschafft und ordnet die öffentlich verfügbaren Quellen zur
Zweckzerlegung der Bundesmittel in der gesetzlichen Rentenversicherung. Sie
prüft, ob die im Reformmodell verwendete Bundesmittel-Klassifikation durch
amtliche oder gutachterliche Quellen ersetzt oder nur plausibilisiert werden
kann.

## Beschaffte Quellen

- DRV Bund, `rentenupdate #10`, September 2025:
  `ingest/dokumente/2026-06-05-drv-rentenupdate-bundeszuschuesse-nicht-beitragsgedeckte-leistungen-2025.md`
- Bundestagsdrucksache 21/1419:
  `ingest/dokumente/2026-06-05-bundestag-drs-21-1419-nicht-beitragsgedeckte-leistungen.md`

## Ergebnis

| Frage | Ergebnis |
| --- | --- |
| Gibt es eine öffentlich verfügbare aktuelle Zweckabschätzung? | Ja, für 2023 über die DRV-Veröffentlichung zu nicht beitragsgedeckten Leistungen und Bundeszuschüssen. |
| Gibt es öffentlich verfügbare amtliche Werte für 2024? | Nein, laut Bundestagsdrucksache 21/1419 liegen der Bundesregierung entsprechende Zahlen nicht vor. |
| Gibt es öffentlich verfügbare Prognosen für 2025/2026? | Nein, laut Bundestagsdrucksache 21/1419 existieren keine öffentlich zugänglichen Prognosen. |
| Sind nicht beitragsgedeckte Leistungen eine Berechnungsgröße für Bundeszuschüsse? | Nein, die Bemessung der Bundeszuschüsse folgt SGB-VI-Regeln; die Entwicklung nicht beitragsgedeckter Leistungen ist keine festgelegte Berechnungsgröße. |
| Kann die CSV `2026-06-04-bundesmittel-zerlegung.csv` als amtliche Zweckzerlegung gelten? | Nein. Sie bleibt Reformklassifikation und muss als Modellannahme geführt werden. |

## Referenzwerte 2023

| Größe | Wert | Quelle |
| --- | ---: | --- |
| Nicht beitragsgedeckte Leistungen, erweiterte DRV-Abgrenzung | 124,1 Mrd. Euro | DRV rentenupdate #10 |
| Bundeszuschüsse | 84,3 Mrd. Euro | DRV rentenupdate #10 |
| Ungedeckte Differenz | rund 40 Mrd. Euro | DRV rentenupdate #10 |
| Unterdeckung relativ zu Rentenausgaben | rund 12 % | DRV rentenupdate #10 |

## Einordnung für das Reformmodell

- Der beschaffte Stand reicht aus, um den bisherigen Prüfer-Blocker zu
  präzisieren: Das Reformmodell darf die Bundesmittel-Zerlegung nicht als
  amtliche Zweckzerlegung für 2025 oder 2026 ausgeben.
- Die DRV-Quelle liefert aber eine belastbare öffentliche Referenz, dass nicht
  beitragsgedeckte Leistungen und Bundeszuschüsse in erheblichem Umfang
  auseinanderfallen.
- Für 2025/2026 muss jede Fortschreibung als Modellannahme mit
  Sensitivität markiert werden.
- Eine spätere Gesetzesänderung kann die Bundesmittel nicht nur
  haushalterisch umetikettieren; sie muss die SGB-VI-Zuschussregeln und
  staatliche Beitragszahlungen normklar trennen.

## Konsequenz

Der offene Punkt `amtliche oder gutachterliche Zweckzerlegung beschaffen` ist
für die öffentliche Quellenlage erledigt: Beschafft sind DRV-Schätzung 2023
und Bundestagsdrucksache 21/1419. Fachlich bleibt die Bewertung offen, weil
für 2024 bis 2026 keine öffentlichen amtlichen Fortschreibungen vorliegen.

## Verknüpfte Artefakte

- `projekte/rentenversicherung/reformkonzept.md`
- `projekte/rentenversicherung/pruefberichte/2026-06-04-abschmelzmodell-bundeszuschuss.md`
- `analysen/2026-06-04-bundeszuschuss-abschmelzung.md`
- `analysen/daten/2026-06-04-bundesmittel-zerlegung.csv`
