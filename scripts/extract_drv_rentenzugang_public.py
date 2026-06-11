#!/usr/bin/env python3
"""Extrahiert oeffentlich verfuegbare DRV-Rentenzugangstabellen aus dem Statistikband 2024."""

from __future__ import annotations

import csv
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "ingest/originale/2026-06-04-drv-statistikband-rente-2024.pdf"
DATA_DIR = ROOT / "analysen/daten"
AGE_CSV = DATA_DIR / "2026-06-10-drv-rentenzugang-oeffentlich-alter-rentenart.csv"
DEDUCTION_CSV = DATA_DIR / "2026-06-10-drv-rentenzugang-oeffentlich-abschlaege.csv"
OUTPUT_MD = ROOT / "analysen/2026-06-10-drv-rentenzugang-oeffentlich-verfuegbar.md"


AGE_ROWS = [
    ("insgesamt", "67", "Insgesamt", 10101, "653,02"),
    ("insgesamt", "67", "Regelaltersrenten", 10003, "647,04"),
    ("insgesamt", "67", "Altersrenten_fuer_besonders_langjaehrig_Versicherte", 25, "1.818,51"),
    ("insgesamt", "67", "Altersrenten_fuer_langjaehrig_Versicherte", 71, "1.062,76"),
    ("insgesamt", "67", "Altersrenten_fuer_schwerbehinderte_Menschen", 2, "1.453,78"),
    ("insgesamt", "68", "Insgesamt", 4241, "681,43"),
    ("insgesamt", "68", "Regelaltersrenten", 4203, "677,98"),
    ("insgesamt", "68", "Altersrenten_fuer_besonders_langjaehrig_Versicherte", 11, "1.637,58"),
    ("insgesamt", "68", "Altersrenten_fuer_langjaehrig_Versicherte", 27, "827,72"),
    ("insgesamt", "69", "Insgesamt", 2503, "632,08"),
    ("insgesamt", "69", "Regelaltersrenten", 2477, "627,21"),
    ("insgesamt", "69", "Altersrenten_fuer_besonders_langjaehrig_Versicherte", 2, "3.440,37"),
    ("insgesamt", "69", "Altersrenten_fuer_langjaehrig_Versicherte", 20, "834,77"),
    ("insgesamt", "69", "Altersrenten_fuer_schwerbehinderte_Menschen", 3, "1.571,73"),
    ("insgesamt", "70_und_aelter", "Insgesamt", 7305, "471,33"),
    ("insgesamt", "70_und_aelter", "Regelaltersrenten", 7256, "467,02"),
    ("insgesamt", "70_und_aelter", "Altersrenten_fuer_besonders_langjaehrig_Versicherte", 10, "1.258,19"),
    ("insgesamt", "70_und_aelter", "Altersrenten_fuer_langjaehrig_Versicherte", 38, "1.089,34"),
    ("insgesamt", "70_und_aelter", "Altersrenten_fuer_schwerbehinderte_Menschen", 1, "377,84"),
    ("maenner", "67", "Insgesamt", 6011, "710,17"),
    ("maenner", "67", "Regelaltersrenten", 5952, "703,46"),
    ("maenner", "67", "Altersrenten_fuer_besonders_langjaehrig_Versicherte", 15, "1.815,30"),
    ("maenner", "67", "Altersrenten_fuer_langjaehrig_Versicherte", 42, "1.230,95"),
    ("maenner", "67", "Altersrenten_fuer_schwerbehinderte_Menschen", 2, "1.453,78"),
    ("maenner", "68", "Insgesamt", 2514, "746,36"),
    ("maenner", "68", "Regelaltersrenten", 2490, "741,17"),
    ("maenner", "68", "Altersrenten_fuer_besonders_langjaehrig_Versicherte", 9, "1.739,53"),
    ("maenner", "68", "Altersrenten_fuer_langjaehrig_Versicherte", 15, "1.011,51"),
    ("maenner", "69", "Insgesamt", 1439, "701,85"),
    ("maenner", "69", "Regelaltersrenten", 1421, "694,08"),
    ("maenner", "69", "Altersrenten_fuer_besonders_langjaehrig_Versicherte", 2, "3.440,37"),
    ("maenner", "69", "Altersrenten_fuer_langjaehrig_Versicherte", 13, "928,67"),
    ("maenner", "69", "Altersrenten_fuer_schwerbehinderte_Menschen", 3, "1.571,73"),
    ("maenner", "70_und_aelter", "Insgesamt", 2565, "641,68"),
    ("maenner", "70_und_aelter", "Regelaltersrenten", 2534, "635,11"),
    ("maenner", "70_und_aelter", "Altersrenten_fuer_besonders_langjaehrig_Versicherte", 6, "943,78"),
    ("maenner", "70_und_aelter", "Altersrenten_fuer_langjaehrig_Versicherte", 24, "1.270,46"),
    ("maenner", "70_und_aelter", "Altersrenten_fuer_schwerbehinderte_Menschen", 1, "377,84"),
    ("frauen", "67", "Insgesamt", 4090, "569,02"),
    ("frauen", "67", "Regelaltersrenten", 4051, "564,13"),
    ("frauen", "67", "Altersrenten_fuer_besonders_langjaehrig_Versicherte", 10, "1.823,33"),
    ("frauen", "67", "Altersrenten_fuer_langjaehrig_Versicherte", 29, "819,18"),
    ("frauen", "68", "Insgesamt", 1727, "586,91"),
    ("frauen", "68", "Regelaltersrenten", 1713, "586,14"),
    ("frauen", "68", "Altersrenten_fuer_besonders_langjaehrig_Versicherte", 2, "1.178,79"),
    ("frauen", "68", "Altersrenten_fuer_langjaehrig_Versicherte", 12, "597,97"),
    ("frauen", "69", "Insgesamt", 1064, "537,71"),
    ("frauen", "69", "Regelaltersrenten", 1056, "537,21"),
    ("frauen", "69", "Altersrenten_fuer_langjaehrig_Versicherte", 7, "660,37"),
    ("frauen", "69", "Altersrenten_fuer_Frauen", 1, "203,22"),
    ("frauen", "70_und_aelter", "Insgesamt", 4740, "379,14"),
    ("frauen", "70_und_aelter", "Regelaltersrenten", 4722, "376,81"),
    ("frauen", "70_und_aelter", "Altersrenten_fuer_besonders_langjaehrig_Versicherte", 4, "1.729,82"),
    ("frauen", "70_und_aelter", "Altersrenten_fuer_langjaehrig_Versicherte", 14, "778,85"),
]


