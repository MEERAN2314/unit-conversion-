"""
Dynamic unit definitions using Pint library with 4000+ units support.
"""

from enum import Enum
from typing import Dict, List, Optional
import pint

# Initialize Pint Unit Registry (singleton)
UNIT_REGISTRY = pint.UnitRegistry()


class UnitCategory(Enum):
    """Categories of units supported by the converter."""
    LENGTH = "length"
    MASS = "mass"
    TEMPERATURE = "temperature"
    PRESSURE = "pressure"
    VOLUME = "volume"
    FLOW = "flow"
    VELOCITY = "velocity"
    ACCELERATION = "acceleration"
    FORCE = "force"
    ENERGY = "energy"
    POWER = "power"
    ELECTRICAL_CURRENT = "electrical_current"
    ELECTRICAL_POTENTIAL = "electrical_potential"
    ELECTRICAL_RESISTANCE = "electrical_resistance"
    ELECTRICAL_CAPACITANCE = "electrical_capacitance"
    FREQUENCY = "frequency"
    ANGLE = "angle"
    TIME = "time"
    AREA = "area"
    DENSITY = "density"
    ACOUSTICS = "acoustics"


# Mapping of unit symbols to categories for quick lookup
# Only includes preferred symbols (no duplicates)
UNIT_CATEGORY_MAP: Dict[str, UnitCategory] = {
    # Length - using standard abbreviations
    "mm": UnitCategory.LENGTH,
    "cm": UnitCategory.LENGTH,
    "m": UnitCategory.LENGTH,
    "km": UnitCategory.LENGTH,
    "in": UnitCategory.LENGTH,
    "ft": UnitCategory.LENGTH,
    "yd": UnitCategory.LENGTH,
    "mi": UnitCategory.LENGTH,
    "nm": UnitCategory.LENGTH,
    "um": UnitCategory.LENGTH,
    
    # Mass - using standard abbreviations
    "g": UnitCategory.MASS,
    "kg": UnitCategory.MASS,
    "mg": UnitCategory.MASS,
    "lb": UnitCategory.MASS,
    "oz": UnitCategory.MASS,
    "ton": UnitCategory.MASS,
    "tonne": UnitCategory.MASS,
    
    # Temperature - using degree notation
    "degC": UnitCategory.TEMPERATURE,
    "degF": UnitCategory.TEMPERATURE,
    "K": UnitCategory.TEMPERATURE,
    "degR": UnitCategory.TEMPERATURE,
    
    # Pressure - using standard abbreviations
    "Pa": UnitCategory.PRESSURE,
    "kPa": UnitCategory.PRESSURE,
    "bar": UnitCategory.PRESSURE,
    "psi": UnitCategory.PRESSURE,
    "atm": UnitCategory.PRESSURE,
    "mmHg": UnitCategory.PRESSURE,
    "torr": UnitCategory.PRESSURE,
    
    # Volume - using standard abbreviations
    "L": UnitCategory.VOLUME,
    "mL": UnitCategory.VOLUME,
    "gal": UnitCategory.VOLUME,
    "qt": UnitCategory.VOLUME,
    "cup": UnitCategory.VOLUME,
    "fl_oz": UnitCategory.VOLUME,
    "m3": UnitCategory.VOLUME,
    "cm3": UnitCategory.VOLUME,
    
    # Flow - using standard abbreviations
    "CFM": UnitCategory.FLOW,
    "L/s": UnitCategory.FLOW,
    "m3/s": UnitCategory.FLOW,
    "gal/min": UnitCategory.FLOW,
    
    # Velocity - using standard abbreviations
    "m/s": UnitCategory.VELOCITY,
    "km/h": UnitCategory.VELOCITY,
    "mph": UnitCategory.VELOCITY,
    "ft/s": UnitCategory.VELOCITY,
    "knot": UnitCategory.VELOCITY,
    
    # Acceleration - using standard abbreviations
    "m/s2": UnitCategory.ACCELERATION,
    "ft/s2": UnitCategory.ACCELERATION,
    
    # Force - using standard abbreviations
    "N": UnitCategory.FORCE,
    "kN": UnitCategory.FORCE,
    "lbf": UnitCategory.FORCE,
    
    # Energy - using standard abbreviations
    "J": UnitCategory.ENERGY,
    "kJ": UnitCategory.ENERGY,
    "MJ": UnitCategory.ENERGY,
    "cal": UnitCategory.ENERGY,
    "kcal": UnitCategory.ENERGY,
    "Wh": UnitCategory.ENERGY,
    "kWh": UnitCategory.ENERGY,
    "BTU": UnitCategory.ENERGY,
    "eV": UnitCategory.ENERGY,
    
    # Power - using standard abbreviations
    "W": UnitCategory.POWER,
    "kW": UnitCategory.POWER,
    "MW": UnitCategory.POWER,
    "hp": UnitCategory.POWER,
    
    # Electrical Current
    "A": UnitCategory.ELECTRICAL_CURRENT,
    "mA": UnitCategory.ELECTRICAL_CURRENT,
    "uA": UnitCategory.ELECTRICAL_CURRENT,
    
    # Electrical Potential
    "V": UnitCategory.ELECTRICAL_POTENTIAL,
    "mV": UnitCategory.ELECTRICAL_POTENTIAL,
    "kV": UnitCategory.ELECTRICAL_POTENTIAL,
    
    # Electrical Resistance
    "ohm": UnitCategory.ELECTRICAL_RESISTANCE,
    "kohm": UnitCategory.ELECTRICAL_RESISTANCE,
    "Mohm": UnitCategory.ELECTRICAL_RESISTANCE,
    
    # Electrical Capacitance
    "F": UnitCategory.ELECTRICAL_CAPACITANCE,
    "uF": UnitCategory.ELECTRICAL_CAPACITANCE,
    "nF": UnitCategory.ELECTRICAL_CAPACITANCE,
    "pF": UnitCategory.ELECTRICAL_CAPACITANCE,
    
    # Frequency
    "Hz": UnitCategory.FREQUENCY,
    "kHz": UnitCategory.FREQUENCY,
    "MHz": UnitCategory.FREQUENCY,
    "GHz": UnitCategory.FREQUENCY,
    
    # Angle
    "rad": UnitCategory.ANGLE,
    "deg": UnitCategory.ANGLE,
    
    # Time
    "s": UnitCategory.TIME,
    "ms": UnitCategory.TIME,
    "min": UnitCategory.TIME,
    "h": UnitCategory.TIME,
    "day": UnitCategory.TIME,
    "week": UnitCategory.TIME,
    "year": UnitCategory.TIME,
    
    # Area
    "m2": UnitCategory.AREA,
    "cm2": UnitCategory.AREA,
    "km2": UnitCategory.AREA,
    "ft2": UnitCategory.AREA,
    "in2": UnitCategory.AREA,
    "acre": UnitCategory.AREA,
    "hectare": UnitCategory.AREA,
    
    # Density
    "kg/m3": UnitCategory.DENSITY,
    "g/cm3": UnitCategory.DENSITY,
    "lb/ft3": UnitCategory.DENSITY,
    
    # Acoustics
    "dB": UnitCategory.ACOUSTICS,
}

