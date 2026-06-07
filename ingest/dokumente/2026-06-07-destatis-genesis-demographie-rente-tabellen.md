---
title: Destatis GENESIS Tabellen Demographie und Rente
date: 2026-06-07
type: ingest
status: erfasst
source_urls:
  - https://genesis.destatis.de/genesisWS/swagger-ui/index.html
  - https://genesis.destatis.de/genesisWS/rest/2020/GOJsonApi.json
ingest_refs:
  - ingest/links/2026-06-06-destatis-genesis-api.md
original_refs:
  - ingest/originale/2026-06-07-genesis-12411-0005-bevoelkerung-altersjahre.json
  - ingest/originale/2026-06-07-genesis-12421-0002-bev-v02-moderat.json
  - ingest/originale/2026-06-07-genesis-12421-0002-bev-v04-alt.json
  - ingest/originale/2026-06-07-genesis-12421-0002-bev-v05-jung.json
  - ingest/originale/2026-06-07-genesis-12211-0002-mikrozensus-erwerbsstatus.json
  - ingest/originale/2026-06-07-genesis-12211-0004-erwerbstaetige-altersgruppen.json
  - ingest/originale/2026-06-07-genesis-values-bevpr1-varianten.json
---

# Ingest: Destatis GENESIS Tabellen Demographie und Rente

## Metadaten

- Typ: Dokument/API-Abruf
- Datum: 2026-06-07
- Quelle: GENESIS-Online RESTful/JSON-API
- Status: erfasst
- Index: `ingest/index/README.md`

## Kurzfassung

Die GENESIS-API wurde genutzt, um reproduzierbare amtliche Datengrundlagen für
das Rentenaltermodell zu beschaffen. Der Schwerpunkt liegt auf
Altersjahrgängen der Bevölkerung, Bevölkerungsvorausberechnungen bis 2070 und
Mikrozensus-Erwerbsstatusdaten.

## Enthaltene Informationen

- `12411-0005`: Bevölkerungsstand Deutschland nach Stichtag und Altersjahren
  bis 31.12.2024.
- `12421-0002`: vorausberechneter Bevölkerungsstand Deutschland nach
  Stichtag, Varianten der Bevölkerungsvorausberechnung, Geschlecht und
  Altersjahren bis 31.12.2070.
- `BEVPR1`: Varianten der Bevölkerungsvorausberechnung, darunter
  `BEV-VARIANTE-02` moderat, `BEV-VARIANTE-04` relativ alte Bevölkerung und
  `BEV-VARIANTE-05` relativ junge Bevölkerung.
- `12211-0002`: Mikrozensus 2025 mit Bevölkerung, Erwerbstätigen,
  Erwerbslosen, Erwerbspersonen und Nichterwerbspersonen nach überwiegendem
  Lebensunterhalt und Altersgruppen.
- `12211-0004`: Mikrozensus 2025 mit Erwerbstätigen nach Geschlecht,
  Altersgruppen und Stellung im Beruf, darunter `65 bis unter 75 Jahre`.

## Jetzt extrahierte relevante Informationen

- Für die Rentenalterrechnung können die Altersjahre 67 bis 72 aus
  GENESIS-Altersjahrgängen statt aus einer pauschalen synthetischen Kohorte
  gebildet werden.
- Für 2025 weist der Mikrozensus bei `65 Jahre und mehr` eine
  Erwerbstätigenquote von rund 10,2 % und eine Erwerbspersonenquote von rund
  10,4 % aus.
- Für 2025 weist `12211-0004` in der näheren Gruppe `65 bis unter 75 Jahre`
  1,650 Mio. Erwerbstätige aus; das Rechenartefakt spiegelt diesen Wert gegen
  die GENESIS-Bevölkerung 65 bis 74.
- `12421-0002` enthält die Geschlechtsdimension `männlich`, `weiblich` und
  `Insgesamt`. Für Summen darf nur `Insgesamt` verwendet werden; die
  Rechenfassung vom 2026-06-07 korrigiert diese Doppelzählungsgefahr.
- Öffentliche GENESIS-Suche/Katalogdaten lieferten keine feinjährigen
  Erwerbsquoten für 67 bis 72. Diese Lücke bleibt als Datenbedarf für
  Sonderauswertung, DRV-Daten oder andere amtliche Quelle bestehen.
- GENESIS-Fehlercode `6` trat bei mehr als drei parallelen Requests auf; für
  Batch-Arbeiten sind sequenzielle Abrufe oder `logincheck` vor Fortsetzung
  erforderlich.

## Relevanz für agenda2030

Dieser Ingest bearbeitet den Prüferpunkt zum synthetischen Rentenaltermodell.
Er löst die Bevölkerungsseite mit amtlichen Altersjahrgängen, ersetzt aber
nicht DRV-spezifische Rentenzugangs-, Abschlags- und Erwerbsminderungsdaten.

## Zuordnung

- Projekt: `projekte/rentenversicherung/reformkonzept.md`
- Analyse: `analysen/2026-06-07-rentenalter-genesis-empirisch.md`
- Themen: Rente, Demographie, GENESIS, Rentenalter, Erwerbstätigkeit

## Verknüpfte Wissensseiten

- `analysen/2026-06-07-rentenalter-genesis-empirisch.md`
- `analysen/2026-06-06-rentenreform-freigabeblocker.md`
- `projekte/rentenversicherung/reformkonzept.md`
- `.agents/skills/destatis-genesis/SKILL.md`

## Mögliche Updates

- Rentenaltermodell im Reformkonzept auf die neuen GENESIS-Artefakte
  umstellen.
- Prüferbericht nach Aktualisierung erneut anstoßen.
- `destatis-genesis`-Skill um Fehlercode `6` und sequenzielle Batch-Regel
  ergänzen.

## Widersprüche/Risiken

- Die Altersjahrgänge sind amtlich und feinjährig. Die Erwerbsquote ist nur
  altersgruppenbasiert (`65 bis unter 75 Jahre`) und deshalb weiterhin eine
  Brückenannahme.
- GENESIS-Daten ersetzen keine DRV-Rentenzugangsdaten zu Abschlägen,
  Erwerbsminderung, Schwerbehinderung oder besonders langjährig Versicherten.

## Offene Fragen

- Gibt es öffentlich abrufbare Mikrozensus- oder Arbeitsmarkt-Tabellen mit
  Erwerbsbeteiligung exakt für 67, 68, 69, 70, 71 und 72 Jahre?
- Können DRV oder Destatis hierfür eine Sonderauswertung liefern?
