# Analysen

Dieser Ordner enthält zweckgebundene Auswertungen, Rechenberichte und
Datenartefakte. Eine Analyse wird nur angelegt, wenn sie eine konkrete Frage
beantwortet oder ein Projekt belastbar vorbereitet.

## Regeln

- Jede Analyse nennt ihren Zweck.
- Externe Quellen werden über `ingest_refs` oder repo-relative Ingest-Pfade
  referenziert.
- Rechtsanalysen verweisen auf vorher abgelegte Normstände unter
  `gesetzbuecher/`.
- Reproduzierbare Rechnungen verweisen auf Skripte unter `scripts/` und
  erzeugte Dateien unter `analysen/daten/`.

## Daten

`analysen/daten/` enthält CSV- oder JSON-Artefakte, die von Skripten erzeugt
oder für Analysen als strukturierter Input genutzt werden.

## Diagramme

`analysen/diagramme/` enthält reproduzierbar erzeugte SVG-Grafiken, die von
Analysen referenziert werden.

## Übersicht

- `2026-06-04-drv-rentenbestand-inputs.md`: DRV-Rentenbestandsstruktur und
  Bundesmittel-Klassifikation als Modellinput.
- `2026-06-04-rente-belastungsrechnung.md`: demographische
  Belastungskennzahlen für Rentenmodelle.
- `2026-06-04-demographie-rente-gkv.md`: gemeinsame Demographie-Basis für
  Rente und GKV.
- `2026-06-04-bundeszuschuss-abschmelzung.md`: Abschmelzpfad des
  Bestandsschutz-Zuschusses.
- `2026-06-04-rentenreform-zukunft.md`: Zukunftsmodell 2027 bis 2070.
- `2026-06-05-strukturumbau-quellen-analysen-projekte-pruefung.md`:
  Prüfung des Strukturumbaus und offener Nachpflegebedarf.
- `2026-06-05-bundesmittel-zweckzerlegung-rente.md`: Einordnung der
  beschafften Quellen zu Bundeszuschüssen und nicht beitragsgedeckten
  Leistungen.
- `2026-06-05-rentenproblem-deutschland-ursachen-auswirkungen.md`:
  Quellenbasierter Problemaufriss zu Ursachen und Folgen steigender
  Rentenbelastung ohne Gegenmaßnahmen, inklusive Hochrechnung der
  Finanzierungslücke bei fixem Beitragssatz und unveränderter Altersgrenze.
- `2026-06-05-rentenreform-stabilitaetskorridor.md`: Hochrechnung des maximal
  finanzierbaren Rentenvolumens bei Beitragssatz-Korridoren von 20 %, 22 %
  und 24 %.
- `2026-06-05-rentenreform-rentenalter-kapitalmarkt.md`: Szenarioanalyse zur
  Kopplung des Renteneintrittsalters an die Lebenserwartung und zu einem
  zusaetzlichen kapitalgedeckten Baustein.
- `2026-06-06-rentenreform-freigabeblocker.md`: Nachbesserung der
  Prüferblocker mit Rentenwert-Budgetformel, feinerem Altersjahrmodell und
  quantifizierten echten öffentlichen Beitragszahlungen.
