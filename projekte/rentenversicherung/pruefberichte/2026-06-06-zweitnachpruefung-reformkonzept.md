---
title: Zweitnachprüfung Reformkonzept Rentenversicherung
date: 2026-06-06
type: pruefbericht
status: offen
reviewed_report: projekte/rentenversicherung/reformkonzept.md
reviewer: pruefer
source_urls:
  - https://www.gesetze-im-internet.de/sgb_6/__68.html
  - https://www.gesetze-im-internet.de/sgb_6/__213.html
  - https://www.gesetze-im-internet.de/sgb_6/__291b.html
  - https://dserver.bundestag.de/btd/21/014/2101419.pdf
  - https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Geburten/Tabellen/lebendgeborene-geschlecht.html
  - https://www.deutsche-rentenversicherung.de/DRV/DE/Ueber-uns-und-Presse/Presse/Meldungen/2025/251111-kindererziehungszeiten-vaeter
  - https://www.bundesgesundheitsministerium.de/themen/pflege/online-ratgeber-pflege/leistungen-der-pflegeversicherung/leistungen-im-ueberblick/soziale-absicherung-fuer-pflegepersonen
ingest_refs:
  - ingest/links/2026-06-04-gesetze-im-internet-sgb-vi.md
  - ingest/dokumente/2026-06-05-bundestag-drs-21-1419-nicht-beitragsgedeckte-leistungen.md
  - ingest/links/2026-06-06-destatis-lebendgeborene-2024.md
  - ingest/links/2026-06-06-drv-kindererziehungszeiten-bund.md
  - ingest/links/2026-06-06-bmg-soziale-absicherung-pflegepersonen.md
  - ingest/links/2026-06-06-drv-pflegepersonen-rentenversicherung.md
---

# Zweitnachprüfung: Reformkonzept Rentenversicherung

## Prüfurteil

- Status: offen
- Kurzbegründung: Die zweite Nachbesserung behebt zwei wesentliche
  Prüferpunkte: Die Rentenwert-Budgetregel liegt nun als konkrete
  SGB-VI-Änderungsskizze vor, und die Haushaltswirkung echter öffentlicher
  Beiträge wird doppelfrei als Brutto-Ausweis, bestehende Finanzierung und
  Netto-Zusatzeffekt getrennt. Die Normstand-Textqualitätsreste sind an den
  beanstandeten Stellen bereinigt. Eine Freigabe ist trotzdem noch nicht
  vertretbar, weil das Rentenaltermodell weiter synthetisch ist, die
  Änderungsskizze noch nicht die notwendigen Folgeänderungen ausformuliert und
  die amtliche Zweckzerlegung 2024-2026 weiterhin nur als Negativbefund
  vorliegt.

## Geprüfter Gegenstand

- Report: `projekte/rentenversicherung/reformkonzept.md`
- Geprüfter Stand: Commit `cf94328`
- Prüfdatum: 2026-06-06
- Neue Nachbesserungsartefakte:
  - `gesetzbuecher/sgb/sgb-vi-paragraf-68-stand-2026-06-06.md`
  - `gesetzbuecher/sgb/sgb-vi-paragraf-68-rentenwert-budgetregel-aenderung-2026-06-06.md`
  - `analysen/daten/2026-06-06-staatsbeitraege-doppelfrei-bruecke.csv`
  - `scripts/calc_rentenreform_freigabeblocker.py`

## Quellenprüfung

| Behauptung/Zahl | Quelle im Report | Unabhängige Prüfung | Ergebnis |
| --- | --- | --- | --- |
| § 68 SGB VI ist als Normstand für die Rentenwertmechanik abgelegt | `gesetze-im-internet.de`, lokale Normstand-Datei | Normstand enthält `source_urls`, `ingest_refs`, Abrufdatum und eine nachvollziehbare lokale Fassung der §-68-Mechanik. | ok |
| Die Rentenwert-Budgetregel ist nicht mehr nur Formel, sondern SGB-VI-Skizze | Änderungsskizze zu § 68 und § 213a | Skizze enthält Budgetfaktor, Referenzausgaben, Nominalschutz, Nachholbetrag und Verordnungsermächtigung. | ok als Arbeitsfassung |
| Bundesmittel-Zweckzerlegung 2024-2026 fehlt weiterhin öffentlich | Bundestagsdrucksache 21/1419 | Die Drucksache bestätigt fehlende Zahlen für 2024/2025 und keine haushaltsrelevante NBL-Berechnungsgröße für 2026. | ok als Negativbefund |
| Echte Staatsbeiträge werden doppelfrei abgegrenzt | Brücken-CSV | CSV trennt Brutto-Ausweis, bereits enthaltene Finanzierung und Netto-Zusatzeffekt; Netto ist für alle vier Kategorien 0. | ok mit Begrenzung |
| Normstand-Textreste wurden bereinigt | SGB-VI-Normstand-Dateien | Suche nach den vorherigen Extraktionsmustern findet keine Treffer mehr. | ok |

