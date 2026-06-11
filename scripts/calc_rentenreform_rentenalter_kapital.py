#!/usr/bin/env python3
"""Szenarien fuer Rentenalter-Kopplung und Kapitalmarktbaustein."""

from __future__ import annotations

import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import calc_rentenreform_zukunft as zukunft


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_CSV = ROOT / "analysen/daten/2026-06-05-rentenreform-rentenalter-kapital.csv"
ASSUMPTIONS_CSV = (
    ROOT / "analysen/daten/2026-06-05-rentenreform-rentenalter-kapital-annahmen.csv"
)
CAPITAL_CSV = (
    ROOT / "analysen/daten/2026-06-05-rentenreform-kapitalmarktbaustein.csv"
)
OUTPUT_MD = ROOT / "analysen/2026-06-05-rentenreform-rentenalter-kapitalmarkt.md"

BASE_RETIREMENT_AGE = Decimal("67")
COHORT_NEAR_RETIREMENT_M = Decimal("0.95")
AVERAGE_WAGE_2026 = Decimal("51944")
CAPITAL_CONTRIBUTION_RATES = [Decimal("0.01"), Decimal("0.02"), Decimal("0.03")]
REAL_RETURN_SCENARIOS = [Decimal("0.01"), Decimal("0.03"), Decimal("0.05")]
SAVING_YEARS = 40
PAYOUT_YEARS = 20

RETIREMENT_AGE_SCENARIOS = {
    "status_quo_67": {
        2027: Decimal("67"),
        2070: Decimal("67"),
    },
    "finnland_ratio_light": {
        2027: Decimal("67"),
        2035: Decimal("68"),
        2045: Decimal("69"),
        2055: Decimal("70"),
        2065: Decimal("71"),
        2070: Decimal("71"),
    },
    "daenemark_2040": {
        2027: Decimal("67"),
        2030: Decimal("68"),
        2035: Decimal("69"),
        2040: Decimal("70"),
        2055: Decimal("71"),
        2070: Decimal("72"),
    },
}

MILESTONES = [2030, 2035, 2039, 2040, 2050, 2060, 2070]


def q(value: Decimal, places: str = "0.001") -> Decimal:
    return value.quantize(Decimal(places), rounding=ROUND_HALF_UP)


def de(value: Decimal, places: str = "0.1") -> str:
    return str(q(value, places)).replace(".", ",")


def pct(value: Decimal) -> str:
    return de(value * Decimal("100"), "0.1")


def interpolate_schedule(schedule: dict[int, Decimal], year: int) -> Decimal:
    ordered = sorted(schedule.items())
    for (left_year, left_age), (right_year, right_age) in zip(ordered, ordered[1:]):
        if left_year <= year <= right_year:
            span = Decimal(right_year - left_year)
            offset = Decimal(year - left_year)
            return left_age + (right_age - left_age) * (offset / span)
    if year < ordered[0][0]:
        return ordered[0][1]
    return ordered[-1][1]


def adjusted_demography(points: list[zukunft.ScenarioPoint], year: int, retirement_age: Decimal) -> tuple[Decimal, Decimal, Decimal]:
    working_age = zukunft.interpolate(points, year, "working_age_m")
    old_age = zukunft.interpolate(points, year, "old_age_m")
    extra_years = max(retirement_age - BASE_RETIREMENT_AGE, Decimal("0"))
    shifted = min(extra_years * COHORT_NEAR_RETIREMENT_M, old_age * Decimal("0.30"))
    return working_age + shifted, old_age - shifted, shifted


