# Unit Converter

A flexible Python unit converter using a base unit system for dynamic conversions between length, weight, temperature, volume, and speed units.

## Installation

```bash
git clone https://github.com/hu-matin/Unit-Converter.git
cd Unit-Converter
python unit_converter.py
```

## Usage

```python
from unit_converter import UnitConverter

converter = UnitConverter()
print(converter.convert(100, "cm", "inch"))  # 39.3701
print(converter.convert(1, "mile", "km"))    # 1.609344
print(converter.convert(0, "c", "k"))        # 273.15
```

## Supported Units

### Length
| Unit | Symbol |
|------|--------|
| Meter | m |
| Centimeter | cm |
| Millimeter | mm |
| Kilometer | km |
| Inch | inch |
| Foot | ft |
| Yard | yard |
| Mile | mile |

### Weight
| Unit | Symbol |
|------|--------|
| Kilogram | kg |
| Gram | g |
| Milligram | mg |
| Ton | ton |
| Pound | lb |
| Ounce | oz |

### Temperature
| Unit | Symbol |
|------|--------|
| Celsius | c |
| Fahrenheit | f |
| Kelvin | k |

### Volume
| Unit | Symbol |
|------|--------|
| Liter | liter |
| Milliliter | ml |
| Gallon | gallon |
| Cup | cup |

### Speed
| Unit | Symbol |
|------|--------|
| Meters/second | ms |
| Kilometers/hour | kmh |
| Miles/hour | mph |

## Examples

```python
converter = UnitConverter()

# Length
converter.convert(100, "cm", "inch")   # 39.3701
converter.convert(1, "mile", "km")     # 1.609344

# Weight
converter.convert(70, "kg", "lb")      # 154.324
converter.convert(16, "oz", "lb")      # 1.0

# Temperature
converter.convert(100, "c", "f")       # 212.0
converter.convert(0, "c", "k")         # 273.15

# Volume
converter.convert(1, "gallon", "liter") # 3.78541

# Speed
converter.convert(100, "kmh", "mph")   # 62.1371
```

## License

MIT