# Mapping for alternative names (for lookup only, not displayed)
UNIT_ALIASES: Dict[str, str] = {
    "millimeter": "mm",
    "centimeter": "cm",
    "meter": "m",
    "kilometer": "km",
    "inch": "in",
    "foot": "ft",
    "yard": "yd",
    "mile": "mi",
    "nanometer": "nm",
    "micrometer": "um",
    "gram": "g",
    "kilogram": "kg",
    "milligram": "mg",
    "pound": "lb",
    "ounce": "oz",
    "celsius": "degC",
    "fahrenheit": "degF",
    "kelvin": "K",
    "rankine": "degR",
    "pascal": "Pa",
    "atmosphere": "atm",
    "liter": "L",
    "milliliter": "mL",
    "gallon": "gal",
    "quart": "qt",
    "newton": "N",
    "joule": "J",
    "calorie": "cal",
    "watt": "W",
    "horsepower": "hp",
    "ampere": "A",
    "volt": "V",
    "farad": "F",
    "hertz": "Hz",
    "radian": "rad",
    "degree": "deg",
    "second": "s",
    "minute": "min",
    "hour": "h",
    "decibel": "dB",
}


def get_unit_category(unit_symbol: str) -> Optional[UnitCategory]:
    """
    Get the category for a given unit symbol.
    
    Args:
        unit_symbol: Unit symbol to look up
        
    Returns:
        UnitCategory or None if not found
    """
    # Check if it's an alias first
    if unit_symbol in UNIT_ALIASES:
        unit_symbol = UNIT_ALIASES[unit_symbol]
    
    return UNIT_CATEGORY_MAP.get(unit_symbol)


