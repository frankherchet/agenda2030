#!/usr/bin/env python3
"""Berechnet ein v1-Zukunftsmodell der Rentenreform bis 2070."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ABSCHMELZUNG_CSV = (
    ROOT / "analysen/daten/2026-06-04-bundeszuschuss-abschmelzung.csv"
)
OUTPUT_CSV = (
    ROOT / "analysen/daten/2026-06-04-rentenreform-zukunft-modell.csv"
)
ASSUMPTIONS_CSV = (
    ROOT / "analysen/daten/2026-06-04-rentenreform-zukunft-annahmen.csv"
)
OUTPUT_MD = (
    ROOT / "analysen/2026-06-04-rentenreform-zukunft.md"
)

START_YEAR = 2027
REFORM_YEAR = 2030
END_YEAR = 2070
BASE_YEAR = 2025

BASE_CONTRIBUTION_RATE = Decimal("0.186")
BASE_CONTRIBUTIONS_BN = Decimal("321.552")
BASE_EXPENSES_BN = Decimal("426.521")
BASE_FEDERAL_BN = Decimal("97.858")
BASE_OTHER_REVENUES_BN = Decimal("3.194")

BASE_WORKING_AGE_M = Decimal("51.2")
BASE_OLD_AGE_M = BASE_WORKING_AGE_M * Decimal("0.33")
SOCIAL_INSURED_EMPLOYEES_M = Decimal("34.885")
SELF_EMPLOYED_M = Decimal("3.666")
PUBLIC_SERVICE_EXEMPT_M = Decimal("1.9557")

NOMINAL_WAGE_GROWTH = Decimal("0.025")
RENT_GROWTH_TO_2039 = Decimal("0.028")
RENT_GROWTH_AFTER_2039 = Decimal("0.023")
SELF_EMPLOYED_EFFECTIVE_COVERAGE = Decimal("0.75")
SELF_EMPLOYED_INCOME_FACTOR = Decimal("0.70")
PUBLIC_SERVICE_INCOME_FACTOR = Decimal("1.10")
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


def phase_in(year: int, start: int, end: int, target: Decimal) -> Decimal:
    if year < start:
        return Decimal("0")
    if year >= end:
        return target
    span = Decimal(end - start + 1)
    offset = Decimal(year - start + 1)
    return target * (offset / span)


def public_service_ramp(year: int) -> Decimal:
    if year < REFORM_YEAR:
        return Decimal("0")
    if year <= 2045:
        return phase_in(year, REFORM_YEAR, 2045, Decimal("0.30"))
    return Decimal("0.30") + phase_in(year, 2046, 2070, Decimal("0.40"))


def federal_support(year: int, status_federal: Decimal, abschmelzung: dict[int, Decimal]) -> Decimal:
    if year < REFORM_YEAR:
        return status_federal
    return abschmelzung[year]


def read_abschmelzung() -> dict[int, Decimal]:
    result: dict[int, Decimal] = {}
    with ABSCHMELZUNG_CSV.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            result[int(row["jahr"])] = Decimal(row["bestandsschutz_zuschuss_mrd_euro"])
    return result


def base_payroll() -> Decimal:
    return BASE_CONTRIBUTIONS_BN / BASE_CONTRIBUTION_RATE


def projected_payroll(scenario_points: list[ScenarioPoint], year: int) -> Decimal:
    working_age = interpolate(scenario_points, year, "working_age_m")
    return (
        base_payroll()
        * compounded_rate(year, NOMINAL_WAGE_GROWTH)
        * (working_age / BASE_WORKING_AGE_M)
    )


def expanded_payroll(scenario_points: list[ScenarioPoint], year: int) -> Decimal:
    base = projected_payroll(scenario_points, year)
    self_ratio = SELF_EMPLOYED_M / SOCIAL_INSURED_EMPLOYEES_M
    public_ratio = PUBLIC_SERVICE_EXEMPT_M / SOCIAL_INSURED_EMPLOYEES_M
    self_phase = phase_in(year, REFORM_YEAR, 2035, SELF_EMPLOYED_EFFECTIVE_COVERAGE)
    public_phase = public_service_ramp(year)
    return base * (
        self_ratio * SELF_EMPLOYED_INCOME_FACTOR * self_phase
        + public_ratio * PUBLIC_SERVICE_INCOME_FACTOR * public_phase
    )


def projected_expenses(scenario_points: list[ScenarioPoint], year: int) -> Decimal:
    old_age = interpolate(scenario_points, year, "old_age_m")
    return BASE_EXPENSES_BN * rent_index(year) * (old_age / BASE_OLD_AGE_M)


def expense_calibration() -> Decimal:
    points = SCENARIOS["moderat"]
    year = START_YEAR
    federal_share = BASE_FEDERAL_BN / BASE_EXPENSES_BN
    target_expenses = (
        STATUS_QUO_2027_RATE_TARGET * projected_payroll(points, year)
        + other_revenues(year)
    ) / (Decimal("1") - federal_share)
    return target_expenses / projected_expenses(points, year)


def other_revenues(year: int) -> Decimal:
    return BASE_OTHER_REVENUES_BN * compounded_rate(year, NOMINAL_WAGE_GROWTH)


def required_rate(expenses: Decimal, federal: Decimal, other: Decimal, payroll: Decimal) -> Decimal:
    return (expenses - federal - other) / payroll


def build_rows() -> list[dict[str, str]]:
    abschmelzung = read_abschmelzung()
    federal_share = BASE_FEDERAL_BN / BASE_EXPENSES_BN
    calibration = expense_calibration()
    rows: list[dict[str, str]] = []

    for scenario, points in SCENARIOS.items():
        for year in range(START_YEAR, END_YEAR + 1):
            expenses = projected_expenses(points, year) * calibration
            payroll_base = projected_payroll(points, year)
            payroll_extra = expanded_payroll(points, year)
            other = other_revenues(year)
            status_federal = expenses * federal_share
            reform_federal = federal_support(year, status_federal, abschmelzung)

            variants = [
                (
                    "status_quo_bund_anteilig",
                    payroll_base,
                    status_federal,
                    "Referenz: Bundesmittel behalten 2025er Ausgabenanteil.",
                ),
                (
                    "reform_ohne_erweiterte_basis",
                    payroll_base,
                    reform_federal,
                    "Bestandsschutz-Zuschuss schmilzt; Beitragsbasis unverändert.",
                ),
                (
                    "reform_mit_erwerbstaetigenbasis",
                    payroll_base + payroll_extra,
                    reform_federal,
                    "Bestandsschutz schmilzt; Selbstständige und Neubeamte beziehungsweise neue Dienstherrenbeiträge erhöhen Beitragsbasis.",
                ),
            ]
            for variant, payroll, federal, note in variants:
                rate = required_rate(expenses, federal, other, payroll)
                rows.append(
                    {
                        "jahr": str(year),
                        "szenario": scenario,
                        "variante": variant,
                        "ausgaben_mrd_euro": str(q(expenses, "0.001")),
                        "beitragsbasis_mrd_euro": str(q(payroll, "0.001")),
                        "zusatzbasis_mrd_euro": str(q(max(payroll - payroll_base, Decimal("0")), "0.001")),
                        "bundesmittel_mrd_euro": str(q(federal, "0.001")),
                        "sonstige_einnahmen_mrd_euro": str(q(other, "0.001")),
                        "erforderlicher_beitragssatz": str(q(rate, "0.000001")),
                        "notiz": note,
                    }
                )
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(rows[0].keys()), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def write_assumptions() -> None:
    rows = [
        ("base_contribution_rate_2025", BASE_CONTRIBUTION_RATE, "DRV/BMAS", "Beitragssatz allgemeine RV"),
        ("base_contributions_2025_mrd", BASE_CONTRIBUTIONS_BN, "DRV Finanzkennzahlen", "Beitragseinnahmen 2025"),
        ("base_expenses_2025_mrd", BASE_EXPENSES_BN, "DRV Finanzkennzahlen", "Ausgaben gesamt 2025"),
        ("base_federal_2025_mrd", BASE_FEDERAL_BN, "DRV Finanzkennzahlen", "Bundesmittel 2025"),
        ("base_other_revenues_2025_mrd", BASE_OTHER_REVENUES_BN, "DRV Finanzkennzahlen", "Erstattungen, Vermögenserträge, sonstige Einnahmen"),
        ("nominal_wage_growth", NOMINAL_WAGE_GROWTH, "Arbeitsannahme", "Lohn-/Beitragsbasiswachstum p.a."),
        ("rent_growth_to_2039", RENT_GROWTH_TO_2039, "BMAS Rentenversicherungsbericht 2025", "Plausibilisiert durch gut 45 % Rentenanstieg bis 2039"),
        ("rent_growth_after_2039", RENT_GROWTH_AFTER_2039, "Arbeitsannahme", "Fortschreibung nach 2039"),
        ("status_quo_2027_rate_target", STATUS_QUO_2027_RATE_TARGET, "BMAS Rentenversicherungsbericht 2025", "Kalibrierung des vorreformlichen Brückenpfads 2027-2029; Reformstart 1.1.2030"),
        ("expense_calibration_factor", expense_calibration(), "Modellkalibrierung", "Skaliert Ausgabenpfad auf moderates Status-quo-Szenario 2027 und die Brückenjahre 2027-2029"),
        ("self_employed_2025_mio", SELF_EMPLOYED_M, "Destatis Arbeitsmarkt-Eckzahlen", "Selbstständige inkl. mithelfende Familienangehörige"),
        ("social_insured_employees_2025_mio", SOCIAL_INSURED_EMPLOYEES_M, "Destatis Arbeitsmarkt-Eckzahlen", "Sozialversicherungspflichtig Beschäftigte"),
        ("public_service_exempt_2024_mio", PUBLIC_SERVICE_EXEMPT_M, "Destatis öffentlicher Dienst", "Beamte/Richter plus Berufs-/Zeitsoldaten als Proxy fuer Neubeamte und neue Dienstherrenbeiträge"),
        ("self_employed_effective_coverage", SELF_EMPLOYED_EFFECTIVE_COVERAGE, "Arbeitsannahme", "Bis 2035 effektiv einbezogener Selbstständigenanteil ab Reformstart 2030"),
        ("self_employed_income_factor", SELF_EMPLOYED_INCOME_FACTOR, "Arbeitsannahme", "Bemessungsbasis relativ zu SV-Beschäftigten"),
        ("public_service_income_factor", PUBLIC_SERVICE_INCOME_FACTOR, "Arbeitsannahme", "Bemessungsbasis relativ zu SV-Beschäftigten; Proxy für Neubeamte und Dienstherrnbeiträge ab 2030"),
    ]
    ASSUMPTIONS_CSV.parent.mkdir(parents=True, exist_ok=True)
    with ASSUMPTIONS_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["parameter", "wert", "quelle", "notiz"])
        writer.writerows(rows)


def rows_by_key(rows: list[dict[str, str]]) -> dict[tuple[str, str, int], dict[str, str]]:
    return {
        (row["szenario"], row["variante"], int(row["jahr"])): row
        for row in rows
    }


def write_markdown(rows: list[dict[str, str]]) -> None:
    by_key = rows_by_key(rows)
    milestones = [2027, 2030, 2035, 2040, 2050, 2060, 2070]
    variants = [
        "status_quo_bund_anteilig",
        "reform_ohne_erweiterte_basis",
        "reform_mit_erwerbstaetigenbasis",
    ]

    lines = [
        "# Zukunftsmodell Rentenreform 2027-2070",
        "",
        "Stand: 2026-06-04",
        "",
        "Reproduzierbar mit:",
        "",
        "```bash",
        "python3 scripts/calc_rentenreform_zukunft.py",
        "```",
        "",
        "## Zweck",
        "",
        "Diese Analyse modelliert die Finanzierungswirkung des Reformprojekts",
        "Rentenversicherung bis 2070 und vergleicht Status quo, abschmelzende",
        "Bundesmittel und erweiterte Erwerbstätigenbasis. Die Jahre 2027 bis 2029",
        "sind interpolierte Brückenjahre; die Reform greift ab 1.1.2030.",
        "",
        "## Quellen und Ingests",
        "",
        "- `ingest/links/2026-06-04-drv-finanzkennzahlen-rentenversicherung.md`",
        "- `ingest/links/2026-06-04-destatis-bevoelkerungsvorausberechnung-16.md`",
        "- `ingest/links/2026-06-04-destatis-arbeitsmarkt-eckzahlen-2025.md`",
        "- `ingest/links/2026-06-04-destatis-oeffentlicher-dienst-2024.md`",
        "- `ingest/links/2026-06-04-bmas-rentenversicherungsbericht-2025.md`",
        "- `analysen/daten/2026-06-04-bundeszuschuss-abschmelzung.csv`",
        "",
        "## Modellcharakter",
        "",
        "Dieses v1-Modell ist ein Finanzierungsmodell, kein vollständiges",
        "versicherungsmathematisches Rentenzugangsmodell. Es zeigt, wie sich",
        "Beitragssätze verändern, wenn Ausgaben mit Demographie und Rentenanpassung",
        "wachsen, heutige Bundesmittel nur noch als Bestandsschutz abschmelzen und",
        "die Beitragsbasis durch eine Erwerbstätigenversicherung erweitert wird.",
        "",
        "Nicht quantifiziert sind in v1 Einsparungen aus künftig wegfallenden",
        "unbezahlten Rentenpunkten; diese Regel wirkt langfristig zusätzlich, braucht",
        "aber eine eigene Normen- und Volumenzerlegung.",
        "",
        "## Kernergebnis",
        "",
        "| Szenario | Jahr | Status quo: Beitragssatz | Reform ohne neue Basis | Reform mit Erwerbstätigenbasis | Reform-Zusatzbasis |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]

    for scenario in ["jung", "moderat", "alt"]:
        for year in milestones:
            status = Decimal(by_key[(scenario, variants[0], year)]["erforderlicher_beitragssatz"])
            no_base = Decimal(by_key[(scenario, variants[1], year)]["erforderlicher_beitragssatz"])
            reform = Decimal(by_key[(scenario, variants[2], year)]["erforderlicher_beitragssatz"])
            extra = Decimal(by_key[(scenario, variants[2], year)]["zusatzbasis_mrd_euro"])
            lines.append(
                f"| {scenario} | {year} | {pct(status)} % | {pct(no_base)} % | {pct(reform)} % | {de(extra, '0.1')} Mrd. Euro |"
            )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Bei anteilig fortgeschriebenen Bundesmitteln steigt der rechnerische Beitragssatz im moderaten Szenario bis 2070 auf rund "
            f"{pct(Decimal(by_key[('moderat', variants[0], 2070)]['erforderlicher_beitragssatz']))} %.",
            "- Die Jahre 2027 bis 2029 sind reine Brückenjahre der Modellierung; die Reformkomponenten starten erst 2030.",
            "- Wenn heutige Bundesmittel wie beschlossen nur mit dem Altbestand abschmelzen und keine neue Beitragsbasis entsteht, steigt der Finanzierungsdruck deutlich stärker.",
            "- Die Erwerbstätigenbasis dämpft den Beitragssatzanstieg, kompensiert den demographischen Druck aber in v1 nicht vollständig.",
            "- Neubeamte sind in v1 nur als Proxy fuer neue Dienstherrnbeiträge und späte Rentenansprüche modelliert; die kurzfristige Entlastung setzt ab 2030 ein und ist nicht dauerhaft.",
            "- Eine stabile Rente ist rechnerisch nur darstellbar, wenn Beitragssatz, echte staatliche Beiträge, Erwerbsbasis und Leistungsindexierung gemeinsam festgelegt werden.",
            "",
            "## Artefakte",
            "",
            f"- Jahreswerte: `{OUTPUT_CSV.relative_to(ROOT)}`",
            f"- Annahmen: `{ASSUMPTIONS_CSV.relative_to(ROOT)}`",
            "",
            "## Restunsicherheiten",
            "",
            "- Keine vollständige Neurentner-Kohortenrechnung.",
            "- Keine amtliche Zweckzerlegung der nicht beitragsgedeckten Leistungen.",
            "- Einkommen von Selbstständigen und Neubeamten nur als Bemessungsfaktor modelliert; die Beamten-Entlastung ist damit nur als Proxy abgebildet.",
            "- Sterblichkeitsverbesserungen nach 2022/2024 sind nicht enthalten.",
            "",
        ]
    )
    OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = build_rows()
    write_csv(OUTPUT_CSV, rows)
    write_assumptions()
    write_markdown(rows)


if __name__ == "__main__":
    main()
