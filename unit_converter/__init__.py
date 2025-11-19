"""
Unit Conversion Library

A Python library for converting between different units of measurement.
Supports length, mass, temperature, pressure, flow, and other unit categories.
"""

from .converter import UnitConverter
from .units import UnitCategory, Unit

__version__ = "1.0.0"
__all__ = ["UnitConverter", "UnitCategory", "Unit"]