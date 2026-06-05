---
title: Nachprüfung Reformkonzept Rentenversicherung
date: 2026-06-06
type: pruefbericht
status: offen
reviewed_report: projekte/rentenversicherung/reformkonzept.md
reviewer: pruefer
source_urls:
  - https://www.gesetze-im-internet.de/sgb_6/
  - https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Geburten/Tabellen/lebendgeborene-geschlecht.html
  - https://www.deutsche-rentenversicherung.de/DRV/DE/Ueber-uns-und-Presse/Presse/Meldungen/2025/251111-kindererziehungszeiten-vaeter
  - https://www.bundesgesundheitsministerium.de/themen/pflege/online-ratgeber-pflege/leistungen-der-pflegeversicherung/leistungen-im-ueberblick/soziale-absicherung-fuer-pflegepersonen
  - https://www.deutsche-rentenversicherung.de/DRV/DE/Ueber-uns-und-Presse/Presse/Pressemitteilungen/Pressemitteilungen-archiv/2025/2025-05-09-pflege-von-angehoerigen.html
  - https://www.deutsche-rentenversicherung.de/DRV/DE/Experten/Zahlen-und-Fakten/Kennzahlen-zur-Finanzentwicklung/kennzahlen-zur-finanzentwicklung_node.html?https=1
  - https://dserver.bundestag.de/btd/21/014/2101419.pdf
ingest_refs:
  - ingest/links/2026-06-04-gesetze-im-internet-sgb-vi.md
  - ingest/links/2026-06-06-destatis-lebendgeborene-2024.md
  - ingest/links/2026-06-06-drv-kindererziehungszeiten-bund.md
  - ingest/links/2026-06-06-bmg-soziale-absicherung-pflegepersonen.md
  - ingest/links/2026-06-06-drv-pflegepersonen-rentenversicherung.md
  - ingest/links/2026-06-04-drv-finanzkennzahlen-rentenversicherung.md
  - ingest/dokumente/2026-06-05-bundestag-drs-21-1419-nicht-beitragsgedeckte-leistungen.md
---

# Nachprüfung: Reformkonzept Rentenversicherung

## Prüfurteil

- Status: offen
- Kurzbegründung: Die am 2026-06-06 nachgereichten Arbeiten schließen die
  vorherigen Freigabeblocker fachlich an, machen das Reformkonzept aber noch
  nicht freigabefähig. Rechenweg und CSV-Artefakte sind reproduzierbar; die
  Gegenrechnung findet keinen offensichtlichen arithmetischen Fehler. Offen
  bleiben die gesetzestextfähige Rentenwertmechanik, eine empirisch belastbare
  feinjährige Kohortenrechnung, die doppelfreie Haushaltswirkung echter
  Staatsbeiträge und eine amtliche Zweckzerlegung der Bundesmittel ab 2024.

## Geprüfter Gegenstand

- Report: `projekte/rentenversicherung/reformkonzept.md`
- Geprüfter Stand: Commit `1840dbd`
- Prüfdatum: 2026-06-06
- Nachbesserungsanalyse:
  `analysen/2026-06-06-rentenreform-freigabeblocker.md`
- Rechenartefakte:
  - `scripts/calc_rentenreform_freigabeblocker.py`
  - `analysen/daten/2026-06-06-rentenreform-freigabeblocker.csv`
  - `analysen/daten/2026-06-06-rentenalter-feinmodell-altersjahre.csv`
  - `analysen/daten/2026-06-06-staatsbeitraege-rentenreform.csv`
  - `analysen/daten/2026-06-06-rentenreform-freigabeblocker-annahmen.csv`

## Quellenprüfung

| Behauptung/Zahl | Quelle im Report | Unabhängige Prüfung | Ergebnis |
| --- | --- | --- | --- |
| SGB-VI-Normstände für Altersgrenzen und Abschläge sind ergänzt | `gesetze-im-internet.de` und lokale Normstand-Dateien | Dateien liegen für SGB VI §§ 34-38, 77, 235, 236, 236a, 237 und 237a mit `source_urls`, `ingest_refs`, Fassungsstand und Abrufdatum vor. | ok mit Textqualitätsrestpunkt |
| Geburten 2024 als Basis für Kindererziehungszeiten | Destatis Lebendgeborene 2024 | Quelle ist als Ingest erfasst und für eine grobe Fortschreibung geeignet. Die Rechnung ersetzt keine DRV-Fallstatistik zu tatsächlich angerechneten Kindererziehungszeiten. | ok mit Begrenzung |
| Bundesbeiträge für Kindererziehungszeiten sind sachlich ausweisbar | DRV-Meldung Kindererziehungszeiten | Quelle stützt die rentenrechtliche Bedeutung und die Bundeszuständigkeit. Die Modellrechnung nutzt Durchschnittsentgelt und Geburtenzahl; das ist transparent, aber nicht haushaltsamtlich final. | offen |
| Pflegepersonen erzeugen rentenversicherungspflichtige Beitragszahlungen | BMG und DRV Pflegepersonen | Quellen bestätigen Beitragspflicht und Beitragszahlung durch die Pflegeversicherung. Für eine Haushaltswirkung fehlen Aufteilung nach Pflegegrad, Pflegestufe, Beitragsbemessung und Zahlungsträger. | offen |
| Nicht beitragsgedeckte Leistungen und Bundesmittel bleiben nur näherungsweise zerlegbar | Bundestagsdrucksache 21/1419, DRV/Bundeszuschuss-Quellen | Die Quellenlage bleibt wie im Konzept markiert: öffentlich nutzbare amtliche Zweckzerlegung für 2024-2026 ist nicht vollständig verfügbar. | offen |

