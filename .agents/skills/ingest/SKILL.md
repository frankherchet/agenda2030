---
name: ingest
description: Fügt neue Dokumente, Links, Notizen, Bundestagsdrucksachen und Ideen in das agenda2030-Repo ein, indem es sie als kompakte Markdown-Ingests ablegt und für spätere Maßnahmen-, Gesetzes- oder Drucksachen-Auswertung vorbereitet. Use when the user asks to ingest, erfassen, ablegen, hinzufügen, speichern, zusammenfassen, importieren, or process a source, URL, PDF, document, article, note, idea, reform proposal, or Bundestag Drucksache for later work in this repository.
---

# Ingest

## Overview

Neue Quellen token-sparend erfassen: nicht den Volltext in die Unterhaltung
ziehen, sondern eine kompakte Markdown-Datei im Repo anlegen. Jede Datei muss
Quelle, Kernaussage, Relevanz, Zuordnung und nächste Schritte enthalten.

Der Ingest ist die Brücke zwischen Rohquelle und gepflegtem Wissensbestand.
Rohquellen bleiben unverändert; das LLM pflegt daraus kompakte, verlinkte
Markdown-Artefakte. Gute Analysen aus der Unterhaltung dürfen nicht nur im Chat
bleiben, sondern werden als Ingest, Auswertung, Report, offene Frage oder
Wissensseiten-Update im Repo gesichert.

## Vorarbeit

Vor jedem Ingest:

1. `index.md`, `log.md` und `eingang/index/README.md` lesen oder gezielt
   durchsuchen.
2. Naheliegende Fachordner prüfen, zum Beispiel `rentenversicherung/`,
   `demographie/`, `bundeshaushalt/`, `reports/`, `pruefberichte/`,
   `ministerien/` und `gesetzbuecher/`.
3. Prüfen, ob die Quelle neue Fakten liefert, bestehende Aussagen stützt,
   bestehende Aussagen widerspricht oder nur Kontext ohne spätere Relevanz ist.
4. Bei fehlender fachlicher Relevanz die Quelle trotzdem sauber erfassen, aber
   die geringe Relevanz und mögliche Nichtverwendung offen benennen.

## Workflow

1. Quelle identifizieren: Dokument, Link, Idee, Notiz oder Bundestagsdrucksache.
2. Zielordner wählen:
   - Bundestagsdrucksache: `bundestag-drucksachen/zusammenfassungen/`
   - sonstiges Dokument oder Bericht: `eingang/dokumente/`
   - URL ohne abgelegte Datei: `eingang/links/`
   - eigener Gedanke oder Reformskizze: `eingang/ideen/`
   - kleine Rohdatei zusätzlich unter `eingang/originale/`
3. Dateinamen bilden: `YYYY-MM-DD-kurzer-slug.md`.
4. Markdown mit der passenden Vorlage erstellen:
   - allgemeiner Ingest: `vorlagen/ingest.md`
   - Bundestagsdrucksache: `vorlagen/drucksache-zusammenfassung.md`
5. Zusammenfassung knapp halten: maximal 5 Sätze plus wenige Stichpunkte.
6. Betroffene Ministerien, Gesetzbücher, Fachordner, Reports, Auswertungen,
   Prüfberichte und Folgearbeiten als Repo-Pfade verlinken, wenn erkennbar.
7. Ingest-Datei in `eingang/index/README.md` eintragen.
8. `index.md` aktualisieren, wenn eine dauerhaft relevante Wissensseite neu
   entsteht, wesentlich verändert wird oder erstmals zentral verknüpft werden
   sollte.
9. `log.md` append-only ergänzen.
10. In allen späteren Artefakten, die diese Quelle nutzen, `ingest_refs` auf
   die Eingang-Datei setzen.
11. Offene Fragen sichtbar lassen, statt unsichere Fakten zu glätten.

## Kontextverknüpfung

Jeder Ingest enthält oder ergänzt sinngemäß:

- `Verknüpfte Wissensseiten`: repo-relative Pfade zu bestehenden Seiten, die
  durch die Quelle gestützt, ergänzt oder herausgefordert werden.
- `Mögliche Updates`: konkrete Folgearbeiten an Reports, Auswertungen,
  Fachordnern, Ministerien oder Gesetzbüchern.
- `Widersprüche/Risiken`: erkennbare Spannungen zu bestehenden Annahmen,
  veraltete Zahlen, unsichere Sprecherzuordnung, methodische Schwächen oder
  fehlende Primärquellen.

Bestehende Wissensseiten werden nur geändert, wenn die Relevanz klar ist. Bei
Unsicherheit wird ein TODO oder eine offene Frage im Ingest hinterlassen.

## Pflicht vor Quellenverwendung

- Eine externe Quelle darf erst fachlich verwendet werden, nachdem sie unter
  `eingang/<typ>/` erfasst und im Index vermerkt wurde.
- `source_urls` bleiben als externe Nachweise erhalten, ersetzen aber niemals
  `ingest_refs`.
- Mehrere Reports oder Auswertungen dürfen dieselbe Ingest-Datei referenzieren.
- Der globale `index.md` ersetzt nicht den Eingangsindex; beide sind bei einem
  Ingest auf notwendige Updates zu prüfen.
- `log.md` ist chronologisch und append-only.

## Token-Sparing Rules

- Do not paste long source text into the answer.
- Store extracted or user-provided substance in Markdown and summarize only the
  working-relevant points.
- Preserve exact source URL, filename, Drucksachennummer, author and date when
  available.
- Quote only short excerpts when exact wording matters.
- Prefer bullets over prose for later machine processing.
- Use `TODO:` markers for missing metadata instead of inventing details.
- Prefer links to existing repo artifacts over free-text references.

## Ingest-Lint

Vor Abschluss jedes Ingests kurz prüfen:

- Wurden `index.md`, `log.md`, `eingang/index/README.md` und naheliegende
  Fachordner berücksichtigt?
- Sind Ministerien, Gesetze, Fachseiten und Folgearbeiten repo-relativ
  verlinkt?
- Sind mögliche Widersprüche, veraltete Aussagen oder ungesicherte Zahlen als
  offene Fragen sichtbar?
- Wurden Eingangsindex, globaler Index und Log aktualisiert oder bewusst als
  nicht betroffen bewertet?
- Bleibt die Rohquelle unverändert und traceable?

Ein tiefer Lint auf Widersprüche, orphan pages, veraltete Claims und fehlende
Querverweise läuft manuell bei Bedarf, nicht automatisch vor jedem Push.

## Destination Guidance

Read `references/ablageorte.md` only when the target folder or naming choice is
unclear.

## Output Standard

After creating or updating files, respond with:

- created/updated file paths,
- updated index/log paths,
- one-sentence summary of what was ingested,
- unresolved metadata or follow-up work.

Keep the final response short; the Markdown file is the durable artifact.

## Quality Bar

- The ingest file must be useful without reopening the original source.
- The original source must remain traceable.
- Zuordnungen must use existing repo folders where possible.
- Relevant existing knowledge pages must be checked and linked when applicable.
- If the source is current, legal, political, financial, or otherwise likely to
  change, verify it from a primary or official source when the user asks for
  factual extraction from a URL.
