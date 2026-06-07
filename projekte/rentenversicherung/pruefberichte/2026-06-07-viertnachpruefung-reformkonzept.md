---
title: Viertnachprüfung Reformkonzept Rentenversicherung
date: 2026-06-07
type: pruefbericht
status: offen
reviewed_report: projekte/rentenversicherung/reformkonzept.md
reviewer: pruefer
source_urls:
  - https://genesis.destatis.de/genesisWS/swagger-ui/index.html
  - https://www.gesetze-im-internet.de/sgb_6/__213.html
  - https://www.gesetze-im-internet.de/bho/__13.html
  - https://www.gesetze-im-internet.de/bho/__17.html
ingest_refs:
  - ingest/links/2026-06-06-destatis-genesis-api.md
  - ingest/dokumente/2026-06-07-destatis-genesis-demographie-rente-tabellen.md
  - ingest/links/2026-06-04-gesetze-im-internet-sgb-vi.md
  - ingest/links/2026-06-07-gesetze-im-internet-bho.md
---

# Viertnachprüfung: Reformkonzept Rentenversicherung

## Prüfurteil

- Status: offen
- Kurzbegründung: Die Nachbesserung nach der Drittnachprüfung behebt den
  arithmetischen Fehler in der GENESIS-Rentenalterrechnung und konkretisiert
  die Ausfallhaftung in § 213a zugunsten der Versicherten. Die BHO-Skizze
  adressiert den Haushaltsausweis echter öffentlicher Rentenbeiträge als
  Arbeitsfassung. Ich finde keine neuen arithmetischen Blocker. Eine Freigabe
  des Gesamtprojekts bleibt offen, weil das Rentenaltermodell weiterhin nur
  eine Sensitivität mit Erwerbsbrückenparameter ist und die amtliche
  Bundesmittel-Ist-Zweckzerlegung 2024-2026 weiterhin fehlt.

## Geprüfter Gegenstand

- Report: `projekte/rentenversicherung/reformkonzept.md`
- Geprüfter Stand: Commit `2884e1a`
- Prüfdatum: 2026-06-07
- Geprüfte Nachbesserungsartefakte:
  - `scripts/calc_rentenalter_genesis_empirisch.py`
  - `analysen/2026-06-07-rentenalter-genesis-empirisch.md`
  - `analysen/daten/2026-06-07-rentenalter-genesis-empirisch-summary.csv`
  - `gesetzbuecher/sgb/sgb-vi-paragraf-213a-vollzug-rechnungslegung-aenderung-2026-06-07.md`
  - `gesetzbuecher/weitere-gesetze/bho-rentenbeitraege-haushaltsausweis-aenderung-2026-06-07.md`

## Quellenprüfung

| Behauptung/Zahl | Quelle im Report | Unabhängige Prüfung | Ergebnis |
| --- | --- | --- | --- |
| GENESIS-Projektion wird nicht mehr nach Geschlecht doppelt gezählt | `scripts/calc_rentenalter_genesis_empirisch.py` | `load_projection()` verwirft alle Zeilen außer `row[2] == "Insgesamt"`; Rohdaten 2025 65-74 enthalten männlich 4.729,6 Tsd., weiblich 5.252,9 Tsd. und Insgesamt 9.982,6 Tsd. | ok |
| Erwerbsbrücke nutzt 65 bis unter 75 statt 65+ | GENESIS `12211-0004` | Rohdatenzeile `2025;Insgesamt;65 bis unter 75 Jahre` weist 1.650 Tsd. Erwerbstätige aus; Quotient gegen 9.982,6 Tsd. Bevölkerung 65-74 ergibt 16,5288 %. | ok als Brücke |
| Effektive Beitragszahler sind aus Brückenquote und Senior-Wage-Faktor abgeleitet | Summary-CSV | Stichproben 2035 und 2070 stimmen mit `nicht_in_rente_mio * 0,165288 * 0,85` auf 0,001 Mio. überein. | ok |
| § 213a schützt Versicherte bei Zahlungsverzug öffentlicher Träger | Änderungsskizze § 213a | Absatz 5 enthält vorläufige Gutschrift, Ausfallhaftung des Bundes und Verlagerung von Einwendungen ins Innenverhältnis. | ok als Arbeitsfassung |
| Haushaltsausweis echter öffentlicher Rentenbeiträge ist angelegt | BHO-Skizze | Skizze ergänzt § 17 BHO um getrennten Ausweis von echten Beiträgen, Bestandsschutz-Zuschüssen, Erstattungen, sonstigen Transfers sowie Ausfall- und Nachholzahlungen. | ok als Arbeitsfassung |

