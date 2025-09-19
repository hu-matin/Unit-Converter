# Unit Converter

A simple Python program for converting common units of length, weight, and temperature.

## Supported Conversions

- Length: cm ↔️ inch, m ↔️ ft  
- Weight: kg ↔️ lb  
- Temperature: Celsius ↔️ Fahrenheit

## Usage

Run the script and call `convert(value, from_unit, to_unit)` method.

**Example:**
```python
from unit_converter import UnitConverter

converter = UnitConverter()
print(converter.convert(100, "cm", "inch"))  # 39.3701
```

## Project Structure

- `unit_converter.py`: main code  
- `README.md`: project description

## Downloade: 
```git
git clone https://github.com/your-username/unit-converter.git
cd unit-converter
python unit_converter.py
```

## License

MIT License

