---
name: ingest
description: Fügt neue Dokumente, Links, Notizen, Bundestagsdrucksachen und Ideen in das agenda2030-Repo ein, indem es sie als kompakte Markdown-Ingests ablegt und für spätere Maßnahmen-, Gesetzes- oder Drucksachen-Auswertung vorbereitet. Use when the user asks to ingest, erfassen, ablegen, hinzufügen, speichern, zusammenfassen, importieren, or process a source, URL, PDF, document, article, note, idea, reform proposal, or Bundestag Drucksache for later work in this repository.
---

# Ingest

## Overview

Neue Quellen token-sparend erfassen: nicht den Volltext in die Unterhaltung
ziehen, sondern eine kompakte Markdown-Datei im Repo anlegen. Jede Datei muss
Quelle, Kernaussage, Relevanz, Zuordnung und nächste Schritte enthalten.

## Workflow

1. Quelle identifizieren: Dokument, Link, Idee, Notiz oder Bundestagsdrucksache.
2. Zielordner wählen:
   - Bundestagsdrucksache: `bundestag-drucksachen/zusammenfassungen/`
   - sonstiges Dokument oder Bericht: `eingang/dokumente/`
   - URL ohne abgelegte Datei: `eingang/links/`
   - eigener Gedanke oder Reformskizze: `eingang/ideen/`
3. Dateinamen bilden: `YYYY-MM-DD-kurzer-slug.md`.
4. Markdown mit der passenden Vorlage erstellen:
   - allgemeiner Ingest: `vorlagen/ingest.md`
   - Bundestagsdrucksache: `vorlagen/drucksache-zusammenfassung.md`
5. Zusammenfassung knapp halten: maximal 5 Sätze plus wenige Stichpunkte.
6. Betroffene Ministerien, Gesetzbücher und Folgearbeiten als Repo-Pfade
   verlinken, wenn erkennbar.
7. Offene Fragen sichtbar lassen, statt unsichere Fakten zu glätten.

## Token-Sparing Rules

- Do not paste long source text into the answer.
- Store extracted or user-provided substance in Markdown and summarize only the
  working-relevant points.
- Preserve exact source URL, filename, Drucksachennummer, author and date when
  available.
- Quote only short excerpts when exact wording matters.
- Prefer bullets over prose for later machine processing.
- Use `TODO:` markers for missing metadata instead of inventing details.

## Destination Guidance

Read `references/ablageorte.md` only when the target folder or naming choice is
unclear.

## Output Standard

After creating or updating files, respond with:

- created/updated file paths,
- one-sentence summary of what was ingested,
- unresolved metadata or follow-up work.

Keep the final response short; the Markdown file is the durable artifact.

## Quality Bar

- The ingest file must be useful without reopening the original source.
- The original source must remain traceable.
- Zuordnungen must use existing repo folders where possible.
- If the source is current, legal, political, financial, or otherwise likely to
  change, verify it from a primary or official source when the user asks for
  factual extraction from a URL.
