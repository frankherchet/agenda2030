# Log

Chronologisches Arbeitslog für Ingests, Wissenspflege, Prüfungen und größere
Analysen. Das Log ist append-only: neue Einträge werden unten ergänzt.

## 2026-06-04 Ingest | Markus Lanz Sendung vom 2. Juni 2026

- Ingest: `eingang/dokumente/2026-06-04-markus-lanz-sendung-2026-06-02.md`
- Rohdatei: `eingang/originale/2026-06-04-markus-lanz-sendung-2026-06-02.json`
- Wirkung: Debattenquelle zu Renteneintrittsalter, Rentenniveau,
  Generationengerechtigkeit, AfD-Abgrenzung und FDP-Richtungskonflikt erfasst.

## 2026-06-04 Wissenspflege | Rohdateien im Eingang

- Neue Struktur: `eingang/originale/README.md`
- Wirkung: Kleine Rohdateien wie JSON, CSV, TXT und kleinere PDFs erhalten eine
  versionierte Ablage; große Medien bleiben außerhalb des Repos.

## 2026-06-05 Struktur | Codex-Skills verschoben

- Neuer Ort: `.agents/skills/`
- Wirkung: Repo-spezifische Skills liegen am von Codex CLI erwarteten Ort.

## 2026-06-05 Wissenspflege | LLM-Wiki-Regeln für Ingest

- Betroffene Regeln: `AGENTS.md`, `eingang/README.md`,
  `.agents/skills/ingest/SKILL.md`
- Neuer Index: `index.md`
- Wirkung: Ingests prüfen künftig kontextabhängig relevante Wissensseiten,
  verknüpfen Quellen mit bestehenden Artefakten und führen Index sowie Log.