## Gegenrechnung

### Rechnung 1: Rentenwert-Budgetfaktor

- Datenquelle: `analysen/daten/2026-06-06-rentenreform-freigabeblocker.csv`
- Formel: `min(1, (Beitragsbasis * Beitragssatz + Bestandsschutz + sonstige Einnahmen) / Referenzausgaben)`
- Ergebnis Prüfer: Die Werte sind aus den CSV-Spalten reproduzierbar; minimale
  Abweichungen von 0,000001 bis 0,000002 entstehen durch bereits gerundete
  CSV-Eingangsspalten.

| Jahr | Variante | CSV-Faktor | Gegenrechnung | Saldo Mrd. Euro |
| ---: | --- | ---: | ---: | ---: |
| 2035 | Status quo 67 | 0,893752 | 0,893753 | -64,930 |
| 2035 | Lebenserwartung 2:1 | 0,950357 | 0,950358 | -28,632 |
| 2035 | Dänemark-nah | 1,000000 | 1,000000 | 7,085 |
| 2039 | Status quo 67 | 0,800503 | 0,800504 | -141,995 |
| 2039 | Lebenserwartung 2:1 | 0,873270 | 0,873270 | -83,102 |
| 2039 | Dänemark-nah | 0,957916 | 0,957917 | -25,238 |
| 2050 | Status quo 67 | 0,745392 | 0,745391 | -232,915 |
| 2050 | Lebenserwartung 2:1 | 0,874672 | 0,874670 | -98,534 |
| 2050 | Dänemark-nah | 0,948926 | 0,948925 | -37,090 |
| 2070 | Status quo 67 | 0,715175 | 0,715175 | -411,210 |
| 2070 | Lebenserwartung 2:1 | 0,969732 | 0,969732 | -32,643 |
| 2070 | Dänemark-nah | 1,000000 | 1,000000 | 8,566 |

Bewertung: rechnerisch ok. Der Prüferhinweis bleibt aber: Die politische
Wirkung ist eine teils deutliche Dämpfung gegenüber dem Referenzpfad, nicht
eine Finanzierungswunderlösung.

### Rechnung 2: Doppelfreie Haushaltsbrücke

- Datenquelle:
  `analysen/daten/2026-06-06-staatsbeitraege-doppelfrei-bruecke.csv`
- Formel: `Netto-Zusatzeffekt = Brutto-Ausweis - bereits in DRV-Finanzierung`
- Ergebnis:

| Jahr | Brutto-Ausweis | bereits enthalten | Netto-Zusatzeffekt |
| ---: | ---: | ---: | ---: |
| 2035 | 40,720 | 40,720 | 0,000 |
| 2039 | 44,949 | 44,949 | 0,000 |
| 2050 | 58,976 | 58,976 | 0,000 |
| 2070 | 96,639 | 96,639 | 0,000 |

Bewertung: Die frühere Doppelzählungsgefahr ist für die vier modellierten
Kategorien bereinigt. Gleichzeitig bedeutet das: Diese Tabelle liefert keinen
zusätzlichen Finanzierungsspielraum für den Budgetfaktor. Neue Haushaltslasten
entstehen erst bei zusätzlichen Sozialzeiten, höheren Bemessungsgrundlagen oder
weiteren Zahlungspflichten.

### Rechnung 3: Rentenaltermodell

- Datenquelle:
  `analysen/daten/2026-06-06-rentenalter-feinmodell-altersjahre.csv`
- Bewertung: Das Modell ist als Sensitivität nachvollziehbar, bleibt aber
  nicht freigabefähig als Entscheidungsrechnung. Es nutzt synthetische
  Altersjahrkohorten, pauschale Erwerbsquoten und einen Senior-Wage-Faktor.
  Amtliche feinjährige Bevölkerung, altersspezifische Erwerbsquoten,
  Rentenzugänge, Abschläge, Erwerbsminderung und Berufsbelastungen fehlen.

## Normstand-Prüfung

Geprüfte Normstände:

- `gesetzbuecher/sgb/sgb-vi-paragraf-68-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-77-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-235-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-236-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-236a-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-237-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-213-stand-2026-06-05.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-291b-stand-2026-06-05.md`

