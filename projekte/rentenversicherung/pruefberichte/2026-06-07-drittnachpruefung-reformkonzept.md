---
title: Drittnachprüfung Reformkonzept Rentenversicherung
date: 2026-06-07
type: pruefbericht
status: offen
reviewed_report: projekte/rentenversicherung/reformkonzept.md
reviewer: pruefer
source_urls:
  - https://genesis.destatis.de/genesisWS/swagger-ui/index.html
  - https://www.gesetze-im-internet.de/sgb_6/__68.html
  - https://www.gesetze-im-internet.de/sgb_6/__69.html
  - https://www.gesetze-im-internet.de/sgb_6/__158.html
  - https://www.gesetze-im-internet.de/sgb_6/__177.html
  - https://www.gesetze-im-internet.de/sgb_6/__213.html
  - https://www.gesetze-im-internet.de/sgb_6/__291b.html
ingest_refs:
  - ingest/links/2026-06-06-destatis-genesis-api.md
  - ingest/dokumente/2026-06-07-destatis-genesis-demographie-rente-tabellen.md
  - ingest/links/2026-06-04-gesetze-im-internet-sgb-vi.md
---

# Drittnachprüfung: Reformkonzept Rentenversicherung

## Prüfurteil

- Status: offen
- Kurzbegründung: Die Nachbesserung vom 2026-06-07 behebt die alten
  Freigabepunkte zur synthetischen Bevölkerungsseite des Rentenaltermodells,
  zu fehlenden §-68-Folgeänderungen und zum fehlenden §-213a-Vollzug als
  Arbeitsfassung. Ich finde keine arithmetischen Blocker in der neuen
  GENESIS-Rechnung. Eine Freigabe des Gesamtprojekts bleibt aber nicht
  vertretbar, weil die Arbeitsmarkt- und Rentenzugangsseite des
  Rentenaltermodells weiter nur als Brücke modelliert ist und die amtliche
  Bundesmittel-Zweckzerlegung 2024-2026 weiterhin nicht öffentlich vorliegt.

## Geprüfter Gegenstand

- Report: `projekte/rentenversicherung/reformkonzept.md`
- Geprüfter Stand: Commit `16c4a13`
- Prüfdatum: 2026-06-07
- Neue Nachbesserungsartefakte:
  - `analysen/2026-06-07-rentenalter-genesis-empirisch.md`
  - `scripts/calc_rentenalter_genesis_empirisch.py`
  - `analysen/daten/2026-06-07-rentenalter-genesis-empirisch-altersjahre.csv`
  - `analysen/daten/2026-06-07-rentenalter-genesis-empirisch-summary.csv`
  - `gesetzbuecher/sgb/sgb-vi-folgeaenderungen-rentenwert-budgetregel-2026-06-07.md`
  - `gesetzbuecher/sgb/sgb-vi-paragraf-213a-vollzug-rechnungslegung-aenderung-2026-06-07.md`
  - `gesetzbuecher/sgb/sgb-vi-paragraf-69-stand-2026-06-07.md`

## Quellenprüfung

| Behauptung/Zahl | Quelle im Report | Unabhängige Prüfung | Ergebnis |
| --- | --- | --- | --- |
| Rentenaltermodell nutzt nun amtliche Altersjahrgänge statt synthetischer Kohorte | GENESIS-Ingest und Rohdaten `12411-0005`, `12421-0002` | Rohdaten enthalten Bevölkerungsstand nach Altersjahren sowie Vorausberechnung nach Variante, Geschlecht und Altersjahren. Das Skript summiert die Geschlechter je Altersjahr. | ok für Bevölkerung |
| 65+-Erwerbstätigenquote ca. 10,2 % und Erwerbspersonenquote ca. 10,4 % | GENESIS/Mikrozensus `12211-0002` | Zeile `2025;Insgesamt;65 Jahre und mehr`: Bevölkerung 18.045 Tsd., Erwerbstätige 1.843 Tsd., Erwerbspersonen 1.873 Tsd.; Quotienten 0,102131 und 0,103816. | ok als Brücke |
| §-68-Folgeänderungen liegen vor | Änderungsskizze vom 2026-06-07 | Skizze behandelt § 69, § 158, § 177, § 213 und § 291b und verlinkt passende Normstände. | ok als Arbeitsfassung |
| §213a-Vollzug ist konkretisiert | Änderungsskizze vom 2026-06-07 | Skizze enthält Konten, Meldung, Fälligkeit, Verzinsung, Prüfung, Zweckgliederung und Verordnungsermächtigung. | ok als Arbeitsfassung |
| Bundesmittel-Zweckzerlegung 2024-2026 bleibt nicht öffentlich beschafft | Reformkonzept und frühere Bundesmittel-Analyse | Keine neue amtliche Ist-Zweckzerlegung wurde beigebracht; das Konzept markiert dies inzwischen ausdrücklich. | offen |

