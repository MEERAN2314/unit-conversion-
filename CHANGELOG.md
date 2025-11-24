# Changelog

All notable changes to Unit Converter Pro will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024-11-25

### 🎉 Major Release - Pint Integration

This is a complete rewrite of the unit conversion engine using the Pint library for dynamic, extensible conversions.

### Added
- **Pint Integration**: 4000+ units with automatic dimensional analysis
- **Expression Parser**: Evaluate mathematical expressions like "5 meters + 3 feet"
- **20+ Unit Categories**: Energy, power, velocity, acceleration, and more
- **Advanced Temperature**: Support for Celsius, Fahrenheit, Kelvin, and Rankine
- **Context-Aware Conversions**: Specialized conversions for different domains
- **Health Check Endpoint**: `/health` for monitoring and deployment
- **Expression API**: `/api/expression` for evaluating unit expressions
- **Production Ready**: Gunicorn configuration for production deployment
- **Docker Support**: Complete Dockerfile and docker-compose setup
- **Render Deployment**: render.yaml for one-click deployment
- **Management Scripts**: manage.sh for common development tasks
- **Comprehensive Tests**: Updated test suite for Pint-based conversions

### Changed
- **Breaking**: Replaced static unit definitions with dynamic Pint registry
- **Breaking**: Temperature units now use Pint notation (degC, degF, K)
- **API Version**: Updated to v2.0.0
- **Conversion Logic**: Now uses Pint's dimensional analysis
- **Unit Info**: Returns dimensionality and category information
- **Error Handling**: Improved error messages with Pint exceptions

### Improved
- **Performance**: Optimized conversion caching
- **Scalability**: Support for custom unit definitions
- **Flexibility**: No hardcoded conversion factors
- **Accuracy**: Pint's precise conversion algorithms
- **Extensibility**: Easy to add new units and categories

### Fixed
- Temperature conversion edge cases
- Unit category detection
- API response consistency
- Documentation accuracy

### Deployment
- **Render**: One-click deployment with render.yaml
- **Docker**: Production-ready Dockerfile
- **Heroku**: Procfile for Heroku deployment
- **Railway**: Auto-detection support

### Documentation
- Updated README.md with new features
- Added DEPLOYMENT.md with detailed deployment guide
- Added CONTRIBUTING.md for contributors
- Added CHANGELOG.md (this file)
- Updated API documentation

### Dependencies
- Added: pint==0.25.2
- Added: gunicorn>=21.2.0
- Updated: FastAPI, Uvicorn to latest versions

## [1.0.0] - 2024-11-20

### Initial Release

### Added
- Basic unit conversion library
- Support for length, mass, temperature, pressure units
- FastAPI web application
- Beautiful blue and white theme
- REST API with Swagger documentation
- Responsive web interface
- Test suite with pytest
- Documentation

### Features
- 15+ units across 10 categories
- Manual conversion factors
- Temperature special handling
- Category-based unit grouping
- Web interface with examples
- API endpoints for conversions

---

## Version History

- **v2.0.0** - Pint integration, 4000+ units, production ready
- **v1.0.0** - Initial release with basic conversions

## Upgrade Guide

### From v1.0.0 to v2.0.0

#### Breaking Changes

1. **Temperature Unit Names**
   ```python
   # Old (v1.0.0)
   converter.convert(25, "DEG_C", ["DEG_F"])
   
   # New (v2.0.0)
   converter.convert(25, "degC", ["degF"])
   ```

2. **Unit Info Structure**
   ```python
   # Old (v1.0.0)
   unit_info.name  # Returns string
   unit_info.category  # Returns UnitCategory enum
   
   # New (v2.0.0)
   unit_info['name']  # Returns string
   unit_info['category']  # Returns string
   unit_info['dimensionality']  # New field
   ```

3. **Import Changes**
   ```python
   # Old (v1.0.0)
   from unit_converter import UnitConverter, Unit
   
   # New (v2.0.0)
   from unit_converter import UnitConverter, UNIT_REGISTRY
   ```

#### Migration Steps

1. Update requirements: `pip install -r requirements.txt`
2. Update temperature unit names in your code
3. Update unit info access patterns
4. Test your conversions
5. Deploy new version

#### New Features You Can Use

```python
# Expression parsing
result = converter.parse_expression("5 meters + 3 feet")

# Context-aware conversion
result = converter.convert_with_context(1, "m", "cm", context="spectroscopy")

# Access to 4000+ units
result = converter.convert(100, "km/h", ["m/s", "mph", "knot"])
```

## Future Roadmap

### v2.1.0 (Planned)
- [ ] Custom unit definitions via API
- [ ] Unit conversion history
- [ ] Batch conversion endpoint
- [ ] WebSocket support for real-time conversions
- [ ] User preferences and favorites

### v2.2.0 (Planned)
- [ ] Currency conversion support
- [ ] Historical exchange rates
- [ ] Conversion analytics
- [ ] Rate limiting
- [ ] Authentication system

### v3.0.0 (Future)
- [ ] Machine learning for unit detection
- [ ] Natural language processing
- [ ] Mobile app integration
- [ ] GraphQL API
- [ ] Multi-language support
