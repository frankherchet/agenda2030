# Reproduzierbare Berechnungen

Berechnungen fuer Reformberichte werden als Skripte abgelegt, sobald sie ueber
einfache Quellenzitate hinausgehen. Reports sollen die erzeugten Artefakte
zitieren, statt Zahlen ausschliesslich im Fliesstext herzuleiten.

Arbeitsweise:

1. Eingabedaten als CSV, JSON oder Markdown im passenden Fachordner ablegen.
2. Rechenskript unter `scripts/` anlegen.
3. Ergebnisdatei im passenden Fachordner unter `auswertungen/` erzeugen.
4. Report auf Eingabedaten, Skript und Ergebnisdatei verweisen lassen.

Aktuelle Skripte:

- `build_drv_renten_inputs.py`: erzeugt aus dem DRV-Statistikband 2024 die
  strukturierte Rentenbestands-CSV nach Rentenart, Alter, Geschlecht und
  Träger sowie die Reformklassifikation der Bundesmittel.
- `calc_demographie_rente.py`: erzeugt die demographische Belastungsrechnung
  fuer die Rentenreform aus `demographie/daten/2026-06-04-demographie-kernzahlen-2024-2070.csv`.
- `calc_rente_bundeszuschuss_abschmelzung.py`: erzeugt den Abschmelzpfad des
  Bestandsschutz-Zuschusses proportional zur erwarteten Überlebendenzahl der
  geschützten Bestandsrentner-Kohorte auf Basis des DRV-Rentenbestands.
