#!/usr/bin/env python3
"""Empirische GENESIS-Altersjahrgaenge fuer das Rentenaltermodell."""

from __future__ import annotations

import csv
import json
import re
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "ingest/originale"
DATA_DIR = ROOT / "analysen/daten"
OUTPUT_DETAIL = DATA_DIR / "2026-06-07-rentenalter-genesis-empirisch-altersjahre.csv"
OUTPUT_SUMMARY = DATA_DIR / "2026-06-07-rentenalter-genesis-empirisch-summary.csv"
OUTPUT_MD = ROOT / "analysen/2026-06-07-rentenalter-genesis-empirisch.md"

RAW_ACTUAL = RAW_DIR / "2026-06-07-genesis-12411-0005-bevoelkerung-altersjahre.json"
RAW_MIKROZENSUS = RAW_DIR / "2026-06-07-genesis-12211-0002-mikrozensus-erwerbsstatus.json"
RAW_MIKROZENSUS_EMPLOYED = RAW_DIR / "2026-06-07-genesis-12211-0004-erwerbstaetige-altersgruppen.json"
RAW_PROJECTIONS = {
    "moderat_g2l2w2": RAW_DIR / "2026-06-07-genesis-12421-0002-bev-v02-moderat.json",
    "alt_g1l3w1": RAW_DIR / "2026-06-07-genesis-12421-0002-bev-v04-alt.json",
    "jung_g3l1w3": RAW_DIR / "2026-06-07-genesis-12421-0002-bev-v05-jung.json",
}

VARIANT_LABELS = {
    "moderat_g2l2w2": "Geburtenrate, Lebenserwartung und Wanderungssaldo moderat",
    "alt_g1l3w1": "relativ alte Bevoelkerung",
    "jung_g3l1w3": "relativ junge Bevoelkerung",
}

RETIREMENT_AGE_SCENARIOS = {
    "status_quo_67": {2027: Decimal("67"), 2070: Decimal("67")},
    "lebenserwartung_2zu1": {
        2027: Decimal("67"),
        2035: Decimal("68"),
        2045: Decimal("69"),
        2055: Decimal("70"),
        2065: Decimal("71"),
        2070: Decimal("71.5"),
    },
    "daenemarknah": {
        2027: Decimal("67"),
        2030: Decimal("68"),
        2035: Decimal("69"),
        2040: Decimal("70"),
        2055: Decimal("71"),
        2070: Decimal("72"),
    },
}

MILESTONES = [2035, 2039, 2050, 2070]
MODEL_AGES = list(range(67, 73))
SENIOR_WAGE_FACTOR = Decimal("0.85")


def q(value: Decimal, places: str = "0.001") -> Decimal:
    return value.quantize(Decimal(places), rounding=ROUND_HALF_UP)


def parse_number(value: str) -> Decimal:
    value = value.strip()
    if value in {"", "-", "/", "x"}:
        return Decimal("0")
    return Decimal(value.replace(".", "").replace(",", "."))


