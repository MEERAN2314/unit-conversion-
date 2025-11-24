"""
FastAPI web application for the Unit Conversion Library.
Powered by Pint for dynamic unit conversions with 4000+ units.
"""

from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
import sys
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add parent directory to path to import unit_converter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unit_converter import UnitConverter, UnitCategory

# Initialize FastAPI app
app = FastAPI(
    title="Unit Converter Pro API",
    description="Dynamic unit conversion with 4000+ units powered by Pint library",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get the directory where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mount static files
static_path = os.path.join(BASE_DIR, "static")
if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")

# Initialize Jinja2 templates
templates_path = os.path.join(BASE_DIR, "templates")
templates = Jinja2Templates(directory=templates_path)

# Initialize the converter
converter = UnitConverter()

# Pydantic models for API
class ConversionRequest(BaseModel):
    value: float
    from_unit: str
    to_units: Optional[List[str]] = None

class ConversionResponse(BaseModel):
    success: bool
    original_value: float
    original_unit: str
    conversions: Dict[str, float]
    error: Optional[str] = None

class ExpressionRequest(BaseModel):
    expression: str

class UnitInfo(BaseModel):
    name: str
    dimensionality: str
    category: str
    notes: str

# Health check endpoint for Render
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy", "version": "2.0.0"}

# Helper function to get units by category
def get_all_units_by_category():
    """Get all units organized by category."""
    units_by_category = {}
    for category in UnitCategory:
        units = converter.get_supported_units(category)
        units_info = []
        for unit_symbol in units:
            try:
                unit_info = converter.get_unit_info(unit_symbol)
                units_info.append({
                    'symbol': unit_symbol,
                    'name': unit_info.get('name', unit_symbol),
                    'notes': unit_info.get('notes', '')
                })
            except Exception as e:
                logger.warning(f"Could not get info for unit {unit_symbol}: {e}")
                continue
        if units_info:  # Only add category if it has units
            units_by_category[category.value] = units_info
    return units_by_category

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Main page with conversion form."""
    units_by_category = get_all_units_by_category()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "units_by_category": units_by_category
    })

@app.post("/convert", response_class=HTMLResponse)
async def convert_form(
    request: Request,
    value: float = Form(...),
    from_unit: str = Form(...),
    to_units: List[str] = Form(default=[])
):
    """Handle conversion requests from web form."""
    try:
        if not from_unit:
            return RedirectResponse(url="/?error=Please select a source unit", status_code=303)
        
        if not to_units:
            to_units = None
        
        # Perform conversion
        result = converter.convert(value, from_unit, to_units)
        
        # Prepare results for template
        conversions = []
        for unit_symbol, converted_value in result.conversions.items():
            try:
                unit_info = converter.get_unit_info(unit_symbol)
                conversions.append({
                    'symbol': unit_symbol,
                    'name': unit_info.get('name', unit_symbol),
                    'value': converted_value,
                    'formatted_value': f"{converted_value:.6f}".rstrip('0').rstrip('.')
                })
            except Exception as e:
                logger.warning(f"Could not get info for {unit_symbol}: {e}")
                conversions.append({
                    'symbol': unit_symbol,
                    'name': unit_symbol,
                    'value': converted_value,
                    'formatted_value': f"{converted_value:.6f}".rstrip('0').rstrip('.')
                })
        
        # Sort conversions by unit name for consistent display
        conversions.sort(key=lambda x: x['name'])
        
        from_unit_info = converter.get_unit_info(from_unit)
        
        return templates.TemplateResponse("result.html", {
            "request": request,
            "original_value": value,
            "original_unit": from_unit,
            "original_unit_name": from_unit_info.get('name', from_unit),
            "conversions": conversions
        })
        
    except ValueError as e:
        return RedirectResponse(url=f"/?error={str(e)}", status_code=303)
    except Exception as e:
        return RedirectResponse(url=f"/?error=Unexpected error: {str(e)}", status_code=303)

@app.post("/api/convert", response_model=ConversionResponse)
async def api_convert(request: ConversionRequest):
    """
    Convert units programmatically.
    
    - **value**: The numeric value to convert
    - **from_unit**: Source unit symbol (e.g., 'mm', 'DEG_C')
    - **to_units**: Optional list of target unit symbols. If not provided, converts to all compatible units
    
    Returns conversion results with original value and all converted values.
    """
    try:
        result = converter.convert(request.value, request.from_unit, request.to_units)
        
        return ConversionResponse(
            success=True,
            original_value=request.value,
            original_unit=request.from_unit,
            conversions=result.conversions
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/units")
async def api_units():
    """
    Get all available units organized by category.
    
    Returns a dictionary where keys are category names and values are 
    dictionaries of unit symbols mapped to unit information.
    """
    units_by_category = {}
    for category in UnitCategory:
        units = converter.get_supported_units(category)
        units_info = {}
        for unit_symbol in units:
            try:
                unit_info = converter.get_unit_info(unit_symbol)
                units_info[unit_symbol] = {
                    'name': unit_info.get('name', unit_symbol),
                    'dimensionality': unit_info.get('dimensionality', ''),
                    'category': unit_info.get('category', category.value),
                    'notes': unit_info.get('notes', '')
                }
            except Exception as e:
                logger.warning(f"Could not get info for {unit_symbol}: {e}")
                continue
        if units_info:
            units_by_category[category.value] = units_info
    
    return units_by_category

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """About page with library information."""
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/api/categories")
async def get_categories():
    """Get all available unit categories."""
    return [category.value for category in UnitCategory]

@app.get("/api/units/{category}")
async def get_units_for_category(category: str):
    """Get units for a specific category."""
    try:
        category_enum = UnitCategory(category)
        units = converter.get_supported_units(category_enum)
        units_info = {}
        for unit_symbol in units:
            try:
                unit_info = converter.get_unit_info(unit_symbol)
                units_info[unit_symbol] = {
                    'name': unit_info.get('name', unit_symbol),
                    'dimensionality': unit_info.get('dimensionality', ''),
                    'category': unit_info.get('category', category),
                    'notes': unit_info.get('notes', '')
                }
            except Exception as e:
                logger.warning(f"Could not get info for {unit_symbol}: {e}")
                continue
        return units_info
    except ValueError:
        raise HTTPException(status_code=404, detail=f"Category '{category}' not found")

@app.get("/api/unit/{unit_symbol}")
async def get_unit_info_endpoint(unit_symbol: str):
    """Get detailed information about a specific unit."""
    try:
        unit_info = converter.get_unit_info(unit_symbol)
        return {
            'name': unit_info.get('name', unit_symbol),
            'dimensionality': unit_info.get('dimensionality', ''),
            'category': unit_info.get('category', 'other'),
            'notes': unit_info.get('notes', '')
        }
    except ValueError:
        raise HTTPException(status_code=404, detail=f"Unit '{unit_symbol}' not found")

@app.post("/api/expression")
async def evaluate_expression(request: ExpressionRequest):
    """
    Evaluate mathematical expressions with units.
    Example: "5 meters + 3 feet"
    """
    try:
        result = converter.parse_expression(request.expression)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=port,
        reload=False
    )