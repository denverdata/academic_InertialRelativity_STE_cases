#!/usr/bin/env python3
"""Single calculation core for a two-system pair.

This is the ONE place pair quantities are computed. Both the appendix table
(generate_pair_table.py) and the worked example blocks (build_example_block.py)
pull their numbers from pair_metrics() so the two presentations are, by
construction, the same numbers -- not two methods that happen to agree.

All per-system primitives come straight from system_properties/UniformSphere
(the validated engine that also produced pair_comparisons_v2_cases.md). Derived
rows are exact Decimal combinations of those primitives. Returns a dict keyed by
the same row labels used in pair_comparisons_v2_cases.md.
"""
import os, sys
from decimal import Decimal as D, getcontext
getcontext().prec = 50

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'system_properties'))
from uniform_sphere import UniformSphere   # noqa: E402


def pair_metrics(M1, R1, M2, R2):
    """Return {row_label: Decimal} for one system pair, computed once via
    UniformSphere. M*/R* may be numbers or numeric strings."""
    s1 = UniformSphere(radius=D(str(R1)), mass=D(str(M1)))
    s2 = UniformSphere(radius=D(str(R2)), mass=D(str(M2)))
    p1 = lambda k: s1._properties[k]
    p2 = lambda k: s2._properties[k]

    # Per-system primitives (straight from the engine).
    m1, m2 = s1.mass, s2.mass
    r1, r2 = s1.radius, s2.radius
    rho1, rho2 = p1('density'), p2('density')
    I1, I2 = p1('moment_of_inertia'), p2('moment_of_inertia')
    Dc1, Dc2 = p1('degerlia_compactness'), p2('degerlia_compactness')
    D1n, D2n = p1('k_d'), p2('k_d')                  # D / D_crit
    rs1, rs2 = p1('schwarzschild_radius'), p2('schwarzschild_radius')
    gs1, gs2 = p1('gtd_s'), p2('gtd_s')              # sqrt(1 - r_s/R)
    ks1, ks2 = p1('k_s'), p2('k_s')                  # r_s / R
    gd1, gd2 = p1('gtd_d'), p2('gtd_d')              # sqrt(1 - D/D_crit)
    # DTD = sqrt(k_d) -- the DeGerlia route (D/D_crit via the 6-digit D_crit),
    # matching how dtd was computed in pair_comparisons_v2_cases.md. Using k_s
    # (r_s/R) instead would drift in the last digit through D_crit's precision.
    dtd1, dtd2 = D1n.sqrt(), D2n.sqrt()

    return {
        'm_1 (kg)': m1, 'm_2 (kg)': m2,
        'r_1 (m)': r1, 'r_2 (m)': r2,
        'ρ_1 (kg/m³)': rho1, 'ρ_2 (kg/m³)': rho2,
        'I_1 (kg·m²)': I1, 'I_2 (kg·m²)': I2,
        'D_1 (kg/m)': Dc1, 'D_2 (kg/m)': Dc2,
        'D_1_norm': D1n, 'D_2_norm': D2n,
        'r_s_1 (m)': rs1, 'r_s_2 (m)': rs2,
        'gtd_1': gs1, 'gtd_2': gs2,
        'k_s_1': ks1, 'k_s_2': ks2,
        'gtd_d_1': gd1, 'gtd_d_2': gd2,
        'dtd_1': dtd1, 'dtd_2': dtd2,
        'dtd_1/dtd_2': dtd1 / dtd2,
        'sqrt(D_1/D_2)': (Dc1 / Dc2).sqrt(),
        'sqrt((m_1·r_2)/(m_2·r_1))': ((m1 * r2) / (m2 * r1)).sqrt(),
        'sqrt((I_1/I_2)*(r_2/r_1)³)': ((I1 / I2) * (r2 / r1) ** 3).sqrt(),
        '(I_1/I_2)^(1/5)*(ρ_1/ρ_2)^(3/10)': (I1 / I2) ** (D(1) / D(5)) * (rho1 / rho2) ** (D(3) / D(10)),
        '(m_2·r_1)/(m_1·r_2)': (m2 * r1) / (m1 * r2),
        '(m_1·r_2)/(m_2·r_1)': (m1 * r2) / (m2 * r1),
        '(*k) D_2/D_1': Dc2 / Dc1,
        '(*k) D_1/D_2': Dc1 / Dc2,
        '(I_1/I_2)*(r_2/r_1)³': (I1 / I2) * (r2 / r1) ** 3,
        'I_1/I_2': I1 / I2,
        '(I_1/I_2)^(1/2)': (I1 / I2).sqrt(),
        'k_i=(ρ_1/ρ_2)^(1/5)*(r_1/r_2)': (rho1 / rho2) ** (D(1) / D(5)) * (r1 / r2),
        '(I_1/I_2)^(1/5)': (I1 / I2) ** (D(1) / D(5)),
        '(dtd_1/dtd_2)²*(r_1/r_2)³': (dtd1 / dtd2) ** 2 * (r1 / r2) ** 3,
        '(*G) gtd_1/gtd_2': gs1 / gs2,
        'sqrt(1-dtd_1²)/sqrt(1-dtd_2²)': (D(1) - dtd1 ** 2).sqrt() / (D(1) - dtd2 ** 2).sqrt(),
        'GTD_d_1/GTD_d_2': gd1 / gd2,
        '(*k) k_m=m_1/m_2': m1 / m2,
        '(*k) k_r=r_1/r_2': r1 / r2,
        'r_2/r_1': r2 / r1,
        'sqrt(r_2/r_1)': (r2 / r1).sqrt(),
        'sqrt(r_1/r_2)': (r1 / r2).sqrt(),
        'sqrt(m_1/m_2)': (m1 / m2).sqrt(),
        'sqrt(m_2²r_2/(m_1²r_1))': ((m2 * m2 * r2) / (m1 * m1 * r1)).sqrt(),
    }
