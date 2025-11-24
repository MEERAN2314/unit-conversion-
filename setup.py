"""
Setup script for the Unit Conversion Library.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="unit-conversion-library",
    version="2.0.0",
    author="Developer",
    author_email="developer@example.com",
    description="Dynamic unit conversion library powered by Pint with 4000+ units support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pint==0.25.2",
    ],
    extras_require={
        "web": [
            "fastapi>=0.104.0",
            "uvicorn[standard]>=0.24.0",
            "jinja2>=3.1.0",
            "python-multipart>=0.0.6",
            "aiofiles>=23.0.0",
            "gunicorn>=21.2.0",
        ],
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "flake8>=4.0",
        ],
    },
)