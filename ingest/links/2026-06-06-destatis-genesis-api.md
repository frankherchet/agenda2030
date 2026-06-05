---
title: Destatis GENESIS-Online API
date: 2026-06-06
type: ingest
status: geprüft
source_urls:
  - https://genesis.destatis.de/genesisWS/swagger-ui/index.html
  - https://www.destatis.de/DE/Service/OpenData/genesis-api-webservice-oberflaeche.html
  - https://www.destatis.de/DE/Home/_neue_startseite/_documents/_aktuelles/text-genesis-meldung.html
---

# Ingest: Destatis GENESIS-Online API

## Metadaten

- Typ: Link
- Datum: 2026-06-06
- Quelle: https://genesis.destatis.de/genesisWS/swagger-ui/index.html
- Status: geprüft
- Index: `ingest/index/README.md`

## Kurzfassung

Destatis stellt für GENESIS-Online eine RESTful/JSON-Webservice-Schnittstelle
bereit. Die Schnittstelle kann Tabellen, Kataloge, Metadaten und Ergebnisdaten
aus GENESIS-Online automatisiert abrufen. Seit dem 15. Juli 2025 sind für die
Webservice-Schnittstelle POST-Methoden der RESTful/JSON-Schnittstelle relevant.
Für repo-interne Nutzung müssen Zugangsdaten über Umgebungsvariablen oder Token
bereitgestellt werden; Zugangsdaten dürfen nicht im Repo gespeichert werden.

## Kernaussagen

- GENESIS-Online ist die Destatis-Datenbank für konfigurierbare amtliche
  Tabellen.
- Die Webservice-Schnittstelle unterstützt automatisierten Zugriff auf Kataloge,
  Metadaten und Daten.
- Die Nutzung ist grundsätzlich kostenfrei; für API-Zugriffe können
  registrierte Zugangsdaten oder Token erforderlich sein.
- Neue Skripte sollen POST/RESTful JSON statt alter GET-/SOAP-Muster nutzen.

## Enthaltene Informationen

- Swagger UI für die GENESIS-Server RESTful/JSON-API.
- Destatis-Open-Data-Seite zu API/Webservice und Weboberfläche.
- Destatis-Hinweis zur Umstellung der Webservice-Schnittstelle auf POST-Methoden.
- Relevante Methodenbereiche: Katalog, Daten, Metadaten, Suche und Logincheck.

## Jetzt extrahierte relevante Informationen

- Base/API-Kontext: GENESIS-Online Webservice `genesisWS`.
- Geeignet für Rentenprojekt-Dateninputs wie Bevölkerung nach Alter,
  Bevölkerungsfortschreibung, Bevölkerungsvorausberechnung und
  Erwerbs-/Arbeitsmarktdaten, soweit GENESIS passende Tabellen enthält.
- Für DRV-spezifische Rentenzugänge, Abschläge und Erwerbsminderung bleibt
  GENESIS nicht ausreichend; dafür sind DRV-/Statistik-Rente-Quellen nötig.
- Zugangsdaten dürfen nur als `DESTATIS_USER`, `DESTATIS_PASSWORD` oder
  `DESTATIS_TOKEN` genutzt werden.

## Relevanz für agenda2030

Die API kann den Prüferblocker zu synthetischen Alterskohorten entschärfen,
indem amtliche Destatis-Daten reproduzierbar aus GENESIS-Online gezogen und als
CSV/JSON-Artefakte im Repo abgelegt werden.

## Zuordnung

- Ministerien: `ministerien/arbeit-soziales/`, `ministerien/finanzen/`
- Gesetze/Gesetzbücher: keine direkte Norm
- Bundestagsdrucksachen: keine
- Themen: Destatis, GENESIS, API, Demographie, Erwerbstätigkeit, Rente

## Verknüpfte Wissensseiten

- `projekte/rentenversicherung/reformkonzept.md`
- `projekte/rentenversicherung/pruefberichte/2026-06-06-zweitnachpruefung-reformkonzept.md`
- `.agents/skills/destatis-genesis/SKILL.md`

## Mögliche Updates

- Skill `destatis-genesis` für reproduzierbare Destatis-Abfragen nutzen.
- Rentenaltermodell von synthetischen Kohorten auf amtliche GENESIS-Daten
  umstellen, soweit passende Tabellen verfügbar sind.

## Widersprüche/Risiken

- Destatis beschreibt GENESIS-Online grundsätzlich als kostenfrei und ohne
  Registrierung nutzbar; praktische API-Nutzung kann dennoch Zugangsdaten oder
  Token benötigen.
- Die API liefert nicht automatisch alle für das Rentenprojekt nötigen
  DRV-Fachdaten.
- Tabellen- und Methodenparameter müssen pro Abruf dokumentiert werden, damit
  spätere Analysen reproduzierbar bleiben.

## Offene Fragen

- Welche konkreten GENESIS-Tabellen liefern feinjährige Bevölkerung und
  altersspezifische Erwerbsquoten für das Rentenaltermodell?
- Ob Token-Authentifizierung für den lokalen Account stabiler ist als
  Benutzername/Passwort.

## Nächste Schritte

- Skill `destatis-genesis` anlegen.
- Fetch-Skript mit ENV-basierter Authentifizierung bereitstellen.
- Erste Katalogsuche nach Rentenmodell-relevanten Tabellen ausführen, sobald
  Zugangsdaten lokal gesetzt sind.
