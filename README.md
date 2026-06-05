# agenda2030

Wie Deutschland wieder fit gemacht werden kann.

Dieses Repo sammelt konkrete Maßnahmen, Reformvorschläge und notwendige
Gesetzesänderungen für Deutschland. Quellen werden zuerst im Ingest erfasst,
Analysen werden zweckgebunden abgelegt, und konkrete Reformvorhaben laufen als
Projekte.

## Struktur

- `ministerien/`: Maßnahmen nach Ressortzuständigkeit.
- `gesetzbuecher/`: notwendige Änderungen nach Gesetzbuch oder Stammgesetz.
- `ingest/`: Quellen, Links, Ideen und Rohdateien mit extrahierten relevanten
  Informationen für spätere Nutzung.
- `analysen/`: zweckgebundene Auswertungen, Modelle und Datenartefakte mit
  Referenzen auf Ingests oder Normstände.
- `projekte/`: konkrete Reformprojekte mit Konzepten, Prüfberichten und
  Umsetzungsartefakten.
- `index.md`: globaler Wissensindex für wiederverwendbare Wissensseiten,
  Analysen, Projekte und Prüfberichte.
- `log.md`: chronologisches Arbeitslog für Ingests, Wissenspflege, Analysen und
  Prüfungen.
- `agenten/`: Rollen, Workflow und Freigaberegeln für Reformer und Prüfer.
- `scripts/`: reproduzierbare Berechnungen für Reformberichte und
  Auswertungen.
- `.agents/skills/`: repo-spezifische Codex-Skills für Codex CLI.
- `web/`: Vite-React-App für GitHub Pages und interaktive Reports.
- `vorlagen/`: einheitliche Arbeitsvorlagen für neue Vorschläge.

## GitHub Pages

Freigegebene Reports werden aus Markdown gebaut. Dafür muss eine
Zusammenfassung im Frontmatter `publish: true` setzen. Analysen unter
`analysen/` und freigegebene Projektartefakte können so als Report erscheinen.
GitHub Actions erzeugt daraus die Datenbasis für die Vite-React-App und
veröffentlicht `web/dist` auf GitHub Pages.

## Arbeitsregeln

Die verbindlichen Repo-Regeln stehen in `AGENTS.md`. Wichtigste Regel: Nach
jedem fertiggestellten Arbeitspaket werden alle Änderungen gestaged,
committed und auf das Remote-Repository gepusht.

## Arbeitsprinzip

Jeder Vorschlag sollte nachvollziehbar beschreiben:

- welches Problem gelöst werden soll,
- welche Maßnahme vorgeschlagen wird,
- welches Ministerium federführend wäre,
- welche Gesetzesänderungen notwendig sind,
- welche Kosten, Wirkungen und Risiken zu erwarten sind,
- welche Abhängigkeiten zu anderen Reformen bestehen.

Neue Quellen landen zuerst unter `ingest/`. Auswertungen mit einem klaren Zweck
landen unter `analysen/`. Reformkonzepte und Prüfberichte werden im passenden
Projekt unter `projekte/` geführt und verweisen repo-relativ auf Ingests,
Analysen und Normstände.

## Stand der Ressortstruktur

Die Ministeriumsordner orientieren sich an der offiziellen Übersicht der
Bundesregierung mit 16 Bundesministerien, abgerufen am 2026-06-04.