## Gegenrechnung

### Rechnung 1: Rentenwert-Budgetfaktor

- Datenquelle: `analysen/daten/2026-06-06-rentenreform-freigabeblocker.csv`
- Formel: `Budgetfaktor = verfuegbares Budget / Referenzausgaben`
- Kontrollszenario: moderates Szenario, Zielkorridor 22 %

| Jahr | Variante | CSV-Budgetfaktor | Prüfer-Gegenrechnung | Saldo Mrd. Euro |
| ---: | --- | ---: | ---: | ---: |
| 2035 | Status quo 67 | 89,4 % | 89,4 % | -64,9 |
| 2035 | Lebenserwartung 2:1 | 95,0 % | 95,0 % | -28,6 |
| 2035 | Dänemark-nah | 100,0 % | 100,0 % | 7,1 |
| 2039 | Status quo 67 | 80,1 % | 80,1 % | -142,0 |
| 2039 | Lebenserwartung 2:1 | 87,3 % | 87,3 % | -83,1 |
| 2039 | Dänemark-nah | 95,8 % | 95,8 % | -25,2 |
| 2050 | Status quo 67 | 74,5 % | 74,5 % | -232,9 |
| 2050 | Lebenserwartung 2:1 | 87,5 % | 87,5 % | -98,5 |
| 2050 | Dänemark-nah | 94,9 % | 94,9 % | -37,1 |
| 2070 | Status quo 67 | 71,5 % | 71,5 % | -411,2 |
| 2070 | Lebenserwartung 2:1 | 97,0 % | 97,0 % | -32,6 |
| 2070 | Dänemark-nah | 100,0 % | 100,0 % | 8,6 |

Bewertung: Die CSV-Werte sind rechnerisch konsistent. Für eine Freigabe reicht
das noch nicht, weil der Budgetfaktor keine vollziehbare SGB-VI-Formel mit
Referenzjahr, Rentenwertanpassung, Schutzklauseln, Rundung, Zugangsrenten,
Bestandsrenten und Übergangsrecht ersetzt.

### Rechnung 2: Echte staatliche Beiträge

- Datenquelle:
  `analysen/daten/2026-06-06-staatsbeitraege-rentenreform.csv`
- Ergebnis Reformer und Prüfer:

| Jahr | Summe auszuweisender Staatsbeiträge Mrd. Euro |
| ---: | ---: |
| 2035 | 40,7 |
| 2039 | 44,9 |
| 2050 | 59,0 |
| 2070 | 96,6 |

- Kontrollwerte 2026:
  - Kindererziehungszeiten: 19,626 Mrd. Euro
  - Pflegepersonen: 5,773 Mrd. Euro

Bewertung: Die Größenordnung ist als Transparenzrechnung brauchbar. Als
Haushaltswirkung ist sie nicht freigegeben, weil die Gegenfinanzierung,
heutige bereits vorhandene Zahlungsströme, Trägeraufteilung und mögliche
Doppelzählungen noch nicht bereinigt sind.

### Rechnung 3: Feineres Rentenaltermodell

- Datenquelle:
  `analysen/daten/2026-06-06-rentenalter-feinmodell-altersjahre.csv`
- Ergebnis: Das Altersjahrmodell ersetzt die frühere pauschale Verschiebung
  und zeigt, dass stärkere Lebenserwartungs-Kopplung die Finanzierungslücke
  deutlich reduziert.
- Bewertung: Als Sensitivität besser als die Vorfassung. Für eine politische
  Freigabe fehlen weiterhin reale deutsche Altersjahrgänge, Erwerbsquoten,
  Rentenzugang nach Jahrgang, Abschlagsinanspruchnahme, Arbeitslosigkeit,
  Erwerbsminderung, Branchenbelastung und Verteilung nach Lebenserwartung.

## Normstand-Prüfung

Geprüfte neue Normstand-Dateien:

- `gesetzbuecher/sgb/sgb-vi-paragraf-34-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-35-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-36-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-37-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-38-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-77-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-235-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-236-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-236a-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-237-stand-2026-06-06.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-237a-stand-2026-06-06.md`

Befund: Der frühere Normstand-Blocker ist formal bearbeitet. Die lokalen
Dateien enthalten aber in mehreren extrahierten Listen und Tabellen
Formatierungsfehler, etwa zusammengezogene Buchstabenkennungen und
Tabellenköpfe. Das ist kein Rechenblocker, aber ein Rechtsarbeits-Restpunkt:
Vor einer konkreten Gesetzesänderung oder veröffentlichten Rechtsanalyse
müssen die Normtexte manuell gegen die amtliche Fassung bereinigt werden.

