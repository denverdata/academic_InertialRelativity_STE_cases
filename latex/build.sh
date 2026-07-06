#!/usr/bin/env bash
# Compile master.tex and save a dated, title-named copy of the PDF.
# Naming rule (per user): "<paper title>_YYYY-MM-DD.pdf" in this directory.
# The title is read from the \LARGE{\textbf{...}} title cell in master.tex,
# so the filename always tracks the real title -- no hardcoding to drift.
set -euo pipefail

cd "$(dirname "$0")"

# Extract the paper title from the title cell in master.tex.
TITLE="$(grep -o '\\LARGE{\\textbf{[^}]*}}' master.tex | head -1 | sed -E 's/.*\\textbf\{([^}]*)\}\}/\1/')"
if [[ -z "$TITLE" ]]; then
  echo "ERROR: could not extract title from master.tex" >&2
  exit 1
fi

# Full build sequence so citations and cross-references resolve:
# pdflatex -> bibtex -> pdflatex -> pdflatex. A single pdflatex pass leaves
# every \cite and \ref undefined and never builds the bibliography.
pdflatex -interaction=nonstopmode master.tex
bibtex master
pdflatex -interaction=nonstopmode master.tex
pdflatex -interaction=nonstopmode master.tex

DATE="$(date +%F)"                       # YYYY-MM-DD
OUT="${TITLE}_${DATE}.pdf"
cp master.pdf "$OUT"

echo "Built: $OUT"
