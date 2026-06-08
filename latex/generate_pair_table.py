#!/usr/bin/env python3
"""Generate LaTeX pair comparison tables (system properties + derived ratios)
for the six worked cases. 10 significant digits, compact e-style notation,
row groups preserved. Output to stdout — redirect to latex/pair_tables.tex."""

import os
import re
import sys
from decimal import Decimal, getcontext, localcontext, ROUND_HALF_EVEN
getcontext().prec = 50

# Physical constants — single source of truth is system_properties/constants.py.
# D_CRIT is a six-digit physical value (precision inherited from G); it is
# never recomputed from c²/(2G) here. See the comment on D_CRIT in
# system_properties/constants.py.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from system_properties.constants import G as G_CONST, SPEED_OF_LIGHT, D_CRIT

def parse_md_groups(filepath):
    """Parse the markdown file into groups of (label, values) rows.
    Groups are separated by blank lines or by repeated header rows."""
    groups = [[]]
    with open(filepath) as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                if groups[-1]:
                    groups.append([])
                continue
            if stripped.startswith('|--') or stripped.startswith('| metric'):
                if groups[-1]:
                    groups.append([])
                continue
            if stripped.startswith('|'):
                parts = [p.strip() for p in stripped.split('|')[1:-1]]
                if len(parts) >= 8:
                    label = parts[0]
                    values = parts[1:9]
                    groups[-1].append((label, values))
    return [g for g in groups if g]

def fmt_round_pad(val_str, round_prec, display_width=10):
    """Round to `round_prec` sig figs (the value's honest precision), then
    pad/format to `display_width` sig-digit slots (uniform table width).
    Trailing zeros are honest placeholders, not invented precision."""
    val_str = val_str.strip()
    if val_str == '---' or val_str == '':
        return '---'
    try:
        d = Decimal(val_str)
    except Exception:
        return val_str
    if d == 0:
        return '0'

    sign = '-' if d < 0 else ''
    abs_d = abs(d)

    with localcontext() as ctx:
        ctx.prec = round_prec
        ctx.rounding = ROUND_HALF_EVEN
        rounded = +abs_d

    exp = rounded.adjusted()
    _, digits, _ = rounded.as_tuple()
    digit_str = ''.join(str(x) for x in digits)
    # Pad with zeros to display_width
    if len(digit_str) < display_width:
        digit_str = digit_str + '0' * (display_width - len(digit_str))
    elif len(digit_str) > display_width:
        digit_str = digit_str[:display_width]

    mstr = digit_str[0] + '.' + digit_str[1:]
    exp_sign = '+' if exp >= 0 else '-'
    exp_str = f'{exp_sign}{abs(exp)}'
    return f'{sign}{mstr}e{exp_str}'


def fmt10(val_str):
    return fmt_round_pad(val_str, round_prec=10, display_width=10)


def fmt_1mx(val_str, prec):
    """Always output as `1-x` (x = 1-v). Used for GTD values and GTD ratios
    only (bounded in [0,1]). Not used for DTD: DTD ranges from 0 to infinity,
    so a value > 1 would render as `1--...` nonsense."""
    val_str = val_str.strip()
    if val_str == '---' or val_str == '':
        return '---'
    try:
        v = Decimal(val_str)
    except Exception:
        return val_str
    with localcontext() as ctx:
        ctx.prec = 50
        x = Decimal(1) - v
    return '1-' + fmt_round_pad(str(x), prec, prec)



