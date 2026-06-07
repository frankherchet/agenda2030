# Ingest: DRV Statistikband Rente 2024

## Metadaten

- Typ: Dokument
- Datum: 2026-06-04
- Quelle: https://www.deutsche-rentenversicherung.de/SharedDocs/Downloads/DE/Statistiken-und-Berichte/statistikpublikationen/statistikband_rente.pdf?__blob=publicationFile&v=5
- Status: zusammengefasst
- Index: `ingest/index/README.md`

## Kurzfassung

Offizieller Statistikband der Deutschen Rentenversicherung zum Rentenbestand
2024. Die Quelle enthält Tabellen nach Rentenart, Alter, Geschlecht und
Versicherungsträger. Sie wurde für das Abschmelzmodell der
Bestandsschutz-Zuschüsse verwendet.

## Kernaussagen

- Rentenbestand am 31.12.2024 als amtliche DRV-Datenbasis.
- Enthält Altersrenten, Erwerbsminderungsrenten und Hinterbliebenenrenten.
- Knappschaft-Bahn-See ist als Träger aggregiert auswertbar.

## Enthaltene Informationen

- DRV-Statistikband Rente 2024 mit Tabellen zum Rentenbestand nach Rentenart,
  Alter, Geschlecht und Versicherungsträger.
- Tabellenteil Rentenzugang mit Verteilungen nach Rentenarten sowie nach
  Alter des Rentenberechtigten bei Rentenbeginn, Rentenzahlbeträgen nach
  Rentenart und Altersgruppen sowie Angaben zum durchschnittlichen Alter bei
  Rentenbeginn.
- Für das Abschmelzmodell besonders genutzt: Tabellen zu
  Erwerbsminderungsrenten, Altersrenten, Hinterbliebenenrenten und
  Trägeraggregaten.

## Jetzt extrahierte relevante Informationen

- Der Rentenbestand zum 31.12.2024 wurde als Strukturinput für
  `analysen/daten/2026-06-04-drv-rentenbestand-struktur.csv` genutzt.
- Die Analyse `analysen/2026-06-04-drv-rentenbestand-inputs.md` verdichtet
  die extrahierten Rentenarten-, Alters- und Geschlechtsstrukturen.
- Für eine Freigabe der Rentenalter-Kopplung sind zusätzlich die
  Rentenzugangstabellen nach Alter/Rentenart sowie Daten zu Zugangsfaktoren,
  Abschlägen, Erwerbsminderung, Schwerbehinderung und besonders langen
  Versicherungszeiten auszuwerten. Der GENESIS-Erwerbsblock ersetzt diese
  DRV-Rentenzugangsdaten nicht.

## Relevanz für agenda2030

Zentrale Quelle für belastbare Rentenbestandsstruktur.

## Zuordnung

- Ministerien: `ministerien/arbeit-soziales/`
- Gesetze/Gesetzbücher: `gesetzbuecher/sgb/`
- Bundestagsdrucksachen: keine
- Themen: DRV, Rentenbestand, Altersstruktur, Knappschaft

## Offene Fragen

- Separate Alters- und Geschlechtsstruktur der Knappschaft-Bahn-See bei Bedarf beschaffen.

## Nächste Schritte

- In Rentenmodellen über `analysen/daten/2026-06-04-drv-rentenbestand-struktur.csv` nutzen.