## Gegenrechnung

### Rechnung 1: Korrektur der 65-74-Erwerbsbrücke

- Datenquelle:
  `ingest/originale/2026-06-07-genesis-12211-0004-erwerbstaetige-altersgruppen.json`
  und
  `ingest/originale/2026-06-07-genesis-12421-0002-bev-v02-moderat.json`
- Formel:
  `Erwerbstätigenquote 65-74 = Erwerbstätige 65-74 / Bevölkerung 65-74`
- Ergebnis Reformer: 16,5 %
- Ergebnis Prüfer: `1.650 / 9.982,6 = 0,1652876`, also 16,5 %
- Abweichung: keine relevante Abweichung
- Bewertung: rechnerisch ok. Methodisch bleibt es eine Brücke, weil
  Erwerbstätige aus dem Mikrozensus mit der Destatis-Vorausberechnung als
  Nenner verbunden werden.

### Rechnung 2: Effektive Beitragszahler im moderaten Szenario

- Datenquelle:
  `analysen/daten/2026-06-07-rentenalter-genesis-empirisch-summary.csv`
- Formel: `nicht_in_rente_mio * 0,1652876 * 0,85`

| Jahr | Szenario | Nicht in Rente Mio. | Ergebnis Reformer effektiv | Ergebnis Prüfer effektiv |
| ---: | --- | ---: | ---: | ---: |
| 2035 | Lebenserwartung 2:1 | 1,201 | 0,169 | 0,169 |
| 2035 | dänemarknah | 2,413 | 0,339 | 0,339 |
| 2070 | dänemarknah | 4,711 | 0,662 | 0,662 |

Bewertung: Die korrigierten Werte sind intern konsistent. Der starke Rückgang
gegenüber der Drittnachprüfung ist plausibel, weil die Vorfassung männlich,
weiblich und Insgesamt zugleich summiert hatte.

## Normstand-Prüfung

Geprüfte Normstände und Rechtsartefakte:

- `gesetzbuecher/sgb/sgb-vi-paragraf-213-stand-2026-06-05.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-213a-vollzug-rechnungslegung-aenderung-2026-06-07.md`
- `gesetzbuecher/weitere-gesetze/bho-paragraf-13-stand-2026-06-07.md`
- `gesetzbuecher/weitere-gesetze/bho-paragraf-17-stand-2026-06-07.md`
- `gesetzbuecher/weitere-gesetze/bho-rentenbeitraege-haushaltsausweis-aenderung-2026-06-07.md`

Befund: Für die neu geprüften Punkte liegen Normstände vor. § 17 BHO trägt
die Ausweislogik besser als § 13 BHO; der §-13-Normstand ist für die
Gruppierungslogik ausreichend, aber nicht der entscheidende Änderungsträger.
Kein neuer Normstand-Blocker.

## Rechtsprüfung

- Zuständigkeit: Die Ergänzung von § 213a SGB VI und § 17 BHO ist als
  Bundesgesetzgebung grundsätzlich plausibel.
- Bestimmtheit: Die Ausfallhaftung ist jetzt als Schutzmechanismus sichtbar.
  Für einen Artikelgesetzentwurf müssten Schätzung, Rückgriff,
  Bund-Länder-/Trägerausgleich und Bundesratszustimmung noch genauer
  geregelt werden.
