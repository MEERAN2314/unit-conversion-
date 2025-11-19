# API Documentation & Endpoints

## 🚀 API Overview

The Unit Converter Pro provides a comprehensive RESTful API built with FastAPI, featuring automatic documentation, type safety, and high performance. The API follows OpenAPI 3.0 standards and includes interactive documentation.

### Base URL
- **Development**: `http://localhost:5000`
- **Production**: `https://your-domain.com`

### API Features
- ✅ **Automatic Documentation**: Swagger UI and ReDoc
- ✅ **Type Safety**: Pydantic model validation
- ✅ **Error Handling**: Structured error responses
- ✅ **CORS Support**: Cross-origin resource sharing
- ✅ **High Performance**: Async operations
- ✅ **Standards Compliant**: OpenAPI 3.0 specification

## 📚 Interactive Documentation

### Swagger UI
- **URL**: `/docs`
- **Features**: Interactive API testing, request/response examples
- **Usage**: Test endpoints directly from the browser

### ReDoc
- **URL**: `/redoc`
- **Features**: Clean, readable documentation
- **Usage**: Reference documentation for developers

## 🔗 API Endpoints

### 1. Convert Units
Convert a value from one unit to other units with high precision.

```http
POST /api/convert
```

#### Request Body
```json
{
  "value": 205,
  "from_unit": "mm",
  "to_units": ["m", "cm", "in", "ft"]
}
```

#### Request Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `value` | `float` | ✅ | Numeric value to convert |
| `from_unit` | `string` | ✅ | Source unit symbol |
| `to_units` | `array[string]` | ❌ | Target units (optional) |

#### Response Schema
```json
{
  "success": true,
  "original_value": 205,
  "original_unit": "mm",
  "conversions": {
    "m": 0.205,
    "cm": 20.5,
    "in": 8.070866,
    "ft": 0.672572
  },
  "error": null
}
```

#### Response Fields
| Field | Type | Description |
|-------|------|-------------|
| `success` | `boolean` | Conversion success status |
| `original_value` | `float` | Original input value |
| `original_unit` | `string` | Original unit symbol |
| `conversions` | `object` | Converted values by unit |
| `error` | `string\|null` | Error message if failed |

#### Example Usage
```bash
curl -X POST "http://localhost:5000/api/convert" \
  -H "Content-Type: application/json" \
  -d '{
    "value": 205,
    "from_unit": "mm",
    "to_units": ["m", "cm", "in", "ft"]
  }'
```

#### Python Example
```python
import requests

response = requests.post("http://localhost:5000/api/convert", json={
    "value": 205,
    "from_unit": "mm",
    "to_units": ["m", "cm", "in", "ft"]
})

data = response.json()
print(f"205 mm = {data['conversions']['m']} meters")
```

#### JavaScript Example
```javascript
const response = await fetch('/api/convert', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        value: 205,
        from_unit: 'mm',
        to_units: ['m', 'cm', 'in', 'ft']
    })
});

const data = await response.json();
console.log(`205 mm = ${data.conversions.m} meters`);
```

### 2. Get All Units
Retrieve all available units organized by category.

```http
GET /api/units
```

#### Response Schema
```json
{
  "length": {
    "mm": {
      "name": "millimeter",
      "notes": ""
    },
    "cm": {
      "name": "centimeter", 
      "notes": ""
    },
    "m": {
      "name": "meter",
      "notes": ""
    }
  },
  "temperature": {
    "DEG_C": {
      "name": "degrees Celsius",
      "notes": ""
    },
    "DEG_F": {
      "name": "degrees Fahrenheit",
      "notes": ""
    }
  }
}
```

#### Example Usage
```bash
curl -X GET "http://localhost:5000/api/units"
```

### 3. Get Unit Categories
Retrieve all available unit categories.

```http
GET /api/categories
```

#### Response Schema
```json
[
  "length",
  "temperature",
  "pressure",
  "flow",
  "electrical_current",
  "acoustics",
  "velocity",
  "frequency",
  "electrical_resistance",
  "mass"
]
```

### 4. Get Units by Category
Retrieve units for a specific category.

```http
GET /api/units/{category}
```

#### Path Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `category` | `string` | Unit category name |

#### Example Request
```http
GET /api/units/length
```

