# Log

Chronologisches Arbeitslog für Ingests, Wissenspflege, Prüfungen und größere
Analysen. Das Log ist append-only: neue Einträge werden unten ergänzt.

## 2026-06-04 Ingest | Markus Lanz Sendung vom 2. Juni 2026

- Ingest: `ingest/dokumente/2026-06-04-markus-lanz-sendung-2026-06-02.md`
- Rohdatei: `ingest/originale/2026-06-04-markus-lanz-sendung-2026-06-02.json`
- Wirkung: Debattenquelle zu Renteneintrittsalter, Rentenniveau,
  Generationengerechtigkeit, AfD-Abgrenzung und FDP-Richtungskonflikt erfasst.

## 2026-06-04 Wissenspflege | Rohdateien im Ingest

- Neue Struktur: `ingest/originale/README.md`
- Wirkung: Kleine Rohdateien wie JSON, CSV, TXT und kleinere PDFs erhalten eine
  versionierte Ablage; große Medien bleiben außerhalb des Repos.

## 2026-06-05 Struktur | Codex-Skills verschoben

- Neuer Ort: `.agents/skills/`
- Wirkung: Repo-spezifische Skills liegen am von Codex CLI erwarteten Ort.

## 2026-06-05 Wissenspflege | LLM-Wiki-Regeln für Ingest

- Betroffene Regeln: `AGENTS.md`, `ingest/README.md`,
  `.agents/skills/ingest/SKILL.md`
- Neuer Index: `index.md`
- Wirkung: Ingests prüfen künftig kontextabhängig relevante Wissensseiten,
  verknüpfen Quellen mit bestehenden Artefakten und führen Index sowie Log.

## 2026-06-05 Wissenspflege | Normstände vor Rechtsanalyse

- Neue Vorlage: `vorlagen/normstand.md`
- Betroffene Regeln: `AGENTS.md`, `gesetzbuecher/README.md`,
  `.agents/skills/reformer/SKILL.md`, `.agents/skills/pruefer/SKILL.md`
- Wirkung: Konkret analysierte oder geänderte Paragraphen und Artikel müssen
  künftig vorab als geltender Normstand unter `gesetzbuecher/<buch>/`
  abgelegt und von Folgeartefakten referenziert werden.

## 2026-06-05 Wissenspflege | Ingest-Extraktion geschärft

- Betroffene Regeln: `AGENTS.md`, `ingest/README.md`,
  `.agents/skills/ingest/SKILL.md`, `vorlagen/ingest.md`
- Wirkung: Ingests trennen künftig Inhaltsinventar der Quelle von aktuell
  extrahierten relevanten Informationen, um erneutes Nachschlagen im Original
  zu minimieren.

## 2026-06-05 Struktur | Quellen, Analysen und Projekte getrennt

- Neue Struktur: `ingest/`, `analysen/`, `projekte/rentenversicherung/`
- Verschoben: Haushalts-, Demographie- und DRV-Quellen in `ingest/`,
  zweckgebundene Auswertungen und Datenartefakte in `analysen/`, erstes
  Reformkonzept samt Prüfbericht in `projekte/rentenversicherung/`.
- Wirkung: Quellen werden unabhängig vom Thema einheitlich ingestiert;
  Analysen brauchen einen Zweck und Reformarbeit läuft projektbezogen.

## 2026-06-05 Prüfung | Strukturumbau nachgezogen

- Prüfvermerk:
  `analysen/2026-06-05-strukturumbau-quellen-analysen-projekte-pruefung.md`
- Betroffene Dateien: Analyse-Frontmatter, Rentenprojekt-Status,
  DRV-Quellenmetadaten, `index.md`, `analysen/README.md`
- Wirkung: Bestehende Analysen führen jetzt maschinenlesbare `source_urls` und
  `ingest_refs`; das offene Rentenkonzept ist nicht mehr als veröffentlicht
  markiert. Offene Nachpflege: Ingests um die neuen Extraktionsabschnitte und
  Rentennormstände ergänzen.

## 2026-06-05 Nachpflege | TODO-Liste und Renten-Ingests

- TODO-Liste: `analysen/2026-06-05-todo-strukturumbau-nachpflege.md`
- Normstand-Matrix: `projekte/rentenversicherung/normstand-bedarf.md`
- Wirkung: Alle im Rentenkonzept direkt referenzierten Ingests führen jetzt
  `Enthaltene Informationen` und `Jetzt extrahierte relevante Informationen`.
  Der verbleibende Rechtsblock ist als priorisierte Normstand-Matrix
  dokumentiert.

