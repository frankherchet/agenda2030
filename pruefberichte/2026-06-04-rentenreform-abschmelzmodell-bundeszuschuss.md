---
title: Prüfung Rentenreform Abschmelzmodell Bundeszuschuss
date: 2026-06-04
type: pruefbericht
status: offen
reviewed_report: reports/rentenversicherung-reform-2026.md
reviewer: pruefer
source_urls:
  - https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Sterbefaelle-Lebenserwartung/Publikationen/_publikationen-innen-periodensterbetafel.html
  - https://www.deutsche-rentenversicherung.de/SharedDocs/Downloads/DE/Statistiken-und-Berichte/statistikpublikationen/statistikband_rente.pdf?__blob=publicationFile&v=5
  - https://www.deutsche-rentenversicherung.de/DRV/DE/Experten/Zahlen-und-Fakten/Kennzahlen-zur-Finanzentwicklung/kennzahlen-zur-finanzentwicklung_node.html?https=1
---

# Prüfung: Rentenreform Abschmelzmodell Bundeszuschuss

## Prüfurteil

- Status: offen
- Kurzbegründung: Die zuvor kritisierten Datenlücken zur tatsächlichen
  DRV-Alters- und Geschlechtsstruktur, zur Trennung nach Rentenarten, zur
  Knappschaft und zur 100+-Behandlung sind in einer reproduzierbaren
  Arbeitsfassung abgearbeitet. Nicht freigabefähig ist weiterhin die
  Bundesmittel-Zerlegung, weil sie eine Reformklassifikation darstellt und noch
  keine amtliche Zweckzerlegung nach Altlasten, neuen Staatsbeiträgen und
  echten Steuertransfers.

## Geprüfter Gegenstand

- Report: `reports/rentenversicherung-reform-2026.md`
- Input-Erzeugung: `scripts/build_drv_renten_inputs.py`
- Rechenmodell: `scripts/calc_rente_bundeszuschuss_abschmelzung.py`
- Datenbasis: `rentenversicherung/daten/2026-06-04-drv-rentenbestand-struktur.csv`
- Auswertung: `rentenversicherung/auswertungen/2026-06-04-bundeszuschuss-abschmelzung.md`
- Prüfdatum: 2026-06-04

## Quellenprüfung

| Behauptung/Zahl | Quelle im Report | Unabhängige Prüfung | Ergebnis |
| --- | --- | --- | --- |
| Sterblichkeit aus Destatis 2022/2024 | Destatis Periodensterbetafel | Original-XLSX liegt unter `demographie/originale/`; Tabellen `12613-b01` und `12613-b02` enthalten `lx`, `px` und Alter. | ok |
| DRV-Rentenbestand gesamt 31.12.2024 | DRV Statistikband Rente 2024 | Kontrollsumme aus CSV: 26.087.662 laufende Renten. | ok |
| Altersrenten | DRV Tabellen `40.00/40.01/40.02 G` | CSV-Summe: 18.919.641. | ok |
| Erwerbsminderungsrenten | DRV Tabellen `30.00/30.01/30.02 G` | CSV-Summe: 1.747.402. | ok |
| Hinterbliebenenrenten | DRV Tabelle `50.00 G` | CSV-Summe: 5.420.619, getrennt nach Witwen-, Witwer-, Waisen- und Erziehungsrenten. | ok |
| Knappschaft-Bahn-See | DRV Tabelle `1.00 G` | Aggregat separat erfasst: 1.570.011 Renten, davon 942.690 Altersrenten und 75.424 Erwerbsminderungsrenten. | ok, aber nur aggregiert |
| Startwert Bundesmittel 2025 | DRV-Rechnungsergebnisse im Report | `65,754 + 32,104 = 97,858` Mrd. Euro. | ok |
| Bundesmittel-Zerlegung | `2026-06-04-bundesmittel-zerlegung.csv` | CSV trennt heutige Zuschusspositionen und künftige Reformkategorien, aber nicht amtlich nach Zuschusszweck. | offen |

