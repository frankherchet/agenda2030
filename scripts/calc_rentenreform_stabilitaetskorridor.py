#!/usr/bin/env python3
"""Berechnet leistbares Rentenvolumen bei stabilen Beitragssatz-Korridoren."""

from __future__ import annotations

import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import calc_rentenreform_zukunft as zukunft


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_CSV = (
    ROOT / "analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor.csv"
)
ASSUMPTIONS_CSV = (
    ROOT / "analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor-annahmen.csv"
)
OUTPUT_MD = ROOT / "analysen/2026-06-05-rentenreform-stabilitaetskorridor.md"

CONTRIBUTION_CAPS = {
    "ziel_20_prozent": Decimal("0.20"),
    "stabil_22_prozent": Decimal("0.22"),
    "obergrenze_24_prozent": Decimal("0.24"),
}

MILESTONES = [2027, 2030, 2035, 2039, 2040, 2050, 2060, 2070]


def q(value: Decimal, places: str = "0.001") -> Decimal:
    return value.quantize(Decimal(places), rounding=ROUND_HALF_UP)


def de(value: Decimal, places: str = "0.1") -> str:
    return str(q(value, places)).replace(".", ",")


def pct(value: Decimal) -> str:
    return de(value * Decimal("100"), "0.1")


def read_abschmelzung() -> dict[int, Decimal]:
    return zukunft.read_abschmelzung()


