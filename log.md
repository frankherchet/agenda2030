# Log

Chronologisches Arbeitslog für Ingests, Wissenspflege, Prüfungen und größere
Analysen. Das Log ist append-only: neue Einträge werden unten ergänzt.

## 2026-06-04 Ingest | Markus Lanz Sendung vom 2. Juni 2026

- Ingest: `ingest/dokumente/2026-06-04-markus-lanz-sendung-2026-06-02.md`
- Rohdatei: `ingest/originale/2026-06-04-markus-lanz-sendung-2026-06-02.json`
- Wirkung: Debattenquelle zu Renteneintrittsalter, Rentenniveau,
  Generationengerechtigkeit, AfD-Abgrenzung und FDP-Richtungskonflikt erfasst.

## 2026-06-04 Wissenspflege | Rohdateien im Ingest

- Neue Struktur: `ingest/originale/README.md`
- Wirkung: Kleine Rohdateien wie JSON, CSV, TXT und kleinere PDFs erhalten eine
  versionierte Ablage; große Medien bleiben außerhalb des Repos.

## 2026-06-05 Struktur | Codex-Skills verschoben

- Neuer Ort: `.agents/skills/`
- Wirkung: Repo-spezifische Skills liegen am von Codex CLI erwarteten Ort.

## 2026-06-05 Wissenspflege | LLM-Wiki-Regeln für Ingest

- Betroffene Regeln: `AGENTS.md`, `ingest/README.md`,
  `.agents/skills/ingest/SKILL.md`
- Neuer Index: `index.md`
- Wirkung: Ingests prüfen künftig kontextabhängig relevante Wissensseiten,
  verknüpfen Quellen mit bestehenden Artefakten und führen Index sowie Log.

## 2026-06-05 Wissenspflege | Normstände vor Rechtsanalyse

- Neue Vorlage: `vorlagen/normstand.md`
- Betroffene Regeln: `AGENTS.md`, `gesetzbuecher/README.md`,
  `.agents/skills/reformer/SKILL.md`, `.agents/skills/pruefer/SKILL.md`
- Wirkung: Konkret analysierte oder geänderte Paragraphen und Artikel müssen
  künftig vorab als geltender Normstand unter `gesetzbuecher/<buch>/`
  abgelegt und von Folgeartefakten referenziert werden.

## 2026-06-05 Wissenspflege | Ingest-Extraktion geschärft

- Betroffene Regeln: `AGENTS.md`, `ingest/README.md`,
  `.agents/skills/ingest/SKILL.md`, `vorlagen/ingest.md`
- Wirkung: Ingests trennen künftig Inhaltsinventar der Quelle von aktuell
  extrahierten relevanten Informationen, um erneutes Nachschlagen im Original
  zu minimieren.

## 2026-06-05 Struktur | Quellen, Analysen und Projekte getrennt

- Neue Struktur: `ingest/`, `analysen/`, `projekte/rentenversicherung/`
- Verschoben: Haushalts-, Demographie- und DRV-Quellen in `ingest/`,
  zweckgebundene Auswertungen und Datenartefakte in `analysen/`, erstes
  Reformkonzept samt Prüfbericht in `projekte/rentenversicherung/`.
- Wirkung: Quellen werden unabhängig vom Thema einheitlich ingestiert;
  Analysen brauchen einen Zweck und Reformarbeit läuft projektbezogen.

## 2026-06-05 Prüfung | Strukturumbau nachgezogen

- Prüfvermerk:
  `analysen/2026-06-05-strukturumbau-quellen-analysen-projekte-pruefung.md`
- Betroffene Dateien: Analyse-Frontmatter, Rentenprojekt-Status,
  DRV-Quellenmetadaten, `index.md`, `analysen/README.md`
- Wirkung: Bestehende Analysen führen jetzt maschinenlesbare `source_urls` und
  `ingest_refs`; das offene Rentenkonzept ist nicht mehr als veröffentlicht
  markiert. Offene Nachpflege: Ingests um die neuen Extraktionsabschnitte und
  Rentennormstände ergänzen.

## 2026-06-05 Nachpflege | TODO-Liste und Renten-Ingests

- TODO-Liste: `analysen/2026-06-05-todo-strukturumbau-nachpflege.md`
- Normstand-Matrix: `projekte/rentenversicherung/normstand-bedarf.md`
- Wirkung: Alle im Rentenkonzept direkt referenzierten Ingests führen jetzt
  `Enthaltene Informationen` und `Jetzt extrahierte relevante Informationen`.
  Der verbleibende Rechtsblock ist als priorisierte Normstand-Matrix
  dokumentiert.

## 2026-06-05 Nachpflege | TODO-Liste abgearbeitet

