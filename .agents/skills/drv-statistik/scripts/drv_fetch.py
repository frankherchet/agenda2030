#!/usr/bin/env python3
"""
DRV Statistik Helper Script

Helps downloading and extracting data from Deutsche Rentenversicherung
publications (Rentenversicherung in Zahlen, Statistikband etc.).

Since there is no public REST API, the script focuses on:
- Downloading annual Statistikbände (PDF)
- Extracting tables using pdfplumber
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


BASE_URL = "https://www.deutsche-rentenversicherung.de/SharedDocs/Downloads/DE/Statistiken-und-Berichte/statistikpublikationen"


def download_band(jahr: int, typ: str = "Rentenversicherung in Zahlen", output_dir: str = "analysen/daten") -> str:
    """Download the annual 'Rentenversicherung in Zahlen' PDF."""
    filename = f"rv_in_zahlen_{jahr}.pdf"
    url = f"{BASE_URL}/{filename}?__blob=publicationFile&v=2"
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    target = Path(output_dir) / filename

    print(f"Downloading {url} ...")
    try:
        urllib.request.urlretrieve(url, target)
        print(f"Saved to {target}")
        return str(target)
    except Exception as e:
        print(f"Error downloading: {e}")
        sys.exit(1)


def extract_text(pdf_path: str, output_dir: str = "analysen/daten") -> str:
    """Extract full text from a PDF (simple version)."""
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

    p_down = sub.add_parser("download-band", help="Download 'Rentenversicherung in Zahlen'")
    p_down.add_argument("--jahr", type=int, required=True)
    p_down.add_argument("--typ", default="Rentenversicherung in Zahlen")
    p_down.add_argument("--output-dir", default="analysen/daten")
    p_down.set_defaults(func=lambda args: download_band(args.jahr, args.typ, args.output_dir))

    p_text = sub.add_parser("extract-text", help="Extract text from downloaded PDF")
    p_text.add_argument("--pdf", required=True)
    p_text.add_argument("--output-dir", default="analysen/daten")
    p_text.set_defaults(func=lambda args: extract_text(args.pdf, args.output_dir))

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