def build_rows() -> list[dict[str, str]]:
    abschmelzung = zukunft.read_abschmelzung()
    calibration = zukunft.expense_calibration()
    rows: list[dict[str, str]] = []

    for scenario, points in zukunft.SCENARIOS.items():
        for year in range(zukunft.START_YEAR, zukunft.END_YEAR + 1):
            base_working = zukunft.interpolate(points, year, "working_age_m")
            base_old = zukunft.interpolate(points, year, "old_age_m")
            base_expenses = zukunft.projected_expenses(points, year) * calibration
            base_payroll = zukunft.projected_payroll(points, year) + zukunft.expanded_payroll(points, year)
            status_federal = base_expenses * (zukunft.BASE_FEDERAL_BN / zukunft.BASE_EXPENSES_BN)
            federal = zukunft.federal_support(year, status_federal, abschmelzung)
            other = zukunft.other_revenues(year)

            for age_scenario, schedule in RETIREMENT_AGE_SCENARIOS.items():
                retirement_age = interpolate_schedule(schedule, year)
                working, old, shifted = adjusted_demography(points, year, retirement_age)
                adjusted_expenses = base_expenses * (old / base_old)
                adjusted_payroll = base_payroll * (working / base_working)
                required_rate = (adjusted_expenses - federal - other) / adjusted_payroll
                rows.append(
                    {
                        "jahr": str(year),
                        "demographie_szenario": scenario,
                        "rentenalter_szenario": age_scenario,
                        "regelaltersgrenze": str(q(retirement_age, "0.001")),
                        "verschobene_kohorten_mio": str(q(shifted, "0.001")),
                        "personen_20_66_adj_mio": str(q(working, "0.001")),
                        "personen_ab_rentenalter_adj_mio": str(q(old, "0.001")),
                        "ausgaben_adj_mrd_euro": str(q(adjusted_expenses, "0.001")),
                        "beitragsbasis_reform_adj_mrd_euro": str(q(adjusted_payroll, "0.001")),
                        "bestandsschutz_zuschuss_mrd_euro": str(q(federal, "0.001")),
                        "sonstige_einnahmen_mrd_euro": str(q(other, "0.001")),
                        "erforderlicher_beitragssatz": str(q(required_rate, "0.000001")),
                        "notiz": "Screeningmodell: spaeteres Rentenalter verschiebt pauschal 0,95 Mio. Personen je Altersjahr von Renten- auf Beitragsseite.",
                    }
                )
    return rows


def future_value_annuity(payment: Decimal, return_rate: Decimal, years: int) -> Decimal:
    if return_rate == 0:
        return payment * Decimal(years)
    factor = ((Decimal("1") + return_rate) ** years - Decimal("1")) / return_rate
    return payment * factor


def payout_annuity(capital: Decimal, return_rate: Decimal, years: int) -> Decimal:
    if return_rate == 0:
        return capital / Decimal(years)
    return capital * return_rate / (Decimal("1") - (Decimal("1") + return_rate) ** Decimal(-years))


def build_capital_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for contribution_rate in CAPITAL_CONTRIBUTION_RATES:
        annual_payment = AVERAGE_WAGE_2026 * contribution_rate
        for return_rate in REAL_RETURN_SCENARIOS:
            capital = future_value_annuity(annual_payment, return_rate, SAVING_YEARS)
            annual_payout = payout_annuity(capital, return_rate, PAYOUT_YEARS)
            rows.append(
                {
                    "zusatzbeitragssatz": str(q(contribution_rate, "0.000001")),
                    "realrendite": str(q(return_rate, "0.000001")),
                    "jahresbeitrag_euro": str(q(annual_payment, "0.01")),
                    "ansparjahre": str(SAVING_YEARS),
                    "kapital_real_euro": str(q(capital, "0.01")),
                    "auszahlungsjahre": str(PAYOUT_YEARS),
                    "zusatzrente_jahr_real_euro": str(q(annual_payout, "0.01")),
                    "zusatzrente_monat_real_euro": str(q(annual_payout / Decimal("12"), "0.01")),
                    "notiz": "Individuelle Modellrechnung auf Basis Durchschnittsentgelt 2026; reale Werte vor Steuern/Abgaben, ohne Garantie.",
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
        ("rentenalter_status_quo", "67", "SGB VI / Modellabgrenzung", "Basisgrenze wie in den bisherigen Demographieartefakten 20-66 zu 67+."),
        ("kohorte_nahe_rentenalter_mio", COHORT_NEAR_RETIREMENT_M, "Arbeitsannahme", "Pauschale Groesse je verschobenem Altersjahr; ersetzt keine Altersjahr-Kohortenrechnung."),
        ("finnland_ratio_light", "68 ab 2035, 69 ab 2045, 70 ab 2055, 71 ab 2065", "Reformszenario nach finnischer Logik", "Stabilisiert grob das Verhaeltnis Erwerbs-/Rentenphase; Reformstart im Modell 2030."),
        ("daenemark_2040", "68 ab 2030, 69 ab 2035, 70 ab 2040, 72 bis 2070", "Reformszenario nach daenischer Logik", "Harte Vergleichsvariante, nicht als direkte Empfehlung zu lesen; im Modell ab 2030 wirksam."),
        ("kapitalmarkt_basis", AVERAGE_WAGE_2026, "BMAS Rechengroessen 2026", "Vorlaufiges Durchschnittsentgelt 2026."),
        ("kapitalmarkt_zusatzbeitraege", "1 %, 2 %, 3 %", "Arbeitsannahme", "Zusaetzlich zur Umlage, nicht als Umleitung bestehender Umlagebeitraege."),
        ("realrenditen", "1 %, 3 %, 5 %", "Sensitivitaet", "Reale Rendite vor Kosten-/Steuerdetails; Kapitalmarktrisiko bleibt beim System/Versicherten."),
    ]
    ASSUMPTIONS_CSV.parent.mkdir(parents=True, exist_ok=True)
    with ASSUMPTIONS_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["parameter", "wert", "quelle", "notiz"])
        writer.writerows(rows)


