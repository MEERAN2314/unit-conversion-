#!/bin/bash
# Cleanup script for Unit Converter Pro

echo "🧹 Cleaning up Unit Converter Pro..."

# Remove Python cache files
echo "Removing __pycache__ directories..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

echo "Removing .pyc files..."
find . -type f -name "*.pyc" -delete 2>/dev/null || true

echo "Removing .pyo files..."
find . -type f -name "*.pyo" -delete 2>/dev/null || true

# Remove egg-info directories
echo "Removing .egg-info directories..."
find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true

# Remove pytest cache
echo "Removing .pytest_cache..."
find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true

# Remove coverage files
echo "Removing coverage files..."
rm -rf htmlcov/ .coverage 2>/dev/null || true

# Remove build directories
echo "Removing build directories..."
rm -rf build/ dist/ 2>/dev/null || true

# Remove log files
echo "Removing log files..."
find . -type f -name "*.log" -delete 2>/dev/null || true

echo "✅ Cleanup complete!"
echo ""
echo "Project is now clean and ready for:"
echo "  - Git commit"
echo "  - Deployment"
echo "  - Fresh installation"
