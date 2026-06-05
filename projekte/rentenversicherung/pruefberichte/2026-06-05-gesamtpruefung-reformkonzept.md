---
title: Prüfung Reformkonzept Rentenversicherung Gesamtprojekt
date: 2026-06-05
type: pruefbericht
status: offen
reviewed_report: projekte/rentenversicherung/reformkonzept.md
reviewer: pruefer
source_urls:
  - https://www.bmas.de/SharedDocs/Downloads/DE/Rente/rentenversicherungsbericht-2025.pdf?__blob=publicationFile&v=3
  - https://www.bmas.de/DE/Service/Presse/Pressemitteilungen/2026/bundeskabinett-beschliesst-rentenanpassung-2026.html
  - https://www.bmas.de/DE/Service/Presse/Pressemitteilungen/2025/das-aendert-sich-im-neuen-jahr.html
  - https://www.pensionsmyndigheten.se/other-languages/english-engelska/english-engelska/retirement-age
  - https://www.etk.fi/en/finnish-pension-system/pensions/determining-the-life-expectancy-coefficient-and-retirement-age/determining-the-retirement-age-for-the-old-age-pension/
  - https://star.dk/da/ydelser/pension-og-efterloen/folkepension-tidlig-pension-foertidspension-og-seniorpension/folkepension/folkepensionsalderen-nu-og-fremover/
  - https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/12/oecd-pensions-outlook-2024_6ac7d5fd/51510909-en.pdf
ingest_refs:
  - ingest/dokumente/2026-06-05-bmas-rentenversicherungsbericht-2025.md
  - ingest/links/2026-06-04-bmas-rentenanpassung-2026.md
  - ingest/links/2026-06-04-bmas-rechengroessen-2026.md
  - ingest/links/2026-06-05-schweden-richtalter-rente-lebenserwartung.md
  - ingest/links/2026-06-05-finnland-rentenalter-lebenserwartung.md
  - ingest/links/2026-06-05-daenemark-folkepensionsalter-lebenserwartung.md
  - ingest/dokumente/2026-06-05-oecd-pensions-outlook-2024-kapitalmarkt-defaults.md
---

# Prüfung: Reformkonzept Rentenversicherung Gesamtprojekt

## Prüfurteil

- Status: offen
- Kurzbegründung: Das Reformkonzept ist als Arbeitsfassung fachlich
  konsistent genug, um weiterentwickelt zu werden, aber noch nicht
  freigabefähig. Die zentralen Modellzahlen lassen sich aus den CSV- und
  Python-Artefakten reproduzieren. Freigabeblocker sind nicht ein einzelner
  Rechenfehler, sondern offene Rechts-, Normstand- und Modellpunkte:
  Altersgrenzen und Abschlagsnormen sind noch nicht lokal abgelegt, die
  Rentenalter-Kopplung ist nur eine Screeningrechnung, die Bundesmittel-
  Zerlegung bleibt Reformklassifikation und die konkrete Rentenwertformel ist
  noch nicht ausformuliert.

## Geprüfter Gegenstand

- Report: `projekte/rentenversicherung/reformkonzept.md`
- Prüfdatum: 2026-06-05
- Rechenartefakte:
  - `scripts/calc_rentenreform_zukunft.py`
  - `scripts/calc_rentenreform_stabilitaetskorridor.py`
  - `scripts/calc_rentenreform_rentenalter_kapital.py`
  - `analysen/daten/2026-06-04-rentenreform-zukunft-modell.csv`
  - `analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor.csv`
  - `analysen/daten/2026-06-05-rentenreform-rentenalter-kapital.csv`
  - `analysen/daten/2026-06-05-rentenreform-kapitalmarktbaustein.csv`
- Bestehender Teilprüfbericht:
  `projekte/rentenversicherung/pruefberichte/2026-06-04-abschmelzmodell-bundeszuschuss.md`

## Quellenprüfung