- Haushalt: Die BHO-Skizze verbessert die doppelfreie Abgrenzung künftiger
  Zahlungsströme. Sie ersetzt aber keine amtliche Ist-Zweckzerlegung der
  Bundesmittel 2024-2026.
- Vollzug: Der Versicherte wird nicht mehr durch Zahlungsverzug öffentlicher
  Träger belastet. Das verlagert Risiken in das Innenverhältnis zwischen Bund,
  zahlungspflichtigem Träger und Rentenversicherung; diese Rückgriffslogik ist
  noch nicht vollständig ausformuliert.
- Rentenalter: Das Konzept kennzeichnet die GENESIS-Rechnung inzwischen als
  Sensitivität. Damit ist sie nicht mehr der zentrale Freigabeanker, aber auch
  noch keine belastbare Entscheidungsrechnung für Altersgrenzen.

## Kritische Gegenposition

Die stärkste Gegenposition lautet: Das Konzept hat die formalen
Transparenzpunkte weitgehend abgearbeitet, zeigt aber noch nicht, dass die
politisch gewünschte Stabilität mit realer Erwerbsfähigkeit älterer Jahrgänge
erreichbar ist. Eine Quote für 65 bis unter 75 Jahre ist besser als 65+, aber
sie vermischt 65- und 66-Jährige mit den eigentlich reformrelevanten
67- bis 72-Jährigen. Genau diese Alter, Rentenarten, Abschläge und
Gesundheits-/Erwerbsminderungspfade entscheiden über Zumutbarkeit und
Finanzwirkung.

## Blocker

- Keine arithmetischen Blocker in der korrigierten GENESIS-Rechnung.
- Kein neuer Normstand-Blocker für § 213 SGB VI sowie BHO §§ 13 und 17.
- Der frühere Prüferpunkt zur fehlenden Ausfallhaftung ist als Arbeitsfassung
  erledigt.
- Der frühere Prüferpunkt zur Haushaltswirkung echter Staatsbeiträge ist für
  künftige Haushaltsausweise als Arbeitsfassung bearbeitet.
- Die Freigabe bleibt offen, weil die Rentenalterwirkung weiterhin nicht mit
  altersscharfen Erwerbs-, Rentenzugangs-, Abschlags- und
  Erwerbsminderungsdaten unterlegt ist.
- Die Freigabe bleibt offen, weil die amtliche Bundesmittel-Ist-Zweckzerlegung
  2024-2026 weiterhin fehlt.

## Offene Punkte

- DRV-Rentenzugangsdaten nach Alter, Rentenart, Zugangsfaktor, Abschlag,
  Erwerbsminderung, Schwerbehinderung und besonders langen
  Versicherungszeiten in das Rentenaltermodell einbauen.
- Amtliche oder belastbar dokumentierte Erwerbsquoten für 67 bis 72 Jahre
  beschaffen oder die Reformwirkung ausdrücklich nur als Szenariokorridor
  ausweisen.
- Rückgriff, Schätzung, Abschlagszahlung und föderale Lastenverteilung der
  §-213a-Ausfallhaftung in einem vollständigen Artikelgesetzentwurf regeln.
- Bundesmittel-Zweckzerlegung 2024-2026 weiter als Negativbefund führen, bis
  eine amtliche Quelle vorliegt; keine Ist-Zweckzerlegung aus der
  Reformklassifikation ableiten.

## Nachbesserungen

- Rentenalterblock für eine spätere Freigabe auf DRV-Rentenzugangsdaten und
  altersscharfe Erwerbsdaten stützen.
- § 213a und die BHO-Folgeänderung zu einem vollständigen
  Artikelgesetzentwurf mit Rückgriffs- und Haushaltsvollzug ausarbeiten.
- Im Reformkonzept den Status `offen` beibehalten und die GENESIS-Rechnung
  nur als Sensitivität verwenden, bis die genannten Datenlücken geschlossen
  sind.
