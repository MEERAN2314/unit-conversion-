"""
Test cases for the unit converter module.
"""

import unittest
from unit_converter import UnitConverter, UnitCategory


class TestUnitConverter(unittest.TestCase):
    """Test cases demonstrating that the module works correctly."""
    
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
        """Test temperature conversions with proper formulas."""
        # Test Celsius to Fahrenheit
        result = self.converter.convert(0, "DEG_C", ["DEG_F"])
        self.assertEqual(result.get_conversion("DEG_F"), 32.0)
        
        result = self.converter.convert(100, "DEG_C", ["DEG_F"])
        self.assertEqual(result.get_conversion("DEG_F"), 212.0)
        
        # Test Fahrenheit to Celsius
        result = self.converter.convert(32, "DEG_F", ["DEG_C"])
        self.assertEqual(result.get_conversion("DEG_C"), 0.0)
        
        result = self.converter.convert(212, "DEG_F", ["DEG_C"])
        self.assertEqual(result.get_conversion("DEG_C"), 100.0)
    
    def test_pressure_conversions(self):
        """Test pressure unit conversions."""
        # Test bar conversions (1 bar = 100 kPa = 100000 Pa)
        result = self.converter.convert(1, "BAR", ["BAR_G"])
        self.assertEqual(result.get_conversion("BAR_G"), 1.0)
    
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
        self.assertEqual(conversions["mm"], 1000.0)
        self.assertEqual(conversions["cm"], 100.0)
    
    def test_error_handling(self):
        """Test proper error handling for invalid inputs."""
        # Test unknown unit
        with self.assertRaises(ValueError):
            self.converter.convert(1, "unknown_unit", ["m"])
        
        # Test incompatible unit categories
        with self.assertRaises(ValueError):
            self.converter.convert(1, "m", ["DEG_C"])  # length to temperature
    
    def test_decimal_values(self):
        """Test handling of decimal values and formatting."""
        result = self.converter.convert(2.54, "cm", ["in"])
        self.assertAlmostEqual(result.get_conversion("in"), 1.0, places=6)
        
        result = self.converter.convert(0.5, "m", ["mm", "cm"])
        self.assertEqual(result.get_conversion("mm"), 500.0)
        self.assertEqual(result.get_conversion("cm"), 50.0)
    
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
        self.assertEqual(unit_info.symbol, "mm")
        self.assertEqual(unit_info.name, "millimeter")
        self.assertEqual(unit_info.category, UnitCategory.LENGTH)
    
    def test_conversion_result_string(self):
        """Test string representation of conversion results."""
        result = self.converter.convert(1, "m", ["cm", "mm"])
        result_str = str(result)
        
        self.assertIn("Original: 1", result_str)
        self.assertIn("Conversions:", result_str)
        self.assertIn("cm", result_str)
        self.assertIn("mm", result_str)


if __name__ == "__main__":
    unittest.main()