---
title: Rentenreform Freigabeblocker - Nachbesserung
date: 2026-06-06
type: analyse
status: arbeitsfassung
publish: false
source_urls:
  - https://www.gesetze-im-internet.de/sgb_6/
  - https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Geburten/Tabellen/lebendgeborene-geschlecht.html
  - https://www.deutsche-rentenversicherung.de/DRV/DE/Ueber-uns-und-Presse/Presse/Meldungen/2025/251111-kindererziehungszeiten-vaeter
  - https://www.bundesgesundheitsministerium.de/themen/pflege/online-ratgeber-pflege/leistungen-der-pflegeversicherung/leistungen-im-ueberblick/soziale-absicherung-fuer-pflegepersonen
  - https://www.deutsche-rentenversicherung.de/DRV/DE/Ueber-uns-und-Presse/Presse/Pressemitteilungen/Pressemitteilungen-archiv/2025/2025-05-09-pflege-von-angehoerigen.html
  - https://dserver.bundestag.de/btd/21/014/2101419.pdf
ingest_refs:
  - ingest/links/2026-06-04-gesetze-im-internet-sgb-vi.md
  - ingest/links/2026-06-06-destatis-lebendgeborene-2024.md
  - ingest/links/2026-06-06-drv-kindererziehungszeiten-bund.md
  - ingest/links/2026-06-06-bmg-soziale-absicherung-pflegepersonen.md
  - ingest/links/2026-06-06-drv-pflegepersonen-rentenversicherung.md
  - ingest/dokumente/2026-06-05-bundestag-drs-21-1419-nicht-beitragsgedeckte-leistungen.md
data_artifacts:
  - analysen/daten/2026-06-06-rentenreform-freigabeblocker.csv
  - analysen/daten/2026-06-06-rentenalter-feinmodell-altersjahre.csv
  - analysen/daten/2026-06-06-staatsbeitraege-rentenreform.csv
  - analysen/daten/2026-06-06-staatsbeitraege-doppelfrei-bruecke.csv
  - analysen/daten/2026-06-06-rentenreform-freigabeblocker-annahmen.csv
scripts:
  - scripts/calc_rentenreform_freigabeblocker.py
related_projects:
  - projekte/rentenversicherung/reformkonzept.md
---

# Rentenreform Freigabeblocker - Nachbesserung

## Kurzfassung

Diese Nachbesserung bearbeitet die im Prüferbericht vom 2026-06-06
weiter offenen Freigabepunkte. Sie ergänzt eine SGB-VI-Mechanik zur
Rentenwert-Budgetregel, trennt Brutto-Ausweis und Netto-Haushaltswirkung
der öffentlichen Beiträge und macht die Grenzen der verfügbaren
Bundesmittel-Zweckzerlegung explizit. Sie ist noch keine Prüferfreigabe.

## Rentenwertformel

Die Reformformel wird nun als Gesetzesänderungsskizze an § 68 SGB VI
angebunden: `gesetzbuecher/sgb/sgb-vi-paragraf-68-rentenwert-budgetregel-aenderung-2026-06-06.md`.
Die technische Formel lautet:

```text
Budget_t = Beitragsbasis_t x Beitragssatzkorridor_t
         + Bestandsschutz-Zuschuss_t
         + sonstige Einnahmen_t

Rentenwert-Budgetfaktor_t = min(1, Budget_t / Referenzausgaben_t)

Aktueller Rentenwert_t = Referenz-Rentenwert_t x Rentenwert-Budgetfaktor_t
```

Ein Faktor unter 1 bedeutet eine Dämpfung gegenüber dem fortgeschriebenen
Referenzpfad. Die Gesetzesskizze enthält nun Nominalschutz für laufende
Monatsrenten, ein Nachholbetragskonto und eine Verordnungsermächtigung für
Datengrundlagen, Rundung und Referenzausgaben.

## Feineres Rentenaltermodell

Statt 0,95 Mio. Personen je zusätzlichem Rentenalterjahr vollständig von
der Renten- auf die Beitragsseite zu verschieben, bildet das Modell die
Altersjahre 67 bis 72 einzeln ab. Für jedes Altersjahr wird eine
synthetische Kohorte gebildet, mit altersspezifischer Erwerbsquote und
einem Senior-Wage-Faktor von 85 % bewertet.

