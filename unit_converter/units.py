from enum import Enum
from typing import Dict, List, Optional
import pint

# Initialize Pint Unit Registry (singleton)
UNIT_REGISTRY = pint.UnitRegistry()


class UnitCategory(Enum):

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



UNIT_CATEGORY_MAP: Dict[str, UnitCategory] = {
    # Length
    "mm": UnitCategory.LENGTH,
    "millimeter": UnitCategory.LENGTH,
    "cm": UnitCategory.LENGTH,
    "centimeter": UnitCategory.LENGTH,
    "m": UnitCategory.LENGTH,
    "meter": UnitCategory.LENGTH,
    "km": UnitCategory.LENGTH,
    "kilometer": UnitCategory.LENGTH,
    "in": UnitCategory.LENGTH,
    "inch": UnitCategory.LENGTH,
    "ft": UnitCategory.LENGTH,
    "foot": UnitCategory.LENGTH,
    "yd": UnitCategory.LENGTH,
    "yard": UnitCategory.LENGTH,
    "mi": UnitCategory.LENGTH,
    "mile": UnitCategory.LENGTH,
    "nm": UnitCategory.LENGTH,
    "nanometer": UnitCategory.LENGTH,
    "um": UnitCategory.LENGTH,
    "micrometer": UnitCategory.LENGTH,
    
    # Mass
    "g": UnitCategory.MASS,
    "gram": UnitCategory.MASS,
    "kg": UnitCategory.MASS,
    "kilogram": UnitCategory.MASS,
    "mg": UnitCategory.MASS,
    "milligram": UnitCategory.MASS,
    "lb": UnitCategory.MASS,
    "pound": UnitCategory.MASS,
    "oz": UnitCategory.MASS,
    "ounce": UnitCategory.MASS,
    "ton": UnitCategory.MASS,
    "tonne": UnitCategory.MASS,
    
    # Temperature
    "degC": UnitCategory.TEMPERATURE,
    "celsius": UnitCategory.TEMPERATURE,
    "degF": UnitCategory.TEMPERATURE,
    "fahrenheit": UnitCategory.TEMPERATURE,
    "K": UnitCategory.TEMPERATURE,
    "kelvin": UnitCategory.TEMPERATURE,
    "degR": UnitCategory.TEMPERATURE,
    "rankine": UnitCategory.TEMPERATURE,
    
    # Pressure
    "Pa": UnitCategory.PRESSURE,
    "pascal": UnitCategory.PRESSURE,
    "kPa": UnitCategory.PRESSURE,
    "bar": UnitCategory.PRESSURE,
    "psi": UnitCategory.PRESSURE,
    "atm": UnitCategory.PRESSURE,
    "atmosphere": UnitCategory.PRESSURE,
    "mmHg": UnitCategory.PRESSURE,
    "torr": UnitCategory.PRESSURE,
    
    # Volume
    "L": UnitCategory.VOLUME,
    "liter": UnitCategory.VOLUME,
    "mL": UnitCategory.VOLUME,
    "milliliter": UnitCategory.VOLUME,
    "gal": UnitCategory.VOLUME,
    "gallon": UnitCategory.VOLUME,
    "qt": UnitCategory.VOLUME,
    "quart": UnitCategory.VOLUME,
    "cup": UnitCategory.VOLUME,
    "fl_oz": UnitCategory.VOLUME,
    
    # Flow
    "CFM": UnitCategory.FLOW,
    "L/s": UnitCategory.FLOW,
    "m3/s": UnitCategory.FLOW,
    "gal/min": UnitCategory.FLOW,
    
    # Velocity
    "m/s": UnitCategory.VELOCITY,
    "km/h": UnitCategory.VELOCITY,
    "mph": UnitCategory.VELOCITY,
    "ft/s": UnitCategory.VELOCITY,
    "knot": UnitCategory.VELOCITY,
    
    # Acceleration
    "m/s2": UnitCategory.ACCELERATION,
    "ft/s2": UnitCategory.ACCELERATION,
    
    # Force
    "N": UnitCategory.FORCE,
    "newton": UnitCategory.FORCE,
    "lbf": UnitCategory.FORCE,
    "kN": UnitCategory.FORCE,
    
    # Energy
    "J": UnitCategory.ENERGY,
    "joule": UnitCategory.ENERGY,
    "kJ": UnitCategory.ENERGY,
    "cal": UnitCategory.ENERGY,
    "calorie": UnitCategory.ENERGY,
    "kcal": UnitCategory.ENERGY,
    "Wh": UnitCategory.ENERGY,
    "kWh": UnitCategory.ENERGY,
    "BTU": UnitCategory.ENERGY,
    "eV": UnitCategory.ENERGY,
    
    # Power
    "W": UnitCategory.POWER,
    "watt": UnitCategory.POWER,
    "kW": UnitCategory.POWER,
    "MW": UnitCategory.POWER,
    "hp": UnitCategory.POWER,
    "horsepower": UnitCategory.POWER,
    
    # Electrical
    "A": UnitCategory.ELECTRICAL_CURRENT,
    "ampere": UnitCategory.ELECTRICAL_CURRENT,
    "mA": UnitCategory.ELECTRICAL_CURRENT,
    "V": UnitCategory.ELECTRICAL_POTENTIAL,
    "volt": UnitCategory.ELECTRICAL_POTENTIAL,
    "kV": UnitCategory.ELECTRICAL_POTENTIAL,
    "ohm": UnitCategory.ELECTRICAL_RESISTANCE,
    "Ω": UnitCategory.ELECTRICAL_RESISTANCE,
    "kohm": UnitCategory.ELECTRICAL_RESISTANCE,
    "Mohm": UnitCategory.ELECTRICAL_RESISTANCE,
    "F": UnitCategory.ELECTRICAL_CAPACITANCE,
    "farad": UnitCategory.ELECTRICAL_CAPACITANCE,
    "uF": UnitCategory.ELECTRICAL_CAPACITANCE,
    "pF": UnitCategory.ELECTRICAL_CAPACITANCE,
    
    # Frequency
    "Hz": UnitCategory.FREQUENCY,
    "hertz": UnitCategory.FREQUENCY,
    "kHz": UnitCategory.FREQUENCY,
    "MHz": UnitCategory.FREQUENCY,
    "GHz": UnitCategory.FREQUENCY,
    
    # Angle
    "rad": UnitCategory.ANGLE,
    "radian": UnitCategory.ANGLE,
    "deg": UnitCategory.ANGLE,
    "degree": UnitCategory.ANGLE,
    
    # Time
    "s": UnitCategory.TIME,
    "second": UnitCategory.TIME,
    "min": UnitCategory.TIME,
    "minute": UnitCategory.TIME,
    "h": UnitCategory.TIME,
    "hour": UnitCategory.TIME,
    "day": UnitCategory.TIME,
    "week": UnitCategory.TIME,
    "year": UnitCategory.TIME,
    
    # Area
    "m2": UnitCategory.AREA,
    "km2": UnitCategory.AREA,
    "ft2": UnitCategory.AREA,
    "acre": UnitCategory.AREA,
    "hectare": UnitCategory.AREA,
    
    # Density
    "kg/m3": UnitCategory.DENSITY,
    "g/cm3": UnitCategory.DENSITY,
    "lb/ft3": UnitCategory.DENSITY,
    
    # Acoustics
    "dB": UnitCategory.ACOUSTICS,
    "decibel": UnitCategory.ACOUSTICS,
}


def get_unit_category(unit_symbol: str) -> Optional[UnitCategory]:

    return UNIT_CATEGORY_MAP.get(unit_symbol)


def get_category_units(category: UnitCategory) -> List[str]:

    return [unit for unit, cat in UNIT_CATEGORY_MAP.items() if cat == category]


def register_custom_unit(symbol: str, definition: str, category: UnitCategory = None):

    try:
        UNIT_REGISTRY.define(f"{symbol} = {definition}")
        if category:
            UNIT_CATEGORY_MAP[symbol] = category
    except Exception as e:
        raise ValueError(f"Failed to register unit '{symbol}': {str(e)}")