# Unit Converter Pro 🚀

A dynamic, professional-grade unit conversion library powered by **Pint** with 4000+ units support. Features a beautiful blue and white web interface built with Python, FastAPI, and modern web technologies.

![Unit Converter Pro](https://img.shields.io/badge/Unit%20Converter-Pro-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?style=flat-square&logo=fastapi)
![Pint](https://img.shields.io/badge/Pint-0.25.2-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

## ✨ What's New in v2.0

- 🎯 **Powered by Pint**: 4000+ units with automatic dimensional analysis
- 🧮 **Expression Parser**: Evaluate "5 meters + 3 feet" directly
- 🔄 **Dynamic Conversions**: No hardcoded conversion factors
- 🌡️ **Advanced Temperature**: Celsius, Fahrenheit, Kelvin, Rankine
- ⚡ **20+ Categories**: Length, mass, energy, power, velocity, and more
- 🚀 **Production Ready**: Optimized for Render deployment
- 📊 **Context-Aware**: Specialized conversions for different domains

## 🌟 Features

### Core Capabilities
- **🎯 4000+ Units**: Powered by Pint library with comprehensive unit support
- **🧮 Expression Parser**: Evaluate complex expressions like "5 meters + 3 feet"
- **🔄 Dynamic Conversions**: Automatic dimensional analysis, no hardcoded factors
- **📊 20+ Categories**: Length, mass, temperature, energy, power, velocity, and more
- **🌡️ Advanced Temperature**: Celsius, Fahrenheit, Kelvin, Rankine with proper formulas
- **⚡ Context-Aware**: Specialized conversions for different scientific domains

### Web Interface
- **🎨 Beautiful Blue & White Theme**: Professional, modern design with smooth animations
- **📱 Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **💾 Auto-save**: Form data persistence using localStorage
- **📋 Copy to Clipboard**: Easy copying of conversion results
- **🖨️ Print Support**: Professional formatting for printed output
- **⌨️ Keyboard Shortcuts**: Enhanced productivity with hotkeys

### API & Integration
- **🔗 RESTful API**: Full API with interactive Swagger documentation
- **⚡ High-Performance**: FastAPI backend with async support
- **🚀 Production Ready**: Optimized for Render, Heroku, Railway deployment
- **📚 Auto Documentation**: Swagger UI and ReDoc included
- **🔌 Easy Integration**: Python library or REST API

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd unit-conversion-library

# Install the library
pip install -e .

# Install web dependencies
pip install -e ".[web]"
```

### Running the Web Application

```bash
# Navigate to web app directory
cd web_app

# Start with uvicorn (recommended)
uvicorn app:app --host 0.0.0.0 --port 5000 --reload

# Or use the Python runner
python app.py
```

### Access Points

- **🌐 Web Interface**: http://localhost:5000
- **📚 Interactive API Docs**: http://localhost:5000/docs
- **📖 Alternative API Docs**: http://localhost:5000/redoc
- **ℹ️ About Page**: http://localhost:5000/about

## 📊 Supported Unit Categories (4000+ Units)

### Physical Quantities
- **Length**: mm, cm, m, km, in, ft, yd, mi, nm, μm
- **Mass**: g, kg, mg, lb, oz, ton, tonne
- **Temperature**: °C, °F, K, °R (Celsius, Fahrenheit, Kelvin, Rankine)
- **Time**: s, min, h, day, week, year
- **Area**: m², km², ft², acre, hectare
- **Volume**: L, mL, gal, qt, cup, fl_oz

### Energy & Power
- **Energy**: J, kJ, cal, kcal, Wh, kWh, BTU, eV
- **Power**: W, kW, MW, hp (horsepower)
- **Force**: N, kN, lbf (newton, pound-force)

### Motion & Mechanics
- **Velocity**: m/s, km/h, mph, ft/s, knot
- **Acceleration**: m/s², ft/s²
- **Pressure**: Pa, kPa, bar, psi, atm, mmHg, torr
- **Flow**: CFM, L/s, m³/s, gal/min

### Electrical
- **Current**: A, mA (ampere, milliampere)
- **Voltage**: V, kV (volt, kilovolt)
- **Resistance**: Ω, kΩ, MΩ (ohm, kiloohm, megaohm)
- **Capacitance**: F, μF, pF (farad, microfarad, picofarad)

### Other
- **Frequency**: Hz, kHz, MHz, GHz
- **Angle**: rad, deg (radian, degree)
- **Density**: kg/m³, g/cm³, lb/ft³
- **Acoustics**: dB (decibel)

**And 3900+ more units!** Pint supports SI, imperial, US customary, and specialized scientific units.

## 💻 Usage Examples

### Web Interface

1. **Basic Conversion**:
   - Enter value: `205`
   - Select from unit: `mm`
   - Choose target units or leave empty for all compatible
   - Click "Convert Units"

2. **Quick Examples**:
   - 205 mm → 0.205 m, 20.5 cm, 8.07 inches, 0.67 ft
   - 25°C → 77°F, 298.15 K
   - 100 km/h → 27.78 m/s, 62.14 mph
   - 1 kWh → 3,600,000 J, 860,421 cal

### Python Library

```python
from unit_converter import UnitConverter

# Initialize converter (powered by Pint)
converter = UnitConverter()

# Basic conversion
result = converter.convert(205, "mm", ["m", "cm", "in", "ft"])
print(f"205 mm = {result.get_conversion('m')} meters")
# Output: 205 mm = 0.205 meters

# Temperature conversion (all scales supported)
temp = converter.convert(25, "degC", ["degF", "K"])
print(f"25°C = {temp.get_conversion('degF')}°F")
# Output: 25°C = 77.0°F

# Auto-convert to all compatible units
result = converter.convert(1, "m")  # Converts to all length units

# Advanced: Expression parsing
result = converter.parse_expression("5 meters + 3 feet")
print(f"Result: {result['value']} {result['unit']}")
# Output: Result: 5.9144 meter

# Context-aware conversion
speed = converter.convert(100, "km/h", ["m/s", "mph"])
print(f"100 km/h = {speed.get_conversion('m/s'):.2f} m/s")
# Output: 100 km/h = 27.78 m/s

# Energy conversions
energy = converter.convert(1, "kWh", ["J", "cal", "BTU"])
print(f"1 kWh = {energy.get_conversion('J'):,.0f} joules")
# Output: 1 kWh = 3,600,000 joules
```

### API Usage

```bash
# Convert units via REST API
curl -X POST https://your-app.onrender.com/api/convert \
  -H "Content-Type: application/json" \
  -d '{
    "value": 205,
    "from_unit": "mm",
    "to_units": ["m", "cm", "in", "ft"]
  }'

# Response:
{
  "success": true,
  "original_value": 205,
  "original_unit": "mm",
  "conversions": {
    "m": 0.205,
    "cm": 20.5,
    "in": 8.070866,
    "ft": 0.672572
  }
}

# Evaluate expression
curl -X POST https://your-app.onrender.com/api/expression \
  -H "Content-Type: application/json" \
  -d '{"expression": "5 meters + 3 feet"}'

# Get all available units
curl https://your-app.onrender.com/api/units

# Health check
curl https://your-app.onrender.com/health
```

### JavaScript Integration

```javascript
// Fetch API example
async function convertUnits(value, fromUnit, toUnits) {
  const response = await fetch('https://your-app.onrender.com/api/convert', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ value, from_unit: fromUnit, to_units: toUnits })
  });
  return await response.json();
}