| Behauptung/Zahl | Quelle im Report | Unabhängige Prüfung | Ergebnis |
| --- | --- | --- | --- |
| Beitragssatz allgemeine RV 2026 18,6 %, knappschaftliche RV 24,7 %, BBG allgemeine RV 8.450 Euro monatlich | BMAS Rechengrößen 2026 | BMAS-Pressemitteilung "Das ändert sich im neuen Jahr" bestätigt Beitragssätze und Rechengrößen für 2026. | ok |
| Aktueller Rentenwert 40,79 Euro bis 30.06.2026 und 42,52 Euro ab 01.07.2026 | BMAS Rentenanpassung 2026 | BMAS-Pressemitteilung zur Rentenanpassung 2026 nennt Erhöhung von 40,79 Euro auf 42,52 Euro. | ok |
| Rentenversicherungsbericht 2025 als amtliche Vergleichsbasis bis 2039 | BMAS Rentenversicherungsbericht 2025 | Quelle ist im Ingest erfasst und als amtliche Bundesregierungsvorlage geeignet. Die lokale Langfristrechnung bis 2070 ist keine amtliche Projektion. | ok mit Abgrenzung |
| Schweden koppelt ein empfohlenes Rentenalter an Lebenserwartung | Schwedische Pensionsmyndigheten | Seite "Recommended retirement age" beschreibt eine Anpassung an durchschnittliche Lebenserwartung und nennt Planungs-/Zugangsfolgen. | ok |
| Finnland koppelt Rentenalter ab Jahrgang 1965 an Lebenserwartung | Finnish Centre for Pensions | ETK beschreibt die Reform von 2017, die Zielrelation Arbeitsleben/Rentenphase und die jährliche Anpassungsregel mit maximal zwei Monaten. | ok |
| Dänemark hebt Folkepensionsalter schrittweise an | Dänische STAR/BM | STAR-Seite bestätigt 68 ab 2030, 69 ab 2035 und 70 ab 2040. | ok |
| Kapitalmarktbaustein als Low-Cost-Default braucht Governance, Kostenkontrolle und Lebenszykluslogik | OECD/AP7-Ingests | OECD- und AP7-Quellen stützen die Governance-Richtung. Ein konkreter deutscher ETF oder Produktanbieter ist dadurch nicht freigegeben. | ok mit Begrenzung |

## Gegenrechnung

### Rechnung 1: Zukunftsmodell Beitragssätze

- Datenquelle: `analysen/daten/2026-06-04-rentenreform-zukunft-modell.csv`
- Formel: `erforderlicher_beitragssatz = (Ausgaben - Bundesmittel - sonstige Einnahmen) / Beitragsbasis`
- Ergebnis Reformer, moderates Szenario:
  - 2050: Status quo 25,1 %, Reform ohne neue Basis 32,1 %, Reform mit
    Erwerbstätigenbasis 29,8 %.
  - 2070: Status quo 26,1 %, Reform ohne neue Basis 33,9 %, Reform mit
    Erwerbstätigenbasis 30,9 %.
- Ergebnis Prüfer: CSV-Gegenlesung ergibt dieselben gerundeten Werte.
- Abweichung: keine relevante Rundungsabweichung.
- Bewertung: rechnerisch nachvollziehbar. Inhaltlich ist die Variante
  "Reform ohne neue Basis" erwartbar teurer, weil Bundesmittel abgeschmolzen
  werden, ohne die Beitragsbasis ausreichend zu verbreitern; das muss im
  Konzept weiter klar als Übergangsrisiko markiert bleiben.

### Rechnung 2: 22-%-Stabilitätskorridor

- Datenquelle: `analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor.csv`
- Formel: `Leistungsfaktor = leistbares Ausgabenvolumen / Referenzausgaben`
- Ergebnis Reformer, moderates Szenario:
  - 2035: 89,4 %
  - 2039: 80,1 %
  - 2050: 74,5 %
  - 2070: 71,5 %
- Ergebnis Prüfer: CSV-Gegenlesung ergibt dieselben gerundeten Werte.
- Bewertung: rechnerisch ok. Politisch und rechtlich ist aber noch offen, wie
  aus dem Leistungsfaktor eine konkrete Rentenwertformel wird und ob nominale
  Kürzungen, Schutzklauseln oder Übergangsdämpfungen vorgesehen sind.

### Rechnung 3: Rentenalter-Kopplung

- Datenquelle: `analysen/daten/2026-06-05-rentenreform-rentenalter-kapital.csv`
- Formel: pauschale Verschiebung von `0,95 Mio.` Personen je zusätzlichem
  Rentenalterjahr von der Renten- auf die Beitragsseite, danach neuer
  Beitragssatz aus angepassten Ausgaben und angepasster Beitragsbasis.
- Ergebnis Reformer, moderates Szenario:

