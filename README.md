# Unit Converter

A simple Python program for converting common units of length, weight, and temperature.

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

---

## Supported Units and Conversions

| From Unit  | To Unit    | Example                |
|------------|------------|------------------------|
| cm         | inch       | 100 cm → 39.3701 inch  |
| inch       | cm         | 10 inch → 25.4 cm      |
| m          | ft         | 5 m → 16.4042 ft       |
| ft         | m          | 10 ft → 3.048 m        |
| kg         | lb         | 70 kg → 154.324 lb     |
| lb         | kg         | 150 lb → 68.0389 kg    |
| c (Celsius)| f (Fahrenheit) | 100 c → 212 f       |
| f (Fahrenheit) | c (Celsius) | 32 f → 0 c          |


## Downloade: 
```git
git clone https://github.com/your-username/unit-converter.git
cd unit-converter
python unit_converter.py
```

## License

MIT License

