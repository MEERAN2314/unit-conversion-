#!/usr/bin/env python3
"""
Test script to verify the duplicate units fix.
Run this to ensure no duplicates exist in any category.
"""

from unit_converter import UnitConverter, UnitCategory, get_category_units, get_unit_display_name

def test_no_duplicates():
    """Test that no category has duplicate units."""
    print("=" * 60)
    print("Testing for Duplicate Units")
    print("=" * 60)
    
    all_passed = True
    
    for category in UnitCategory:
        units = get_category_units(category)
        unique_units = set(units)
        
        if len(units) != len(unique_units):
            print(f"❌ FAIL: {category.value} has duplicates!")
            print(f"   Total: {len(units)}, Unique: {len(unique_units)}")
            duplicates = [u for u in units if units.count(u) > 1]
            print(f"   Duplicates: {set(duplicates)}")
            all_passed = False
        else:
            print(f"✅ PASS: {category.value} ({len(units)} unique units)")
    
    print("=" * 60)
    if all_passed:
        print("✅ All tests passed! No duplicates found.")
    else:
        print("❌ Some tests failed. Duplicates detected.")
    print("=" * 60)
    
    return all_passed


def test_display_names():
    """Test that display names work correctly."""
    print("\n" + "=" * 60)
    print("Testing Display Names")
    print("=" * 60)
    
    test_cases = {
        "mm": "millimeter",
        "cm": "centimeter",
        "m": "meter",
        "km": "kilometer",
        "in": "inch",
        "ft": "foot",
        "g": "gram",
        "kg": "kilogram",
        "degC": "Celsius",
        "degF": "Fahrenheit",
    }
    
    all_passed = True
    
    for symbol, expected_name in test_cases.items():
        actual_name = get_unit_display_name(symbol)
        if actual_name == expected_name:
            print(f"✅ {symbol} → {actual_name}")
        else:
            print(f"❌ {symbol} → {actual_name} (expected: {expected_name})")
            all_passed = False
    
    print("=" * 60)
    if all_passed:
        print("✅ All display names correct!")
    else:
        print("❌ Some display names incorrect.")
    print("=" * 60)
    
    return all_passed


def test_conversions():
    """Test that conversions still work correctly."""
    print("\n" + "=" * 60)
    print("Testing Conversions")
    print("=" * 60)
    
    converter = UnitConverter()
    
    test_cases = [
        (100, "mm", ["cm", "m", "in"], "Length conversion"),
        (25, "degC", ["degF"], "Temperature conversion"),
        (1, "kg", ["g", "lb"], "Mass conversion"),
        (1, "L", ["mL", "gal"], "Volume conversion"),
    ]
    
    all_passed = True
    
    for value, from_unit, to_units, description in test_cases:
        try:
            result = converter.convert(value, from_unit, to_units)
            if len(result.conversions) > 0:
                print(f"✅ {description}: {value} {from_unit}")
                for unit, converted in result.conversions.items():
                    print(f"   → {converted:.4f} {unit}")
            else:
                print(f"❌ {description}: No conversions returned")
                all_passed = False
        except Exception as e:
            print(f"❌ {description}: {str(e)}")
            all_passed = False
    
    print("=" * 60)
    if all_passed:
        print("✅ All conversions working!")
    else:
        print("❌ Some conversions failed.")
    print("=" * 60)
    
    return all_passed


def show_category_units():
    """Display all units in each category."""
    print("\n" + "=" * 60)
    print("All Units by Category")
    print("=" * 60)
    
    for category in UnitCategory:
        units = get_category_units(category)
        print(f"\n{category.value.upper()} ({len(units)} units):")
        for unit in units:
            display_name = get_unit_display_name(unit)
            print(f"  • {unit} - {display_name}")
    
    print("=" * 60)


def main():
    """Run all tests."""
    print("\n🧪 Unit Converter - Duplicate Units Fix Test Suite\n")
    
    # Run tests
    test1 = test_no_duplicates()
    test2 = test_display_names()
    test3 = test_conversions()
    
    # Show all units
    show_category_units()
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"No Duplicates Test: {'✅ PASS' if test1 else '❌ FAIL'}")
    print(f"Display Names Test: {'✅ PASS' if test2 else '❌ FAIL'}")
    print(f"Conversions Test:   {'✅ PASS' if test3 else '❌ FAIL'}")
    print("=" * 60)
    
    if test1 and test2 and test3:
        print("\n🎉 All tests passed! The duplicate units fix is working correctly.\n")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please review the output above.\n")
        return 1


if __name__ == "__main__":
    exit(main())
