@echo off
REM Cleanup script for Unit Converter Pro (Windows)

echo Cleaning up Unit Converter Pro...

REM Remove Python cache files
echo Removing __pycache__ directories...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"

echo Removing .pyc files...
del /s /q *.pyc 2>nul

echo Removing .pyo files...
del /s /q *.pyo 2>nul

REM Remove egg-info directories
echo Removing .egg-info directories...
for /d /r . %%d in (*.egg-info) do @if exist "%%d" rd /s /q "%%d"

REM Remove pytest cache
echo Removing .pytest_cache...
for /d /r . %%d in (.pytest_cache) do @if exist "%%d" rd /s /q "%%d"

REM Remove coverage files
echo Removing coverage files...
if exist htmlcov rd /s /q htmlcov
if exist .coverage del /q .coverage

REM Remove build directories
echo Removing build directories...
if exist build rd /s /q build
if exist dist rd /s /q dist

REM Remove log files
echo Removing log files...
del /s /q *.log 2>nul

echo.
echo Cleanup complete!
echo.
echo Project is now clean and ready for:
echo   - Git commit
echo   - Deployment
echo   - Fresh installation
pause
