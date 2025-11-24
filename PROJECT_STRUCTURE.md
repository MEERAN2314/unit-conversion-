# Unit Converter Pro - Project Structure

## 📁 Directory Layout

```
unit-converter-pro/
├── 📄 Core Configuration
│   ├── requirements.txt          # Python dependencies
│   ├── setup.py                  # Package installation config
│   ├── .gitignore               # Git ignore patterns
│   └── README.md                # Main documentation
│
├── 🚀 Deployment Files
│   ├── render.yaml              # Render deployment config
│   ├── Procfile                 # Process configuration
│   ├── runtime.txt              # Python version
│   ├── Dockerfile               # Docker container config
│   ├── .dockerignore            # Docker ignore patterns
│   └── DEPLOYMENT.md            # Deployment guide
│
├── 🧹 Utility Scripts
│   ├── clean.sh                 # Cleanup script (Linux/Mac)
│   └── clean.bat                # Cleanup script (Windows)
│
├── 📦 Core Library (unit_converter/)
│   ├── __init__.py              # Package initialization
│   ├── converter.py             # Main conversion logic (Pint-powered)
│   └── units.py                 # Unit definitions & categories
│
├── 🌐 Web Application (web_app/)
│   ├── app.py                   # FastAPI application
│   ├── templates/               # Jinja2 HTML templates
│   │   ├── base.html           # Base template
│   │   ├── index.html          # Main conversion page
│   │   ├── result.html         # Results display
│   │   └── about.html          # About page
│   └── static/                  # Static assets
│       ├── css/                # Stylesheets
│       └── js/                 # JavaScript files
│
├── 🧪 Tests (tests/)
│   ├── __init__.py
│   └── test_converter.py        # Unit tests
│
└── 📚 Documentation (documentation/)
    ├── API_DOCUMENTATION.md
    ├── DEPLOYMENT_GUIDE.md
    ├── IMPLEMENTATION_DETAILS.md
    ├── PROJECT_OVERVIEW.md
    ├── TECHNICAL_STACK.md
    └── TESTING_STRATEGY.md
```

## 🔑 Key Files Explained

### Core Configuration

**requirements.txt**
- Lists all Python dependencies
- Includes Pint 0.25.2 for unit conversions
- FastAPI, Uvicorn, Gunicorn for web server
- Development tools (pytest, black, flake8)

**setup.py**
- Package installation configuration
- Defines package metadata
- Specifies dependencies and extras

### Deployment Files

**render.yaml**
- Automatic deployment configuration for Render
- Defines build and start commands
- Sets environment variables

**Procfile**
- Process configuration for Heroku/Render
- Specifies how to run the web server

**Dockerfile**
- Container configuration for Docker deployment
- Multi-stage build for optimization
- Includes health checks

### Core Library

**unit_converter/converter.py**
- Main `UnitConverter` class
- Powered by Pint library
- Handles 4000+ unit conversions
- Expression parsing support
- Context-aware conversions

**unit_converter/units.py**
- Unit category definitions
- Pint registry initialization
- Category mapping for 20+ unit types
- Helper functions for unit lookup

### Web Application

**web_app/app.py**
- FastAPI application setup
- REST API endpoints
- Web interface routes
- Health check endpoint
- CORS configuration

**web_app/templates/**
- Jinja2 HTML templates
- Blue and white theme
- Responsive design
- Interactive forms

**web_app/static/**
- CSS stylesheets
- JavaScript for interactivity
- Images and icons

### Tests

**tests/test_converter.py**
- Comprehensive unit tests
- Tests for all conversion types
- Expression parsing tests
- Error handling validation

## 🚀 Quick Start Commands

### Installation
```bash
# Install package
pip install -e .

# Install with web dependencies
pip install -r requirements.txt
```

### Development
```bash
# Run web app
cd web_app
python app.py

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=unit_converter
```

### Cleanup
```bash
# Linux/Mac
chmod +x clean.sh
./clean.sh

# Windows
clean.bat
```

### Deployment
```bash
# Local with Gunicorn
cd web_app
gunicorn app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000

# Docker
docker build -t unit-converter-pro .
docker run -p 5000:5000 unit-converter-pro
```

## 📊 File Statistics

- **Total Python Files**: 6
- **Total Templates**: 4
- **Total Tests**: 1 file (15+ test cases)
- **Total Documentation**: 8 files
- **Lines of Code**: ~2,000+
- **Supported Units**: 4,000+
- **Unit Categories**: 20+

## 🔄 Development Workflow

1. **Make changes** to code
2. **Run tests**: `pytest tests/`
3. **Clean up**: `./clean.sh`
4. **Commit**: `git add . && git commit -m "message"`
5. **Push**: `git push origin main`
6. **Deploy**: Automatic via Render

## 🛠️ Maintenance

### Regular Tasks
- Run cleanup script before commits
- Update dependencies: `pip install --upgrade -r requirements.txt`
- Run tests: `pytest tests/ -v`
- Check code style: `black . && flake8`

### Adding New Features
1. Update `unit_converter/` for core logic
2. Update `web_app/app.py` for API endpoints
3. Update templates for UI changes
4. Add tests in `tests/`
5. Update documentation

## 📝 Notes

- All Python cache files are gitignored
- Static files are served by FastAPI
- Templates use Jinja2 syntax
- API documentation auto-generated at `/docs`
- Health check available at `/health`
