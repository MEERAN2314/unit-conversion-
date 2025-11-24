# Quick Start Guide 🚀

Get Unit Converter Pro running in 5 minutes!

## Prerequisites

- Python 3.11+ installed
- pip package manager
- Git (optional)

## Installation

### Option 1: Quick Install (Recommended)

```bash
# Clone or download the project
git clone <your-repo-url>
cd unit-converter-pro

# Make management script executable
chmod +x manage.sh

# Install everything
./manage.sh install

# Start development server
./manage.sh dev
```

Visit: http://localhost:5000

### Option 2: Manual Install

```bash
# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .

# Start server
cd web_app
python app.py
```

### Option 3: Docker

```bash
# Build and run
docker build -t unit-converter-pro .
docker run -p 5000:5000 unit-converter-pro
```

Visit: http://localhost:5000

## First Conversion

### Web Interface

1. Open http://localhost:5000
2. Enter value: `100`
3. Select from unit: `km/h`
4. Select target units: `m/s`, `mph`
5. Click "Convert Units"

Result: 100 km/h = 27.78 m/s = 62.14 mph

### Python Code

```python
from unit_converter import UnitConverter

converter = UnitConverter()
result = converter.convert(100, "km/h", ["m/s", "mph"])

print(f"100 km/h = {result.get_conversion('m/s'):.2f} m/s")
print(f"100 km/h = {result.get_conversion('mph'):.2f} mph")
```

### API Call

```bash
curl -X POST http://localhost:5000/api/convert \
  -H "Content-Type: application/json" \
  -d '{
    "value": 100,
    "from_unit": "km/h",
    "to_units": ["m/s", "mph"]
  }'
```

## Common Tasks

### Run Tests
```bash
./manage.sh test
```

### Clean Project
```bash
./manage.sh clean
```

### Format Code
```bash
./manage.sh format
```

### Check Deployment Readiness
```bash
./manage.sh deploy-check
```

## Examples

### Length Conversion
```python
result = converter.convert(205, "mm", ["m", "cm", "in", "ft"])
# 205 mm = 0.205 m = 20.5 cm = 8.07 in = 0.67 ft
```

### Temperature Conversion
```python
result = converter.convert(25, "degC", ["degF", "K"])
# 25°C = 77°F = 298.15 K
```

### Energy Conversion
```python
result = converter.convert(1, "kWh", ["J", "cal", "BTU"])
# 1 kWh = 3,600,000 J = 860,421 cal = 3,412 BTU
```

### Expression Evaluation
```python
result = converter.parse_expression("5 meters + 3 feet")
# Result: 5.9144 meter
```

## API Endpoints

- `GET /` - Web interface
- `GET /health` - Health check
- `GET /docs` - API documentation (Swagger)
- `GET /redoc` - API documentation (ReDoc)
- `POST /api/convert` - Convert units
- `POST /api/expression` - Evaluate expression
- `GET /api/units` - Get all units
- `GET /api/categories` - Get categories

## Troubleshooting

### Port Already in Use
```bash
# Change port
PORT=8000 python web_app/app.py
```

### Import Errors
```bash
# Reinstall package
pip install -e .
```

### Pint Not Found
```bash
# Install dependencies
pip install -r requirements.txt
```

### Tests Failing
```bash
# Clean and reinstall
./manage.sh clean
./manage.sh install
./manage.sh test
```

## Next Steps

1. **Explore the Web Interface**: Try different unit conversions
2. **Read the API Docs**: Visit http://localhost:5000/docs
3. **Check Examples**: See README.md for more examples
4. **Deploy**: Follow DEPLOYMENT.md to deploy to Render
5. **Contribute**: Read CONTRIBUTING.md to contribute

## Support

- **Documentation**: See README.md
- **Deployment**: See DEPLOYMENT.md
- **Contributing**: See CONTRIBUTING.md
- **Issues**: Open an issue on GitHub

## Quick Reference

### Management Commands
```bash
./manage.sh install       # Install dependencies
./manage.sh dev           # Start dev server
./manage.sh prod          # Start production server
./manage.sh test          # Run tests
./manage.sh clean         # Clean project
./manage.sh format        # Format code
./manage.sh lint          # Lint code
./manage.sh docker-build  # Build Docker image
./manage.sh deploy-check  # Check deployment readiness
```

### Python API
```python
from unit_converter import UnitConverter

converter = UnitConverter()

# Basic conversion
result = converter.convert(value, from_unit, [to_units])

# Expression parsing
result = converter.parse_expression("5 meters + 3 feet")

# Context conversion
result = converter.convert_with_context(value, from_unit, to_unit, context)

# Get supported units
units = converter.get_supported_units(category)

# Get unit info
info = converter.get_unit_info(unit_symbol)
```

### REST API
```bash
# Convert
curl -X POST http://localhost:5000/api/convert \
  -H "Content-Type: application/json" \
  -d '{"value": 100, "from_unit": "km/h", "to_units": ["m/s"]}'

# Expression
curl -X POST http://localhost:5000/api/expression \
  -H "Content-Type: application/json" \
  -d '{"expression": "5 meters + 3 feet"}'

# Get units
curl http://localhost:5000/api/units

# Health check
curl http://localhost:5000/health
```

Happy converting! 🎉