| Jahr | Status quo 67 | Finnland-nahe Kopplung | Dänemark-nahe Kopplung |
| ---: | ---: | ---: | ---: |
| 2035 | 25,0 % | 23,2 % | 21,5 % |
| 2039 | 28,0 % | 25,4 % | 22,9 % |
| 2050 | 29,8 % | 25,0 % | 22,9 % |
| 2070 | 30,9 % | 23,1 % | 21,3 % |

- Ergebnis Prüfer: CSV-Gegenlesung bestätigt die Zahlen.
- Bewertung: als Screening plausibel, nicht freigabefähig als
  Gesetzesgrundlage. Die Rechnung nutzt keine feinjährigen Kohorten, keine
  altersspezifischen Erwerbsquoten, keine Arbeitslosigkeits-, Gesundheits- und
  Schwerarbeitsprofile und keine differenzierte vorgezogene Renteninanspruchnahme.

### Rechnung 4: Kapitalmarktbaustein

- Datenquelle: `analysen/daten/2026-06-05-rentenreform-kapitalmarktbaustein.csv`
- Formel: 40 Jahre jährliche Einzahlung aus Durchschnittsentgelt 2026,
  reale Renditeannahme, Verrentung über 20 Jahre.
- Ergebnis Reformer: Bei 2 % Zusatzbeitrag und 3 % realer Rendite entstehen
  rund 78.333 Euro reales Kapital und rund 439 Euro reale Monatszahlung über
  20 Jahre.
- Ergebnis Prüfer: CSV-Gegenlesung bestätigt gerundet 78.333 Euro und 439 Euro.
- Bewertung: mathematisch ok, aber nicht ausreichend für Produktfreigabe.
  Fehlend sind Kostenquote, Steuern/Abgaben, Verwaltungskosten, Langlebigkeits-
  pooling, Auszahlungsmodus, Sequenzrisiko und Garantiefreiheit.

## Normstand-Prüfung

Geprüfte vorhandene Normstand-Dateien, stichprobenartig und inhaltlich passend
zum aktuellen Reformkonzept:

- `gesetzbuecher/sgb/sgb-vi-paragraf-1-stand-2026-06-05.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-2-stand-2026-06-05.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-63-stand-2026-06-05.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-66-stand-2026-06-05.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-157-stand-2026-06-05.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-158-stand-2026-06-05.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-213-stand-2026-06-05.md`
- `gesetzbuecher/sgb/sgb-vi-paragraf-216-stand-2026-06-05.md`
- `gesetzbuecher/grundgesetz/gg-artikel-3-stand-2026-06-05.md`
- `gesetzbuecher/grundgesetz/gg-artikel-14-stand-2026-06-05.md`
- `gesetzbuecher/grundgesetz/gg-artikel-20-stand-2026-06-05.md`
- `gesetzbuecher/grundgesetz/gg-artikel-33-stand-2026-06-05.md`

Befund: Für die ältere Fassung des Reformkonzepts liegt ein breites
Normstand-Paket vor. Seit der Ergänzung der Rentenalter-Kopplung fehlen aber
tragende Normstände für Regelaltersgrenze, vorgezogene Altersrenten und
Zugangs-/Abschlagslogik, insbesondere voraussichtlich SGB VI §§ 35 ff. und
§ 77. Das Reformkonzept benennt diesen Bedarf selbst als Folgearbeit. Solange
diese Normstände fehlen, ist keine Freigabe einer Altersgrenzen-Rechtsanalyse
oder Gesetzesänderung möglich.

## Rechtsprüfung

- Zuständigkeit: Bundesgesetzgebung für die gesetzliche Rentenversicherung ist
  grundsätzlich tragfähig. Beamtenversorgung, berufsständische Versorgung,
  Selbständigenpflicht und Kapitalmarktbaustein berühren aber zusätzliche
  Zuständigkeits- und Übergangsfragen.
- Grundrechte/Verfassung: Die Linie "keine rückwirkende Enteignung, Schutz
  erworbener Anwartschaften, Neuzugangsregeln" ist verfassungsnäher als eine
  rückwirkende Einbeziehung. Kritisch bleiben Gleichbehandlung zwischen
  Kohorten, Beamtenstatus, Eigentumsschutz und Vertrauensschutz bei einer
  Rentenwert-Budgetregel.
- Übergangsrecht/Bestandsschutz: Das Konzept erkennt Bestandsschutz korrekt
  als Kernproblem. Noch offen ist, welche Jahrgänge, Berufsgruppen und
  rentennahen Personen wie lange geschützt werden.
