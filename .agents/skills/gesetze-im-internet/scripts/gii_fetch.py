#!/usr/bin/env python3
"""Search and download laws from gesetze-im-internet.de.

This helper keeps the workflow deliberately simple:
- search-title: query the official TOC (gii-toc.xml)
- search-text: query the official full-text search endpoint
- ingest: write a compact Markdown source note for one law slug
- norm: write a Markdown normstand or norm extract for one selected norm

The script only uses the Python standard library.
"""

from __future__ import annotations

import argparse
import html
import io
import json
import os
import re
import sys
from datetime import date
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any
import xml.etree.ElementTree as ET


BASE_URL = "https://www.gesetze-im-internet.de"
TOC_URL = f"{BASE_URL}/gii-toc.xml"
SEARCH_URL = f"{BASE_URL}/cgi-bin/htsearch"
CACHE_DIR = Path(os.environ.get("XDG_CACHE_HOME") or (Path.home() / ".cache"))
CACHE_DIR = CACHE_DIR / "agenda2030" / "gesetze-im-internet"


def fetch_bytes(url: str, timeout: int = 60) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "*/*",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {exc.code} from {url}: {detail[:500]}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"Could not reach {url}: {exc.reason}") from exc


def normalize_url(url: str) -> str:
    return url.replace("http://www.gesetze-im-internet.de", BASE_URL).replace(
        "http://gesetze-im-internet.de", BASE_URL
    )


def slug_from_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    parts = [part for part in parsed.path.split("/") if part]
    if not parts:
        raise SystemExit(f"Could not derive slug from URL: {url}")
    if parts[-1] == "xml.zip" and len(parts) >= 2:
        return parts[-2]
    if parts[-1].endswith(".html") and len(parts) >= 2:
        return parts[-2]
    return parts[-1]


def law_base_url(slug: str) -> str:
    return f"{BASE_URL}/{slug.strip('/')}/"


def law_xml_url(slug: str) -> str:
    return f"{law_base_url(slug)}xml.zip"


def default_norm_url(slug: str, norm: str) -> str:
    clean = norm_key(norm)
    if slug == "gg":
        if clean.isdigit():
            return f"{law_base_url(slug)}art_{clean}.html"
    return f"{law_base_url(slug)}__{clean}.html"


def norm_key(value: str) -> str:
    key = re.sub(r"[^0-9a-zA-Z]+", "", value).lower()
    return re.sub(r"^(artikel|art|paragraph|par)", "", key)


def cache_path(name: str) -> Path:
    return CACHE_DIR / name


