from .converter import UnitConverter, ConversionResult
from .units import UnitCategory, UNIT_REGISTRY, get_unit_category, get_category_units

__version__ = "2.0.0"
__all__ = ["UnitConverter", "ConversionResult", "UnitCategory", "UNIT_REGISTRY", 
           "get_unit_category", "get_category_units"]