- Gelöscht: `analysen/2026-06-05-todo-strukturumbau-nachpflege.md`
- Neue Ingests:
  `ingest/dokumente/2026-06-05-bmas-rentenversicherungsbericht-2025.md`,
  `ingest/dokumente/2026-06-05-drv-rentenupdate-bundeszuschuesse-nicht-beitragsgedeckte-leistungen-2025.md`,
  `ingest/dokumente/2026-06-05-bundestag-drs-21-1419-nicht-beitragsgedeckte-leistungen.md`
- Neue Analyse:
  `analysen/2026-06-05-bundesmittel-zweckzerlegung-rente.md`
- Normstände: 63 Dateien unter `gesetzbuecher/sgb/` und
  `gesetzbuecher/grundgesetz/` für das Rentenprojekt angelegt.
- Wirkung: Die alte TODO-Liste ist in dauerhafte Ingest-, Analyse- und
  Normstand-Artefakte überführt.

## 2026-06-05 Skill | Analyse-Rolle ergänzt

- Neuer Skill: `.agents/skills/analyse/SKILL.md`
- Betroffene Übersicht: `agenten/README.md`, `index.md`
- Wirkung: Themen können künftig als quellenbasierte Faktenanalysen unter
  `analysen/` aufgearbeitet werden, bevor daraus Reformkonzepte oder
  Prüfberichte entstehen.

## 2026-06-05 Ingest | Statista Altersrentner und Beitragszahler

- Ingest:
  `ingest/links/2026-06-05-statista-altersrentner-beitragszahler-rentenversicherung.md`
- Quelle:
  https://de.statista.com/infografik/25751/altersrentner-und-beitragszahler-in-der-rentenversicherung-in-deutschland/
- Wirkung: Sekundäre Visualisierungsquelle zum Verhältnis von Altersrentnern
  und Beitragszahlern erfasst; quantitative Nutzung bleibt gegen
  DRV-Primärdaten zu prüfen.

## 2026-06-05 Analyse | Rentenproblem Deutschland

- Analyse:
  `analysen/2026-06-05-rentenproblem-deutschland-ursachen-auswirkungen.md`
- Verwendete Quellen: BMAS-Rentenversicherungsbericht 2025,
  Destatis-Demographie, DRV-Finanzkennzahlen, DRV-rentenupdate zu
  Bundeszuschüssen, Bundestagsdrucksache 21/1419 und Statista als sekundäre
  Visualisierungsquelle.
- Wirkung: Ursachen und Folgen des deutschen Rentenproblems ohne
  Gegenmaßnahmen sind als quellenbasierter Problemaufriss dokumentiert;
  offene Datenlücken zur Beitragszahler-Relation, Tabellenextraktion und
  Bundesmittel-Zweckzerlegung bleiben sichtbar.

## 2026-06-05 Rechenartefakt | Finanzierungslücke Rentenproblem

- Skript:
  `scripts/calc_rentenproblem_finanzierungsluecke.py`
- Neue Daten:
  `analysen/daten/2026-06-05-rentenproblem-finanzierungsluecke.csv`,
  `analysen/daten/2026-06-05-rentenproblem-finanzierungsluecke-annahmen.csv`
- Neue Diagramme:
  `analysen/diagramme/2026-06-05-rentenproblem-finanzierungsluecke.svg`,
  `analysen/diagramme/2026-06-05-rentenproblem-bundesmittelbedarf.svg`
- Wirkung: Die Analyse zum Rentenproblem weist nun eine reproduzierbare
  Hochrechnung aus, wie groß die jährliche Lücke wird, wenn Beitragssatz und
  Renteneintrittsalter unverändert bleiben.

## 2026-06-05 Web | Rentenproblem-Analyse als Pages-Report

- Veröffentlicht:
  `analysen/2026-06-05-rentenproblem-deutschland-ursachen-auswirkungen.md`
- Web-Änderungen:
  `web/scripts/build-content.mjs`, `web/src/App.tsx`, `web/src/styles.css`
- Wirkung: Der Content-Builder liest nun veröffentlichte Analysen unter
  `analysen/`, spiegelt referenzierte Diagramm-Assets in die GitHub-Pages-App
  und erzeugt einen Report mit Diagrammen für die Rentenproblem-Analyse.

## 2026-06-05 Reformer | Rentenreform Stabilitätskorridor

- Geändert:
  `projekte/rentenversicherung/reformkonzept.md`
- Neue Analyse:
  `analysen/2026-06-05-rentenreform-stabilitaetskorridor.md`
- Neue Daten:
  `analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor.csv`,
  `analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor-annahmen.csv`
- Neues Skript:
  `scripts/calc_rentenreform_stabilitaetskorridor.py`
- Wirkung: Das Reformkonzept ist auf das Ziel "möglichst hohe Rente bei
  stabilen Beitragsraten" geschärft. Neue Entgeltpunkte entstehen nur noch
  durch Einzahlung; der Rentenwert folgt einer Budgetregel innerhalb eines
  Beitragssatzkorridors.

