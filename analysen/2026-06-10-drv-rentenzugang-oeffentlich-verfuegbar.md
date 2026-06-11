---
title: Oeffentlich verfuegbare DRV-Rentenzugangsdaten fuer das Reformmodell
date: 2026-06-10
type: analyse
status: arbeitsfassung
publish: false
source_urls:
  - https://www.deutsche-rentenversicherung.de/SharedDocs/Downloads/DE/Statistiken-und-Berichte/statistikpublikationen/statistikband_rente.pdf?__blob=publicationFile&v=5
  - https://statistik-rente.de/drv/extern/rente/rentenbestand/
  - https://www.bmas.de/SharedDocs/Downloads/DE/Rente/rentenversicherungsbericht-2025.pdf?__blob=publicationFile&v=3
ingest_refs:
  - ingest/dokumente/2026-06-04-drv-statistikband-rente-2024.md
  - ingest/links/2026-06-04-statistik-rente-rentenbestand.md
  - ingest/dokumente/2026-06-05-bmas-rentenversicherungsbericht-2025.md
data_artifacts:
  - analysen/daten/2026-06-10-drv-rentenzugang-oeffentlich-alter-rentenart.csv
  - analysen/daten/2026-06-10-drv-rentenzugang-oeffentlich-abschlaege.csv
scripts:
  - scripts/extract_drv_rentenzugang_public.py
related_projects:
  - projekte/rentenversicherung/reformkonzept.md
---

# Oeffentlich verfuegbare DRV-Rentenzugangsdaten fuer das Reformmodell

## Zweck

Diese Analyse zieht aus frei zugaenglichen DRV-Quellen das heraus, was ohne
formale Datenanfrage bereits belastbar beschaffbar ist. Sie grenzt zugleich
ab, welche Datenluecken fuer das Rentenreformmodell offen bleiben.

## Beschaffbar ohne Anfrage

- DRV-Statistikband 2024, Tabellen `40.00 Z`, `40.01 Z`, `40.02 Z`: Rentenzugang
  2024 bei Altersrenten nach Einzelalter bei Rentenbeginn fuer 67, 68, 69 sowie
  Sammelkategorie `70 und aelter`, jeweils mit Anzahl und durchschnittlichem
  Rentenzahlbetrag, getrennt nach Gesamt, Maennern und Frauen.
- Tabelle `20.00 Z`: Renten mit Abschlagsmonaten nach Rentenarten, inklusive
  durchschnittlicher Anzahl der Abschlagsmonate; allerdings ohne Aufschluesselung
  nach Einzelalter 67 bis 72.

## Kernergebnisse aus den oeffentlichen Tabellen

| Ebene | Oeffentlich verfuegbar | Aussage |
| --- | --- | --- |
| Alter 67 | Ja | Rentenzugang nach Rentenart und Geschlecht ist direkt sichtbar. |
| Alter 68 | Ja | Rentenzugang nach Rentenart und Geschlecht ist direkt sichtbar. |
| Alter 69 | Ja | Rentenzugang nach Rentenart und Geschlecht ist direkt sichtbar. |
| Alter 70 | Nein, nur in `70 und aelter` | Einzelalter 70, 71, 72 sind nicht getrennt ausgewiesen. |
| Abschlaege/Zugangsfaktor nach 67-72 | Nein | Nur aggregierte Abschlagstabellen nach Rentenart, nicht nach Einzelalter 67-72. |
| Erwerbsminderung 67-72 | Nein als altersscharfe Zugangstabelle | Im frei verfuegbaren Paket keine getrennte DRV-Zugangstabelle 67-72 fuer EM-Renten. |

## Direkt nutzbare Zahlen fuer das Reformmodell

- Insgesamt 2024 gingen bei Altersrenten `10.101` Zugaenge mit Rentenbeginn `67`,
  `4.241` mit `68`, `2.503` mit `69` und `7.305` in `70 und aelter` zu.
- Bei Maennern entfallen auf `67`: `6.011`, auf `68`: `2.514`, auf `69`: `1.439`,
  auf `70 und aelter`: `2.565` Altersrentenzugaenge.
- Bei Frauen entfallen auf `67`: `4.090`, auf `68`: `1.727`, auf `69`: `1.064`,
  auf `70 und aelter`: `4.740` Altersrentenzugaenge.
- Von allen Altersrentenzugaengen 2024 hatten `251.013` Abschlaege; die
  durchschnittliche Anzahl der Abschlagsmonate lag bei `32,15`.
- Bei Altersrenten fuer langjaehrig Versicherte hatten `211.540` von `213.530`
  Vollrenten Abschlaege; fuer schwerbehinderte Menschen `39.083` von `60.211`.

## Was weiter fehlt

- Einzelalter 70, 71 und 72 als getrennte Rentenzugangstabellen.
- Kreuztabellen `Alter x Rentenart x Zugangsfaktor/Abschlag` fuer 67 bis 72.
- Altersscharfe DRV-Daten zu Erwerbsminderungsrenten im Korridor 67 bis 72.
- Amtliche Bundesmittel-Ist-Zweckzerlegung 2024 bis 2026.

## Einordnung

Die offene Luecke ist damit kleiner als zuvor: Fuer 67 bis 69 liegen oeffentlich
echte DRV-Rentenzugangsangaben fuer Altersrenten vor. Die harte Restluecke
bleibt aber genau dort, wo das Reformmodell fein werden soll: Einzelalter 70, 71
und 72 sowie altersscharfe Abschlags- und Zugangsfaktordaten sind in den frei
zugaenglichen Publikationen nicht getrennt ausgewiesen.
