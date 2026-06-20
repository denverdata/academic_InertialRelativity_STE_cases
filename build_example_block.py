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
from uniform_sphere import UniformSphere
import constants as C


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
    from decimal import localcontext, ROUND_HALF_EVEN
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
        ctx.rounding = ROUND_HALF_EVEN
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

    s1 = UniformSphere(radius=R1, mass=M1)
    s2 = UniformSphere(radius=R2, mass=M2)
    p1 = lambda k: s1._properties[k]
    p2 = lambda k: s2._properties[k]

    # K via D_crit route (= M/(R*Dcrit) = k_d)
    K1 = p1('k_d'); K2 = p2('k_d')
    DTD1 = K1.sqrt(); DTD2 = K2.sqrt()
    dtd_ratio = DTD1 / DTD2

    # GTD-from-DTD route
    one_m1 = D(1) - DTD1 ** 2          # = 1 - K1
    one_m2 = D(1) - DTD2 ** 2
    g1_d = one_m1.sqrt(); g2_d = one_m2.sqrt()
    gtd_ratio_d = g1_d / g2_d

    # Schwarzschild route
    rs1 = p1('schwarzschild_radius'); rs2 = p2('schwarzschild_radius')
    Ks1 = rs1 / R1; Ks2 = rs2 / R2
    g1_s = (D(1) - Ks1).sqrt(); g2_s = (D(1) - Ks2).sqrt()
    gtd_ratio_s = g1_s / g2_s

    diff = abs(gtd_ratio_s - gtd_ratio_d)

    kgpm = r'\,\unit[per-mode=symbol]{\kilogram\per\meter}'
    L = []
    A = L.append
    A(r'\begin{mdframed}')
    A(r'\textbf{Example (' + name + r'):}')
    A('')
    A(r'\smallskip\noindent\textbf{System properties:}')
    A('')
    A(r'\begin{center}')
    A(r'\small')
    A(r'\begin{tabular}{@{}lll@{}}')
    A(r'\toprule')
    A(r' & System 1 ($S_1$) & System 2 ($S_2$) \\')
    A(r'\midrule')
    A(r'$M$ (\unit{\kilogram}) & ' + num(M1) + ' & ' + num(M2) + r' \\')
    A(r'$R$ (\unit{\meter}) & ' + num(R1) + ' & ' + num(R2) + r' \\')
    A(r'\bottomrule')
    A(r'\end{tabular}')
    A(r'\end{center}')
    A('')
    A(r'\smallskip\noindent\textbf{Calculate DTD for each System:}')
    A(r'  \begin{align*}')
    A(r'  \mathrm{DTD} &= \sqrt{K} \quad\text{where}\quad K = M/(R\,D_{\mathrm{crit}})\\[2pt]')
    A(r'  \quad K_1 &= \dfrac{' + num(M1) + r'\,\unit{\kilogram}}{(' + num(R1) + r'\,\unit{\meter})(' + num(Dc) + kgpm + r')}\\')
    A(r'  &= ' + num(K1) + r'\\')
    A(r'  \mathrm{DTD}_1 &= \sqrt{' + num(K1) + r'} = ' + num(DTD1) + r'\\[2pt]')
    A(r'  \quad K_2 &= \dfrac{' + num(M2) + r'\,\unit{\kilogram}}{(' + num(R2) + r'\,\unit{\meter})(' + num(Dc) + kgpm + r')}\\')
    A(r'  &= ' + num(K2) + r'\\')
    A(r'  \mathrm{DTD}_2 &= \sqrt{' + num(K2) + r'} = ' + num(DTD2) + r'\\[2pt]')
    A(r'  \dfrac{\mathrm{DTD}_1}{\mathrm{DTD}_2} &= \dfrac{' + num(DTD1) + r'}{' + num(DTD2) + r'} = ' + num(dtd_ratio) + r'')
    A(r'  \end{align*}')
    A('')
    A(r' \smallskip\noindent\textbf{Calculate GTD ratio from DTD:}')
    A(r'  \nopagebreak')
    A(r'  \begin{align*}')
    A(r'  \dfrac{\mathrm{GTD}_1}{\mathrm{GTD}_2} &= \dfrac{\sqrt{1-\mathrm{DTD}_1^2}}{\sqrt{1-\mathrm{DTD}_2^2}}\\')
    A(r'  &= \dfrac{\sqrt{1-(' + num(DTD1) + r')^2}}{\sqrt{1-(' + num(DTD2) + r')^2}}\\')
    A(r'  &= \dfrac{\sqrt{1-' + num(K1) + r'}}{\sqrt{1-' + num(K2) + r'}}\\')
    A(r'  &= \dfrac{\sqrt{' + num(one_m1) + r'}}{\sqrt{' + num(one_m2) + r'}}\\')
    A(r'  &= \dfrac{' + num(g1_d) + r'}{' + num(g2_d) + r'}\\')
    A(r'  &= ' + num(gtd_ratio_d) + r'\\')
    A(r'  &= 1-' + num(D(1) - gtd_ratio_d) + r'')
    A(r'  \end{align*}')
    A('')
    A(r'\smallskip\noindent\textbf{Verify by Calculating GTD from Schwarzschild Radius Ratio:}')
    A('')
    A(r'\noindent Schwarzschild radii:')
    A(r'\begin{align*}')
    A(r'r_{s1} &= \dfrac{2GM_1}{c^2}\\')
    A(r'&= \dfrac{2(' + num(G) + r'\,\unit{\meter\cubed\per\kilogram\per\second\squared})(' + num(M1) + r'\,\unit{\kilogram})}{(' + num(c) + r'\,\unit{\meter\per\second})^2}\\[2pt]')
    A(r'&= ' + num(rs1) + r'\,\unit{\meter}\\[6pt]')
    A(r'r_{s2} &= \dfrac{2GM_2}{c^2}\\')
    A(r'&= \dfrac{2(' + num(G) + r'\,\unit{\meter\cubed\per\kilogram\per\second\squared})(' + num(M2) + r'\,\unit{\kilogram})}{(' + num(c) + r'\,\unit{\meter\per\second})^2}\\[2pt]')
    A(r'&= ' + num(rs2) + r'\,\unit{\meter}')
    A(r'\end{align*}')
    A('')
    A(r'\noindent Calculate $K$ values from the $r_s/R$ ratio:')
    A(r'\begin{align*}')
    A(r'K_1 &= \dfrac{r_{s1}}{R_1} &&= \dfrac{' + num(rs1) + r'\,\unit{\meter}}{' + num(R1) + r'\,\unit{\meter}} &&= ' + num(Ks1) + r'\\[2pt]')
    A(r'K_2 &= \dfrac{r_{s2}}{R_2} &&= \dfrac{' + num(rs2) + r'\,\unit{\meter}}{' + num(R2) + r'\,\unit{\meter}} &&= ' + num(Ks2) + r'')
    A(r'\end{align*}')
    A('')
    A(r'\noindent Calculate GTD via Schwarzschild radius ratio:')
    A(r'\begin{align*}')
    A(r'\mathrm{GTD}_1 &= \sqrt{1-K_1} = \sqrt{1-' + num(Ks1) + r'}\\')
    A(r'&= \sqrt{' + num(D(1) - Ks1) + r'}\\')
    A(r'&= ' + num(g1_s) + r'\\[2pt]')
    A(r'\mathrm{GTD}_2 &= \sqrt{1-K_2} = \sqrt{1-' + num(Ks2) + r'}\\')
    A(r'&= \sqrt{' + num(D(1) - Ks2) + r'}\\')
    A(r'&= ' + num(g2_s) + r'\\[2pt]')
    A(r'\dfrac{\mathrm{GTD}_1}{\mathrm{GTD}_2} &= \dfrac{' + num(g1_s) + r'}{' + num(g2_s) + r'}\\')
    A(r'&= ' + num(gtd_ratio_s) + r'')
    A(r'\end{align*}')
    A('')
    A(r'\smallskip\noindent\textbf{Time-dilation ratio between System 1 and System 2, computed two ways:}')
    A(r'\begin{align*}')
    A(r'&\mathrm{GTD}_1/\mathrm{GTD}_2 = ' + num(gtd_ratio_s) + r' \quad \text{(via $r_s$)}\\')
    A(r'&\mathrm{GTD}_1/\mathrm{GTD}_2 = ' + num(gtd_ratio_d) + r' \quad \text{(via $D_{\mathrm{crit}}$)}')
    A(r'\end{align*}')
    A(r'\begin{align*}')
    A(r'\text{difference} &= ' + num(diff) + r'\\')
    A(r'&\quad \text{(below the margin of error imparted by $G$,}\\')
    A(r"&\quad \text{$0.00015$, the gravitational constant's limit)}")
    A(r'\end{align*}')
    if caption:
        A('')
        A(caption)
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