- Vollzug: Die Ausweitung auf Selbständige, Neubeamte, staatliche
  Zahlungspflichtige und Kapitalmarktverwaltung erzeugt erheblichen
  Verwaltungsaufwand. Es fehlen Melde-, Prüf-, Säumnis-, Einkommensschätz- und
  Schnittstellenregeln.
- Haushalt: Die Forderung echter staatlicher Beiträge ist transparent, kann
  aber Bundes- und Sozialhaushalte kurzfristig erheblich belasten. Ohne
  konkrete jährliche Volumina für Kindererziehung, Pflege, Arbeitslosigkeit,
  Dienstzeiten und Übergänge ist die Haushaltswirkung nicht freigabefähig.

## Kritische Gegenposition

Die stärkste Gegenposition lautet: Das Konzept löst das Rentenproblem nicht,
sondern macht die Kosten nur sichtbarer und verschiebt sie politisch. Wenn der
Beitragssatz gedeckelt wird, fällt der Leistungsfaktor deutlich unter den
Referenzpfad. Wenn staatliche Beitragszahlungen vollständig ehrlich verbucht
werden, steigt der Druck im Bundeshaushalt. Wenn das Rentenalter stark an die
Lebenserwartung gekoppelt wird, tragen gesundheitlich belastete Gruppen einen
überproportionalen Teil der Last. Wenn ein Kapitalmarktbaustein zusätzlich
finanziert wird, steigen die Abgaben kurzfristig weiter; wenn er aus
Umlagebeiträgen finanziert wird, reißt er eine neue Finanzierungslücke.

Diese Gegenposition widerlegt das Konzept nicht vollständig. Sie zeigt aber,
dass das Konzept nur freigabefähig wird, wenn es ehrlich zwischen drei
Entscheidungen trennt: höhere Beiträge oder längere Erwerbsphase, geringerer
Referenz-Leistungspfad oder höhere echte Staatsbeiträge.

## Blocker

- Fehlende Normstand-Dateien und Rechtsprüfung für Altersgrenzen,
  vorgezogene Altersrenten, Zugangsfaktor/Zuschläge/Abschläge und
  Kapitalmarktbaustein.
- Keine konkrete Rentenwertformel für die Budgetregel; der Leistungsfaktor ist
  noch kein vollziehbarer Gesetzesmechanismus.
- Rentenalter-Kopplung nur Screeningrechnung mit pauschaler Kohortengröße.
- Bundesmittel-Zerlegung weiterhin Reformklassifikation, keine amtliche
  Zweckzerlegung für 2024 bis 2026.
- Haushaltswirkung echter staatlicher Beiträge für Sozialzeiten nicht
  quantifiziert.

## Offene Punkte

- Feinjährige Kohortenrechnung mit Erwerbsquoten, Arbeitslosigkeit,
  gesundheitlichen Einschränkungen und vorgezogener Renteninanspruchnahme.
- Volumen nicht beitragsgedeckter Rentenwirkungen je Norm und
  Zahlungspflichtigem.
- Übergangsmodell für Selbständige, Beamte, berufsständische Versorgung und
  rentennahe Jahrgänge.
- Governance-Modell für Kapitalmarktbaustein: Institution, Kostenlimit,
  Anlageuniversum, Auszahlungsphase, Haftung und politischer Zugriffsschutz.
- Sensitivität zu niedrigeren realen Kapitalmarktrenditen, Verwaltungskosten
  und längerer Rentenbezugsdauer.

## Nachbesserungen

- Normstand-Bedarf auf Altersgrenzen, vorgezogene Altersrenten,
  Zugangsfaktor/Abschläge und Kapitalmarktgesetz erweitern und die Dateien vor
  einer Gesetzesänderungsskizze anlegen.
- Rentenwert-Budgetregel als konkrete Formel mit Schutzklauseln,
  Übergangspfad und automatischen Auslösern formulieren.
- Rentenalter-Kopplung mit feinjährigen Altersdaten und Erwerbsquoten neu
  rechnen.
- Staatliche Beitragszahlungen für Kindererziehung, Pflege, Arbeitslosigkeit,
  Dienstzeiten und Übergangsgruppen jährlich quantifizieren.
- Kapitalmarktbaustein nicht als ETF-Empfehlung formulieren, sondern als
  regulierten Default mit Kosten- und Governance-Regeln.