// Usage
const result = await convertUnits(205, 'mm', ['m', 'cm', 'in', 'ft']);
console.log(result.conversions);
// Output: { m: 0.205, cm: 20.5, in: 8.070866, ft: 0.672572 }

// Expression evaluation
async function evaluateExpression(expr) {
  const response = await fetch('https://your-app.onrender.com/api/expression', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ expression: expr })
  });
  return await response.json();
}

const result = await evaluateExpression('5 meters + 3 feet');
console.log(`${result.value} ${result.unit}`);
// Output: 5.9144 meter
```

## 🎨 Design Features

### Blue & White Theme
- **Primary Blue**: `#1e40af` - Professional, trustworthy
- **Secondary Blue**: `#3b82f6` - Modern, vibrant
- **Light Blue**: `#dbeafe` - Soft, elegant backgrounds
- **White**: `#ffffff` - Clean, minimalist

### Visual Elements
- **Gradient Backgrounds**: Smooth blue-to-white transitions
- **Card Shadows**: Subtle depth with blue-tinted shadows
- **Hover Effects**: Interactive elements with smooth animations
- **Loading States**: Professional loading indicators
- **Responsive Grid**: Adaptive layouts for all screen sizes

### Typography
- **Font**: Inter - Modern, readable sans-serif
- **Weights**: 300-700 for proper hierarchy
- **Colors**: Blue tones for headings, gray for body text

