"""
Main unit conversion logic using Pint library for dynamic conversions.
"""

from typing import Dict, List, Optional, Set
import pint
from .units import UNIT_REGISTRY, UnitCategory, get_unit_category, get_category_units, get_unit_display_name


class ConversionResult:
    """Represents the result of a unit conversion."""
    
    def __init__(self, original_value: float, original_unit: str, 
                 conversions: Dict[str, float]):
        self.original_value = original_value
        self.original_unit = original_unit
        self.conversions = conversions
    
    def get_conversion(self, target_unit: str) -> Optional[float]:
        """Get conversion result for a specific unit."""
        return self.conversions.get(target_unit)
    
    def __str__(self):
        lines = [f"Original: {self.original_value} {self.original_unit}"]
        lines.append("Conversions:")
        for unit, value in self.conversions.items():
            lines.append(f"  {value:.6f} {unit}")
        return "\n".join(lines)


class UnitConverter:
    """
    Dynamic unit converter using Pint library.
    Supports 4000+ units with automatic dimensional analysis.
    """
    
    def __init__(self):
        self.ureg = UNIT_REGISTRY
        self._cache = {}
    
    def convert(self, value: float, from_unit: str, 
                to_units: Optional[List[str]] = None) -> ConversionResult:
        """
        Convert a value from one unit to other units dynamically.
        
        Args:
            value: The numeric value to convert
            from_unit: Source unit symbol (supports Pint notation)
            to_units: List of target unit symbols. If None, converts to all 
                     compatible units in the same category.
        
        Returns:
            ConversionResult object containing all conversions
        
        Raises:
            ValueError: If units are invalid or incompatible
        """
        try:
            # Create quantity with Pint
            quantity = self.ureg.Quantity(value, from_unit)
        except (pint.UndefinedUnitError, pint.DimensionalityError) as e:
            raise ValueError(f"Invalid unit '{from_unit}': {str(e)}")
        
        # If no target units specified, use all units in same category
        if to_units is None:
            category = get_unit_category(from_unit)
            if category:
                to_units = [u for u in get_category_units(category) if u != from_unit]
            else:
                # Fallback: try to find compatible units
                to_units = self._find_compatible_units(from_unit)
        
        # Perform conversions
        conversions = {}
        
        for target_unit in to_units:
            try:
                converted = quantity.to(target_unit)
                conversions[target_unit] = float(converted.magnitude)
            except (pint.DimensionalityError, pint.UndefinedUnitError) as e:
                # Skip incompatible units silently or raise based on preference
                continue
        
        return ConversionResult(value, from_unit, conversions)
    
    def _find_compatible_units(self, unit: str, limit: int = 20) -> List[str]:
        """
        Find units compatible with the given unit using dimensional analysis.
        
        Args:
            unit: Source unit
            limit: Maximum number of compatible units to return
            
        Returns:
            List of compatible unit symbols
        """
        try:
            quantity = self.ureg.Quantity(1, unit)
            dimensionality = quantity.dimensionality
            
            compatible = []
            # Check common units for compatibility
            common_units = self._get_common_units()
            
            for test_unit in common_units:
                if test_unit == unit:
                    continue
                try:
                    test_quantity = self.ureg.Quantity(1, test_unit)
                    if test_quantity.dimensionality == dimensionality:
                        compatible.append(test_unit)
                        if len(compatible) >= limit:
                            break
                except:
                    continue
            
            return compatible
        except:
            return []
    
    def _get_common_units(self) -> List[str]:
        """Get list of commonly used units across all categories."""
        common = []
        for category in UnitCategory:
            common.extend(get_category_units(category))
        return common
    
    def get_supported_units(self, category: Optional[UnitCategory] = None) -> List[str]:
        """
        Get list of supported unit symbols.
        
        Args:
            category: Optional category filter
            
        Returns:
            List of unit symbols
        """
        if category is None:
            # Return all common units
            return self._get_common_units()
        
        return get_category_units(category)
    
    def get_unit_info(self, unit_symbol: str) -> Dict[str, any]:
        """
        Get detailed information about a unit using Pint.
        
        Args:
            unit_symbol: Unit symbol to query
            
        Returns:
            Dictionary with unit information
        """
        try:
            unit = self.ureg.Unit(unit_symbol)
            quantity = self.ureg.Quantity(1, unit)
            
            category = get_unit_category(unit_symbol)
            
            return {
                'symbol': unit_symbol,
                'name': get_unit_display_name(unit_symbol),
                'dimensionality': str(quantity.dimensionality),
                'category': category.value if category else 'other',
                'notes': self._get_unit_notes(unit_symbol)
            }
        except Exception as e:
            raise ValueError(f"Unknown unit: {unit_symbol}")
    
    def _get_unit_notes(self, unit_symbol: str) -> str:
        """Get descriptive notes for a unit."""
        notes_map = {
            'bar': '1 bar = 100 kPa',
            'CFM': 'Cubic feet per minute',
            'dB': 'Logarithmic unit',
            'GHz': 'Gigahertz',
            'GΩ': 'Gigaohm',
        }
        return notes_map.get(unit_symbol, '')
    
    def convert_with_context(self, value: float, from_unit: str, 
                            to_unit: str, context: str = None) -> float:
        """
        Convert with optional context (e.g., 'spectroscopy' for wavelength).
        
        Args:
            value: Value to convert
            from_unit: Source unit
            to_unit: Target unit
            context: Optional Pint context
            
        Returns:
            Converted value
        """
        try:
            quantity = self.ureg.Quantity(value, from_unit)
            
            if context:
                with self.ureg.context(context):
                    converted = quantity.to(to_unit)
            else:
                converted = quantity.to(to_unit)
            
            return float(converted.magnitude)
        except Exception as e:
            raise ValueError(f"Conversion failed: {str(e)}")
    
    def parse_expression(self, expression: str) -> Dict[str, any]:
        """
        Parse and evaluate unit expressions like '5 meters + 3 feet'.
        
        Args:
            expression: Mathematical expression with units
            
        Returns:
            Dictionary with result and unit
        """
        try:
            result = self.ureg.parse_expression(expression)
            return {
                'value': float(result.magnitude),
                'unit': str(result.units),
                'dimensionality': str(result.dimensionality)
            }
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")