def get_category_units(category: UnitCategory) -> List[str]:
    """
    Get all unit symbols for a given category (no duplicates).
    
    Args:
        category: UnitCategory to filter by
        
    Returns:
        List of unique unit symbols
    """
    # Get units from the main map (already deduplicated)
    units = [unit for unit, cat in UNIT_CATEGORY_MAP.items() if cat == category]
    
    # Sort for consistent ordering
    return sorted(units)


def get_unit_display_name(unit_symbol: str) -> str:
    """
    Get the display name for a unit symbol.
    
    Args:
        unit_symbol: Unit symbol
        
    Returns:
        Human-readable display name
    """
    display_names = {
        # Length
        "mm": "millimeter",
        "cm": "centimeter",
        "m": "meter",
        "km": "kilometer",
        "in": "inch",
        "ft": "foot",
        "yd": "yard",
        "mi": "mile",
        "nm": "nanometer",
        "um": "micrometer",
        
        # Mass
        "g": "gram",
        "kg": "kilogram",
        "mg": "milligram",
        "lb": "pound",
        "oz": "ounce",
        "ton": "ton",
        "tonne": "metric ton",
        
        # Temperature
        "degC": "Celsius",
        "degF": "Fahrenheit",
        "K": "Kelvin",
        "degR": "Rankine",
        
        # Pressure
        "Pa": "pascal",
        "kPa": "kilopascal",
        "bar": "bar",
        "psi": "pound per square inch",
        "atm": "atmosphere",
        "mmHg": "millimeter of mercury",
        "torr": "torr",
        
        # Volume
        "L": "liter",
        "mL": "milliliter",
        "gal": "gallon",
        "qt": "quart",
        "cup": "cup",
        "fl_oz": "fluid ounce",
        "m3": "cubic meter",
        "cm3": "cubic centimeter",
        
        # Flow
        "CFM": "cubic feet per minute",
        "L/s": "liters per second",
        "m3/s": "cubic meters per second",
        "gal/min": "gallons per minute",
        
        # Velocity
        "m/s": "meters per second",
        "km/h": "kilometers per hour",
        "mph": "miles per hour",
        "ft/s": "feet per second",
        "knot": "knot",
        
        # Acceleration
        "m/s2": "meters per second squared",
        "ft/s2": "feet per second squared",
        
        # Force
        "N": "newton",
        "kN": "kilonewton",
        "lbf": "pound-force",
        
        # Energy
        "J": "joule",
        "kJ": "kilojoule",
        "MJ": "megajoule",
        "cal": "calorie",
        "kcal": "kilocalorie",
        "Wh": "watt-hour",
        "kWh": "kilowatt-hour",
        "BTU": "British thermal unit",
        "eV": "electronvolt",
        
        # Power
        "W": "watt",
        "kW": "kilowatt",
        "MW": "megawatt",
        "hp": "horsepower",
        
        # Electrical
        "A": "ampere",
        "mA": "milliampere",
        "uA": "microampere",
        "V": "volt",
        "mV": "millivolt",
        "kV": "kilovolt",
        "ohm": "ohm",
        "kohm": "kiloohm",
        "Mohm": "megaohm",
        "F": "farad",
        "uF": "microfarad",
        "nF": "nanofarad",
        "pF": "picofarad",
        
        # Frequency
        "Hz": "hertz",
        "kHz": "kilohertz",
        "MHz": "megahertz",
        "GHz": "gigahertz",
        
        # Angle
        "rad": "radian",
        "deg": "degree",
        
        # Time
        "s": "second",
        "ms": "millisecond",
        "min": "minute",
        "h": "hour",
        "day": "day",
        "week": "week",
        "year": "year",
        
        # Area
        "m2": "square meter",
        "cm2": "square centimeter",
        "km2": "square kilometer",
        "ft2": "square foot",
        "in2": "square inch",
        "acre": "acre",
        "hectare": "hectare",
        
        # Density
        "kg/m3": "kilogram per cubic meter",
        "g/cm3": "gram per cubic centimeter",
        "lb/ft3": "pound per cubic foot",
        
        # Acoustics
        "dB": "decibel",
    }
    
    return display_names.get(unit_symbol, unit_symbol)


def register_custom_unit(symbol: str, definition: str, category: UnitCategory = None):
    """
    Register a custom unit with Pint.
    
    Args:
        symbol: Unit symbol
        definition: Pint definition (e.g., "1000 * meter")
        category: Optional category for the unit
    """
    try:
        UNIT_REGISTRY.define(f"{symbol} = {definition}")
        if category:
            UNIT_CATEGORY_MAP[symbol] = category
    except Exception as e:
        raise ValueError(f"Failed to register unit '{symbol}': {str(e)}")