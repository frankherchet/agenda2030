---
title: Bundeshaushalt <Jahr>
date: <YYYY-MM-DD>
type: bundeshaushalt
publish: false
tags: []
source_urls: []
ingest_refs: []
related_ministries: []
related_laws: []
---

# Bundeshaushalt <Jahr>

## Metadaten

- Haushaltsjahr: <Jahr>
- Stand: <Soll | Ist | unterjährige Ist-Entwicklung>
- Stichtag: <Datum>
- Quelle: <URL oder Datei>

## Kurzfassung

<Maximal 5 Sätze.>

## Kernzahlen

- Ausgaben: <Betrag>
- Einnahmen ohne Nettokreditaufnahme: <Betrag>
- Steuereinnahmen: <Betrag>
- Nettokreditaufnahme: <Betrag>
- Finanzierungssaldo: <Betrag>

## Einnahmen

- <Einnahmeart>: <Betrag>

## Ausgaben

- <Aufgabenbereich oder Ausgabeart>: <Betrag>

## Sankey-Diagramm

Optional kann ein Sankey-Diagramm als JSON-Datenblock gepflegt werden. Werte
sind in der im Feld `unit` genannten Einheit anzugeben.

```json sankey
{
  "title": "<Titel>",
  "unit": "Mrd. Euro",
  "centerLabel": "Bundeshaushalt <Jahr>",
  "note": "<Einordnung der Darstellung>",
  "income": [
    { "label": "<Einnahmequelle>", "value": 0 }
  ],
  "spending": [
    { "label": "<Ausgabenbereich>", "value": 0 }
  ]
}
```

## Relevanz für agenda2030

<Welche Reformfragen ergeben sich daraus?>

## Zuordnung

- Ministerien: <Pfade in `ministerien/`>
- Gesetze/Gesetzbücher: <Pfade in `gesetzbuecher/`>
- Themen: <Schlagworte>

## Offene Fragen

- <Frage 1>

## Nächste Schritte

- <konkreter nächster Schritt>