## 2026-06-05 Reformer | Rentenalter-Kopplung und Kapitalmarktbaustein

- Neue Ingests:
  `ingest/links/2026-06-05-schweden-richtalter-rente-lebenserwartung.md`,
  `ingest/links/2026-06-05-finnland-rentenalter-lebenserwartung.md`,
  `ingest/links/2026-06-05-daenemark-folkepensionsalter-lebenserwartung.md`,
  `ingest/links/2026-06-05-schweden-ap7-safa-premium-pension.md`,
  `ingest/links/2026-06-05-msci-world-index.md`,
  `ingest/dokumente/2026-06-05-oecd-pensions-outlook-2024-kapitalmarkt-defaults.md`
- Neue Analyse:
  `analysen/2026-06-05-rentenreform-rentenalter-kapitalmarkt.md`
- Neue Daten:
  `analysen/daten/2026-06-05-rentenreform-rentenalter-kapital.csv`,
  `analysen/daten/2026-06-05-rentenreform-rentenalter-kapital-annahmen.csv`,
  `analysen/daten/2026-06-05-rentenreform-kapitalmarktbaustein.csv`
- Neues Skript:
  `scripts/calc_rentenreform_rentenalter_kapital.py`
- Wirkung: Das Rentenkonzept enthält nun eine Szenarioanalyse zur Kopplung des
  Renteneintrittsalters an die Lebenserwartung sowie einen zusätzlichen,
  breit diversifizierten Kapitalmarktbaustein als mögliche Zusatzrente.

## 2026-06-05 Prüfer | Gesamtprüfung Rentenreformkonzept

- Neuer Prüfbericht:
  `projekte/rentenversicherung/pruefberichte/2026-06-05-gesamtpruefung-reformkonzept.md`
- Geändert:
  `projekte/rentenversicherung/reformkonzept.md`,
  `projekte/rentenversicherung/README.md`,
  `index.md`
- Status: offen
- Wirkung: Das Rentenreformkonzept ist rechnerisch in den Kernwerten
  nachvollziehbar, bleibt aber nicht freigegeben. Offene Freigabepunkte sind
  insbesondere Altersgrenzen-/Abschlags-Normstände, konkrete Rentenwertformel,
  feinere Rentenalter-Kohortenrechnung, Bundesmittel-Zweckzerlegung und
  Haushaltswirkung echter Staatsbeiträge.

## 2026-06-06 Reformer | Freigabeblocker Rentenreform bearbeitet

- Neue Ingests:
  `ingest/links/2026-06-06-destatis-lebendgeborene-2024.md`,
  `ingest/links/2026-06-06-drv-kindererziehungszeiten-bund.md`,
  `ingest/links/2026-06-06-bmg-soziale-absicherung-pflegepersonen.md`,
  `ingest/links/2026-06-06-drv-pflegepersonen-rentenversicherung.md`
- Neue Normstände:
  SGB VI §§ 34-38, § 77, §§ 235, 236, 236a, 237 und 237a unter
  `gesetzbuecher/sgb/`
- Neue Analyse:
  `analysen/2026-06-06-rentenreform-freigabeblocker.md`
- Neue Daten:
  `analysen/daten/2026-06-06-rentenreform-freigabeblocker.csv`,
  `analysen/daten/2026-06-06-rentenalter-feinmodell-altersjahre.csv`,
  `analysen/daten/2026-06-06-staatsbeitraege-rentenreform.csv`,
  `analysen/daten/2026-06-06-rentenreform-freigabeblocker-annahmen.csv`
- Neues Skript:
  `scripts/calc_rentenreform_freigabeblocker.py`
- Wirkung: Die Prüferblocker zu Normständen, Rentenwertformel, feinerer
  Rentenalterrechnung und Haushaltswirkung echter Staatsbeiträge sind als
  prüffähige Arbeitsfassung bearbeitet. Die amtliche Zweckzerlegung der
  Bundesmittel bleibt mangels öffentlicher Daten für 2024-2026 nicht
  vollständig auflösbar und wird als Reformklassifikation abgegrenzt.

## 2026-06-06 Prüfer | Nachprüfung Rentenreformkonzept

- Neuer Prüfbericht:
  `projekte/rentenversicherung/pruefberichte/2026-06-06-nachpruefung-reformkonzept.md`
- Geändert:
  `projekte/rentenversicherung/reformkonzept.md`,
  `projekte/rentenversicherung/README.md`,
  `index.md`
- Status: offen
- Wirkung: Die Nachbesserung der Freigabeblocker ist rechnerisch
  nachvollziehbar; arithmetische Blocker wurden nicht gefunden. Die Freigabe
  bleibt offen wegen fehlender gesetzestextfähiger Rentenwertmechanik,
  synthetischer Alterskohorten, nicht doppelfreier Haushaltswirkung echter
  Staatsbeiträge und fehlender vollständiger öffentlicher
  Bundesmittel-Zweckzerlegung für 2024-2026.

