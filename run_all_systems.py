#!/usr/bin/env python3
"""
Run all systems through UniformSphere and output to systems_output.md,
then build systems_table.md by parsing systems_output.md.
"""

import sys
import os
import re
import io
import math
from decimal import Decimal, getcontext
from contextlib import redirect_stdout

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'system_properties'))

from system_properties.uniform_sphere import UniformSphere  # noqa: E402
from system_properties import constants  # noqa: E402

# Override precision after import (constants.py sets it to 50)
getcontext().prec = 100

# Define all systems: (number, mass, radius)
SYSTEMS = [
    (1,  '1.98847e30', '6.96342e8'),
    (2,  '1.98847e30', '3.93779e3'),
    (3,  '1e30',     '1e8'),
    (4,  '1e24',     '1e8'),
    (5,  '1e30',     '1e8'),
    (6,  '1e27',     '1e7'),
    (7,  '1e33',     '1e7'),
    (8,  '1e31',     '1e5'),
    (9,  '1e30',     '1e8'),
    (10, '1e20',     '1e7'),
    (11, '1e32',     '1e6'),
]


def generate_output(output_path):
    """
    Step 1: Run each system through UniformSphere, compute derived values,
    and write everything to systems_output.md.
    """
    # First pass: run all systems, collect data
    system_data = []
    for num, mass, radius in SYSTEMS:
        sphere = UniformSphere(radius=radius, mass=mass, name='Sphere from CLI parameters')

        # Capture print_properties output
        f = io.StringIO()
        with redirect_stdout(f):
            sphere.print_properties()
        props_output = f.getvalue()

        p = sphere._properties
        gtd = p['gravitational_time_dilation']
        k = Decimal('1') - gtd * gtd

        system_data.append({
            'num': num,
            'mass': mass,
            'radius': radius,
            'props_output': props_output,
            'gtd': gtd,
            'k': k,
            'radius_dec': Decimal(radius),
            'mass_dec': Decimal(mass),
            'moi_dec': p['moment_of_inertia'],
            'rs_dec': p['schwarzschild_radius'],
        })

    # Second pass: compute ratios and write output
    output_lines = ['# System Properties Output\n']

    for idx, sd in enumerate(system_data):
        prev_idx = (idx - 1) % len(system_data)
        prev = system_data[prev_idx]

        r_ratio = sd['radius_dec'] / prev['radius_dec']
        m_ratio = sd['mass_dec'] / prev['mass_dec']
        i_ratio = sd['moi_dec'] / prev['moi_dec']
        gtd_ratio = sd['gtd'] / prev['gtd']
        m_ratio_cbrt = m_ratio ** (Decimal('1') / Decimal('3'))
        i_ratio_5rt = i_ratio ** (Decimal('1') / Decimal('5'))
        rs_over_r = sd['rs_dec'] / sd['radius_dec']
        prev_rs_over_r = prev['rs_dec'] / prev['radius_dec']
        rs_r_ratio = rs_over_r / prev_rs_over_r
        k_over_k_prev = sd['k'] / prev['k'] if prev['k'] != 0 else Decimal('Infinity')

        # Format inputs to 6 significant figures
        m_float = float(sd['mass'])
        m_base, m_exp = f'{m_float:.5e}'.split('e')
        mass_fmt = f'{m_base}e{int(m_exp)}'
        r_float = float(sd['radius'])
        r_base, r_exp = f'{r_float:.5e}'.split('e')
        radius_fmt = f'{r_base}e{int(r_exp)}'

        output_lines.append(f'\n## System {sd["num"]}')
        output_lines.append(f'Mass: {mass_fmt} kg, Radius: {radius_fmt} m')
        output_lines.append('')

        output_lines.append('```')
        output_lines.append(sd['props_output'].rstrip())
        output_lines.append('```')

        output_lines.append(f"**Derived:** k = 1 - GTD² = {sd['k']:.50e}  ")
        output_lines.append(f"**Derived:** R/R_prev = {r_ratio:.50e}  ")
        output_lines.append(f"**Derived:** M/M_prev = {m_ratio:.50e}  ")
        output_lines.append(f"**Derived:** I/I_prev = {i_ratio:.50e}  ")
        output_lines.append(f"**Derived:** (M/M_prev)^(1/3) = {m_ratio_cbrt:.50e}  ")
        output_lines.append(f"**Derived:** (I/I_prev)^(1/5) = {i_ratio_5rt:.50e}  ")
        output_lines.append(f"**Derived:** GTD/GTD_prev = {gtd_ratio:.50e}  ")
        output_lines.append(f"**Derived:** r_s/R = {rs_over_r:.50e}  ")
        output_lines.append(f"**Derived:** (r_s/R)/(r_s/R)_prev = {rs_r_ratio:.50e}  ")
        output_lines.append(f"**Derived:** k/k_prev = {k_over_k_prev:.50e}")
        output_lines.append('')

    with open(output_path, 'w') as f:
        f.write('\n'.join(output_lines))



