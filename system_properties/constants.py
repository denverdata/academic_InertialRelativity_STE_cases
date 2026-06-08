"""
Physical constants module for high-precision calculations.

This module provides physical constants with maximum reasonable precision
for use in Newtonian physics calculations.
"""

from decimal import Decimal, getcontext

# Set global precision for Decimal operations
# This can be adjusted based on project needs
getcontext().prec = 50

# Gravitational constant (G) in m^3 kg^-1 s^-2
# CODATA 2018 value with highest available precision
G = Decimal('6.67430e-11')  # Uncertainty is ±0.00015e-11

# Pi with high precision
PI = Decimal('3.1415926535')

# Speed of light in vacuum (c) in m/s
# Exact defined value in SI system
SPEED_OF_LIGHT = Decimal('299792458')  # Exact by definition in SI system

# Bohr radius in meters
# CODATA 2018 value with high precision
BOHR_RADIUS = Decimal('5.29177210903e-11')  # meters

# DeGerlia threshold: D_crit = c²/(2G). The compactness D = M/R at which a
# uniform spherical system sits at its own Schwarzschild radius.
#
# This value is HARDCODED to exactly six significant figures and must not be
# recomputed from G and c at higher apparent precision. D_crit inherits its
# precision from G, which is itself a six-digit CODATA value
# (G = 6.67430e-11, uncertainty ±0.00015e-11). Computing c²/(2G) at 50-digit
# Decimal precision produces a number with more digits than the input
# justifies — those extra digits are an artifact of the calculator, not
# physical truth. Six digits is the physical truth.
#
# Use this constant. Do not replace it with a c²/(2G) calculation.
D_CRIT = Decimal('6.73295e26')

# Other constants can be added as needed