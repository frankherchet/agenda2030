#!/usr/bin/env python3
"""
DRV Statistik Helper Script

Supports:
- Downloading annual DRV Statistikbände (PDF)
- Extracting text/tables
- Downloading from BMAS Open Data (Rentenbestandsstatistik)
"""

import argparse
import os
import sys
import urllib.request
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("pdfplumber not installed. Run: uv pip install pdfplumber")
    sys.exit(1)


def download_drv_band(jahr: int, output_dir: str = "analysen/daten") -> str:
    """Download 'Rentenversicherung in Zahlen' PDF."""
    filename = f"rv_in_zahlen_{jahr}.pdf"
    url = f"https://www.deutsche-rentenversicherung.de/SharedDocs/Downloads/DE/Statistiken-und-Berichte/statistikpublikationen/{filename}?__blob=publicationFile&v=2"
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    target = Path(output_dir) / filename

    print(f"Downloading {url} ...")
    try:
        urllib.request.urlretrieve(url, target)
        print(f"Saved to {target}")
        return str(target)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def download_bmas_rentenbestand(output_dir: str = "analysen/daten") -> str:
    """Download latest Rentenbestandsstatistik from BMAS."""
    url = "https://www.bmas.de/SharedDocs/Downloads/DE/Statistiken/Rentenbestandsstatistik/rentenbestandsstatistik-2025.xlsx?__blob=publicationFile&v=2"
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    target = Path(output_dir) / "bmas_rentenbestandsstatistik_2025.xlsx"

    print(f"Downloading BMAS Rentenbestandsstatistik ...")
    try:
        urllib.request.urlretrieve(url, target)
        print(f"Saved to {target}")
        return str(target)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def extract_text(pdf_path: str, output_dir: str = "analysen/daten") -> str:
    """Extract text from PDF."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"File not found: {pdf_path}")
        sys.exit(1)

    out_file = Path(output_dir) / (pdf_path.stem + "_text.md")
    out_file.parent.mkdir(parents=True, exist_ok=True)

    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n\n"

    out_file.write_text(text, encoding="utf-8")
    print(f"Text extracted to {out_file}")
    return str(out_file)


def main():
    parser = argparse.ArgumentParser(description="DRV Statistik Helper")
    sub = parser.add_subparsers(dest="command", required=True)

    p1 = sub.add_parser("download-band", help="Download DRV 'Rentenversicherung in Zahlen'")
    p1.add_argument("--jahr", type=int, required=True)
    p1.add_argument("--output-dir", default="analysen/daten")
    p1.set_defaults(func=lambda args: download_drv_band(args.jahr, args.output_dir))

    p2 = sub.add_parser("download-bmas", help="Download BMAS Rentenbestandsstatistik")
    p2.add_argument("--output-dir", default="analysen/daten")
    p2.set_defaults(func=lambda args: download_bmas_rentenbestand(args.output_dir))

    p3 = sub.add_parser("extract-text", help="Extract text from PDF")
    p3.add_argument("--pdf", required=True)
    p3.add_argument("--output-dir", default="analysen/daten")
    p3.set_defaults(func=lambda args: extract_text(args.pdf, args.output_dir))

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
