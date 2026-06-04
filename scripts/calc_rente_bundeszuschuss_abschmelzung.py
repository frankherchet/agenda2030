#!/usr/bin/env python3
"""Berechnet den Abschmelzpfad des Bestandsschutz-Zuschusses."""

from __future__ import annotations

import csv
import re
import zipfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STERBETAFEL = (
    ROOT / "ingest/originale/2026-06-04-destatis-sterbetafeln-2022-2024.xlsx"
)
BESTAND_CSV = ROOT / "analysen/daten/2026-06-04-drv-rentenbestand-struktur.csv"
BUNDESMITTEL_CSV = ROOT / "analysen/daten/2026-06-04-bundesmittel-zerlegung.csv"
OUTPUT_MD = (
    ROOT / "analysen/2026-06-04-bundeszuschuss-abschmelzung.md"
)
OUTPUT_CSV = (
    ROOT / "analysen/daten/2026-06-04-bundeszuschuss-abschmelzung.csv"
)

REFORM_YEAR = 2027
END_YEAR = 2070

NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


@dataclass(frozen=True)
class LifeTable:
    lx_by_age: dict[int, Decimal]
    px_at_100: Decimal


@dataclass(frozen=True)
class Cohort:
    counts_by_sex_age: dict[tuple[str, int], Decimal]
    included_count: Decimal
    excluded_count: Decimal


def q(value: Decimal, places: str = "0.001") -> Decimal:
    return value.quantize(Decimal(places), rounding=ROUND_HALF_UP)


def de(value: Decimal, places: str = "0.1") -> str:
    return str(q(value, places)).replace(".", ",")


def de_int(value: Decimal) -> str:
    return f"{int(q(value, '1')):,}".replace(",", ".")


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


def read_life_table(sheet_name: str) -> LifeTable:
    with zipfile.ZipFile(STERBETAFEL) as zip_file:
        strings = shared_strings(zip_file)
        paths = sheet_paths(zip_file)
        rows = sheet_rows(zip_file, paths[sheet_name], strings)

    lx_by_age: dict[int, Decimal] = {}
    px_at_100: Decimal | None = None
    for row in rows:
        age_raw = row.get(1)
        px_raw = row.get(3)
        lx_raw = row.get(4)
        if age_raw is None or lx_raw is None:
            continue
        try:
            age = int(Decimal(age_raw))
            lx = Decimal(lx_raw)
            px = Decimal(px_raw) if px_raw is not None else None
        except Exception:
            continue
        lx_by_age[age] = lx
        if age == 100 and px is not None:
            px_at_100 = px

    if 20 not in lx_by_age or 100 not in lx_by_age or px_at_100 is None:
        raise ValueError(f"Unexpected life table shape in {sheet_name}")
    return LifeTable(lx_by_age=lx_by_age, px_at_100=px_at_100)


def parse_decimal(value: str) -> Decimal:
    return Decimal(value.replace(",", "."))


def start_zuschuss() -> Decimal:
    total = Decimal("0")
    with BUNDESMITTEL_CSV.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if row["abschmelzbar"] == "ja":
                total += parse_decimal(row["betrag_mrd_euro"])
    if total <= 0:
        raise ValueError("No abschmelzbare Bundesmittel found")
    return total


def expand_age_range(age_from: str, age_to: str) -> list[int]:
    start = int(age_from)
    if age_to == "":
        return [start]
    end = int(age_to)
    return list(range(start, end + 1))


def add_count(
    counts: dict[tuple[str, int], Decimal], sex: str, age: int, count: Decimal
) -> None:
    key = (sex, age)
    counts[key] = counts.get(key, Decimal("0")) + count


def read_cohort() -> Cohort:
    counts: dict[tuple[str, int], Decimal] = {}
    included = Decimal("0")
    excluded = Decimal("0")

    with BESTAND_CSV.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if row["system"] != "rv_gesamt":
                continue

            count = parse_decimal(row["anzahl_renten"])
            if row["alter_von"] == "":
                excluded += count
                continue

            ages = expand_age_range(row["alter_von"], row["alter_bis"])
            count_per_age = count / Decimal(len(ages))
            sex = row["geschlecht"]
            for age in ages:
                if sex == "unbekannt":
                    # Waisen- und Erziehungsrenten sind im DRV-Tabellenband nicht
                    # geschlechtsspezifisch ausgewiesen; der konservative Split
                    # verhindert eine implizite Ein-Geschlecht-Annahme.
                    add_count(counts, "maennlich", age, count_per_age / Decimal("2"))
                    add_count(counts, "weiblich", age, count_per_age / Decimal("2"))
                else:
                    add_count(counts, sex, age, count_per_age)
            included += count

    if included <= 0:
        raise ValueError("No modeled DRV cohort found")
    return Cohort(
        counts_by_sex_age=counts,
        included_count=included,
        excluded_count=excluded,
    )


def survival_for_age(table: LifeTable, age: int, years: int) -> Decimal:
    if years == 0:
        return Decimal("1")

    lx = table.lx_by_age
    max_age = max(lx)
    if age > max_age:
        return table.px_at_100**years

    target_age = age + years
    if target_age <= max_age:
        return lx[target_age] / lx[age]

    years_after_table = target_age - max_age
    return (lx[max_age] / lx[age]) * (table.px_at_100**years_after_table)