## Gegenrechnung

### Rechnung 1: Rentenbestand

- Datenquelle: `rentenversicherung/daten/2026-06-04-drv-rentenbestand-struktur.csv`
- Formel: Summe `rv_gesamt` nach Rentenart
- Ergebnis Reformer: `1.747.402 + 18.919.641 + 5.420.619 = 26.087.662`
- Ergebnis Prüfer: identisch
- Bewertung: ok

### Rechnung 2: Startwert Bestandsschutz-Zuschuss

- Datenquelle: `rentenversicherung/daten/2026-06-04-bundesmittel-zerlegung.csv`
- Formel: Summe aller Zeilen mit `abschmelzbar = ja`
- Ergebnis Reformer: `65,754 + 32,104 = 97,858 Mrd. Euro`
- Ergebnis Prüfer: identisch
- Bewertung: rechnerisch ok; Klassifikation bleibt politisch/rechtlich zu
  belegen.

### Rechnung 3: Monotonie

- Datenquelle: `rentenversicherung/daten/2026-06-04-bundeszuschuss-abschmelzung.csv`
- Formel: `Zuschuss(t+1) <= Zuschuss(t)`
- Ergebnis Reformer: Zuschuss sinkt von `97,858 Mrd. Euro` 2027 auf
  `1,648 Mrd. Euro` 2070.
- Ergebnis Prüfer: alle Jahreswerte erfüllen die Monotoniebedingung.
- Bewertung: technisch ok.

### Rechnung 4: 100+-Tail

- Datenquelle: Rechenskript und Destatis-Sterbetafel
- Formel: Offene Altersgruppen ab `100` und `105` werden mit `px` bei Alter 100
  fortgeschrieben.
- Ergebnis Prüfer: kein hartes Abschneiden bei Alter 100 mehr; die frühere
  Fehlerquelle ist geschlossen.
- Bewertung: ok als Arbeitsmodell; Sensitivität mit Sterblichkeitsverbesserung
  fehlt noch.

## Rechts- und Vollzugsprüfung

- Bestandsschutz: Die Regel "nur proportional zum Versterben" ist mit dem
  Schutz laufender Renten besser vereinbar als politische Pauschalkürzungen.
- Rentenarten: Altersrenten, Erwerbsminderung und Hinterbliebene werden jetzt
  getrennt modelliert; das reduziert den vorherigen Strukturfehler erheblich.
- Knappschaft: Die Trägertrennung ist vorhanden, aber nur aggregiert. Eine
  separate knappschaftliche Simulation braucht zusätzliche Alters- und
  Geschlechtsdaten.
- Bundesmittel: Kritisch bleibt, ob die gesamten heutigen Bundesmittel
  rechtlich als abschmelzbare Altlast behandelt werden dürfen. Dafür braucht
  der Report eine amtliche oder gutachterliche Zweckzerlegung.

## Blockerstatus

| Punkt | Status | Bewertung |
| --- | --- | --- |
| Echte DRV-Alters- und Geschlechtsstruktur | erledigt | Für Alters- und Erwerbsminderungsrenten umgesetzt; Hinterbliebene geschlechtsnah, Waisen/Erziehungsrenten hälftig modelliert. |
| Trennung nach Rentenarten | erledigt | Altersrenten, Erwerbsminderung, Hinterbliebene und Knappschaft sind separat erfasst. |
| Bundeszuschüsse zerlegen | teilweise offen | Quellpositionen sind getrennt; amtliche Zweckzerlegung fehlt. |
| Rentenbezieher ab 100 Jahren | erledigt | Offene Altersgruppen werden mit Tail-Regel fortgeschrieben. |

## Nachbesserungen

- Report darf die Bundesmittel-Zerlegung nur als Reformklassifikation
  bezeichnen, bis eine amtliche Zweckzerlegung vorliegt.
- Für spätere Haushaltsfreigabe sollte eine Sensitivität mit
  Sterblichkeitsverbesserung und eine separate knappschaftliche Altersstruktur
  ergänzt werden.