def cached_fetch(url: str, name: str, refresh: bool = False) -> bytes:
    path = cache_path(name)
    if path.exists() and not refresh:
        return path.read_bytes()
    data = fetch_bytes(url)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def normalize_text(text: str) -> str:
    text = text.replace("\r", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def inline_text(node: ET.Element | None) -> str:
    if node is None:
        return ""
    return normalize_text("".join(node.itertext()))


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def render_dl(node: ET.Element) -> str:
    children = list(node)
    items: list[str] = []
    index = 0
    while index < len(children):
        current = children[index]
        if local_name(current.tag) != "DT":
            index += 1
            continue
        label = inline_text(current)
        content = ""
        if index + 1 < len(children) and local_name(children[index + 1].tag) == "DD":
            content = inline_text(children[index + 1])
            index += 2
        else:
            index += 1
        if label and content:
            items.append(f"{label} {content}".strip())
        elif content:
            items.append(f"- {content}")
        elif label:
            items.append(label)
    return "\n".join(items)


def render_table(node: ET.Element) -> str:
    rows: list[str] = []
    for row in node.iter():
        if local_name(row.tag) != "row":
            continue
        cells = []
        for entry in row:
            if local_name(entry.tag) != "entry":
                continue
            cells.append(inline_text(entry))
        cells = [cell for cell in cells if cell]
        if cells:
            rows.append("| " + " | ".join(cells) + " |")
    return "\n".join(rows)


def render_node(node: ET.Element) -> str:
    tag = local_name(node.tag)
    if tag == "BR":
        return "\n"
    if tag == "DL":
        return f"{render_dl(node)}\n\n"
    if tag == "table":
        return f"{render_table(node)}\n\n"
    if tag == "P":
        return f"{render_children(node)}\n\n"
    if tag in {"Content", "text", "DD", "DT", "LA", "fussnoten"}:
        return render_children(node)
    if tag == "pre":
        return f"{''.join(node.itertext())}\n\n"
    return render_children(node)


def render_children(node: ET.Element) -> str:
    parts: list[str] = []
    if node.text:
        parts.append(node.text)
    for child in node:
        rendered = render_node(child)
        if rendered:
            parts.append(rendered)
        if child.tail:
            parts.append(child.tail)
    return normalize_text("".join(parts))


def render_block(node: ET.Element | None) -> str:
    if node is None:
        return ""
    text = render_children(node)
    return normalize_text(text)


def load_toc(refresh: bool = False) -> list[dict[str, str]]:
    raw = cached_fetch(TOC_URL, "gii-toc.xml", refresh=refresh)
    root = ET.fromstring(raw)
    items: list[dict[str, str]] = []
    for item in root.findall("item"):
        title = inline_text(item.find("title"))
        link = normalize_url(inline_text(item.find("link")))
        if not title or not link:
            continue
        items.append(
            {
                "title": title,
                "link": link,
                "slug": slug_from_url(link),
            }
        )
    return items


def score_title(query: str, title: str, slug: str) -> float:
    query_n = normalize_text(query.lower())
    title_n = normalize_text(title.lower())
    slug_n = slug.lower()
    query_tokens = [token for token in re.split(r"[^a-z0-9]+", query_n) if len(token) > 1]
    title_tokens = set(token for token in re.split(r"[^a-z0-9]+", title_n) if len(token) > 1)
    score = 0.0
    if query_n == title_n:
        score += 10.0
    if query_n in title_n:
        score += 5.0
    if query_n in slug_n:
        score += 4.0
    score += sum(2.0 for token in query_tokens if token in title_tokens)
    if query_tokens and all(token in title_tokens for token in query_tokens):
        score += 2.5
    score += SequenceMatcher(None, query_n, title_n).ratio()
    return score


def search_title(query: str, limit: int = 10, refresh: bool = False) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for item in load_toc(refresh=refresh):
        score = score_title(query, item["title"], item["slug"])
        if score <= 0:
            continue
        results.append({**item, "score": round(score, 6)})
    results.sort(key=lambda item: (-item["score"], item["title"]))
    return results[:limit]


def search_text(query: str, method: str = "and", page: int = 1) -> list[dict[str, Any]]:
    params = {
        "config": "Gesamt_bmjhome2005",
        "method": method,
        "words": query,
    }
    if page > 1:
        params["page"] = str(page)
    url = f"{SEARCH_URL}?{urllib.parse.urlencode(params)}"
    raw = fetch_bytes(url)
    text = raw.decode("iso-8859-1", errors="replace")
    pattern = re.compile(
        r'<dt><strong><a href="([^"]+)".*?>(.*?)</a></strong>(.*?)</dt>\s*<dd>(.*?)</dd>',
        re.S,
    )
    results: list[dict[str, Any]] = []
    for match in pattern.finditer(text):
        url = normalize_url(match.group(1))
        title = html.unescape(re.sub(r"<.*?>", "", match.group(2)))
        snippet = html.unescape(re.sub(r"<.*?>", " ", match.group(4)))
        results.append(
            {
                "title": normalize_text(title),
                "url": url,
                "slug": slug_from_url(url),
                "snippet": normalize_text(snippet),
            }
        )
    return results


def download_law_xml(slug: str, refresh: bool = False) -> tuple[bytes, str]:
    slug = slug.strip().strip("/")
    if slug.startswith("http://") or slug.startswith("https://"):
        slug = slug_from_url(slug)
    url = law_xml_url(slug)
    cache_name = f"{slug}.xml.zip"
    return cached_fetch(url, cache_name, refresh=refresh), url


def unzip_xml(zip_bytes: bytes) -> tuple[str, bytes]:
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as archive:
        xml_names = [name for name in archive.namelist() if name.lower().endswith(".xml")]
        if not xml_names:
            raise SystemExit("No XML document found in downloaded zip archive")
        xml_name = sorted(xml_names)[0]
        return xml_name, archive.read(xml_name)


def parse_law(xml_bytes: bytes) -> dict[str, Any]:
    root = ET.fromstring(xml_bytes)
    builddate = root.attrib.get("builddate", "")
    norms = list(root.findall("norm"))
    if not norms:
        raise SystemExit("Downloaded XML does not contain any norm nodes")

    first_meta = norms[0].find("metadaten")
    jurabk = inline_text(first_meta.find("jurabk")) if first_meta is not None else ""
    title = inline_text(first_meta.find("langue")) if first_meta is not None else ""
    ausfertigung = inline_text(first_meta.find("ausfertigung-datum")) if first_meta is not None else ""

    fundstelle = ""
    if first_meta is not None:
        fundstelle_node = first_meta.find("fundstelle")
        if fundstelle_node is not None:
            periodikum = inline_text(fundstelle_node.find("periodikum"))
            zitstelle = inline_text(fundstelle_node.find("zitstelle"))
            fundstelle = normalize_text(" ".join(part for part in [periodikum, zitstelle] if part))

    standangaben: list[str] = []
    if first_meta is not None:
        for stand in first_meta.findall("standangabe"):
            comment = inline_text(stand.find("standkommentar")) or inline_text(stand.find("standtyp"))
            if comment:
                standangaben.append(normalize_text(comment))

    toc_text = ""
    toc_norm = None
    actual_norms: list[ET.Element] = []
    for norm in norms:
        meta = norm.find("metadaten")
        enbez = inline_text(meta.find("enbez")) if meta is not None else ""
        gliederungsbez = inline_text(meta.find("gliederungseinheit/gliederungsbez")) if meta is not None else ""
        if enbez == "Inhaltsübersicht" and toc_norm is None:
            toc_norm = norm
            continue
        if enbez.startswith("§") or enbez.startswith("Art.") or enbez.startswith("Artikel"):
            actual_norms.append(norm)
        elif gliederungsbez:
            actual_norms.append(norm)

    if toc_norm is not None:
        toc_text = render_block(toc_norm.find("textdaten/text"))

    return {
        "builddate": builddate,
        "jurabk": jurabk,
        "title": title,
        "ausfertigung": ausfertigung,
        "fundstelle": fundstelle,
        "standangaben": standangaben,
        "toc_text": toc_text,
        "norms": actual_norms,
    }


def parse_selected_norm(xml_bytes: bytes, norm_query: str) -> dict[str, Any]:
    root = ET.fromstring(xml_bytes)
    norms = list(root.findall("norm"))
    query = norm_key(norm_query)
    for norm in norms:
        meta = norm.find("metadaten")
        if meta is None:
            continue
        enbez = inline_text(meta.find("enbez"))
        if not enbez:
            continue
        enbez_n = norm_key(enbez)
        if query == enbez_n:
            return {
                "norm": norm,
                "enbez": enbez,
                "titel": inline_text(meta.find("titel")),
                "jurabk": inline_text(meta.find("jurabk")),
            }
    raise SystemExit(f"Could not find norm {norm_query!r} in downloaded XML")


def render_norm_text(norm: ET.Element) -> str:
    text_node = norm.find("textdaten/text")
    if text_node is None:
        return ""
    rendered = render_block(text_node)
    footnotes_node = norm.find("fussnoten")
    if footnotes_node is not None:
        footnotes_text = render_block(footnotes_node)
        if footnotes_text:
            rendered = f"{rendered}\n\n## Fußnoten\n\n{footnotes_text}" if rendered else footnotes_text
    rendered = normalize_text(rendered)
    rendered = re.sub(r"(?<!\n)\b(\d+\.)", r"\n\1", rendered)
    return normalize_text(rendered)


def write_text(text: str, output: str | None) -> None:
    if output:
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text.rstrip() + "\n", encoding="utf-8")
        print(path)
    else:
        print(text)