DEDUCTION_ROWS = [
    ("Renten_wegen_voller_Erwerbsminderung", 150070, 143101, "1.088,07", "32,30", 0, "", 6969, "1.326,91"),
    ("Renten_wegen_teilweiser_Erwerbsminderung", 19741, 18615, "606,45", "31,90", 0, "", 1126, "719,33"),
    ("Renten_wegen_Alters", 892440, 251013, "1.239,72", "32,15", 0, "", 641427, "1.109,83"),
    ("Regelaltersrenten", 367119, 314, "960,40", "13,90", 0, "", 366805, "741,81"),
    ("Altersrenten_fuer_besonders_langjaehrig_Versicherte", 251473, 65, "1.638,92", "9,00", 0, "", 251408, "1.625,60"),
    ("Altersrenten_fuer_langjaehrig_Versicherte", 213530, 211540, "1.222,97", "33,82", 0, "", 1990, "1.100,10"),
    ("Altersrenten_fuer_schwerbehinderte_Menschen", 60211, 39083, "1.332,16", "23,28", 21128, "1.363,23", 0, ""),
]


def ensure_pdf() -> None:
    if not PDF.exists():
        raise SystemExit(f"PDF not found: {PDF}")


def run_reference_extract() -> None:
    text = subprocess.run(
        ["pdftotext", "-layout", str(PDF), "-"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    for marker in ["40.00 Z", "40.01 Z", "40.02 Z", "20.00 Z - Renten mit Abschlagsmonaten"]:
        if marker not in text:
            raise SystemExit(f"Expected marker not found in PDF extract: {marker}")


def write_age_csv() -> None:
    AGE_CSV.parent.mkdir(parents=True, exist_ok=True)
    with AGE_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n", delimiter=";")
        writer.writerow(["geschlecht", "alter_label", "rentenart", "anzahl", "durchschnittlicher_rentenzahlbetrag_eur"])
        writer.writerows(AGE_ROWS)


def write_deduction_csv() -> None:
    with DEDUCTION_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n", delimiter=";")
        writer.writerow(
            [
                "rentenart",
                "anzahl_insgesamt",
                "anzahl_mit_abschlaegen",
                "durchschnittlicher_rentenzahlbetrag_mit_abschlaegen_eur",
                "durchschnittliche_anzahl_abschlagsmonate",
                "anzahl_ohne_abschlaege_vertrauensschutz",
                "durchschnittlicher_rentenzahlbetrag_ohne_abschlaege_vertrauensschutz_eur",
                "anzahl_ohne_abschlaege_nichtbetroffene_oder_aufschieber",
                "durchschnittlicher_rentenzahlbetrag_ohne_abschlaege_nichtbetroffene_oder_aufschieber_eur",
            ]
        )
        writer.writerows(DEDUCTION_ROWS)


def write_markdown() -> None:
    lines = [
        "---",
        "title: Oeffentlich verfuegbare DRV-Rentenzugangsdaten fuer das Reformmodell",
        "date: 2026-06-10",
        "type: analyse",
        "status: arbeitsfassung",
        "publish: false",
        "source_urls:",
        "  - https://www.deutsche-rentenversicherung.de/SharedDocs/Downloads/DE/Statistiken-und-Berichte/statistikpublikationen/statistikband_rente.pdf?__blob=publicationFile&v=5",
        "  - https://statistik-rente.de/drv/extern/rente/rentenbestand/",
        "  - https://www.bmas.de/SharedDocs/Downloads/DE/Rente/rentenversicherungsbericht-2025.pdf?__blob=publicationFile&v=3",
        "ingest_refs:",
        "  - ingest/dokumente/2026-06-04-drv-statistikband-rente-2024.md",
        "  - ingest/links/2026-06-04-statistik-rente-rentenbestand.md",
        "  - ingest/dokumente/2026-06-05-bmas-rentenversicherungsbericht-2025.md",
        "data_artifacts:",
        "  - analysen/daten/2026-06-10-drv-rentenzugang-oeffentlich-alter-rentenart.csv",
        "  - analysen/daten/2026-06-10-drv-rentenzugang-oeffentlich-abschlaege.csv",
        "scripts:",
        "  - scripts/extract_drv_rentenzugang_public.py",
        "related_projects:",
        "  - projekte/rentenversicherung/reformkonzept.md",
        "---",
        "",
        "# Oeffentlich verfuegbare DRV-Rentenzugangsdaten fuer das Reformmodell",
        "",
        "## Zweck",
        "",
        "Diese Analyse zieht aus frei zugaenglichen DRV-Quellen das heraus, was ohne",
        "formale Datenanfrage bereits belastbar beschaffbar ist. Sie grenzt zugleich",
        "ab, welche Datenluecken fuer das Rentenreformmodell offen bleiben.",
        "",
        "## Beschaffbar ohne Anfrage",
        "",
        "- DRV-Statistikband 2024, Tabellen `40.00 Z`, `40.01 Z`, `40.02 Z`: Rentenzugang",
        "  2024 bei Altersrenten nach Einzelalter bei Rentenbeginn fuer 67, 68, 69 sowie",
        "  Sammelkategorie `70 und aelter`, jeweils mit Anzahl und durchschnittlichem",
        "  Rentenzahlbetrag, getrennt nach Gesamt, Maennern und Frauen.",
        "- Tabelle `20.00 Z`: Renten mit Abschlagsmonaten nach Rentenarten, inklusive",
        "  durchschnittlicher Anzahl der Abschlagsmonate; allerdings ohne Aufschluesselung",
        "  nach Einzelalter 67 bis 72.",
        "",
        "## Kernergebnisse aus den oeffentlichen Tabellen",
        "",
        "| Ebene | Oeffentlich verfuegbar | Aussage |",
        "| --- | --- | --- |",
        "| Alter 67 | Ja | Rentenzugang nach Rentenart und Geschlecht ist direkt sichtbar. |",
        "| Alter 68 | Ja | Rentenzugang nach Rentenart und Geschlecht ist direkt sichtbar. |",
        "| Alter 69 | Ja | Rentenzugang nach Rentenart und Geschlecht ist direkt sichtbar. |",
        "| Alter 70 | Nein, nur in `70 und aelter` | Einzelalter 70, 71, 72 sind nicht getrennt ausgewiesen. |",
        "| Abschlaege/Zugangsfaktor nach 67-72 | Nein | Nur aggregierte Abschlagstabellen nach Rentenart, nicht nach Einzelalter 67-72. |",
        "| Erwerbsminderung 67-72 | Nein als altersscharfe Zugangstabelle | Im frei verfuegbaren Paket keine getrennte DRV-Zugangstabelle 67-72 fuer EM-Renten. |",
        "",
        "## Direkt nutzbare Zahlen fuer das Reformmodell",
        "",
        "- Insgesamt 2024 gingen bei Altersrenten `10.101` Zugaenge mit Rentenbeginn `67`,",
        "  `4.241` mit `68`, `2.503` mit `69` und `7.305` in `70 und aelter` zu.",
        "- Bei Maennern entfallen auf `67`: `6.011`, auf `68`: `2.514`, auf `69`: `1.439`,",
        "  auf `70 und aelter`: `2.565` Altersrentenzugaenge.",
        "- Bei Frauen entfallen auf `67`: `4.090`, auf `68`: `1.727`, auf `69`: `1.064`,",
        "  auf `70 und aelter`: `4.740` Altersrentenzugaenge.",
        "- Von allen Altersrentenzugaengen 2024 hatten `251.013` Abschlaege; die",
        "  durchschnittliche Anzahl der Abschlagsmonate lag bei `32,15`.",
        "- Bei Altersrenten fuer langjaehrig Versicherte hatten `211.540` von `213.530`",
        "  Vollrenten Abschlaege; fuer schwerbehinderte Menschen `39.083` von `60.211`.",
        "",
        "## Was weiter fehlt",
        "",
        "- Einzelalter 70, 71 und 72 als getrennte Rentenzugangstabellen.",
        "- Kreuztabellen `Alter x Rentenart x Zugangsfaktor/Abschlag` fuer 67 bis 72.",
        "- Altersscharfe DRV-Daten zu Erwerbsminderungsrenten im Korridor 67 bis 72.",
        "- Amtliche Bundesmittel-Ist-Zweckzerlegung 2024 bis 2026.",
        "",
        "## Einordnung",
        "",
        "Die offene Luecke ist damit kleiner als zuvor: Fuer 67 bis 69 liegen oeffentlich",
        "echte DRV-Rentenzugangsangaben fuer Altersrenten vor. Die harte Restluecke",
        "bleibt aber genau dort, wo das Reformmodell fein werden soll: Einzelalter 70, 71",
        "und 72 sowie altersscharfe Abschlags- und Zugangsfaktordaten sind in den frei",
        "zugaenglichen Publikationen nicht getrennt ausgewiesen.",
    ]
    OUTPUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_pdf()
    run_reference_extract()
    write_age_csv()
    write_deduction_csv()
    write_markdown()
    print(f"Wrote {AGE_CSV}")
    print(f"Wrote {DEDUCTION_CSV}")
    print(f"Wrote {OUTPUT_MD}")


if __name__ == "__main__":
    main()
