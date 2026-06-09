---
name: dip-bundestag
description: Nutzt die DIP-Bundestag-API (über bundesAPI/dip-bundestag-api oder direkt) für reproduzierbare Abruf von Bundestagsdrucksachen, Vorgängen, Plenarprotokollen, Metadaten und Volltexten im agenda2030-Repo. Integriert mit Ingest- und Drucksachen-Vorlagen. Use when the user asks to use DIP, Bundestag API, dip.bundestag.de, Drucksachen abrufen, Bundestag-Dokumente importieren, Plenarprotokolle fetchen, or fetch parliamentary documents, drucksachen, vorgänge for analyses, reform models or ingest.
---

# DIP Bundestag

## Overview

Rufe amtliche Bundestagsdokumente über die DIP-API (Dokumentations- und Informationssystem für Parlamentsmaterialien) reproduzierbar ab und bereite sie für Ingests, Analysen oder Prüfberichte vor. Die API liefert strukturierte Metadaten, Fundstellen, PDFs und teilweise Volltexte. Zugangsdaten (API-Key) werden nie gespeichert oder committet.

Die offizielle API-Basis ist `https://search.dip.bundestag.de/api/v1`. Der bundesAPI-Client vereinfacht Authentifizierung und Pagination.

## Secrets

- Niemals API-Key in Dateien, Commits, Logs oder Antworten schreiben.
- Nutze lokale Umgebungsvariable:
  - `DIP_API_KEY`
- Wenn der Key fehlt, Skript/Anleitung vorbereiten und den User bitten, die ENV-Variable lokal zu setzen (z. B. in `.env` oder Shell-Profil).
- Der Client liest den Key automatisch aus der Umgebung.

## Quellenpflicht

Vor fachlicher Nutzung eines API-Ergebnisses:

1. API-Quelle als Ingest referenzieren (falls nicht schon vorhanden):
   z. B. `ingest/links/2026-06-09-dip-bundestag-api.md`
2. Rohantwort oder strukturierte Ausgabe versionierbar ablegen:
   - kleine JSON: `ingest/originale/` oder `analysen/daten/`
   - Drucksachen: nach erfolgreichem Fetch Ingest unter `ingest/dokumente/` mit Vorlage `vorlagen/drucksache-zusammenfassung.md` anlegen.
3. Analyse-/Projektdateien führen `source_urls` und `ingest_refs`.
4. Dokumentnummer (z. B. BT-21-1419), Wahlperiode, Typ, Abrufdatum und API-Parameter dokumentieren.

## Workflow

1. Kläre Zweck: Suche nach Drucksachen/Vorgängen, Metadatenabruf, Volltext oder PDF-Link für Ingest.
2. Suche zuerst über API (z. B. nach Titel, Aktenzeichen, Datum, Typ).
3. Prüfe Metadaten: Titel, Urheber, Datum, Fundstelle, PDF-URL, Vorgangsbezug.
4. Rufe bei Bedarf Detail- oder Volltext-Endpunkt mit dokumentierten Parametern ab.
5. Speichere Ergebnis als JSON unter `analysen/daten/` oder `ingest/originale/`.
6. Für Bundestagsdrucksachen: Ingest-Datei mit `vorlagen/drucksache-zusammenfassung.md` erstellen und in `ingest/index/README.md` eintragen.
7. `log.md` append-only ergänzen.
8. Bei Modellnutzung klar trennen: DIP liefert offizielle Drucksachen und Protokolle; eigene Berechnungen bleiben in Skripten unter `scripts/`.

## Helper Script

Nutze bei API-Arbeiten bevorzugt:

```text
.agents/skills/dip-bundestag/scripts/dip_fetch.py
```

Typische Aufrufe (Beispiel, nach Implementierung):

```bash
python3 .agents/skills/dip-bundestag/scripts/dip_fetch.py search --term "Rentenreform" --type Drucksache --wahlperiode 21 --limit 20
python3 .agents/skills/dip-bundestag/scripts/dip_fetch.py document --id "21/1419" --output ingest/originale/2026-06-09-bt-21-1419.json
python3 .agents/skills/dip-bundestag/scripts/dip_fetch.py vorgang --id "..." 
```

Das Skript liest `DIP_API_KEY` aus der Umgebung und sendet Requests an die DIP-API. Parameter mit `--param` ergänzen. Pagination und Rate-Limits beachten.

## API Reference

Die offizielle Dokumentation und Swagger/OpenAPI-Spezifikation liegt nicht direkt im Skill. Bei Bedarf kompakte Referenz unter:

```text
.agents/skills/dip-bundestag/references/api.md
```

Diese enthält extrahierte Endpunkte wie `/document`, `/vorgang`, `/plenarprotokoll`, Suchparameter und Authentifizierungsbeispiele.

## Betriebsgrenzen

- Die DIP-API hat Rate-Limits (üblicherweise 100 Requests/Minute oder ähnlich; bei Überschreitung HTTP 429).
- Bei Fehlern zuerst Key prüfen und `logincheck`-äquivalent (einfache Suche) ausführen.
- Große Suchen oder Bulk-Abrufe sequenziell oder mit Delay ausführen; keine massiven parallelen Abfragen starten.
- PDFs werden nicht von der API selbst geliefert, sondern über separate `dserver.bundestag.de`-Links; diese separat mit `fetch` oder Ingest-Workflow herunterladen.

## Output Standard

Nach einem Abruf knapp melden:

- genutzte Methode/Endpunkt und Suchkriterien,
- Ausgabe-Datei,
- Ingest-Pfad (falls Drucksache),
- zentrale Parameter (Wahlperiode, Typ, ID),
- ob API-Key fehlte oder der Abruf erfolgreich war,
- nächste Schritte (Ingest, Analyse, Prüfung).