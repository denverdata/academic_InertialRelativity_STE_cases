"""
Utility functions for formatting numerical outputs in scientific notation.

This module provides functions for converting values to Decimal type and
formatting outputs in scientific notation with 8 digits past the decimal.
"""

from decimal import Decimal, getcontext

def to_decimal(value):
    """
    Convert a value to Decimal type.
    
    Args:
        value: Input value (can be string, float, or Decimal)
        
    Returns:
        Decimal: Decimal representation of the input
    """
    if isinstance(value, Decimal):
        return value
    
    # Convert to string first to preserve precision
    if isinstance(value, float):
        value_str = str(value)
    else:
        value_str = str(value)
        
    return Decimal(value_str)

def format_scientific(value):
    """
    Format a numerical value in scientific notation with exactly 8 digits past the decimal.
    
    Args:
        value: Value to format (can be Decimal, float, or string)
        
    Returns:
        str: Formatted value in scientific notation with 8 digits past the decimal
    """
    # Convert to Decimal for consistent handling
    decimal_value = to_decimal(value)
    
    # Format with exactly 8 digits past the decimal as required in project brief
    format_str = '%.8e'
    result = format_str % float(decimal_value)
    
    # Ensure the format matches the required e notation
    if 'e' in result:
        base, exponent = result.split('e')
        exponent_value = int(exponent)
        return f"{base}e{exponent_value}"
    
    return result