## Gegenrechnung

### Rechnung 1: Erwerbsquotenbrücke 65+

- Datenquelle: `ingest/originale/2026-06-07-genesis-12211-0002-mikrozensus-erwerbsstatus.json`
- Formel: `Erwerbstätigenquote = Erwerbstätige 65+ / Bevölkerung 65+`
- Ergebnis Reformer: 10,2 %
- Ergebnis Prüfer: `1.843 / 18.045 = 0,102131`, also 10,2 %
- Abweichung: keine relevante Abweichung
- Bewertung: rechnerisch ok. Inhaltlich ist diese Quote keine feinjährige
  Erwerbsquote für 67, 68, 69, 70, 71 und 72 Jahre.

### Rechnung 2: Effektive Beitragszahler aus GENESIS-Altersjahren

- Datenquelle:
  `analysen/daten/2026-06-07-rentenalter-genesis-empirisch-altersjahre.csv`
- Formel: `Summe(nicht_in_rente_mio je Altersjahr) * 0,102131 * 0,85`
- Ergebnis Prüfer:

| Jahr | Szenario | Detailsumme nicht in Rente | Detailsumme effektiv | Summary nicht in Rente | Summary effektiv |
| ---: | --- | ---: | ---: | ---: | ---: |
| 2035 | Lebenserwartung 2:1 | 2,403 | 0,209 | 2,403 | 0,209 |
| 2035 | dänemarknah | 4,827 | 0,419 | 4,826 | 0,419 |
| 2070 | Lebenserwartung 2:1 | 8,460 | 0,735 | 8,459 | 0,734 |
| 2070 | dänemarknah | 9,423 | 0,818 | 9,422 | 0,818 |

Bewertung: Die Abweichungen von 0,001 Mio. entstehen durch Rundung in den
Detailzeilen vor der Summierung. Die ungerundete Skriptlogik ist plausibel;
kein arithmetischer Blocker.

### Rechnung 3: Rentenaltermodell als Entscheidungsrechnung

- Datenquelle:
  `analysen/2026-06-07-rentenalter-genesis-empirisch.md`
- Befund: Die Bevölkerungsseite ist jetzt amtlich und feinjährig. Die
  eigentliche Entscheidungswirkung hängt aber weiter an nicht belegten Größen:
  altersscharfe Erwerbsbeteiligung, beitragspflichtiges Entgelt,
  Rentenzugänge, Zugangsfaktoren, Erwerbsminderung, Schwerbehinderung und
  Schutzpfade für belastete Erwerbsbiografien.
- Bewertung: als Sensitivität deutlich verbessert, als finale
  Entscheidungsrechnung weiter offen.

## Normstand-Prüfung

Geprüfte Normstände:

- `gesetzbuecher/sgb/sgb-vi-paragraf-68-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-69-stand-2026-06-07.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-158-stand-2026-06-05.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-177-stand-2026-06-05.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-213-stand-2026-06-05.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-291b-stand-2026-06-05.md`
- bereits geprüfte Altersgrenzen-Normstände:
  `gesetzbuecher/sgb/sgb-vi-paragraf-34-stand-2026-06-06.md` bis
  `gesetzbuecher/sgb/sgb-vi-paragraf-38-stand-2026-06-06.md`,
  `gesetzbuecher/sgb/sgb-vi-paragraf-77-stand-2026-06-06.md`,
  `gesetzbuecher/sgb/sgb-vi-paragraf-235-stand-2026-06-06.md`,
  `gesetzbuecher/sgb/sgb-vi-paragraf-236-stand-2026-06-06.md`,
  `gesetzbuecher/sgb/sgb-vi-paragraf-236a-stand-2026-06-06.md`,
  `gesetzbuecher/sgb/sgb-vi-paragraf-237-stand-2026-06-06.md`,
  `gesetzbuecher/sgb/sgb-vi-paragraf-237a-stand-2026-06-06.md`

Befund: Kein neuer Normstand-Blocker für die am 2026-06-07 angelegten
Folgeänderungen. Die rechtliche Arbeitsfassung ist aber noch kein
vollständiger Artikelgesetzentwurf; insbesondere Verweisnormen außerhalb des
SGB VI und Haushalts-/Rechnungslegungsvorschriften sind nur als Folgearbeit
benannt.

## Rechtsprüfung

