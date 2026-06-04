# agenda2030

Wie Deutschland wieder fit gemacht werden kann.

Dieses Repo sammelt konkrete Maßnahmen, Reformvorschläge und notwendige
Gesetzesänderungen für Deutschland. Die Struktur trennt fachliche
Zuständigkeiten nach Bundesministerien und rechtliche Änderungen nach
Gesetzbüchern beziehungsweise relevanten Stammgesetzen.

## Struktur

- `ministerien/`: Maßnahmen nach Ressortzuständigkeit.
- `gesetzbuecher/`: notwendige Änderungen nach Gesetzbuch oder Stammgesetz.
- `bundestag-drucksachen/`: abgelegte Bundestagsdrucksachen und kompakte
  Zusammenfassungen.
- `bundeshaushalt/`: Haushaltsdaten, Einnahmen, Ausgaben und Auswertungen des
  Bundes.
- `demographie/`: Bevölkerungsdaten, Altersstruktur und Vorausberechnungen als
  wiederverwendbare Inputquelle für Sozialversicherungen.
- `eingang/`: neue Dokumente, Links und Ideen als Markdown für die weitere
  Verarbeitung.
- `index.md`: globaler Wissensindex für wiederverwendbare Wissensseiten,
  Reports, Auswertungen und Prüfberichte.
- `log.md`: chronologisches Arbeitslog für Ingests, Wissenspflege, Analysen und
  Prüfungen.
- `agenten/`: Rollen, Workflow und Freigaberegeln für Reformer und Prüfer.
- `pruefberichte/`: unabhängige Prüfberichte zu Reformvorhaben.
- `reports/`: ausgearbeitete, veröffentlichbare Reform- und Analyseberichte.
- `rentenversicherung/`: Daten und Auswertungen zur gesetzlichen
  Rentenversicherung.
- `scripts/`: reproduzierbare Berechnungen für Reformberichte und
  Auswertungen.
- `.agents/skills/`: repo-spezifische Codex-Skills für Codex CLI.
- `web/`: Vite-React-App für GitHub Pages und interaktive Reports.
- `vorlagen/`: einheitliche Arbeitsvorlagen für neue Vorschläge.

## GitHub Pages

Freigegebene Reports werden aus Markdown gebaut. Dafür muss eine
Zusammenfassung im Frontmatter `publish: true` setzen. GitHub Actions erzeugt
daraus die Datenbasis für die Vite-React-App und veröffentlicht `web/dist` auf
GitHub Pages.

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

Neue Inhalte sollten zunächst mit den Vorlagen in `vorlagen/` angelegt und
anschließend dem passenden Ministeriums- und Gesetzbuchordner zugeordnet
werden.

## Stand der Ressortstruktur

Die Ministeriumsordner orientieren sich an der offiziellen Übersicht der
Bundesregierung mit 16 Bundesministerien, abgerufen am 2026-06-04.
