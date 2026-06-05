#!/usr/bin/env python3
"""Hochrechnung der Renten-Finanzierungsluecke bei fixem Beitragssatz."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_CSV = (
    ROOT / "analysen/daten/2026-06-05-rentenproblem-finanzierungsluecke.csv"
)
ASSUMPTIONS_CSV = (
    ROOT / "analysen/daten/2026-06-05-rentenproblem-finanzierungsluecke-annahmen.csv"
)
GAP_SVG = (
    ROOT / "analysen/diagramme/2026-06-05-rentenproblem-finanzierungsluecke.svg"
)
FEDERAL_SVG = (
    ROOT / "analysen/diagramme/2026-06-05-rentenproblem-bundesmittelbedarf.svg"
)

START_YEAR = 2027
END_YEAR = 2070
BASE_YEAR = 2025

FIXED_CONTRIBUTION_RATE = Decimal("0.186")
BASE_CONTRIBUTIONS_BN = Decimal("321.552")
BASE_EXPENSES_BN = Decimal("426.521")
BASE_FEDERAL_BN = Decimal("97.858")
BASE_OTHER_REVENUES_BN = Decimal("3.194")
BASE_WORKING_AGE_M = Decimal("51.2")
BASE_OLD_AGE_M = BASE_WORKING_AGE_M * Decimal("0.33")

NOMINAL_WAGE_GROWTH = Decimal("0.025")
RENT_GROWTH_TO_2039 = Decimal("0.028")
RENT_GROWTH_AFTER_2039 = Decimal("0.023")
STATUS_QUO_2027_RATE_TARGET = Decimal("0.186")


@dataclass(frozen=True)
class ScenarioPoint:
    year: int
    working_age_m: Decimal
    old_age_m: Decimal


SCENARIOS = {
    "jung": [
        ScenarioPoint(2024, BASE_WORKING_AGE_M, BASE_OLD_AGE_M),
        ScenarioPoint(2038, Decimal("47.674419"), Decimal("20.5")),
        ScenarioPoint(2070, Decimal("45.3"), Decimal("20.1")),
    ],
    "moderat": [
        ScenarioPoint(2024, BASE_WORKING_AGE_M, BASE_OLD_AGE_M),
        ScenarioPoint(2038, Decimal("46.444444"), Decimal("20.9")),
        ScenarioPoint(2070, Decimal("41.2"), Decimal("20.95")),
    ],
    "alt": [
        ScenarioPoint(2024, BASE_WORKING_AGE_M, BASE_OLD_AGE_M),
        ScenarioPoint(2038, Decimal("45.319149"), Decimal("21.3")),
        ScenarioPoint(2070, Decimal("37.1"), Decimal("21.8")),
    ],
}

SCENARIO_LABELS = {
    "jung": "Junge Variante",
    "moderat": "Moderate Variante",
    "alt": "Alte Variante",
}

SCENARIO_COLORS = {
    "jung": "#0f766e",
    "moderat": "#b45309",
    "alt": "#be123c",
}


def q(value: Decimal, places: str = "0.001") -> Decimal:
    return value.quantize(Decimal(places), rounding=ROUND_HALF_UP)


def de(value: Decimal, places: str = "0.1") -> str:
    return str(q(value, places)).replace(".", ",")


def pct(value: Decimal) -> str:
    return de(value * Decimal("100"), "0.1")


def interpolate(points: list[ScenarioPoint], year: int, attr: str) -> Decimal:
    ordered = sorted(points, key=lambda item: item.year)
    for left, right in zip(ordered, ordered[1:]):
        if left.year <= year <= right.year:
            span = Decimal(right.year - left.year)
            offset = Decimal(year - left.year)
            start = getattr(left, attr)
            end = getattr(right, attr)
            return start + (end - start) * (offset / span)
    if year < ordered[0].year:
        return getattr(ordered[0], attr)
    return getattr(ordered[-1], attr)


def compounded_rate(year: int, rate: Decimal) -> Decimal:
    if year <= BASE_YEAR:
        return Decimal("1")
    return (Decimal("1") + rate) ** Decimal(year - BASE_YEAR)


def rent_index(year: int) -> Decimal:
    result = Decimal("1")
    for current_year in range(BASE_YEAR + 1, year + 1):
        growth = RENT_GROWTH_TO_2039 if current_year <= 2039 else RENT_GROWTH_AFTER_2039
        result *= Decimal("1") + growth
    return result


def base_payroll() -> Decimal:
    return BASE_CONTRIBUTIONS_BN / FIXED_CONTRIBUTION_RATE


def projected_payroll(points: list[ScenarioPoint], year: int) -> Decimal:
    working_age = interpolate(points, year, "working_age_m")
    return (
        base_payroll()
        * compounded_rate(year, NOMINAL_WAGE_GROWTH)
        * (working_age / BASE_WORKING_AGE_M)
    )


def projected_expenses_raw(points: list[ScenarioPoint], year: int) -> Decimal:
    old_age = interpolate(points, year, "old_age_m")
    return BASE_EXPENSES_BN * rent_index(year) * (old_age / BASE_OLD_AGE_M)


def other_revenues(year: int) -> Decimal:
    return BASE_OTHER_REVENUES_BN * compounded_rate(year, NOMINAL_WAGE_GROWTH)


def expense_calibration() -> Decimal:
    points = SCENARIOS["moderat"]
    year = START_YEAR
    federal_share = BASE_FEDERAL_BN / BASE_EXPENSES_BN
    target_expenses = (
        STATUS_QUO_2027_RATE_TARGET * projected_payroll(points, year)
        + other_revenues(year)
    ) / (Decimal("1") - federal_share)
    return target_expenses / projected_expenses_raw(points, year)


def projected_expenses(points: list[ScenarioPoint], year: int) -> Decimal:
    return projected_expenses_raw(points, year) * expense_calibration()


def build_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for scenario, points in SCENARIOS.items():
        for year in range(START_YEAR, END_YEAR + 1):
            working_age = interpolate(points, year, "working_age_m")
            old_age = interpolate(points, year, "old_age_m")
            payroll = projected_payroll(points, year)
            expenses = projected_expenses(points, year)
            fixed_contributions = payroll * FIXED_CONTRIBUTION_RATE
            other = other_revenues(year)
            baseline_revenues = fixed_contributions + BASE_FEDERAL_BN + other
            gap = expenses - baseline_revenues
            required_federal = expenses - fixed_contributions - other
            additional_federal = required_federal - BASE_FEDERAL_BN
            equivalent_rate = gap / payroll
            rows.append(
                {
                    "jahr": str(year),
                    "szenario": scenario,
                    "personen_20_66_mio": str(q(working_age, "0.001")),
                    "personen_67_plus_mio": str(q(old_age, "0.001")),
                    "ausgaben_mrd_euro": str(q(expenses, "0.001")),
                    "beitragsbasis_mrd_euro": str(q(payroll, "0.001")),
                    "fixer_beitragssatz": str(q(FIXED_CONTRIBUTION_RATE, "0.000001")),
                    "beitragseinnahmen_fix_mrd_euro": str(q(fixed_contributions, "0.001")),
                    "sonstige_einnahmen_mrd_euro": str(q(other, "0.001")),
                    "bundesmittel_basis_2025_mrd_euro": str(q(BASE_FEDERAL_BN, "0.001")),
                    "einnahmen_bei_fixem_beitrag_mrd_euro": str(q(baseline_revenues, "0.001")),
                    "finanzierungsluecke_mrd_euro": str(q(gap, "0.001")),
                    "erforderliche_bundesmittel_mrd_euro": str(q(required_federal, "0.001")),
                    "zusatz_bundesmittel_vs_2025_mrd_euro": str(q(additional_federal, "0.001")),
                    "aequivalenter_zusatzbeitragssatz_punkte": str(q(equivalent_rate * Decimal("100"), "0.001")),
                    "notiz": (
                        "Beitragssatz bleibt 18,6 %, Renteneintrittsalter bleibt "
                        "bei 67, Bundesmittel bleiben nominal auf 2025-Niveau."
                    ),
                }
            )
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_assumptions() -> None:
    rows = [
        ("fixed_contribution_rate", FIXED_CONTRIBUTION_RATE, "Status quo 2025/BMAS", "Beitragssatz bleibt ueber den gesamten Projektionszeitraum unveraendert."),
        ("retirement_age_boundary", "67+", "Destatis-Altersabgrenzung", "Renteneintrittsalter wird nicht angehoben; Lastseite bleibt Personen ab 67."),
        ("base_contributions_2025_mrd", BASE_CONTRIBUTIONS_BN, "DRV Finanzkennzahlen", "Beitragseinnahmen 2025."),
        ("base_expenses_2025_mrd", BASE_EXPENSES_BN, "DRV Finanzkennzahlen", "Ausgaben gesamt 2025."),
        ("base_federal_2025_mrd", BASE_FEDERAL_BN, "DRV Finanzkennzahlen", "Bundesmittel werden in der Lueckenrechnung nominal konstant gehalten."),
        ("base_other_revenues_2025_mrd", BASE_OTHER_REVENUES_BN, "DRV Finanzkennzahlen", "Sonstige Einnahmen; Fortschreibung mit Lohnwachstum."),
        ("nominal_wage_growth", NOMINAL_WAGE_GROWTH, "Arbeitsannahme wie Zukunftsmodell", "Wachstum der Beitragsbasis pro Jahr vor Demographieeffekt."),
        ("rent_growth_to_2039", RENT_GROWTH_TO_2039, "BMAS Rentenversicherungsbericht 2025", "Plausibilisiert durch Rentenanstieg bis 2039."),
        ("rent_growth_after_2039", RENT_GROWTH_AFTER_2039, "Arbeitsannahme wie Zukunftsmodell", "Fortschreibung nach 2039."),
        ("expense_calibration_factor", expense_calibration(), "Modellkalibrierung", "Kalibriert moderate Variante 2027 auf 18,6 % bei 2025er Bundesmittelanteil."),
    ]
    ASSUMPTIONS_CSV.parent.mkdir(parents=True, exist_ok=True)
    with ASSUMPTIONS_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["parameter", "wert", "quelle", "notiz"])
        writer.writerows(rows)


def row_value(row: dict[str, str], key: str) -> float:
    return float(row[key])


def nice_max(value: float) -> float:
    if value <= 0:
        return 1.0
    step = 50.0
    return ((int(value / step) + 1) * step)


def nice_min(value: float) -> float:
    if value >= 0:
        return 0.0
    step = 50.0
    return -((int(abs(value) / step) + 1) * step)


def svg_line_chart(
    rows: list[dict[str, str]],
    value_key: str,
    output: Path,
    title: str,
    y_label: str,
    baseline: float | None = None,
    baseline_label: str | None = None,
) -> None:
    width = 980
    height = 560
    left = 88
    right = 26
    top = 62
    bottom = 82
    plot_w = width - left - right
    plot_h = height - top - bottom
    years = list(range(START_YEAR, END_YEAR + 1))
    grouped = {
        scenario: [row for row in rows if row["szenario"] == scenario]
        for scenario in SCENARIOS
    }
    min_value = min(row_value(row, value_key) for row in rows)
    max_value = max(row_value(row, value_key) for row in rows)
    if baseline is not None:
        min_value = min(min_value, baseline)
        max_value = max(max_value, baseline)
    y_min = nice_min(min_value)
    y_max = nice_max(max_value)
    y_range = y_max - y_min

    def x(year: int) -> float:
        return left + ((year - START_YEAR) / (END_YEAR - START_YEAR)) * plot_w

    def y(value: float) -> float:
        return top + plot_h - ((value - y_min) / y_range) * plot_h

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">',
        f"<title>{title}</title>",
        "<style>",
        "text{font-family:Arial,Helvetica,sans-serif;fill:#1f2937}",
        ".axis{stroke:#111827;stroke-width:1.2}",
        ".grid{stroke:#d1d5db;stroke-width:1}",
        ".line{fill:none;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}",
        ".note{font-size:13px;fill:#4b5563}",
        "</style>",
        f'<rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>',
        f'<text x="{left}" y="32" font-size="22" font-weight="700">{title}</text>',
        f'<text x="{left}" y="52" class="note">{y_label}</text>',
    ]

    for tick in range(int(y_min), int(y_max) + 1, 50):
        yy = y(float(tick))
        lines.append(f'<line x1="{left}" y1="{yy:.1f}" x2="{width - right}" y2="{yy:.1f}" class="grid"/>')
        lines.append(f'<text x="{left - 12}" y="{yy + 4:.1f}" text-anchor="end" font-size="12">{tick}</text>')

    for year in [2030, 2040, 2050, 2060, 2070]:
        xx = x(year)
        lines.append(f'<line x1="{xx:.1f}" y1="{top}" x2="{xx:.1f}" y2="{height - bottom}" class="grid"/>')
        lines.append(f'<text x="{xx:.1f}" y="{height - bottom + 24}" text-anchor="middle" font-size="12">{year}</text>')

    zero_y = y(0.0) if y_min <= 0 <= y_max else height - bottom
    lines.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{height - bottom}" class="axis"/>')
    lines.append(f'<line x1="{left}" y1="{zero_y:.1f}" x2="{width - right}" y2="{zero_y:.1f}" class="axis"/>')

    if baseline is not None:
        yy = y(baseline)
        lines.append(f'<line x1="{left}" y1="{yy:.1f}" x2="{width - right}" y2="{yy:.1f}" stroke="#6b7280" stroke-width="2" stroke-dasharray="6 6"/>')
        if baseline_label:
            lines.append(f'<text x="{width - right - 6}" y="{yy - 8:.1f}" text-anchor="end" class="note">{baseline_label}</text>')

    legend_x = left
    legend_y = height - 32
    for i, scenario in enumerate(["jung", "moderat", "alt"]):
        values = sorted(grouped[scenario], key=lambda item: int(item["jahr"]))
        points = " ".join(
            f"{x(int(row['jahr'])):.1f},{y(row_value(row, value_key)):.1f}"
            for row in values
        )
        color = SCENARIO_COLORS[scenario]
        lines.append(f'<polyline points="{points}" class="line" stroke="{color}"/>')
        lx = legend_x + i * 230
        lines.append(f'<line x1="{lx}" y1="{legend_y}" x2="{lx + 28}" y2="{legend_y}" stroke="{color}" stroke-width="3"/>')
        lines.append(f'<text x="{lx + 38}" y="{legend_y + 5}" font-size="14">{SCENARIO_LABELS[scenario]}</text>')

    lines.append("</svg>")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_svgs(rows: list[dict[str, str]]) -> None:
    svg_line_chart(
        rows,
        "finanzierungsluecke_mrd_euro",
        GAP_SVG,
        "Finanzierungsluecke bei 18,6 % Beitragssatz",
        "Mrd. Euro pro Jahr, Bundesmittel nominal auf 2025-Niveau",
    )
    svg_line_chart(
        rows,
        "erforderliche_bundesmittel_mrd_euro",
        FEDERAL_SVG,
        "Erforderliche Bundesmittel bei fixem Beitragssatz",
        "Mrd. Euro pro Jahr",
        baseline=float(BASE_FEDERAL_BN),
        baseline_label="Bundesmittel 2025",
    )


def main() -> None:
    rows = build_rows()
    write_csv(OUTPUT_CSV, rows)
    write_assumptions()
    write_svgs(rows)


if __name__ == "__main__":
    main()