def by_key(rows: list[dict[str, str]]) -> dict[tuple[str, str, int], dict[str, str]]:
    return {
        (row["demographie_szenario"], row["rentenalter_szenario"], int(row["jahr"])): row
        for row in rows
    }


def capital_by_key(rows: list[dict[str, str]]) -> dict[tuple[str, str], dict[str, str]]:
    return {
        (row["zusatzbeitragssatz"], row["realrendite"]): row
        for row in rows
    }


def write_markdown(rows: list[dict[str, str]], capital_rows: list[dict[str, str]]) -> None:
    keyed = by_key(rows)
    cap_keyed = capital_by_key(capital_rows)
    lines = [
        "---",
        "title: Rentenreform Rentenalter-Kopplung und Kapitalmarktbaustein",
        "date: 2026-06-05",
        "type: analyse",
        "status: arbeitsfassung",
        "source_urls:",
        "  - https://www.pensionsmyndigheten.se/other-languages/english-engelska/english-engelska/retirement-age",
        "  - https://www.etk.fi/en/finnish-pension-system/pensions/determining-the-life-expectancy-coefficient-and-retirement-age/determining-the-retirement-age-for-the-old-age-pension/",
        "  - https://bm.dk/nyheder/pressemeddelelser/2025/05/forhoejelse-af-folkepensionsalderen-i-2040-sikrer-velfaerden",
        "  - https://star.dk/da/ydelser/pension-og-efterloen/folkepension-tidlig-pension-foertidspension-og-seniorpension/folkepension/folkepensionsalderen-nu-og-fremover/",
        "  - https://www.pensionsmyndigheten.se/forsta-din-pension/valj-och-byt-fonder/forvalet-ap7safa",
        "  - https://www.ap7.se/english/ap7-safa/",
        "  - https://www.msci.com/World",
        "  - https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/12/oecd-pensions-outlook-2024_6ac7d5fd/51510909-en.pdf",
        "ingest_refs:",
        "  - ingest/links/2026-06-05-schweden-richtalter-rente-lebenserwartung.md",
        "  - ingest/links/2026-06-05-finnland-rentenalter-lebenserwartung.md",
        "  - ingest/links/2026-06-05-daenemark-folkepensionsalter-lebenserwartung.md",
        "  - ingest/links/2026-06-05-schweden-ap7-safa-premium-pension.md",
        "  - ingest/links/2026-06-05-msci-world-index.md",
        "  - ingest/dokumente/2026-06-05-oecd-pensions-outlook-2024-kapitalmarkt-defaults.md",
        "data_artifacts:",
        "  - analysen/daten/2026-06-05-rentenreform-rentenalter-kapital.csv",
        "  - analysen/daten/2026-06-05-rentenreform-rentenalter-kapital-annahmen.csv",
        "  - analysen/daten/2026-06-05-rentenreform-kapitalmarktbaustein.csv",
        "scripts:",
        "  - scripts/calc_rentenreform_rentenalter_kapital.py",
        "related_projects:",
        "  - projekte/rentenversicherung/reformkonzept.md",
        "---",
        "",
        "# Rentenreform Rentenalter-Kopplung und Kapitalmarktbaustein",
        "",
        "Reproduzierbar mit:",
        "",
        "```bash",
        "python3 scripts/calc_rentenreform_rentenalter_kapital.py",
        "```",
        "",
        "## Zweck",
        "",
        "Diese Analyse ergaenzt das Reformkonzept um zwei Szenarien: spaeterer",
        "Renteneintritt durch Kopplung an die Lebenserwartung und ein zusaetzlicher",
        "kapitalgedeckter Baustein nach schwedisch inspiriertem Default-Modell.",
        "Die Modelljahre 2027 bis 2029 sind Brückenjahre; die Reform wirkt ab 1.1.2030.",
        "",
        "## Renteneintrittsalter-Szenarien",
        "",
        "| Szenario | Logik |",
        "| --- | --- |",
        "| status_quo_67 | Regelaltersgrenze bleibt modellhaft bei 67. |",
        "| finnland_ratio_light | Langsame Kopplung: 68 ab 2035, 69 ab 2045, 70 ab 2055, 71 ab 2065. |",
        "| daenemark_2040 | Harte Kopplung: 68 ab 2030, 69 ab 2035, 70 ab 2040, 72 bis 2070. |",
        "",
        "## Beitragssatzwirkung im moderaten Demographieszenario",
        "",
        "| Jahr | Status quo 67 | Finnland-nahe Kopplung | Daenemark-nahe Kopplung |",
        "| ---: | ---: | ---: | ---: |",
    ]
    for year in MILESTONES:
        values = []
        for scenario in RETIREMENT_AGE_SCENARIOS:
            row = keyed[("moderat", scenario, year)]
            values.append(pct(Decimal(row["erforderlicher_beitragssatz"])))
        lines.append(f"| {year} | {values[0]} % | {values[1]} % | {values[2]} % |")

    lines.extend(
        [
            "",
            "## Kapitalmarktbaustein",
            "",
            "Der Kapitalmarktbaustein wird als zusaetzlicher Beitrag gerechnet. Eine",
            "Umleitung bestehender Umlagebeitraege wuerde die heutige Rentenkasse",
            "zunaechst schwaechen und passt deshalb nicht zum Ziel stabiler",
            "Beitragssaetze.",
            "",
            "| Zusatzbeitrag | reale Rendite | Kapital nach 40 Jahren | Zusatzrente pro Monat, 20 Jahre |",
            "| ---: | ---: | ---: | ---: |",
        ]
    )
    for contribution_rate in [Decimal("0.01"), Decimal("0.02"), Decimal("0.03")]:
        for return_rate in REAL_RETURN_SCENARIOS:
            row = cap_keyed[(str(q(contribution_rate, "0.000001")), str(q(return_rate, "0.000001")))]
            lines.append(
                f"| {pct(contribution_rate)} % | {pct(return_rate)} % | "
                f"{de(Decimal(row['kapital_real_euro']), '0.01')} Euro | "
                f"{de(Decimal(row['zusatzrente_monat_real_euro']), '0.01')} Euro |"
            )

    lines.extend(
        [
            "",
            "## Einordnung",
            "",
            "- Eine Lebenserwartungs-Kopplung verbessert die Umlage deutlich, weil sie",
            "  gleichzeitig Ausgaben senkt und Beitragsjahre erhoeht. Sie ersetzt aber",
            "  keine breite Beitragsbasis und keine Budgetregel.",
            "- Eine daenemarknahe harte Kopplung wirkt staerker, ist aber sozial",
            "  konflikttraechtiger und braucht Schutzregeln fuer lange Versicherungszeiten",
            "  und gesundheitlich belastende Arbeit.",
            "- Ein Kapitalmarktbaustein kann individuelle Zusatzrente schaffen, muss aber",
            "  als Zusatzbeitrag, mit niedrigem Kostenlimit, breiter Streuung,",
            "  Lebenszyklus-Default und klarer Auszahlungsphase geregelt werden.",
            "- MSCI World ist eine moegliche Benchmark fuer entwickelte Maerkte, aber kein",
            "  Produkt. Fuer einen deutschen Default waere auch ein breiterer All-World-",
            "  Ansatz inklusive Schwellenlaender zu pruefen.",
            "",
        ]
    )
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = build_rows()
    capital_rows = build_capital_rows()
    write_csv(OUTPUT_CSV, rows)
    write_csv(CAPITAL_CSV, capital_rows)
    write_assumptions()
    write_markdown(rows, capital_rows)


if __name__ == "__main__":
    main()