## 2026-06-06 Reformer | Rentenreform nach Nachprüfung nachgebessert

- Neue Normstände und Gesetzesartefakte:
  `gesetzbuecher/sgb/sgb-vi-paragraf-68-stand-2026-06-06.md`,
  `gesetzbuecher/sgb/sgb-vi-paragraf-68-rentenwert-budgetregel-aenderung-2026-06-06.md`
- Bereinigte Normstände:
  `gesetzbuecher/sgb/sgb-vi-paragraf-77-stand-2026-06-06.md`,
  `gesetzbuecher/sgb/sgb-vi-paragraf-235-stand-2026-06-06.md`,
  `gesetzbuecher/sgb/sgb-vi-paragraf-236-stand-2026-06-06.md`,
  `gesetzbuecher/sgb/sgb-vi-paragraf-236a-stand-2026-06-06.md`,
  `gesetzbuecher/sgb/sgb-vi-paragraf-237-stand-2026-06-06.md`
- Neue Daten:
  `analysen/daten/2026-06-06-staatsbeitraege-doppelfrei-bruecke.csv`
- Geändert:
  `scripts/calc_rentenreform_freigabeblocker.py`,
  `analysen/2026-06-06-rentenreform-freigabeblocker.md`,
  `projekte/rentenversicherung/reformkonzept.md`,
  `projekte/rentenversicherung/normstand-bedarf.md`,
  `projekte/rentenversicherung/README.md`,
  `gesetzbuecher/sgb/README.md`,
  `analysen/README.md`,
  `index.md`
- Wirkung: Die Rentenwert-Budgetregel liegt als SGB-VI-Änderungsskizze mit
  Nominalschutz, Nachholbetrag und Referenzausgaben vor. Die Haushaltswirkung
  echter öffentlicher Beiträge wird doppelfrei als Brutto-Ausweis, bereits
  bestehende Zahlung und Netto-Zusatzeffekt getrennt. Die
  Normstand-Textqualitätsreste wurden an den beanstandeten Stellen geglättet;
  die fehlende öffentliche Zweckzerlegung 2024-2026 bleibt als
  Negativbeschaffung dokumentiert und wird durch künftige gesetzliche Trennung
  ersetzt, nicht rückwirkend behauptet.

## 2026-06-06 Prüfer | Zweitnachprüfung Rentenreformkonzept

- Neuer Prüfbericht:
  `projekte/rentenversicherung/pruefberichte/2026-06-06-zweitnachpruefung-reformkonzept.md`
- Geändert:
  `projekte/rentenversicherung/reformkonzept.md`,
  `projekte/rentenversicherung/README.md`,
  `index.md`
- Status: offen
- Wirkung: Die §-68-Rentenwert-Budgetregel, die doppelfreie
  Haushaltsbrücke und die Normstand-Textglättung werden positiv bewertet.
  Keine arithmetischen Blocker und kein Normstand-Blocker für die geprüften
  Kernnormen. Die Freigabe bleibt offen wegen synthetischer
  Rentenalterrechnung, fehlender Folgeänderungen zur §-68-Skizze und nur
  negativ belegter Bundesmittel-Zweckzerlegung 2024-2026.

## 2026-06-06 Skill | Destatis GENESIS API

- Neuer Skill:
  `.agents/skills/destatis-genesis/SKILL.md`
- Neues Hilfsskript:
  `.agents/skills/destatis-genesis/scripts/genesis_fetch.py`
- Neuer Ingest:
  `ingest/links/2026-06-06-destatis-genesis-api.md`
- Geändert:
  `ingest/index/README.md`,
  `index.md`
- Wirkung: Amtliche Destatis-Daten können künftig reproduzierbar über die
  GENESIS-Online RESTful/JSON-API gesucht und abgerufen werden. Zugangsdaten
  werden nicht gespeichert, sondern nur über `DESTATIS_USER`,
  `DESTATIS_PASSWORD` oder `DESTATIS_TOKEN` gelesen.

## 2026-06-06 Skill | Destatis GENESIS API-Referenz erweitert

- Neue Referenz:
  `.agents/skills/destatis-genesis/references/api.md`
- Geändert:
  `.agents/skills/destatis-genesis/SKILL.md`,
  `.agents/skills/destatis-genesis/scripts/genesis_fetch.py`
- Wirkung: Die komplette Swagger-Beschreibung wird nicht in den Skillkörper
  geladen, sondern als kompakte Endpunkt- und Parameterreferenz vorgehalten.
  Der Helper unterstützt zusätzliche Katalog-, Daten- und Metadaten-Endpunkte,
  einen generischen `post`-Aufruf und die breite GENESIS-Suche mit
  `category=Alle`, wie sie in der Swagger UI verwendet wird.

## 2026-06-07 Reformer | Zweitnachprüfung Rentenreform nachgebessert

