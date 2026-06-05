#!/usr/bin/env python3
"""Rechenartefakte zur Bearbeitung der Rentenreform-Freigabeblocker."""

from __future__ import annotations

import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import calc_rentenreform_zukunft as zukunft


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_CSV = ROOT / "analysen/daten/2026-06-06-rentenreform-freigabeblocker.csv"
AGE_DETAIL_CSV = (
    ROOT / "analysen/daten/2026-06-06-rentenalter-feinmodell-altersjahre.csv"
)
STATE_CSV = ROOT / "analysen/daten/2026-06-06-staatsbeitraege-rentenreform.csv"
ASSUMPTIONS_CSV = (
    ROOT / "analysen/daten/2026-06-06-rentenreform-freigabeblocker-annahmen.csv"
)
OUTPUT_MD = ROOT / "analysen/2026-06-06-rentenreform-freigabeblocker.md"

BASE_RETIREMENT_AGE = Decimal("67")
BASE_NEAR_RETIREMENT_COHORT_M = Decimal("0.95")
SENIOR_WAGE_FACTOR = Decimal("0.85")
AVERAGE_WAGE_2026 = Decimal("51944")
CONTRIBUTION_RATE_2026 = Decimal("0.186")
LIVE_BIRTHS_2024 = Decimal("677117")
CARE_PERSONS_M = Decimal("1.10")
CARE_MONTHLY_LOW = Decimal("747.50")
CARE_MONTHLY_HIGH = Decimal("3955.00")
BA_CONTRIBUTIONS_2025_BN = Decimal("5.82633")
PUBLIC_SERVICE_REIMBURSEMENTS_2025_BN = Decimal("1.38149")

CORRIDORS = {
    "ziel_20_prozent": Decimal("0.20"),
    "stabil_22_prozent": Decimal("0.22"),
    "obergrenze_24_prozent": Decimal("0.24"),
}