def build_rows() -> list[dict[str, str]]:
    abschmelzung = read_abschmelzung()
    rows: list[dict[str, str]] = []

    for scenario, points in zukunft.SCENARIOS.items():
        for year in range(zukunft.START_YEAR, zukunft.END_YEAR + 1):
            reference_expenses = zukunft.projected_expenses(points, year) * zukunft.expense_calibration()
            payroll_base = zukunft.projected_payroll(points, year)
            payroll_extra = zukunft.expanded_payroll(points, year)
            payroll_total = payroll_base + payroll_extra
            status_federal = reference_expenses * (zukunft.BASE_FEDERAL_BN / zukunft.BASE_EXPENSES_BN)
            legacy_federal = zukunft.federal_support(year, status_federal, abschmelzung)
            other = zukunft.other_revenues(year)

            for corridor, cap in CONTRIBUTION_CAPS.items():
                contribution_revenue = payroll_total * cap
                affordable_expenses = contribution_revenue + legacy_federal + other
                gap = reference_expenses - affordable_expenses
                leistungsfaktor = affordable_expenses / reference_expenses
                rows.append(
                    {
                        "jahr": str(year),
                        "szenario": scenario,
                        "korridor": corridor,
                        "beitragssatz_obergrenze": str(q(cap, "0.000001")),
                        "referenzausgaben_mrd_euro": str(q(reference_expenses, "0.001")),
                        "beitragsbasis_status_quo_mrd_euro": str(q(payroll_base, "0.001")),
                        "zusatzbasis_erwerbstaetige_mrd_euro": str(q(payroll_extra, "0.001")),
                        "beitragsbasis_reform_mrd_euro": str(q(payroll_total, "0.001")),
                        "beitragseinnahmen_mrd_euro": str(q(contribution_revenue, "0.001")),
                        "bestandsschutz_zuschuss_mrd_euro": str(q(legacy_federal, "0.001")),
                        "sonstige_einnahmen_mrd_euro": str(q(other, "0.001")),
                        "leistbares_ausgabenvolumen_mrd_euro": str(q(affordable_expenses, "0.001")),
                        "finanzierungsluecke_vs_referenz_mrd_euro": str(q(gap, "0.001")),
                        "leistungsfaktor_vs_referenz": str(q(leistungsfaktor, "0.000001")),
                        "notiz": (
                            "Maximal leistbares Rentenvolumen bei stabiler "
                            "Beitragssatz-Obergrenze, Erwerbstaetigenbasis und "
                            "abschmelzendem Bestandsschutz-Zuschuss."
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
        ("modell", "Stabilitaetskorridor", "Arbeitsmodell", "Berechnet das maximal finanzierbare Ausgabenvolumen bei fixen Beitragssatz-Obergrenzen."),
        ("beitragssatz_korridore", "20 %, 22 %, 24 %", "Politische Arbeitsannahme", "20 % Zielkorridor, 22 % Stabilitaetskorridor, 24 % harte Obergrenze."),
        ("beitragsbasis", "Status quo plus Erwerbstaetigenbasis", "scripts/calc_rentenreform_zukunft.py", "Selbststaendige und Neubeamte beziehungsweise neue Dienstherrenbeiträge werden ab 2030 schrittweise einbezogen."),
        ("bestandsschutz_zuschuss", "ab 2030 abschmelzend", "analysen/daten/2026-06-04-bundeszuschuss-abschmelzung.csv", "Altzuschuss bleibt 2027-2029 als Brückenphase erhalten und sinkt ab 2030 proportional zum Bestandsrentner-Modell."),
        ("referenzausgaben", "Status quo Ausgabenpfad", "scripts/calc_rentenreform_zukunft.py", "Ausgaben mit Demographie und Rentenanpassung, auf 2027 kalibriert; 2027-2029 sind Brückenjahre."),
        ("leistungsfaktor", "leistbares Ausgabenvolumen / Referenzausgaben", "Formel", "Wert 1,0 bedeutet Referenzpfad voll finanzierbar; darunter muss Rentenwert/Leistungsindexierung gedämpft oder externe Finanzierung geschaffen werden."),
    ]
    ASSUMPTIONS_CSV.parent.mkdir(parents=True, exist_ok=True)
    with ASSUMPTIONS_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["parameter", "wert", "quelle", "notiz"])
        writer.writerows(rows)


def by_key(rows: list[dict[str, str]]) -> dict[tuple[str, str, int], dict[str, str]]:
    return {
        (row["szenario"], row["korridor"], int(row["jahr"])): row
        for row in rows
    }


def write_markdown(rows: list[dict[str, str]]) -> None:
    keyed = by_key(rows)
    lines = [
        "---",
        "title: Rentenreform Stabilitaetskorridor",
        "date: 2026-06-05",
        "type: analyse",
        "status: arbeitsfassung",
        "source_urls:",
        "  - https://www.deutsche-rentenversicherung.de/DRV/DE/Experten/Zahlen-und-Fakten/Kennzahlen-zur-Finanzentwicklung/kennzahlen-zur-finanzentwicklung_node.html?https=1",
        "  - https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsvorausberechnung/annahmen_ergebnisse_16te_kBv.html",
        "  - https://www.bmas.de/SharedDocs/Downloads/DE/Rente/rentenversicherungsbericht-2025.pdf?__blob=publicationFile&v=3",
        "ingest_refs:",
        "  - ingest/links/2026-06-04-drv-finanzkennzahlen-rentenversicherung.md",
        "  - ingest/dokumente/2026-06-04-destatis-demographie.md",
        "  - ingest/dokumente/2026-06-05-bmas-rentenversicherungsbericht-2025.md",
        "data_artifacts:",
        "  - analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor.csv",
        "  - analysen/daten/2026-06-05-rentenreform-stabilitaetskorridor-annahmen.csv",
        "scripts:",
        "  - scripts/calc_rentenreform_stabilitaetskorridor.py",
        "related_projects:",
        "  - projekte/rentenversicherung/reformkonzept.md",
        "---",
        "",
        "# Rentenreform Stabilitaetskorridor",
        "",
        "Reproduzierbar mit:",
        "",
        "```bash",
        "python3 scripts/calc_rentenreform_stabilitaetskorridor.py",
        "```",
        "",
        "## Zweck",
        "",
        "Diese Analyse berechnet, wie viel Rentenvolumen maximal finanzierbar ist,",
        "wenn die Reform rein umlagefinanziert bleibt, neue Entgeltpunkte nur aus",
        "Einzahlungen entstehen und der Beitragssatz politisch stabil gehalten",
        "werden soll.",
        "",
        "## Modell",
        "",
        "- Beitragsbasis: Status quo plus schrittweise Erwerbstätigenbasis aus dem",
        "  bestehenden Zukunftsmodell; Neubeamte wirken darin ab 2030 als zusätzliche Beitragsbasis und spätere Rentenlast.",
        "- Bundesmittel: 2027-2029 Brückenphase, danach abschmelzender Bestandsschutz-Zuschuss für Altlasten.",
        "- Beitragssatz-Korridore: 20 %, 22 % und 24 %.",
        "- Leistungsfaktor: maximal finanzierbares Ausgabenvolumen geteilt durch",
        "  Referenzausgaben des bisherigen Rentenpfads.",
        "- Brückenjahre 2027-2029 sind modelliert, aber noch nicht reformwirksam.",
        "",
        "## Kernergebnis moderate Variante",
        "",
        "| Korridor | Jahr | leistbares Volumen | Referenzausgaben | Leistungsfaktor | Luecke vs. Referenz |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]

    for corridor in CONTRIBUTION_CAPS:
        for year in [2030, 2035, 2039, 2050, 2070]:
            row = keyed[("moderat", corridor, year)]
            lines.append(
                "| "
                f"{corridor} | {year} | "
                f"{de(Decimal(row['leistbares_ausgabenvolumen_mrd_euro']))} Mrd. Euro | "
                f"{de(Decimal(row['referenzausgaben_mrd_euro']))} Mrd. Euro | "
                f"{pct(Decimal(row['leistungsfaktor_vs_referenz']))} % | "
                f"{de(Decimal(row['finanzierungsluecke_vs_referenz_mrd_euro']))} Mrd. Euro |"
            )

    lines.extend(
        [
            "",
            "## Szenariovergleich 2070",
            "",
            "| Szenario | 20 % | 22 % | 24 % |",
            "| --- | ---: | ---: | ---: |",
        ]
    )

    for scenario in ["jung", "moderat", "alt"]:
        values = []
        for corridor in CONTRIBUTION_CAPS:
            row = keyed[(scenario, corridor, 2070)]
            values.append(f"{pct(Decimal(row['leistungsfaktor_vs_referenz']))} %")
        lines.append(f"| {scenario} | {values[0]} | {values[1]} | {values[2]} |")

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Im moderaten Szenario finanziert ein 22-%-Korridor 2035 rund 89 %",
            "des Referenzpfads, 2039 rund 80 %, 2050 rund 75 % und 2070 rund",
            "72 %. Ein 24-%-Korridor verbessert die Lage, reicht aber 2070 im",
            "moderaten Szenario nur für rund 78 % des Referenzpfads.",
            "",
            "Folgerung für das Reformkonzept: Eine hohe Rente bei stabilen",
            "Beitragssätzen braucht eine automatische Budgetregel. Innerhalb des",
            "Beitragssatzkorridors wird der Rentenwert so hoch wie möglich gesetzt;",
            "neue Entgeltpunkte entstehen nur durch Beiträge. Politische",
            "Rentenwirkungen müssen durch echte Beiträge öffentlicher Träger",
            "finanziert werden und dürfen den Korridor nicht verdeckt belasten.",
            "",
        ]
    )
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = build_rows()
    write_csv(OUTPUT_CSV, rows)
    write_assumptions()
    write_markdown(rows)


if __name__ == "__main__":
    main()
