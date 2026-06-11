---
title: Prüfung Rentenreform als öffentliche Konzeptfassung
date: 2026-06-11
type: pruefbericht
status: freigegeben
reviewed_report: projekte/rentenversicherung/reformkonzept.md
reviewer: pruefer
publish: false
source_urls:
  - https://www.deutsche-rentenversicherung.de/SharedDocs/Downloads/DE/Statistiken-und-Berichte/statistikpublikationen/statistikband_rente.pdf?__blob=publicationFile&v=5
  - https://statistik-rente.de/drv/extern/rente/rentenbestand/
  - https://www.bmas.de/SharedDocs/Downloads/DE/Rente/rentenversicherungsbericht-2025.pdf?__blob=publicationFile&v=3
  - https://dserver.bundestag.de/btd/21/014/2101419.pdf
  - https://rentenupdate.drv-bund.de/SharedDocs/Dokumente/2025/10_Bundeszuschuesse_nbL/rentenupdate_10_Bundeszuschuesse_nbL_lang.pdf?__blob=publicationFile&v=4
  - https://www.gesetze-im-internet.de/sgb_6/
  - https://www.gesetze-im-internet.de/bho/
ingest_refs:
  - ingest/dokumente/2026-06-04-drv-statistikband-rente-2024.md
  - ingest/links/2026-06-04-statistik-rente-rentenbestand.md
  - ingest/dokumente/2026-06-05-bmas-rentenversicherungsbericht-2025.md
  - ingest/dokumente/2026-06-05-bundestag-drs-21-1419-nicht-beitragsgedeckte-leistungen.md
  - ingest/dokumente/2026-06-05-drv-rentenupdate-bundeszuschuesse-nicht-beitragsgedeckte-leistungen-2025.md
  - ingest/links/2026-06-04-gesetze-im-internet-sgb-vi.md
  - ingest/links/2026-06-07-gesetze-im-internet-bho.md
---

# Prüfung: Rentenreform als öffentliche Konzeptfassung

## Prüfurteil

- Status: freigegeben
- Kurzbegründung: Die Rentenreform ist als öffentliche Konzeptfassung
  prüffähig und freigegeben. Die Kernrechnungen sind reproduzierbar, die
  Quellenkette ist lokal nachvollziehbar und die bisherigen Freigabeblocker
  werden nach dem neuen Maßstab korrekt als Restlücken, Proxys oder
  Sensitivitäten geführt. Die Freigabe gilt nicht als finale Gesetzes- oder
  Haushaltsvollzugsfreigabe.

## Geprüfter Gegenstand

- Report: `projekte/rentenversicherung/reformkonzept.md`
- Version/Commit: `5551f3e`
- Prüfdatum: 2026-06-11
- Zusätzlich geprüft:
  `analysen/2026-06-10-drv-rentenzugang-oeffentlich-verfuegbar.md`,
  `projekte/rentenversicherung/2026-06-09-status-offene-pruefpunkte.md`,
  `.agents/skills/pruefer/SKILL.md`

## Quellenprüfung

| Behauptung/Zahl | Quelle im Report | Unabhängige Prüfung | Ergebnis |
| --- | --- | --- | --- |
| Konzept darf ohne manuelle Datenabfrage mit öffentlichen Proxys arbeiten | Reformkonzept und Prüfer-Skill | Neuer Prüfermaßstab erlaubt Restlücken, solange sie nicht als amtlich vollständig behauptet werden. | ok |
| DRV-Rentenzugang 67, 68, 69 und `70 und älter` öffentlich nutzbar | DRV-Statistikband und `analysen/2026-06-10-drv-rentenzugang-oeffentlich-verfuegbar.md` | CSV enthält die aus Tabellen `40.00 Z`, `40.01 Z`, `40.02 Z` extrahierten Werte; die Lücke 70/71/72 wird offen markiert. | ok |
| Abschläge sind nur aggregiert nach Rentenart verfügbar | DRV-Statistikband Tabelle `20.00 Z` | CSV weist Abschlagsmonate nach Rentenart aus, aber keine Einzelalter-Kreuztabelle. | ok |
| Bundesmittel-Ist-Zweckzerlegung 2024-2026 ist öffentlich nicht vollständig verfügbar | BT-Drs. 21/1419, Rentenupdate, BMAS-Bericht | Konzept behauptet keine amtliche Zweckvollständigkeit, sondern nutzt Reformklassifikation und Negativbefund. | ok |
| Rentenalterrechnung nutzt GENESIS-Altersjahrgänge und öffentliche Erwerbsbrücke | GENESIS-Artefakte und `calc_rentenalter_genesis_empirisch.py` | Reproduzierbare CSVs weisen Altersjahrgänge und 65-bis-unter-75-Brückenquote aus. | ok |

