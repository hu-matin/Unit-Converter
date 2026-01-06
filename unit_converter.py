class UnitConverter:
    """A flexible unit converter using base unit system for dynamic conversions."""

    # Unit definitions with base units and conversion factors
    UNIT_DEFINITIONS = {
        "length": {
            "base": "m",
            "units": {
                "m": 1,
                "cm": 0.01,
                "mm": 0.001,
                "km": 1000,
                "inch": 0.0254,
                "ft": 0.3048,
                "yard": 0.9144,
                "mile": 1609.344,
            },
        },
        "weight": {
            "base": "kg",
            "units": {
                "kg": 1,
                "g": 0.001,
                "mg": 0.000001,
                "ton": 1000,
                "lb": 0.453592,
                "oz": 0.0283495,
            },
        },
        "volume": {
            "base": "liter",
            "units": {
                "liter": 1,
                "ml": 0.001,
                "gallon": 3.78541,
                "cup": 0.236588,
            },
        },
        "speed": {
            "base": "ms",  # meters per second
            "units": {
                "ms": 1,
                "kmh": 0.277778,
                "mph": 0.44704,
            },
        },
    }

    # Temperature requires special handling (not linear)
    TEMPERATURE_CONVERSIONS = {
        ("c", "f"): lambda c: (c * 9 / 5) + 32,
        ("f", "c"): lambda f: (f - 32) * 5 / 9,
        ("c", "k"): lambda c: c + 273.15,
        ("k", "c"): lambda k: k - 273.15,
        ("f", "k"): lambda f: (f - 32) * 5 / 9 + 273.15,
        ("k", "f"): lambda k: (k - 273.15) * 9 / 5 + 32,
    }

    def __init__(self):
        # Build lookup for unit -> category
        self._unit_to_category = {}
        for category, data in self.UNIT_DEFINITIONS.items():
            for unit in data["units"]:
                self._unit_to_category[unit] = category

        # Add temperature units
        for unit in ["c", "f", "k"]:
            self._unit_to_category[unit] = "temperature"

    def convert(self, value, from_unit, to_unit):
        """Convert a value from one unit to another."""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # Same unit, no conversion needed
        if from_unit == to_unit:
            return value

        # Check if units exist
        if from_unit not in self._unit_to_category:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self._unit_to_category:
            raise ValueError(f"Unknown unit: {to_unit}")

        # Check if units are compatible
        from_category = self._unit_to_category[from_unit]
        to_category = self._unit_to_category[to_unit]

        if from_category != to_category:
            raise ValueError(
                f"Cannot convert between {from_category} ({from_unit}) "
                f"and {to_category} ({to_unit})"
            )

        # Handle temperature specially
        if from_category == "temperature":
            return self._convert_temperature(value, from_unit, to_unit)

        # Linear conversion via base unit
        category_data = self.UNIT_DEFINITIONS[from_category]
        from_factor = category_data["units"][from_unit]
        to_factor = category_data["units"][to_unit]

        # Convert: value -> base unit -> target unit
        base_value = value * from_factor
        return base_value / to_factor

    def _convert_temperature(self, value, from_unit, to_unit):
        """Handle temperature conversions (non-linear)."""
        key = (from_unit, to_unit)
        if key in self.TEMPERATURE_CONVERSIONS:
            return self.TEMPERATURE_CONVERSIONS[key](value)
        raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported")

    def get_supported_units(self):
        """Return a dict of all supported units by category."""
        result = {}
        for category, data in self.UNIT_DEFINITIONS.items():
            result[category] = list(data["units"].keys())
        result["temperature"] = ["c", "f", "k"]
        return result


if __name__ == "__main__":
    converter = UnitConverter()

    # Length examples
    print(f"100 cm = {converter.convert(100, 'cm', 'inch'):.4f} inch")
    print(f"1 mile = {converter.convert(1, 'mile', 'km'):.4f} km")

    # Weight examples
    print(f"70 kg = {converter.convert(70, 'kg', 'lb'):.4f} lb")
    print(f"16 oz = {converter.convert(16, 'oz', 'lb'):.4f} lb")

    # Temperature examples
    print(f"100 C = {converter.convert(100, 'c', 'f'):.1f} F")
    print(f"0 C = {converter.convert(0, 'c', 'k'):.2f} K")

    # Volume examples
    print(f"1 gallon = {converter.convert(1, 'gallon', 'liter'):.4f} liters")

    # Speed examples
    print(f"100 km/h = {converter.convert(100, 'kmh', 'mph'):.4f} mph")
