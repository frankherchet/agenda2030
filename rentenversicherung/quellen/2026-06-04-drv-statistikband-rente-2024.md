---
title: DRV Statistikband Rente 2024
date: 2026-06-04
type: quelle
source_type: pdf
publisher: Deutsche Rentenversicherung Bund
source_url: https://www.deutsche-rentenversicherung.de/SharedDocs/Downloads/DE/Statistiken-und-Berichte/statistikpublikationen/statistikband_rente.pdf?__blob=publicationFile&v=5
local_original: rentenversicherung/originale/2026-06-04-drv-statistikband-rente-2024.pdf
used_for:
  - rentenversicherung/daten/2026-06-04-drv-rentenbestand-struktur.csv
  - rentenversicherung/auswertungen/2026-06-04-drv-rentenbestand-inputs.md
---

# DRV Statistikband Rente 2024

Amtliche DRV-Quelle für den Rentenbestand am 31.12.2024.

## Genutzte Tabellen

- Tabelle `1.00 G`: Rentenbestand nach Versicherungsträger, inklusive
  `DRV Knappschaft-Bahn-See`.
- Tabellen `30.00 G`, `30.01 G`, `30.02 G`: Renten wegen verminderter
  Erwerbsfähigkeit nach Alter und Geschlecht.
- Tabellen `40.00 G`, `40.01 G`, `40.02 G`: Altersrenten nach Einzelalter und
  Geschlecht.
- Tabelle `50.00 G`: Renten wegen Todes nach Alter und Rentenart.

## Extrahierte Struktur

Die Werte werden in
`rentenversicherung/daten/2026-06-04-drv-rentenbestand-struktur.csv`
normalisiert. Offene Altersgruppen (`100 und älter`, `105 und älter`) bleiben
als offene Gruppen gekennzeichnet, damit das Rechenmodell sie mit einer
expliziten Tail-Regel behandelt.
