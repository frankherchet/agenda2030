#!/usr/bin/env python3
"""Small GENESIS-Online RESTful/JSON helper for agenda2030.

Credentials are read from DESTATIS_USER/DESTATIS_PASSWORD or DESTATIS_TOKEN.
They are never printed.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


BASE_URL = "https://genesis.destatis.de/genesisWS/rest/2020"
KNOWN_POST_PATHS = {
    "cubes": "catalogue/cubes",
    "jobs": "catalogue/jobs",
    "modifieddata": "catalogue/modifieddata",
    "results": "catalogue/results",
    "statistics": "catalogue/statistics",
    "tables": "catalogue/tables",
    "terms": "catalogue/terms",
    "timeseries": "catalogue/timeseries",
    "values": "catalogue/values",
    "variables": "catalogue/variables",
    "metadata-cube": "metadata/cube",
    "metadata-statistic": "metadata/statistic",
    "metadata-table": "metadata/table",
    "metadata-timeseries": "metadata/timeseries",
    "metadata-value": "metadata/value",
    "metadata-variable": "metadata/variable",
    "table": "data/table",
    "tablefile": "data/tablefile",
    "cube": "data/cube",
    "cubefile": "data/cubefile",
    "timeseries-data": "data/timeseries",
    "timeseriesfile": "data/timeseriesfile",
    "result": "data/result",
    "resultfile": "data/resultfile",
}


def parse_params(items: list[str]) -> dict[str, str]:
    params: dict[str, str] = {}
    for item in items:
        if "=" not in item:
            raise SystemExit(f"invalid --param {item!r}; expected key=value")
        key, value = item.split("=", 1)
        params[key] = value
    return params


def credentials() -> dict[str, str]:
    token = os.environ.get("DESTATIS_TOKEN")
    user = os.environ.get("DESTATIS_USER")
    password = os.environ.get("DESTATIS_PASSWORD")
    if token:
        return {"username": token, "password": ""}
    if not user or not password:
        raise SystemExit(
            "Missing credentials. Set DESTATIS_USER and DESTATIS_PASSWORD "
            "or DESTATIS_TOKEN in the environment."
        )
    return {"username": user, "password": password}


def post_json(path: str, payload: dict[str, Any]) -> dict[str, Any]:
    url = f"{BASE_URL}/{path.lstrip('/')}"
    auth_headers = {
        key: value
        for key, value in {
            "username": payload.get("username"),
            "password": payload.get("password"),
        }.items()
        if value
    }
    body = urllib.parse.urlencode(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded", **auth_headers},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {exc.code} from GENESIS endpoint {path}: {detail[:500]}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"Could not reach GENESIS endpoint {path}: {exc.reason}") from exc
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"raw": raw}


def write_output(data: dict[str, Any], output: str | None) -> None:
    text = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)
    if output:
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + "\n", encoding="utf-8")
        print(path)
    else:
        print(text)


def command_payload(args: argparse.Namespace) -> tuple[str, dict[str, Any]]:
    auth = credentials()
    common: dict[str, Any] = {
        **auth,
        "language": args.language,
    }
    common.update(parse_params(args.param))

    if args.command == "logincheck":
        return "helloworld/logincheck", common
    if args.command == "find":
        return "find/find", {
            **common,
            "term": args.term,
            "category": args.category,
            "pagelength": args.pagelength,
        }
    if args.command == "post":
        path = KNOWN_POST_PATHS.get(args.path, args.path)
        return path, common
    if args.command == "table":
        return "data/table", {
            **common,
            "name": args.name,
            "area": args.area,
            "compress": args.compress,
            "transpose": args.transpose,
            "startyear": args.startyear,
            "endyear": args.endyear,
        }
    if args.command == "tablefile":
        return "data/tablefile", {
            **common,
            "name": args.name,
            "area": args.area,
            "format": args.format,
            "compress": args.compress,
            "transpose": args.transpose,
            "startyear": args.startyear,
            "endyear": args.endyear,
        }
    if args.command == "metadata-table":
        return "metadata/table", {
            **common,
            "name": args.name,
        }
    if args.command in KNOWN_POST_PATHS:
        return KNOWN_POST_PATHS[args.command], common
    raise SystemExit(f"unsupported command: {args.command}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fetch data from Destatis GENESIS.")
    parser.add_argument("--language", default="de", choices=["de", "en"])
    parser.add_argument("--param", action="append", default=[], help="Extra API parameter key=value")
    sub = parser.add_subparsers(dest="command", required=True)

    login = sub.add_parser("logincheck")
    login.add_argument("--output")
    login.add_argument("--param", action="append", default=argparse.SUPPRESS, help="Extra API parameter key=value")

    find = sub.add_parser("find")
    find.add_argument("--term", required=True)
    find.add_argument("--category", default="Alle")
    find.add_argument("--pagelength", default="25")
    find.add_argument("--output")
    find.add_argument("--param", action="append", default=argparse.SUPPRESS, help="Extra API parameter key=value")

    generic = sub.add_parser("post")
    generic.add_argument("path", help="API path such as catalogue/tables or a known alias")
    generic.add_argument("--output")
    generic.add_argument("--param", action="append", default=argparse.SUPPRESS, help="Extra API parameter key=value")

    table = sub.add_parser("table")
    table.add_argument("--name", required=True)
    table.add_argument("--area", default="all")
    table.add_argument("--compress", default="false")
    table.add_argument("--transpose", default="false")
    table.add_argument("--startyear", default="")
    table.add_argument("--endyear", default="")
    table.add_argument("--output")
    table.add_argument("--param", action="append", default=argparse.SUPPRESS, help="Extra API parameter key=value")

    tablefile = sub.add_parser("tablefile")
    tablefile.add_argument("--name", required=True)
    tablefile.add_argument("--area", default="all")
    tablefile.add_argument("--format", default="ffcsv")
    tablefile.add_argument("--compress", default="false")
    tablefile.add_argument("--transpose", default="false")
    tablefile.add_argument("--startyear", default="")
    tablefile.add_argument("--endyear", default="")
    tablefile.add_argument("--output")
    tablefile.add_argument("--param", action="append", default=argparse.SUPPRESS, help="Extra API parameter key=value")

    metadata = sub.add_parser("metadata-table")
    metadata.add_argument("--name", required=True)
    metadata.add_argument("--output")
    metadata.add_argument("--param", action="append", default=argparse.SUPPRESS, help="Extra API parameter key=value")

    for command in [
        "cubes",
        "jobs",
        "modifieddata",
        "results",
        "statistics",
        "tables",
        "terms",
        "timeseries",
        "values",
        "variables",
        "metadata-cube",
        "metadata-statistic",
        "metadata-timeseries",
        "metadata-value",
        "metadata-variable",
        "cube",
        "cubefile",
        "timeseries-data",
        "timeseriesfile",
        "result",
        "resultfile",
    ]:
        known = sub.add_parser(command)
        known.add_argument("--output")
        known.add_argument("--param", action="append", default=argparse.SUPPRESS, help="Extra API parameter key=value")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    path, payload = command_payload(args)
    output = getattr(args, "output", None)
    write_output(post_json(path, payload), output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
