# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## Purpose

This paper is **The DeGerlia Time Dilation Framework**: a two-system, scale-free notational and conceptual reframing of general relativity. It introduces no new physics — every relation stated is already contained in GR. The framework makes one relation explicit and convenient: time dilation as the inherently two-system, geometric quantity it already is, with GTD and DTD as orthogonal legs of a single unit relationship bound by GTD² + DTD² = 1.

Companion to the main Inertial Relativity paper at `../academic_InertialRelativity-deriving-gr-sr-from-ste/`. Both stay alive.

## Active revision

The current revision plan lives at `latex/local_plan.md` (mirrored at `~/.claude/plans/wondrous-waddling-iverson.md`). It is the authoritative spec for the work in progress. The plan retains Paper A (current `master.tex`) and imparts a defined set of targeted updates, some of which import content from Paper B (`/tmp/degerlia_new/DeGerlia_Time_Dilation_Framework.tex`). It is not a merge of A and B. Read the plan at session start before touching `master.tex`; its "Operating principles for execution" are binding.

## Operating principles

These govern paper-revision work. The full list is in the plan; the four most likely to be violated:

- **The user directs, I execute one step at a time.** No batching beyond what's been explicitly authorized. No "let me also do X while I'm here." Concrete edit, concrete report, then wait.
- **Compile after every LaTeX edit.** `cd latex && latexmk -pdf master.tex`. Report the result in the same turn as the edit — don't wait to be asked.
- **Every number is computed, never eyeballed.** Run `system_properties/` (or equivalent). No "approximately" or "matches" without showing the calculation. No claim that two methods agree without computing both.
- **One-word reset.** If the user says "stop" or "reset," drop whatever's in progress and wait.

## Speed & scope rules (binding — the user values turnaround)

These exist because past sessions wasted huge time. Violating them is the main failure mode here.

- **Plug numbers in; do not "learn the theory."** Don't read the whole paper for context. Read only the box/lines named. Never re-derive the framework or explain/defend the physics — the framing is settled GR and evaluating it is not your job. Zero physics commentary unless explicitly asked.
- **No open-ended trial-and-error.** State the goal before editing. Edit, compile, and — if a visual check is warranted — render *once* to verify that specific change, then stop. Do not loop render→tweak→render chasing perfection past the stated goal.
- **Rendering is welcome, but only to verify a specific requested change** — not as exploration. When the user says "don't render," edit + compile only and let them eyeball the PDF.
- **Don't read the whole file to copy an example between boxes.** Read the source box and the target, swap numbers, done.
- **One short clarifying question beats exploration.** If an instruction is ambiguous, ask one line; don't investigate to disambiguate.
- **Formatting/layout is unsettled** — do not codify or auto-apply a house style for the example boxes. Match the existing box being edited and change only what's asked.

## Framing

- This is general relativity. No new physics, no new predictions. A re-notation of the same quantities.
- DTD (DeGerlia time dilation, √k) is a **core paper term** and a defined geometric complement of GTD. Use it freely.
- The paper presents critiques of the conventional *interpretive presentation* of GR (single-system framing, flat-spacetime habit) — never of the theory itself. Both are explicitly distinguished in the introduction.
- Numbers: carry full precision, round once at the end to six significant figures. Last-digit differences between the k_s and k_d routes are calculation precision (D_crit precision), not physics.
- Tone is confident and concrete. Define, present, demonstrate.

## Terminology

- **DeGerlia compactness**: $D = M/\bar{R}$, symbol italic `$D$` (not `\mathrm{DID}$`).
- **DeGerlia Threshold**: `$D_{\mathrm{crit}} = c^2/2G = 6.73295 \times 10^{26}$ kg/m`.
- **Scale factor**: `$k$` in three equivalent forms — `$v^2/c^2$`, `$r_s/R$`, `$D/D_{\mathrm{crit}}$`.
- **Route labels**: `$k_s = r_s/R$` (Schwarzschild route), `$k_d = D/D_{\mathrm{crit}}$` (DeGerlia route). Analytically identical.
- **GTD**: gravitational time dilation, `$\mathrm{GTD} = \sqrt{1-k}$`.
- **DTD**: DeGerlia time dilation, `$\mathrm{DTD} = \sqrt{k}$` — the geometric complement of GTD.

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
- **Read memory files at session start.** The project memory at `~/.claude/projects/-Users-tomdegerlia-Develop-academic-academic-InertialRelativity-STE-cases/memory/MEMORY.md` indexes the relevant feedback memories — open them all up front, not on-demand. The framing locks in `project_scope.md` are non-negotiable.
- **The `system_properties/` package and `pair_comparisons_v2_cases.md` are copies from the main project** — not symlinks. Edits here will not flow back. If physics calculations or case data need to change, decide whether to update both projects or only this one.
- **Companion paper, not replacement.** The main paper at `../academic_InertialRelativity-deriving-gr-sr-from-ste/` is the long-form derivation with full motivation. This paper is the framework re-notation. Both stay alive.
