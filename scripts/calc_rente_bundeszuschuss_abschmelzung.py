#!/usr/bin/env python3
"""Berechnet den Abschmelzpfad des Bestandsschutz-Zuschusses."""

from __future__ import annotations

import csv
import re
import zipfile
import xml.etree.ElementTree as ET
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STERBETAFEL = (
    ROOT / "demographie/originale/2026-06-04-destatis-sterbetafeln-2022-2024.xlsx"
)
OUTPUT_MD = (
    ROOT / "rentenversicherung/auswertungen/2026-06-04-bundeszuschuss-abschmelzung.md"
)
OUTPUT_CSV = (
    ROOT / "rentenversicherung/daten/2026-06-04-bundeszuschuss-abschmelzung.csv"
)

REFORM_YEAR = 2027
END_YEAR = 2070
START_ZUSCHUSS_BN = Decimal("97.858")
MALE_SHARE = Decimal("0.45")
FEMALE_SHARE = Decimal("0.55")

NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def q(value: Decimal, places: str = "0.001") -> Decimal:
    return value.quantize(Decimal(places), rounding=ROUND_HALF_UP)


def de(value: Decimal, places: str = "0.1") -> str:
    return str(q(value, places)).replace(".", ",")


def colnum(ref: str) -> int:
    letters = re.match(r"([A-Z]+)", ref)
    if not letters:
        raise ValueError(f"Invalid cell reference: {ref}")
    number = 0
    for char in letters.group(1):
        number = number * 26 + ord(char) - 64
    return number


def shared_strings(zip_file: zipfile.ZipFile) -> list[str]:
    root = ET.fromstring(zip_file.read("xl/sharedStrings.xml"))
    strings: list[str] = []
    for item in root.findall("m:si", NS):
        strings.append(
            "".join(
                text.text or ""
                for text in item.iter(
                    "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t"
                )
            )
        )
    return strings


def sheet_paths(zip_file: zipfile.ZipFile) -> dict[str, str]:
    workbook = ET.fromstring(zip_file.read("xl/workbook.xml"))
    rels = ET.fromstring(zip_file.read("xl/_rels/workbook.xml.rels"))
    rel_by_id = {rel.attrib["Id"]: rel.attrib["Target"] for rel in rels}
    result: dict[str, str] = {}

    for sheet in workbook.find("m:sheets", NS):
        name = sheet.attrib["name"]
        rel_id = sheet.attrib[
            "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
        ]
        target = rel_by_id[rel_id].lstrip("/")
        if not target.startswith("xl/"):
            target = f"xl/{target}"
        result[name] = target

    return result


def sheet_rows(
    zip_file: zipfile.ZipFile, sheet_path: str, strings: list[str]
) -> list[dict[int, str]]:
    root = ET.fromstring(zip_file.read(sheet_path))
    result: list[dict[int, str]] = []

    for row in root.findall(".//m:sheetData/m:row", NS):
        values: dict[int, str] = {}
        for cell in row.findall("m:c", NS):
            value = cell.find("m:v", NS)
            if value is None:
                continue
            text = value.text or ""
            if cell.attrib.get("t") == "s":
                text = strings[int(text)]
            values[colnum(cell.attrib.get("r", "A1"))] = text
        if values:
            result.append(values)

    return result


def read_lx(sheet_name: str) -> dict[int, Decimal]:
    with zipfile.ZipFile(STERBETAFEL) as zip_file:
        strings = shared_strings(zip_file)
        paths = sheet_paths(zip_file)
        rows = sheet_rows(zip_file, paths[sheet_name], strings)

    lx_by_age: dict[int, Decimal] = {}
    for row in rows:
        age_raw = row.get(1)
        lx_raw = row.get(4)
        if age_raw is None or lx_raw is None:
            continue
        try:
            age = int(Decimal(age_raw))
            lx = Decimal(lx_raw)
        except Exception:
            continue
        lx_by_age[age] = lx

    if 67 not in lx_by_age or 100 not in lx_by_age:
        raise ValueError(f"Unexpected life table shape in {sheet_name}")
    return lx_by_age


def age_weights() -> dict[int, Decimal]:
    """Arbeitsannahme bis echte DRV-Bestandsstruktur vorliegt.

    Die Bestandsrentner-Kohorte wird auf Altersjahre 67 bis 100 verteilt. Die
    Altersjahre 67 bis 79 erhalten zusammen 70 %, die Altersjahre 80 bis 100
    zusammen 30 %. Innerhalb der beiden Gruppen wird gleich gewichtet.
    """

    weights: dict[int, Decimal] = {}
    younger_weight = Decimal("0.70") / Decimal("13")
    older_weight = Decimal("0.30") / Decimal("21")
    for age in range(67, 80):
        weights[age] = younger_weight
    for age in range(80, 101):
        weights[age] = older_weight
    return weights


def survival_for_age(lx_by_age: dict[int, Decimal], age: int, years: int) -> Decimal:
    target_age = age + years
    if target_age > max(lx_by_age):
        return Decimal("0")
    return lx_by_age[target_age] / lx_by_age[age]


def cohort_survival(
    male_lx: dict[int, Decimal], female_lx: dict[int, Decimal], years: int
) -> Decimal:
    total = Decimal("0")
    for age, weight in age_weights().items():
        male_survival = survival_for_age(male_lx, age, years)
        female_survival = survival_for_age(female_lx, age, years)
        blended = MALE_SHARE * male_survival + FEMALE_SHARE * female_survival
        total += weight * blended
    return total