## Rechtsprüfung

- Zuständigkeit: Für die gesetzliche Rentenversicherung grundsätzlich
  tragfähig. Ausweitung auf neue Gruppen, echte Staatsbeiträge und ein
  Kapitalmarktbaustein benötigen separate Übergangs-, Haushalts- und
  Aufsichtsregeln.
- Grundrechte/Verfassung: Der Schutz erworbener Anwartschaften ist erkannt.
  Offen bleiben Kohortengleichheit, Berufsunfähigkeits- und
  Erwerbsminderungsfolgen, Belastung körperlich schwerer Berufe,
  Eigentums-/Vertrauensschutz bei Rentenwertdämpfung und Gleichbehandlung
  bisheriger Beamter, Selbständiger und berufsständischer Versorgungen.
- Übergangsrecht/Bestandsschutz: Konzeptuell vorhanden, aber noch nicht
  normiert. Rentennahe Jahrgänge, laufende Renten, bereits erworbene
  Entgeltpunkte und Neuzugang müssen getrennt geregelt werden.
- Vollzug: Die Beitragspflicht echter staatlicher Träger, das Meldewesen und
  die Schnittstellen zwischen Pflegeversicherung, BA, Dienstherren,
  Selbständigen und DRV sind noch nicht vollzugsreif beschrieben.
- Haushalt: Die Transparenzrechnung ersetzt keine doppelfreie
  Finanzplanung. Einige Zahlungen sind bereits heute Beitrags- oder
  Bundesmittelströme; die Reformwirkung darf nicht als vollständige
  Zusatzbelastung oder vollständige Entlastung gezählt werden.

## Kritische Gegenposition

Die stärkste Gegenposition lautet: Das Reformkonzept macht die
Finanzierungslücke sichtbar, löst sie aber nur durch politische Härten. Bei
festen Beitragssätzen sinkt der Rentenwert relativ zum Referenzpfad; bei
echten staatlichen Beiträgen steigt der Haushaltsdruck; bei späterem
Renteneintritt tragen Menschen mit geringerer gesunder Lebenserwartung einen
größeren Teil der Anpassung; bei zusätzlicher Kapitaldeckung steigt die
Belastung kurzfristig. Die Nachbesserung widerlegt diese Gegenposition nicht,
sondern zeigt präziser, wo die Entscheidungslasten liegen.

## Blocker

- Keine arithmetischen Blocker in der geprüften Nachbesserungsrechnung.
- Kein Quellenketten-Blocker für die neu genutzten amtlichen und
  gutachterlichen Ausgangsquellen.
- Freigabe bleibt offen, weil die Rentenwert-Budgetregel noch nicht als
  konkrete SGB-VI-Anpassungsformel vorliegt.
- Freigabe bleibt offen, weil das Rentenaltermodell trotz Verbesserung
  synthetisch bleibt und keine empirische feinjährige Kohortenrechnung
  ersetzt.
- Freigabe bleibt offen, weil die Haushaltswirkung echter Staatsbeiträge
  noch nicht doppelfrei gegen heutige Zahlungsströme abgegrenzt ist.
- Freigabe bleibt offen, weil für 2024 bis 2026 weiterhin keine vollständige
  öffentliche amtliche Bundesmittel-Zweckzerlegung vorliegt.

## Offene Punkte

- Lokale Normstand-Texte für SGB VI §§ 34-38, 77, 235, 236, 236a, 237 und
  237a manuell gegen die amtliche Fassung glätten.
- Budgetfaktor in einen konkreten Gesetzesmechanismus übersetzen:
  Referenzausgaben, aktueller Rentenwert, Schutzklausel, Zugangsrenten,
  Bestandsrenten, Rundung und Übergang.
- Altersjahrmodell mit deutschen Bevölkerungs-, Erwerbs-, Rentenzugangs- und
  Abschlagsdaten ersetzen.
- Staatsbeiträge als Netto-Haushaltswirkung berechnen: heutige Zahlungen,
  neue echte Beiträge, entfallende pauschale Bundesmittel, Trägeraufteilung
  und Doppelzählungen.
- Kapitalmarktbaustein rechtlich getrennt ausarbeiten: Träger, Aufsicht,
  Default-Mechanik, Kosten, Garantiefreiheit, Auszahlung und Opt-out.

## Nachbesserungen

- Eine Gesetzesänderungs-Skizze für die Rentenwert-Budgetregel anlegen und
  auf die geprüften Normstände verweisen.
- Ein reproduzierbares Kohortenmodell mit feinjährigen Altersdaten und
  altersspezifischen Erwerbsquoten ergänzen.
- Eine fiskalische Brückenrechnung bauen, die alle heutigen und künftigen
  Bundes-/Trägerzahlungen getrennt als Brutto-, Netto- und Umbuchungseffekt
  ausweist.
- Erst nach diesen Punkten einen neuen Prüferlauf mit möglicher
  Freigabeentscheidung starten.
