"""
Unit Conversion Library

A dynamic Python library for converting between 4000+ units of measurement.
Powered by Pint for advanced dimensional analysis and conversions.
"""

from .converter import UnitConverter, ConversionResult
from .units import UnitCategory, UNIT_REGISTRY, get_unit_category, get_category_units, get_unit_display_name

__version__ = "2.0.1"
__all__ = ["UnitConverter", "ConversionResult", "UnitCategory", "UNIT_REGISTRY", 
           "get_unit_category", "get_category_units", "get_unit_display_name"]