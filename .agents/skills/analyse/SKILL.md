---
name: analyse
description: Analysiert ein Thema im agenda2030-Repo quellenbasiert, sucht und bewertet relevante Quellen, legt externe Quellen zuerst als Ingests ab und erstellt daraus eine strukturierte Markdown-Analyse unter analysen/. Use when the user asks to analysieren, einordnen, erklaeren, darstellen, untersuchen, recherchieren, Quellen suchen, Überblick geben, Faktenlage klaeren, or ein Thema wie Rentenluecke, Rentenkosten, Pflegekosten, Wohnungsbau, Energiepreise or ähnliche Politik- und Gesellschaftsthemen strukturiert aufbereiten.
---

# Analyse

## Overview

Erstelle quellenbasierte Themenanalysen, keine Reformkonzepte und keine
Prüferberichte. Ziel ist ein belastbarer Faktenüberblick: Begriff, Datenlage,
Entwicklung, Ursachen, Akteure, Unsicherheiten, offene Fragen und relevante
Folgearbeiten.

## Abgrenzung

- Nutze `ingest`, sobald externe Quellen fachlich verwendet werden.
- Nutze `reformer` erst, wenn aus der Analyse ein Reformmodell, eine
  Gesetzesänderung, ein Finanzmodell oder eine konkrete Maßnahme entstehen
  soll.
- Nutze `pruefer` erst, wenn ein bestehendes Artefakt kritisch geprüft oder
  freigegeben werden soll.
- Analysen sind Arbeitsstände. Behaupte keine Veröffentlichungsfreigabe.

## Workflow

1. Thema und Leitfrage präzisieren.
2. Vorarbeit im Repo:
   - `index.md`
   - `log.md`
   - `ingest/index/README.md`
   - naheliegende Dateien in `analysen/`, `projekte/`, `ministerien/` und
     `gesetzbuecher/`
3. Bestehende Quellen und Analysen wiederverwenden, statt neu zu duplizieren.
4. Fehlende externe Quellen recherchieren.
5. Jede externe Quelle vor fachlicher Nutzung ingestieren:
   - Links nach `ingest/links/`
   - Dokumente und Berichte nach `ingest/dokumente/`
   - kleine Rohdateien zusätzlich nach `ingest/originale/`
6. Quellenlage bewerten:
   - amtlich oder primär
   - wissenschaftlich oder gutachterlich
   - journalistisch oder debattierend
   - Interessenquelle
7. Analyse unter `analysen/YYYY-MM-DD-<thema>.md` erstellen.
8. `source_urls`, `ingest_refs`, relevante Datenartefakte und Folgearbeiten im
   Frontmatter oder klar im Text dokumentieren.
9. `analysen/README.md`, `index.md` und `log.md` aktualisieren.
10. Offene Datenlücken und Widersprüche sichtbar lassen.

## Analyse-Artefakt

Neue Analysen verwenden diese Grundstruktur:

```markdown
---
title: <Titel>
date: <YYYY-MM-DD>
type: analyse
status: arbeitsfassung
source_urls:
  - <externe Quelle>
ingest_refs:
  - <repo-relativer Ingest-Pfad>
data_artifacts: []
related_projects: []
---

# <Titel>

## Leitfrage

## Kurzfassung

## Begriff und Abgrenzung

## Datenlage

## Entwicklung und Trends

## Ursachen und Treiber

## Betroffene Gruppen und Akteure

## Quellenlage und Belastbarkeit

## Unsicherheiten und Widersprüche

## Offene Fragen

## Mögliche Folgearbeiten
```

Kürze Abschnitte nur, wenn sie für das Thema offensichtlich nicht passen. Lasse
Datenlücken sichtbar, statt sie durch glatte Prosa zu verdecken.

## Zahlen und Berechnungen

Standard ist ein Faktenüberblick ohne eigenes Modell. Wenn mehr als einfache
Quellenzitate, Summen oder Prozentrechnungen nötig sind:

- Rechenskript unter `scripts/` anlegen.
- Datenartefakt unter `analysen/daten/` speichern.
- Analyse verweist auf Skript und Datenartefakt.
- Annahmen, Stichtag, Einheit und Sensitivität dokumentieren.

## Normen

Wenn konkrete Paragraphen oder Artikel analysiert werden:

- Vorher passenden Normstand unter `gesetzbuecher/` suchen.
- Falls fehlend, Normstand mit `vorlagen/normstand.md` anlegen.
- Analyse verweist auf die Normstand-Datei.
- Bloße Randverweise lösen keine Normstand-Pflicht aus.

## Quellenqualität

Bevorzugte Reihenfolge:

1. Amtliche oder primäre Quellen
2. Statistik- und Forschungsinstitutionen
3. Wissenschaftliche Studien oder Gutachten
4. Verbände und Interessenquellen, klar gekennzeichnet
5. Medienquellen nur für Debatte, Ereignisse oder öffentliche Aussagen

Bei aktuellen Zahlen immer Abrufdatum und Datenstand nennen.

## Output Standard

Nach Abschluss knapp melden:

- Analysepfad
- neu angelegte Ingests
- verwendete bestehende Quellen
- wichtigste Erkenntnis
- wichtigste offene Datenlücken
