#!/usr/bin/env python3
"""Berechnet demographische Belastungskennzahlen fuer die Rentenreform."""

from __future__ import annotations

import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "analysen/daten/2026-06-04-demographie-kernzahlen-2024-2070.csv"
OUTPUT = ROOT / "analysen/2026-06-04-rente-belastungsrechnung.md"


def read_rows() -> list[dict[str, str]]:
    with INPUT.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def row(
    rows: list[dict[str, str]],
    stichtag: str,
    kennzahl: str,
    variante: str = "",
) -> dict[str, str]:
    matches = [
        item
        for item in rows
        if item["stichtag"] == stichtag
        and item["kennzahl"] == kennzahl
        and item["variante"] == variante
    ]
    if len(matches) != 1:
        raise ValueError(
            f"Expected exactly one row for {stichtag=} {kennzahl=} {variante=}, "
            f"found {len(matches)}"
        )
    return matches[0]


def value(item: dict[str, str]) -> Decimal:
    return Decimal(item["wert"])


def pct_change(base: Decimal, target: Decimal) -> Decimal:
    return (target - base) / base * Decimal("100")


def q(value_: Decimal, places: str = "0.1") -> Decimal:
    return value_.quantize(Decimal(places), rounding=ROUND_HALF_UP)


def de_decimal(value_: Decimal, places: str = "0.1") -> str:
    return str(q(value_, places)).replace(".", ",")


def de_int(value_: Decimal) -> str:
    return str(value_.quantize(Decimal("1"), rounding=ROUND_HALF_UP)).replace(".", ",")


def de_million_from_people(value_: Decimal) -> str:
    return de_decimal(value_ / Decimal("1000000"), "0.001")