def table_content(path: Path) -> list[list[str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return [line.split(";") for line in data["Object"]["Content"].splitlines()]


def age_from_label(label: str) -> int | None:
    if label == "unter 1 Jahr":
        return 0
    match = re.match(r"(\d+)", label)
    if match:
        return int(match.group(1))
    return None


def interpolate_schedule(schedule: dict[int, Decimal], year: int) -> Decimal:
    points = sorted(schedule.items())
    for (left_year, left_age), (right_year, right_age) in zip(points, points[1:]):
        if left_year <= year <= right_year:
            span = Decimal(right_year - left_year)
            offset = Decimal(year - left_year)
            return left_age + (right_age - left_age) * (offset / span)
    if year < points[0][0]:
        return points[0][1]
    return points[-1][1]


def active_fraction(age: int, retirement_age: Decimal) -> Decimal:
    if retirement_age <= Decimal(age):
        return Decimal("0")
    if retirement_age >= Decimal(age + 1):
        return Decimal("1")
    return retirement_age - Decimal(age)


def load_actual_population_2024() -> dict[int, Decimal]:
    rows = table_content(RAW_ACTUAL)
    date_row = next(row for row in rows if len(row) > 2 and row[1] == "31.12.2020")
    year_index = date_row.index("31.12.2024")
    result: dict[int, Decimal] = {}
    for row in rows:
        if len(row) <= year_index:
            continue
        age = age_from_label(row[0])
        if age is not None:
            result[age] = parse_number(row[year_index]) / Decimal("1000")
    return result


def load_projection(path: Path) -> dict[int, dict[int, Decimal]]:
    rows = table_content(path)
    date_row = next(row for row in rows if len(row) > 5 and row[4].startswith("31.12.2025"))
    years = [int(cell[-4:]) for cell in date_row[4:] if cell.startswith("31.12.")]
    result: dict[int, dict[int, Decimal]] = {year: {} for year in years}
    for row in rows:
        if len(row) < 5:
            continue
        if row[2] != "Insgesamt":
            continue
        age = age_from_label(row[3])
        if age is None:
            continue
        for year, cell in zip(years, row[4:]):
            result[year][age] = result[year].get(age, Decimal("0")) + parse_number(cell)
    return result


def load_senior_rates(projections: dict[str, dict[int, dict[int, Decimal]]]) -> dict[str, Decimal]:
    rows = table_content(RAW_MIKROZENSUS)
    line = next(row for row in rows if row[:3] == ["2025", "Insgesamt", "65 Jahre und mehr"])
    population = parse_number(line[3])
    employed = parse_number(line[4])
    labour_force = parse_number(line[6])
    employed_rows = table_content(RAW_MIKROZENSUS_EMPLOYED)
    employed_65_74_line = next(
        row for row in employed_rows if row[:3] == ["2025", "Insgesamt", "65 bis unter 75 Jahre"]
    )
    employed_65_74 = parse_number(employed_65_74_line[-1])
    population_65_74 = sum(projections["moderat_g2l2w2"][2025][age] for age in range(65, 75))
    return {
        "erwerbstaetigenquote_65plus": employed / population,
        "erwerbspersonenquote_65plus": labour_force / population,
        "erwerbstaetigenquote_65_74": employed_65_74 / population_65_74,
        "senior_wage_factor": SENIOR_WAGE_FACTOR,
    }


def population_for_year(
    actual_2024: dict[int, Decimal],
    projections: dict[str, dict[int, dict[int, Decimal]]],
    variant: str,
    year: int,
    age: int,
) -> Decimal:
    if year == 2024:
        return actual_2024.get(age, Decimal("0"))
    return projections[variant][year].get(age, Decimal("0"))


def build_rows() -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, Decimal]]:
    actual_2024 = load_actual_population_2024()
    projections = {variant: load_projection(path) for variant, path in RAW_PROJECTIONS.items()}
    rates = load_senior_rates(projections)
    detail_rows: list[dict[str, str]] = []
    summary_rows: list[dict[str, str]] = []

    for variant in RAW_PROJECTIONS:
        for year in MILESTONES:
            for scenario, schedule in RETIREMENT_AGE_SCENARIOS.items():
                retirement_age = interpolate_schedule(schedule, year)
                delayed_total = Decimal("0")
                effective_workers = Decimal("0")
                for age in MODEL_AGES:
                    population = population_for_year(actual_2024, projections, variant, year, age)
                    fraction = active_fraction(age, retirement_age)
                    delayed = population * fraction
                    effective = delayed * rates["erwerbstaetigenquote_65_74"] * SENIOR_WAGE_FACTOR
                    delayed_total += delayed
                    effective_workers += effective
                    detail_rows.append(
                        {
                            "jahr": str(year),
                            "destatis_variante": variant,
                            "destatis_variante_label": VARIANT_LABELS[variant],
                            "rentenalter_szenario": scenario,
                            "regelaltersgrenze": str(q(retirement_age, "0.001")),
                            "alter": str(age),
                            "bevoelkerung_altersjahr_mio": str(q(population / Decimal("1000"), "0.001")),
                            "nicht_in_rente_anteil": str(q(fraction, "0.001")),
                            "nicht_in_rente_mio": str(q(delayed / Decimal("1000"), "0.001")),
                            "erwerbstaetigenquote_bruecke_65_74": str(q(rates["erwerbstaetigenquote_65_74"], "0.000001")),
                            "erwerbstaetigenquote_65plus": str(q(rates["erwerbstaetigenquote_65plus"], "0.000001")),
                            "effektive_beitragszahler_mio": str(q(effective / Decimal("1000"), "0.001")),
                        }
                    )
                summary_rows.append(
                    {
                        "jahr": str(year),
                        "destatis_variante": variant,
                        "destatis_variante_label": VARIANT_LABELS[variant],
                        "rentenalter_szenario": scenario,
                        "regelaltersgrenze": str(q(retirement_age, "0.001")),
                        "nicht_in_rente_mio": str(q(delayed_total / Decimal("1000"), "0.001")),
                        "effektive_beitragszahler_mio": str(q(effective_workers / Decimal("1000"), "0.001")),
                        "erwerbstaetigenquote_bruecke_65_74": str(q(rates["erwerbstaetigenquote_65_74"], "0.000001")),
                        "erwerbstaetigenquote_65plus": str(q(rates["erwerbstaetigenquote_65plus"], "0.000001")),
                        "erwerbspersonenquote_65plus": str(q(rates["erwerbspersonenquote_65plus"], "0.000001")),
                        "notiz": "Altersjahrgaenge aus GENESIS; Erwerbstaetigenquote fuer 65 bis unter 75 aus Mikrozensus 2025 als Brueckenparameter.",
                    }
                )
    return detail_rows, summary_rows, rates


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def pick(summary_rows: list[dict[str, str]], variant: str, scenario: str, year: int) -> dict[str, str]:
    return next(
        row
        for row in summary_rows
        if row["destatis_variante"] == variant
        and row["rentenalter_szenario"] == scenario
        and int(row["jahr"]) == year
    )


