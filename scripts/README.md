# Reproduzierbare Berechnungen

Berechnungen fuer Reformkonzepte und Analysen werden als Skripte abgelegt,
sobald sie ueber einfache Quellenzitate hinausgehen. Analysen und
Projektartefakte sollen die erzeugten Artefakte zitieren, statt Zahlen
ausschliesslich im Fliesstext herzuleiten.

Arbeitsweise:

1. Eingabedaten als CSV, JSON oder Markdown unter `ingest/` oder
   `analysen/daten/` ablegen.
2. Rechenskript unter `scripts/` anlegen.
3. Ergebnisdatei unter `analysen/` oder `analysen/daten/` erzeugen.
4. Analyse oder Projektartefakt auf Eingabedaten, Skript und Ergebnisdatei
   verweisen lassen.

Aktuelle Skripte:

- `build_drv_renten_inputs.py`: erzeugt aus dem DRV-Statistikband 2024 die
  strukturierte Rentenbestands-CSV nach Rentenart, Alter, Geschlecht und
  Träger sowie die Reformklassifikation der Bundesmittel.
- `calc_demographie_rente.py`: erzeugt die demographische Belastungsrechnung
  fuer die Rentenreform aus `analysen/daten/2026-06-04-demographie-kernzahlen-2024-2070.csv`.
- `calc_rente_bundeszuschuss_abschmelzung.py`: erzeugt den Abschmelzpfad des
  Bestandsschutz-Zuschusses proportional zur erwarteten Überlebendenzahl der
  geschützten Bestandsrentner-Kohorte auf Basis des DRV-Rentenbestands.
- `calc_rentenreform_zukunft.py`: erzeugt ein v1-Zukunftsmodell 2027-2070 für
  Status quo, abschmelzende Bundesmittel und erweiterte Erwerbstätigenbasis.
