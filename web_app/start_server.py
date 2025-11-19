#!/usr/bin/env python3
"""
Startup script for Unit Converter Pro FastAPI Web App.
Handles installation and server startup.
"""

import os
import sys
import subprocess
import uvicorn

def install_unit_converter():
    """Install the unit_converter package in development mode."""
    try:
        # Try to import unit_converter
        import unit_converter
        print("✅ unit_converter package is already installed")
        return True
    except ImportError:
        print("📦 Installing unit_converter package...")
        try:
            # Install from parent directory
            parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", parent_dir])
            print("✅ unit_converter package installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install unit_converter package: {e}")
            return False

def main():
    """Main startup function."""
    print("🚀 Starting Unit Converter Pro...")
    
    # Install unit_converter if needed
    if not install_unit_converter():
        print("❌ Cannot start server without unit_converter package")
        sys.exit(1)
    
    # Get configuration from environment variables
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    reload = os.environ.get('DEBUG', 'True').lower() == 'true'
    
    print(f"🌐 Host: {host}")
    print(f"🔌 Port: {port}")
    print(f"🔄 Reload: {reload}")
    print(f"📱 Web Interface: http://{host}:{port}")
    print(f"📚 API Documentation: http://{host}:{port}/docs")
    print(f"📖 Alternative API Docs: http://{host}:{port}/redoc")
    print("=" * 50)
    
    # Start the server
    uvicorn.run(
        "app:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )

if __name__ == '__main__':
    main()