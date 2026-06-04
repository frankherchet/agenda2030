# Demographie

Dieser Bereich sammelt demographische Grundlagen für Reformvorhaben. Die Daten
sind besonders relevant für Rentenversicherung, gesetzliche Krankenversicherung,
Pflege, Arbeitsmarkt, Bildung, Wohnungsbau und öffentliche Finanzen.

## Struktur

- `quellen/`: zitierfähige Quellenkataloge und kompakte Einordnungen.
- `daten/`: strukturierte Kernzahlen, bevorzugt CSV.
- `zusammenfassungen/`: thematische Auswertungen für Reformbereiche.
- `originale/`: abgelegte Originaldokumente, falls notwendig.
- `index/`: Übersichten nach Thema, Jahr, Quelle oder Reformbezug.

## Arbeitsweise

1. Amtliche Quellen bevorzugen, insbesondere Destatis.
2. Bestandszahlen und Vorausberechnungen strikt trennen.
3. Varianten der Bevölkerungsvorausberechnung immer benennen.
4. Fehlende Werte leer lassen, nicht schätzen.
5. Reformreports sollen diese Demographiequellen zitieren, damit Rente und GKV
   mit denselben Annahmen arbeiten.

## Namensschema

- Quelle: `quellen/YYYY-MM-DD-<quelle>-<thema>.md`
- Datensatz: `daten/YYYY-MM-DD-<thema>.csv`
- Zusammenfassung: `zusammenfassungen/YYYY-MM-DD-<thema>.md`
