# Analysen

Dieser Ordner enthält zweckgebundene Auswertungen, Rechenberichte und
Datenartefakte. Eine Analyse wird nur angelegt, wenn sie eine konkrete Frage
beantwortet oder ein Projekt belastbar vorbereitet.

## Regeln

- Jede Analyse nennt ihren Zweck.
- Externe Quellen werden über `ingest_refs` oder repo-relative Ingest-Pfade
  referenziert.
- Rechtsanalysen verweisen auf vorher abgelegte Normstände unter
  `gesetzbuecher/`.
- Reproduzierbare Rechnungen verweisen auf Skripte unter `scripts/` und
  erzeugte Dateien unter `analysen/daten/`.

## Daten

`analysen/daten/` enthält CSV- oder JSON-Artefakte, die von Skripten erzeugt
oder für Analysen als strukturierter Input genutzt werden.