def build_rows() -> list[dict[str, Decimal | int]]:
    male_lx = read_lx("12613-b01")
    female_lx = read_lx("12613-b02")
    rows: list[dict[str, Decimal | int]] = []
    previous_zuschuss: Decimal | None = None

    for year in range(REFORM_YEAR, END_YEAR + 1):
        years_since_start = year - REFORM_YEAR
        survival = cohort_survival(male_lx, female_lx, years_since_start)
        zuschuss = START_ZUSCHUSS_BN * survival
        if previous_zuschuss is not None and zuschuss > previous_zuschuss:
            raise ValueError("Bestandsschutz-Zuschuss must not increase")
        annual_decline = (
            Decimal("0") if previous_zuschuss is None else previous_zuschuss - zuschuss
        )
        previous_zuschuss = zuschuss
        rows.append(
            {
                "jahr": year,
                "jahre_seit_reform": years_since_start,
                "ueberlebensquote": survival,
                "bestandsschutz_zuschuss_mrd_euro": zuschuss,
                "jaehrliche_abschmelzung_mrd_euro": annual_decline,
            }
        )
    return rows


def write_csv(rows: list[dict[str, Decimal | int]]) -> None:
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: str(q(value, "0.000001")) if isinstance(value, Decimal) else value
                    for key, value in row.items()
                }
            )


def milestone_rows(rows: list[dict[str, Decimal | int]]) -> list[dict[str, Decimal | int]]:
    milestones = {2027, 2030, 2035, 2040, 2045, 2050, 2060, 2070}
    return [row for row in rows if row["jahr"] in milestones]


def write_markdown(rows: list[dict[str, Decimal | int]]) -> None:
    OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Abschmelzmodell Bestandsschutz-Zuschuss Rentenversicherung",
        "",
        "Stand: 2026-06-04",
        "",
        "Reproduzierbar mit:",
        "",
        "```bash",
        "python3 scripts/calc_rente_bundeszuschuss_abschmelzung.py",
        "```",
        "",
        "## Eingaben",
        "",
        f"- Reformstichtag: {REFORM_YEAR}",
        f"- Startwert Bundesmittel 2025: {de(START_ZUSCHUSS_BN, '0.001')} Mrd. Euro",
        (
            "- Quelle Sterblichkeit: "
            "`demographie/originale/2026-06-04-destatis-sterbetafeln-2022-2024.xlsx`"
        ),
        "- Verwendete Tabellen: `12613-b01` männlich, `12613-b02` weiblich",
        "- Verwendete Größe: `Überlebende - lx` nach vollendetem Alter",
        "- Arbeitsannahme Geschlecht: 45 % männlich, 55 % weiblich",
        (
            "- Arbeitsannahme Alter: 70 % der Bestandsrentner in Altersjahren "
            "67-79, 30 % in Altersjahren 80-100, jeweils gleich verteilt"
        ),
        (
            "- Tabellenende: Die Destatis-Altersjahrestabelle endet bei Alter 100; "
            "Überleben oberhalb dieses Alters wird in v1 nicht fortgeschrieben"
        ),
        "",
        "## Modellregel",
        "",
        (
            "`Bestandsschutz-Zuschuss(t) = Startwert * erwartete Überlebendenzahl "
            "Bestandskohorte(t) / Bestandskohorte(2027)`"
        ),
        "",
        "Politische Sonderkürzungen sind in diesem Modell ausgeschlossen. Der Zuschuss",
        "sinkt nur proportional zum erwarteten Versterben der geschützten",
        "Bestandsrentner-Kohorte.",
        "",
        "## Ergebnisse",
        "",
        "| Jahr | Überlebensquote Bestandskohorte | Bestandsschutz-Zuschuss | Jährliche Abschmelzung |",
        "| --- | ---: | ---: | ---: |",
    ]

    for row in milestone_rows(rows):
        lines.append(
            "| {jahr} | {survival} % | {zuschuss} Mrd. Euro | {decline} Mrd. Euro |".format(
                jahr=row["jahr"],
                survival=de(row["ueberlebensquote"] * Decimal("100"), "0.1"),
                zuschuss=de(row["bestandsschutz_zuschuss_mrd_euro"], "0.001"),
                decline=de(row["jaehrliche_abschmelzung_mrd_euro"], "0.001"),
            )
        )

    lines.extend(
        [
            "",
            "Vollständige Jahreswerte:",
            "",
            "`rentenversicherung/daten/2026-06-04-bundeszuschuss-abschmelzung.csv`",
            "",
            "## Interpretation",
            "",
            "- Der Zuschuss bleibt im Reformjahr vollständig erhalten.",
            "- Danach sinkt er nur mit der erwarteten Überlebendenquote des Altbestands.",
            "- Neue rentenwirksame Staatsleistungen ab 2027 sind zusätzlich als echte Beiträge zu finanzieren.",
            "",
            "## Offene Punkte",
            "",
            "- Tatsächliche Alters- und Geschlechtsstruktur der laufenden Renten fehlt noch.",
            "- Die v1-Altersverteilung ist eine Arbeitsannahme und muss durch DRV-Daten ersetzt werden.",
            "- Der 100+-Tail muss in einer Prüffassung explizit modelliert werden.",
            "- Sterblichkeitsverbesserungen nach 2022/2024 sind noch nicht als Sensitivität modelliert.",
            "",
        ]
    )
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = build_rows()
    write_csv(rows)
    write_markdown(rows)


if __name__ == "__main__":
    main()