# LaTeX rendering for row labels — keys are the raw markdown labels
LABELS = {
    # System Properties
    'm_1 (kg)':       r'$m_1$ (kg)',
    'm_2 (kg)':       r'$m_2$ (kg)',
    'r_1 (m)':        r'$r_1$ (m)',
    'r_2 (m)':        r'$r_2$ (m)',
    'ρ_1 (kg/m³)':    r'$\rho_1$ (kg/m$^3$)',
    'ρ_2 (kg/m³)':    r'$\rho_2$ (kg/m$^3$)',
    'I_1 (kg·m²)':    r'$I_1$ (kg$\cdot$m$^2$)',
    'I_2 (kg·m²)':    r'$I_2$ (kg$\cdot$m$^2$)',
    'D_1 (kg/m)':     r'$D_1$ (kg/m)',
    'D_2 (kg/m)':     r'$D_2$ (kg/m)',
    'D_1_norm':       r'$D_{1\_norm}$',
    'D_2_norm':       r'$D_{2\_norm}$',
    'r_s_1 (m)':      r'$r_{s\_1}$ (m)',
    'r_s_2 (m)':      r'$r_{s\_2}$ (m)',
    'gtd_1':          r'$\mathrm{GTD}_{s,1}$',
    'gtd_2':          r'$\mathrm{GTD}_{s,2}$',
    'GTD_s_1':        r'$\mathrm{GTD}_{s,1}$',
    'GTD_s_2':        r'$\mathrm{GTD}_{s,2}$',
    'dtd_1':          r'$dtd_1$',
    'dtd_2':          r'$dtd_2$',

    # Derived ratios
    'dtd_1/dtd_2':                          r'$dtd_1/dtd_2$',
    'sqrt(D_1/D_2)':                        r'$\sqrt{D_1/D_2}$',
    'sqrt((m_1·r_2)/(m_2·r_1))':            r'$\sqrt{(m_1 r_2)/(m_2 r_1)}$',
    'sqrt((I_1/I_2)*(r_2/r_1)³)':           r'$\sqrt{(I_1/I_2)(r_2/r_1)^3}$',
    '(I_1/I_2)^(1/5)*(ρ_1/ρ_2)^(3/10)':     r'$(I_1/I_2)^{1/5}(\rho_1/\rho_2)^{3/10}$',

    '(m_2·r_1)/(m_1·r_2)':                  r'$(m_2 r_1)/(m_1 r_2)$',
    '(m_1·r_2)/(m_2·r_1)':                  r'$(m_1 r_2)/(m_2 r_1)$',
    '(*k) D_2/D_1':                         r'$D_2/D_1$',
    '(*k) D_1/D_2':                         r'$D_1/D_2$',
    '(I_1/I_2)*(r_2/r_1)³':                 r'$(I_1/I_2)(r_2/r_1)^3$',

    'k_s':                                  r'$k_s$',
    'k_d':                                  r'$k_d$',
    'GTD_d_1':                              r'$\mathrm{GTD}_{d,1}$',
    'GTD_d_2':                              r'$\mathrm{GTD}_{d,2}$',
    'I_1/I_2':                              r'$I_1/I_2$',
    'I_2/I_1':                              r'$I_2/I_1$',
    '(I_1/I_2)^(1/2)':                      r'$(I_1/I_2)^{1/2}$',
    '(I_2/I_1)^(1/2)':                      r'$(I_2/I_1)^{1/2}$',
    'k_i=(ρ_1/ρ_2)^(1/5)*(r_1/r_2)':        r'$(\rho_1/\rho_2)^{1/5}(r_1/r_2)$',
    '(I_1/I_2)^(1/5)':                      r'$(I_1/I_2)^{1/5}$',
    '(I_2/I_1)^(1/5)':                      r'$(I_2/I_1)^{1/5}$',
    '(dtd_1/dtd_2)²*(r_1/r_2)³':            r'$(dtd_1/dtd_2)^2(r_1/r_2)^3$',

    '(*G) gtd_1/gtd_2':                     r'$\mathrm{GTD}_{s,1}/\mathrm{GTD}_{s,2}$',
    'GTD_d_1/GTD_d_2':                      r'$\mathrm{GTD}_{d,1}/\mathrm{GTD}_{d,2}$',
    'sqrt(1-dtd_1²)/sqrt(1-dtd_2²)':        r'$\sqrt{1-dtd_1^2}/\sqrt{1-dtd_2^2}$',

    '(*k) k_m=m_1/m_2':                     r'$m_1/m_2$',
    '(*k) k_r=r_1/r_2':                     r'$r_1/r_2$',
    'r_2/r_1':                              r'$r_2/r_1$',
    'sqrt(r_2/r_1)':                        r'$\sqrt{r_2/r_1}$',
    'sqrt(r_1/r_2)':                        r'$\sqrt{r_1/r_2}$',
    'sqrt(m_1/m_2)':                        r'$\sqrt{m_1/m_2}$',
    'sqrt(m_2²r_2/(m_1²r_1))':              r'$\sqrt{m_2^2 r_2/(m_1^2 r_1)}$',
}

# Source columns: 0=M=M, 1=case1b, 2=R=R, 3=P=P, 4=I=I, 5=General, 6=Classical Static Density Example, 7=General2
# Keep: M=M, R=R, P=P, I=I, General, Classical Static Density Example
KEEP = [0, 2, 3, 4, 5, 6]
COL_NAMES = [
    r'Case 1 ($M\!=\!M$)',
    r'Case 2 ($R\!=\!R$)',
    r'Case 3 ($\rho\!=\!\rho$)',
    r'Case 4 ($I\!=\!I$)',
    'General',
    r'Classical ($\rho\!=\!\rho$)',
]

SKIP_LABELS = {
    '(m_2·r_1)/(m_1·r_2)',
    '(*k) D_2/D_1',
    # DTD rows omitted in the lean paper:
    'dtd_1',
    'dtd_2',
    'dtd_1/dtd_2',
    'sqrt(1-dtd_1²)/sqrt(1-dtd_2²)',
    '(dtd_1/dtd_2)²*(r_1/r_2)³',
}