def ingest_markdown(slug: str, law: dict[str, Any], law_url: str, xml_url: str) -> str:
    title = law["title"] or law["jurabk"] or slug
    lines = [
        "---",
        f"title: Gesetze im Internet {law['jurabk'] or slug}",
        f"date: {date.today().isoformat()}",
        "type: ingest",
        "status: erfasst",
        "source_urls:",
        f"  - {law_url}",
        f"  - {xml_url}",
        "ingest_refs: []",
        "---",
        "",
        f"# Ingest: Gesetze im Internet {law['jurabk'] or slug}",
        "",
        "## Metadaten",
        "",
        "- Typ: Link/Rechtsquelle",
        f"- Datum: {date.today().isoformat()}",
        "- Quelle: Gesetze im Internet",
        "- Status: erfasst",
        "- Index: `ingest/index/README.md`",
    ]
    if law["builddate"]:
        lines.append(f"- Builddate: {law['builddate']}")
    if law["ausfertigung"]:
        lines.append(f"- Ausfertigung: {law['ausfertigung']}")
    if law["fundstelle"]:
        lines.append(f"- Fundstelle: {law['fundstelle']}")
    if law["standangaben"]:
        lines.append("- Standangaben:")
        for item in law["standangaben"]:
            lines.append(f"  - {item}")
    lines.extend(
        [
            "",
            "## Kurzfassung",
            "",
            f"Amtliche konsolidierte Fassung von {title}.",
            "",
            "## Enthaltene Informationen",
            "",
            "- Vollständige konsolidierte Norm mit Inhaltsübersicht, Einzelnormen und Fußnoten.",
            "- XML-Zip für maschinelle Weiterverarbeitung und lokalen Markdown-Export.",
            "",
            "## Jetzt extrahierte relevante Informationen",
            "",
            f"- Jurabk: {law['jurabk'] or 'TODO'}",
            f"- Ausfertigung: {law['ausfertigung'] or 'TODO'}",
            f"- Fundstelle: {law['fundstelle'] or 'TODO'}",
        ]
    )
    if law["toc_text"]:
        preview = law["toc_text"].splitlines()
        preview = [line for line in preview if line.strip()]
        if preview:
            lines.extend(["- Inhaltsübersicht:", ""])
            for item in preview[:20]:
                cells = [cell.strip() for cell in item.strip().strip("|").split("|") if cell.strip()]
                if cells:
                    lines.append(f"  - {' / '.join(cells)}")
                else:
                    lines.append(f"  - {item}")
    lines.extend(
        [
            "",
            "## Offene Fragen",
            "",
            "- Relevante Normen für die aktuelle Aufgabe im Anschluss als Normstand-Dateien ausarbeiten.",
        ]
    )
    return "\n".join(lines)


