#!/usr/bin/env python3
"""Append the new computed column to pair_comparisons_v2_cases.md as a new
rightmost (9th) value column. Every existing column is left byte-for-byte
unchanged; we only append ` value |` to each pipe row.

Run build_new_pair_column.py first to (re)generate the values, or rely on the
embedded dict below which it produced.
"""
import subprocess, sys, os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, 'pair_comparisons_v2_cases.md')
HEADER = 'M=M, R1=4/3 rs (1e30, 4/3rs - 1e8)'

# Pull the freshly computed values from the engine-driven builder.
out = subprocess.check_output([sys.executable, os.path.join(HERE, 'build_new_pair_column.py')], text=True)
values = {}
for line in out.strip().splitlines():
    label, val = line.split('\t')
    values[label] = val

with open(MD) as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    raw = line.rstrip('\n')
    if not raw.startswith('|'):
        new_lines.append(line)
        continue
    # Separator row: | --- | --- | ...
    cells = [c for c in raw.split('|')]
    # cells[0] and cells[-1] are the empty strings outside the outer pipes
    inner = [c.strip() for c in raw.split('|')[1:-1]]
    if inner and all(set(c) <= set('-') and c for c in inner[1:]):
        new_lines.append(raw + '---|\n')
        continue
    # Header row
    if inner and inner[0] == 'metric_description':
        new_lines.append(raw + f' {HEADER} |\n')
        continue
    # Data row: first inner cell is the label
    label = inner[0]
    if label in values:
        new_lines.append(raw + f' {values[label]} |\n')
    else:
        # Unknown label -> blank cell, never silently wrong
        new_lines.append(raw + ' --- |\n')

shutil.copyfile(MD, MD + '.bak')
with open(MD, 'w') as f:
    f.writelines(new_lines)

print(f'Wrote new column "{HEADER}" to {MD} (backup at {MD}.bak)')
print(f'Matched {sum(1 for L in lines if L.startswith("|") and L.split("|")[1].strip() in values)} data rows.')
