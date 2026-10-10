# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Group-project workspace for NUS CM5241 Modern Analytical Techniques, **Topic 9: Structural Elucidation of Unknown Organic Compounds Using 2D NMR Spectroscopy**. Deliverable is a 12–15 min presentation (or video) by 5 people, split 2+3: **Part 2** (this user's sub-team, 2 people) = history, principle, experiment types and uses of 2D NMR; **Part 3** (3 people) = real cases solvable only by 2D NMR (COSY/HSQC/HMQC → planar structure, NOESY → stereochemistry). Reply in Chinese; content is Chinese with English technical terms.

- Git repo, remote `github.com/dzylol/CM5241-NMR-group-project` (private, Discussions on). Lives in iCloud Drive — the user also pushes from GitHub's web UI, so `git fetch` before pushing.
- `project.md` (the group chat brief) is **gitignored on purpose** — it exists locally only. Before any pull/rebase that touches it, back it up; a remote delete of a once-tracked file removes the local copy.
- Parent folder (`../`) holds course PDFs and the user's exam-prep workspace (`../exam-notes`, own CLAUDE.md) — read-only from here.

## Course requirements that constrain content

Summarised with slide numbers in `requirements.md` (source: Lecture 1 Course Intro post-lecture slides). The ones that bite:
- "Use authentic, traceable data from credible sources" → every fact/figure on a slide needs a citation that exists in `refered-doc/references.json`. Never cite from memory.
- NMR is **not** taught in the course → Part 2 must start from 1D basics.
- Video option forbids AI-generated voice/video; AI use must be disclosed in a note at the end.
- Deadlines: .pptx Week 12 Tue 23:59 (Canvas); presentation Week 12 Wed 14:00–18:00 LT28.

## Layout

- `part2-principles/outline.md` — slide-by-slide plan for Part 2 (Slides 1–7, ~6 min). The "分工与时间" section is pending the user's discussion with their partner; don't fill it in.
- `refered-doc/` — the reference database:
  - `references.json` — **single source of truth** (array of objects: `id`, `category` ∈ primary|nobel|textbook|review|tutorial|data, `title`, `authors`, `year`, `venue`, `doi`, `url`, `oa_pdf_url`, `quote`, `verified_via`, `use_on_slide`, `note_zh`, …). `verified_via: "UNVERIFIED"` marks items not yet confirmed — they show ⚠️ and must not go on slides.
  - `index.md`, `references.bib` — **generated**; never hand-edit.
  - `script/build_index.py` — validates (required fields, unique ids, DOI format; `data` category may omit authors/year) and regenerates both files.
  - `paper/` — PDFs named `<id>.pdf` matching `references.json` ids; `paper/README.md` lists page counts and licence per file. `kupce-claridge-2017-noah.pdf` is a licensed NUS-library download, gitignored — don't commit it.
  - `report/project/` — source of the review-report Design canvas artifact (`https://claude.ai/artifact/6Ru7AXefU21UCbRNkLjpFy`): `canvas.json` + `Main.dc.html`. Edit these files and republish to the same artifact URL with `root` = `refered-doc/report`.

## Commands

```bash
# After any edit to references.json — must print "OK: N refs"
python3 refered-doc/script/build_index.py

# Read/inspect a PDF (pymupdf via uv; `file` misreports page counts)
uv run --quiet --with pymupdf python3 -I -c 'import pymupdf; d=pymupdf.open("refered-doc/paper/<id>.pdf"); print(d.page_count)'
```

## Working conventions

- Verify bibliographic metadata against Crossref (`api.crossref.org/works/<DOI>`), Open Library (books) or nobelprize.org before adding a reference; record the method in `verified_via`.
- Downloading publisher PDFs from scripts usually hits Cloudflare/bot checks (ACS, ORA, PMC, EPFL) — don't try to bypass; give the user the URL and the target filename `<id>.pdf` to download manually, then check it's a real PDF.
- Subagents used for web/paper searches should run on Haiku (user preference).
- Commit messages: conventional (`docs:`, `chore:` …). Push only when the user asks.