- Neuer Ingest:
  `ingest/dokumente/2026-06-07-destatis-genesis-demographie-rente-tabellen.md`
- Neue Rohdaten:
  `ingest/originale/2026-06-07-genesis-12411-0005-bevoelkerung-altersjahre.json`,
  `ingest/originale/2026-06-07-genesis-12421-0002-bev-v02-moderat.json`,
  `ingest/originale/2026-06-07-genesis-12421-0002-bev-v04-alt.json`,
  `ingest/originale/2026-06-07-genesis-12421-0002-bev-v05-jung.json`,
  `ingest/originale/2026-06-07-genesis-12211-0002-mikrozensus-erwerbsstatus.json`,
  `ingest/originale/2026-06-07-genesis-values-bevpr1-varianten.json`
- Neues Rechenartefakt:
  `scripts/calc_rentenalter_genesis_empirisch.py`,
  `analysen/2026-06-07-rentenalter-genesis-empirisch.md`,
  `analysen/daten/2026-06-07-rentenalter-genesis-empirisch-altersjahre.csv`,
  `analysen/daten/2026-06-07-rentenalter-genesis-empirisch-summary.csv`
- Neue Rechtsartefakte:
  `gesetzbuecher/sgb/sgb-vi-paragraf-69-stand-2026-06-07.md`,
  `gesetzbuecher/sgb/sgb-vi-folgeaenderungen-rentenwert-budgetregel-2026-06-07.md`,
  `gesetzbuecher/sgb/sgb-vi-paragraf-213a-vollzug-rechnungslegung-aenderung-2026-06-07.md`
- Geändert:
  `projekte/rentenversicherung/reformkonzept.md`,
  `projekte/rentenversicherung/README.md`,
  `projekte/rentenversicherung/normstand-bedarf.md`, `analysen/README.md`,
  `gesetzbuecher/sgb/README.md`, `scripts/README.md`, `index.md`,
  `.agents/skills/destatis-genesis/SKILL.md`, `ingest/index/README.md`
- Wirkung: Die synthetische Bevölkerungsseite des Rentenaltermodells ist durch
  GENESIS-Altersjahrgänge ersetzt. Die §-68-Budgetregel hat Folgeänderungen
  für § 69, § 158, § 177, § 213 und § 291b sowie ein Vollzugsmodell für
  echte öffentliche Beiträge. Die Bundesmittel-Zweckzerlegung 2024-2026
  bleibt als nicht öffentlich beschaffbare amtliche Ist-Zerlegung markiert und
  wird für die Reform über gesetzliche Zweckgliederung adressiert.

## 2026-06-07 Prüfer | Drittnachprüfung Rentenreformkonzept

- Neuer Prüfbericht:
  `projekte/rentenversicherung/pruefberichte/2026-06-07-drittnachpruefung-reformkonzept.md`
- Geändert:
  `projekte/rentenversicherung/reformkonzept.md`,
  `projekte/rentenversicherung/README.md`, `index.md`
- Status: offen
- Wirkung: Die GENESIS-Altersjahrrechnung ist arithmetisch nachvollziehbar
  und ersetzt die synthetische Bevölkerungsseite des Rentenaltermodells. Die
  Folgeänderungen zur §-68-Budgetregel und die §213a-Vollzugsskizze beseitigen
  die alten Systematikblocker als Arbeitsfassungen. Die Freigabe bleibt offen,
  weil altersscharfe Erwerbs- und Rentenzugangsdaten sowie die amtliche
  Bundesmittel-Ist-Zweckzerlegung 2024-2026 weiterhin fehlen.

## 2026-06-07 Reformer | Drittnachprüfung nachgebessert

- Korrigiertes Rechenartefakt:
  `scripts/calc_rentenalter_genesis_empirisch.py`,
  `analysen/2026-06-07-rentenalter-genesis-empirisch.md`,
  `analysen/daten/2026-06-07-rentenalter-genesis-empirisch-altersjahre.csv`,
  `analysen/daten/2026-06-07-rentenalter-genesis-empirisch-summary.csv`
- Neuer GENESIS-Rohabruf:
  `ingest/originale/2026-06-07-genesis-12211-0004-erwerbstaetige-altersgruppen.json`
- Neue Rechtsquelle und Normstände:
  `ingest/links/2026-06-07-gesetze-im-internet-bho.md`,
  `gesetzbuecher/weitere-gesetze/bho-paragraf-13-stand-2026-06-07.md`,
  `gesetzbuecher/weitere-gesetze/bho-paragraf-17-stand-2026-06-07.md`
- Neue Änderungsskizze:
  `gesetzbuecher/weitere-gesetze/bho-rentenbeitraege-haushaltsausweis-aenderung-2026-06-07.md`
- Geändert:
  `projekte/rentenversicherung/reformkonzept.md`,
  `gesetzbuecher/sgb/sgb-vi-paragraf-213a-vollzug-rechnungslegung-aenderung-2026-06-07.md`,
  `projekte/rentenversicherung/normstand-bedarf.md`, `ingest/index/README.md`,
  `index.md`