#### Response Schema
```json
{
  "mm": {
    "name": "millimeter",
    "notes": ""
  },
  "cm": {
    "name": "centimeter",
    "notes": ""
  },
  "m": {
    "name": "meter",
    "notes": ""
  },
  "in": {
    "name": "inch",
    "notes": ""
  },
  "ft": {
    "name": "foot",
    "notes": ""
  }
}
```

### 5. Get Unit Information
Retrieve detailed information about a specific unit.

```http
GET /api/unit/{unit_symbol}
```

#### Path Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `unit_symbol` | `string` | Unit symbol (e.g., "mm", "DEG_C") |

#### Example Request
```http
GET /api/unit/mm
```

#### Response Schema
```json
{
  "name": "millimeter",
  "notes": ""
}
```

## ❌ Error Handling

### Error Response Format
```json
{
  "detail": "Error message describing what went wrong"
}
```

### HTTP Status Codes
| Code | Description | Example |
|------|-------------|---------|
| `200` | Success | Conversion completed |
| `400` | Bad Request | Invalid unit or incompatible categories |
| `404` | Not Found | Unit or category not found |
| `422` | Validation Error | Invalid request format |
| `500` | Server Error | Internal server error |

### Common Error Examples

#### Unknown Unit
```json
{
  "detail": "Unknown unit: xyz"
}
```

#### Incompatible Categories
```json
{
  "detail": "Cannot convert length to temperature"
}
```

#### Invalid Input Format
```json
{
  "detail": [
    {
      "loc": ["body", "value"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

## 🔧 API Client Examples

### Python Client Class
```python
import requests
from typing import List, Optional, Dict, Any

class UnitConverterClient:
    def __init__(self, base_url: str = "http://localhost:5000"):
        self.base_url = base_url
    
    def convert(self, value: float, from_unit: str, 
                to_units: Optional[List[str]] = None) -> Dict[str, Any]:
        """Convert units using the API."""
        response = requests.post(f"{self.base_url}/api/convert", json={
            "value": value,
            "from_unit": from_unit,
            "to_units": to_units
        })
        response.raise_for_status()
        return response.json()
    
    def get_units(self) -> Dict[str, Any]:
        """Get all available units."""
        response = requests.get(f"{self.base_url}/api/units")
        response.raise_for_status()
        return response.json()
    
    def get_categories(self) -> List[str]:
        """Get all unit categories."""
        response = requests.get(f"{self.base_url}/api/categories")
        response.raise_for_status()
        return response.json()

# Usage
client = UnitConverterClient()
result = client.convert(205, "mm", ["m", "cm", "in", "ft"])
print(result["conversions"])
```

### JavaScript Client Class
```javascript
class UnitConverterAPI {
    constructor(baseUrl = '') {
        this.baseUrl = baseUrl;
    }
    
    async convert(value, fromUnit, toUnits = null) {
        const response = await fetch(`${this.baseUrl}/api/convert`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                value: value,
                from_unit: fromUnit,
                to_units: toUnits
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    }
    
    async getUnits() {
        const response = await fetch(`${this.baseUrl}/api/units`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    }
    
    async getCategories() {
        const response = await fetch(`${this.baseUrl}/api/categories`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    }
}

// Usage
const api = new UnitConverterAPI();
const result = await api.convert(205, 'mm', ['m', 'cm', 'in', 'ft']);
console.log(result.conversions);
```

## 📊 Performance Characteristics

### Response Times
- **Simple Conversion**: < 10ms
- **Multiple Units**: < 50ms
- **Category Lookup**: < 5ms
- **Unit Information**: < 5ms

### Rate Limiting
- **Development**: No limits
- **Production**: 1000 requests/minute per IP

### Caching
- **Static Data**: 1 hour cache
- **Unit Definitions**: Cached in memory
- **API Responses**: No caching (real-time calculations)

## 🔒 Security Features

### Input Validation
- **Type Checking**: Pydantic model validation
- **Range Validation**: Reasonable numeric ranges
- **String Sanitization**: Safe string handling

### CORS Configuration
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

### Error Information
- **Development**: Detailed error messages
- **Production**: Sanitized error responses
- **Logging**: Comprehensive request logging

This API provides a robust, well-documented interface for unit conversion with modern web standards and best practices.