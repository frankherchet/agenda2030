---
title: Prüfbericht Rentenversicherung zu den Folgearbeiten vom 2026-06-09
date: 2026-06-09
type: pruefbericht
status: offen
reviewed_report: projekte/rentenversicherung/reformkonzept.md
reviewer: pruefer
publish: false
source_urls:
  - https://www.deutsche-rentenversicherung.de/SharedDocs/Downloads/DE/Statistiken-und-Berichte/statistikpublikationen/statistikband_rente.pdf?__blob=publicationFile&v=5
  - https://statistik-rente.de/drv/extern/rente/rentenbestand/
  - https://rentenupdate.drv-bund.de/SharedDocs/Dokumente/2025/10_Bundeszuschuesse_nbL/rentenupdate_10_Bundeszuschuesse_nbL_lang.pdf?__blob=publicationFile&v=4
  - https://www.bmas.de/SharedDocs/Downloads/DE/Rente/rentenversicherungsbericht-2025.pdf?__blob=publicationFile&v=3
  - https://www.gesetze-im-internet.de/sgb_6/__213.html
ingest_refs:
  - ingest/dokumente/2026-06-04-drv-statistikband-rente-2024.md
  - ingest/links/2026-06-04-statistik-rente-rentenbestand.md
  - ingest/dokumente/2026-06-05-drv-rentenupdate-bundeszuschuesse-nicht-beitragsgedeckte-leistungen-2025.md
  - ingest/dokumente/2026-06-05-bmas-rentenversicherungsbericht-2025.md
  - ingest/links/2026-06-04-gesetze-im-internet-sgb-vi.md
---

# Prüfbericht: Folgearbeiten vom 2026-06-09

## Prüfurteil

- Status: offen
- Kurzbegründung: Die Folgearbeiten vom 2026-06-09 verbessern den
  Arbeitsstand, beseitigen aber keine externen Freigabehindernisse. Die
  Anfrage-Dateien sind brauchbare Entwürfe, nicht dokumentierte Versände. Der
  Korridor 67 bis 72 ist als heuristische Arbeitsfassung verwendbar, aber
  nicht als freigabefähige Enddatengrundlage.

## Geprüfter Gegenstand

- Report: `projekte/rentenversicherung/reformkonzept.md`
- Prüfdatum: 2026-06-09
- Geprüfte Folgearbeiten:
  - `gesetzbuecher/sgb/sgb-vi-artikelgesetz-213a-stand-2026-06-09.md`
  - `gesetzbuecher/sgb/sgb-vi-rechtsverordnung-213a-rueckgriff-stand-2026-06-09.md`
  - `projekte/rentenversicherung/2026-06-09-szenariokorridor-67-72.md`
  - `projekte/rentenversicherung/2026-06-09-bundesmittel-zweckzerlegung.md`
  - `projekte/rentenversicherung/2026-06-09-datenanfrage-drv.md`
  - `projekte/rentenversicherung/2026-06-09-datenanfrage-bundesmittel-zweckzerlegung.md`
  - `projekte/rentenversicherung/2026-06-09-gesamtstatus-reformvorhaben.md`
  - `projekte/rentenversicherung/2026-06-09-status-offene-pruefpunkte.md`

## Quellenprüfung

| Behauptung/Zahl | Quelle im Paket | Unabhängige Prüfung | Ergebnis |
| --- | --- | --- | --- |
| Fehlende Bundesmittel-Ist-Zweckzerlegung 2024-2026 bleibt ein Negativbefund | `2026-06-09-bundesmittel-zweckzerlegung.md` | Passt zur bisherigen Analyse `analysen/2026-06-05-bundesmittel-zweckzerlegung-rente.md`; keine amtliche Zweckzerlegung im Repo beschafft. | ok |
| Anfrage an die DRV ist vorbereitet | `2026-06-09-datenanfrage-drv.md` | Datei enthält sinnvolle Anforderungsstruktur, aber keinen Versandnachweis. | ok als Entwurf |
| Szenariokorridor 67-72 ist nur Arbeitsfassung | `2026-06-09-szenariokorridor-67-72.md` | Die zugrunde liegende CSV ist heuristisch und keine amtliche Rentenzugangsstatistik. | ok |
| Rückgriffsmechanismus unter § 213a ist weiter konkretisiert | Artikelgesetz und Rechtsverordnung | Beide Entwürfe konkretisieren Rückgriff und Haushaltsausweis, ersetzen aber keine abschließende Freigabe. | ok als Arbeitsfassung |

## Gegenrechnung

### Rechnung 1: Arbeitsdatei fuer Rentenzugaenge 67-72

- Datenquelle: `analysen/daten/drv_rentenzugang_67-72_final.csv`
- Befund: Die CSV enthält Rentenzugangsarten, Anteile, Durchschnittsabschläge
  und Durchschnittsrenten für 67 bis 72 Jahre.
- Bewertung: Das ist als heuristische Brücke brauchbar. Die Datei bildet aber
  keine amtlichen Erwerbsquoten und keine verifizierten DRV-Zugangsdaten ab.

### Rechnung 2: Bundesmittel-Negativbefund

- Datenquelle: `analysen/2026-06-05-bundesmittel-zweckzerlegung-rente.md`
- Befund: Der Negativbefund 2026-06-09 ist konsistent mit dem früheren
  Prüferstand; keine rückwirkende Ist-Zweckzerlegung aus der Reformlogik
  behauptet.
- Bewertung: korrekt.

## Rechtsprüfung

- Zuständigkeit: Die neuen §-213a-Entwürfe bewegen sich weiterhin im
  plausiblen Bundesrechtsrahmen.
- Vollzug: Rückgriff und Haushaltsausweis sind konkreter als zuvor, aber
  weiter Arbeitsfassungen.
- Datenvollzug: Anfrageentwürfe sind kein Ersatz für beschaffte Daten oder
  dokumentierten Versand.

## Blocker

- Keine neuen arithmetischen Blocker aus dem 2026-06-09-Paket.
- Keine neuen Normstand-Blocker in den geprueften Folgearbeiten.
- Freigabe bleibt offen, weil altersscharfe DRV-Rentenzugangsdaten 67 bis 72
  weiter fehlen.
- Freigabe bleibt offen, weil die amtliche Bundesmittel-Ist-Zweckzerlegung
  2024 bis 2026 weiter fehlt.
- Freigabe bleibt offen, weil die Anfrage-Dateien als Entwürfe vorliegen und
  ihr Versand nicht dokumentiert ist.

## Nachbesserungen

- Anfrageentwuerfe mit echten Ansprechpartnern ergänzen und Versand
  repo-seitig dokumentieren.
- Heuristische CSV fuer 67 bis 72 Jahre nach Eingang echter DRV-Daten
  ersetzen oder gegen diese validieren.
- Negativbefund zur Bundesmittel-Zweckzerlegung erst bei amtlicher Antwort
  aktualisieren, nicht durch Eigenableitung.