def format_gtd(val_str):
    """Format GTD: show the leading digit and all 9s, plus six digits past the last 9."""
    val_str = val_str.split()[0]
    gtd = Decimal(val_str)
    # Get the scientific notation: X.XXXeN
    sign, digits, exponent = gtd.normalize().as_tuple()
    # Convert to string with plenty of digits
    gtd_str = format(gtd, '.45e')
    # Split into coefficient and exponent
    coeff, exp = gtd_str.split('e')
    integer_part, dec_part = coeff.split('.')
    # Count leading 9s in the decimal part
    nine_count = 0
    for ch in dec_part:
        if ch == '9':
            nine_count += 1
        else:
            break
    # Show six digits past the last 9
    six_digits = dec_part[nine_count:nine_count + 6]
    nines = '9' * nine_count
    return f"{integer_part}.{nines}{six_digits}e{int(exp)}"


def format_sci6(val_str):
    """Format a numeric string to scientific notation with 6 significant figures."""
    f = float(val_str)
    if f == 0:
        return '0.00000e0'
    s = f'{f:.5e}'
    base, exp = s.split('e')
    exp_val = int(exp)
    return f'{base}e{exp_val}'


def build_table(output_path, table_path):
    """
    Step 2: Parse systems_output.md and build systems_table.md.
    All values come from the output sheet.
    """
    with open(output_path, 'r') as f:
        content = f.read()

    # Split into system sections
    sections = re.split(r'\n## System (\d+)\n', content)
    # sections[0] is header, then alternating: number, body

    table_rows = []
    for i in range(1, len(sections), 2):
        num = sections[i]
        body = sections[i + 1]

        # Parse fields from the code block and derived lines
        def get(pattern: str, text: str) -> str:
            match = re.search(pattern, text)
            if match is None:
                raise ValueError(f"System {num}: pattern not found: {pattern}")
            return match.group(1)

        table_rows.append({
            'num': num,
            'radius': format_sci6(get(r'Radius:\s+([\d.eE+\-]+)\s+m', body)),
            'mass': format_sci6(get(r'Mass:\s+([\d.eE+\-]+)\s+kg', body)),
            'moi': format_sci6(get(r'Moment Of Inertia:\s+([\d.eE+\-]+)\s+kg', body)),
            'rs': format_sci6(get(r'Schwarzschild Radius:\s+([\d.eE+\-]+)\s+m', body)),
            'D': format_sci6(get(r'DeGerlia Compactness \(m/r\):\s+([\d.eE+\-]+)', body)),
            'D_over_Dcrit': format_sci6(str(float(get(r'DeGerlia Compactness \(m/r\):\s+([\d.eE+\-]+)', body)) / 6.73295e26)),
            'gtd': format_gtd(get(r'Gravitational Time Dilation:\s+([\d.eE+\-]+)', body)),
            'k': format_sci6(get(r'k = 1 - GTD² = ([\d.eE+\-]+)', body)),
            'r_ratio': format_sci6(get(r'R/R_prev = ([\d.eE+\-]+)', body)),
            'm_ratio': format_sci6(get(r'M/M_prev = ([\d.eE+\-]+)', body)),
            'i_ratio': format_sci6(get(r'I/I_prev = ([\d.eE+\-]+)', body)),
            'm_cbrt': format_sci6(get(r'\(M/M_prev\)\^\(1/3\) = ([\d.eE+\-]+)', body)),
            'i_5rt': format_sci6(get(r'\(I/I_prev\)\^\(1/5\) = ([\d.eE+\-]+)', body)),
            'rs_over_r': format_sci6(get(r'r_s/R = ([\d.eE+\-]+)', body)),
            'gtd_ratio': format_gtd(get(r'GTD/GTD_prev = ([\d.eE+\-]+)', body)),
            'k_ratio': format_sci6(get(r'\(r_s/R\)/\(r_s/R\)_prev = ([\d.eE+\-]+)', body)),
            'k_over_k_prev': format_sci6(get(r'k/k_prev = ([\d.eE+\-]+)', body)),
        })

    # Compute 1 - D/D_crit and ITD = sqrt((1 - D/D_crit) / (1 - D/D_crit)_prev)
    for row in table_rows:
        val = float(row['D_over_Dcrit'])
        row['one_minus_D_Dcrit'] = format_sci6(str(1.0 - val))
        row['one_minus_D_Dcrit_raw'] = 1.0 - val
    for idx, row in enumerate(table_rows):
        prev_idx = (idx - 1) % len(table_rows)
        prev_val = table_rows[prev_idx]['one_minus_D_Dcrit_raw']
        cur_val = row['one_minus_D_Dcrit_raw']
        if prev_val != 0:
            row['ITD'] = format_gtd(str(math.sqrt(cur_val / prev_val)))
        else:
            row['ITD'] = 'Inf'

    # Write table
    header = '| System | Radius (m) | Mass (kg) | Moment of Inertia (kg·m²) | D = m/r (kg/m) | r_s (m) | GTD | ITD = ((1 - k_D)/(1 - k_D_prev))^1/2 | k_s = r_s/R | k_D = D/D_crit | k_G = 1 - GTD^2 | 1 - D/D_crit | GTD/GTD_prev | k/k_prev | (r_s/R)/(r_s/R)_prev | R/R_prev | M/M_prev | (M/M)^1/3 | I/I_prev | (I/I)^1/5 |'
    sep = '|----------|------------|-----------|----------------------------|----------------|------------|-------------------------------|-------------------------------|----------|----------|----------|------------|------------|----------|----------|----------|----------|-----------|----------|-----------|'
    with open(table_path, 'w') as f:
        f.write('# System Properties Summary\n\n')
        f.write(header + '\n')
        f.write(sep + '\n')
        for row in table_rows:
            f.write(f"| System {row['num']} | {row['radius']} | {row['mass']} | {row['moi']} | {row['D']} | {row['rs']} | {row['gtd']} | {row['ITD']} | {row['rs_over_r']} | {row['D_over_Dcrit']} | {row['k']} | {row['one_minus_D_Dcrit']} | {row['gtd_ratio']} | {row['k_over_k_prev']} | {row['k_ratio']} | {row['r_ratio']} | {row['m_ratio']} | {row['m_cbrt']} | {row['i_ratio']} | {row['i_5rt']} |\n")


def main():
    project_root = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(project_root, 'systems_output.md')
    table_path = os.path.join(project_root, 'systems_table.md')

    # Step 1: Generate systems_output.md
    generate_output(output_path)
    print(f'Wrote {output_path}')

    # Step 2: Parse systems_output.md → systems_table.md
    build_table(output_path, table_path)
    print(f'Wrote {table_path}')


if __name__ == '__main__':
    main()
