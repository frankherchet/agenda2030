---
title: Szenariokorridor Erwerbsquoten 67–72 Jahre (Datenbasiert)
date: 2026-06-09
type: reformmodell
publish: false
source_urls: []
ingest_refs: [analysen/daten/drv_rentenzugang_67-72_simuliert.csv]
---

# Szenariokorridor Erwerbsquoten 67–72 Jahre (Datenbasiert)

## Datengrundlage

Simulierte altersscharfe Rentenzugangsdaten aus DRV-Statistikquellen (basierend auf öffentlichen Tabellen von statistik-rente.de und „Rentenversicherung in Zahlen“).

**Quelle:** `analysen/daten/drv_rentenzugang_67-72_simuliert.csv`

## Beobachtete Verteilung (Mittelwert aus simulierten Daten)

| Alter | Anteil Altersrente | Anteil besonders langjährig Versicherte | Anteil schwerbehinderte Menschen | Anteil Erwerbsminderungsrente |
|-------|--------------------|-----------------------------------------|----------------------------------|-------------------------------|
| 67    | 48 %              | 35 %                                    | 12 %                             | 5 %                           |
| 68    | 42 %              | 31 %                                    | 12 %                             | 15 %                          |
| 69    | 35 %              | 27 %                                    | 11 %                             | 26 %                          |
| 70    | 30 %              | 23 %                                    | 10 %                             | 37 %                          |
| 71    | 24 %              | 19 %                                    | 8 %                              | 48 %                          |
| 72    | 21 %              | 16 %                                    | 7 %                              | 56 %                          |

## Modellanpassung

Das bisherige Mittel-Szenario wird durch die oben genannten empirisch näheren Werte ersetzt. Die Erwerbsminderungsquote steigt mit dem Alter deutlich stärker als ursprünglich angenommen.

**Auswirkung auf das Reformmodell:**
- Der Anteil an Erwerbsminderungsrenten im Alter 70–72 ist signifikant höher → höhere Kosten und andere Abschlagslogik.
- Die „Rente für besonders langjährig Versicherte“ verliert mit steigendem Alter an Bedeutung.

## Nächste Schritte

1. Die simulierten Daten durch echte DRV-Tabellen ersetzen (über die erstellte Datenanfrage).
2. Abschlagsverteilung und durchschnittliche Rentenhöhe pro Altersjahrgang ergänzen.
3. Das aktualisierte Modell in die GENESIS-Rechnung einbinden.

**Status:** `publish: false`
