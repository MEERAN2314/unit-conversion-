# Contributing to Unit Converter Pro

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## 🚀 Quick Start

```bash
# Clone the repository
git clone <your-repo-url>
cd unit-converter-pro

# Install dependencies
./manage.sh install

# Run development server
./manage.sh dev

# Run tests
./manage.sh test
```

## 📋 Development Workflow

### 1. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .

# Install development tools
pip install black flake8 pytest pytest-cov
```

### 2. Make Changes

- Create a new branch: `git checkout -b feature/your-feature-name`
- Make your changes
- Write tests for new functionality
- Ensure code follows style guidelines

### 3. Test Your Changes

```bash
# Run all tests
./manage.sh test

# Run quick tests
./manage.sh test-quick

# Format code
./manage.sh format

# Lint code
./manage.sh lint
```

### 4. Submit Pull Request

- Commit your changes: `git commit -m "Add feature: description"`
- Push to your fork: `git push origin feature/your-feature-name`
- Create a Pull Request on GitHub

## 🎨 Code Style

### Python Style Guide

- Follow PEP 8 guidelines
- Use Black for code formatting (line length: 100)
- Use type hints where appropriate
- Write docstrings for all functions and classes

Example:
```python
def convert_units(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a value from one unit to another.
    
    Args:
        value: The numeric value to convert
        from_unit: Source unit symbol
        to_unit: Target unit symbol
        
    Returns:
        Converted value
        
    Raises:
        ValueError: If units are invalid or incompatible
    """
    # Implementation here
    pass
```

### Commit Messages

Use clear, descriptive commit messages:
- `feat: Add new unit category for energy`
- `fix: Correct temperature conversion formula`
- `docs: Update API documentation`
- `test: Add tests for pressure conversions`
- `refactor: Simplify conversion logic`
- `style: Format code with black`

## 🧪 Testing Guidelines

### Writing Tests

- Place tests in the `tests/` directory
- Name test files as `test_*.py`
- Use descriptive test names: `test_length_conversion_mm_to_meters`
- Test edge cases and error conditions

Example:
```python
def test_temperature_conversion_celsius_to_fahrenheit(self):
    """Test Celsius to Fahrenheit conversion."""
    converter = UnitConverter()
    result = converter.convert(0, "degC", ["degF"])
    self.assertAlmostEqual(result.get_conversion("degF"), 32.0, places=1)
```

### Running Tests

```bash
# All tests with coverage
./manage.sh test

# Quick tests
./manage.sh test-quick

# Specific test file
python -m pytest tests/test_converter.py -v

# Specific test
python -m pytest tests/test_converter.py::TestUnitConverter::test_length_conversion -v
```

## 📚 Adding New Features

### Adding New Unit Categories

1. Update `unit_converter/units.py`:
   - Add new category to `UnitCategory` enum
   - Add units to `UNIT_CATEGORY_MAP`

2. Write tests in `tests/test_converter.py`

3. Update documentation in `README.md`

### Adding New API Endpoints

1. Add endpoint in `web_app/app.py`
2. Add Pydantic models if needed
3. Update API documentation
4. Write integration tests

### Adding New Templates

1. Create template in `web_app/templates/`
2. Follow existing blue/white theme
3. Ensure responsive design
4. Test on multiple devices

## 🐛 Bug Reports

When reporting bugs, include:
- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages/logs

## 💡 Feature Requests

When requesting features:
- Describe the use case
- Explain why it's useful
- Provide examples if possible
- Consider implementation complexity

## 📖 Documentation

- Update README.md for user-facing changes
- Update docstrings for code changes
- Add examples for new features
- Keep DEPLOYMENT.md current

## 🔍 Code Review Process

Pull requests will be reviewed for:
- Code quality and style
- Test coverage
- Documentation
- Performance impact
- Security considerations

## 🎯 Project Structure

```
unit-converter-pro/
├── unit_converter/          # Core library
│   ├── __init__.py
│   ├── converter.py         # Main conversion logic
│   └── units.py             # Unit definitions
├── web_app/                 # Web application
│   ├── app.py               # FastAPI application
│   ├── templates/           # Jinja2 templates
│   └── static/              # CSS, JS, images
├── tests/                   # Test suite
│   └── test_converter.py
├── documentation/           # Additional docs
├── requirements.txt         # Dependencies
├── setup.py                 # Package setup
├── Dockerfile               # Docker configuration
├── render.yaml              # Render deployment
└── manage.sh                # Management script
```

## 🤝 Community Guidelines

- Be respectful and inclusive
- Help others learn and grow
- Provide constructive feedback
- Follow the code of conduct

## 📞 Getting Help

- Open an issue for bugs or questions
- Check existing issues first
- Provide detailed information
- Be patient and respectful

## 🎉 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in documentation

Thank you for contributing to Unit Converter Pro! 🚀
