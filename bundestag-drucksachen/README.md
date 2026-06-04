# Bundestagsdrucksachen

Dieser Bereich dient dazu, aktuelle Drucksachen des Deutschen Bundestages
abzulegen und token-sparend auszuwerten.

## Struktur

- `originale/`: unveränderte Originaldokumente, zum Beispiel PDF-Dateien.
- `zusammenfassungen/`: kurze Markdown-Zusammenfassungen je Drucksache.
- `index/`: Übersichten, Listen und thematische Register.

## Namensschema

Dateien sollten nach Wahlperiode und Drucksachennummer benannt werden:

- Original: `BT-<wahlperiode>-<nummer>.pdf`
- Zusammenfassung: `BT-<wahlperiode>-<nummer>.md`

Beispiel:

- `originale/BT-20-12345.pdf`
- `zusammenfassungen/BT-20-12345.md`

## Arbeitsweise

1. Originaldokument in `originale/` ablegen.
2. Zusammenfassung mit `vorlagen/drucksache-zusammenfassung.md` erstellen.
3. Betroffene Ministerien und Gesetzbücher verlinken.
4. Nur relevante Passagen detailliert auswerten; Volltexte bleiben im Original.

## Ziel der Zusammenfassungen

Die Zusammenfassungen sollen kurz genug sein, um schnell in weiteren
Analyseschritten genutzt zu werden, aber vollständig genug, um politische,
rechtliche und finanzielle Relevanz einschätzen zu können.