def norm_markdown(
    slug: str,
    law: dict[str, Any],
    selected: dict[str, Any],
    law_url: str,
    xml_url: str,
    ingest_ref: str | None,
    source_url: str | None,
) -> str:
    norm = selected["norm"]
    enbez = selected["enbez"]
    titel = selected["titel"]
    norm_title = titel or enbez
    page_url = source_url or default_norm_url(slug, enbez)
    ingest_ref_line = ingest_ref or "TODO: passende Ingest-Datei ergänzen"
    norm_text = render_norm_text(norm)
    meta_lines = [
        "---",
        f"title: Normstand {selected['jurabk'] or slug} {enbez}",
        f"date: {date.today().isoformat()}",
        "type: normstand",
        "status: geltender-normstand",
        "source_urls:",
        f"  - {page_url}",
        f"  - {xml_url}",
        "ingest_refs:",
        f"  - {ingest_ref_line}",
        "---",
        "",
        f"# Normstand: {selected['jurabk'] or slug} {enbez}",
        "",
        "## Metadaten",
        "",
        f"- Gesetz: {selected['jurabk'] or slug}",
        f"- Norm: {enbez}",
    ]
    meta_lines.append(f"- Normtitel: {norm_title}")
    if law["ausfertigung"]:
        meta_lines.append(f"- Fassung/Stand: {law['ausfertigung']}")
    if law["builddate"]:
        meta_lines.append(f"- Builddate: {law['builddate']}")
    meta_lines.extend(
        [
            f"- Abrufdatum: {date.today().isoformat()}",
            f"- Quelle: {page_url}",
            "- source_urls:",
            f"  - {page_url}",
            f"  - {xml_url}",
            "- ingest_refs:",
            f"  - {ingest_ref_line}",
            "- Status: geltender Normstand",
            "",
            "## Normtitel",
            "",
            norm_title,
            "",
            "## Normtext",
            "",
            "```text",
            norm_text,
            "```",
            "",
            "## Kurzeinordnung",
            "",
            "Amtliche Einzelnormfassung des geltenden Normstands.",
            "",
            "## Relevanz für agenda2030",
            "",
            "Lokale Rechtsgrundlage für Folgearbeiten, Prüfungen und Änderungsskizzen im agenda2030-Repo.",
            "",
            "## Verknüpfte Artefakte",
            "",
            f"- Ingests: {ingest_ref_line}",
            "- Analysen/Projektartefakte: TODO",
            "- Gesetzesänderungen: TODO",
            "",
            "## Offene Fragen",
            "",
            "- Keine zusätzlichen offenen Fragen für die reine Ablage des Normstands.",
        ]
    )
    return "\n".join(meta_lines)


