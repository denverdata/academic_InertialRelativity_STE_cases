# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## Purpose

This is a stripped-down companion to the main Inertial Relativity paper at `../academic_InertialRelativity-deriving-gr-sr-from-ste/`. It presents the M₁R₂/(M₂R₁) compactness relation that governs the time-dilation ratio between two uniform spherical systems, validated across six worked cases (classical-through-relativistic).

The paper is an **analysis of general relativity and special relativity as currently stated**. Not a new theory. Not an extension. Nothing is added to GR/SR. The math is drawn directly from the standard formulations.

## Non-negotiable framing locks

Read `~/.claude/projects/-Users-tomdegerlia-Develop-academic-academic_InertialRelativity_STE_cases/memory/project_scope.md` first — the framing locks are non-negotiable and govern all editing.

In short:
- **Do not state implications of any kind, anywhere.** Permitted: describe what the math IS or SHOWS. Forbidden: describe what the math MEANS, IMPLIES, SUGGESTS, or CHANGES about how to think about anything.
- Do not treat anything as speculative or novel.
- Do not add new derivations or extend equations. Strip-don't-author.
- Tone is confident and minimal. Define, present, demonstrate, stop.

## Terminology — specific to this paper

- **DeGerlia compactness** (not "DeGerlia inertial density"). Same quantity, more accessible term for general physics readership.
- Symbol: italic **`$D$`** (not `\mathrm{DID}$`). Aligns with the appendix tables and with prior `degerlia202505` convention.
- Threshold: **`$D_{crit}$`**.
- Compactness ratio: **`$k_d$`** (unchanged).
- **No DTD anywhere.** Use "gravitational time dilation," "Lorentz time dilation," or "time-dilation ratio."

## Build commands

Compile the paper (from the `latex/` directory):
```bash
cd latex && latexmk -pdf master.tex
```

Clean LaTeX build artifacts:
```bash
cd latex && latexmk -c
```

Rebuild the STE isometric scaling diagram (`ste_example.pdf` and `.png`):
```bash
cd latex && pdflatex ste_example.tex && pdftoppm -png -r 300 -singlefile ste_example.pdf ste_example
```

## Data pipeline

The six case-study numbers in the appendix come from:
1. `run_all_systems.py` (repo root) → instantiates the systems via `system_properties/`, writes `systems_output.md` and `systems_table.md`.
2. `latex/generate_pair_table.py` → reads `pair_comparisons_v2_cases.md` (repo root), emits `latex/pair_tables.tex` to stdout. Redirect: `python3 latex/generate_pair_table.py > latex/pair_tables.tex`.
3. `master.tex` does `\input{pair_tables}` in the appendix.

Per `feedback_generator_scripts.md`: never hand-edit `pair_tables.tex` — update the generator instead.

## Repository structure

| Path | Purpose |
|------|---------|
| `latex/master.tex` | The paper. |
| `latex/master_template.tex` | Original unmodified RSC template — **do not modify**. |
| `latex/rsc.bst` | RSC bibliography style — **do not modify**. |
| `latex/rsc.bib` | Bibliography. |
| `latex/ste_example.tex` | TikZ source for the STE isometric scaling diagram. |
| `latex/ste_example.pdf`/`.png` | Compiled diagram (embedded via `\includegraphics`). |
| `latex/pair_tables.tex` | Appendix tables (generated). |
| `latex/generate_pair_table.py` | Generator for the appendix tables. |
| `latex/head_foot/` | RSC journal header/footer graphics — do not modify. |
| `system_properties/` | High-precision (100-decimal) `Decimal` arithmetic for physical systems. No external deps. |
| `run_all_systems.py` | Runner: 11 systems → `systems_output.md` / `systems_table.md`. |
| `pair_comparisons_v2_cases.md` | Source data for `generate_pair_table.py`. |

## Gotchas

- **Always compile from `latex/` directory** — root-level aux files pollute the tree and can break the build.
- **Read memory files at session start.** The project memory at `~/.claude/projects/-Users-tomdegerlia-Develop-academic-academic_InertialRelativity_STE_cases/memory/MEMORY.md` indexes the relevant feedback memories — open them all up front, not on-demand. The framing locks in `project_scope.md` are non-negotiable.
- **The `system_properties/` package and `pair_comparisons_v2_cases.md` are copies from the main project** — not symlinks. Edits here will not flow back. If physics calculations or case data need to change, decide whether to update both projects or only this one.
- **Companion paper, not replacement.** The main paper at `../academic_InertialRelativity-deriving-gr-sr-from-ste/` is the long-form derivation with full motivation and DTD construction. This paper is the stripped version. Both stay alive.