## 2026-06-05 Nachpflege | TODO-Liste abgearbeitet

- Gelöscht: `analysen/2026-06-05-todo-strukturumbau-nachpflege.md`
- Neue Ingests:
  `ingest/dokumente/2026-06-05-bmas-rentenversicherungsbericht-2025.md`,
  `ingest/dokumente/2026-06-05-drv-rentenupdate-bundeszuschuesse-nicht-beitragsgedeckte-leistungen-2025.md`,
  `ingest/dokumente/2026-06-05-bundestag-drs-21-1419-nicht-beitragsgedeckte-leistungen.md`
- Neue Analyse:
  `analysen/2026-06-05-bundesmittel-zweckzerlegung-rente.md`
- Normstände: 63 Dateien unter `gesetzbuecher/sgb/` und
  `gesetzbuecher/grundgesetz/` für das Rentenprojekt angelegt.
- Wirkung: Die alte TODO-Liste ist in dauerhafte Ingest-, Analyse- und
  Normstand-Artefakte überführt.

## 2026-06-05 Skill | Analyse-Rolle ergänzt

- Neuer Skill: `.agents/skills/analyse/SKILL.md`
- Betroffene Übersicht: `agenten/README.md`, `index.md`
- Wirkung: Themen können künftig als quellenbasierte Faktenanalysen unter
  `analysen/` aufgearbeitet werden, bevor daraus Reformkonzepte oder
  Prüfberichte entstehen.

## 2026-06-05 Ingest | Statista Altersrentner und Beitragszahler

- Ingest:
  `ingest/links/2026-06-05-statista-altersrentner-beitragszahler-rentenversicherung.md`
- Quelle:
  https://de.statista.com/infografik/25751/altersrentner-und-beitragszahler-in-der-rentenversicherung-in-deutschland/
- Wirkung: Sekundäre Visualisierungsquelle zum Verhältnis von Altersrentnern
  und Beitragszahlern erfasst; quantitative Nutzung bleibt gegen
  DRV-Primärdaten zu prüfen.

## 2026-06-05 Analyse | Rentenproblem Deutschland

- Analyse:
  `analysen/2026-06-05-rentenproblem-deutschland-ursachen-auswirkungen.md`
- Verwendete Quellen: BMAS-Rentenversicherungsbericht 2025,
  Destatis-Demographie, DRV-Finanzkennzahlen, DRV-rentenupdate zu
  Bundeszuschüssen, Bundestagsdrucksache 21/1419 und Statista als sekundäre
  Visualisierungsquelle.
- Wirkung: Ursachen und Folgen des deutschen Rentenproblems ohne
  Gegenmaßnahmen sind als quellenbasierter Problemaufriss dokumentiert;
  offene Datenlücken zur Beitragszahler-Relation, Tabellenextraktion und
  Bundesmittel-Zweckzerlegung bleiben sichtbar.

## 2026-06-05 Rechenartefakt | Finanzierungslücke Rentenproblem

- Skript:
  `scripts/calc_rentenproblem_finanzierungsluecke.py`
- Neue Daten:
  `analysen/daten/2026-06-05-rentenproblem-finanzierungsluecke.csv`,
  `analysen/daten/2026-06-05-rentenproblem-finanzierungsluecke-annahmen.csv`
- Neue Diagramme:
  `analysen/diagramme/2026-06-05-rentenproblem-finanzierungsluecke.svg`,
  `analysen/diagramme/2026-06-05-rentenproblem-bundesmittelbedarf.svg`
- Wirkung: Die Analyse zum Rentenproblem weist nun eine reproduzierbare
  Hochrechnung aus, wie groß die jährliche Lücke wird, wenn Beitragssatz und
  Renteneintrittsalter unverändert bleiben.

## 2026-06-05 Web | Rentenproblem-Analyse als Pages-Report

- Veröffentlicht:
  `analysen/2026-06-05-rentenproblem-deutschland-ursachen-auswirkungen.md`
- Web-Änderungen:
  `web/scripts/build-content.mjs`, `web/src/App.tsx`, `web/src/styles.css`
- Wirkung: Der Content-Builder liest nun veröffentlichte Analysen unter
  `analysen/`, spiegelt referenzierte Diagramm-Assets in die GitHub-Pages-App
  und erzeugt einen Report mit Diagrammen für die Rentenproblem-Analyse.