def cmd_search_title(args: argparse.Namespace) -> int:
    results = search_title(args.query, limit=args.limit, refresh=args.refresh)
    payload = {
        "query": args.query,
        "source": TOC_URL,
        "count": len(results),
        "results": results,
    }
    write_text(json.dumps(payload, ensure_ascii=False, indent=2), args.output)
    return 0


def cmd_search_text(args: argparse.Namespace) -> int:
    results = search_text(args.query, method=args.method, page=args.page)
    payload = {
        "query": args.query,
        "method": args.method,
        "source": f"{SEARCH_URL}?config=Gesamt_bmjhome2005",
        "count": len(results),
        "results": results[: args.limit],
    }
    write_text(json.dumps(payload, ensure_ascii=False, indent=2), args.output)
    return 0


def cmd_ingest(args: argparse.Namespace) -> int:
    zip_bytes, xml_url = download_law_xml(args.slug, refresh=args.refresh)
    _, xml_bytes = unzip_xml(zip_bytes)
    law = parse_law(xml_bytes)
    slug = args.slug.strip().strip("/")
    text = ingest_markdown(slug, law, law_base_url(slug), xml_url)
    write_text(text, args.output)
    return 0


def cmd_norm(args: argparse.Namespace) -> int:
    zip_bytes, xml_url = download_law_xml(args.slug, refresh=args.refresh)
    _, xml_bytes = unzip_xml(zip_bytes)
    law = parse_law(xml_bytes)
    selected = parse_selected_norm(xml_bytes, args.norm)
    slug = args.slug.strip().strip("/")
    text = norm_markdown(
        slug=slug,
        law=law,
        selected=selected,
        law_url=law_base_url(slug),
        xml_url=xml_url,
        ingest_ref=args.ingest_ref,
        source_url=args.source_url,
    )
    write_text(text, args.output)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Search and download Gesetze im Internet content as Markdown.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_title = sub.add_parser("search-title", help="Search the official TOC by title or abbreviation")
    p_title.add_argument("query")
    p_title.add_argument("--limit", type=int, default=10)
    p_title.add_argument("--refresh", action="store_true")
    p_title.add_argument("--output")
    p_title.set_defaults(func=cmd_search_title)

    p_text = sub.add_parser("search-text", help="Search the official full-text search")
    p_text.add_argument("query")
    p_text.add_argument("--method", choices=["and", "or"], default="and")
    p_text.add_argument("--page", type=int, default=1)
    p_text.add_argument("--limit", type=int, default=10)
    p_text.add_argument("--output")
    p_text.set_defaults(func=cmd_search_text)

    p_ingest = sub.add_parser("ingest", help="Download a law slug and write a compact ingest Markdown file")
    p_ingest.add_argument("slug")
    p_ingest.add_argument("--output", required=True)
    p_ingest.add_argument("--refresh", action="store_true")
    p_ingest.set_defaults(func=cmd_ingest)

    p_norm = sub.add_parser("norm", help="Download a law slug and write one norm Markdown file")
    p_norm.add_argument("slug")
    p_norm.add_argument("--norm", required=True, help="Norm number, e.g. 213 or Art. 3")
    p_norm.add_argument("--ingest-ref", help="Repo-relative path to the matching ingest file")
    p_norm.add_argument("--source-url", help="Exact HTML URL for the selected norm")
    p_norm.add_argument("--output", required=True)
    p_norm.add_argument("--refresh", action="store_true")
    p_norm.set_defaults(func=cmd_norm)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
