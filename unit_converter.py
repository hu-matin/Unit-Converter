class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            "cm_to_inch": 0.393701,
            "inch_to_cm": 2.54,
            "m_to_ft": 3.28084,
            "ft_to_m": 0.3048,
            "kg_to_lb": 2.20462,
            "lb_to_kg": 0.453592,
            "c_to_f": lambda c: (c * 9/5) + 32,
            "f_to_c": lambda f: (f - 32) * 5/9,
        }

    def convert(self, value, from_unit, to_unit):
        key = f"{from_unit}_to_{to_unit}"
        if key in self.conversion_factors:
            factor = self.conversion_factors[key]
            if callable(factor):
                return factor(value)
            else:
                return value * factor
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported")


if __name__ == "__main__":
    converter = UnitConverter()
    print(converter.convert(100, "cm", "inch"))  # Example output: 39.3701
    print(converter.convert(212, "f", "c"))      # Example output: 100.0