## Gegenrechnung

### Rechnung 1: DRV-Rentenzugang 67 bis `70 und älter`

- Datenquelle: `analysen/daten/2026-06-10-drv-rentenzugang-oeffentlich-alter-rentenart.csv`
- Befund Prüfer: Die Gesamtwerte lauten 67: `10.101`, 68: `4.241`,
  69: `2.503`, `70 und älter`: `7.305` Altersrentenzugänge.
- Bewertung: Die Zahlen sind als öffentliche DRV-Basis verwendbar. Die
  fehlende Auflösung von 70, 71 und 72 bleibt ein Restpunkt, aber kein
  Konzeptblocker.

### Rechnung 2: Abschläge nach Rentenart

- Datenquelle: `analysen/daten/2026-06-10-drv-rentenzugang-oeffentlich-abschlaege.csv`
- Befund Prüfer: Bei Altersrenten insgesamt sind `251.013` Zugänge mit
  Abschlägen ausgewiesen; der Durchschnitt liegt bei `32,15`
  Abschlagsmonaten. Bei Altersrenten für langjährig Versicherte sind
  `211.540` von `213.530` Zugängen abschlagsbehaftet.
- Bewertung: Die aggregierte Abschlagsbasis ist plausibel und für eine
  Konzeptfassung ausreichend. Für eine finale Vollzugsmodellierung bleibt die
  Kreuztabelle `Alter x Rentenart x Zugangsfaktor` offen.

### Rechnung 3: Rentenalter-Sensitivität

- Datenquelle: `analysen/daten/2026-06-07-rentenalter-genesis-empirisch-summary.csv`
- Befund Prüfer: Im moderaten Pfad ergeben sich 2039 beim
  Lebenserwartungsmodell `1,365` Mio. nicht in den Rentenbestand wechselnde
  Personen und `0,192` Mio. effektive zusätzliche Beitragszahler; beim
  daenemarknahen Pfad `2,829` Mio. und `0,397` Mio.
- Bewertung: Die Rechnung ist als Sensitivität nachvollziehbar. Sie wird im
  Konzept nicht als harte Erwerbsprognose ausgegeben.

## Rechtsprüfung

- Zuständigkeit: Bundesgesetzliche Regelung der gesetzlichen Rentenversicherung
  und haushaltsrechtlicher Ausweis sind plausibel beim Bund verortet.
- Grundrechte/Verfassung: Bestandsschutz für bereits erworbene Anwartschaften
  und laufende Renten ist als tragendes Prinzip enthalten.
- Übergangsrecht: Übergangslogik ist konzeptionell angelegt; die finale
  Kohorten- und Vertrauensschutzstaffel bleibt für Gesetzgebung auszuarbeiten.
- Vollzug: §-213a-Mechanik, BHO-Ausweis und Rückgriff sind als Arbeitsfassungen
  ausreichend konkret für die Konzeptfreigabe, aber noch nicht
  vollzugsabschließend.

## Kritische Gegenposition

Die stärkste Gegenposition lautet: Ein Rentenreformkonzept ohne vollständige
amtliche Zweckzerlegung der Bundesmittel und ohne altersscharfe DRV-Daten für
70, 71 und 72 könne keine belastbare Reformwirkung behaupten. Diese Kritik
trägt für eine finale Vollzugs- oder Gesetzesfolgenabschätzung. Sie trägt
nicht mehr als Blocker für die Konzeptfassung, weil das Konzept die fehlenden
Detaildaten offenlegt und seine Kernlogik auf öffentlichen Quellen,
Rechenartefakten und Sensitivitäten aufbaut.

## Blocker

- Keine Blocker für die öffentliche Konzeptfassung.

## Offene Punkte

- Keine entscheidungskritischen Restpunkte für die Konzeptfassung.
- Für die spätere Endvalidierung bleiben offen: Einzelalter 70, 71 und 72,
  altersscharfe Abschläge/Zugangsfaktoren, EM-Zugänge 67 bis 72 und amtliche
  Bundesmittel-Ist-Zweckzerlegung 2024 bis 2026.

## Nachbesserungen

- Reformkonzept-Metadaten um diesen Prüfbericht und die öffentliche
  DRV-Auswertung ergänzen.
- Projekt-README, globalen Index und Log auf den neuen Freigabestand
  aktualisieren.