| Jahr | Szenario | Korridor | Rentenwert-Budgetfaktor | Budgetsaldo vs. Referenz |
| ---: | --- | --- | ---: | ---: |
| 2035 | status_quo_67 | 22 % | 89,4 % | -64,9 Mrd. Euro |
| 2035 | lebenserwartung_gekoppelt_2zu1 | 22 % | 95,0 % | -28,6 Mrd. Euro |
| 2035 | daenemarknah | 22 % | 100,0 % | 7,1 Mrd. Euro |
| 2039 | status_quo_67 | 22 % | 80,1 % | -142,0 Mrd. Euro |
| 2039 | lebenserwartung_gekoppelt_2zu1 | 22 % | 87,3 % | -83,1 Mrd. Euro |
| 2039 | daenemarknah | 22 % | 95,8 % | -25,2 Mrd. Euro |
| 2050 | status_quo_67 | 22 % | 74,5 % | -232,9 Mrd. Euro |
| 2050 | lebenserwartung_gekoppelt_2zu1 | 22 % | 87,5 % | -98,5 Mrd. Euro |
| 2050 | daenemarknah | 22 % | 94,9 % | -37,1 Mrd. Euro |
| 2070 | status_quo_67 | 22 % | 71,5 % | -411,2 Mrd. Euro |
| 2070 | lebenserwartung_gekoppelt_2zu1 | 22 % | 97,0 % | -32,6 Mrd. Euro |
| 2070 | daenemarknah | 22 % | 100,0 % | 8,6 Mrd. Euro |

Interpretation: Die Lebenserwartungs-Kopplung entlastet weiterhin stark,
aber weniger optimistisch als die erste Screeningrechnung, weil ältere
zusätzliche Erwerbsjahre nur teilweise als Beitragsjahre wirken.

## Echte öffentliche Beitragszahlungen

Die folgende Tabelle ist keine zusätzliche Einnahmeannahme für die
Rentenversicherung, sondern eine Transparenzrechnung: rentenwirksame
Sozialzeiten müssen als echte Zahlung des zuständigen Trägers sichtbar
werden und dürfen nicht als kostenloser Entgeltpunkt erscheinen.

| Jahr | Auszuweisende öffentliche Beiträge |
| ---: | ---: |
| 2035 | 40,7 Mrd. Euro |
| 2039 | 44,9 Mrd. Euro |
| 2050 | 59,0 Mrd. Euro |
| 2070 | 96,6 Mrd. Euro |

Enthalten sind modellhaft Kindererziehungszeiten, Pflegezeiten,
BA-Leistungsempfänger und Erstattungen von Versorgungsdienststellen.
Die Beträge wachsen nominal mit 2,5 % pro Jahr.

### Doppelfreie Haushaltsbrücke

Die Prüferkritik betraf zu Recht die Gefahr, bestehende Zahlungsströme als
neue Reformmittel zu zählen. Die neue Brückenrechnung trennt deshalb
Brutto-Ausweis, bereits in der DRV-Finanzierung enthaltene Zahlungen und
modellierten Netto-Zusatzeffekt. Für die vier aktuell modellierten
Kategorien ist der Netto-Zusatzeffekt null, solange keine zusätzliche
Leistung oder höhere Bemessungsgrundlage beschlossen wird.

| Jahr | Brutto-Ausweis | bereits in DRV-Finanzierung | Netto-Zusatzeffekt |
| ---: | ---: | ---: | ---: |
| 2035 | 40,7 Mrd. Euro | 40,7 Mrd. Euro | 0,0 Mrd. Euro |
| 2039 | 44,9 Mrd. Euro | 44,9 Mrd. Euro | 0,0 Mrd. Euro |
| 2050 | 59,0 Mrd. Euro | 59,0 Mrd. Euro | 0,0 Mrd. Euro |
| 2070 | 96,6 Mrd. Euro | 96,6 Mrd. Euro | 0,0 Mrd. Euro |

Damit ist die Tabelle kein Einnahmehebel, sondern eine Buchungs- und
Transparenzvorschrift. Zusätzliche Haushaltslasten entstehen erst, wenn
weitere Sozialzeiten einbezogen oder heutige Bemessungsgrundlagen erhöht
werden.

## Bundesmittel-Zweckzerlegung

Der bisherige Freigabeblocker kann nicht durch eine nicht vorhandene
öffentliche Quelle erledigt werden. Die Negativbeschaffung bleibt:
Nach den ingested Quellen liegt für 2024 bis 2026 keine vollständige
öffentliche amtliche Zweckzerlegung vor. Die Reform löst deshalb nicht
rückwirkend die Datenlage, sondern normiert künftig eine zwingende
Dreiteilung zwischen Bestandsschutz-Zuschuss, echten Staatsbeiträgen und
sonstigen Steuertransfers. Diese Dreiteilung ist in der
§-68/§-213a-Gesetzesskizze angelegt.

## Prüffähige Folgepunkte

- Normstände für Altersgrenzen und Zugangsfaktor wurden separat angelegt.
- Rentenwertformel ist als SGB-VI-Gesetzesänderungsskizze ausgearbeitet.
- Rentenaltermodell ist feiner, aber weiter als Sensitivität zu behandeln,
  bis echte feinjährige Bevölkerung, Erwerbsquoten und Rentenzugangsdaten
  in das Modell übernommen sind.
- Staatsbeiträge sind doppelfrei als Brutto-Ausweis, bestehende Zahlung und
  Netto-Zusatzeffekt getrennt.