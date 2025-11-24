"""
Test cases for the Pint-powered unit converter module.
"""

import unittest
from unit_converter import UnitConverter, UnitCategory


class TestUnitConverter(unittest.TestCase):
    """Test cases demonstrating that the module works correctly with Pint."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.converter = UnitConverter()
    
    def test_length_conversion_example(self):
        """Test the example from requirements: 205 mm conversion."""
        result = self.converter.convert(205, "mm", ["m", "cm", "in", "ft"])
        
        # Expected conversions
        self.assertAlmostEqual(result.get_conversion("m"), 0.205, places=6)
        self.assertAlmostEqual(result.get_conversion("cm"), 20.5, places=6)
        self.assertAlmostEqual(result.get_conversion("in"), 8.070866, places=5)
        self.assertAlmostEqual(result.get_conversion("ft"), 0.672572, places=5)
    
    def test_length_conversions(self):
        """Test various length unit conversions."""
        # Test mm to other units
        result = self.converter.convert(1000, "mm", ["m", "cm"])
        self.assertAlmostEqual(result.get_conversion("m"), 1.0, places=10)
        self.assertAlmostEqual(result.get_conversion("cm"), 100.0, places=10)
        
        # Test inches to metric
        result = self.converter.convert(12, "in", ["ft", "cm", "m"])
        self.assertAlmostEqual(result.get_conversion("ft"), 1.0, places=10)
        self.assertAlmostEqual(result.get_conversion("cm"), 30.48, places=2)
        self.assertAlmostEqual(result.get_conversion("m"), 0.3048, places=4)
    
    def test_temperature_conversions(self):
        """Test temperature conversions with Pint."""
        # Test Celsius to Fahrenheit
        result = self.converter.convert(0, "degC", ["degF"])
        self.assertAlmostEqual(result.get_conversion("degF"), 32.0, places=1)
        
        result = self.converter.convert(100, "degC", ["degF"])
        self.assertAlmostEqual(result.get_conversion("degF"), 212.0, places=1)
        
        # Test Fahrenheit to Celsius
        result = self.converter.convert(32, "degF", ["degC"])
        self.assertAlmostEqual(result.get_conversion("degC"), 0.0, places=1)
        
        result = self.converter.convert(212, "degF", ["degC"])
        self.assertAlmostEqual(result.get_conversion("degC"), 100.0, places=1)
    
    def test_pressure_conversions(self):
        """Test pressure unit conversions."""
        # Test bar to psi
        result = self.converter.convert(1, "bar", ["psi", "Pa"])
        self.assertAlmostEqual(result.get_conversion("psi"), 14.5038, places=2)
        self.assertAlmostEqual(result.get_conversion("Pa"), 100000, places=0)
    
    def test_auto_conversion_to_category(self):
        """Test automatic conversion to all units in same category."""
        result = self.converter.convert(1, "m")  # No target units specified
        
        # Should convert to all other length units
        conversions = result.conversions
        self.assertIn("mm", conversions)
        self.assertIn("cm", conversions)
        self.assertIn("in", conversions)
        self.assertIn("ft", conversions)
        
        # Check some values
        self.assertAlmostEqual(conversions["mm"], 1000.0, places=1)
        self.assertAlmostEqual(conversions["cm"], 100.0, places=1)
    
    def test_error_handling(self):
        """Test proper error handling for invalid inputs."""
        # Test unknown unit
        with self.assertRaises(ValueError):
            self.converter.convert(1, "unknown_unit_xyz", ["m"])
    
    def test_decimal_values(self):
        """Test handling of decimal values and formatting."""
        result = self.converter.convert(2.54, "cm", ["in"])
        self.assertAlmostEqual(result.get_conversion("in"), 1.0, places=6)
        
        result = self.converter.convert(0.5, "m", ["mm", "cm"])
        self.assertAlmostEqual(result.get_conversion("mm"), 500.0, places=1)
        self.assertAlmostEqual(result.get_conversion("cm"), 50.0, places=1)
    
    def test_get_supported_units(self):
        """Test getting supported units by category."""
        length_units = self.converter.get_supported_units(UnitCategory.LENGTH)
        self.assertIn("mm", length_units)
        self.assertIn("m", length_units)
        self.assertIn("in", length_units)
        self.assertIn("ft", length_units)
        
        all_units = self.converter.get_supported_units()
        self.assertGreater(len(all_units), len(length_units))
    
    def test_unit_info(self):
        """Test getting unit information."""
        unit_info = self.converter.get_unit_info("mm")
        self.assertIn('name', unit_info)
        self.assertIn('dimensionality', unit_info)
        self.assertIn('category', unit_info)
    
    def test_conversion_result_string(self):
        """Test string representation of conversion results."""
        result = self.converter.convert(1, "m", ["cm", "mm"])
        result_str = str(result)
        
        self.assertIn("Original: 1", result_str)
        self.assertIn("Conversions:", result_str)
        self.assertIn("cm", result_str)
        self.assertIn("mm", result_str)
    
    def test_advanced_units(self):
        """Test advanced units that Pint supports."""
        # Test velocity
        result = self.converter.convert(100, "km/h", ["m/s", "mph"])
        self.assertAlmostEqual(result.get_conversion("m/s"), 27.778, places=2)
        self.assertAlmostEqual(result.get_conversion("mph"), 62.137, places=2)
        
        # Test energy
        result = self.converter.convert(1, "kWh", ["J", "cal"])
        self.assertAlmostEqual(result.get_conversion("J"), 3600000, places=0)
    
    def test_expression_parsing(self):
        """Test mathematical expression parsing."""
        result = self.converter.parse_expression("5 meters + 3 feet")
        self.assertIn('value', result)
        self.assertIn('unit', result)
        # 5m + 3ft = 5m + 0.9144m = 5.9144m
        self.assertAlmostEqual(result['value'], 5.9144, places=3)
    
    def test_context_conversion(self):
        """Test conversion with context."""
        # Basic conversion without context
        result = self.converter.convert_with_context(1, "m", "cm")
        self.assertAlmostEqual(result, 100.0, places=1)


if __name__ == "__main__":
    unittest.main()