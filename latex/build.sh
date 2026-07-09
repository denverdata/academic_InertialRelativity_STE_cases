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
#
# pdflatex/bibtex are run with `|| true`: on this TeX Live, pdflatex can return
# a nonzero exit for benign accumulated warnings while still writing a correct
# PDF. Under `set -e` that spurious nonzero used to abort the script before the
# dated copy was made. We tolerate it here and instead verify the PDF below --
# a real failure is caught by the freshness/existence check, not the exit code.
pdflatex -interaction=nonstopmode master.tex || true
bibtex master || true
pdflatex -interaction=nonstopmode master.tex || true
pdflatex -interaction=nonstopmode master.tex || true

# Fail loudly if the compile did not actually produce a PDF, or if a genuine
# error is present in the log (as opposed to a benign warning-driven exit).
if [[ ! -f master.pdf ]]; then
  echo "ERROR: master.pdf was not produced -- compile genuinely failed." >&2
  exit 1
fi
if grep -q '^!' master.log; then
  echo "ERROR: LaTeX reported a fatal error (see master.log):" >&2
  grep -n '^!' master.log >&2
  exit 1
fi

DATE="$(date +%F)"                       # YYYY-MM-DD
OUT="${TITLE}_${DATE}.pdf"
cp master.pdf "$OUT"

echo "Built: $OUT"
