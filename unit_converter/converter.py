"""
Main unit conversion logic and UnitConverter class.
"""

from typing import Dict, List, Union, Optional
from .units import UNITS, Unit, UnitCategory


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
    """Main unit converter class."""
    
    def __init__(self):
        self.units = UNITS
    
    def convert(self, value: float, from_unit: str, 
                to_units: Optional[List[str]] = None) -> ConversionResult:
        """
        Convert a value from one unit to other units.
        
        Args:
            value: The numeric value to convert
            from_unit: Source unit symbol
            to_units: List of target unit symbols. If None, converts to all 
                     compatible units in the same category.
        
        Returns:
            ConversionResult object containing all conversions
        
        Raises:
            ValueError: If units are invalid or incompatible
        """
        if from_unit not in self.units:
            raise ValueError(f"Unknown unit: {from_unit}")
        
        source_unit = self.units[from_unit]
        
        # If no target units specified, use all units in same category
        if to_units is None:
            to_units = [symbol for symbol, unit in self.units.items() 
                       if unit.category == source_unit.category and symbol != from_unit]
        
        # Validate target units
        for unit_symbol in to_units:
            if unit_symbol not in self.units:
                raise ValueError(f"Unknown unit: {unit_symbol}")
            
            target_unit = self.units[unit_symbol]
            if target_unit.category != source_unit.category:
                raise ValueError(f"Cannot convert {source_unit.category.value} "
                               f"to {target_unit.category.value}")
        
        # Perform conversions
        conversions = {}
        
        if source_unit.category == UnitCategory.TEMPERATURE:
            # Special handling for temperature conversions
            conversions = self._convert_temperature(value, from_unit, to_units)
        else:
            # Standard linear conversions
            # Convert to base unit first
            base_value = value * source_unit.to_base_factor
            
            # Convert from base to target units
            for target_symbol in to_units:
                target_unit = self.units[target_symbol]
                converted_value = base_value / target_unit.to_base_factor
                conversions[target_symbol] = converted_value
        
        return ConversionResult(value, from_unit, conversions)
    
    def _convert_temperature(self, value: float, from_unit: str, 
                           to_units: List[str]) -> Dict[str, float]:
        """Handle temperature conversions with proper formulas."""
        conversions = {}
        
        for target_unit in to_units:
            if from_unit == "DEG_C" and target_unit == "DEG_F":
                # Celsius to Fahrenheit: F = C * 9/5 + 32
                conversions[target_unit] = value * 9/5 + 32
            elif from_unit == "DEG_F" and target_unit == "DEG_C":
                # Fahrenheit to Celsius: C = (F - 32) * 5/9
                conversions[target_unit] = (value - 32) * 5/9
            elif from_unit == target_unit:
                conversions[target_unit] = value
        
        return conversions
    
    def get_supported_units(self, category: Optional[UnitCategory] = None) -> List[str]:
        """
        Get list of supported unit symbols.
        
        Args:
            category: Optional category filter
            
        Returns:
            List of unit symbols
        """
        if category is None:
            return list(self.units.keys())
        
        return [symbol for symbol, unit in self.units.items() 
                if unit.category == category]
    
    def get_unit_info(self, unit_symbol: str) -> Unit:
        """Get detailed information about a unit."""
        if unit_symbol not in self.units:
            raise ValueError(f"Unknown unit: {unit_symbol}")
        return self.units[unit_symbol]