- Zuständigkeit: Für Rentenwert, Beitragssatz, Bundeszuschüsse und
  Rechnungslegung im SGB-VI-Rahmen grundsätzlich plausibel.
- Bestimmtheit: Die Folgeänderungen verbessern die Systematik deutlich. Noch
  offen bleibt, ob Referenzausgaben, Budgetfaktor, Nachholkonto, Rundung und
  Datenquellen gesetzlich ausreichend vorgezeichnet sind oder zu stark in die
  Rechtsverordnung wandern.
- Eigentum/Vertrauensschutz: Nominalschutz und Bestandsschutz-Zuschuss sind
  tragende Sicherungen. Eine lange Phase niedrigerer Anpassungen bleibt
  verfassungs- und sozialpolitisch sensibel.
- Gleichheit: Die Rentenalterkopplung braucht weiter tragfähige Ausnahmen und
  Schutzpfade für Erwerbsminderung, Schwerbehinderung, besonders lange
  Versicherungszeiten und Gruppen mit geringerer gesunder Lebenserwartung.
- Haushalt: §213a erhöht Transparenz, ersetzt aber keine amtliche
  Ist-Zweckzerlegung der Bundesmittel 2024-2026. Für die Zukunft ist die
  Zweckgliederung geregelt; für die Ausgangslage bleibt der Datenbefund offen.
- Vollzug: §213a enthält nun ein prüfbares Vollzugsmodell. Kritisch bleibt die
  Regel, dass Entgeltpunkte erst nach Zahlung gutgeschrieben werden: Bei
  Zahlungsverzug öffentlicher Träger darf der Versicherte nicht belastet
  werden. Die Skizze erkennt das und verweist auf Abschlagszahlung oder
  Ausfallhaftung; ausformuliert ist es noch nicht.

## Kritische Gegenposition

Die stärkste Gegenposition lautet: Das Konzept ist inzwischen transparenter,
aber genau dadurch wird sichtbar, dass die harte Finanzierungslogik politisch
teuer ist. Wenn Beitragssätze stabil bleiben sollen und keine zusätzlichen
Netto-Bundesmittel entstehen, müssen spätere Rentenzugänge länger arbeiten,
Rentenanpassungen relativ zum Referenzpfad niedriger ausfallen oder echte
öffentliche Beiträge haushaltswirksam bereitgestellt werden. Die GENESIS-Daten
helfen bei der Demographie, entscheiden aber nicht, wie viele 68- bis
72-Jährige tatsächlich beitragspflichtig weiterarbeiten können.

## Blocker

- Keine arithmetischen Blocker in der neuen GENESIS-Rechnung.
- Kein neuer Normstand-Blocker für § 69, § 158, § 177, § 213 und § 291b.
- Der frühere Blocker `synthetische Altersjahrkohorten` ist für die
  Bevölkerungsseite erledigt.
- Die Freigabe bleibt offen, weil die Erwerbs- und Rentenzugangsseite der
  Rentenalterkopplung nicht empirisch altersscharf belegt ist.
- Die Freigabe bleibt offen, weil die amtliche Bundesmittel-Zweckzerlegung
  2024-2026 weiterhin nicht als öffentliche Ist-Datenbasis vorliegt.

## Offene Punkte

- Amtliche feinjährige Erwerbsquoten oder Sonderauswertung für 67 bis 72 Jahre.
- DRV-Rentenzugangsdaten nach Alter, Rentenart, Zugangsfaktor, Abschlag,
  Erwerbsminderung und Schutzgruppen.
- Ausformulierte Ausfallhaftung oder gleichgestellte Abschlagszahlung bei
  Zahlungsverzug öffentlicher Träger nach §213a.
- Vollständiger Artikelgesetzentwurf mit SGB-IV-, Haushalts- und
  Rechnungslegungsfolgeänderungen.
- Kapitalmarktbaustein weiterhin nur konzeptionell; kein freigabefähiges
  Stammgesetz oder Aufsichtsmodell.

## Nachbesserungen

- Rentenaltermodell um altersscharfe Erwerbs- und Rentenzugangsdaten ergänzen
  oder den Rentenalterblock ausdrücklich nur als Sensitivität und nicht als
  Freigabegrundlage behandeln.
- §213a um konkrete Ausfallhaftung zugunsten der Versicherten ergänzen.
- Haushalts- und Rechnungslegungsfolgeänderungen außerhalb des SGB VI
  ausarbeiten.
- Bundesmittel-Zweckzerlegung 2024-2026 weiter als Negativbefund führen, bis
  eine amtliche Quelle beschafft ist; keine rückwirkende Ist-Zerlegung
  behaupten.