def main() -> None:
    rows = read_rows()

    population_2024 = value(row(rows, "2024-12-31", "Bevölkerung insgesamt"))
    workforce_2024 = value(row(rows, "2024", "Personen im Erwerbsalter 20 bis 66"))
    old_share_2024 = value(row(rows, "2024", "Anteil 67 Jahre und älter"))
    old_ratio_2024 = value(row(rows, "2024", "Altenquotient 20-66 zu 67+"))
    old_share_2035 = value(
        row(rows, "2035", "Anteil 67 Jahre und älter", "alle Varianten")
    )
    old_2038_min = value(
        row(rows, "2038", "Zahl 67 Jahre und älter Minimum", "Spannweite Varianten")
    )
    old_2038_max = value(
        row(rows, "2038", "Zahl 67 Jahre und älter Maximum", "Spannweite Varianten")
    )

    ratios = {
        "2038 Variante 5 G3L1W3": value(
            row(rows, "2038", "Altenquotient 20-66 zu 67+", "Variante 5 G3L1W3")
        ),
        "2038 Variante 2 G2L2W2": value(
            row(rows, "2038", "Altenquotient 20-66 zu 67+", "Variante 2 G2L2W2")
        ),
        "2038 Variante 4 G1L3W1": value(
            row(rows, "2038", "Altenquotient 20-66 zu 67+", "Variante 4 G1L3W1")
        ),
        "2070 Variante 5 G3L1W3": value(
            row(rows, "2070", "Altenquotient 20-66 zu 67+", "Variante 5 G3L1W3")
        ),
        "2070 Variante 2 G2L2W2": value(
            row(rows, "2070", "Altenquotient 20-66 zu 67+", "Variante 2 G2L2W2")
        ),
        "2070 Variante 4 G1L3W1": value(
            row(rows, "2070", "Altenquotient 20-66 zu 67+", "Variante 4 G1L3W1")
        ),
    }

    workforce_2070_min = value(
        row(
            rows,
            "2070",
            "Personen im Erwerbsalter 20 bis 66 Minimum",
            "Spannweite Varianten",
        )
    )
    workforce_2070_max = value(
        row(
            rows,
            "2070",
            "Personen im Erwerbsalter 20 bis 66 Maximum",
            "Spannweite Varianten",
        )
    )

    quotient_results = [
        (
            label,
            f"({de_int(target)} - {de_int(old_ratio_2024)}) / {de_int(old_ratio_2024)}",
            pct_change(old_ratio_2024, target),
        )
        for label, target in ratios.items()
    ]

    workforce_results = [
        (
            "2070 günstigerer Randwert",
            (
                f"({de_decimal(workforce_2070_max)} - "
                f"{de_decimal(workforce_2024)}) / {de_decimal(workforce_2024)}"
            ),
            pct_change(workforce_2024, workforce_2070_max),
        ),
        (
            "2070 ungünstigerer Randwert",
            (
                f"({de_decimal(workforce_2070_min)} - "
                f"{de_decimal(workforce_2024)}) / {de_decimal(workforce_2024)}"
            ),
            pct_change(workforce_2024, workforce_2070_min),
        ),
    ]

    lines = [
        "# Demographische Belastungsrechnung Rentenversicherung",
        "",
        "Stand: 2026-06-04",
        "",
        "Reproduzierbar mit:",
        "",
        "```bash",
        "python3 scripts/calc_demographie_rente.py",
        "```",
        "",
        f"Datenquelle: `{INPUT.relative_to(ROOT)}`",
        "",
        "## Zweck",
        "",
        "Diese Analyse berechnet aus den demographischen Eingangsdaten zentrale",
        "Belastungskennzahlen für Rentenreformmodelle, damit Altenquotient und",
        "Erwerbsbevölkerung nicht in jedem Konzept neu hergeleitet werden müssen.",
        "",
        "## Eingabewerte",
        "",
        "| Jahr | Variante | Kennzahl | Wert |",
        "| --- | --- | --- | ---: |",
        (
            "| 2024 | Ausgangswert | Bevölkerung insgesamt | "
            f"{de_million_from_people(population_2024)} Mio. |"
        ),
        (
            "| 2024 | Ausgangswert | Personen im Erwerbsalter 20-66 | "
            f"{de_decimal(workforce_2024)} Mio. |"
        ),
        f"| 2024 | Ausgangswert | Anteil 67 Jahre und älter | {de_int(old_share_2024)} % |",
        f"| 2024 | Ausgangswert | Altenquotient 20-66 / 67+ | {de_int(old_ratio_2024)} |",
        f"| 2035 | alle Varianten | Anteil 67 Jahre und älter | {de_int(old_share_2035)} % |",
        f"| 2038 | Spannweite Varianten | Personen ab 67 Jahren | {de_decimal(old_2038_min)} bis {de_decimal(old_2038_max)} Mio. |",
    ]

    for label, target in ratios.items():
        year, variant = label.split(" ", 1)
        lines.append(
            f"| {year} | {variant} | Altenquotient 20-66 / 67+ | {de_int(target)} |"
        )

    lines.extend(
        [
            (
                "| 2070 | Spannweite Varianten | Personen im Erwerbsalter 20-66 | "
                f"{de_decimal(workforce_2070_min)} bis "
                f"{de_decimal(workforce_2070_max)} Mio. |"
            ),
            "",
            "## Rechenergebnisse",
            "",
            "| Rechnung | Formel | Ergebnis |",
            "| --- | --- | ---: |",
        ]
    )

    for label, formula, result in quotient_results:
        lines.append(
            f"| Altenquotient {label} | `{formula}` | {de_decimal(result)} % |"
        )

    for label, formula, result in workforce_results:
        lines.append(f"| Erwerbsbevölkerung {label} | `{formula}` | {de_decimal(result)} % |")

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            (
                "- In der moderaten Variante steigt der Altenquotient bis 2038 "
                "um 36,4 % und bis 2070 um 54,5 % gegenüber 2024."
            ),
            (
                "- Selbst die relativ junge Variante liegt 2070 mit einem "
                "Altenquotienten von 43 klar über dem Ausgangswert 2024 von 33."
            ),
            (
                "- Die Bevölkerung im Alter 20-66 sinkt bis 2070 je nach "
                "Randwert um 11,5 % bis 27,5 % gegenüber 2024."
            ),
            "",
        ]
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
