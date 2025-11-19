"""
Unit definitions and categories for the conversion library.
"""

from enum import Enum
from typing import Dict


class UnitCategory(Enum):
    """Categories of units supported by the converter."""
    LENGTH = "length"
    MASS = "mass"
    TEMPERATURE = "temperature"
    PRESSURE = "pressure"
    FLOW = "flow"
    ELECTRICAL_CURRENT = "electrical_current"
    ACOUSTICS = "acoustics"
    VELOCITY = "velocity"
    FREQUENCY = "frequency"
    ELECTRICAL_RESISTANCE = "electrical_resistance"


class Unit:
    """Represents a unit with its conversion factor and metadata."""
    
    def __init__(self, symbol: str, name: str, category: UnitCategory, 
                 to_base_factor: float, notes: str = ""):
        self.symbol = symbol
        self.name = name
        self.category = category
        self.to_base_factor = to_base_factor  # Factor to convert to base unit
        self.notes = notes
    
    def __str__(self):
        return f"{self.symbol} ({self.name})"
    
    def __repr__(self):
        return f"Unit('{self.symbol}', '{self.name}', {self.category})"


# Unit definitions with conversion factors to base units
UNITS: Dict[str, Unit] = {
    # Length units (base: meter)
    "mm": Unit("mm", "millimeter", UnitCategory.LENGTH, 0.001),
    "cm": Unit("cm", "centimeter", UnitCategory.LENGTH, 0.01),
    "m": Unit("m", "meter", UnitCategory.LENGTH, 1.0),
    "in": Unit("in", "inch", UnitCategory.LENGTH, 0.0254),
    "ft": Unit("ft", "foot", UnitCategory.LENGTH, 0.3048),
    
    # Mass units (base: gram)
    "g": Unit("g", "gram", UnitCategory.MASS, 1.0, "Assumed gram; could mean gravitational acceleration (g)"),
    
    # Temperature units (special handling required)
    "DEG_C": Unit("°C", "degrees Celsius", UnitCategory.TEMPERATURE, 1.0),
    "DEG_F": Unit("°F", "degrees Fahrenheit", UnitCategory.TEMPERATURE, 1.0),
    
    # Pressure units (base: Pascal)
    "BAR": Unit("bar", "bar", UnitCategory.PRESSURE, 100000, "1 bar = 100 kPa"),
    "BAR_G": Unit("bar(g)", "bar gauge", UnitCategory.PRESSURE, 100000, "Gauge pressure variant"),
    
    # Flow units (base: cubic meter per second)
    "CFM": Unit("CFM", "cubic feet per minute", UnitCategory.FLOW, 0.000471947, "Imperial volumetric flow"),
    
    # Electrical current (base: Ampere)
    "A": Unit("A", "ampere", UnitCategory.ELECTRICAL_CURRENT, 1.0),
    
    # Acoustics/signal level (base: decibel)
    "DB": Unit("dB", "decibel", UnitCategory.ACOUSTICS, 1.0, "Logarithmic unit"),
    
    # Velocity units (base: meter per second)
    "FT/SEC": Unit("ft/s", "foot per second", UnitCategory.VELOCITY, 0.3048),
    
    # Frequency units (base: Hertz)
    "GHZ": Unit("GHz", "gigahertz", UnitCategory.FREQUENCY, 1e9),
    
    # Electrical resistance (base: Ohm)
    "GOHM": Unit("GΩ", "gigaohm", UnitCategory.ELECTRICAL_RESISTANCE, 1e9, "Assumed gigaohm; symbol often GΩ"),
}