# Gesetzbücher und Stammgesetze

Dieser Bereich sammelt Normstände und Änderungsvorschläge nach betroffenen
Gesetzbüchern oder zentralen Stammgesetzen. Wenn eine Maßnahme mehrere
Rechtsgebiete berührt, sollten die einzelnen Änderungen in den jeweiligen
Ordnern referenziert werden.

## Artefakttypen

- Normstand: abgelegter geltender Paragraphen- oder Artikeltext als lokaler
  Arbeitskontext. Normstand-Dateien sind keine Reformvorschläge.
- Gesetzesänderung: Analyse und konkreter Änderungsvorschlag zu einer
  bestehenden oder neuen Norm.

Vor jeder Sichtung, Analyse oder Änderung einer Norm muss der geltende Stand
unter `gesetzbuecher/<buch>/` abgelegt werden. Dateischema:

```text
<gesetz>-<norm>-stand-YYYY-MM-DD.md
```

Beispiel:

```text
gesetzbuecher/sgb/sgb-vi-paragraf-68-stand-2026-06-05.md
```

Normstand-Dateien verwenden `vorlagen/normstand.md`. Änderungsvorschläge
verwenden `vorlagen/gesetzesaenderung.md` und verweisen auf die passende
Normstand-Datei.

## Ordner

- `grundgesetz`: Grundgesetz.
- `bgb`: Bürgerliches Gesetzbuch.
- `stgb`: Strafgesetzbuch.
- `stpo`: Strafprozessordnung.
- `zpo`: Zivilprozessordnung.
- `hgb`: Handelsgesetzbuch.
- `ao`: Abgabenordnung.
- `sgb`: Sozialgesetzbücher.
- `baugb`: Baugesetzbuch.
- `aufenthg-asylg`: Aufenthaltsgesetz und Asylgesetz.
- `gwb`: Gesetz gegen Wettbewerbsbeschränkungen.
- `weitere-gesetze`: Fachgesetze ohne eigenen Ordner.

## Mindestangaben je Gesetzesänderung

- betroffene Norm
- referenzierte Normstand-Datei
- geltende Rechtslage
- Änderungsbedarf
- Formulierungsvorschlag
- Begründung
- Folgeänderungen
- verfassungsrechtliche Prüfung
- Umsetzungsfrist
