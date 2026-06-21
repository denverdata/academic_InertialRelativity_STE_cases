#!/usr/bin/env python3
"""Generate one worked Example block (mdframed) for the paper, identical in
structure to the General Case block in master.tex.

Inputs: a name/label and the four system parameters (M1, R1, M2, R2).
All numbers are computed via the canonical system_properties engine
(UniformSphere) -- nothing is reimplemented or eyeballed.

Usage:
    python3 build_example_block.py "General Case" 1e20 2e-7 1e30 1e7
    (M1 R1 M2 R2)  -> prints the LaTeX block to stdout.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'system_properties'))
from decimal import Decimal as D, getcontext
getcontext().prec = 50
import constants as C
from pair_calc import pair_metrics


def sig(x, n=6):
    """Format Decimal x for siunitx \\num{...}, applying the project precision rule:

      * Default: 6 significant figures (precision limited by G).
      * Leading-nines exception: if the significand's first digit is 9 (the
        signature of a value subtracted from 1, e.g. a GTD like 0.9999257356),
        keep 6 significant digits AFTER the leading run of 9s. So the total
        precision is (number of leading 9s) + 6. Examples:
          0.999851477   -> 9.99851477e-1   (3 nines + 6)
          0.9999257356  -> 9.999257356e-1  (4 nines + 6)
    """
    from decimal import localcontext, ROUND_HALF_UP
    x = D(x)
    if x == 0:
        return '0'

    # Determine effective precision. Look at the leading run of 9s in the
    # significand (at high precision so we count them honestly before rounding).
    with localcontext() as ctx:
        ctx.prec = 50
        probe = +abs(x)
    _, pdigits, _ = probe.as_tuple()
    lead_nines = 0
    for d in pdigits:
        if d == 9:
            lead_nines += 1
        else:
            break
    prec = (lead_nines + n) if lead_nines > 0 else n

    sign = '-' if x < 0 else ''
    with localcontext() as ctx:
        ctx.prec = prec
        ctx.rounding = ROUND_HALF_UP
        r = +abs(x)
    exp = r.adjusted()
    _, digits, _ = r.as_tuple()
    ds = ''.join(str(d) for d in digits)
    if len(ds) < prec:
        ds = ds + '0' * (prec - len(ds))
    else:
        ds = ds[:prec]
    mant = ds[0] + '.' + ds[1:]
    return f'{sign}{mant}e{exp}'


def num(x, n=6):
    return r'\num{' + sig(x, n) + '}'


def build_block(name, M1, R1, M2, R2, caption=None):
    M1, R1, M2, R2 = D(str(M1)), D(str(R1)), D(str(M2)), D(str(R2))
    Dc = C.D_CRIT
    G, c = C.G, C.SPEED_OF_LIGHT

    # All numbers come from the single shared core (pair_calc), so the worked
    # example and the appendix table are guaranteed to show the same values.
    m = pair_metrics(M1, R1, M2, R2)

    # K via D_crit route (= M/(R*Dcrit) = k_d)  -- this is also what DTD uses.
    K1 = m['D_1_norm']; K2 = m['D_2_norm']
    DTD1 = m['dtd_1']; DTD2 = m['dtd_2']
    dtd_ratio = m['dtd_1/dtd_2']

    # GTD-from-DTD route (DeGerlia): gtd_d = sqrt(1 - k_d)
    one_m1 = D(1) - DTD1 ** 2          # = 1 - K1
    one_m2 = D(1) - DTD2 ** 2
    g1_d = m['gtd_d_1']; g2_d = m['gtd_d_2']

    # Schwarzschild route: k_s = r_s/R, gtd_s = sqrt(1 - k_s)
    rs1 = m['r_s_1 (m)']; rs2 = m['r_s_2 (m)']
    Ks1 = m['k_s_1']; Ks2 = m['k_s_2']
    g1_s = m['gtd_1']; g2_s = m['gtd_2']

    # GTD ratios: the LARGER GTD always goes in the denominator so the ratio
    # is <= 1 (a GTD ratio is never inverted to exceed unity). Pick top/bottom
    # subscripts accordingly, per route. (DTD ratios have no such constraint.)
    if g1_d <= g2_d:
        gd_top, gd_bot, gd_topv, gd_botv = '1', '2', g1_d, g2_d
    else:
        gd_top, gd_bot, gd_topv, gd_botv = '2', '1', g2_d, g1_d
    gtd_ratio_d = gd_topv / gd_botv
    if g1_s <= g2_s:
        gs_top, gs_bot, gs_topv, gs_botv = '1', '2', g1_s, g2_s
    else:
        gs_top, gs_bot, gs_topv, gs_botv = '2', '1', g2_s, g1_s
    gtd_ratio_s = gs_topv / gs_botv

    kgpm = r'\,\unit[per-mode=symbol]{\kilogram\per\meter}'
    INDENT = r'1.5em'   # one shared indent for all content under headings
    L = []
    A = L.append

    # --- Heading helpers (single source of truth for block typography) -------
    # Spacing model (deliberately uniform, no per-heading magic):
    #   * Every heading is flush-left at the box margin.
    #   * Every piece of content under a heading -- table AND math -- is indented
    #     by ONE shared amount (INDENT), via \mathindent (fleqn) for math and an
    #     \hspace* for the table. Two clean horizontal levels, nothing else.
    #   * The vertical gap above every heading is the previous block's
    #     \belowdisplayskip; the gap below is \abovedisplayskip. Both are set to
    #     the SAME value below, so every heading has identical space above and
    #     below it regardless of what precedes it.
    # title : large bold name line.  sub : bold section heading.
    # lbl   : plain (non-bold) inline label for sub-steps within a section.
    def title(text): A(r'{\large\textbf{' + text + r'}}\par\vspace{\belowdisplayskip}')
    def sub(text):   A(r'\noindent\textbf{' + text + r'}\par\nobreak')
    def lbl(text):   A(r'\noindent ' + text + r'\par\nobreak')
    def eq(*rows):
        A(r'\begin{align*}')
        for r in rows:
            A(r)
        A(r'\end{align*}')

    # j(): build one aligned equation row "LHS &= p0 = p1 = ...". Pieces are
    # joined inline with ' = ', EXCEPT a piece is pushed onto a new aligned
    # continuation line ("\\ &= piece") when it (or the running line) would be
    # too wide -- so the full-precision nines-heavy numbers never overflow the
    # column. No digits are ever dropped; only the line wraps. WIDE = max chars
    # allowed on a line before forcing a break.
    import re as _re
    WIDE = 46
    def _w(s):
        # rough rendered width: drop trailing annotations (\quad, \text{...})
        # which don't drive wrapping, strip TeX control words/markup, count
        # what's left, then add back the thin spaces siunitx inserts every 3
        # digits (so a 33-digit number reads as wide as it actually renders).
        t = _re.sub(r'\\quad', '', s)
        t = _re.sub(r'\\text\{[^}]*\}', '', t)
        t = _re.sub(r'\\[a-zA-Z]+|[{}\\$]', '', t)
        digits = sum(c.isdigit() for c in t)
        t = t.replace(',', '')
        return len(t) + digits // 3
    def j(lhs, *pieces):
        line = lhs + r' &= ' + pieces[0]
        cur = _w(lhs) + 2 + _w(pieces[0])
        for p in pieces[1:]:
            if cur + 3 + _w(p) > WIDE:
                line += r'\\' + '\n' + r'&\quad = ' + p
                cur = 4 + _w(p)
            else:
                line += r' = ' + p
                cur += 3 + _w(p)
        return line

    A(r'\begin{mdframed}')
    # Typography: pair-table font size; one symmetric display skip drives all
    # heading gaps; jot controls inter-row gap inside align; mathindent gives
    # math the same indent as the table.
    A(r'\fontsize{7}{8.5}\selectfont')
    # No gap between a heading and the math right under it (abovedisplayskip=0);
    # section separation comes from belowdisplayskip above the next heading.
    A(r'\setlength{\abovedisplayskip}{0pt}\setlength{\belowdisplayskip}{4pt}')
    A(r'\setlength{\abovedisplayshortskip}{0pt}\setlength{\belowdisplayshortskip}{4pt}')
    A(r'\setlength{\jot}{1pt}')
    A(r'\setlength{\mathindent}{' + INDENT + r'}')

    title('Example (' + name + '):')

    sub('System properties:')
    # Left-indented, vertically tight table (reduced row height + zero rule pad).
    A(r'{\renewcommand{\arraystretch}{0.9}'
      r'\setlength{\aboverulesep}{0pt}\setlength{\belowrulesep}{0pt}'
      r'\setlength{\extrarowheight}{0pt}')
    A(r'\hspace*{' + INDENT + r'}\begin{tabular}{@{}l l@{\hspace{1.5em}} l@{}}')
    A(r'\toprule')
    A(r' & System 1 ($S_1$) & System 2 ($S_2$) \\')
    A(r'\midrule')
    A(r'$M$ (\unit{\kilogram}) & ' + num(M1) + ' & ' + num(M2) + r' \\')
    A(r'$R$ (\unit{\meter}) & ' + num(R1) + ' & ' + num(R2) + r' \\')
    A(r'\bottomrule')
    A(r'\end{tabular}}\par\vspace{\belowdisplayskip}')

    sub('Calculate DTD for each System:')
    eq(
        r'\mathrm{DTD} &= \sqrt{K} \quad\text{where}\quad K = M/(R\,D_{\mathrm{crit}})\\',
        r'\quad K_1 &= \dfrac{' + num(M1) + r'\,\unit{\kilogram}}{(' + num(R1) + r'\,\unit{\meter})(' + num(Dc) + kgpm + r')} = ' + num(K1) + r'\\',
        r'\mathrm{DTD}_1 &= \sqrt{' + num(K1) + r'} = ' + num(DTD1) + r'\\',
        r'\quad K_2 &= \dfrac{' + num(M2) + r'\,\unit{\kilogram}}{(' + num(R2) + r'\,\unit{\meter})(' + num(Dc) + kgpm + r')} = ' + num(K2) + r'\\',
        r'\mathrm{DTD}_2 &= \sqrt{' + num(K2) + r'} = ' + num(DTD2) + r'\\',
        r'\dfrac{\mathrm{DTD}_1}{\mathrm{DTD}_2} &= \dfrac{' + num(DTD1) + r'}{' + num(DTD2) + r'} = ' + num(dtd_ratio),
    )

    sub('Calculate GTD ratio from DTD:')
    # Larger GTD in the denominator (gd_top / gd_bot), so the ratio stays <= 1.
    dtt, dtb = ('DTD_' + gd_top), ('DTD_' + gd_bot)
    DTt, DTb = (DTD1 if gd_top == '1' else DTD2), (DTD1 if gd_bot == '1' else DTD2)
    Kt, Kb = (K1 if gd_top == '1' else K2), (K1 if gd_bot == '1' else K2)
    omt, omb = (one_m1 if gd_top == '1' else one_m2), (one_m1 if gd_bot == '1' else one_m2)
    eq(
        j(r'\dfrac{\mathrm{GTD}_' + gd_top + r'}{\mathrm{GTD}_' + gd_bot + r'}',
          r'\dfrac{\sqrt{1-\mathrm{' + dtt + r'}^2}}{\sqrt{1-\mathrm{' + dtb + r'}^2}}',
          r'\dfrac{\sqrt{1-(' + num(DTt) + r')^2}}{\sqrt{1-(' + num(DTb) + r')^2}}',
          r'\dfrac{\sqrt{1-' + num(Kt) + r'}}{\sqrt{1-' + num(Kb) + r'}}',
          r'\dfrac{\sqrt{' + num(omt) + r'}}{\sqrt{' + num(omb) + r'}}',
          r'\dfrac{' + num(gd_topv) + r'}{' + num(gd_botv) + r'}',
          num(gtd_ratio_d),
          r'1-' + num(D(1) - gtd_ratio_d)),
    )

    sub('Verify by Calculating GTD from Schwarzschild Radius Ratio:')
    lbl('Schwarzschild radii:')
    eq(
        r'r_{s1} &= \dfrac{2GM_1}{c^2} = \dfrac{2(' + num(G) + r'\,\unit{\meter\cubed\per\kilogram\per\second\squared})(' + num(M1) + r'\,\unit{\kilogram})}{(' + num(c) + r'\,\unit{\meter\per\second})^2}\\',
        r'&= ' + num(rs1) + r'\,\unit{\meter}\\',
        r'r_{s2} &= \dfrac{2GM_2}{c^2} = \dfrac{2(' + num(G) + r'\,\unit{\meter\cubed\per\kilogram\per\second\squared})(' + num(M2) + r'\,\unit{\kilogram})}{(' + num(c) + r'\,\unit{\meter\per\second})^2}\\',
        r'&= ' + num(rs2) + r'\,\unit{\meter}',
    )
    lbl(r'Calculate $K$ values from the $r_s/R$ ratio:')
    eq(
        r'K_1 &= \dfrac{r_{s1}}{R_1} &&= \dfrac{' + num(rs1) + r'\,\unit{\meter}}{' + num(R1) + r'\,\unit{\meter}} &&= ' + num(Ks1) + r'\\',
        r'K_2 &= \dfrac{r_{s2}}{R_2} &&= \dfrac{' + num(rs2) + r'\,\unit{\meter}}{' + num(R2) + r'\,\unit{\meter}} &&= ' + num(Ks2),
    )
    lbl('Calculate GTD via Schwarzschild radius ratio:')
    eq(
        j(r'\mathrm{GTD}_1', r'\sqrt{1-K_1}', r'\sqrt{' + num(D(1) - Ks1) + r'}', num(g1_s), r'1-' + num(D(1) - g1_s)) + r'\\',
        j(r'\mathrm{GTD}_2', r'\sqrt{1-K_2}', r'\sqrt{' + num(D(1) - Ks2) + r'}', num(g2_s), r'1-' + num(D(1) - g2_s)) + r'\\',
        j(r'\dfrac{\mathrm{GTD}_' + gs_top + r'}{\mathrm{GTD}_' + gs_bot + r'}', r'\dfrac{' + num(gs_topv) + r'}{' + num(gs_botv) + r'}', num(gtd_ratio_s), r'1-' + num(D(1) - gtd_ratio_s)),
    )

    # Heading names the systems in the direction actually computed (numerator
    # first), since that order names the comparator.
    sub('Time-dilation ratio between System ' + gs_top + ' and System ' + gs_bot + ', computed two ways:')
    # Reuse the already-computed/presented ratios -- equation use only, no
    # second 1-x presentation. Larger GTD stays in the denominator (subscripts
    # match each route's ordering above).
    eq(
        r'&\dfrac{\mathrm{GTD}_' + gs_top + r'}{\mathrm{GTD}_' + gs_bot + r'} = ' + num(gtd_ratio_s) + r' \quad \text{(via $r_s$)}\\',
        r'&\dfrac{\mathrm{GTD}_' + gd_top + r'}{\mathrm{GTD}_' + gd_bot + r'} = ' + num(gtd_ratio_d) + r' \quad \text{(via $D_{\mathrm{crit}}$)}',
    )
    if caption:
        A(r'\par' + caption)
    A(r'\end{mdframed}')
    return '\n'.join(L)


if __name__ == '__main__':
    if len(sys.argv) == 6:
        name = sys.argv[1]
        M1, R1, M2, R2 = sys.argv[2:6]
        cap = None
        print(build_block(name, M1, R1, M2, R2, caption=cap))
    else:
        # Default: reproduce the General Case block for verification.
        name, M1, R1, M2, R2 = 'General Case', '1e20', '2e-7', '1e30', '1e7'
        cap = (r'This case is tabulated in Table~\ref{tab:pair_ratios}, '
               r'column General of \ref{app:pair_table}.')
        print(build_block(name, M1, R1, M2, R2, caption=cap))
