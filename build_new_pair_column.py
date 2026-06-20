#!/usr/bin/env python3
"""Author one new column for pair_comparisons_v2_cases.md, computed exactly the
way every other column was: by driving the canonical system_properties engine
(UniformSphere) for the two systems. No formulas are reimplemented here for the
per-system rows -- they are read straight off the UniformSphere properties.
Inter-system ratio rows are simple Decimal ratios of those engine values.

New case:  M=M, R_1 = 4/3 r_s
  System 1: M = 1e30 kg, R_1 = 4/3 * r_s(M)   (= 1980.309... m)
  System 2: M = 1e30 kg, R_2 = 1e8 m

Output: the 45 metric rows in the file's exact 50-sig-digit E-notation, one per
line as `<label> = <value>`, for hand-insertion as a new column.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'system_properties'))
from decimal import Decimal as D, getcontext
getcontext().prec = 50
from uniform_sphere import UniformSphere
import constants as C

# --- Define the two systems via the canonical engine ---------------------
M = D('1e30')
rs = D(2) * C.G * M / (C.SPEED_OF_LIGHT ** 2)   # same expression UniformSphere uses
R1 = D(4) / D(3) * rs
R2 = D('1e8')

s1 = UniformSphere(radius=R1, mass=M)
s2 = UniformSphere(radius=R2, mass=M)
p1 = lambda k: s1._properties[k]
p2 = lambda k: s2._properties[k]

# Per-system rows: read directly from the engine ---------------------------
m_1   = s1.mass;   m_2   = s2.mass
r_1   = s1.radius; r_2   = s2.radius
rho_1 = p1('density');               rho_2 = p2('density')
I_1   = p1('moment_of_inertia');     I_2   = p2('moment_of_inertia')
D_1   = p1('degerlia_compactness');  D_2   = p2('degerlia_compactness')
D1n   = p1('k_d');                   D2n   = p2('k_d')   # D/D_crit
rs_1  = p1('schwarzschild_radius');  rs_2  = p2('schwarzschild_radius')
gtd_1 = p1('gtd_s');                 gtd_2 = p2('gtd_s')
ks_1  = p1('k_s');                   ks_2  = p2('k_s')
gtdd_1= p1('gtd_d');                 gtdd_2= p2('gtd_d')
dtd_1 = ks_1.sqrt();                 dtd_2 = ks_2.sqrt()   # DTD = sqrt(k_s)

# Inter-system ratio rows: ratios of the engine values ---------------------
rows = [
    ('m_1 (kg)', m_1), ('m_2 (kg)', m_2),
    ('r_1 (m)', r_1),  ('r_2 (m)', r_2),
    ('ρ_1 (kg/m³)', rho_1), ('ρ_2 (kg/m³)', rho_2),
    ('I_1 (kg·m²)', I_1),   ('I_2 (kg·m²)', I_2),
    ('D_1 (kg/m)', D_1),    ('D_2 (kg/m)', D_2),
    ('D_1_norm', D1n),      ('D_2_norm', D2n),
    ('r_s_1 (m)', rs_1),    ('r_s_2 (m)', rs_2),
    ('gtd_1', gtd_1),       ('gtd_2', gtd_2),
    ('k_s_1', ks_1),        ('k_s_2', ks_2),
    ('gtd_d_1', gtdd_1),    ('gtd_d_2', gtdd_2),
    ('dtd_1', dtd_1),       ('dtd_2', dtd_2),
    ('dtd_1/dtd_2', dtd_1 / dtd_2),
    ('sqrt(D_1/D_2)', (D_1 / D_2).sqrt()),
    ('sqrt((m_1·r_2)/(m_2·r_1))', ((m_1 * r_2) / (m_2 * r_1)).sqrt()),
    ('sqrt((I_1/I_2)*(r_2/r_1)³)', ((I_1 / I_2) * (r_2 / r_1) ** 3).sqrt()),
    ('(I_1/I_2)^(1/5)*(ρ_1/ρ_2)^(3/10)', (I_1 / I_2) ** (D(1) / D(5)) * (rho_1 / rho_2) ** (D(3) / D(10))),
    ('(m_2·r_1)/(m_1·r_2)', (m_2 * r_1) / (m_1 * r_2)),
    ('(m_1·r_2)/(m_2·r_1)', (m_1 * r_2) / (m_2 * r_1)),
    ('(*k) D_2/D_1', D_2 / D_1),
    ('(*k) D_1/D_2', D_1 / D_2),
    ('(I_1/I_2)*(r_2/r_1)³', (I_1 / I_2) * (r_2 / r_1) ** 3),
    ('I_1/I_2', I_1 / I_2),
    ('(I_1/I_2)^(1/2)', (I_1 / I_2).sqrt()),
    ('k_i=(ρ_1/ρ_2)^(1/5)*(r_1/r_2)', (rho_1 / rho_2) ** (D(1) / D(5)) * (r_1 / r_2)),
    ('(I_1/I_2)^(1/5)', (I_1 / I_2) ** (D(1) / D(5))),
    ('(dtd_1/dtd_2)²*(r_1/r_2)³', (dtd_1 / dtd_2) ** 2 * (r_1 / r_2) ** 3),
    ('(*G) gtd_1/gtd_2', gtd_1 / gtd_2),
    ('sqrt(1-dtd_1²)/sqrt(1-dtd_2²)', (D(1) - dtd_1 ** 2).sqrt() / (D(1) - dtd_2 ** 2).sqrt()),
    ('(*k) k_m=m_1/m_2', m_1 / m_2),
    ('(*k) k_r=r_1/r_2', r_1 / r_2),
    ('r_2/r_1', r_2 / r_1),
    ('sqrt(r_2/r_1)', (r_2 / r_1).sqrt()),
    ('sqrt(m_1/m_2)', (m_1 / m_2).sqrt()),
    ('sqrt(m_2²r_2/(m_1²r_1))', ((m_2 * m_2 * r_2) / (m_1 * m_1 * r_1)).sqrt()),
]

def efmt(x):
    """50 sig digits, E+exp notation, matching the source file."""
    return f'{x:.49E}'

for label, val in rows:
    print(f'{label}\t{efmt(D(val))}')