## 🛠️ Technical Architecture

### Backend
- **Python 3.7+**: Modern Python with type hints
- **FastAPI**: High-performance async web framework
- **Pydantic**: Data validation and serialization
- **Uvicorn**: ASGI server for production deployment

### Frontend
- **Bootstrap 5**: Responsive CSS framework
- **Jinja2**: Server-side templating
- **Vanilla JavaScript**: Enhanced interactivity
- **Font Awesome**: Professional icons
- **Custom CSS**: Blue and white theme implementation

### API Features
- **Automatic Documentation**: Swagger UI and ReDoc
- **Type Safety**: Request/response validation
- **CORS Support**: Cross-origin resource sharing
- **Error Handling**: Structured HTTP exceptions

## 🧪 Testing

```bash
# Run tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=unit_converter --cov-report=html

# Run specific test
python -m unittest tests.test_converter.TestUnitConverter.test_length_conversion_example
```

## 📦 Deployment

### Quick Deploy to Render (Recommended)

1. **Fork/Clone this repository**
2. **Push to GitHub**
3. **Go to [Render Dashboard](https://dashboard.render.com/)**
4. **Click "New" → "Blueprint"**
5. **Connect your repository**
6. **Click "Apply"** - Render auto-detects `render.yaml`
7. **Done!** Your app is live at `https://your-app.onrender.com`

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt
pip install -e .

# Run development server
cd web_app
python app.py

# Or with uvicorn
uvicorn app:app --reload --host 0.0.0.0 --port 5000
```

### Production with Docker
```bash
# Build image
docker build -t unit-converter-pro .

# Run container
docker run -p 5000:5000 unit-converter-pro

# Access at http://localhost:5000
```

### Production with Gunicorn
```bash
cd web_app
gunicorn app:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:5000
```

### Environment Variables
- `PORT` - Server port (default: 5000)
- `PYTHON_VERSION` - Python version (3.11.0)
- `DEBUG` - Debug mode (false in production)

## ⌨️ Keyboard Shortcuts

- **Ctrl/Cmd + Enter**: Submit conversion form
- **Escape**: Clear form and return to home
- **Ctrl/Cmd + /**: Focus on value input
- **Ctrl/Cmd + C**: Copy first result (on results page)
- **Ctrl/Cmd + P**: Print results

## 🎯 Requirements Compliance

✅ **All Requirements Met**:
- ✅ Multiple length units (mm, cm, m, in, ft)
- ✅ Takes value + base unit as input
- ✅ Converts to other relevant unit formats
- ✅ Returns clean and readable structure
- ✅ Main conversion function implemented
- ✅ Reference formula for conversions
- ✅ Proper error handling for invalid inputs
- ✅ Built as reusable library
- ✅ Modular, readable, and commented code
- ✅ Follows Python best practices
- ✅ Complete documentation with examples
- ✅ Comprehensive test cases
- ✅ Professional blue and white theme

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For support, please open an issue on GitHub or contact the development team.

---

**Unit Converter Pro** - Professional unit conversion with precision and style! 🎯