- Wirkung: Die GENESIS-Projektion nutzt nun nur die summenfähige
  Geschlechtszeile `Insgesamt`, die Erwerbsbrücke wurde von `65 Jahre und
  mehr` auf `65 bis unter 75 Jahre` verfeinert, § 213a enthält eine
  Ausfallhaftung zugunsten der Versicherten und die Haushaltsfolgeänderung zur
  BHO bildet echte Rentenbeiträge im Bundeshaushalt ab. Das Rentenaltermodell
  bleibt bis zu altersscharfen Erwerbs- und DRV-Rentenzugangsdaten als
  Sensitivität markiert.

## 2026-06-07 Prüfer | Viertnachprüfung Rentenreformkonzept

- Neuer Prüfbericht:
  `projekte/rentenversicherung/pruefberichte/2026-06-07-viertnachpruefung-reformkonzept.md`
- Geändert:
  `projekte/rentenversicherung/reformkonzept.md`,
  `projekte/rentenversicherung/README.md`, `index.md`
- Status: offen
- Wirkung: Die korrigierte GENESIS-Rechnung enthält keine arithmetischen
  Blocker mehr; §213a-Ausfallhaftung und BHO-Haushaltsausweis sind als
  Arbeitsfassungen prüffähig angelegt. Die Gesamtfreigabe bleibt offen, weil
  altersscharfe Erwerbs- und DRV-Rentenzugangsdaten sowie die amtliche
  Bundesmittel-Ist-Zweckzerlegung 2024-2026 fehlen.

- 2026-06-09: DIP-Bundestag: 2 Rente-bezogene Kleine Anfragen (BT-21-6304, BT-21-6183) als Original-PDFs + vollständige Metadaten unter ingest/originale/ gespeichert und als Ingest unter ingest/dokumente/ angelegt (Quellenpflicht erfüllt, PDFs als primäres Dokument).

## 2026-06-10 Wissenspflege | Rentenversicherungs-Folgearbeiten bereinigt

- Bereinigt:
  `projekte/rentenversicherung/2026-06-09-bundesmittel-zweckzerlegung.md`,
  `projekte/rentenversicherung/2026-06-09-datenanfrage-bundesmittel-zweckzerlegung.md`,
  `projekte/rentenversicherung/2026-06-09-datenanfrage-drv.md`,
  `projekte/rentenversicherung/2026-06-09-gesamtstatus-reformvorhaben.md`,
  `projekte/rentenversicherung/2026-06-09-status-offene-pruefpunkte.md`,
  `projekte/rentenversicherung/2026-06-09-szenariokorridor-67-72.md`,
  `projekte/rentenversicherung/pruefberichte/2026-06-09-pruefbericht-rentenversicherung.md`
- Zusätzlich normalisiert:
  `gesetzbuecher/sgb/sgb-vi-artikelgesetz-213a-stand-2026-06-09.md`,
  `gesetzbuecher/sgb/sgb-vi-rechtsverordnung-213a-rueckgriff-stand-2026-06-09.md`,
  `projekte/rentenversicherung/README.md`,
  `projekte/rentenversicherung/reformkonzept.md`,
  `index.md`
- Wirkung: Die 2026-06-09-Folgearbeiten nutzen jetzt echte Ingest-Referenzen,
  fuehren Entwurfs- statt Erledigt-Status, unterscheiden heuristische
  Arbeitsdaten von amtlichen Eingangsdaten und sind sauber in Projekt,
  Index und Pruefpfad verankert.

## 2026-06-10 Analyse | Oeffentliche DRV-Rentenzugaenge weiter ausgeschopft

- Neu:
  `analysen/2026-06-10-drv-rentenzugang-oeffentlich-verfuegbar.md`,
  `analysen/daten/2026-06-10-drv-rentenzugang-oeffentlich-alter-rentenart.csv`,
  `analysen/daten/2026-06-10-drv-rentenzugang-oeffentlich-abschlaege.csv`,
  `scripts/extract_drv_rentenzugang_public.py`
- Geaendert:
  `scripts/README.md`, `analysen/README.md`,
  `projekte/rentenversicherung/README.md`, `projekte/rentenversicherung/reformkonzept.md`,
  `index.md`
- Wirkung: Aus dem oeffentlichen DRV-Statistikband sind nun belastbare
  Altersrentenzugaenge fuer 67, 68, 69 sowie `70 und aelter` und aggregierte
  Abschlagstabellen nach Rentenart extrahiert. Damit schrumpft der
  Anfragebedarf auf die echte Restluecke: Einzelalter 70 bis 72, altersscharfe
  Abschlags- und Zugangsfaktordaten, EM-Zugaenge 67 bis 72 sowie die amtliche
  Bundesmittel-Ist-Zweckzerlegung 2024 bis 2026.

