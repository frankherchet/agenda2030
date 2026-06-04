#!/usr/bin/env python3
"""Erzeugt DRV-Inputdaten fuer das Renten-Abschmelzmodell."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BESTAND_CSV = ROOT / "rentenversicherung/daten/2026-06-04-drv-rentenbestand-struktur.csv"
BUNDESMITTEL_CSV = ROOT / "rentenversicherung/daten/2026-06-04-bundesmittel-zerlegung.csv"
SUMMARY_MD = ROOT / "rentenversicherung/auswertungen/2026-06-04-drv-rentenbestand-inputs.md"

SOURCE = "DRV Statistikband Rente 2024, Rentenbestand am 31.12.2024"
STICHTAG = "2024-12-31"


EM_MALE = [
    ("unter 20", 19, 19, 4),
    ("20 - 24", 20, 24, 424),
    ("25 - 29", 25, 29, 2616),
    ("30 - 34", 30, 34, 7405),
    ("35 - 39", 35, 39, 20183),
    ("40 - 44", 40, 44, 43739),
    ("45 - 49", 45, 49, 60414),
    ("50 - 54", 50, 54, 97275),
    ("55 - 59", 55, 59, 189268),
    ("60 und älter", 60, 66, 360565),
]

EM_FEMALE = [
    ("unter 20", 19, 19, 3),
    ("20 - 24", 20, 24, 402),
    ("25 - 29", 25, 29, 2946),
    ("30 - 34", 30, 34, 9458),
    ("35 - 39", 35, 39, 25014),
    ("40 - 44", 40, 44, 51829),
    ("45 - 49", 45, 49, 76976),
    ("50 - 54", 50, 54, 128554),
    ("55 - 59", 55, 59, 244059),
    ("60 und älter", 60, 66, 426268),
]

OLD_AGE_MALE = {
    61: 2383,
    62: 13527,
    63: 71733,
    64: 186488,
    65: 283591,
    66: 468899,
    67: 486570,
    68: 469497,
    69: 449345,
    70: 432754,
    71: 410649,
    72: 403230,
    73: 388869,
    74: 381962,
    75: 363181,
    76: 327905,
    77: 301379,
    78: 256113,
    79: 215935,
    80: 269855,
    81: 262187,
    82: 243211,
    83: 273278,
    84: 265234,
    85: 237811,
    86: 199038,
    87: 165100,
    88: 137223,
    89: 111365,
    90: 84806,
    91: 54745,
    92: 41952,
    93: 32226,
    94: 24843,
    95: 16766,
    96: 11384,
    97: 7004,
    98: 4238,
    99: 2498,
    100: 3021,
}

OLD_AGE_FEMALE = {
    61: 631,
    62: 11801,
    63: 93818,
    64: 198520,
    65: 283443,
    66: 511244,
    67: 534630,
    68: 520648,
    69: 505064,
    70: 497961,
    71: 482278,
    72: 479094,
    73: 466274,
    74: 461469,
    75: 439874,
    76: 395570,
    77: 367258,
    78: 313328,
    79: 270525,
    80: 348106,
    81: 342725,
    82: 320838,
    83: 375380,
    84: 377526,
    85: 350896,
    86: 303756,
    87: 260392,
    88: 227285,
    89: 193721,
    90: 156439,
    91: 105853,
    92: 87290,
    93: 72458,
    94: 60467,
    95: 44194,
    96: 32549,
    97: 22533,
    98: 15600,
    99: 10718,
    100: 15464,
}

DEATH_ROWS = [
    ("unter 20", 0, 19, 0, 0, 0, 0, 167765, 2303, 0),
    ("20 bis 24", 20, 24, 3, 9, 0, 0, 73312, 1792, 0),
    ("25 bis 29", 25, 29, 32, 227, 10, 20, 21494, 794, 5),
    ("30 bis 34", 30, 34, 91, 1258, 32, 160, 0, 0, 118),
    ("35 bis 39", 35, 39, 188, 4393, 82, 717, 0, 2, 576),
    ("40 bis 44", 40, 44, 604, 9438, 93, 1501, 0, 0, 1442),
    ("45 bis 49", 45, 49, 310, 22204, 39, 3292, 1, 0, 1914),
    ("50 bis 54", 50, 54, 0, 51202, 0, 8157, 0, 0, 1427),
    ("55 bis 59", 55, 59, 0, 119039, 0, 20066, 0, 0, 755),
    ("60 bis 64", 60, 64, 0, 238466, 0, 42346, 2, 0, 329),
    ("65 bis 69", 65, 69, 0, 384883, 0, 74113, 4, 0, 30),
    ("70 bis 74", 70, 74, 0, 565035, 0, 103952, 8, 0, 0),
    ("75 bis 79", 75, 79, 0, 647331, 0, 111569, 5, 0, 0),
    ("80 bis 84", 80, 84, 0, 899634, 0, 157776, 11, 0, 0),
    ("85 bis 89", 85, 89, 0, 914935, 0, 153530, 5, 2, 0),
    ("90 bis 94", 90, 94, 0, 407384, 0, 61783, 6, 0, 0),
    ("95 bis 99", 95, 99, 0, 112081, 0, 13274, 7, 1, 0),
    ("100 bis 104", 100, 104, 0, 13235, 0, 882, 3, 0, 0),
    ("105 und älter", 105, None, 0, 606, 0, 24, 1, 0, 0),
    ("Alter nicht erfasst", None, None, 57, 165, 7, 0, 266, 4, 0),
]

KBS_TOTALS = {
    "alle_renten": 1570011,
    "erwerbsminderungsrente": 75424,
    "altersrente": 942690,
    "witwenrente": 518894,
    "witwerrente": 20050,
    "waisenrente": 12801,
    "erziehungsrente": 152,
}


def row(
    rentenart_gruppe: str,
    rentenart_detail: str,
    system: str,
    geschlecht: str,
    alter_label: str,
    alter_von: int | None,
    alter_bis: int | None,
    anzahl: int,
    notiz: str = "",
) -> dict[str, str | int]:
    return {
        "stichtag": STICHTAG,
        "rentenart_gruppe": rentenart_gruppe,
        "rentenart_detail": rentenart_detail,
        "system": system,
        "geschlecht": geschlecht,
        "alter_label": alter_label,
        "alter_von": "" if alter_von is None else alter_von,
        "alter_bis": "" if alter_bis is None else alter_bis,
        "anzahl_renten": anzahl,
        "quelle": SOURCE,
        "notiz": notiz,
    }


def build_bestand_rows() -> list[dict[str, str | int]]:
    rows: list[dict[str, str | int]] = []

    for label, von, bis, anzahl in EM_MALE:
        rows.append(
            row(
                "erwerbsminderungsrente",
                "erwerbsminderungsrente_insgesamt",
                "rv_gesamt",
                "maennlich",
                label,
                von,
                bis,
                anzahl,
                "Altersgruppe 60+ in v1 als 60-66 modelliert.",
            )
        )
    for label, von, bis, anzahl in EM_FEMALE:
        rows.append(
            row(
                "erwerbsminderungsrente",
                "erwerbsminderungsrente_insgesamt",
                "rv_gesamt",
                "weiblich",
                label,
                von,
                bis,
                anzahl,
                "Altersgruppe 60+ in v1 als 60-66 modelliert.",
            )
        )

    for age, anzahl in OLD_AGE_MALE.items():
        label = "100 und älter" if age == 100 else str(age)
        rows.append(
            row(
                "altersrente",
                "altersrente_insgesamt",
                "rv_gesamt",
                "maennlich",
                label,
                age,
                None if age == 100 else age,
                anzahl,
                "100+ wird mit Tail-Regel ab Alter 100 modelliert." if age == 100 else "",
            )
        )
    rows.append(
        row(
            "altersrente",
            "altersrente_insgesamt",
            "rv_gesamt",
            "maennlich",
            "Alter nicht erfasst",
            None,
            None,
            81,
            "Nicht in Sterblichkeitsmodell einbezogen; als offener Rest ausgewiesen.",
        )
    )

    for age, anzahl in OLD_AGE_FEMALE.items():
        label = "100 und älter" if age == 100 else str(age)
        rows.append(
            row(
                "altersrente",
                "altersrente_insgesamt",
                "rv_gesamt",
                "weiblich",
                label,
                age,
                None if age == 100 else age,
                anzahl,
                "100+ wird mit Tail-Regel ab Alter 100 modelliert." if age == 100 else "",
            )
        )
    rows.append(
        row(
            "altersrente",
            "altersrente_insgesamt",
            "rv_gesamt",
            "weiblich",
            "Alter nicht erfasst",
            None,
            None,
            145,
            "Nicht in Sterblichkeitsmodell einbezogen; als offener Rest ausgewiesen.",
        )
    )

    death_specs = [
        ("kleine_witwenrente", "weiblich", 3),
        ("grosse_witwenrente", "weiblich", 4),
        ("kleine_witwerrente", "maennlich", 5),
        ("grosse_witwerrente", "maennlich", 6),
        ("halbwaisenrente", "unbekannt", 7),
        ("vollwaisenrente", "unbekannt", 8),
        ("erziehungsrente", "unbekannt", 9),
    ]
    for death_row in DEATH_ROWS:
        label, von, bis, *_ = death_row
        for detail, geschlecht, index in death_specs:
            anzahl = death_row[index]
            if anzahl == 0:
                continue
            rows.append(
                row(
                    "hinterbliebenenrente",
                    detail,
                    "rv_gesamt",
                    geschlecht,
                    label,
                    von,
                    bis,
                    anzahl,
                    (
                        "Geschlecht bei Waisen/Erziehungsrenten im Tabellenband "
                        "nicht getrennt ausgewiesen."
                        if geschlecht == "unbekannt"
                        else ""
                    ),
                )
            )

    for detail, anzahl in KBS_TOTALS.items():
        gruppe = "alle_renten" if detail == "alle_renten" else (
            "hinterbliebenenrente" if detail.endswith("rente") and detail not in {"altersrente", "erwerbsminderungsrente"} else detail
        )
        rows.append(
            row(
                gruppe,
                f"knappschaft_aggregate_{detail}",
                "knappschaft_bahn_see",
                "gesamt",
                "alle",
                None,
                None,
                anzahl,
                "Nur aggregierte Trennung nach Träger; keine Alters-/Geschlechtsstruktur im Tabellenband.",
            )
        )

    return rows


def build_bundesmittel_rows() -> list[dict[str, str]]:
    return [
        {
            "jahr": "2025",
            "position": "allgemeiner Bundeszuschuss / Defizitausgleich KnRV",
            "betrag_mrd_euro": "65.754",
            "kategorie": "bestandsschutz_altlast_vorlaeufig",
            "abschmelzbar": "ja",
            "quelle": "DRV-Rechnungsergebnisse 2025",
            "notiz": (
                "Politische Reformklassifikation: heutige Zuschüsse bleiben als "
                "Bestandsschutzmasse erhalten und werden proportional zum Sterben "
                "der geschützten Bestandskohorte abgeschmolzen."
            ),
        },
        {
            "jahr": "2025",
            "position": "zusätzlicher Bundeszuschuss",
            "betrag_mrd_euro": "32.104",
            "kategorie": "bestandsschutz_altlast_vorlaeufig",
            "abschmelzbar": "ja",
            "quelle": "DRV-Rechnungsergebnisse 2025",
            "notiz": (
                "Politische Reformklassifikation: heutige Zuschüsse bleiben als "
                "Bestandsschutzmasse erhalten und werden proportional zum Sterben "
                "der geschützten Bestandskohorte abgeschmolzen."
            ),
        },
        {
            "jahr": "ab 2027",
            "position": "neue rentenwirksame Staatsleistungen",
            "betrag_mrd_euro": "0.000",
            "kategorie": "neuer_staatlicher_beitrag",
            "abschmelzbar": "nein",
            "quelle": "Reformmodell",
            "notiz": "Neue Ansprüche werden künftig separat durch echte Beiträge finanziert.",
        },
        {
            "jahr": "ab 2027",
            "position": "echte Steuertransfers ohne Rentenpunkte",
            "betrag_mrd_euro": "0.000",
            "kategorie": "steuertransfer",
            "abschmelzbar": "nein",
            "quelle": "Reformmodell",
            "notiz": "Bewusst nicht rentenwirksame Leistungen bleiben außerhalb der Beitragsrente.",
        },
    ]


def write_csv(path: Path, rows: list[dict[str, str | int]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(rows[0].keys()), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def write_summary(bestand_rows: list[dict[str, str | int]]) -> None:
    totals: dict[str, int] = {}
    for item in bestand_rows:
        if item["system"] != "rv_gesamt":
            continue
        totals[item["rentenart_gruppe"]] = totals.get(item["rentenart_gruppe"], 0) + int(
            item["anzahl_renten"]
        )

    expected = {
        "erwerbsminderungsrente": 1_747_402,
        "altersrente": 18_919_641,
        "hinterbliebenenrente": 5_420_619,
    }
    if totals != expected:
        raise ValueError(f"DRV Kontrollsummen weichen ab: {totals} != {expected}")

    lines = [
        "# DRV-Rentenbestand Inputs für Abschmelzmodell",
        "",
        "Stand: 2026-06-04",
        "",
        "Quelle: `rentenversicherung/originale/2026-06-04-drv-statistikband-rente-2024.pdf`",
        "",
        "## Summen",
        "",
        "| Gruppe | Renten |",
        "| --- | ---: |",
    ]
    for key in ["erwerbsminderungsrente", "altersrente", "hinterbliebenenrente"]:
        lines.append(f"| {key} | {totals.get(key, 0):,} |".replace(",", "."))
    lines.append(f"| gesamt | {sum(totals.values()):,} |".replace(",", "."))
    lines.extend(
        [
            "",
            "## Hinweise",
            "",
            "- Altersrenten und Erwerbsminderungsrenten sind nach Geschlecht getrennt.",
            "- Hinterbliebenenrenten werden über Witwen-/Witwerrenten geschlechtsnah zugeordnet; Waisen- und Erziehungsrenten bleiben `unbekannt`.",
            "- Knappschaft-Bahn-See ist im Tabellenband nur aggregiert nach Träger übernommen, nicht alters- und geschlechtsspezifisch.",
            "- `100 und älter` beziehungsweise `105 und älter` werden als offene Altersgruppen für die Tail-Regel markiert.",
            "",
        ]
    )
    SUMMARY_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    bestand_rows = build_bestand_rows()
    write_csv(BESTAND_CSV, bestand_rows)
    write_csv(BUNDESMITTEL_CSV, build_bundesmittel_rows())
    write_summary(bestand_rows)


if __name__ == "__main__":
    main()