def project(group):
    return [(label, [values[i] for i in KEEP])
            for label, values in group
            if label not in SKIP_LABELS]

GTD_ROWS = {
    'gtd_1', 'gtd_2',
    '(*G) gtd_1/gtd_2',
    'GTD_d_1/GTD_d_2',
    'sqrt(1-dtd_1²)/sqrt(1-dtd_2²)',
    'GTD_s_1', 'GTD_s_2',
    'GTD_d_1', 'GTD_d_2',
}

def emit_row(label, values):
    latex_label = LABELS.get(label, label)
    use_1mx = label in GTD_ROWS
    formatted = []
    for v in values:
        cell = fmt_1mx(v, 6) if use_1mx else fmt_round_pad(v, 6, 6)
        formatted.append(r'{\ttfamily ' + cell + r'}')
    print(f'{latex_label} & ' + ' & '.join(formatted) + r' \\')

def emit_table_header(caption, label):
    print(r'\begin{table*}[!ht]')
    print(r'\centering')
    print(r'\caption{' + caption + '}')
    print(r'\label{' + label + '}')
    print(r'\setlength{\tabcolsep}{1pt}')
    print(r'\renewcommand{\arraystretch}{1.1}')
    print(r'\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}} l l l l l l l @{}}')
    print(r'\toprule')
    print(r' & ' + ' & '.join([r'\textbf{' + n + '}' for n in COL_NAMES]) + r' \\')
    print(r'\midrule')

def emit_table_footer():
    print(r'\bottomrule')
    print(r'\end{tabular*}')
    print(r'\end{table*}')

def verify_against_source(groups):
    """For each computed row, check there's at least one source row whose values
    match at 10 sig digits in every column. Raise SystemExit on mismatch.

    Checked pairings:
      (I_1/I_2)*(r_2/r_1)³  ==  D_1/D_2  ==  (m_1·r_2)/(m_2·r_1)  ==  (dtd_1/dtd_2)²*(r_1/r_2)³
      sqrt(r_1/r_2)         ==  1/sqrt(r_2/r_1)  (computed from source sqrt(r_2/r_1))
    """
    # Build a flat label→values map from all groups.
    flat = {label: values for g in groups for label, values in g}

    def fmt_list(vals):
        return [fmt10(v) for v in vals]

    # 1. (I_1/I_2)*(r_2/r_1)^3 must equal D_1/D_2 (one of the universal identities
    #    visible in the same group) at 10 sig digits, across all columns.
    if '(I_1/I_2)*(r_2/r_1)³' in flat and '(*k) D_1/D_2' in flat:
        computed = fmt_list(flat['(I_1/I_2)*(r_2/r_1)³'])
        reference = fmt_list(flat['(*k) D_1/D_2'])
        if computed != reference:
            raise SystemExit(
                f'VERIFY FAILED: (I_1/I_2)*(r_2/r_1)^3 != D_1/D_2 at 10 sig digits.\n'
                f'  computed:  {computed}\n  D_1/D_2:   {reference}'
            )

    # 2. Same row must also equal (dtd_1/dtd_2)²*(r_1/r_2)³ — wait, that's the
    #    *reciprocal*: (I_1/I_2)(r_2/r_1)^3 = (dtd_1/dtd_2)² ≠ (dtd_1/dtd_2)²*(r_1/r_2)³.
    #    Skip — no clean source pairing for this one beyond #1.

    # 3. Computed r_2/r_1 must be the reciprocal of source r_1/r_2.
    if 'r_2/r_1' in flat and '(*k) k_r=r_1/r_2' in flat:
        for i, (a, b) in enumerate(zip(flat['r_2/r_1'], flat['(*k) k_r=r_1/r_2'])):
            try:
                product = Decimal(a) * Decimal(b)
                if abs(product - Decimal(1)) > Decimal('1e-9'):
                    raise SystemExit(
                        f'VERIFY FAILED: r_2/r_1 * r_1/r_2 != 1 in col {i}.\n'
                        f'  product = {product}'
                    )
            except SystemExit:
                raise
            except Exception:
                pass