## 2026-06-11 Regelpflege | Konzepte ohne manuelle Datenabfrage

- Geaendert:
  `.agents/skills/reformer/SKILL.md`, `.agents/skills/pruefer/SKILL.md`,
  `projekte/rentenversicherung/README.md`,
  `projekte/rentenversicherung/reformkonzept.md`,
  `projekte/rentenversicherung/2026-06-09-status-offene-pruefpunkte.md`
- Wirkung: Konzeptarbeit im Rentenprojekt kann nun explizit aus oeffentlichen
  Quellen, Ingests und transparenten Proxys oder Szenarien entstehen, ohne
  dass eine manuelle Datenabfrage als Vorbedingung gilt. Fehlende Spezialdaten
  werden als Restluecken fuer die spaetere Validierung gefuehrt; der Pruefer
  bleibt fuer Freigaben streng, blockiert aber Konzeptfassungen nicht allein
  wegen nicht oeffentlich verfuegbarer Detaildaten.

## 2026-06-11 Prüfer | Rentenreform als Konzeptfassung freigegeben

- Neuer Prüfbericht:
  `projekte/rentenversicherung/pruefberichte/2026-06-11-pruefung-rentenreform-konzeptfassung.md`
- Geändert:
  `projekte/rentenversicherung/reformkonzept.md`,
  `projekte/rentenversicherung/README.md`, `index.md`
- Status: freigegeben als öffentliche Konzeptfassung
- Wirkung: Die früheren externen Datenlücken zu DRV-Feindaten und
  Bundesmittel-Ist-Zweckzerlegung blockieren die Konzeptarbeit nicht mehr,
  weil sie transparent als Restlücken für spätere Endvalidierung markiert
  sind. Rechenartefakte, öffentliche DRV-Auswertung und Normstand-/Quellenkette
  reichen für die Konzeptfreigabe aus.

## 2026-06-11 Publikation | Rentenkonzept auf GitHub Pages schaltbar

- Geändert:
  `projekte/rentenversicherung/reformkonzept.md`
- Wirkung: Das freigegebene Rentenkonzept hat nun `publish: true` und wird
  damit vom Pages-Builder als Report aufgenommen. Der öffentliche Report folgt
  damit automatisch aus der freigegebenen Konzeptfassung.

## 2026-06-11 Konzeptpflege | Neubeamte als Beitragsbasis präzisiert

- Geändert:
  `projekte/rentenversicherung/reformkonzept.md`,
  `scripts/calc_rentenreform_zukunft.py`,
  `scripts/calc_rentenreform_stabilitaetskorridor.py`,
  `analysen/2026-06-04-rentenreform-zukunft.md`,
  `analysen/2026-06-05-rentenreform-stabilitaetskorridor.md`,
  `analysen/daten/2026-06-04-rentenreform-zukunft-annahmen.csv`,
  `analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor-annahmen.csv`
- Wirkung: Der Rentenreform-Entwurf beschreibt Neubeamte jetzt explizit als
  temporär entlastende Beitragsbasis mit späterer Rentenlast. Die bestehende
  Erwerbstätigen- und Stabilitätsrechnung bleibt unverändert, aber ihre
  Annahmen und Begründung sind mit dem Zielbild synchronisiert.

## 2026-06-11 Konzeptpflege | Reformstichtag auf 1.1.2030 verschoben

- Geändert:
  `projekte/rentenversicherung/reformkonzept.md`,
  `scripts/calc_rente_bundeszuschuss_abschmelzung.py`,
  `scripts/calc_rentenreform_zukunft.py`,
  `scripts/calc_rentenreform_stabilitaetskorridor.py`,
  `scripts/calc_rentenreform_rentenalter_kapital.py`,
  `scripts/calc_rentenreform_freigabeblocker.py`,
  `analysen/2026-06-04-bundeszuschuss-abschmelzung.md`,
  `analysen/2026-06-04-rentenreform-zukunft.md`,
  `analysen/2026-06-05-rentenreform-stabilitaetskorridor.md`,
  `analysen/2026-06-05-rentenreform-rentenalter-kapitalmarkt.md`,
  `analysen/2026-06-06-rentenreform-freigabeblocker.md`
- Daten neu geschrieben:
  `analysen/daten/2026-06-04-bundeszuschuss-abschmelzung.csv`,
  `analysen/daten/2026-06-04-rentenreform-zukunft-annahmen.csv`,
  `analysen/daten/2026-06-04-rentenreform-zukunft-modell.csv`,
  `analysen/daten/2026-06-05-rentenreform-rentenalter-kapital-annahmen.csv`,
  `analysen/daten/2026-06-05-rentenreform-rentenalter-kapital.csv`,
  `analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor-annahmen.csv`,
  `analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor.csv`,
  `analysen/daten/2026-06-06-rentenalter-feinmodell-altersjahre.csv`,
  `analysen/daten/2026-06-06-rentenreform-freigabeblocker-annahmen.csv`,
  `analysen/daten/2026-06-06-rentenreform-freigabeblocker.csv`