def cohort_survival(
    cohort: Cohort, male_table: LifeTable, female_table: LifeTable, years: int
) -> Decimal:
    total_survivors = Decimal("0")
    for (sex, age), count in cohort.counts_by_sex_age.items():
        table = male_table if sex == "maennlich" else female_table
        total_survivors += count * survival_for_age(table, age, years)
    return total_survivors / cohort.included_count


def build_rows() -> tuple[list[dict[str, Decimal | int]], Cohort, Decimal]:
    male_table = read_life_table("12613-b01")
    female_table = read_life_table("12613-b02")
    cohort = read_cohort()
    start = start_zuschuss()
    rows: list[dict[str, Decimal | int]] = []
    previous_zuschuss: Decimal | None = None

    for year in range(REFORM_YEAR, END_YEAR + 1):
        years_since_start = year - REFORM_YEAR
        survival = cohort_survival(cohort, male_table, female_table, years_since_start)
        zuschuss = start * survival
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
    return rows, cohort, start


def write_csv(rows: list[dict[str, Decimal | int]]) -> None:
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(rows[0].keys()), lineterminator="\n"
        )
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


def write_markdown(
    rows: list[dict[str, Decimal | int]], cohort: Cohort, start: Decimal
) -> None:
    OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Abschmelzmodell Bestandsschutz-Zuschuss Rentenversicherung",
        "",
        "Stand: 2026-06-04",
        "",
        "Reproduzierbar mit:",
        "",
        "```bash",
        "python3 scripts/build_drv_renten_inputs.py",
        "python3 scripts/calc_rente_bundeszuschuss_abschmelzung.py",
        "```",
        "",
        "## Zweck",
        "",
        "Diese Analyse modelliert, wie ein Bestandsschutz-Zuschuss für bereits",
        "erworbene Rentenansprüche anhand der erwarteten Überlebendenzahl der",
        "Bestandskohorte abschmelzen kann.",
        "",
        "## Eingaben",
        "",
        f"- Reformstichtag: {REFORM_YEAR}",
        f"- Abschmelzbarer Startwert Bundesmittel 2025: {de(start, '0.001')} Mrd. Euro",
        f"- Modellierte laufende Renten aus DRV-Rentenbestand 2024: {de_int(cohort.included_count)} Renten",
        f"- Nicht modellierte Restzeilen ohne Alter: {de_int(cohort.excluded_count)} Renten",
        "- Rentenbestandsstruktur: `analysen/daten/2026-06-04-drv-rentenbestand-struktur.csv`",
        "- Bundesmittel-Zerlegung: `analysen/daten/2026-06-04-bundesmittel-zerlegung.csv`",
        (
            "- Quelle Sterblichkeit: "
            "`ingest/originale/2026-06-04-destatis-sterbetafeln-2022-2024.xlsx`"
        ),
        "- Verwendete Tabellen: `12613-b01` männlich, `12613-b02` weiblich",
        "- Verwendete Größen: `Überlebende - lx` und `Überlebenswahrscheinlichkeit - px` bei Alter 100",
        (
            "- Offene Altersgruppen: `100 und älter` und `105 und älter` werden ab "
            "dem Gruppenstart mit der Destatis-Überlebenswahrscheinlichkeit bei "
            "Alter 100 fortgeschrieben."
        ),
        (
            "- Waisen- und Erziehungsrenten: mangels Geschlechtstrennung im "
            "DRV-Tabellenband je hälftig männlich/weiblich modelliert."
        ),
        (
            "- Knappschaft-Bahn-See: als eigene aggregierte Trägergruppe erfasst; "
            "nicht zusätzlich modelliert, weil ihre Renten bereits in `rv_gesamt` enthalten sind."
        ),
        "",
        "## Modellregel",
        "",
        (
            "`Bestandsschutz-Zuschuss(t) = abschmelzbarer Startwert * erwartete "
            "Überlebendenzahl Bestandskohorte(t) / Bestandskohorte(2027)`"
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
            "`analysen/daten/2026-06-04-bundeszuschuss-abschmelzung.csv`",
            "",
            "## Interpretation",
            "",
            "- Der Zuschuss bleibt im Reformjahr vollständig erhalten.",
            "- Danach sinkt er nur mit der erwarteten Überlebendenquote des Altbestands.",
            "- Neue rentenwirksame Staatsleistungen ab 2027 sind zusätzlich als echte Beiträge zu finanzieren.",
            "- Die frühere 70/30-Ersatzverteilung wurde durch DRV-Rentenbestandsdaten ersetzt.",
            "",
            "## Restunsicherheiten",
            "",
            "- Die Zerlegung der Bundesmittel ist in dieser Fassung eine Reformklassifikation, keine amtliche Zweckzerlegung.",
            "- Für Knappschaft-Bahn-See liegt im DRV-Tabellenband nur eine aggregierte Trägertrennung vor.",
            "- Sterblichkeitsverbesserungen nach 2022/2024 sind noch nicht als Sensitivität modelliert.",
            "",
        ]
    )
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows, cohort, start = build_rows()
    write_csv(rows)
    write_markdown(rows, cohort, start)


if __name__ == "__main__":
    main()