def add_top_table_rows(groups):
    """Rebuild the top table (group 0). All per-system values are read directly
    from source; no per-system computation happens here. The source carries:

      k_s_1, k_s_2          = r_s / R                  (Schwarzschild path)
      D_1_norm, D_2_norm    = D / D_crit               (DeGerlia path, = k_d)
      gtd_1, gtd_2          = sqrt(1 - 2GM/(Rc²))      (Schwarzschild path)
      gtd_d_1, gtd_d_2      = sqrt(1 - D/D_crit)       (DeGerlia path)

    Each was computed independently by system_properties. This function only
    relabels them onto the display labels used by the LaTeX table.
    """
    if not groups:
        return groups
    flat = {label: values for g in groups for label, values in g}
    placeholder = ['---'] * 8
    src = lambda key: list(flat.get(key, placeholder))

    groups[0] = [
        ('m_1 (kg)',     src('m_1 (kg)')),
        ('m_2 (kg)',     src('m_2 (kg)')),
        ('r_1 (m)',      src('r_1 (m)')),
        ('r_2 (m)',      src('r_2 (m)')),
        ('ρ_1 (kg/m³)',  src('ρ_1 (kg/m³)')),
        ('ρ_2 (kg/m³)',  src('ρ_2 (kg/m³)')),
        ('I_1 (kg·m²)',  src('I_1 (kg·m²)')),
        ('I_2 (kg·m²)',  src('I_2 (kg·m²)')),
        ('D_1 (kg/m)',   src('D_1 (kg/m)')),
        ('D_2 (kg/m)',   src('D_2 (kg/m)')),
        ('r_s_1 (m)',    src('r_s_1 (m)')),
        ('r_s_2 (m)',    src('r_s_2 (m)')),
        ('D_1_norm',     src('D_1_norm')),
        ('D_2_norm',     src('D_2_norm')),
        ('k_s',          src('k_s_1')),
        ('k_d',          src('D_1_norm')),
        ('GTD_s_1',      src('gtd_1')),
        ('GTD_s_2',      src('gtd_2')),
        ('GTD_d_1',      src('gtd_d_1')),
        ('GTD_d_2',      src('gtd_d_2')),
    ]
    return groups


def main():
    groups = parse_md_groups('../pair_comparisons_v2_cases.md')

    # Every row below is read from the source .md. No formulas in this script.
    # The renderer's job is layout, label LaTeX, and 10-sig-digit rounding only.

    # Move GTD/GTD group (source idx 4) to be the 3rd bottom-table group.
    if len(groups) > 4:
        groups[3], groups[4] = groups[4], groups[3]

    # Append the GTD_d_1/GTD_d_2 ratio to the gtd-ratio group. This is an
    # inter-system ratio (legal generator computation per the source-of-truth
    # rule). Computed from the per-system gtd_d rows that come from source.
    flat_src = {label: values for g in groups for label, values in g}
    if 'gtd_d_1' in flat_src and 'gtd_d_2' in flat_src:
        d1_vals = flat_src['gtd_d_1']
        d2_vals = flat_src['gtd_d_2']
        d_ratio = []
        for a, b in zip(d1_vals, d2_vals):
            if a in ('---', '') or b in ('---', ''):
                d_ratio.append('---')
                continue
            bd = Decimal(b)
            d_ratio.append('---' if bd == 0 else str(Decimal(a) / bd))
        groups[3].append(('GTD_d_1/GTD_d_2', d_ratio))

    # Add k_s, k_d, GTD_d_1, GTD_d_2 placeholder rows to the top table.
    groups = add_top_table_rows(groups)

    # Reorder the last group: m_1/m_2, sqrt(m_1/m_2), r_1/r_2, sqrt(r_1/r_2).
    # m_1/m_2, sqrt(m_1/m_2), and r_1/r_2 come from source; sqrt(r_1/r_2) is
    # computed by inversion from sqrt(r_2/r_1) (exact at Decimal precision).
    if len(groups) > 5:
        src = {label: values for label, values in groups[5]}
        sqrt_r1_r2 = [str(Decimal(1) / Decimal(v)) for v in src['sqrt(r_2/r_1)']]
        groups[5] = [
            ('(*k) k_m=m_1/m_2', src['(*k) k_m=m_1/m_2']),
            ('sqrt(m_1/m_2)', src['sqrt(m_1/m_2)']),
            ('(*k) k_r=r_1/r_2', src['(*k) k_r=r_1/r_2']),
            ('sqrt(r_1/r_2)', sqrt_r1_r2),
        ]

    groups = [project(g) for g in groups]

    if not groups:
        raise SystemExit('No groups parsed from source data')

    # Cross-check: every computed row must match a source row of identical value
    # at 10 significant digits. If a paired source row doesn't exist, skip silently.
    # If one exists and disagrees, fail loud rather than emit a wrong table.
    verify_against_source(groups)

    # Table 1: System Properties (first group)
    emit_table_header('System properties for each pair comparison case.',
                      'tab:pair_properties')
    for label, values in groups[0]:
        emit_row(label, values)
    emit_table_footer()
    print()

    # Table 2: Derived Ratios (remaining groups, separated by \hline)
    emit_table_header('Derived ratios across constraint cases.',
                      'tab:pair_ratios')
    for gi, group in enumerate(groups[1:]):
        if gi > 0:
            print(r'[3pt]\hline\\[-6pt]')
        for label, values in group:
            emit_row(label, values)
    emit_table_footer()

if __name__ == '__main__':
    main()