def write_markdown(summary_rows: list[dict[str, str]], rates: dict[str, Decimal]) -> None:
    lines = [
        "---",
        "title: Empirisches Rentenaltermodell mit GENESIS-Altersjahrgaengen",
        "date: 2026-06-07",
        "type: analyse",
        "status: arbeitsfassung",
        "publish: false",
        "source_urls:",
        "  - https://genesis.destatis.de/genesisWS/swagger-ui/index.html",
        "ingest_refs:",
        "  - ingest/links/2026-06-06-destatis-genesis-api.md",
        "  - ingest/dokumente/2026-06-07-destatis-genesis-demographie-rente-tabellen.md",
        "data_artifacts:",
        "  - analysen/daten/2026-06-07-rentenalter-genesis-empirisch-altersjahre.csv",
        "  - analysen/daten/2026-06-07-rentenalter-genesis-empirisch-summary.csv",
        "scripts:",
        "  - scripts/calc_rentenalter_genesis_empirisch.py",
        "related_projects:",
        "  - projekte/rentenversicherung/reformkonzept.md",
        "---",
        "",
        "# Empirisches Rentenaltermodell mit GENESIS-Altersjahrgaengen",
        "",
        "## Zweck",
        "",
        "Diese Analyse ersetzt im Rentenalterblock die pauschale",
        "`0,95 Mio. je Altersjahr`-Kohorte durch amtliche GENESIS-Altersjahrgaenge",
        "aus der 16. koordinierten Bevoelkerungsvorausberechnung.",
        "",
        "## Datenbasis",
        "",
        "- `12411-0005`: Bevoelkerung Deutschland nach Altersjahren bis 31.12.2024.",
        "- `12421-0002`: vorausberechneter Bevoelkerungsstand Deutschland nach",
        "  Altersjahren, Geschlecht und Variante bis 31.12.2070.",
        "- `12211-0002`: Mikrozensus 2025, Erwerbstaetige und Erwerbspersonen",
        "  in Hauptwohnsitzhaushalten nach Altersgruppen.",
        "- `12211-0004`: Mikrozensus 2025, Erwerbstaetige nach Geschlecht,",
        "  Altersgruppen und Stellung im Beruf.",
        "",
        "## Brueckenparameter Erwerb",
        "",
        f"- Erwerbstaetigenquote 65 bis unter 75: {q(rates['erwerbstaetigenquote_65_74'] * Decimal('100'), '0.1')} %.",
        f"- Vergleichswert Erwerbstaetigenquote 65+: {q(rates['erwerbstaetigenquote_65plus'] * Decimal('100'), '0.1')} %.",
        f"- Erwerbspersonenquote 65+: {q(rates['erwerbspersonenquote_65plus'] * Decimal('100'), '0.1')} %.",
        "- Senior-Wage-Faktor: 0,85 als konservativer Abschlag auf volle",
        "  Beitragswirkung.",
        "",
        "Die Altersjahrgaenge sind damit empirisch. Die Erwerbsquote bleibt",
        "mangels oeffentlich gefundener feinjaehriger GENESIS-Erwerbsquoten ein",
        "transparenter Brueckenparameter. Gegenueber der Vorfassung wird nicht",
        "mehr `65 Jahre und mehr`, sondern die naehere amtliche Gruppe",
        "`65 bis unter 75 Jahre` verwendet.",
        "",
        "## Ergebnis",
        "",
        "| Jahr | Variante | Rentenalter | Nicht in Rente Mio. | Effektive Beitragszahler Mio. |",
        "| ---: | --- | --- | ---: | ---: |",
    ]
    for year in MILESTONES:
        for scenario in ["status_quo_67", "lebenserwartung_2zu1", "daenemarknah"]:
            row = pick(summary_rows, "moderat_g2l2w2", scenario, year)
            lines.append(
                f"| {year} | moderat | {scenario} ({row['regelaltersgrenze']}) | "
                f"{row['nicht_in_rente_mio']} | {row['effektive_beitragszahler_mio']} |"
            )
    lines.extend(
        [
            "",
            "## Sensitivitaet 2070",
            "",
            "| Variante | Szenario | Nicht in Rente Mio. | Effektive Beitragszahler Mio. |",
            "| --- | --- | ---: | ---: |",
        ]
    )
    for variant in ["alt_g1l3w1", "moderat_g2l2w2", "jung_g3l1w3"]:
        for scenario in ["lebenserwartung_2zu1", "daenemarknah"]:
            row = pick(summary_rows, variant, scenario, 2070)
            lines.append(
                f"| {VARIANT_LABELS[variant]} | {scenario} | "
                f"{row['nicht_in_rente_mio']} | {row['effektive_beitragszahler_mio']} |"
            )
    lines.extend(
        [
            "",
            "## Einordnung",
            "",
        "Der fruehere Prüferblocker `synthetische Altersjahrkohorten` ist damit",
        "fuer die Bevoelkerungsseite bearbeitet: die betroffenen Jahrgaenge",
        "67 bis 72 stammen aus GENESIS. Die Korrektur vom 2026-06-07 nutzt in",
        "`12421-0002` ausschliesslich die Geschlechtszeile `Insgesamt`; die",
        "Vorfassung hatte maennlich, weiblich und Insgesamt zusammengezählt.",
        "Nicht vollstaendig erledigt ist die Arbeitsmarktseite, weil GENESIS",
        "oeffentlich keine feinjaehrigen Erwerbsquoten fuer 67 bis 72 liefert.",
        "Fuer eine Freigabe sollte entweder ein Mikrozensus-Sondertabellenzugang,",
        "DRV-Rentenzugangsdaten oder eine andere amtliche Quelle fuer",
        "altersscharfe Erwerbsbeteiligung ergaenzt werden.",
            "",
        ]
    )
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    detail_rows, summary_rows, rates = build_rows()
    write_csv(OUTPUT_DETAIL, detail_rows)
    write_csv(OUTPUT_SUMMARY, summary_rows)
    write_markdown(summary_rows, rates)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