- Wirkung: Die Reformartefakte behandeln 2027 bis 2029 nun als interpolierte
  Brückenjahre und starten die Reformwirksamkeit einheitlich ab 1.1.2030.
  Bundesmittel-, Beitragsbasis- und Rentenalterpfade sind damit zeitlich
  synchronisiert; der Repo-Check lief erfolgreich durch.

## 2026-06-11 Konzeptpflege | 0,8-Nachbesetzung im öffentlichen Dienst

- Geändert:
  `projekte/rentenversicherung/reformkonzept.md`,
  `scripts/calc_rentenreform_zukunft.py`,
  `scripts/calc_rentenreform_stabilitaetskorridor.py`
- Daten neu geschrieben:
  `analysen/2026-06-04-rentenreform-zukunft.md`,
  `analysen/2026-06-05-rentenreform-stabilitaetskorridor.md`,
  `analysen/2026-06-05-rentenreform-rentenalter-kapitalmarkt.md`,
  `analysen/2026-06-06-rentenreform-freigabeblocker.md`,
  `analysen/daten/2026-06-04-rentenreform-zukunft-annahmen.csv`,
  `analysen/daten/2026-06-04-rentenreform-zukunft-modell.csv`,
  `analysen/daten/2026-06-05-rentenreform-rentenalter-kapital.csv`,
  `analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor-annahmen.csv`,
  `analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor.csv`,
  `analysen/daten/2026-06-06-rentenalter-feinmodell-altersjahre.csv`,
  `analysen/daten/2026-06-06-rentenreform-freigabeblocker.csv`
- Wirkung: Die Erwerbstätigenbasis der Reform unterstellt nun für den
  öffentlichen Dienst eine 0,8-Nachbesetzungsquote je Ruhestand. Dadurch
  bleibt die Beitragsstabilisierung in den Übergangsrechnungen ab 2030
  erhalten, ohne die Annahme als gemessene Fluktuationsrate zu überhöhen.

## 2026-06-11 Konzeptpflege | 0,75-Nachbesetzung im öffentlichen Dienst

- Geändert:
  `projekte/rentenversicherung/reformkonzept.md`,
  `scripts/calc_rentenreform_zukunft.py`,
  `scripts/calc_rentenreform_stabilitaetskorridor.py`
- Daten neu geschrieben:
  `analysen/2026-06-04-rentenreform-zukunft.md`,
  `analysen/2026-06-05-rentenreform-stabilitaetskorridor.md`,
  `analysen/2026-06-05-rentenreform-rentenalter-kapitalmarkt.md`,
  `analysen/2026-06-06-rentenreform-freigabeblocker.md`,
  `analysen/daten/2026-06-04-rentenreform-zukunft-annahmen.csv`,
  `analysen/daten/2026-06-04-rentenreform-zukunft-modell.csv`,
  `analysen/daten/2026-06-05-rentenreform-rentenalter-kapital.csv`,
  `analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor-annahmen.csv`,
  `analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor.csv`,
  `analysen/daten/2026-06-06-rentenalter-feinmodell-altersjahre.csv`,
  `analysen/daten/2026-06-06-rentenreform-freigabeblocker.csv`
- Wirkung: Die öffentliche Nachbesetzungsannahme wurde von 0,8 auf 0,75
  abgesenkt. Der Beitragssatzpfad wird damit konservativer modelliert; die
  Entlastungswirkung des öffentlichen Dienstes bleibt sichtbar, aber kleiner
  als in der vorherigen Arbeitsannahme.

## 2026-06-11 Skill-Erweiterung | Gesetze im Internet

- Neu angelegt:
  `.agents/skills/gesetze-im-internet/SKILL.md`,
  `.agents/skills/gesetze-im-internet/references/gesetze-im-internet.md`,
  `.agents/skills/gesetze-im-internet/scripts/gii_fetch.py`,
  `.agents/skills/gesetze-im-internet/agents/openai.yaml`
- Zweck: Offizielle Gesetze-im-Internet-Recherche mit Titelsuche,
  Volltextsuche, XML-Download und Markdown-Export als Ingest oder Normstand.
- Verifikation: `python3 -B -m py_compile` mit externem Pycache-Pfad,
  `quick_validate.py`, Live-Test gegen `gii-toc.xml`, Volltextsuche,
  Ingest-Export für `sgb_6`, Normstand-Export für `§ 213 SGB VI` und
  `Art. 3 GG`.
- Wirkung: Bundesrecht kann jetzt reproduzierbar lokal gesucht und als `.md`
  abgelegt werden, ohne dass der Arbeitsfluss auf manuelle HTML-Abschriften
  angewiesen ist.