RETIREMENT_AGE_SCENARIOS = {
    "status_quo_67": {
        2027: Decimal("67"),
        2070: Decimal("67"),
    },
    "lebenserwartung_gekoppelt_2zu1": {
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

SENIOR_EMPLOYMENT_RATES = {
    67: Decimal("0.20"),
    68: Decimal("0.14"),
    69: Decimal("0.10"),
    70: Decimal("0.07"),
    71: Decimal("0.05"),
    72: Decimal("0.04"),
}

MILESTONES = [2035, 2039, 2050, 2070]


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


def senior_age_rows(
    old_age_m: Decimal,
    retirement_age: Decimal,
    payroll_per_million: Decimal,
) -> tuple[list[dict[str, str]], Decimal, Decimal]:
    cohort_m = BASE_NEAR_RETIREMENT_COHORT_M * (old_age_m / zukunft.BASE_OLD_AGE_M)
    detail: list[dict[str, str]] = []
    removed_pensioners = Decimal("0")
    added_effective_workers = Decimal("0")

    for age in range(67, 73):
        active_fraction = max(Decimal("0"), min(Decimal("1"), retirement_age - Decimal(age)))
        employment_rate = SENIOR_EMPLOYMENT_RATES[age]
        cohort_active_m = cohort_m * active_fraction
        effective_workers_m = cohort_active_m * employment_rate * SENIOR_WAGE_FACTOR
        removed_pensioners += cohort_active_m
        added_effective_workers += effective_workers_m
        detail.append(
            {
                "alter": str(age),
                "synthetische_kohorte_mio": str(q(cohort_m, "0.001")),
                "nicht_in_rente_anteil": str(q(active_fraction, "0.001")),
                "nicht_in_rente_mio": str(q(cohort_active_m, "0.001")),
                "erwerbsquote": str(q(employment_rate, "0.001")),
                "effektive_beitragszahler_mio": str(q(effective_workers_m, "0.001")),
                "zusatz_beitragsbasis_mrd_euro": str(q(effective_workers_m * payroll_per_million, "0.001")),
            }
        )

    return detail, removed_pensioners, added_effective_workers * payroll_per_million


def state_contribution_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    child_base = (
        LIVE_BIRTHS_2024
        * Decimal("3")
        * AVERAGE_WAGE_2026
        * CONTRIBUTION_RATE_2026
        / Decimal("1000000000")
    )
    care_mid_annual = ((CARE_MONTHLY_LOW + CARE_MONTHLY_HIGH) / Decimal("2")) * Decimal("12")
    care_base = CARE_PERSONS_M * Decimal("1000000") * care_mid_annual * CONTRIBUTION_RATE_2026 / Decimal("1000000000")
    base_rows = [
        (
            "kindererziehungszeiten",
            child_base,
            "Bund",
            "677.117 Geburten 2024 x 3 Jahre x Durchschnittsentgelt 2026 x 18,6 %",
        ),
        (
            "pflegezeiten",
            care_base,
            "Pflegeversicherung",
            "1,1 Mio. Pflegepersonen x mittlere BMG-Bemessungsspanne 2026 x 18,6 %",
        ),
        (
            "ba_leistungsempfaenger",
            BA_CONTRIBUTIONS_2025_BN,
            "Bundesagentur fuer Arbeit",
            "DRV-Rechnungsergebnisse 2025: Pflichtbeitraege fuer BA-Leistungsempfaenger",
        ),
        (
            "versorgungsdienststellen",
            PUBLIC_SERVICE_REIMBURSEMENTS_2025_BN,
            "Versorgungsdienststellen",
            "DRV-Rechnungsergebnisse 2025: Erstattungen von Versorgungsdienststellen",
        ),
    ]
    for year in range(zukunft.START_YEAR, zukunft.END_YEAR + 1):
        wage_factor = (Decimal("1") + zukunft.NOMINAL_WAGE_GROWTH) ** Decimal(max(0, year - 2026))
        for category, base, payer, note in base_rows:
            amount = base * wage_factor
            rows.append(
                {
                    "jahr": str(year),
                    "kategorie": category,
                    "zahlungspflichtiger": payer,
                    "betrag_mrd_euro": str(q(amount, "0.001")),
                    "notiz": note,
                }
            )
    return rows


def build_rows() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    abschmelzung = zukunft.read_abschmelzung()
    calibration = zukunft.expense_calibration()
    rows: list[dict[str, str]] = []
    age_details: list[dict[str, str]] = []

    for scenario, points in zukunft.SCENARIOS.items():
        for year in range(zukunft.START_YEAR, zukunft.END_YEAR + 1):
            base_working = zukunft.interpolate(points, year, "working_age_m")
            base_old = zukunft.interpolate(points, year, "old_age_m")
            base_expenses = zukunft.projected_expenses(points, year) * calibration
            base_payroll = zukunft.projected_payroll(points, year) + zukunft.expanded_payroll(points, year)
            payroll_per_million = base_payroll / base_working
            federal = abschmelzung[year]
            other = zukunft.other_revenues(year)

            for age_scenario, schedule in RETIREMENT_AGE_SCENARIOS.items():
                retirement_age = interpolate_schedule(schedule, year)
                detail, removed_pensioners, added_payroll = senior_age_rows(
                    base_old,
                    retirement_age,
                    payroll_per_million,
                )
                old_adjusted = max(Decimal("0.001"), base_old - removed_pensioners)
                expenses_adjusted = base_expenses * (old_adjusted / base_old)
                payroll_adjusted = base_payroll + added_payroll

                for detail_row in detail:
                    age_details.append(
                        {
                            "jahr": str(year),
                            "demographie_szenario": scenario,
                            "rentenalter_szenario": age_scenario,
                            "regelaltersgrenze": str(q(retirement_age, "0.001")),
                            **detail_row,
                        }
                    )

                for corridor_name, corridor_rate in CORRIDORS.items():
                    available_budget = payroll_adjusted * corridor_rate + federal + other
                    raw_factor = available_budget / expenses_adjusted
                    rent_value_factor = min(Decimal("1"), raw_factor)
                    reserve_or_gap = available_budget - expenses_adjusted
                    rows.append(
                        {
                            "jahr": str(year),
                            "demographie_szenario": scenario,
                            "rentenalter_szenario": age_scenario,
                            "korridor": corridor_name,
                            "beitragssatz": str(q(corridor_rate, "0.000001")),
                            "regelaltersgrenze": str(q(retirement_age, "0.001")),
                            "entlastete_rentner_mio": str(q(removed_pensioners, "0.001")),
                            "zusatz_beitragsbasis_mrd_euro": str(q(added_payroll, "0.001")),
                            "referenzausgaben_adj_mrd_euro": str(q(expenses_adjusted, "0.001")),
                            "beitragsbasis_adj_mrd_euro": str(q(payroll_adjusted, "0.001")),
                            "bestandsschutz_zuschuss_mrd_euro": str(q(federal, "0.001")),
                            "sonstige_einnahmen_mrd_euro": str(q(other, "0.001")),
                            "leistbares_budget_mrd_euro": str(q(available_budget, "0.001")),
                            "budgetsaldo_vs_referenz_mrd_euro": str(q(reserve_or_gap, "0.001")),
                            "rentenwert_budgetfaktor": str(q(rent_value_factor, "0.000001")),
                            "notiz": "Formel: Rentenwertfaktor = min(1, (Beitragsbasis x Korridor + Bestandsschutz + sonstige Einnahmen) / Referenzausgaben).",
                        }
                    )
    return rows, age_details


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_assumptions() -> None:
    rows = [
        ("rentenwert_budgetformel", "min(1, Budget / Referenzausgaben)", "Reformformel", "Nominale Schutz- und Übergangsklauseln bleiben gesetzlich auszuformulieren."),
        ("budget", "Beitragsbasis x Beitragssatzkorridor + Bestandsschutz-Zuschuss + sonstige Einnahmen", "Reformformel", "Echte Staatsbeiträge werden separat ausgewiesen; finale Zahlungsströme dürfen nicht doppelt gezählt werden."),
        ("senior_wage_factor", SENIOR_WAGE_FACTOR, "Arbeitsannahme", "Personen oberhalb 67 werden mit 85 % der durchschnittlichen Beitragsbasis je Erwerbsalter-Person angesetzt."),
        ("senior_employment_rates", "67:20 %, 68:14 %, 69:10 %, 70:7 %, 71:5 %, 72:4 %", "Arbeitsannahme", "Ersetzt die bisherige pauschale Vollverschiebung durch altersjahrspezifische Erwerbsquoten."),
        ("near_retirement_cohort", BASE_NEAR_RETIREMENT_COHORT_M, "Arbeitsannahme", "Synthetische Altersjahr-Kohorte, skaliert mit der Entwicklung der 67+-Population."),
        ("live_births_2024", LIVE_BIRTHS_2024, "Destatis", "Basis für Kindererziehungszeiten."),
        ("care_persons", "1,10 Mio.", "DRV", "Rund 1,1 Mio. rentenversicherte Pflegepersonen."),
        ("care_assessment_base", f"{CARE_MONTHLY_LOW} bis {CARE_MONTHLY_HIGH} Euro monatlich", "BMG", "Modell nutzt den Mittelwert der 2026 genannten Spanne."),
    ]
    ASSUMPTIONS_CSV.parent.mkdir(parents=True, exist_ok=True)
    with ASSUMPTIONS_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["parameter", "wert", "quelle", "notiz"])
        writer.writerows(rows)


def pick(rows: list[dict[str, str]], year: int, age_scenario: str, corridor: str) -> dict[str, str]:
    return next(
        row
        for row in rows
        if row["jahr"] == str(year)
        and row["demographie_szenario"] == "moderat"
        and row["rentenalter_szenario"] == age_scenario
        and row["korridor"] == corridor
    )


def state_total(state_rows: list[dict[str, str]], year: int) -> Decimal:
    return sum(
        Decimal(row["betrag_mrd_euro"])
        for row in state_rows
        if row["jahr"] == str(year)
    )


def write_markdown(rows: list[dict[str, str]], state_rows: list[dict[str, str]]) -> None:
    lines = [
        "---",
        "title: Rentenreform Freigabeblocker - Nachbesserung",
        "date: 2026-06-06",
        "type: analyse",
        "status: arbeitsfassung",
        "publish: false",
        "source_urls:",
        "  - https://www.gesetze-im-internet.de/sgb_6/",
        "  - https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Geburten/Tabellen/lebendgeborene-geschlecht.html",
        "  - https://www.deutsche-rentenversicherung.de/DRV/DE/Ueber-uns-und-Presse/Presse/Meldungen/2025/251111-kindererziehungszeiten-vaeter",
        "  - https://www.bundesgesundheitsministerium.de/themen/pflege/online-ratgeber-pflege/leistungen-der-pflegeversicherung/leistungen-im-ueberblick/soziale-absicherung-fuer-pflegepersonen",
        "  - https://www.deutsche-rentenversicherung.de/DRV/DE/Ueber-uns-und-Presse/Presse/Pressemitteilungen/Pressemitteilungen-archiv/2025/2025-05-09-pflege-von-angehoerigen.html",
        "ingest_refs:",
        "  - ingest/links/2026-06-04-gesetze-im-internet-sgb-vi.md",
        "  - ingest/links/2026-06-06-destatis-lebendgeborene-2024.md",
        "  - ingest/links/2026-06-06-drv-kindererziehungszeiten-bund.md",
        "  - ingest/links/2026-06-06-bmg-soziale-absicherung-pflegepersonen.md",
        "  - ingest/links/2026-06-06-drv-pflegepersonen-rentenversicherung.md",
        "data_artifacts:",
        f"  - {OUTPUT_CSV.relative_to(ROOT)}",
        f"  - {AGE_DETAIL_CSV.relative_to(ROOT)}",
        f"  - {STATE_CSV.relative_to(ROOT)}",
        f"  - {ASSUMPTIONS_CSV.relative_to(ROOT)}",
        "scripts:",
        "  - scripts/calc_rentenreform_freigabeblocker.py",
        "related_projects:",
        "  - projekte/rentenversicherung/reformkonzept.md",
        "---",
        "",
        "# Rentenreform Freigabeblocker - Nachbesserung",
        "",
        "## Kurzfassung",
        "",
        "Diese Nachbesserung bearbeitet die im Prüferbericht vom 2026-06-05",
        "benannten Freigabeblocker. Sie ersetzt die vorherige pauschale",
        "Rentenalter-Verschiebung durch ein synthetisches Altersjahrmodell,",
        "formuliert eine konkrete Rentenwert-Budgetregel und quantifiziert die",
        "auszuweisenden echten öffentlichen Beitragszahlungen für zentrale",
        "Sozialzeiten. Sie ist noch keine Prüferfreigabe.",
        "",
        "## Rentenwertformel",
        "",
        "Die Reformformel lautet als Arbeitsfassung:",
        "",
        "```text",
        "Budget_t = Beitragsbasis_t x Beitragssatzkorridor_t",
        "         + Bestandsschutz-Zuschuss_t",
        "         + sonstige Einnahmen_t",
        "",
        "Rentenwert-Budgetfaktor_t = min(1, Budget_t / Referenzausgaben_t)",
        "",
        "Aktueller Rentenwert_t = Referenz-Rentenwert_t x Rentenwert-Budgetfaktor_t",
        "```",
        "",
        "Ein Faktor unter 1 bedeutet eine Dämpfung gegenüber dem fortgeschriebenen",
        "Referenzpfad, nicht automatisch eine nominale Kürzung. Nominalschutz,",
        "Nachholfaktor und Übergangspfad müssen in einer Gesetzesskizze separat",
        "ausformuliert werden.",
        "",
        "## Feineres Rentenaltermodell",
        "",
        "Statt 0,95 Mio. Personen je zusätzlichem Rentenalterjahr vollständig von",
        "der Renten- auf die Beitragsseite zu verschieben, bildet das Modell die",
        "Altersjahre 67 bis 72 einzeln ab. Für jedes Altersjahr wird eine",
        "synthetische Kohorte gebildet, mit altersspezifischer Erwerbsquote und",
        "einem Senior-Wage-Faktor von 85 % bewertet.",
        "",
        "| Jahr | Szenario | Korridor | Rentenwert-Budgetfaktor | Budgetsaldo vs. Referenz |",
        "| ---: | --- | --- | ---: | ---: |",
    ]
    for year in MILESTONES:
        for scenario in ["status_quo_67", "lebenserwartung_gekoppelt_2zu1", "daenemarknah"]:
            row = pick(rows, year, scenario, "stabil_22_prozent")
            lines.append(
                f"| {year} | {scenario} | 22 % | "
                f"{pct(Decimal(row['rentenwert_budgetfaktor']))} % | "
                f"{de(Decimal(row['budgetsaldo_vs_referenz_mrd_euro']), '0.1')} Mrd. Euro |"
            )
    lines.extend(
        [
            "",
            "Interpretation: Die Lebenserwartungs-Kopplung entlastet weiterhin stark,",
            "aber weniger optimistisch als die erste Screeningrechnung, weil ältere",
            "zusätzliche Erwerbsjahre nur teilweise als Beitragsjahre wirken.",
            "",
            "## Echte öffentliche Beitragszahlungen",
            "",
            "Die folgende Tabelle ist keine zusätzliche Einnahmeannahme für die",
            "Rentenversicherung, sondern eine Transparenzrechnung: rentenwirksame",
            "Sozialzeiten müssen als echte Zahlung des zuständigen Trägers sichtbar",
            "werden und dürfen nicht als kostenloser Entgeltpunkt erscheinen.",
            "",
            "| Jahr | Auszuweisende öffentliche Beiträge |",
            "| ---: | ---: |",
        ]
    )
    for year in MILESTONES:
        lines.append(f"| {year} | {de(state_total(state_rows, year), '0.1')} Mrd. Euro |")
    lines.extend(
        [
            "",
            "Enthalten sind modellhaft Kindererziehungszeiten, Pflegezeiten,",
            "BA-Leistungsempfänger und Erstattungen von Versorgungsdienststellen.",
            "Die Beträge wachsen nominal mit 2,5 % pro Jahr. Für eine finale",
            "Haushaltsfreigabe müssen Ist-Zahlungen und neue Reformzahlungen",
            "doppelfrei gegen die DRV-Finanzrechnung abgegrenzt werden.",
            "",
            "## Bundesmittel-Zweckzerlegung",
            "",
            "Der bisherige Freigabeblocker kann fachlich nur teilweise behoben werden:",
            "Eine öffentliche amtliche Zweckzerlegung für 2024 bis 2026 liegt nach",
            "den bereits ingested Quellen nicht vor. Die Reform trennt deshalb",
            "künftig normativ zwischen Bestandsschutz-Zuschuss, echten",
            "Staatsbeiträgen und Steuertransfers. Das ist eine belastbarere",
            "Reformklassifikation, ersetzt aber keine amtliche rückwirkende",
            "Zweckzerlegung.",
            "",
            "## Prüffähige Folgepunkte",
            "",
            "- Normstände für Altersgrenzen und Zugangsfaktor wurden separat angelegt.",
            "- Rentenwertformel ist nun konkret genug für eine Gesetzesskizze.",
            "- Rentenaltermodell ist feiner, aber weiter synthetisch und braucht",
            "  echte feinjährige Bevölkerung, Erwerbsquoten und Rentenzugangsdaten.",
            "- Staatsbeiträge sind als Größenordnung quantifiziert; die finale",
            "  Haushaltsrechnung muss doppelfrei aus Ist-Daten abgeleitet werden.",
        ]
    )
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows, age_details = build_rows()
    state_rows = state_contribution_rows()
    write_csv(OUTPUT_CSV, rows)
    write_csv(AGE_DETAIL_CSV, age_details)
    write_csv(STATE_CSV, state_rows)
    write_assumptions()
    write_markdown(rows, state_rows)


if __name__ == "__main__":
    main()
