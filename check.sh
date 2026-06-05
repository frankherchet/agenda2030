#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

echo "[check] Markdown-Frontmatter pruefen"
python3 - <<'PY'
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml


def tracked_files(pattern: str) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z", pattern],
        check=True,
        stdout=subprocess.PIPE,
    )
    return [Path(item.decode()) for item in result.stdout.split(b"\0") if item]


errors: list[str] = []

for path in tracked_files("*.md"):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        continue

    closing = text.find("\n---", 4)
    if closing == -1:
        errors.append(f"{path}: Frontmatter wurde nicht geschlossen")
        continue

    frontmatter = text[4:closing]
    try:
        data = yaml.safe_load(frontmatter) if frontmatter.strip() else {}
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        if mark:
            errors.append(
                f"{path}:{mark.line + 1}:{mark.column + 1}: YAML-Fehler: {exc.problem}"
            )
        else:
            errors.append(f"{path}: YAML-Fehler: {exc}")
        continue

    if data is not None and not isinstance(data, dict):
        errors.append(f"{path}: Frontmatter muss ein YAML-Mapping sein")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)

print("OK")
PY

echo "[check] Python-Syntax pruefen"
PYCACHE_DIR="$(mktemp -d)"
PYTHONPYCACHEPREFIX="$PYCACHE_DIR" python3 -m py_compile $(git ls-files '*.py')
rm -rf "$PYCACHE_DIR"

echo "[check] Rechenartefakte reproduzieren"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT
TMP_REPO="$TMP_DIR/repo"
mkdir -p "$TMP_REPO"

while IFS= read -r -d '' file; do
  mkdir -p "$TMP_REPO/$(dirname "$file")"
  cp "$file" "$TMP_REPO/$file"
done < <(git ls-files -z)

for script in "$TMP_REPO"/scripts/*.py; do
  echo "  python3 scripts/$(basename "$script")"
  (cd "$TMP_REPO" && python3 "scripts/$(basename "$script")")
done

echo "[check] Pages-Build pruefen"
npm --prefix web run build

echo "[check] Git-Diff auf Whitespace-Fehler pruefen"
git diff --check

echo "[check] OK"