Befund: Der frühere Normstand-Blocker ist für die aktuell genutzten
Kernnormen formal erledigt. Die konkrete §-68-Skizze benennt aber selbst
Folgeänderungen zu § 69, § 158, § 177, § 213 und § 291b; diese sind noch nicht
als ausformulierte Gesetzesänderungen geprüft. Das verhindert die Freigabe des
Gesamtprojekts, nicht aber die Weiterarbeit an der Skizze.

## Rechtsprüfung

- Zuständigkeit: Für § 68 SGB VI und Bundeszuschüsse grundsätzlich tragfähig.
- Bestimmtheit: Die Budgetklausel ist deutlich konkreter als vorher. Kritisch
  bleibt, dass zentrale Detailgrößen in eine Rechtsverordnung verlagert werden:
  Referenzausgaben, Datengrundlagen, Rundung und Nachholbetrag müssen im Gesetz
  hinreichend vorgezeichnet werden.
- Eigentum/Vertrauensschutz: Nominalschutz ist ein wichtiger Fortschritt. Die
  Dämpfung künftiger Anpassungen kann trotzdem verfassungsrechtlich sensibel
  sein, wenn sie über viele Jahre ein erhebliches Nachholkonto aufbaut.
- Gleichheit: Die Kopplung des Rentenalters braucht Sonderpfade für
  Erwerbsminderung, Schwerbehinderung, lange Versicherungszeiten und Gruppen
  mit niedrigerer gesunder Lebenserwartung.
- Haushalt: Die neue Brückenrechnung ist sauberer, zeigt aber gerade keinen
  Nettofinanzierungsbeitrag. Die Bundesmittel-Zweckzerlegung bleibt wegen der
  öffentlichen Datenlage offen.
- Vollzug: Die Trennung von Bestandsschutz-Zuschuss, echten Beiträgen und
  Steuertransfers braucht jährliche Rechnungslegung, Trägerkonten,
  Prüfverfahren und klare Sanktionen bei Zahlungsausfall öffentlicher Träger.

## Kritische Gegenposition

Die stärkste Gegenposition lautet nun nicht mehr, dass das Konzept seine
Kosten versteckt. Im Gegenteil: Die zweite Nachbesserung macht sichtbar, dass
die Reform vor allem eine harte Budgetregel ist. Wenn keine zusätzlichen
Netto-Mittel entstehen und das Rentenaltermodell nur teilweise entlastet, wird
der Rentenwert relativ zum Referenzpfad gedämpft. Das ist ehrlich, aber
politisch und sozial schwer: Die Reform stabilisiert Beiträge nur, wenn
Versicherte längere Erwerbsphasen akzeptieren, Rentenanpassungen niedriger
ausfallen oder der Staat echte zusätzliche Mittel bereitstellt.

## Blocker

- Keine arithmetischen Blocker in den geprüften Rechenartefakten.
- Kein Normstand-Blocker für § 68, § 77, §§ 235-237a, § 213 und § 291b.
- Freigabe bleibt offen, weil die Rentenalterrechnung weiterhin synthetisch
  ist und keine empirische feinjährige Entscheidungsrechnung ersetzt.
- Freigabe bleibt offen, weil die §-68-Skizze noch keine vollständigen
  Folgeänderungen zu Beitragssatz, Rentenwertfestsetzung, Bundesmitteln,
  Kindererziehungszeiten und Haltelinien-Erstattung enthält.
- Freigabe bleibt offen, weil die Bundesmittel-Zweckzerlegung 2024-2026 nur
  als belastbarer Negativbefund vorliegt, nicht als amtliche Datenbasis.

## Offene Punkte

- Feinjähriges Rentenaltermodell mit amtlichen Alters-, Erwerbs-,
  Rentenzugangs-, Abschlags- und Erwerbsminderungsdaten.
- Gesetzesänderungsskizzen für § 69, § 158, § 177, § 213 und § 291b SGB VI.
- Vollzugsmodell für § 213a: Kontierung, Meldung, Prüfung, Fälligkeit und
  Sanktionierung öffentlicher Zahlungspflichten.
- Kapitalmarktbaustein weiterhin nur konzeptionell; kein freigabefähiges
  Stammgesetz oder Aufsichtsmodell.

## Nachbesserungen

- Rentenaltermodell mit amtlichen feinjährigen Daten ersetzen oder als
  ausdrücklich nicht freigaberelevante Sensitivität aus dem Kernkonzept
  herauslösen.
- Folgeänderungen zur §-68-Budgetregel als eigene Änderungsskizzen anlegen.
- Für § 213a ein Vollzugs- und Rechnungslegungskapitel ergänzen.
- Danach erneut prüfen; eine Freigabe des Gesamtprojekts ist erst mit
  empirischer Rentenalterrechnung und vollständigerer Gesetzessystematik
  vertretbar.
