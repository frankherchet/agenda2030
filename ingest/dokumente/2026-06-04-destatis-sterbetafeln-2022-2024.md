# Destatis-Sterbetafel 2022/2024

## Metadaten

- Datum der Ablage: 2026-06-04
- Hauptquelle: Statistisches Bundesamt (Destatis)
- Dokument: Statistischer Bericht - Sterbetafeln - 2022/2024
- Originaldatei: `ingest/originale/2026-06-04-destatis-sterbetafeln-2022-2024.xlsx`
- Status: zitierfähige Inputquelle
- Relevanz: Rentenversicherung, Pflegeversicherung, Krankenversicherung,
  Versicherungsbarwerte und Bestandsschutzmodelle
- Ingest-Referenzen:
  - `ingest/links/2026-06-04-destatis-periodensterbetafeln-publikationen.md`
  - `ingest/links/2026-06-04-destatis-sterbefaelle-lebenserwartung-thema.md`
  - `ingest/links/2026-06-04-destatis-entwicklung-lebenserwartung.md`

## Quellen

- Publikationsseite:
  https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Sterbefaelle-Lebenserwartung/Publikationen/_publikationen-innen-periodensterbetafel.html
- Themenseite Sterbefälle und Lebenserwartung:
  https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Sterbefaelle-Lebenserwartung/_inhalt.html
- Entwicklung der Lebenserwartung:
  https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Sterbefaelle-Lebenserwartung/sterbetafel.html

## Kurzfassung

Destatis stellt für Deutschland die Periodensterbetafel 2022/2024 als
Statistischen Bericht bereit. Sie enthält nach Altersjahren und Geschlecht
Sterbe- und Überlebenswahrscheinlichkeiten, Überlebende, Gestorbene und
fernere Lebenserwartung. Nach Destatis liegt die Lebenserwartung bei Geburt in
der aktuellen Sterbetafel bei 78,5 Jahren für Männer und 83,2 Jahren für
Frauen. Periodensterbetafeln bilden die Sterblichkeitsverhältnisse des
Berichtszeitraums ab und enthalten keine Annahme über künftige
Sterblichkeitsverbesserungen.

## Enthaltene Informationen

- Statistischer Bericht zu Periodensterbetafeln 2022/2024 mit Tabellen nach
  Alter und Geschlecht.
- Enthält Sterbewahrscheinlichkeiten, Überlebenswahrscheinlichkeiten,
  Überlebende und fernere Lebenserwartung.

## Jetzt extrahierte relevante Informationen

- Für das Abschmelzmodell genutzt wurden die Tabellen `12613-b01` und
  `12613-b02` mit `lx`- und `px`-Werten.
- Die Quelle dient zur Fortschreibung der erwarteten Überlebendenzahl der
  geschützten Rentenbestandskohorte.

## Relevanz für Rentenversicherung

- Der Bestandsschutz-Zuschuss kann proportional zur erwarteten Überlebendenzahl
  einer geschützten Bestandsrentner-Kohorte abgeschmolzen werden.
- Für v1 werden die `lx`-Werte der Tabellen `12613-b01` und `12613-b02`
  genutzt.
- Die tatsächliche DRV-Alters- und Geschlechtsstruktur der Rentenbezieher ist
  in `analysen/daten/2026-06-04-drv-rentenbestand-struktur.csv`
  ergänzt.

## Offene Punkte

- Das Arbeitsmodell nutzt die aktuelle Periodensterbetafel; eine
  Kohortensterbetafel oder Sterblichkeitsverbesserung kann später als
  Sensitivität ergänzt werden.
