#!/usr/bin/env python3
"""Validate references.json and generate index.md + references.bib.

references.json is the single source of truth; never edit the generated files.
Run from anywhere:  python3 refered-doc/script/build_index.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "references.json"
INDEX = ROOT / "index.md"
BIB = ROOT / "references.bib"

REQUIRED = ("id", "category", "title", "url", "verified_via")
CITABLE_REQUIRED = ("authors", "year")  # websites in "data" may omit these
CATEGORY_ORDER = ("primary", "nobel", "textbook", "review", "tutorial", "data")
CATEGORY_TITLE = {
    "primary": "原始文献（历史 / 各实验首次提出）",
    "nobel": "诺贝尔奖",
    "textbook": "教科书",
    "review": "综述",
    "tutorial": "教学文章",
    "data": "谱图数据来源",
}
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
BIB_TYPE = {"textbook": "book", "nobel": "misc", "data": "misc"}


def validate(refs):
    errors = []
    seen = set()
    for i, ref in enumerate(refs):
        tag = ref.get("id", f"#{i}")
        required = REQUIRED if ref.get("category") == "data" else REQUIRED + CITABLE_REQUIRED
        missing = [k for k in required if not ref.get(k)]
        if missing:
            errors.append(f"{tag}: missing {', '.join(missing)}")
        if tag in seen:
            errors.append(f"{tag}: duplicate id")
        seen.add(tag)
        if ref.get("category") not in CATEGORY_ORDER:
            errors.append(f"{tag}: unknown category {ref.get('category')!r}")
        doi = ref.get("doi")
        if doi and not DOI_RE.match(doi):
            errors.append(f"{tag}: malformed DOI {doi!r}")
    return errors


def short_authors(authors):
    if not authors:
        return ""
    return authors[0] if len(authors) == 1 else f"{authors[0]} et al."


def index_row(ref):
    link = f"https://doi.org/{ref['doi']}" if ref.get("doi") else ref["url"]
    oa = f"[PDF]({ref['oa_pdf_url']})" if ref.get("oa_pdf_url") else ""
    flag = "⚠️" if ref["verified_via"] == "UNVERIFIED" else "✓"
    exps = ", ".join(ref.get("experiment") or [])
    return (f"| {flag} | [{ref['title']}]({link}) | {short_authors(ref['authors'])} | "
            f"{ref.get('year') or ''} | {exps} | {ref.get('use_on_slide', '').replace('|', ' / ')} | {oa} | "
            f"{ref.get('note_zh', '')} |")


def render_index(refs):
    lines = ["# 参考文献数据库", "",
             "> 由 `script/build_index.py` 从 `references.json` 生成，请勿手改。",
             "> ✓ = 已在登记库核实；⚠️ = 未核实，不要上 slide。", ""]
    for cat in CATEGORY_ORDER:
        group = sorted((r for r in refs if r["category"] == cat), key=lambda r: r.get("year") or 0)
        if not group:
            continue
        lines += [f"## {CATEGORY_TITLE[cat]}（{len(group)}）", "",
                  "| | 标题 | 作者 | 年份 | 实验 | 用于 | OA | 说明 |",
                  "|---|---|---|---|---|---|---|---|"]
        lines += [index_row(r) for r in group]
        lines.append("")
    return "\n".join(lines)


def render_bib(refs):
    entries = []
    for ref in refs:
        kind = BIB_TYPE.get(ref["category"], "article")
        fields = {
            "title": "{" + ref["title"] + "}",
            "author": " and ".join(ref.get("authors") or []),
            "year": str(ref["year"]) if ref.get("year") else None,
            "journal" if kind == "article" else "publisher": ref.get("venue"),
            "volume": ref.get("volume"),
            "pages": ref.get("pages"),
            "doi": ref.get("doi"),
            "isbn": ref.get("isbn"),
            "url": ref["url"],
        }
        body = ",\n".join(f"  {k} = {{{v}}}" for k, v in fields.items() if v)
        entries.append(f"@{kind}{{{ref['id']},\n{body}\n}}")
    return "\n\n".join(entries) + "\n"


def main():
    refs = json.loads(DB.read_text(encoding="utf-8"))
    errors = validate(refs)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    INDEX.write_text(render_index(refs), encoding="utf-8")
    BIB.write_text(render_bib(refs), encoding="utf-8")
    unverified = sum(r["verified_via"] == "UNVERIFIED" for r in refs)
    print(f"OK: {len(refs)} refs ({unverified} unverified) -> index.md, references.bib")


if __name__ == "__main__":
    main()
