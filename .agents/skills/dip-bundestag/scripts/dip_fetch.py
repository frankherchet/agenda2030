#!/usr/bin/env python3
"""DIP-Bundestag API Fetch Script.

Uses the de-dip-bundestag package (import: deutschland.dip_bundestag) to query
the official Bundestag DIP API. API key is read exclusively from the
DIP_API_KEY environment variable (never hardcoded).

The skill uses `uv` as package manager:
  uv venv
  uv pip install de-dip-bundestag
  export DIP_API_KEY=yourkey

Examples (for today/yesterday Drucksachen):
  python3 .agents/skills/dip-bundestag/scripts/dip_fetch.py search-drucksachen --f-datum-start 2026-06-08 --f-datum-end 2026-06-09 --output /tmp/recent.json
"""

import argparse
import json
import os
import sys
import urllib.request
from datetime import date

try:
    from deutschland.dip_bundestag import Configuration, ApiClient
    from deutschland.dip_bundestag.api.drucksachen_api import DrucksachenApi
except ImportError:
    print("ERROR: de-dip-bundestag not installed. Run: uv pip install de-dip-bundestag", file=sys.stderr)
    sys.exit(1)


def get_api_key() -> str:
    key = os.getenv("DIP_API_KEY")
    if not key:
        print("ERROR: DIP_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)
    return key


def download_pdf(data: dict, base_path: str) -> None:
    """Download the PDF from fundstelle.pdf_url if present (for 'pdf_fundstelle')."""
    pdf_url = None
    if isinstance(data, dict):
        fs = data.get("fundstelle") or {}
        pdf_url = fs.get("pdf_url") or data.get("pdf_url")
    if pdf_url:
        pdf_path = base_path.replace(".json", ".pdf") if base_path.endswith(".json") else base_path + ".pdf"
        try:
            urllib.request.urlretrieve(pdf_url, pdf_path)
            print(f"PDF downloaded: {pdf_path}")
        except Exception as e:
            print(f"Warning: could not download PDF {pdf_url}: {e}", file=sys.stderr)


def build_configuration() -> Configuration:
    configuration = Configuration()
    key = get_api_key()
    configuration.api_key["ApiKeyHeader"] = key
    configuration.api_key["ApiKeyQuery"] = key
    return configuration


def cmd_search_drucksachen(args):
    config = build_configuration()
    with ApiClient(config) as api_client:
        api = DrucksachenApi(api_client)
        params = {}
        if args.f_datum_start:
            params["f_datum_start"] = args.f_datum_start
        if args.f_datum_end:
            params["f_datum_end"] = args.f_datum_end
        if args.f_drucksachetyp:
            params["f_drucksachetyp"] = args.f_drucksachetyp
        if args.f_wahlperiode is not None:
            params["f_wahlperiode"] = args.f_wahlperiode
        if args.f_dokumentnummer:
            params["f_dokumentnummer"] = args.f_dokumentnummer
        if args.f_titel:
            params["f_titel"] = args.f_titel
        if args.cursor:
            params["cursor"] = args.cursor
        if args.format:
            params["format"] = args.format
        try:
            # Use raw response to avoid model validation errors in the generated client
            # (some Drucksache records have incomplete author data)
            http_response = api.get_drucksache_list(_preload_content=False, **params)
            data = json.loads(http_response.data)
        except Exception as exc:
            print(f"API error: {exc}", file=sys.stderr)
            sys.exit(2)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2, default=str)
            print(f"Saved to {args.output}")
        else:
            print(json.dumps(data, ensure_ascii=False, indent=2, default=str))


def cmd_get_drucksache(args):
    config = build_configuration()
    with ApiClient(config) as api_client:
        api = DrucksachenApi(api_client)
        try:
            doc_id = int(args.id) if str(args.id).isdigit() else args.id
            http_response = api.get_drucksache(doc_id, _preload_content=False, format=args.format or "json")
            data = json.loads(http_response.data)
        except Exception as exc:
            print(f"API error: {exc}", file=sys.stderr)
            sys.exit(2)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2, default=str)
            print(f"Saved to {args.output}")
            download_pdf(data, args.output)
        else:
            print(json.dumps(data, ensure_ascii=False, indent=2, default=str))


def main():
    parser = argparse.ArgumentParser(description="DIP Bundestag API client (uv + de-dip-bundestag)")
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search-drucksachen", help="Search Drucksachen (supports f_datum_start/end for yesterday/today)")
    p_search.add_argument("--f-datum-start", type=date.fromisoformat, help="Earliest document date (YYYY-MM-DD)")
    p_search.add_argument("--f-datum-end", type=date.fromisoformat, help="Latest document date (YYYY-MM-DD)")
    p_search.add_argument("--f-drucksachetyp", help="Type filter")
    p_search.add_argument("--f-wahlperiode", type=int, help="Wahlperiode")
    p_search.add_argument("--f-dokumentnummer", help="Document number")
    p_search.add_argument("--term", "--f-titel", dest="f_titel", help="Search term in title (maps to f_titel)")
    p_search.add_argument("--cursor", help="Pagination cursor")
    p_search.add_argument("--format", default="json", choices=["json", "xml"])
    p_search.add_argument("--output", "-o", help="Output file")
    p_search.set_defaults(func=cmd_search_drucksachen)

    p_get = sub.add_parser("get-drucksache", help="Get single Drucksache by ID")
    p_get.add_argument("--id", required=True)
    p_get.add_argument("--format", default="json", choices=["json", "xml"])
    p_get.add_argument("--output", "-o", help="Output file")
    p_get.set_defaults(func=cmd_get_drucksache)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
