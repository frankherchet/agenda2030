---
title: Prüfung Rentenreform Abschmelzmodell Bundeszuschuss
date: 2026-06-04
type: pruefbericht
status: offen
reviewed_report: reports/rentenversicherung-reform-2026.md
reviewer: pruefer
source_urls:
  - https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Sterbefaelle-Lebenserwartung/Publikationen/_publikationen-innen-periodensterbetafel.html
  - https://statistik-rente.de/drv/extern/rente/rentenbestand/
  - https://www.deutsche-rentenversicherung.de/DRV/DE/Experten/Zahlen-und-Fakten/Statistiken-und-Berichte/statistiken_und_berichte.html
---

# Prüfung: Rentenreform Abschmelzmodell Bundeszuschuss

## Prüfurteil

- Status: offen
- Kurzbegründung: Die Modellregel ist fachlich richtig umgesetzt: Der
  Bestandsschutz-Zuschuss sinkt nicht politisch frei, sondern proportional zur
  erwarteten Überlebendenzahl einer Bestandskohorte. Die Rechnung ist
  reproduzierbar und der Zuschuss steigt in keinem Jahr. Für eine Freigabe
  fehlen jedoch die tatsächliche Alters- und Geschlechtsstruktur der
  Rentenbezieher am Reformstichtag sowie eine saubere Behandlung von
  Rentenbeziehenden unter 67 und ab 100 Jahren.

## Geprüfter Gegenstand

- Report: `reports/rentenversicherung-reform-2026.md`
- Rechenmodell: `scripts/calc_rente_bundeszuschuss_abschmelzung.py`
- Auswertung: `rentenversicherung/auswertungen/2026-06-04-bundeszuschuss-abschmelzung.md`
- Version/Commit: `1b1d031`
- Prüfdatum: 2026-06-04

## Quellenprüfung

| Behauptung/Zahl | Quelle im Report | Unabhängige Prüfung | Ergebnis |
| --- | --- | --- | --- |
| Sterblichkeit aus Destatis 2022/2024 | Destatis Periodensterbetafel | Original-XLSX liegt unter `demographie/originale/`; Tabellen `12613-b01` und `12613-b02` enthalten `lx` nach Alter und Geschlecht. | ok |
| Startwert Bundesmittel 2025: 97,858 Mrd. Euro | DRV-Kennzahlen im Report: 65,754 + 32,104 | Addition geprüft: `65,754 + 32,104 = 97,858`. | ok |
| Abschmelzung proportional zum Versterben | Rechenskript | Formel nutzt Überlebendenquote der modellierten Bestandskohorte und multipliziert diese mit dem Startwert. | ok |
| Tatsächliche Rentenbezieherstruktur | nicht enthalten | DRV-Rentenbestand weist Renten zum Stichtag aus; eine maschinenlesbare Alters-/Geschlechtsstruktur ist im Repo noch nicht abgelegt. | offen |
| Rentenbezieher unter 67 und ab 100 | nicht vollständig enthalten | v1 modelliert nur Altersjahre 67-100; Erwerbsminderungs-, Hinterbliebenen- und jüngere Renten sowie 100+ sind nicht ausreichend abgebildet. | problem |

## Gegenrechnung

### Rechnung 1: Startwert

- Datenquelle: Reporttabelle Einnahmen 2025
- Formel: `65,754 + 32,104`
- Ergebnis Reformer: `97,858 Mrd. Euro`
- Ergebnis Prüfer: `97,858 Mrd. Euro`
- Abweichung: `0,000 Mrd. Euro`
- Bewertung: ok

### Rechnung 2: Monotonie

- Datenquelle: `rentenversicherung/daten/2026-06-04-bundeszuschuss-abschmelzung.csv`
- Formel: `Zuschuss(t+1) <= Zuschuss(t)`
- Ergebnis Reformer: Zuschuss sinkt von `97,858 Mrd. Euro` 2027 auf
  `0,000 Mrd. Euro` 2070.
- Ergebnis Prüfer: alle 44 Jahreswerte erfüllen die Monotoniebedingung.
- Abweichung: keine
- Bewertung: technisch ok, aber inhaltlich noch nicht freigegeben.

### Rechnung 3: Modellannahme Altersstruktur

- Datenquelle: Rechenskript
- Formel: `70 % gleichverteilt 67-79, 30 % gleichverteilt 80-100`
- Ergebnis Reformer: Bestandsschutz-Zuschuss `56,166 Mrd. Euro` 2035,
  `37,031 Mrd. Euro` 2040 und `7,236 Mrd. Euro` 2050.
- Ergebnis Prüfer: Werte sind aus der Annahme reproduzierbar.
- Abweichung: keine rechnerische Abweichung.
- Bewertung: nicht freigabefähig, weil die Annahme nicht durch DRV-Bestandsdaten
  belegt ist und den Abschmelzpfad wesentlich bestimmt.

## Rechtsprüfung

- Zuständigkeit: Gesetzliche Änderungen an SGB VI und Haushaltszuordnung liegen
  beim Bund; die Grundlogik ist zuständigkeitskonform.
- Grundrechte/Verfassung: Bestandsschutz wird besser gewahrt als bei pauschaler
  Zuschusskürzung. Problematisch wäre nur eine faktische Unterfinanzierung
  bereits zugesagter Ansprüche.
- Übergangsrecht/Bestandsschutz: Regel "nur proportional zum Versterben" ist
  bestandsschutzfreundlich, muss aber exakt definieren, welche Rentenarten und
  welche Stichtagsansprüche zur geschützten Kohorte gehören.
- Vollzug: Ohne DRV-Bestandsdaten nach Alter, Geschlecht und Rentenart ist das
  Modell nicht vollzugs- und haushaltsfest.

## Kritische Gegenposition

Das Modell könnte den Bestandsschutz-Zuschuss zu schnell abschmelzen, wenn die
geschützte Kohorte tatsächlich jünger ist, wenn Hinterbliebenen- und
Erwerbsminderungsrenten anders auslaufen oder wenn der 100+-Tail unterschätzt
wird. Außerdem ist nicht belegt, dass der gesamte heutige Bundeszuschuss
vollständig proportional zum Tod aktueller Rentenbeziehender auslaufen darf;
ein Teil kann strukturelle oder jährlich neu entstehende Steuerfinanzierung
betreffen.

## Blocker

- Keine tatsächliche Alters- und Geschlechtsstruktur des Rentenbestands am
  Reformstichtag im Repo.
- Keine Abgrenzung nach Rentenarten: Altersrenten, Erwerbsminderungsrenten,
  Hinterbliebenenrenten und Knappschaft.
- Keine Zerlegung der heutigen Bundeszuschüsse in echte Altlasten,
  laufend neu entstehende Staatsbeiträge und Steuertransfers.
- 100+-Tail nicht modelliert.

## Offene Punkte

- DRV-Rentenbestand nach Alter, Geschlecht und Rentenart als Inputquelle
  ingestieren.
- Startwert `97,858 Mrd. Euro` nach Zuschusszweck zerlegen.
- Prüfszenario mit tatsächlicher Rentenbestandsstruktur und 100+-Tail rechnen.

## Nachbesserungen

- Report muss das Abschmelzmodell ausdrücklich als nicht freigegebenes
  Arbeitsmodell kennzeichnen.
- Die Ergebniszahlen dürfen nur als Sensitivität auf Basis der Ersatzverteilung
  erscheinen.
- Nächster Umsetzungsschritt ist ein Daten-Ingest des DRV-Rentenbestands 2024
  beziehungsweise der aktuellsten verfügbaren Stichtagsdaten.
